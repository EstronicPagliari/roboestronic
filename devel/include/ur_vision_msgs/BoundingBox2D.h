// Generated by gencpp from file ur_vision_msgs/BoundingBox2D.msg
// DO NOT EDIT!


#ifndef UR_VISION_MSGS_MESSAGE_BOUNDINGBOX2D_H
#define UR_VISION_MSGS_MESSAGE_BOUNDINGBOX2D_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Pose2D.h>

namespace ur_vision_msgs
{
template <class ContainerAllocator>
struct BoundingBox2D_
{
  typedef BoundingBox2D_<ContainerAllocator> Type;

  BoundingBox2D_()
    : center()
    , w(0.0)
    , h(0.0)  {
    }
  BoundingBox2D_(const ContainerAllocator& _alloc)
    : center(_alloc)
    , w(0.0)
    , h(0.0)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Pose2D_<ContainerAllocator>  _center_type;
  _center_type center;

   typedef float _w_type;
  _w_type w;

   typedef float _h_type;
  _h_type h;





  typedef boost::shared_ptr< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> const> ConstPtr;

}; // struct BoundingBox2D_

typedef ::ur_vision_msgs::BoundingBox2D_<std::allocator<void> > BoundingBox2D;

typedef boost::shared_ptr< ::ur_vision_msgs::BoundingBox2D > BoundingBox2DPtr;
typedef boost::shared_ptr< ::ur_vision_msgs::BoundingBox2D const> BoundingBox2DConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator1> & lhs, const ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator2> & rhs)
{
  return lhs.center == rhs.center &&
    lhs.w == rhs.w &&
    lhs.h == rhs.h;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator1> & lhs, const ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ur_vision_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "46d3d089c3f3f7448497052cba2d6ff1";
  }

  static const char* value(const ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x46d3d089c3f3f744ULL;
  static const uint64_t static_value2 = 0x8497052cba2d6ff1ULL;
};

template<class ContainerAllocator>
struct DataType< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ur_vision_msgs/BoundingBox2D";
  }

  static const char* value(const ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# BoundingBox2D\n"
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

  static const char* value(const ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.center);
      stream.next(m.w);
      stream.next(m.h);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct BoundingBox2D_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ur_vision_msgs::BoundingBox2D_<ContainerAllocator>& v)
  {
    s << indent << "center: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose2D_<ContainerAllocator> >::stream(s, indent + "  ", v.center);
    s << indent << "w: ";
    Printer<float>::stream(s, indent + "  ", v.w);
    s << indent << "h: ";
    Printer<float>::stream(s, indent + "  ", v.h);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UR_VISION_MSGS_MESSAGE_BOUNDINGBOX2D_H
