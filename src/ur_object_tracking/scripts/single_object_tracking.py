#!/usr/bin/python3

from rospy import Publisher
from cv_bridge import CvBridge, CvBridgeError
import rospy
import cv2
import numpy as np
from ur_vision_msgs.msg import *
from sensor_msgs.msg import CompressedImage, Image
from collections import OrderedDict

OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,
    "tld": cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,
    "mosse": cv2.TrackerMOSSE_create
}


class TrackingNode:
    def __init__(self,
                 tracker_name: str,
                 camera_resolution: str,
                 fail_threshold: int,
                 IOU_threshold: float,
                 input_image_topic: str = '/raspicam_node/image/compressed',
                 input_BB_topic: str = '/detect_objects/detection_array',
                 output_image_topic: str = 'track/image/compressed',
                 output_BB_topic: str = 'track/BB',
                 output_video: str = ""
                 ):

        self.bridge: CvBridge = CvBridge()
        self.skip: int = 0
        self.fail: int = 0
        self.i: int = 0
        self.tracking: int = False
        self.image_queue: OrderedDict = OrderedDict()
        self.bb_queue: OrderedDict = OrderedDict()
        self.detections: list = []

        self.tracker_name: str = tracker_name
        print("using", tracker_name)

        try:
            self.tracker: cv2.Tracker = OPENCV_OBJECT_TRACKERS[self.tracker_name]()
        except ValueError:
            raise ValueError("Unsupported tracking algorithm: ", self.tracker_name)

        if len(camera_resolution.split('x')) == 2:
            w, h = camera_resolution.split('x')

            try:
                w: int = int(w)
                h: int = int(h)
            except ValueError:
                raise ValueError("Camera resolution error! Values can't be converted to integers. Width: ", w,
                                 " Height: ", h)

            if w < 0 or h < 0:
                raise ValueError("Camera resolution error! Got: width: ", w, " and height: ", h,
                                 " . Both values should be positive!")

            else:
                self.frame_w: int = w
                self.frame_h: int = h
        else:
            raise ValueError("Camera resolution error! Got: ", camera_resolution, " . But should be (width)x(height)")

        if fail_threshold < 0:
            raise ValueError("Wrong fail threshold! Got value: ", fail_threshold,
                             " . The value should be grater than 0 ")
        else:
            self.fail_threshold: int = fail_threshold

        if IOU_threshold < 0 or IOU_threshold > 1:
            raise ValueError("Wrong IOU threshold! Got value: ", IOU_threshold,
                             " . The value should be between 0 and 1")
        else:
            self.IOU_threshold: float = IOU_threshold

        if len(output_video) > 0:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            try:
                self.out = cv2.VideoWriter('output_video', fourcc, 30, (self.frame_w, self.frame_h))
            except FileNotFoundError:
                raise FileNotFoundError("output_video path not valid")

        self.image_publisher: Publisher = rospy.Publisher(output_image_topic, CompressedImage,
                                                          queue_size=1)
        self.BB_publisher: Publisher = rospy.Publisher(output_BB_topic, TrackedObject2D,
                                                       queue_size=1)
        self.input_image_topic: str = input_image_topic
        self.input_BB_topic: str = input_BB_topic

    def run(self):
        '''
        spin the subscribers
        '''
        rospy.Subscriber(self.input_image_topic, CompressedImage, self.__image_callback, queue_size=1,
                         buff_size=(3 * 8 * self.frame_w * self.frame_h + 500))
        rospy.Subscriber(self.input_BB_topic, DetectedObjectArray2D, self.__detection_callback,
                         queue_size=1)
        rospy.spin()

    def bbox2cv(self, bbox: BoundingBox2D):
        '''
        Convert bounding box from ur_vison_msgs BoundingBox2D format to cv2 format
        :param bbox: BoundingBox2D ur_vison_msgs bounding box format
        :return: tuple bounding box converted to the cv2 format
        '''
        rect = (int(bbox.center.x - int(bbox.w / 2)), int(bbox.center.y - int(bbox.h / 2)), int(bbox.w), int(bbox.h))
        return rect

    def cv2bbox(self, bbox):
        '''
        Convert bounding box from cv2 format to ur_vison_msgs BoundingBox2D format
        :param bbox: tuple bounding box in cv2 format
        :return: BoundingBox2D ur_vison_msgs bounding box format
        '''
        BB = BoundingBox2D()
        BB.center.x = bbox[0] + bbox[2] / 2
        BB.center.y = bbox[1] + bbox[3] / 2
        BB.w = bbox[2]
        BB.h = bbox[3]

        return BB

    def iou(self, boxA, boxB):
        '''
        Intersection over union
        :param boxA: tuple first bounding box
        :param boxB: tuple second bounding box
        :return: float intersection over union
        '''
        boxA = list(boxA)
        boxB = list(boxB)
        boxA[2] = boxA[0] + boxA[2]
        boxA[3] = boxA[1] + boxA[3]

        boxB[2] = boxB[0] + boxB[2]
        boxB[3] = boxB[1] + boxB[3]
        # determine the (x, y)-coordinates of the intersection rectangle
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])
        # compute the area of intersection rectangle
        interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
        # compute the area of both the prediction and ground-truth
        # rectangles
        boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
        boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area
        iou = interArea / float(boxAArea + boxBArea - interArea)
        # return the intersection over union value
        return iou

    def __detection_callback(self, msg):
        '''
        Callback function called on every detection. The function finds the closest tracking image to the detection image
        (tracking and detection might not use the SAME image, so the closest image is used in such cases), and initializes
        tracking on the detection bounding box. The bounding box with the highest score is used. The function also detects
        tracking failures by comparing them to detections. In it detects a failure it reinitializes tracking on the latest
        detection.
        '''

        #if self.skip > 2:
        if (len(msg.detected_objects) > 0):  # check if there are any detected objects
            self.fail = 0
            score_max = 0

            seq = msg.detected_objects[0].image_seq
            BB_overlap_flag = False
            BBs = []

            for i in range(100):  # find the closest tracking image_seq to the detection image_seq.
                if (seq + i) in self.image_queue:
                    for object in msg.detected_objects:  # find object of the relevant class with the highest score
                        if object.class_name == "person":
                            BBs.append(self.bbox2cv(object.bbox))
                            score = object.score
                            if score > score_max:
                                score_max = score
                                BB = self.bbox2cv(object.bbox)
                    if score_max > 0:
                        if self.tracking is False:
                            self.tracker.init(self.image_queue[seq + i], BB)
                            self.detection_bbox = BB
                            self.tracking = True
                        else:
                            for bbox in BBs:
                                if self.iou(self.bb_queue[seq + i], bbox) > self.IOU_threshold:
                                    BB_overlap_flag = True
                                    break
                    break

            if BB_overlap_flag == False:
                self.tracker = OPENCV_OBJECT_TRACKERS[self.tracker_name]()
                self.tracker.init(self.image_queue[seq + i], BB)
                self.detection_bbox = BB

        else:
            self.fail += 1
            if self.fail > self.fail_threshold:
                self.tracker = OPENCV_OBJECT_TRACKERS[self.tracker_name]()
                self.fail = 0
                self.tracking = False

        #self.skip += 1

    def __image_callback(self, msg):
        '''
        tracking callback function, called on every incoming camera frame.
        '''
        self.frame: np.ndarray = self.bridge.compressed_imgmsg_to_cv2(msg)
        self.image_queue[
            msg.header.seq] = self.frame  # append image to a list of images used for finding the closest match in detection

        if len(self.image_queue) > 100:  # fifo list of size 100
            self.image_queue.popitem(last=False)

        (success, self.box) = self.tracker.update(self.frame)  # update tracker

        # convert negative values of the bounding box to 0 for drawing the rectangle
        box = list(self.box)
        for i in range(len(box)):
            box[i] = int(box[i])
            if box[i] < 0:
                box[i] = 0
        self.box = tuple(box)

        self.bb_queue[msg.header.seq] = self.box  # append bounding box to list of bounding boxes

        if len(self.bb_queue) > 100:  # fifo list of size 100
            self.bb_queue.popitem(last=False)

        # draw bounding box on frame
        (x, y, w, h) = [int(v) for v in self.box]
        cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # publish the image
        msg2: CompressedImage = self.bridge.cv2_to_compressed_imgmsg(self.frame)
        self.image_publisher.publish(msg2)

        # publish the bounding box
        BB = TrackedObject2D()
        BB.bbox = self.cv2bbox(self.box)
        BB.tracking_ID = 1
        BB.class_name = "person"
        self.BB_publisher.publish(BB)

        # video recording
        if "self.out" in globals():
            self.out.write(self.frame)
            self.i += 1
            if self.i == 2000:
                self.out.release()
                print("exiting\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def main():
    print("started")
    rospy.init_node('ur_object_tracking', anonymous=False)

    tracker_name: str = rospy.get_param("~tracker_name")
    camera_resolution: str = rospy.get_param("~camera_resolution")
    fail_threshold: int = rospy.get_param("~fail_threshold")
    IOU_threshold: float = rospy.get_param("~IOU_threshold")
    input_image_topic: str = rospy.get_param("~input_image_topic")
    input_BB_topic: str = rospy.get_param("~input_BB_topic")
    output_image_topic: str = rospy.get_param("~output_image_topic")
    output_BB_topic: str = rospy.get_param("~output_BB_topic")
    output_video: str = rospy.get_param("~output_video")

    tracking_node: TrackingNode = TrackingNode(tracker_name,
                                               camera_resolution,
                                               fail_threshold,
                                               IOU_threshold,
                                               input_image_topic,
                                               input_BB_topic,
                                               output_image_topic,
                                               output_BB_topic,
                                               output_video)
    tracking_node.run()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:

        pass
