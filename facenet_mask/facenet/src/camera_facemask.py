from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from scipy import misc
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from tensorflow.keras.models import load_model 
import numpy as np
import sys
import os
import copy
import argparse
import facenet
import sqlite3
import cv2
from mask_detect import detect_mask
import asyncio

cap = cv2.VideoCapture(1)

dbname = 'facenet/register.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

select_sql = 'SELECT * FROM persons'

def main(args):
    with tf.Graph().as_default():
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=args.gpu_memory_fraction)
        sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
        with tf.Session() as sess:

            # Load the model for FaceNet
            facenet.load_model(args.model)

            # Get input and output tensors
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

            # Load the model for mask detect
            model = load_model("facenet/src/mask_detect/mask_detector.model")
            while True:
                # tick = cv2.getTickCount()
                ret, frame = cap.read()
                try:
                    images_list,box_list = load_and_align_data(frame, args.image_size, args.margin,model)

                except:
                    continue
                # Run forward pass to calculate embeddings

                
                for num,images in enumerate(images_list):
                    feed_dict = { images_placeholder: images, phase_train_placeholder:False }
                    emb = sess.run(embeddings, feed_dict=feed_dict)
                    detect_name = detect_f(emb)
                    # cv2.FONT_HERSHEY_PLAIN

                    cv2.putText(frame,detect_name,
                                (int(box_list[num][0]+30), int(box_list[num][1])-30),cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                # Show fps
                # fps = cv2.getTickFrequency() / (cv2.getTickCount() - tick)
                # cv2.putText(frame, "FPS:{} ".format(int(fps)),
                #            (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2, cv2.LINE_AA)

                cv2.imshow('cap',frame)
                if cv2.waitKey(1) == ord('q'):
                    break

def detect_f(emb):

    for row in cur.execute(select_sql):
        name = row[0]
        data = np.array(eval(row[1]))
        dis = np.sqrt(np.sum(np.square(np.subtract(data,emb[0,:]))))
        if dis < 0.65:
            #cur.close()
            #conn.close()
            return name
    #cur.close()
    #conn.close()
    return 'unknown'

            
def load_and_align_data(frame, image_size, margin, model):
    img_list = []
    img = frame
    img_size = np.asarray(img.shape)[0:2]
    box_list = detect_mask.mask_image(img, model)
    images_list = []
    for det in box_list:
        bb = np.zeros(4, dtype=np.int32)
        bb[0] = np.maximum(det[0]-margin/2, 0)
        bb[1] = np.maximum(det[1]-margin/2, 0)
        bb[2] = np.minimum(det[2]+margin/2, img_size[1])
        bb[3] = np.minimum(det[3]+margin/2, img_size[0])
        cropped = img[bb[1]:bb[3],bb[0]:bb[2],:]
        aligned = misc.imresize(cropped, (image_size, image_size), interp='bilinear')
        prewhitened = facenet.prewhiten(aligned)
        img_list.append(prewhitened)
        images = np.stack(img_list)
        images_list.append(images)
        img_list.clear()
    return images_list,box_list

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('model', type=str, 
        help='Could be either a directory containing the meta_file and ckpt_file or a model protobuf (.pb) file')
    parser.add_argument('--image_size', type=int,
        help='Image size (height, width) in pixels.', default=160)
    parser.add_argument('--margin', type=int,
        help='Margin for the crop around the bounding box (height, width) in pixels.', default=44)
    parser.add_argument('--gpu_memory_fraction', type=float,
        help='Upper bound on the amount of GPU memory that will be used by the process.', default=1.0)
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
