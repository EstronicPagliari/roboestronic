;; Auto-generated. Do not edit!


(when (boundp 'ur_vision_msgs::BoundingBox2D)
  (if (not (find-package "UR_VISION_MSGS"))
    (make-package "UR_VISION_MSGS"))
  (shadow 'BoundingBox2D (find-package "UR_VISION_MSGS")))
(unless (find-package "UR_VISION_MSGS::BOUNDINGBOX2D")
  (make-package "UR_VISION_MSGS::BOUNDINGBOX2D"))

(in-package "ROS")
;;//! \htmlinclude BoundingBox2D.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass ur_vision_msgs::BoundingBox2D
  :super ros::object
  :slots (_center _w _h ))

(defmethod ur_vision_msgs::BoundingBox2D
  (:init
   (&key
    ((:center __center) (instance geometry_msgs::Pose2D :init))
    ((:w __w) 0.0)
    ((:h __h) 0.0)
    )
   (send-super :init)
   (setq _center __center)
   (setq _w (float __w))
   (setq _h (float __h))
   self)
  (:center
   (&rest __center)
   (if (keywordp (car __center))
       (send* _center __center)
     (progn
       (if __center (setq _center (car __center)))
       _center)))
  (:w
   (&optional __w)
   (if __w (setq _w __w)) _w)
  (:h
   (&optional __h)
   (if __h (setq _h __h)) _h)
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose2D _center
    (send _center :serialization-length)
    ;; float32 _w
    4
    ;; float32 _h
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose2D _center
       (send _center :serialize s)
     ;; float32 _w
       (sys::poke _w (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _h
       (sys::poke _h (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose2D _center
     (send _center :deserialize buf ptr-) (incf ptr- (send _center :serialization-length))
   ;; float32 _w
     (setq _w (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _h
     (setq _h (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get ur_vision_msgs::BoundingBox2D :md5sum-) "46d3d089c3f3f7448497052cba2d6ff1")
(setf (get ur_vision_msgs::BoundingBox2D :datatype-) "ur_vision_msgs/BoundingBox2D")
(setf (get ur_vision_msgs::BoundingBox2D :definition-)
      "# BoundingBox2D

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

")



(provide :ur_vision_msgs/BoundingBox2D "46d3d089c3f3f7448497052cba2d6ff1")


