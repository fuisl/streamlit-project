"""
DNN model for dog cat classification
"""

import cv2
import numpy as np

MODEL = "models/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "models/MobileNetSSD_deploy.prototxt.txt"


def process_img(img):
    """
    Preprocess the image for the DNN model
    """
    blob = cv2.dnn.blobFromImage(
        cv2.resize(img, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections

def annotate_img(img, detections, confidence_threshold=0.5):
    """
    Annotate the image with the detections
    """
    (h, w) = img.shape[:2]
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * \
                np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(img, (startX, startY), (endX, endY), 70, 2)
    return img