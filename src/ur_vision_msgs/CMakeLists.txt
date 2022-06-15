cmake_minimum_required(VERSION 3.0.2)

project(ur_vision_msgs)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs
  geometry_msgs)

include_directories(include)

add_message_files(
  DIRECTORY msg
  FILES
  BoundingBox2D.msg
  DetectedObject2D.msg
  DetectedObjectArray2D.msg
  TrackedObject2D.msg
  TrackedObjectArray2D.msg
)

generate_messages(DEPENDENCIES
  std_msgs
  geometry_msgs
)

catkin_package(CATKIN_DEPENDS
  message_runtime
  std_msgs
  geometry_msgs
)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
)

