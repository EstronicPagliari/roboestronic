; Auto-generated. Do not edit!


(cl:in-package ur_vision_msgs-msg)


;//! \htmlinclude TrackedObject2D.msg.html

(cl:defclass <TrackedObject2D> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (tracking_ID
    :reader tracking_ID
    :initarg :tracking_ID
    :type cl:integer
    :initform 0)
   (class_name
    :reader class_name
    :initarg :class_name
    :type cl:string
    :initform "")
   (bbox
    :reader bbox
    :initarg :bbox
    :type ur_vision_msgs-msg:BoundingBox2D
    :initform (cl:make-instance 'ur_vision_msgs-msg:BoundingBox2D))
   (velocity
    :reader velocity
    :initarg :velocity
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3)))
)

(cl:defclass TrackedObject2D (<TrackedObject2D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TrackedObject2D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TrackedObject2D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_vision_msgs-msg:<TrackedObject2D> is deprecated: use ur_vision_msgs-msg:TrackedObject2D instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <TrackedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:header-val is deprecated.  Use ur_vision_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'tracking_ID-val :lambda-list '(m))
(cl:defmethod tracking_ID-val ((m <TrackedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:tracking_ID-val is deprecated.  Use ur_vision_msgs-msg:tracking_ID instead.")
  (tracking_ID m))

(cl:ensure-generic-function 'class_name-val :lambda-list '(m))
(cl:defmethod class_name-val ((m <TrackedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:class_name-val is deprecated.  Use ur_vision_msgs-msg:class_name instead.")
  (class_name m))

(cl:ensure-generic-function 'bbox-val :lambda-list '(m))
(cl:defmethod bbox-val ((m <TrackedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:bbox-val is deprecated.  Use ur_vision_msgs-msg:bbox instead.")
  (bbox m))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <TrackedObject2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:velocity-val is deprecated.  Use ur_vision_msgs-msg:velocity instead.")
  (velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TrackedObject2D>) ostream)
  "Serializes a message object of type '<TrackedObject2D>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'tracking_ID)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'class_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'class_name))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'bbox) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'velocity) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TrackedObject2D>) istream)
  "Deserializes a message object of type '<TrackedObject2D>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'tracking_ID) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'class_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'class_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'bbox) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'velocity) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TrackedObject2D>)))
  "Returns string type for a message object of type '<TrackedObject2D>"
  "ur_vision_msgs/TrackedObject2D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrackedObject2D)))
  "Returns string type for a message object of type 'TrackedObject2D"
  "ur_vision_msgs/TrackedObject2D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TrackedObject2D>)))
  "Returns md5sum for a message object of type '<TrackedObject2D>"
  "cc8e28f11d977ee02934446183df155f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TrackedObject2D)))
  "Returns md5sum for a message object of type 'TrackedObject2D"
  "cc8e28f11d977ee02934446183df155f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TrackedObject2D>)))
  "Returns full string definition for message of type '<TrackedObject2D>"
  (cl:format cl:nil "# TrackedObject2D~%~%# Header~%std_msgs/Header header~%~%# ID of tracked object~%int32 tracking_ID~%~%# Class of detected object~%string class_name~%~%# Object bounding box~%BoundingBox2D bbox~%~%# Velocity of detected objects~%geometry_msgs/Vector3 velocity	~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: ur_vision_msgs/BoundingBox2D~%# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TrackedObject2D)))
  "Returns full string definition for message of type 'TrackedObject2D"
  (cl:format cl:nil "# TrackedObject2D~%~%# Header~%std_msgs/Header header~%~%# ID of tracked object~%int32 tracking_ID~%~%# Class of detected object~%string class_name~%~%# Object bounding box~%BoundingBox2D bbox~%~%# Velocity of detected objects~%geometry_msgs/Vector3 velocity	~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: ur_vision_msgs/BoundingBox2D~%# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TrackedObject2D>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4 (cl:length (cl:slot-value msg 'class_name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'bbox))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'velocity))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TrackedObject2D>))
  "Converts a ROS message object to a list"
  (cl:list 'TrackedObject2D
    (cl:cons ':header (header msg))
    (cl:cons ':tracking_ID (tracking_ID msg))
    (cl:cons ':class_name (class_name msg))
    (cl:cons ':bbox (bbox msg))
    (cl:cons ':velocity (velocity msg))
))
