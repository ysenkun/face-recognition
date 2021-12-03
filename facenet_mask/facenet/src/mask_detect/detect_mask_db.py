import sys
import pprint
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
#from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
import os
import time

def mask_image(img,model):
    print("[INFO] loading face detector model...")
    prototxtPath = "src/mask_detect/face_detector/deploy.prototxt"
    weightsPath = "src/mask_detect/face_detector/res10_300x300_ssd_iter_140000.caffemodel"
    net = cv2.dnn.readNet(prototxtPath, weightsPath)

    # load the face mask detector model from disk
    print("[INFO] loading face mask detector model...")

    image = img

    orig = image.copy()
    (h, w) = image.shape[:2]

    # construct a blob from the image
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
	(104.0, 177.0, 123.0))
    
    # pass the blob through the network and obtain the face detections
    print("[INFO] computing face detections...")
    net.setInput(blob)
    detections = net.forward()
    
    # loop over the detections
    for i in range(0, detections.shape[2]):

        confidence = detections[0, 0, i, 2]
	# filter out weak detections by ensuring the confidence is
	# greater than the minimum confidence
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for
            # the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            return box
