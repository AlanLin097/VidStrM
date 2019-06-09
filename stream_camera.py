import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
currentFrame = 0
frameBuffer = []

while(True):
    if currentFrame == 50:
        break
    ret, frame = cap.read()
    if ret == False:
        print('f')
        continue
    frameBuffer.append(frame)
    currentFrame+=1
    time.sleep(0.1) 
fourcc = cv2.VideoWriter_fourcc('m','p','v','4')
outputMovie = cv2.VideoWriter('output_test01.mp4', fourcc, 10, (640,480))
print(frameBuffer[0])
# for f in range(frameBuffer):
#     output_movie.write("./")  
#     print(f)

cv2.destroyAllWindows()  
