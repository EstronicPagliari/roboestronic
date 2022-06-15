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
from dataclasses import dataclass
from std_msgs.msg import Int32
from queue import Queue


@dataclass
class BTMessage:
    id :str
    rssi1: int
    angle_horizontal: int
    angle_vertical: int
    reserved_param: int
    channel: int
    anchor_id: str
    user_str: str
    timestamp: int

    def __init__(self, array):
        try:
            self.id = array[0]
            self.rssi1=int(array[1])
            self.angle_horizontal = int(array[2])
            self.angle_vertical = int(array[3])
            self.reserved_param = int(array[4])
            self.channel = int(array[5])
            self.anchor_id = array[6]
            self.user_str = array[7]
            self.timestamp = int(array[8])
        except ValueError:
            raise ValueError("error")
class BTFollow:
    def __init__(self, usb_port: str):
        self.pose_pub: Publisher = rospy.Publisher("/beacon_pose", Pose2D, queue_size=1)
        self.rssi_pub: Publisher = rospy.Publisher("/beacon_rssi", Int32, queue_size=1)
        self.CAEN = serial.Serial(port = usb_port,
                                  baudrate = 115200,
                                  parity = serial.PARITY_NONE,
                                  stopbits = 1,
                                  bytesize = 8,
                                  xonxoff = True,
                                  timeout = 1,
                                  )
        antena_height = 0.2
        beacon_height = 1
        self.height_dif = beacon_height-antena_height
        self.tfBuffer = tf2.Buffer()
        self.listener = tf2.TransformListener(self.tfBuffer)
        self.robot_width = 0.6
        self.q_sum = -70
        self.q = Queue(10)


    def get_message(self):
        timeout = 0
        line = ""
        while timeout<1000:
            for c in self.CAEN.read():
                timeout += 1
                if c == 13 or c == 10:
                    if len(line) > 10:
                        bt_message = BTMessage(line.split(","))
                        return(bt_message)
                else:
                    line+=chr(c)

    def get_pose(self, message):
        tangens = math.tan(math.radians(message.angle_vertical))
        if tangens == 0:
            tangens=0.01
        d = (self.height_dif / tangens)
        x = math.cos(math.radians(message.angle_horizontal)) * d
        y = math.sin(math.radians(message.angle_horizontal)) * d
        pose = Pose2D()
        pose.x = x
        pose.y = y
        pose.theta = math.radians(message.angle_horizontal)
        return pose




    def run(self):
        while not rospy.is_shutdown():
            message =self.get_message()
            pose = self.get_pose(message)
            self.q.put(message.rssi1)
            if self.q.full():
                self.q_sum = (sum(list(self.q.queue))/10)
                print(self.q_sum)
                self.q.get()
            if self.q_sum > -65:
                self.pose_pub.publish(pose)
            self.rssi_pub.publish(message.rssi1)


if __name__ == '__main__':
    rospy.init_node('bt_pos_publisher')
    usb_device: str = rospy.get_param("~bt_device")  # camera info
    #usb_device ="/dev/ttyUSB0"
    bt_follow=BTFollow(usb_device)
    bt_follow.run()
