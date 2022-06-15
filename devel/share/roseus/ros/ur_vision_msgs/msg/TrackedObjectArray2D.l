;; Auto-generated. Do not edit!


(when (boundp 'ur_vision_msgs::TrackedObjectArray2D)
  (if (not (find-package "UR_VISION_MSGS"))
    (make-package "UR_VISION_MSGS"))
  (shadow 'TrackedObjectArray2D (find-package "UR_VISION_MSGS")))
(unless (find-package "UR_VISION_MSGS::TRACKEDOBJECTARRAY2D")
  (make-package "UR_VISION_MSGS::TRACKEDOBJECTARRAY2D"))

(in-package "ROS")
;;//! \htmlinclude TrackedObjectArray2D.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass ur_vision_msgs::TrackedObjectArray2D
  :super ros::object
  :slots (_header _tracked_objects ))

(defmethod ur_vision_msgs::TrackedObjectArray2D
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:tracked_objects __tracked_objects) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _tracked_objects __tracked_objects)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:tracked_objects
   (&rest __tracked_objects)
   (if (keywordp (car __tracked_objects))
       (send* _tracked_objects __tracked_objects)
     (progn
       (if __tracked_objects (setq _tracked_objects (car __tracked_objects)))
       _tracked_objects)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; ur_vision_msgs/TrackedObject2D[] _tracked_objects
    (apply #'+ (send-all _tracked_objects :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; ur_vision_msgs/TrackedObject2D[] _tracked_objects
     (write-long (length _tracked_objects) s)
     (dolist (elem _tracked_objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; ur_vision_msgs/TrackedObject2D[] _tracked_objects
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tracked_objects (let (r) (dotimes (i n) (push (instance ur_vision_msgs::TrackedObject2D :init) r)) r))
     (dolist (elem- _tracked_objects)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ur_vision_msgs::TrackedObjectArray2D :md5sum-) "528705386720f4b0ead8da1628c48ac9")
(setf (get ur_vision_msgs::TrackedObjectArray2D :datatype-) "ur_vision_msgs/TrackedObjectArray2D")
(setf (get ur_vision_msgs::TrackedObjectArray2D :definition-)
      "# TrackedObjectArray2D

# Header
std_msgs/Header header

# Array of detected object in frame
TrackedObject2D[] tracked_objects

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
MSG: ur_vision_msgs/TrackedObject2D
# TrackedObject2D

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



(provide :ur_vision_msgs/TrackedObjectArray2D "528705386720f4b0ead8da1628c48ac9")


