# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ur_vision_msgs/BoundingBox2D.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class BoundingBox2D(genpy.Message):
  _md5sum = "46d3d089c3f3f7448497052cba2d6ff1"
  _type = "ur_vision_msgs/BoundingBox2D"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# BoundingBox2D

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
"""
  __slots__ = ['center','w','h']
  _slot_types = ['geometry_msgs/Pose2D','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       center,w,h

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BoundingBox2D, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.center is None:
        self.center = geometry_msgs.msg.Pose2D()
      if self.w is None:
        self.w = 0.
      if self.h is None:
        self.h = 0.
    else:
      self.center = geometry_msgs.msg.Pose2D()
      self.w = 0.
      self.h = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3d2f().pack(_x.center.x, _x.center.y, _x.center.theta, _x.w, _x.h))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.center is None:
        self.center = geometry_msgs.msg.Pose2D()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.center.x, _x.center.y, _x.center.theta, _x.w, _x.h,) = _get_struct_3d2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3d2f().pack(_x.center.x, _x.center.y, _x.center.theta, _x.w, _x.h))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.center is None:
        self.center = geometry_msgs.msg.Pose2D()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.center.x, _x.center.y, _x.center.theta, _x.w, _x.h,) = _get_struct_3d2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d2f = None
def _get_struct_3d2f():
    global _struct_3d2f
    if _struct_3d2f is None:
        _struct_3d2f = struct.Struct("<3d2f")
    return _struct_3d2f
