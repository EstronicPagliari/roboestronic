#!/usr/bin/python3
import following.msg
import time
import actionlib
from geometry_msgs.msg import Twist
import numpy as np
from sensor_msgs.msg import CameraInfo
from ur_vision_msgs.msg import *
from following.utils import *
import rospy
import queue


class FollowAction(object):
    # create messages that are used to publish feedback/result
    _feedback = following.msg.FollowFeedback()
    _result = following.msg.FollowResult()

    def __init__(self,
                 name,
                 input_image_info_topic: str = '/raspicam_node/camera_info',
                 angular_pid: list = [0.3, 0, 0],
                 max_speed: float = 0.4,
                 acceleration_step: float = 0.05,
                 deceleration_step: float = 0.15,
                 max_time_without_object: float = 7,
                 max_time_stopped: float = 1,
                 angular_speed_coefficient: float = 0.05,
                 iou: float = 0.3
                 ):

        try:
            angular_pid = angular_pid.split(',')
            kp: float = float(angular_pid[0])
            ki: float = float(angular_pid[1])
            kd: float = float(angular_pid[2])
            self.angular_pid: PID = PID(kp, ki, kd)
        except ValueError:
            raise ValueError("angular PID parameter error! Got: ", angular_pid, " . But should be [kp, ki, kd]")


        if max_speed <= 0:
            raise ValueError("Got max speed: ", deceleration_pid, " . But should be greater then 0")
        else:
            self.max_speed: float = max_speed

        if acceleration_step <= 0:
            raise ValueError("Got acceleration_step ", acceleration_step, " . But should be greater then 0")
        else:
            self.acceleration_step: float = acceleration_step

        if deceleration_step <= 0:
            raise ValueError("Got deceleration_step ", deceleration_step, " . But should be greater then 0")
        else:
            self.deceleration_step: float = deceleration_step

        if max_time_without_object < 0:
            raise ValueError("Got max_time_without_object ", max_time_without_object, " . But should be greater or equal to 0")
        else:
            self.max_time_without_object: float =  max_time_without_object

        if max_time_stopped < 0:
            raise ValueError("Got max_time_stopped ", max_time_stopped, " . But should be greater or equal to 0")
        else:
            self.max_time_stopped: float =  max_time_stopped

        if angular_speed_coefficient <= 0:
            raise ValueError("Got angular_speed_coefficient: ", angular_speed_coefficient, " . But should be greater than 0")
        else:
            self.angular_speed_coefficient: float = angular_speed_coefficient

        if iou < 0 or iou > 1:
            raise ValueError("Got iou: ", iou, " . But should be between 0 an 1")
        else:
            self.iou_threshold : float = iou

        self.input_image_info_topic = input_image_info_topic

        # Motor command publisher
        self.cmdPub: Publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

        # Collision detection and speed setting
        self.sonar_collision: SonarCollision = SonarCollision()

        # Action Lib
        self._action_name: str = name
        self._as = actionlib.SimpleActionServer(self._action_name, following.msg.FollowAction,
                                                execute_cb=self.execute_cb, auto_start=False)
        self._as.start()

        # Internal variables
        self.got_info: bool = False
        self.initialize: bool = False
        self.twist: Twist = Twist()
        self.time_with_no_id: float = time.time()
        self.bbox: BoundingBox2D = BoundingBox2D()

        self.followed_object: TrackedObject2D = TrackedObject2D()
    def iou(self, boxA: BoundingBox2D, boxB: BoundingBox2D) -> float:
        '''
        Intersection over union
        :param1 BoundingBox2D: first bounding box
        :param2 BoundingBox2D: second bounding box
        :return float: intersection over union
        '''
        BoxA = []
        BoxB = []
        BoxA.append(boxA.center.x - boxA.w / 2)
        BoxA.append(boxA.center.y - boxA.h / 2)
        BoxA.append(boxA.center.x + boxA.w / 2)
        BoxA.append(boxA.center.x + boxA.h / 2)

        BoxB.append(boxB.center.x - boxB.w / 2)
        BoxB.append(boxB.center.y - boxB.h / 2)
        BoxB.append(boxB.center.x + boxB.w / 2)
        BoxB.append(boxB.center.x + boxB.h / 2)

        boxA=BoxA
        boxB=BoxB
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
    
    def __bbox_callback(self, msg: TrackedObjectArray2D):
        '''
        Handles which bounding box to track
        :param msg TrackedObjectArray2D: array of tracked objects
        '''

        initialize: bool = True
        closest2center: float = self.frame_w
        success: bool = False
        
        # check if current object we track is among tracked objects
        for tracked_object in msg.tracked_objects:
            if tracked_object.tracking_ID > 0:
                if self.followed_object.tracking_ID == tracked_object.tracking_ID:
                    self.bbox = tracked_object.bbox
                    self.followed_object = tracked_object
                    self.time_with_no_id = time.time()
                    success = True
                    break

        if success is False:
            for tracked_object in msg.tracked_objects:
                if tracked_object.tracking_ID > 0:
                    if time.time()-self.time_with_no_id  < 2 and self.iou(self.followed_object.bbox, tracked_object.bbox) > self.iou_threshold:
                        success = True
                        self.bbox: BoundingBox2D = tracked_object.bbox
                        self.followed_object = tracked_object
                        if tracked_object.bbox.center.x > 0 and tracked_object.bbox.center.y > 0:
                            self.time_with_no_id = time.time()
                    elif time.time()-self.time_with_no_id >= 2 and abs(tracked_object.bbox.center.x - self.frame_center_x) < closest2center and self.initialize is True:
                        success = True
                        closest2center = abs(tracked_object.bbox.center.x - self.frame_center_x)
                        self.followed_object = tracked_object
                        self.bbox: BoundingBox2D = tracked_object.bbox
                        initialize = False
                    if initialize is False and self.initialize is True:
                        self.initialize = False

        if success is False:
            #print("no success")
            self.bbox: BoundingBox2D = BoundingBox2D()
        else:
            self.time_with_no_id = time.time()
        self._feedback.progress = str(self.followed_object.tracking_ID)

    def __info_callback(self, msg: CameraInfo):
        '''
        gets camera info
        :param msg CameraInfo: camera info
        :return:
        '''

        if (msg.height > 0 and msg.width > 0 and self.got_info is False):
            self.frame_w: int = msg.width
            self.frame_h: int = msg.height
            print(self.frame_w,self.frame_h)
            self.frame_center_x: float = self.frame_w / 2
            self.frame_center_y: float = self.frame_h / 2
            self.frame: np.ndarray = np.zeros((self.frame_w, self.frame_h))
            self.got_info = True



    def execute_cb(self, goal):
        '''
        Follows a set object once receiving a follow command
        :param goal: goal to follow
        :return:
        '''

        if goal.task == "Follow":
            self.initialize = True
            rospy.Subscriber(self.input_image_info_topic, CameraInfo,
                             self.__info_callback,
                             queue_size=1)

            time_wating = time.time()
            print("waiting for camera info")

            # wait for camera info
            while self.got_info is False:
                if time.time() - time_wating < 20:
                    time.sleep(0.1)
                else:
                    self._result.state = "No camera info"
                    rospy.loginfo(
                        '%s: Aborted: No camera info' % self._action_name)
                    self._as.set_aborted(self._result)

            print("got camera info")

            if self.got_info is True:
                rospy.Subscriber("/track/BB", TrackedObjectArray2D,
                                 self.__bbox_callback,
                                 queue_size=1)

                self.sonar_collision.run_sonars()
                r = rospy.Rate(20)

                # variable initialization
                twist: Twist = Twist()
                time_since_last_object: float = time.time()
                time_old: float = time.time()
                speed: float = 0
                angular_speed: float = 0
                object_center: float = self.frame_center_x + self.frame_center_x/4
                time_stopped: float = time.time()
                self._feedback.progress = "None"

                while not rospy.is_shutdown():
                    d_time: float = time.time() - time_old

                    # check if action was canceled by the server
                    if self._as.is_preempt_requested():
                        rospy.loginfo('%s: Preempted' % self._action_name)
                        self._as.set_preempted()
                        break

                    # check if the tracked object is in frame
                    if (self.bbox.center.x > 0 and self.bbox.center.x < self.frame_w and self.bbox.center.y > 0 and self.bbox.center.y < self.frame_h):
                        time_since_last_object = time.time()
                        object_center: float = self.bbox.center.x

                        # the speed coefficient is a factor by which the speed is multiplied in regards to the distance between the object and the robot.
                        # its purpose is that the robot decelerates the closer it gets to the obstacle
                        self.sonar_collision.set_speed_coefficient_setpoint()
                        if self.sonar_collision.speed_coefficient_setpoint <= 1:
                            if speed < self.max_speed:
                                speed += self.acceleration_step * d_time
                    elif speed > 0:
                        speed -= self.deceleration_step * d_time

                    # stop following if no object is detected for a set period of time
                    if time.time() - time_since_last_object > self.max_time_without_object:
                        twist.angular.z = 0
                        twist.linear.x = 0
                        self.cmdPub.publish(twist)
                        self._result.state = "Lost_object"
                        rospy.loginfo(
                            '%s: Aborted: object lost' % self._action_name)
                        self._as.set_aborted(self._result)
                        break

                    # check if sonars detected an obstacle
                    if self.sonar_collision.collision():
                        speed = 0
                        print("obstacle detected")

                    # speed checking
                    if speed < 0:
                        speed = 0
                    if speed != 0:
                        time_stopped = time.time()

                    # finish following if the robot doesn't move for a set period of time
                    if time.time() - time_stopped >= self.max_time_stopped:
                        twist.angular.z = 0
                        twist.linear.x = 0
                        self.cmdPub.publish(twist)
                        if deceleration_coefficient < 0.5:
                            #self._result.state = "Reached_object"
                            self._result.state = "Lost_object"
                            rospy.loginfo(
                                '%s: Succeeded: object reached' % self._action_name)
                            self._as.set_succeeded(self._result)
                        else:
                            self._result.state = "Lost_object"
                            rospy.loginfo(
                                '%s: Aborted: object lost' % self._action_name)
                            self._as.set_aborted(self._result)
                        break

                    # update deceleration coefficient (using a PID)
                    deceleration_coefficient: float = self.sonar_collision.get_speed_coefficient()
                    # set the linear speed as a product of the speed setpoint multiplied by the deceleration coefficient
                    twist.linear.x = speed * deceleration_coefficient
                    # get the angular velocity setpoint by computing the offset between the object center and the center of frame
                    # multiplied by an angular speed coefficient
                    angular_speed_setpoint: float = (self.frame_center_x - object_center) * self.angular_speed_coefficient

                    # update the angulat speed PID
                    angular_speed = self.angular_pid.update(
                        angular_speed_setpoint, angular_speed)
                    # set the angular speed
                    twist.angular.z = angular_speed

                    self.cmdPub.publish(twist)
                    self._as.publish_feedback(self._feedback)

                    time_old = time.time()
                    r.sleep()

        else:
            print("wrong goal task")


if __name__ == '__main__':
    rospy.init_node('following')

    input_image_info_topic: str = rospy.get_param("~input_image_info_topic")  # camera info
    angular_pid: list = rospy.get_param("~angular_pid")  # kd, ki and kd parameters for the angular velocity PID
    max_speed: float = rospy.get_param("~max_speed") # maximum linear speed of the robot
    acceleration_step: float = rospy.get_param("~acceleration_step") # acceleration step per tick (20 Hz by default)
    deceleration_step: float = rospy.get_param("~deceleration_step") # deceleration step per tick (20 Hz by default)
    max_time_without_object: float = rospy.get_param("~max_time_without_object") # time without any detection until the robot stops following
    max_time_stopped: float = rospy.get_param("~max_time_stopped") # maximum amount of time stopped until the robot stops following
    angular_speed_coefficient: float = rospy.get_param("~angular_speed_coefficient") # coefficient used to set the angular velocity
    iou: float = rospy.get_param("~iou")  # re-acquisition iou threshold

    server = FollowAction(rospy.get_name(),
                          input_image_info_topic,
                          angular_pid,
                          max_speed,
                          acceleration_step,
                          deceleration_step,
                          max_time_without_object,
                          max_time_stopped,
                          angular_speed_coefficient,
                          iou
                          )
    rospy.spin()
