// Generated by gencpp from file ur_vision_msgs/TrackedObjectArray2D.msg
// DO NOT EDIT!


#ifndef UR_VISION_MSGS_MESSAGE_TRACKEDOBJECTARRAY2D_H
#define UR_VISION_MSGS_MESSAGE_TRACKEDOBJECTARRAY2D_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <ur_vision_msgs/TrackedObject2D.h>

namespace ur_vision_msgs
{
template <class ContainerAllocator>
struct TrackedObjectArray2D_
{
  typedef TrackedObjectArray2D_<ContainerAllocator> Type;

  TrackedObjectArray2D_()
    : header()
    , tracked_objects()  {
    }
  TrackedObjectArray2D_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , tracked_objects(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector< ::ur_vision_msgs::TrackedObject2D_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::ur_vision_msgs::TrackedObject2D_<ContainerAllocator> >::other >  _tracked_objects_type;
  _tracked_objects_type tracked_objects;





  typedef boost::shared_ptr< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> const> ConstPtr;

}; // struct TrackedObjectArray2D_

typedef ::ur_vision_msgs::TrackedObjectArray2D_<std::allocator<void> > TrackedObjectArray2D;

typedef boost::shared_ptr< ::ur_vision_msgs::TrackedObjectArray2D > TrackedObjectArray2DPtr;
typedef boost::shared_ptr< ::ur_vision_msgs::TrackedObjectArray2D const> TrackedObjectArray2DConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator1> & lhs, const ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.tracked_objects == rhs.tracked_objects;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator1> & lhs, const ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ur_vision_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "528705386720f4b0ead8da1628c48ac9";
  }

  static const char* value(const ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x528705386720f4b0ULL;
  static const uint64_t static_value2 = 0xead8da1628c48ac9ULL;
};

template<class ContainerAllocator>
struct DataType< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ur_vision_msgs/TrackedObjectArray2D";
  }

  static const char* value(const ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# TrackedObjectArray2D\n"
"\n"
"# Header\n"
"std_msgs/Header header\n"
"\n"
"# Array of detected object in frame\n"
"TrackedObject2D[] tracked_objects\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: ur_vision_msgs/TrackedObject2D\n"
"# TrackedObject2D\n"
"\n"
"# Header\n"
"std_msgs/Header header\n"
"\n"
"# ID of tracked object\n"
"int32 tracking_ID\n"
"\n"
"# Class of detected object\n"
"string class_name\n"
"\n"
"# Object bounding box\n"
"BoundingBox2D bbox\n"
"\n"
"# Velocity of detected objects\n"
"geometry_msgs/Vector3 velocity	\n"
"\n"
"================================================================================\n"
"MSG: ur_vision_msgs/BoundingBox2D\n"
"# BoundingBox2D\n"
"\n"
"# Object center\n"
"geometry_msgs/Pose2D center\n"
"\n"
"# Object width\n"
"float32 w\n"
"\n"
"# Object height\n"
"float32 h\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose2D\n"
"# Deprecated\n"
"# Please use the full 3D pose.\n"
"\n"
"# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.\n"
"\n"
"# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.\n"
"\n"
"\n"
"# This expresses a position and orientation on a 2D manifold.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 theta\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.tracked_objects);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TrackedObjectArray2D_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ur_vision_msgs::TrackedObjectArray2D_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "tracked_objects[]" << std::endl;
    for (size_t i = 0; i < v.tracked_objects.size(); ++i)
    {
      s << indent << "  tracked_objects[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::ur_vision_msgs::TrackedObject2D_<ContainerAllocator> >::stream(s, indent + "    ", v.tracked_objects[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // UR_VISION_MSGS_MESSAGE_TRACKEDOBJECTARRAY2D_H
