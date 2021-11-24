#!/bin/sh

model='facenet_model/vggface2/20180402-114759.pb'

#conda facenet
#/opt/anaconda3/envs/facenet/bin/python3 src/camera_face.py ${model} --image_size 160 --margin 32 --gpu_memory_fraction 0.5

#conda facent_mask
/opt/anaconda3/envs/mask/bin/python facenet/src/camera_facemask.py ${model} --image_size 160 --margin 32 --gpu_memory_fraction 0.5

