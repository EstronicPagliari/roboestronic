; Auto-generated. Do not edit!


(cl:in-package ur_vision_msgs-msg)


;//! \htmlinclude TrackedObjectArray2D.msg.html

(cl:defclass <TrackedObjectArray2D> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (tracked_objects
    :reader tracked_objects
    :initarg :tracked_objects
    :type (cl:vector ur_vision_msgs-msg:TrackedObject2D)
   :initform (cl:make-array 0 :element-type 'ur_vision_msgs-msg:TrackedObject2D :initial-element (cl:make-instance 'ur_vision_msgs-msg:TrackedObject2D))))
)

(cl:defclass TrackedObjectArray2D (<TrackedObjectArray2D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TrackedObjectArray2D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TrackedObjectArray2D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_vision_msgs-msg:<TrackedObjectArray2D> is deprecated: use ur_vision_msgs-msg:TrackedObjectArray2D instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <TrackedObjectArray2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:header-val is deprecated.  Use ur_vision_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'tracked_objects-val :lambda-list '(m))
(cl:defmethod tracked_objects-val ((m <TrackedObjectArray2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:tracked_objects-val is deprecated.  Use ur_vision_msgs-msg:tracked_objects instead.")
  (tracked_objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TrackedObjectArray2D>) ostream)
  "Serializes a message object of type '<TrackedObjectArray2D>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'tracked_objects))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'tracked_objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TrackedObjectArray2D>) istream)
  "Deserializes a message object of type '<TrackedObjectArray2D>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'tracked_objects) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'tracked_objects)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'ur_vision_msgs-msg:TrackedObject2D))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TrackedObjectArray2D>)))
  "Returns string type for a message object of type '<TrackedObjectArray2D>"
  "ur_vision_msgs/TrackedObjectArray2D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrackedObjectArray2D)))
  "Returns string type for a message object of type 'TrackedObjectArray2D"
  "ur_vision_msgs/TrackedObjectArray2D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TrackedObjectArray2D>)))
  "Returns md5sum for a message object of type '<TrackedObjectArray2D>"
  "528705386720f4b0ead8da1628c48ac9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TrackedObjectArray2D)))
  "Returns md5sum for a message object of type 'TrackedObjectArray2D"
  "528705386720f4b0ead8da1628c48ac9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TrackedObjectArray2D>)))
  "Returns full string definition for message of type '<TrackedObjectArray2D>"
  (cl:format cl:nil "# TrackedObjectArray2D~%~%# Header~%std_msgs/Header header~%~%# Array of detected object in frame~%TrackedObject2D[] tracked_objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: ur_vision_msgs/TrackedObject2D~%# TrackedObject2D~%~%# Header~%std_msgs/Header header~%~%# ID of tracked object~%int32 tracking_ID~%~%# Class of detected object~%string class_name~%~%# Object bounding box~%BoundingBox2D bbox~%~%# Velocity of detected objects~%geometry_msgs/Vector3 velocity	~%~%================================================================================~%MSG: ur_vision_msgs/BoundingBox2D~%# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TrackedObjectArray2D)))
  "Returns full string definition for message of type 'TrackedObjectArray2D"
  (cl:format cl:nil "# TrackedObjectArray2D~%~%# Header~%std_msgs/Header header~%~%# Array of detected object in frame~%TrackedObject2D[] tracked_objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: ur_vision_msgs/TrackedObject2D~%# TrackedObject2D~%~%# Header~%std_msgs/Header header~%~%# ID of tracked object~%int32 tracking_ID~%~%# Class of detected object~%string class_name~%~%# Object bounding box~%BoundingBox2D bbox~%~%# Velocity of detected objects~%geometry_msgs/Vector3 velocity	~%~%================================================================================~%MSG: ur_vision_msgs/BoundingBox2D~%# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TrackedObjectArray2D>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'tracked_objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TrackedObjectArray2D>))
  "Converts a ROS message object to a list"
  (cl:list 'TrackedObjectArray2D
    (cl:cons ':header (header msg))
    (cl:cons ':tracked_objects (tracked_objects msg))
))
