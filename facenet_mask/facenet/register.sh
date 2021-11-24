#!/bin/sh

model='../facenet_model/vggface2/20180402-114759.pb'

#image1='data/images/sentaro001.jpg'
# image1='./src/data/images/sentaro001.jpg'
# image2='./src/data/images/sentaro002.jpg'
#image1='./src/data/images/kari.001.jpg'
image1='./src/data/images/iuchi.001.jpg'
file='image'

#/opt/anaconda3/envs/mask/bin/python3 src/create_register.py ${model} ${image1} ${image2} --image_size 160 --margin 32 --gpu_memory_fraction 0

/opt/anaconda3/envs/mask/bin/python3 src/create_register.py ${model} ${image1} --image_size 160 --margin 32 --gpu_memory_fraction 0
