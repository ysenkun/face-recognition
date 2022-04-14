#!/bin/sh

model='../facenet_model/vggface2/20180402-114759.pb'
image1='./src/data/images/name.001.jpg'

/opt/anaconda3/envs/mask/bin/python3 src/create_register.py ${model} ${image1} --image_size 160 --margin 32 --gpu_memory_fraction 0
