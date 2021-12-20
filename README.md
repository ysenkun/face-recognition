# yurihs_demo

## Introduction
This repository is a minimal system that uses FaceNet for face recognition.
### :raising_hand: Cited by:
1. https://github.com/davidsandberg/facenet

## Before you run the tracker
The Python environment is Python==3.7.0.
```bash
cd facenet_mask
pip install -r requirements.txt
```
### Pre-trained models
| Model name      | LFW accuracy | Training dataset | Architecture |
|-----------------|--------------|------------------|-------------|
| [20180408-102900](https://drive.google.com/open?id=1R77HmFADxe87GmoLwzfgMu_HY0IhcyBz) | 0.9905        | CASIA-WebFace    | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |
| [20180402-114759](https://drive.google.com/open?id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-) | 0.9965        | VGGFace2      | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |

* NOTE: If you use any of the models, please do not forget to give proper credit to those providing the training dataset as well.
* Where to save the model:
```bash
cd facenet_mask
mkdir facenet_model
```

## Run

### Create DB(register)
To face recognition, register the face with the following command.When the following command is executed, the number of registered faces and their names will be entered and the image will be taken.
```bash
cd yurihs_demo/facenet_mask/facenet
```

※key(A)でカメラのシャッターを切る
```bash
bash create.sh
```

### Face Recognition
It compares the face image with the one registered earlier and face recognition.
```bash
cd yurihs_demo/facenet_mask`
```

```bash
bash camera.shp
```
