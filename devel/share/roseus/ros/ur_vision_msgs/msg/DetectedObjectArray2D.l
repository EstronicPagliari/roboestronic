;; Auto-generated. Do not edit!


(when (boundp 'ur_vision_msgs::DetectedObjectArray2D)
  (if (not (find-package "UR_VISION_MSGS"))
    (make-package "UR_VISION_MSGS"))
  (shadow 'DetectedObjectArray2D (find-package "UR_VISION_MSGS")))
(unless (find-package "UR_VISION_MSGS::DETECTEDOBJECTARRAY2D")
  (make-package "UR_VISION_MSGS::DETECTEDOBJECTARRAY2D"))

(in-package "ROS")
;;//! \htmlinclude DetectedObjectArray2D.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass ur_vision_msgs::DetectedObjectArray2D
  :super ros::object
  :slots (_header _detected_objects ))

(defmethod ur_vision_msgs::DetectedObjectArray2D
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:detected_objects __detected_objects) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _detected_objects __detected_objects)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:detected_objects
   (&rest __detected_objects)
   (if (keywordp (car __detected_objects))
       (send* _detected_objects __detected_objects)
     (progn
       (if __detected_objects (setq _detected_objects (car __detected_objects)))
       _detected_objects)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; ur_vision_msgs/DetectedObject2D[] _detected_objects
    (apply #'+ (send-all _detected_objects :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; ur_vision_msgs/DetectedObject2D[] _detected_objects
     (write-long (length _detected_objects) s)
     (dolist (elem _detected_objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; ur_vision_msgs/DetectedObject2D[] _detected_objects
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _detected_objects (let (r) (dotimes (i n) (push (instance ur_vision_msgs::DetectedObject2D :init) r)) r))
     (dolist (elem- _detected_objects)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ur_vision_msgs::DetectedObjectArray2D :md5sum-) "705846d459e449e2d96224cc35ed3c41")
(setf (get ur_vision_msgs::DetectedObjectArray2D :datatype-) "ur_vision_msgs/DetectedObjectArray2D")
(setf (get ur_vision_msgs::DetectedObjectArray2D :definition-)
      "# DetectedObjectArray2D

# Header
std_msgs/Header header

# Array of detected object in frame
DetectedObject2D[] detected_objects

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: ur_vision_msgs/DetectedObject2D
# DetectedObject2D

# Header
std_msgs/Header header

# Source image sequence number
uint32 image_seq

# Detection confidence score
float32 score

# Class of detected object
string class_name

# Object bounding box
BoundingBox2D bbox

================================================================================
MSG: ur_vision_msgs/BoundingBox2D
# BoundingBox2D

# Object center
geometry_msgs/Pose2D center

# Object width
float32 w

# Object height
float32 h

================================================================================
MSG: geometry_msgs/Pose2D
# Deprecated
# Please use the full 3D pose.

# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.

# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.


# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
float64 theta

")



(provide :ur_vision_msgs/DetectedObjectArray2D "705846d459e449e2d96224cc35ed3c41")


