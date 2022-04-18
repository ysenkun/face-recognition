#!/bin/sh

model='facenet_model/vggface2/20180402-114759.pb'

#conda activate facenet
{YOUR_APPROPRIATE_PATH}/facenet/bin/python facenet/src/camera_facemask.py ${model} --image_size 160 --margin 32 --gpu_memory_fraction 0.5


