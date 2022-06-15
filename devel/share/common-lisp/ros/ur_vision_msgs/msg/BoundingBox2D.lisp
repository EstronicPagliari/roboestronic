; Auto-generated. Do not edit!


(cl:in-package ur_vision_msgs-msg)


;//! \htmlinclude BoundingBox2D.msg.html

(cl:defclass <BoundingBox2D> (roslisp-msg-protocol:ros-message)
  ((center
    :reader center
    :initarg :center
    :type geometry_msgs-msg:Pose2D
    :initform (cl:make-instance 'geometry_msgs-msg:Pose2D))
   (w
    :reader w
    :initarg :w
    :type cl:float
    :initform 0.0)
   (h
    :reader h
    :initarg :h
    :type cl:float
    :initform 0.0))
)

(cl:defclass BoundingBox2D (<BoundingBox2D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BoundingBox2D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BoundingBox2D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_vision_msgs-msg:<BoundingBox2D> is deprecated: use ur_vision_msgs-msg:BoundingBox2D instead.")))

(cl:ensure-generic-function 'center-val :lambda-list '(m))
(cl:defmethod center-val ((m <BoundingBox2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:center-val is deprecated.  Use ur_vision_msgs-msg:center instead.")
  (center m))

(cl:ensure-generic-function 'w-val :lambda-list '(m))
(cl:defmethod w-val ((m <BoundingBox2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:w-val is deprecated.  Use ur_vision_msgs-msg:w instead.")
  (w m))

(cl:ensure-generic-function 'h-val :lambda-list '(m))
(cl:defmethod h-val ((m <BoundingBox2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:h-val is deprecated.  Use ur_vision_msgs-msg:h instead.")
  (h m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BoundingBox2D>) ostream)
  "Serializes a message object of type '<BoundingBox2D>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'center) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'w))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'h))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BoundingBox2D>) istream)
  "Deserializes a message object of type '<BoundingBox2D>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'center) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'w) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'h) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BoundingBox2D>)))
  "Returns string type for a message object of type '<BoundingBox2D>"
  "ur_vision_msgs/BoundingBox2D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BoundingBox2D)))
  "Returns string type for a message object of type 'BoundingBox2D"
  "ur_vision_msgs/BoundingBox2D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BoundingBox2D>)))
  "Returns md5sum for a message object of type '<BoundingBox2D>"
  "46d3d089c3f3f7448497052cba2d6ff1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BoundingBox2D)))
  "Returns md5sum for a message object of type 'BoundingBox2D"
  "46d3d089c3f3f7448497052cba2d6ff1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BoundingBox2D>)))
  "Returns full string definition for message of type '<BoundingBox2D>"
  (cl:format cl:nil "# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BoundingBox2D)))
  "Returns full string definition for message of type 'BoundingBox2D"
  (cl:format cl:nil "# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BoundingBox2D>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'center))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BoundingBox2D>))
  "Converts a ROS message object to a list"
  (cl:list 'BoundingBox2D
    (cl:cons ':center (center msg))
    (cl:cons ':w (w msg))
    (cl:cons ':h (h msg))
))
