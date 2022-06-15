#!/usr/bin/python3

from __future__ import print_function

import sys

import rospy
# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import following.msg
from ur_vision_msgs.msg import *
from geometry_msgs.msg import Twist
class FollowAndSearch:
    def __init__(self):
        self.old_msg: str = ""

    def feedback_cb(self, msg: actionlib.GoalStatus):
        '''
        Get following status i.e. the ID of the current followed object
        :param msg:
        :return:
        '''

        new_msg: str = str(msg)
        new_msg = new_msg.split('"')
        new_msg=new_msg[1]

        if self.old_msg != new_msg:
            print("currently following ID: ", new_msg)
            self.old_msg = new_msg

    def run(self):
        client = actionlib.SimpleActionClient('following', following.msg.FollowAction)

        while not rospy.is_shutdown():
            print("waiting for server")
            client.wait_for_server()
            print("got server response")
            print("waiting for input to start following")
            input()
            goal = following.msg.FollowGoal(task="Follow")
            print("sending goal")
            # Sends the goal to the action server.
            client.send_goal(goal, feedback_cb=self.feedback_cb)
            print("following")
            # Waits for the server to finish performing the action.
            client.wait_for_result()
            print("stopped following")
            result = client.get_result()
            print(result)
            # Prints out the result of executing the action
        return client.get_result()

if __name__ == '__main__':
    try:
        # publish and subscribe over ROS.
        rospy.init_node('follow_client')
        fs = FollowAndSearch()
        fs.run()

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
