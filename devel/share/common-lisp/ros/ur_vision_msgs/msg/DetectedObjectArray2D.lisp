; Auto-generated. Do not edit!


(cl:in-package ur_vision_msgs-msg)


;//! \htmlinclude DetectedObjectArray2D.msg.html

(cl:defclass <DetectedObjectArray2D> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (detected_objects
    :reader detected_objects
    :initarg :detected_objects
    :type (cl:vector ur_vision_msgs-msg:DetectedObject2D)
   :initform (cl:make-array 0 :element-type 'ur_vision_msgs-msg:DetectedObject2D :initial-element (cl:make-instance 'ur_vision_msgs-msg:DetectedObject2D))))
)

(cl:defclass DetectedObjectArray2D (<DetectedObjectArray2D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectedObjectArray2D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectedObjectArray2D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_vision_msgs-msg:<DetectedObjectArray2D> is deprecated: use ur_vision_msgs-msg:DetectedObjectArray2D instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <DetectedObjectArray2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:header-val is deprecated.  Use ur_vision_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'detected_objects-val :lambda-list '(m))
(cl:defmethod detected_objects-val ((m <DetectedObjectArray2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_vision_msgs-msg:detected_objects-val is deprecated.  Use ur_vision_msgs-msg:detected_objects instead.")
  (detected_objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectedObjectArray2D>) ostream)
  "Serializes a message object of type '<DetectedObjectArray2D>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'detected_objects))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'detected_objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectedObjectArray2D>) istream)
  "Deserializes a message object of type '<DetectedObjectArray2D>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'detected_objects) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'detected_objects)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'ur_vision_msgs-msg:DetectedObject2D))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectedObjectArray2D>)))
  "Returns string type for a message object of type '<DetectedObjectArray2D>"
  "ur_vision_msgs/DetectedObjectArray2D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectedObjectArray2D)))
  "Returns string type for a message object of type 'DetectedObjectArray2D"
  "ur_vision_msgs/DetectedObjectArray2D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectedObjectArray2D>)))
  "Returns md5sum for a message object of type '<DetectedObjectArray2D>"
  "705846d459e449e2d96224cc35ed3c41")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectedObjectArray2D)))
  "Returns md5sum for a message object of type 'DetectedObjectArray2D"
  "705846d459e449e2d96224cc35ed3c41")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectedObjectArray2D>)))
  "Returns full string definition for message of type '<DetectedObjectArray2D>"
  (cl:format cl:nil "# DetectedObjectArray2D~%~%# Header~%std_msgs/Header header~%~%# Array of detected object in frame~%DetectedObject2D[] detected_objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: ur_vision_msgs/DetectedObject2D~%# DetectedObject2D~%~%# Header~%std_msgs/Header header~%~%# Source image sequence number~%uint32 image_seq~%~%# Detection confidence score~%float32 score~%~%# Class of detected object~%string class_name~%~%# Object bounding box~%BoundingBox2D bbox~%~%================================================================================~%MSG: ur_vision_msgs/BoundingBox2D~%# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectedObjectArray2D)))
  "Returns full string definition for message of type 'DetectedObjectArray2D"
  (cl:format cl:nil "# DetectedObjectArray2D~%~%# Header~%std_msgs/Header header~%~%# Array of detected object in frame~%DetectedObject2D[] detected_objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: ur_vision_msgs/DetectedObject2D~%# DetectedObject2D~%~%# Header~%std_msgs/Header header~%~%# Source image sequence number~%uint32 image_seq~%~%# Detection confidence score~%float32 score~%~%# Class of detected object~%string class_name~%~%# Object bounding box~%BoundingBox2D bbox~%~%================================================================================~%MSG: ur_vision_msgs/BoundingBox2D~%# BoundingBox2D~%~%# Object center~%geometry_msgs/Pose2D center~%~%# Object width~%float32 w~%~%# Object height~%float32 h~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# Deprecated~%# Please use the full 3D pose.~%~%# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.~%~%# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.~%~%~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectedObjectArray2D>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'detected_objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectedObjectArray2D>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectedObjectArray2D
    (cl:cons ':header (header msg))
    (cl:cons ':detected_objects (detected_objects msg))
))
