#!/usr/bin/python3

import rospy
from rospy import Publisher
import numpy as np
from ur_vision_msgs.msg import *
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CompressedImage, Image
from detect_objects import Detect_objects
from typing import Union


class Detection_node:
    def __init__(self,
                 selected_classes: str,
                 camera_resolution: str,
                 IOU_threshold: float,
                 input_image_topic: str = '/raspicam_node/image/compressed',
                 input_BB_topic: str = '/detect_objects/detection_array',
                 output_image_topic: str = 'track/image/compressed',
                 output_BB_topic: str = 'track/BB',
                 tracker: str = 'medianflow',
                 ):

        self.tracking: SingleObjectTracking = SingleObjectTracking(model_dir,
                                                             default_model,
                                                             tpu_model,
                                                             labels,
                                                             selected_classes,
                                                             model_resolution,
                                                             camera_resolution,
                                                             tpu,
                                                             cores,
                                                             detection_threshold)
        # initialize cvBridge
        self.bridge: CvBridge = CvBridge()
        self.input_image_topic: str = input_image_topic
        self.output_image_topic: str = output_image_topic
        self.output_bounding_box_topic: str = output_bounding_box_topic

        # Input parameter checks
        if len(camera_resolution.split('x')) == 2:
            w, h = camera_resolution.split('x')

            try:
                w: int = int(w)
                h: int = int(h)
            except ValueError:
                raise ValueError("Camera resolution error! Values can't be converted to integers. Width: ", w,
                                 " Height: ", h)

            if w < 0 or h < 0:
                raise ValueError("Camera resolution error! Got: width: ", w, " and height: ", h,
                                 " . Both values should be positive!")

            else:
                self.frame_w: int = w
                self.frame_h: int = h
        else:
            raise ValueError("Camera resolution error! Got: ", camera_resolution, " . But should be (width)x(height)")

        if len(model_resolution.split('x')) == 2:
            w, h = model_resolution.split('x')

            try:
                w: int = int(w)
                h: int = int(h)
            except ValueError:
                raise ValueError("Model resolution error! Values can't be converted to integers. Width: ", w,
                                 " Height: ", h)

            if w < 0 or h < 0:
                raise ValueError("Model resolution error! Got: width: ", w, " and height: ", h,
                                 " . Both values should be positive!")

            else:
                self.model_w: int = w
                self.model_h: int = h
        else:
            raise ValueError("Model resolution error! Got: ", model_resolution, " . But should be (width)x(height)")

        # if bounding box topic is empty don't publish it
        if len(self.output_bounding_box_topic) > 0:
            self.bounding_box_publisher: Publisher = rospy.Publisher(output_bounding_box_topic,
                                                                                  DetectedObjectArray2D, queue_size=1)

        # if image topic is empty don't publish it
        if len(self.output_image_topic) > 0:
            if "compressed" in self.output_image_topic:
                self.image_publisher: Publisher = rospy.Publisher(output_image_topic, CompressedImage,
                                                                               queue_size=1)
            else:
                self.image_publisher: Publisher = rospy.Publisher(output_image_topic, Image, queue_size=1)

    def run(self):
        rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.tracking.tracking_step, queue_size=1,
                         buff_size=(3 * 8 * self.frame_w * self.frame_h + 500))
        rospy.Subscriber("/detect_objects/detection_array", DetectedObjectArray2D, self.tracking.detection_step,
                         queue_size=1)
        rospy.spin()

    def __callback(self, msg: Union[Image, CompressedImage]):
        '''Function called when the Subscriber receives a new frame. Converts the input message to np.ndarray (cv.Image) calls
        the object detection function and publishes the results

        :param msg: [Image or CompressedImage] Subscribed image frame
        '''

            frame: np.ndarray = self.bridge.compressed_imgmsg_to_cv2(msg)
            frame, DetectedObjectArray2D = self.detect_objects.detect(frame)
            msg: CompressedImage = self.bridge.cv2_to_compressed_imgmsg(frame)
            if len(self.output_bounding_box_topic) > 0:
                self.bounding_box_publisher.publish(DetectedObjectArray2D)
            if len(self.output_image_topic) > 0:
                self.image_publisher.publish(msg)


def main():
    rospy.init_node('detect_objects', anonymous=False)

    # read parameters from the .launch file
    # topics
    input_image_topic: str = rospy.get_param("~input_image_topic")  # image topic we subscribe to
    output_image_topic: str = rospy.get_param("~output_image_topic")  # image topic we publish to
    output_bounding_box_topic: str = rospy.get_param(
        "~output_bounding_box_topic")  # Detection2DArray topic we publish to

    # paths and files
    model_dir: str = rospy.get_param("~model_dir")  # path to dir containing model files, labels, etc.
    default_model: str = rospy.get_param("~default_model")  # name of TFLite model file
    tpu_model: str = rospy.get_param("~tpu_model")  # name of TFLite model file used for TPU
    labels: str = rospy.get_param("~labels")  # name of labels file
    selected_classes: str = rospy.get_param("~selected_classes")  # name of file defining which objects to track

    # model parameters
    model_resolution: str = rospy.get_param("~model_resolution")  # input image dimensions required by the model
    camera_resolution: str = rospy.get_param("~camera_resolution")  # camera resolution
    tpu: bool = rospy.get_param("~tpu")  # use Coral TPU "False" or "True"
    cores: int = rospy.get_param("~cores")  # number of cores used by TFLite
    detection_threshold: float = rospy.get_param("~detection_threshold")  # detection threshold value (from 0 to 1)

    # initialize Detection_node using parameters from the launch file
    detection_node: Detection_node = Detection_node(model_dir,
                                                    default_model,
                                                    tpu_model,
                                                    labels,
                                                    selected_classes,
                                                    model_resolution,
                                                    camera_resolution,
                                                    tpu,
                                                    cores,
                                                    detection_threshold,
                                                    input_image_topic,
                                                    output_image_topic,
                                                    output_bounding_box_topic)
    # run the detection node
    detection_node.run()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
