# detect_objects

## Introduction

This is a Package that detects objects using Tensor Flow Lite. 

## Installation

### Dependencies

If you don't have a Ubiquity noetic image:

:TODO

If you already have a Ubiquity noetic image: 

Install Tensor Flow Lite:

    pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
Install ur_vision messages:

    https://github.com/UbiquityRobotics/ur_vision_msgs.git

ROS vision_msgs (currently not used):

    apt-get install  ros-noetic-vision-msgs

#### Coral TPU (optional)

Execute the following commands if you want to use a Coral TPU.

    echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install libedgetpu1-std
    sudo apt-get install python3-pycoral

If the TPU still doesn't work after executing the above commands replug it. 

After you've installed the dependencies clone this repository, and you're ready to go.

## Parameters

### Topics

#### Input topic
`input_image_topic` (string, default: "/raspicam_node/image/compressed")
image topic we subscribe to

#### Output topics
`output_image_topic` (string, default: "/detect_objects/detection_img/compressed")
image topic we publish to

    if empty: no Image/CompressedImage topic will be published

`output_bounding_box_topic` (string, default: "/detect_objects/detection_array")
Detection2DArray topic we publish to

    if empty: no Detection2DArray topic will be published

### Path parameters

`model_dir` (string, default: "$(find detect_objects)/model") 
Path to dir containing TF model files, labels, etc.

`default_model`  (string, default: "default_model.tflite")
name of TFLite model file

`tpu_model` (string, default: "tpu_model.tflite")
name of TFLite model file used for TPU

`labels` (string, default: "labels.txt")
name of class labels file

### Model parameters

`selected_classes` (string, default: "person")
select which classes to detect

    if suffix `.txt`: name of file defining which objects to detect
    if no suffix : name of objects to detect. Delimiter = `,`
    if empty : detect all detectable objects

`model_resolution` (string, default: "320x320")
input image dimensions required by the model

`camera_resolution` (string, default: "410x308")
camera resolution

`tpu` (bool, default: False)
use Coral TPU

`cores` (int, default: 4)
number of cores used by TFLite (from 1 to 4)

`detection_threshold` (float, default: 0.6)
detection threshold value (from 0 to 1)

## Run

run detect_objects using:

        roslaunch detect_objects detect_objects.launch
        
before running detect_objects you should run:

        roslaunch raspicam_node camerav2_410x308_30fps.launch 

        


