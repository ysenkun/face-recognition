# Face Recognition with FaceNet

## Introduction
This repository is a face recognition system based on FaceNet.
### :raising_hand: Reference:
1. https://github.com/davidsandberg/facenet

## Seting Up Environment
The Python environment is python==3.7.0
```bash
$ conda create -n facenet python==3.7.0
$ conda activate facenet
```
```bash
$ git clone https://github.com/ysenkun/face_recognition.git
```
```bash
$ cd facenet_mask
```
```bash
$ pip3 install -r requirements.txt
```
```bash
$ pip3 install numpy==1.16.1
```
### Pre-trained Models(FaceNet)
| Model name      | LFW accuracy | Training dataset | Architecture |
|-----------------|--------------|------------------|-------------|
| [20180408-102900](https://drive.google.com/open?id=1R77HmFADxe87GmoLwzfgMu_HY0IhcyBz) | 0.9905        | CASIA-WebFace    | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |
| [20180402-114759](https://drive.google.com/open?id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-) | 0.9965        | VGGFace2      | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |

* NOTE: If you use any of the models, please do not forget to give proper credits to those providing the training datasets as well.
* Where to save the model:
```bash
$ cd facenet_mask
```
```bash
$ mkdir facenet_model
```
Download the vggface2 model and rename the folder to vggface2
```bash
$ mv ~/Downloads/20180402-114759 vggface2
```
```bash
$ mv vggface2 facenet_model/
```

### Pre-trained Models (For face detection)
After downloading [mask_detector.model](https://drive.google.com/file/d/1DdaF3eRnlbv2ssvsJhHqlGQTnlhqK2wi/view?usp=sharing), save it in the following directory
```bash
$ mv mask_detector.model facenet_mask/facenet/src/mask_detect
```
### :raising_hand: Reference:
1. https://github.com/chandrikadeb7/Face-Mask-Detection

## Modifying Shell Script
Fill out the Python virtual environment in the following shell script.  
e.g. {YOUR_APPROPRIATE_PATH}/facenet/bin/python
* facenet_mask/camera.sh
* face_recognition/facenet_mask/facenet/create.sh

## Run

### Creating DB (register)
To face recognition, register your face with the following command.When the following command is executed, the number of registered faces and their names will be entered and the image will be taken.
```bash
$ cd facenet_mask/facenet
```
※A on the keyboard to release the shutter (camera)
```bash
$ bash create.sh
```

### Face Recognition
It compares the face image with the one registered earlier and face recognition.
```bash
$ cd facenet_mask
```

```bash
$ bash camera.sh
```
