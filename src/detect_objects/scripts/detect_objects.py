#!/usr/bin/python3

from tflite_runtime.interpreter import Interpreter
from ur_vision_msgs.msg import *
import os
import cv2
import numpy as np
from dataclasses import dataclass
from typing import List


@dataclass
class Rect:
    x_min: float
    x_max: float
    y_min: float
    y_max: float


class Detect_objects:
    def __init__(self,
                 model_dir: str = 'src/detect_objects/model',
                 default_model: str = 'default_model.tflite',
                 tpu_model: str = 'tpu_model.tflite',
                 labels: str = 'labels.txt',
                 selected_classes: str = '',
                 model_resolution: str = '320x320',
                 frame_w: int = 403,
                 frame_h: int = 308,
                 tpu: bool = False,
                 cores: int = 4,
                 detection_threshold: float = 0.6):

        if detection_threshold < 0 or detection_threshold > 1:
            raise ValueError("Wrong detection threshold! Got value: ", detection_threshold,
                             " . The value should be between 0 and 1")
        else:
            self.detection_threshold: float = detection_threshold

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



        try:
            frame_w: int = int(frame_w)
            frame_h: int = int(frame_h)
        except ValueError:
            raise ValueError("Camera resolution error! Values can't be converted to integers. Width: ", w,
                             " Height: ", h)

        if frame_w < 0 or frame_h < 0:
            raise ValueError("Camera resolution error! Got: width: ", frame_w, " and height: ", frame_h,
                             " . Both values should be positive!")

        else:
            self.frame_w: int = frame_w
            self.frame_h: int = frame_h

        print(os.path.exists(model_dir))
        if os.path.exists(model_dir):
            if os.path.exists(os.path.join(model_dir, default_model)):
                self.default_model_path: str = os.path.join(model_dir, default_model)
            else:
                raise FileNotFoundError("default_model_path not valid")

            if os.path.exists(os.path.join(model_dir, tpu_model)):
                self.tpu_model_path: str = os.path.join(model_dir, tpu_model)
            else:
                raise FileNotFoundError("tpu_model_path not valid")

            if os.path.exists(os.path.join(model_dir, labels)):
                self.labels_path: str = os.path.join(model_dir, labels)
                with open(self.labels_path, 'r') as f:
                    self.labels: List[str] = [line.strip() for line in f.readlines()]
            else:
                raise FileNotFoundError("labels_path not valid")

            if len(selected_classes) == 0:
                self.selected_classes: List[str] = self.labels
            elif os.path.exists(os.path.join(model_dir, selected_classes)):
                with open(os.path.join(model_dir, selected_classes), 'r') as f:
                    self.selected_classes: List[str] = [line.strip() for line in f.readlines()]
            else:
                self.selected_classes: List[str] = selected_classes.split(',')
                if len(selected_classes) < 1:
                    raise FileNotFoundError("selected_classes not found")



        else:
            raise NotADirectoryError("model_dir not valid")

        if cores < 1 or cores > 4:
            raise ValueError("Wrong core count! got: ", self.cores, " . select a valid core count (from 1 to 4).")
        else:
            self.cores: int = cores

        # if we use the Coral TPU
        if tpu:
            # import module needed to run on TF Lite on TPU
            from tflite_runtime.interpreter import load_delegate
            self.interpreter: Interpreter = Interpreter(
                model_path=os.path.join(model_dir, tpu_model),
                experimental_delegates=[load_delegate('libedgetpu.so.1.0')])
        else:
            self.interpreter: Interpreter = Interpreter(
                model_path=os.path.join(model_dir, default_model),
                num_threads=cores)

        self.interpreter.allocate_tensors()
        self.input_details: List[dict] = self.interpreter.get_input_details()
        self.output_details: List[dict] = self.interpreter.get_output_details()
        print(self.frame_w, self.frame_h)

 

    def __render(self, frame: np.ndarray, rect: Rect, score: float, label: str) -> np.ndarray:
        ''' Draws bounding boxes and detections scores on the input frame and returns it.
        :param frame: np.ndarray input image frame
        :param rect: Rect detected bounding box
        :param score: float detection score
        :param label: str class name of detected object
        :return: np.ndarray frame with added bounding boxes, class names and scores
        '''
        cv2.rectangle(frame, (rect.x_min, rect.y_min), (rect.x_max, rect.y_max), (0, 255, 0), 2)
        text: str = str(label) + " : " + str(int(score * 100)) + " %"
        cv2.putText(frame, text, (rect.x_min + 5, rect.y_min + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0),
                    2)
        cv2.rectangle(frame, (rect.x_min, rect.y_min), (rect.x_max, rect.y_max), (10, 255, 0), 2)
        return frame

    def detect(self, frame: np.ndarray) -> [np.ndarray, DetectedObjectArray2D]:
        ''' Inputs the frame to the neural network, which returns bounding boxes, scores and class names. Returns the bounding boxes
        and the frame with with drawn on bounding boxes
        :param frame: np.ndarray input frame
        :return: np.ndarray output frame with drawn on bounding boxes and corresponding class names and scores
        :return: Detection2DArray output bounding boxes, with class labels and scores
        '''
        frame: np.ndarray = frame.copy()
        frame_rgb: np.ndarray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized: np.ndarray = cv2.resize(frame_rgb, (self.model_w, self.model_h))
        input_data: np.ndarray = np.expand_dims(frame_resized, axis=0)

        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()

        boxes: np.ndarray = self.interpreter.get_tensor(self.output_details[0]['index'])[0]  # Bounding box coordinates of detected objects
        classes: np.ndarray = self.interpreter.get_tensor(self.output_details[1]['index'])[0]  # Class index of detected objects
        scores: np.ndarray = self.interpreter.get_tensor(self.output_details[2]['index'])[0]  # Confidence of detected objects

        boxes_nms=[]
        scores_nms=[]
        classes_nms=[]

        #select only selected classes to apply non maxima suppression
        for i in range(len(scores)):
            if self.labels[int(classes[i])] in self.selected_classes:
                boxes_nms.append(boxes[i,:])
                scores_nms.append(scores[i])
                classes_nms.append(classes[i])

        #apply non maxima suppression
        #indexes=nms.boxes(boxes_nms,scores_nms)
        #indexes = nms.fast.nms(boxes_nms, scores_nms)
        detection2DArray: DetectedObjectArray2D = DetectedObjectArray2D()
        indexes=range(len(boxes_nms))
        for i in indexes:
            if ((scores_nms[i] > self.detection_threshold)  and (scores_nms[i] <= 1.0)):
                detection2D: DetectedObject2D = DetectedObject2D()

                #object_hypothesis: ObjectHypothesisWithPose = ObjectHypothesisWithPose()
                #object_hypothesis.id = int(classes[i]) # some version might require string :TODO check versions
                #print(self.labels[int(classes_nms[i])])
                detection2D.class_name = self.labels[int(classes_nms[i])]
                detection2D.score = scores[i]

                y_min: int = int(max(1, (boxes_nms[i][0] * self.frame_h)))
                x_min: int = int(max(1, (boxes_nms[i][1] * self.frame_w)))
                y_max: int = int(min(self.frame_h, (boxes_nms[i][2] * self.frame_h)))
                x_max: int = int(min(self.frame_w, (boxes_nms[i][3] * self.frame_w)))

                rect: Rect = Rect(x_min, x_max, y_min, y_max)

                detection2D.bbox = self.__rect_to_BoundingBox2D(rect)

                detection2DArray.detected_objects.append(detection2D)

                frame: np.ndarray = self.__render(frame, rect, scores_nms[i], self.labels[int(classes_nms[i])])

        return frame, detection2DArray

    def __rect_to_BoundingBox2D(self, rect: Rect) -> BoundingBox2D:
        ''' Converts input Rect to BoundingBox2D

        :param rect: Rect input of type Rect
        :return: BoundingBox2D output of type BoundingBox2D
        '''
        bbox: BoundingBox2D = BoundingBox2D()
        bbox.w = rect.x_max - rect.x_min
        bbox.h = rect.y_max - rect.y_min
        bbox.center.x = bbox.w / 2 + rect.x_min
        bbox.center.y = bbox.h / 2 + rect.y_min
        bbox.center.theta = 0

        return bbox
