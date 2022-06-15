#!/usr/bin/python3

import rospy
import math
from sensor_msgs.msg import LaserScan

def callback(msg):
    # values at 0 degree
    current_angle=msg.angle_min
    hits=0
    AOI=0.5
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
        angle/=(math.pi/2)
        intensity/=hits
    print("angle= ", angle , "intensity= ", intensity)
            


if __name__ == '__main__':
    rospy.init_node('obstacle_avoidance')
    sub = rospy.Subscriber('/scan_filtered', LaserScan, callback)
    rospy.spin()


