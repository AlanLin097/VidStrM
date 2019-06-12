import cv2
import os
import time
from skimage.transform import resize
import numpy as np

vidNum = 0
while(True):
    try:
        os.rename("./op0.mp4", "./op1.mp4")
    except:
        print("first")
    videoCapture = cv2.VideoCapture('./op1.mp4')
    if videoCapture == -1:
        print("VidStrm Error: network error!!")
        time.sleep(0.5)
        continue

    #获得码率及尺寸
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print(str(size[0]) + ' ' + str(size[1]))
    
    #读帧
    success, frame = videoCapture.read()
    while success :
        cv2.imshow('windows', frame) #显示
        cv2.waitKey(int(1000/int(fps))) #延迟
        success, frame = videoCapture.read() #获取下一帧
    
    videoCapture.release()
    os.remove('./op1.mp4')
vidNum+=1