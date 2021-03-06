#!/usr/bin/python3

from __future__ import print_function

import sys

import rospy
# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import follow_me.msg

def fibonacci_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('follow_me', follow_me.msg.FollowAction)
    # Waits until the action server has started up and started
    # listening for goals.

    # Creates a goal to send to the action server.

    while not rospy.is_shutdown():
        print("waiting")
        client.wait_for_server()
        print("stopped waiting")
        goal = follow_me.msg.FollowGoal(task="Follow")
        print("sending goal")
        # Sends the goal to the action server.
        client.send_goal(goal)
        # Waits for the server to finish performing the action.
        client.wait_for_result()
        result = client.get_result()
        print(result)
        # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('fibonacci_client_py')
        result = fibonacci_client()
        print("Result:", result.state)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
