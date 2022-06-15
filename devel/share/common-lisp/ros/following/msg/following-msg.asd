
(cl:in-package :asdf)

(defsystem "following-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "FollowAction" :depends-on ("_package_FollowAction"))
    (:file "_package_FollowAction" :depends-on ("_package"))
    (:file "FollowActionFeedback" :depends-on ("_package_FollowActionFeedback"))
    (:file "_package_FollowActionFeedback" :depends-on ("_package"))
    (:file "FollowActionGoal" :depends-on ("_package_FollowActionGoal"))
    (:file "_package_FollowActionGoal" :depends-on ("_package"))
    (:file "FollowActionResult" :depends-on ("_package_FollowActionResult"))
    (:file "_package_FollowActionResult" :depends-on ("_package"))
    (:file "FollowFeedback" :depends-on ("_package_FollowFeedback"))
    (:file "_package_FollowFeedback" :depends-on ("_package"))
    (:file "FollowGoal" :depends-on ("_package_FollowGoal"))
    (:file "_package_FollowGoal" :depends-on ("_package"))
    (:file "FollowResult" :depends-on ("_package_FollowResult"))
    (:file "_package_FollowResult" :depends-on ("_package"))
  ))