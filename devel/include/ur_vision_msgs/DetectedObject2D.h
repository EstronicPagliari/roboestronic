// Generated by gencpp from file ur_vision_msgs/DetectedObject2D.msg
// DO NOT EDIT!


#ifndef UR_VISION_MSGS_MESSAGE_DETECTEDOBJECT2D_H
#define UR_VISION_MSGS_MESSAGE_DETECTEDOBJECT2D_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <ur_vision_msgs/BoundingBox2D.h>

namespace ur_vision_msgs
{
template <class ContainerAllocator>
struct DetectedObject2D_
{
  typedef DetectedObject2D_<ContainerAllocator> Type;

  DetectedObject2D_()
    : header()
    , image_seq(0)
    , score(0.0)
    , class_name()
    , bbox()  {
    }
  DetectedObject2D_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , image_seq(0)
    , score(0.0)
    , class_name(_alloc)
    , bbox(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint32_t _image_seq_type;
  _image_seq_type image_seq;

   typedef float _score_type;
  _score_type score;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _class_name_type;
  _class_name_type class_name;

   typedef  ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator>  _bbox_type;
  _bbox_type bbox;





  typedef boost::shared_ptr< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> const> ConstPtr;

}; // struct DetectedObject2D_

typedef ::ur_vision_msgs::DetectedObject2D_<std::allocator<void> > DetectedObject2D;

typedef boost::shared_ptr< ::ur_vision_msgs::DetectedObject2D > DetectedObject2DPtr;
typedef boost::shared_ptr< ::ur_vision_msgs::DetectedObject2D const> DetectedObject2DConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator1> & lhs, const ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.image_seq == rhs.image_seq &&
    lhs.score == rhs.score &&
    lhs.class_name == rhs.class_name &&
    lhs.bbox == rhs.bbox;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator1> & lhs, const ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ur_vision_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "50d0e80dfe5f1b10cdeb5b4a212534cb";
  }

  static const char* value(const ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x50d0e80dfe5f1b10ULL;
  static const uint64_t static_value2 = 0xcdeb5b4a212534cbULL;
};

template<class ContainerAllocator>
struct DataType< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ur_vision_msgs/DetectedObject2D";
  }

  static const char* value(const ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# DetectedObject2D\n"
"\n"
"# Header\n"
"std_msgs/Header header\n"
"\n"
"# Source image sequence number\n"
"uint32 image_seq\n"
"\n"
"# Detection confidence score\n"
"float32 score\n"
"\n"
"# Class of detected object\n"
"string class_name\n"
"\n"
"# Object bounding box\n"
"BoundingBox2D bbox\n"
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
;
  }

  static const char* value(const ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.image_seq);
      stream.next(m.score);
      stream.next(m.class_name);
      stream.next(m.bbox);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DetectedObject2D_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ur_vision_msgs::DetectedObject2D_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "image_seq: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.image_seq);
    s << indent << "score: ";
    Printer<float>::stream(s, indent + "  ", v.score);
    s << indent << "class_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.class_name);
    s << indent << "bbox: ";
    s << std::endl;
    Printer< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >::stream(s, indent + "  ", v.bbox);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UR_VISION_MSGS_MESSAGE_DETECTEDOBJECT2D_H