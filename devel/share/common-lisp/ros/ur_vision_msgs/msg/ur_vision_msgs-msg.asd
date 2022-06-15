
(cl:in-package :asdf)

(defsystem "ur_vision_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BoundingBox2D" :depends-on ("_package_BoundingBox2D"))
    (:file "_package_BoundingBox2D" :depends-on ("_package"))
    (:file "DetectedObject2D" :depends-on ("_package_DetectedObject2D"))
    (:file "_package_DetectedObject2D" :depends-on ("_package"))
    (:file "DetectedObjectArray2D" :depends-on ("_package_DetectedObjectArray2D"))
    (:file "_package_DetectedObjectArray2D" :depends-on ("_package"))
    (:file "TrackedObject2D" :depends-on ("_package_TrackedObject2D"))
    (:file "_package_TrackedObject2D" :depends-on ("_package"))
    (:file "TrackedObjectArray2D" :depends-on ("_package_TrackedObjectArray2D"))
    (:file "_package_TrackedObjectArray2D" :depends-on ("_package"))
  ))