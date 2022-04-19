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
Modify _{YOUR_APPROPRIATE_PATH}/facenet/bin/python_ to appropriate file path.  
You need to modify 1 location in facenet_mask/camera.sh, and 2 locations in face_recognition/facenet_mask/facenet/create.sh.

## Run

### Registering Face Detection Targets
The _create.sh_ would first prompt the user to define how many faces to be registered. Then it would take a photo for each user. Finally, it would make a database for the detection.
```bash
$ cd facenet_mask/facenet
```
```bash
$ bash create.sh
```
In order to reset the registered faces, use:
```bash
$ rm register.db
```

### Face Recognition
The following command would perform a face recognition based on the faces registered.
```bash
$ cd facenet_mask
```

```bash
$ bash camera.sh
```
![sample](https://user-images.githubusercontent.com/82140392/163969654-e555e41f-aa25-42d6-9c9e-c1fc5bc79a09.gif)
