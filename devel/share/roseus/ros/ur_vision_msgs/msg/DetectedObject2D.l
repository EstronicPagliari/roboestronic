;; Auto-generated. Do not edit!


(when (boundp 'ur_vision_msgs::DetectedObject2D)
  (if (not (find-package "UR_VISION_MSGS"))
    (make-package "UR_VISION_MSGS"))
  (shadow 'DetectedObject2D (find-package "UR_VISION_MSGS")))
(unless (find-package "UR_VISION_MSGS::DETECTEDOBJECT2D")
  (make-package "UR_VISION_MSGS::DETECTEDOBJECT2D"))

(in-package "ROS")
;;//! \htmlinclude DetectedObject2D.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass ur_vision_msgs::DetectedObject2D
  :super ros::object
  :slots (_header _image_seq _score _class_name _bbox ))

(defmethod ur_vision_msgs::DetectedObject2D
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:image_seq __image_seq) 0)
    ((:score __score) 0.0)
    ((:class_name __class_name) "")
    ((:bbox __bbox) (instance ur_vision_msgs::BoundingBox2D :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _image_seq (round __image_seq))
   (setq _score (float __score))
   (setq _class_name (string __class_name))
   (setq _bbox __bbox)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:image_seq
   (&optional __image_seq)
   (if __image_seq (setq _image_seq __image_seq)) _image_seq)
  (:score
   (&optional __score)
   (if __score (setq _score __score)) _score)
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
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint32 _image_seq
    4
    ;; float32 _score
    4
    ;; string _class_name
    4 (length _class_name)
    ;; ur_vision_msgs/BoundingBox2D _bbox
    (send _bbox :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint32 _image_seq
       (write-long _image_seq s)
     ;; float32 _score
       (sys::poke _score (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _class_name
       (write-long (length _class_name) s) (princ _class_name s)
     ;; ur_vision_msgs/BoundingBox2D _bbox
       (send _bbox :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint32 _image_seq
     (setq _image_seq (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _score
     (setq _score (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _class_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _class_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; ur_vision_msgs/BoundingBox2D _bbox
     (send _bbox :deserialize buf ptr-) (incf ptr- (send _bbox :serialization-length))
   ;;
   self)
  )

(setf (get ur_vision_msgs::DetectedObject2D :md5sum-) "50d0e80dfe5f1b10cdeb5b4a212534cb")
(setf (get ur_vision_msgs::DetectedObject2D :datatype-) "ur_vision_msgs/DetectedObject2D")
(setf (get ur_vision_msgs::DetectedObject2D :definition-)
      "# DetectedObject2D

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

")



(provide :ur_vision_msgs/DetectedObject2D "50d0e80dfe5f1b10cdeb5b4a212534cb")


