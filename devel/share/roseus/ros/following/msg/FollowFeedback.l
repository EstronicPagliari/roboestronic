;; Auto-generated. Do not edit!


(when (boundp 'following::FollowFeedback)
  (if (not (find-package "FOLLOWING"))
    (make-package "FOLLOWING"))
  (shadow 'FollowFeedback (find-package "FOLLOWING")))
(unless (find-package "FOLLOWING::FOLLOWFEEDBACK")
  (make-package "FOLLOWING::FOLLOWFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude FollowFeedback.msg.html


(defclass following::FollowFeedback
  :super ros::object
  :slots (_progress ))

(defmethod following::FollowFeedback
  (:init
   (&key
    ((:progress __progress) "")
    )
   (send-super :init)
   (setq _progress (string __progress))
   self)
  (:progress
   (&optional __progress)
   (if __progress (setq _progress __progress)) _progress)
  (:serialization-length
   ()
   (+
    ;; string _progress
    4 (length _progress)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _progress
       (write-long (length _progress) s) (princ _progress s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _progress
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _progress (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get following::FollowFeedback :md5sum-) "4e8180fd8cffb84e555b1c648b3e7287")
(setf (get following::FollowFeedback :datatype-) "following/FollowFeedback")
(setf (get following::FollowFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#feedback
string progress


")



(provide :following/FollowFeedback "4e8180fd8cffb84e555b1c648b3e7287")


