#!/usr/bin/python3
#import follow_me.msg
import time
import actionlib
from geometry_msgs.msg import Twist, Pose2D
import numpy as np
from sensor_msgs.msg import CameraInfo, LaserScan
from ur_vision_msgs.msg import *
from following.utils import *
import rospy
import serial
import sys
import math
import tf
import tf2_ros as tf2
from leg_tracker.msg import Person, PersonArray, Leg, LegArray





class BTFollow:
    def __init__(self, usb_port: str):
        self.cmdPub: Publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.CAEN = serial.Serial(port = usb_port,
                                  baudrate = 115200,
                                  parity = serial.PARITY_NONE,
                                  stopbits = 1,
                                  bytesize = 8,
                                  xonxoff = True,
                                  timeout = 1,
                                  )
        self.follow = False
        self.follow_i = 0
        self.stop_i = 0
        self.max_linear_speed = 0.8
        self.max_angular_speed = 1
        ki=0.05
        kp=0.3
        kd=0
        self.linear_speed=0
        self.angular_speed = 0
        self.pose = Pose2D()
        self.new_pose=Pose2D()
        self.old_pose = Pose2D()
        self.linear_pid: PID = PID(kp, ki, kd, 0.04)
        self.angular_pid: PID = PID(kp, ki, kd)
        self.lidar_collision: LidarCollision = LidarCollision()
        self.lidar_collision.run()
        self.intensity=0
        self.angle=0
        self.tfBuffer = tf2.Buffer()
        self.listener = tf2.TransformListener(self.tfBuffer)
        self.robot_width = 0.6
        self.beacon_timestamp=time.time()


        sub = rospy.Subscriber('/beacon_pose', Pose2D, self.beacon_callback)
        #sub = rospy.Subscriber('/people_tracked ', PersonArray, self.PersonArray_callback)
    def PersonArray_callback(self, msg):
        for person in msg.people:
            distance=person.pose.position

    def beacon_callback(self, msg):
        self.new_pose = msg
        self.beacon_timestamp = time.time()
        print(self.new_pose)

    def position_filtering(self):
        if self.new_pose.x < 0:
            self.new_pose.x = self.old_pose.x
        self.pose.x += (self.new_pose.x - self.old_pose.x) * 0.1
        self.pose.y += (self.new_pose.y - self.old_pose.y) * 0.1
        self.pose.theta += (self.new_pose.theta - self.old_pose.theta) * 0.3
        self.old_pose = self.pose


    def get_speed(self, pose):


        linear_speed = pose.x * 0.25
        angle=pose.theta
        angular_speed = -angle
        #print(angle)
        if pose.x  < 0.7 :
            linear_speed = 0
        elif linear_speed  > self.max_linear_speed:
            linear_speed = self.max_linear_speed

        if angular_speed < -self.max_angular_speed :
            angular_speed = -self.max_angular_speed
        elif angular_speed > self.max_angular_speed:
            angular_speed = self.max_angular_speed
        self.linear_speed=self.linear_pid.update(linear_speed, self.linear_speed)
        self.angular_speed = self.angular_pid.update(angular_speed, self.angular_speed)
        return self.linear_speed, self.angular_speed

    def run(self):
        rate = rospy.Rate(20)
        linear_speed=0
        #rospy.Subscriber('/scan_filtered', LaserScan, self.scan_callback)

        while not rospy.is_shutdown():

            self.position_filtering()
            linear_speed, angular_speed = self.get_speed(self.pose)

            twist: Twist = Twist()
            if self.lidar_collision.collision():
                linear_speed = 0
                print("collision")
            if time.time() - self.beacon_timestamp > 1:
                linear_speed = 0
                angular_speed = 0
                print("no beacon detected")
            self.lidar_collision.set_speed_coefficient_setpoint()
            twist.linear.x=linear_speed * (1-abs(angular_speed)) * self.lidar_collision.get_speed_coefficient()
            twist.angular.z = angular_speed
            #print(self.pose)
            #print("linear_speed: ", linear_speed, " angular_speed: ", angular_speed)
            #twist: Twist = Twist()
            self.cmdPub.publish(twist)
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('bt_following')
    usb_device: str = rospy.get_param("~bt_device")  # camera info
    bt_follow=BTFollow(usb_device)
    bt_follow.run()
