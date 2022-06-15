// Generated by gencpp from file bt_follow/FollowActionGoal.msg
// DO NOT EDIT!


#ifndef BT_FOLLOW_MESSAGE_FOLLOWACTIONGOAL_H
#define BT_FOLLOW_MESSAGE_FOLLOWACTIONGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <actionlib_msgs/GoalID.h>
#include <bt_follow/FollowGoal.h>

namespace bt_follow
{
template <class ContainerAllocator>
struct FollowActionGoal_
{
  typedef FollowActionGoal_<ContainerAllocator> Type;

  FollowActionGoal_()
    : header()
    , goal_id()
    , goal()  {
    }
  FollowActionGoal_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , goal_id(_alloc)
    , goal(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
  _goal_id_type goal_id;

   typedef  ::bt_follow::FollowGoal_<ContainerAllocator>  _goal_type;
  _goal_type goal;





  typedef boost::shared_ptr< ::bt_follow::FollowActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bt_follow::FollowActionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct FollowActionGoal_

typedef ::bt_follow::FollowActionGoal_<std::allocator<void> > FollowActionGoal;

typedef boost::shared_ptr< ::bt_follow::FollowActionGoal > FollowActionGoalPtr;
typedef boost::shared_ptr< ::bt_follow::FollowActionGoal const> FollowActionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bt_follow::FollowActionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bt_follow::FollowActionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::bt_follow::FollowActionGoal_<ContainerAllocator1> & lhs, const ::bt_follow::FollowActionGoal_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.goal_id == rhs.goal_id &&
    lhs.goal == rhs.goal;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::bt_follow::FollowActionGoal_<ContainerAllocator1> & lhs, const ::bt_follow::FollowActionGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace bt_follow

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::bt_follow::FollowActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bt_follow::FollowActionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bt_follow::FollowActionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bt_follow::FollowActionGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bt_follow::FollowActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bt_follow::FollowActionGoal_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bt_follow::FollowActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ca7ba45f264bad91f4a699f8282e60b9";
  }

  static const char* value(const ::bt_follow::FollowActionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xca7ba45f264bad91ULL;
  static const uint64_t static_value2 = 0xf4a699f8282e60b9ULL;
};

template<class ContainerAllocator>
struct DataType< ::bt_follow::FollowActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bt_follow/FollowActionGoal";
  }

  static const char* value(const ::bt_follow::FollowActionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bt_follow::FollowActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalID goal_id\n"
"FollowGoal goal\n"
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
"MSG: actionlib_msgs/GoalID\n"
"# The stamp should store the time at which this goal was requested.\n"
"# It is used by an action server when it tries to preempt all\n"
"# goals that were requested before a certain time\n"
"time stamp\n"
"\n"
"# The id provides a way to associate feedback and\n"
"# result message with specific goal requests. The id\n"
"# specified must be unique.\n"
"string id\n"
"\n"
"\n"
"================================================================================\n"
"MSG: bt_follow/FollowGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#goal definition\n"
"string task\n"
;
  }

  static const char* value(const ::bt_follow::FollowActionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bt_follow::FollowActionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.goal_id);
      stream.next(m.goal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct FollowActionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bt_follow::FollowActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bt_follow::FollowActionGoal_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
    s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
    s << std::endl;
    Printer< ::bt_follow::FollowGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BT_FOLLOW_MESSAGE_FOLLOWACTIONGOAL_H