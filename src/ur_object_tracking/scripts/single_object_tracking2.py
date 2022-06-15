#!/usr/bin/python3

from rospy import Publisher
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CompressedImage, Image
from typing import Union
import rospy
import cv2
import numpy as np
import queue
from ur_vision_msgs.msg import *
from sensor_msgs.msg import CompressedImage, Image
from collections import OrderedDict
from scipy.optimize import linear_sum_assignment

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
    def __init__(self):

        self.bridge: CvBridge = CvBridge()

        self.num_lost = 0
        self.trackerName = 'kcf'
        self.tracker = OPENCV_OBJECT_TRACKERS[self.trackerName]()
        self.flag = False
        self.image_queue = OrderedDict()
        self.bb_queue = OrderedDict()
        self.num_detections = 0;
        self.frame_w = 410
        self.frame_h = 308
        self.cnt = 0
        self.skip = 0
        self.fail = 0
        self.image_publisher: Publisher = rospy.Publisher("track/image/compressed", CompressedImage,
                                                          queue_size=1)
        self.i = 0
        self.detections = []
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        self.out = cv2.VideoWriter('/home/ubuntu/Desktop/video3.mp4', fourcc, 30, (410, 308))

    def run(self):
        print("here")
        rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.__image_callback, queue_size=1,
                         buff_size=(3 * 8 * self.frame_w * self.frame_h + 500))
        rospy.Subscriber("/detect_objects/detection_array", DetectedObjectArray2D, self.__detection_callback,
                         queue_size=1)
        rospy.spin()

    def bbox2cv(self, bbox):
        '''
        Convert bounding box from ur_vison_msgs format to cv2 format
        :param bbox:
        :return:
        '''
        rect = (int(bbox.center.x - int(bbox.w / 2)), int(bbox.center.y - int(bbox.h / 2)), int(bbox.w), int(bbox.h))
        return rect

    def iou(self, boxA, boxB):
        '''
        Intersection over union
        :param boxA: first bounding box
        :param boxB: second bounding box
        :return:
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

        if self.cnt >= 100 and (len(msg.detected_objects) > 0):
            score_max=0
            idx=0
            for object in msg.detected_objects:
                if object.class_name == "person":
                    score = object.score
                    if score > score_max:
                        index = idx
                        score_max = score
                        bbox = self.bbox2cv(object.bbox)
                idx+=1

                self.tracker = OPENCV_OBJECT_TRACKERS[self.trackerName]()
                self.tracker.init(self.image_queue[seq + i], bbox)
                self.cnt=0
        self.cnt +=1
        self.skip += 1

    def __image_callback(self, msg):
        self.frame: np.ndarray = self.bridge.compressed_imgmsg_to_cv2(msg)
        self.image_queue[msg.header.seq] = self.frame

        if len(self.image_queue) > 100:
            self.image_queue.popitem(last=False)

        (success, self.box) = self.tracker.update(self.frame)
        if not success:
            #self.box =
            print("failed\n\n")
        box = list(self.box)
        for i in range(len(box)):
            box[i] = int(box[i])
            if box[i] < 0:
                box[i] = 0
        self.box = tuple(box)
        self.bb_queue[msg.header.seq] = self.box
        if len(self.bb_queue) > 100:
            self.bb_queue.popitem(last=False)
        (x, y, w, h) = [int(v) for v in self.box]
        cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        msg2: CompressedImage = self.bridge.cv2_to_compressed_imgmsg(self.frame)
        self.image_publisher.publish(msg2)
        self.out.write(self.frame)
        self.i += 1
        if self.i == 2000:
            self.out.release()
            print("exiting\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def main():
    print("started")
    rospy.init_node('ur_object_tracking', anonymous=False)
    tracking_node: TrackingNode = TrackingNode()
    tracking_node.run()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:

        pass
