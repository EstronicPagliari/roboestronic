#!/usr/bin/python3
#import follow_me.msg
import time
import actionlib
from geometry_msgs.msg import Twist
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
        ki=0.05
        kp=0.3
        kd=0
        self.linear_pid: PID = PID(kp, ki, kd)
        self.lidar_collision: LidarCollision = LidarCollision()
        self.lidar_collision.run()
        self.intensity=0
        self.angle=0
        self.tfBuffer = tf2.Buffer()
        self.listener = tf2.TransformListener(self.tfBuffer)
        self.robot_width = 0.6
        #sub = rospy.Subscriber('/scan_filtered', LaserScan, callback)
    
    def lidar_callback(self, msg):
        cloud = msg #self.laser_projector.projectLaser(msg)
        min_range = math.inf
        start=time.time()
        #a=self.listener.transformPointCloud('/base_link',cloud)
        #trans=self.tfBuffer.lookup_transform("laser","base_link",rospy.Time())
        trans = self.tfBuffer.lookup_transform("base_link", "laser",rospy.Time())
        cloud_out = do_transform_cloud(cloud, trans)
        hits=0
        x_s=0
        y_s=0
        AOI=0.7
        for p in pc2.read_points(cloud_out, field_names = ("x", "y", "z"), skip_nans=True):
            point = Point()
            point.x = p[0]
            point.y = p[1]
            point.z = p[2]
            
            if point.y < self.robot_width/2 and point.y > -self.robot_width/2:
                hits+=1
                #y_s+=point.y* math.copysign(1,point.y)
                #x_s+=point.x
                y_s+= 1 / (1 + (point.y+AOI)**2) * math.copysign(1,point.y)
                x_s+= 1 / (1 + (point.x+AOI)**2) * math.copysign(1,point.x)
        if hits > 0:
            y_s/=hits
            x_s/=hits
        self.angle=y_s
        print("x_s ",x_s, "y_s",y_s, "hits ", hits )                
    
    def scan_callback(self,msg):
        # values at 0 degree
        current_angle=msg.angle_min
        hits = 0
        AOI = 0.7
        intensity=0
        angle=0
        for range in msg.ranges:
            current_angle+=msg.angle_increment

            if range < AOI:
                hits+=1
                intensity+=abs(range-AOI)
                angle+=current_angle + math.pi
        if hits > 0:
            angle/=hits
            angle-=(math.pi*1.5)
            intensity/=hits
        self.intensity=intensity
        self.angle=angle
        #print("angle= ", angle , "intensity= ", intensity)
        print ("speed factor =", math.cos(angle)*intensity, "angle factor= ", self.angle*self.intensity)
        
    def run(self):
        rate = rospy.Rate(20)
        linear_speed=0
        #rospy.Subscriber('/scan_filtered', LaserScan, self.scan_callback)
        rospy.Subscriber("/cloud_filtered", PointCloud2, self.lidar_callback,
                         queue_size=1)
        while not rospy.is_shutdown():

            #self.CAEN.set_low_latency_mode()
            #self.CAEN.set_buffer_size(100)
            output = str(self.CAEN.readlines(5))
            self.CAEN.flushInput()
            #output = str(self.CAEN.read_until(b'""', 50))
            #print(output)
            field = output.split(",")
            success = False
            RSSI_1=0
            RSSI_2=0
            angle_hor=0
            angle_ver=0
            try:
                RSSI_1 = int(field[2])
                RSSI_2 = int(field[5])
                angle_hor = int(field[3])
                angle_ver = int(field[4])
                # q1.put(angle_hor)
                # print("field ", field)
                #print("angle_hor: ", angle_hor)
                #print("angle_ver: ", angle_ver)
                #print("RSSI_1: ", RSSI_1)
                #print("RSSI_2: ", RSSI_2)
            except:
                ValueError
                continue

            if angle_ver < 30 and self.follow is False:
                if self.follow_i >= 5:
                    self.stop_i = 0
                    self.follow = True
                else:
                    self.follow_i += 1

            elif angle_ver >= 30 and self.follow is True:
                if self.stop_i >= 5:
                    self.follow_i = 0
                    self.follow = False
                else:
                    self.stop_i += 1

            twist: Twist = Twist()
            if self.follow is True:
                linear_speed_setpoint=(30-abs(angle_ver)) /60# - math.cos(self.angle)*self.intensity
                if linear_speed_setpoint < 0:
                    linear_speed_setpoint=0
                elif linear_speed_setpoint >= 0.4:
                    linear_speed_setpoint = 0.4
            else:
                linear_speed_setpoint = 0.0
            linear_speed = self.linear_pid.update(linear_speed_setpoint, linear_speed)
            if self.lidar_collision.collision():
                linear_speed = 0
            twist.linear.x=linear_speed 
            twist.angular.z = (-angle_hor / 50)#- self.angle#*self.intensity
            #twist: Twist = Twist()
            self.cmdPub.publish(twist)
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('bt_follow')
    usb_device: str = rospy.get_param("~bt_device")  # camera info
    bt_follow=BTFollow(usb_device)
    bt_follow.run()
