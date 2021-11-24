import cv2
import os

input = '.mp4'
input_g = '.mp4'

def save_all_frames(input, input_g , basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    cap_g = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
        while True:
            ret_g,frame_f = cap_g.read()
        
        if not ret:
            break

save_all_frames(input, input_g, 'frame')
