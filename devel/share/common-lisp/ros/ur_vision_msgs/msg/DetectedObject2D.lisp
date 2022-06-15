; Auto-generated. Do not edit!


(cl:in-package ur_vision_msgs-msg)


;//! \htmlinclude DetectedObject2D.msg.html

(cl:defclass <DetectedObject2D> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (image_seq
    :reader image_seq
    :initarg :image_seq
    :type cl:integer
    :initform 0)
   (score
    :reader score
    :initarg :score
    :type cl:float
    :initform 0.0)
   (class_name
    :reader class_name
    :initarg :class_name
    :type cl:string
    :initform "")
   (bbox
    :reader bbox
    :initarg :bbox
    :type ur_vision_msgs-msg:BoundingBox2D
    :initform (cl:make-instance 'ur_vision_msgs-msg:BoundingBox2D)))
)

(cl:defclass DetectedObject2D (<DetectedObject2D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectedObject2D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectedObject2D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_vision_msgs-msg:<DetectedObject2D> is deprecated: use ur_vision_msgs-msg:DetectedObject2D instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <DetectedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:header-val is deprecated.  Use ur_vision_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'image_seq-val :lambda-list '(m))
(cl:defmethod image_seq-val ((m <DetectedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:image_seq-val is deprecated.  Use ur_vision_msgs-msg:image_seq instead.")
  (image_seq m))

(cl:ensure-generic-function 'score-val :lambda-list '(m))
(cl:defmethod score-val ((m <DetectedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:score-val is deprecated.  Use ur_vision_msgs-msg:score instead.")
  (score m))

(cl:ensure-generic-function 'class_name-val :lambda-list '(m))
(cl:defmethod class_name-val ((m <DetectedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:class_name-val is deprecated.  Use ur_vision_msgs-msg:class_name instead.")
  (class_name m))

(cl:ensure-generic-function 'bbox-val :lambda-list '(m))
(cl:defmethod bbox-val ((m <DetectedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:bbox-val is deprecated.  Use ur_vision_msgs-msg:bbox instead.")
  (bbox m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectedObject2D>) ostream)
  "Serializes a message object of type '<DetectedObject2D>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'image_seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'image_seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'image_seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'image_seq)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'score))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'class_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'class_name))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'bbox) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectedObject2D>) istream)
  "Deserializes a message object of type '<DetectedObject2D>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'image_seq)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'image_seq)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'image_seq)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'image_seq)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'score) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'class_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'class_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'bbox) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectedObject2D>)))
  "Returns string type for a message object of type '<DetectedObject2D>"
  "ur_vision_msgs/DetectedObject2D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectedObject2D)))
  "Returns string type for a message object of type 'DetectedObject2D"
  "ur_vision_msgs/DetectedObject2D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectedObject2D>)))
  "Returns md5sum for a message object of type '<DetectedObject2D>"
  "50d0e80dfe5f1b10cdeb5b4a212534cb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectedObject2D)))
  "Returns md5sum for a message object of type 'DetectedObject2D"
  "50d0e80dfe5f1b10cdeb5b4a212534cb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectedObject2D>)))
  "Returns full string definition for message of type '<DetectedObject2D>"
  (cl:format cl:nil "# DetectedObject2D~%~%# Header~%std_msgs/Header header~%~%# Source image sequence number~%uint32 image_seq~%~%# Detection confidence score~%float32 score~%~%# Class of detected object~%string class_name~%~%# Object bounding box~%BoundingBox2D bbox~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: ur_vision_msgs/BoundingBox2D~%# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectedObject2D)))
  "Returns full string definition for message of type 'DetectedObject2D"
  (cl:format cl:nil "# DetectedObject2D~%~%# Header~%std_msgs/Header header~%~%# Source image sequence number~%uint32 image_seq~%~%# Detection confidence score~%float32 score~%~%# Class of detected object~%string class_name~%~%# Object bounding box~%BoundingBox2D bbox~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: ur_vision_msgs/BoundingBox2D~%# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectedObject2D>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4 (cl:length (cl:slot-value msg 'class_name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'bbox))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectedObject2D>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectedObject2D
    (cl:cons ':header (header msg))
    (cl:cons ':image_seq (image_seq msg))
    (cl:cons ':score (score msg))
    (cl:cons ':class_name (class_name msg))
    (cl:cons ':bbox (bbox msg))
))
