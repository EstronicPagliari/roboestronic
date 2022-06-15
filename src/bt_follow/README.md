# follow_me

## Introduction
This is a package for object following. The robot follows tracked object unill it reaches them. The main node in this package is follow.py, which is an actionlib
server, that starts following once it recieves a "Follow" goal. The following stops if it recieves a cancel request, if the robot reaches and object or if the 
tracked object is lost for a set period of time. Followin slows down if the robot gets near to obstacles, and stops completely once it is very close to an obstacle
Continuous_follow is an actionlib client, that sends "Follow" goals to follow.py everytime it stops following, thus making the following continuos. 

# Installation

This package uses ur_vision messages:

    https://github.com/UbiquityRobotics/ur_vision_msgs.git
    
It aslo uses the actionlib package:
  
    apt-get istall ros-noetic-actionlib

## Parameters

`camera_resolution` (string, default: "410x308")
camera resolution (format "WIDTHxHEIGHT")

`angular_pid` (str, default: "0.3, 0.0, 0.0")
PID parameters for angular speed. (fromat "kp, ki, kd")

`deceleration_pid` (str, default: "0.3, 0.05, 0.0")
PID parameters for the deceleration coefficient. (fromat "kp, ki, kd")

`max_speed` (float, default: 0.4)
maximum linear speed of robot.

`acceleration_step` (float, default: 0.05)
acceleration increase on every cycle (20 Hz). Accelerating to max speed if tracked object is in frame.

`deceleration_pid` (float, default: 0.15)
acceleration decrease on every cycle (20 Hz). Decelerating if no tracked object is in frame.

`max_time_without_object` (float, default: 7)
time threshold without trackable object in frame before stopping following and returning "Lost_object"


`max_time_stopped` (float, default: 1)
time trashold where robot is stationary before stopping following and returning "Reached_object"

`angular_speed_coefficient` (float, default: 0.01)
coefficient used to set the angular velocity setpoint

## Run

run the folllow me server:

    roslaunch follow_me follow_me.launch
    
Note that follow_me requires an object tracking node to run (the current object tracking package is ur_object_tracking)

    roslaunch ur_object_tracking track.launch
