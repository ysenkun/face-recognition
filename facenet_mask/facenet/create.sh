#!/bin/sh
model='../facenet_model/vggface2/20180402-114759.pb'

for i in {1..3}
do
	echo $i
	python3 camera_cv.py
done

files="./src/data/images/*"
array=($files)

image1=${array[0]}
image2=${array[1]}
image3=${array[2]}

rm register.db

/opt/anaconda3/envs/mask/bin/python3 src/create_register.py ${model} ${image1} ${image2} ${image3} --image_size 160 --margin 32 --gpu_memory_fraction 0

rm ./src/data/images/*
