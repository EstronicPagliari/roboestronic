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
        self.kalman = cv2.KalmanFilter(8, 4)
        dt = 1/25
        self.kalman.measurementMatrix = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
        ])
        self.kalman.transitionMatrix = np.array([
            [1, 0, 0, 0, dt, 0, 0, 0],
            [0, 1, 0, 0, 0, dt, 0, 0],
            [0, 0, 1, 0, 0, 0, dt, 0],
            [0, 0, 0, 1, 0, 0, 0, dt],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
        ])

        self.kalman.processNoiseCov = np.identity(self.kalman.transitionMatrix.shape[0])
        self.kalman.processNoiseCov[0, 4] = 1
        self.kalman.processNoiseCov[4, 0] = 1
        self.kalman.processNoiseCov[1, 5] = 1
        self.kalman.processNoiseCov[5, 1] = 1
        self.kalman.processNoiseCov[2, 6] = 1
        self.kalman.processNoiseCov[6, 2] = 1
        self.kalman.processNoiseCov[3, 7] = 1
        self.kalman.processNoiseCov[7, 3] = 1
        self.bridge: CvBridge = CvBridge()

        self.num_lost=0
        self.trackers = cv2.MultiTracker_create()
        self.trackerName = 'medianflow'
        self.flag=False
        self.image_queue = OrderedDict()
        self.bb_queue = OrderedDict()
        self.num_detections=0;
        self.frame_w=410
        self.frame_h=308
        self.cnt=0
        self.image_publisher: Publisher = rospy.Publisher("track/image/compressed", CompressedImage,
                                                          queue_size=1)
        self.i=0
        self.detections=[]
        #fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        #self.out = cv2.VideoWriter('/home/ubuntu/Desktop/video1.mp4',fourcc,30,(410,308))

    def run(self):
        print("here")
        rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.__image_callback, queue_size=1,
                         buff_size=(3 * 8 * self.frame_w * self.frame_h + 500))
        rospy.Subscriber("/detect_objects/detection_array", DetectedObjectArray2D, self.__detection_callback, queue_size=1)
        rospy.spin()

    def bbox2cv(self, bbox):
        rect=( (bbox.center.x-int(bbox.w/2)), (bbox.center.y - int(bbox.h / 2)), bbox.w, bbox.h)
        return rect

    def iou(self, boxA, boxB):
        boxA=list(boxA)
        boxB = list(boxB)
        boxA[2]=boxA[0]+boxA[2]
        boxA[3] = boxA[1] + boxA[3]

        boxB[2]=boxB[0]+boxB[2]
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

    def reinitialize_tracking(self):
        self.trackers.clear()
        self.trackers = cv2.MultiTracker_create()
        self.cnt = 0
        self.num_detections = 0
        if len(self.detections) > self.num_detections:
            i=0
            while int(self.detections[0].image_seq)+i not in self.image_queue:
                i += 1
            frame = self.image_queue[int(self.detections[0].image_seq)+i]
            for i in range( len(self.detections) - self.num_detections):
                tracker = OPENCV_OBJECT_TRACKERS[self.trackerName]()
                print(self.bbox2cv(self.detections[self.num_detections+i].bbox))
                self.trackers.add(tracker, frame, self.bbox2cv(self.detections[self.num_detections+i].bbox))
            self.num_detections = len(self.detections)
            print(self.num_detections)

    def __detection_callback(self, msg):
        old_detections=self.detections
        self.detections = msg.detected_objects
        self.cnt=self.cnt+1
        g={}
        if self.detections:
            seq = self.detections[0].image_seq
        if self.detections and old_detections:
            print(len(old_detections))
            print(len(self.detections))
            cost = np.empty((len(self.detections), len(old_detections)))
            i = 0
            for detection in self.detections:
                j=0
                for old_detection in old_detections:
                    cost[i,j]=self.iou(self.bbox2cv(detection.bbox),self.bbox2cv(old_detection.bbox))
                    j+=1
                i += 1
            assign=linear_sum_assignment(cost)
            self.detections=list(np.array(self.detections)[assign[0]])


            bb_keys=list(self.bb_queue.keys())
            for i in range(20):
                if seq+i in bb_keys:
                    seq+=i
                    break
            print("bbq ", self.bb_queue)
            bbs = self.bb_queue[int(seq)]
            i=0
            cost = np.empty((len(self.detections), len(old_detections)))
            for bb in bbs:
                j=0
                for detection in self.detections:
                    cost[i, j] = self.iou(self.bbox2cv(bb), self.bbox2cv(detection.bbox))
                    j+=1
                i+=1
            assign = linear_sum_assignment(cost)
            print("assign ",assign[0])
            print("bbs ", bbs)
            bbs = list(np.array(bbs)[assign[0]])
            for i in range(len(bbs)):
                if self.iou(self.bbox2cv(bbs[i]), self.bbox2cv(self.detections[i].bbox)) < 0.4:
                    #self.reinitialize_tracking()
                    print("reint")


        if self.cnt>100:
            self.reinitialize_tracking()


        if len(self.detections) > self.num_detections:
            for key,val in self.image_queue.items():
                print(key)
            print("seq: ",seq)
            frame = self.image_queue[int(seq)]
            for i in range( len(self.detections) - self.num_detections):
                tracker = OPENCV_OBJECT_TRACKERS[self.trackerName]()
                print(self.bbox2cv(self.detections[self.num_detections+i].bbox))
                self.trackers.add(tracker, frame, self.bbox2cv(self.detections[self.num_detections+i].bbox))
            self.num_detections = len(self.detections)
            print(self.num_detections)



    def __image_callback(self, msg):
        self.frame: np.ndarray = self.bridge.compressed_imgmsg_to_cv2(msg)
        self.image_queue[msg.header.seq] = self.frame

        if len(self.image_queue)>20:
            self.image_queue.popitem(last=False)

        (self.success, self.boxes) = self.trackers.update(self.frame)
        if self.success is False:
            self.num_lost+=1
        else:
            self.num_lost = 0
        if self.num_lost>1:
            self.reinitialize_tracking()
        #print(self.success)
        for box in self.boxes:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        msg2: CompressedImage = self.bridge.cv2_to_compressed_imgmsg(self.frame)
        self.image_publisher.publish(msg2)

        self.bb_queue[msg.header.seq]=self.boxes
        if len(self.bb_queue)>20:
            self.bb_queue.popitem(last=False)
        #self.out.write(self.frame)
        #self.i+=1
        #if self.i==2000:
        #    self.out.release()
        #    print("exiting")

        '''
        if self.flag is False:
            self.tracker.init(init_frame, state_to_bbox(self.state))
            self.flag = True
        self.kalman.correct(msg)
        '''

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
