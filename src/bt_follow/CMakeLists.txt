cmake_minimum_required(VERSION 3.0.2)
project(bt_follow)

## Find catkin dependencies
find_package(catkin REQUIRED COMPONENTS actionlib message_generation)

## Find Boost
find_package(Boost REQUIRED COMPONENTS system thread)


## Add actions
add_action_files(DIRECTORY action FILES Follow.action)

## Generate messages
generate_messages(DEPENDENCIES std_msgs actionlib_msgs)



## Define catkin exports
catkin_package(
  CATKIN_DEPENDS message_runtime roscpp actionlib
  DEPENDS Boost
)

## Setup include dirs
include_directories(include ${catkin_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS})

## Install scripts and executables
install(PROGRAMS
  scripts/follow_me.py
  scripts/test_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})



