#!/bin/sh
model='../facenet_model/vggface2/20180402-114759.pb'

echo '何人ですか？'
read num

ARR=`seq -s ' ' $num `
for i in $ARR
do
	echo $i'人目'
	python3 camera.py
done

files="./src/data/images/*"

rm register.db

# conda activate facenet
/opt/anaconda3/envs/facenet/bin/python3 src/create_register.py ${model} ${files} --image_size 160 --margin 32 --gpu_memory_fraction 0

rm ./src/data/images/*
