#!/bin/sh
model='../facenet_model/vggface2/20180402-114759.pb'

echo 'How many faces to register?'
read num

ARR=`seq -s ' ' $num `
for i in $ARR
do
	echo 'Face number: ' $i
	{YOUR_APPROPRIATE_PATH}/facenet/bin/python3 camera.py
done

files="./src/data/images/*"

#If you want to rest the registered faces database, use the command bellow.
#rm register.db

# conda activate facenet
{YOUR_APPROPRIATE_PATH}/facenet/bin/python3 src/create_register.py ${model} ${files} --image_size 160 --margin 32 --gpu_memory_fraction 0

rm ./src/data/images/*
