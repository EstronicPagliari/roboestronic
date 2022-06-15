// Auto-generated. Do not edit!

// (in-package ur_vision_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let TrackedObject2D = require('./TrackedObject2D.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class TrackedObjectArray2D {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.tracked_objects = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('tracked_objects')) {
        this.tracked_objects = initObj.tracked_objects
      }
      else {
        this.tracked_objects = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TrackedObjectArray2D
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [tracked_objects]
    // Serialize the length for message field [tracked_objects]
    bufferOffset = _serializer.uint32(obj.tracked_objects.length, buffer, bufferOffset);
    obj.tracked_objects.forEach((val) => {
      bufferOffset = TrackedObject2D.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TrackedObjectArray2D
    let len;
    let data = new TrackedObjectArray2D(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [tracked_objects]
    // Deserialize array length for message field [tracked_objects]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.tracked_objects = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.tracked_objects[i] = TrackedObject2D.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.tracked_objects.forEach((val) => {
      length += TrackedObject2D.getMessageSize(val);
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ur_vision_msgs/TrackedObjectArray2D';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '528705386720f4b0ead8da1628c48ac9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # TrackedObjectArray2D
    
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TrackedObjectArray2D(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.tracked_objects !== undefined) {
      resolved.tracked_objects = new Array(msg.tracked_objects.length);
      for (let i = 0; i < resolved.tracked_objects.length; ++i) {
        resolved.tracked_objects[i] = TrackedObject2D.Resolve(msg.tracked_objects[i]);
      }
    }
    else {
      resolved.tracked_objects = []
    }

    return resolved;
    }
};

module.exports = TrackedObjectArray2D;
