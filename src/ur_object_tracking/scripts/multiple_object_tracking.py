#!/usr/bin/python3

from rospy import Publisher
from cv_bridge import CvBridge, CvBridgeError
import rospy
import cv2
import numpy as np
from ur_vision_msgs.msg import *
from sensor_msgs.msg import CompressedImage, Image, CameraInfo
from collections import OrderedDict
import time
from sort import *

class TrackingNode:
    def __init__(self,
                 iou_threshold: float,
                 input_image_info_topic: str = '/raspicam_node/camera_info',
                 input_image_topic: str = '/raspicam_node/image/compressed',
                 input_BB_topic: str = '/detect_objects/detection_array',
                 output_image_topic: str = 'track/image/compressed',
                 output_BB_topic: str = 'track/BB',
                 min_detection_area: int = 500,
                 untracked_perserverance: int = 10,
                 min_detection_hits: int = 3,
                 max_untracked_age: int = 10,
                 aspect_ratio: float = 1,
                 ):

        self.bridge: CvBridge = CvBridge()

        if iou_threshold < 0 or iou_threshold > 1:
            raise ValueError("Wrong IOU threshold! Got value: ", iou_threshold,
                             " . The value should be between 0 and 1")

        if min_detection_area < 1:
            raise ValueError("Wrong min detection area! Got value: ", min_detection_area,
                             " . The value should be higher than 0")
        else:
            self.min_detection_area = min_detection_area

        if untracked_perserverance < 0:
            raise ValueError("Wrong untracked perseverance! Gor value: ", untracked_perserverance, " . The value should be 0 or higher. ")

        if min_detection_hits < 0:
            raise ValueError("Wrong min detection hits! Gor value: ", min_detection_hits, " . The value should be 0 or higher. ")

        if max_untracked_age < 0:
            raise ValueError("Wrong max untracked age! Gor value: ", max_untracked_age, " . The value should be 0 or higher. ")




        self.image_publisher: Publisher = rospy.Publisher(output_image_topic, CompressedImage,
                                                          queue_size=1)
        self.BB_publisher: Publisher = rospy.Publisher(output_BB_topic, TrackedObjectArray2D,
                                                       queue_size=1)
        self.input_image_topic: str = input_image_topic
        self.input_BB_topic: str = input_BB_topic
        self.input_image_info_topic: str = input_image_info_topic
        self.tracker2: Sort = Sort(max_age=max_untracked_age, min_hits=min_detection_hits, iou_threshold=iou_threshold,
                                   untracked_perserverance=untracked_perserverance)

        self.got_info: bool = False
        self.colors: dict = {}
        self.aspect_ratio: float = aspect_ratio

        self.tracked_BBs: np.array = np.zeros(2)


    def run(self):
        '''
        spin the subscribers
        '''
        rospy.Subscriber(self.input_image_info_topic, CameraInfo, self.__info_callback,
                         queue_size=1)
        time_wating = time.time()

        print("waiting for camera info")

        while self.got_info is False and time.time() - time_wating < 20:
            time.sleep(0.1)

        print("got camera info")
        if self.got_info is True:
            rospy.Subscriber(self.input_image_topic, CompressedImage, self.__image_callback, queue_size=1,
                             buff_size=(3 * 8 * self.frame_w * self.frame_h + 500))
            rospy.Subscriber(self.input_BB_topic, DetectedObjectArray2D, self.__detection_callback,
                             queue_size=1)
        rospy.spin()

    def __info_callback(self, msg: CameraInfo):
        if (msg.height > 0 and msg.width > 0 and self.got_info is False):
            self.frame_w: int = msg.width
            self.frame_h: int = msg.height
            self.got_info = True

    def track2bbox(self, bbox: np.array) -> BoundingBox2D:
        '''
        Convert bounding box from cv2 format to ur_vison_msgs BoundingBox2D format
        :param bbox: tuple bounding box in cv2 format
        :return: BoundingBox2D ur_vison_msgs bounding box format
        '''
        bb: BouningBox2D = BoundingBox2D()
        bb.center.x = (bbox[0] + bbox[2]) / 2
        bb.center.y = (bbox[1] + bbox[3]) / 2
        bb.w = bbox[2]-bbox[0]
        bb.h = bbox[3]-bbox[1]

        return bb

    def __detection_callback(self, msg):
        '''
        Callback function called on every detection. The function finds the closest tracking image to the detection image
        (tracking and detection might not use the SAME image, so the closest image is used in such cases), and initializes
        tracking on the detection bounding box. The bounding box with the highest score is used. The function also detects
        tracking failures by comparing them to detections. In it detects a failure it reinitializes tracking on the latest
        detection.
        '''

        detections = np.empty((0, 5))

        if (len(msg.detected_objects) > 0):  # check if there are any detected objects
            score_max = 0

            for object in msg.detected_objects:
                x1 = round(object.bbox.center.x-object.bbox.w/2)
                x2 = round(object.bbox.center.x + object.bbox.w / 2)
                y1 = round(object.bbox.center.y-object.bbox.h/2)
                y2 = round(object.bbox.center.y + object.bbox.h / 2)
                score=object.score
                if ( object.bbox.w * object.bbox.h > self.min_detection_area) and (object.bbox.w / object.bbox.h < self.aspect_ratio):
                    detection=np.array([x1,y1,x2,y2,score])
                    detections=np.vstack((detections,detection))
        self.tracked_BBs = self.tracker2.update(detections)
        # print("+++++++++++++++",self.tracked_BBs)
        for track in self.tracked_BBs:
            if sum(track) <= 0:
                continue
            if track[0] < 0:
                track[0] = 0
            if track[0] > self.frame_w:
                track[0] = self.frame_w
            if track[2] < 0:
                track[2] = 0
            if track[2] > self.frame_w:
                track[2] = self.frame_w
            if track[1] < 0:
                track[1] = 0
            if track[1] > self.frame_h:
                track[1] = self.frame_h
            if track[3] < 0:
                track[3] = 0
            if track[3] > self.frame_h:
                track[3] = self.frame_h

    def __image_callback(self, msg):
        '''
        tracking callback function, called on every incoming camera frame.
        '''
        self.frame: np.ndarray = self.bridge.compressed_imgmsg_to_cv2(msg)
        
        BBs = TrackedObjectArray2D()

        if self.tracked_BBs.any():
            for tracked_BB in self.tracked_BBs:
                BB = TrackedObject2D()
                BB.bbox = self.track2bbox(tracked_BB)
                BB.tracking_ID = int(tracked_BB[4])
                BB.class_name = "person"
                BBs.tracked_objects.append(BB)
                if str(tracked_BB[4]) not in self.colors:
                    self.colors[str(tracked_BB[4])] = list(np.random.random(size=3) * 256)
                #print(bb[0],bb[1],bb[2],bb[3])
                cv2.rectangle(self.frame,
                              (int(tracked_BB[0]), int(tracked_BB[1])),
                              (int(tracked_BB[2]), int(tracked_BB[3])),
                              self.colors[str(tracked_BB[4])],
                              2)
                cv2.putText(self.frame,
                            str(int(tracked_BB[4])),
                            (int(tracked_BB[0])+20, int(tracked_BB[1])+20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            self.colors[str(tracked_BB[4])],
                            2)

        self.BB_publisher.publish(BBs)
        # publish the image
        msg2: CompressedImage = self.bridge.cv2_to_compressed_imgmsg(self.frame)
        self.image_publisher.publish(msg2)



def main():
    print("started")
    rospy.init_node('ur_object_tracking', anonymous=False)

    input_image_info_topic: str = rospy.get_param("~input_image_info_topic")
    iou_threshold: float = rospy.get_param("~iou_threshold")
    input_image_topic: str = rospy.get_param("~input_image_topic")
    input_BB_topic: str = rospy.get_param("~input_BB_topic")
    output_image_topic: str = rospy.get_param("~output_image_topic")
    output_BB_topic: str = rospy.get_param("~output_BB_topic")
    min_detection_area: int = rospy.get_param("~min_detection_area")
    untracked_perseverance: int = rospy.get_param("~untracked_perseverance")
    min_detection_hits: int = rospy.get_param("~min_detection_hits")
    max_untracked_age: int = rospy.get_param("~max_untracked_age")
    aspect_ratio: float = rospy.get_param("~aspect_ratio")

    tracking_node: TrackingNode = TrackingNode(iou_threshold,
                                               input_image_info_topic,
                                               input_image_topic,
                                               input_BB_topic,
                                               output_image_topic,
                                               output_BB_topic,
                                               min_detection_area,
                                               untracked_perseverance,
                                               min_detection_hits,
                                               max_untracked_age,
                                               aspect_ratio)
    tracking_node.run()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:

        pass
