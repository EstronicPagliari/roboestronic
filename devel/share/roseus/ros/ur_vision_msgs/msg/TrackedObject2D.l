;; Auto-generated. Do not edit!


(when (boundp 'ur_vision_msgs::TrackedObject2D)
  (if (not (find-package "UR_VISION_MSGS"))
    (make-package "UR_VISION_MSGS"))
  (shadow 'TrackedObject2D (find-package "UR_VISION_MSGS")))
(unless (find-package "UR_VISION_MSGS::TRACKEDOBJECT2D")
  (make-package "UR_VISION_MSGS::TRACKEDOBJECT2D"))

(in-package "ROS")
;;//! \htmlinclude TrackedObject2D.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass ur_vision_msgs::TrackedObject2D
  :super ros::object
  :slots (_header _tracking_ID _class_name _bbox _velocity ))

(defmethod ur_vision_msgs::TrackedObject2D
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:tracking_ID __tracking_ID) 0)
    ((:class_name __class_name) "")
    ((:bbox __bbox) (instance ur_vision_msgs::BoundingBox2D :init))
    ((:velocity __velocity) (instance geometry_msgs::Vector3 :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _tracking_ID (round __tracking_ID))
   (setq _class_name (string __class_name))
   (setq _bbox __bbox)
   (setq _velocity __velocity)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:tracking_ID
   (&optional __tracking_ID)
   (if __tracking_ID (setq _tracking_ID __tracking_ID)) _tracking_ID)
  (:class_name
   (&optional __class_name)
   (if __class_name (setq _class_name __class_name)) _class_name)
  (:bbox
   (&rest __bbox)
   (if (keywordp (car __bbox))
       (send* _bbox __bbox)
     (progn
       (if __bbox (setq _bbox (car __bbox)))
       _bbox)))
  (:velocity
   (&rest __velocity)
   (if (keywordp (car __velocity))
       (send* _velocity __velocity)
     (progn
       (if __velocity (setq _velocity (car __velocity)))
       _velocity)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _tracking_ID
    4
    ;; string _class_name
    4 (length _class_name)
    ;; ur_vision_msgs/BoundingBox2D _bbox
    (send _bbox :serialization-length)
    ;; geometry_msgs/Vector3 _velocity
    (send _velocity :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _tracking_ID
       (write-long _tracking_ID s)
     ;; string _class_name
       (write-long (length _class_name) s) (princ _class_name s)
     ;; ur_vision_msgs/BoundingBox2D _bbox
       (send _bbox :serialize s)
     ;; geometry_msgs/Vector3 _velocity
       (send _velocity :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _tracking_ID
     (setq _tracking_ID (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _class_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _class_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; ur_vision_msgs/BoundingBox2D _bbox
     (send _bbox :deserialize buf ptr-) (incf ptr- (send _bbox :serialization-length))
   ;; geometry_msgs/Vector3 _velocity
     (send _velocity :deserialize buf ptr-) (incf ptr- (send _velocity :serialization-length))
   ;;
   self)
  )

(setf (get ur_vision_msgs::TrackedObject2D :md5sum-) "cc8e28f11d977ee02934446183df155f")
(setf (get ur_vision_msgs::TrackedObject2D :datatype-) "ur_vision_msgs/TrackedObject2D")
(setf (get ur_vision_msgs::TrackedObject2D :definition-)
      "# TrackedObject2D

# Header
std_msgs/Header header

# ID of tracked object
int32 tracking_ID

# Class of detected object
string class_name

# Object bounding box
BoundingBox2D bbox

# Velocity of detected objects
geometry_msgs/Vector3 velocity	

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

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :ur_vision_msgs/TrackedObject2D "cc8e28f11d977ee02934446183df155f")


