cmake_minimum_required(VERSION 3.0.2)
project(detect_objects)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
  sensor_msgs
  ur_vision_msgs REQUIRED
)


catkin_package(
   #INCLUDE_DIRS include
   LIBRARIES detect_objects
   CATKIN_DEPENDS rospy std_msgs message_generation ur_vision_msgs sensor_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

