import os
import cv2
import time
from skimage.transform import resize
import numpy as np
 
# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.
length = 10
 
# Create an output movie file (make sure resolution/frame rate matches input video!)
#fourcc = cv2.VideoWriter_fourcc(*'MP4V')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# output_movie_1 = cv2.VideoWriter('output.mp4', fourcc, length, (320, 240))
# output_movie_2 = cv2.VideoWriter('output.mp4', fourcc, length, (640, 480))

cap = cv2.VideoCapture(0)
cap.open(0)
##########################
cap.set(3,640) # width
cap.set(4,480) # length
##########################

nT, oT = 0, 0
vidNum = 0
while(True):
    if vidNum > 20:
        break
    output_movie_1 = cv2.VideoWriter('1output'+str(vidNum)+'.mp4', fourcc, length, (320, 240))
    output_movie_2 = cv2.VideoWriter('0output'+str(vidNum)+'.mp4', fourcc, length, (640, 480))
    frame_number = 0
    # frameBuffer = []
    oT = nT
    nT = time.time()
    print(nT-oT)
    while (True):
        fT = time.time()
        ret, frame = cap.read()
        if ret == False:
            print('f')
            continue

        output_movie_2.write(frame)

        frame = resize(frame, (240 , 320))
        cv2.imshow('frame' , frame)
        frame = 255 * frame
        frame = frame.astype(np.uint8)

        output_movie_1.write(frame)


        '''rescaled_image = 255 * resized_image
        # Convert to integer data type pixels.
        final_image = rescaled_image.astype(np.uint8)
        # show resized image
        img = Image.fromarray(final_image, 'RGB')
        # Grab a single frame of video'''
        
        frame_number += 1
        if frame_number == 50:
            break
        dt = time.time()-fT
        if (dt<0.1):
            time.sleep(0.1-dt)
            # print("!!!<0.1")


    # print(time.time() - T)
    # for frame in frameBuffer:
    #     cv2.imshow('frame', frame)
    #     # print(f, end = ' ')
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #     # Write the resulting image to the output video file
    #     output_movie.write(frame)
    print("end write of"+ str(vidNum))
    # f = open("vidnum.txt", 'w')
    # f.write(str(vidNum))
    vidNum+=1
    dt = time.time()-nT
    if (dt<5):
        time.sleep(5-dt-0.004)
# All done!

cv2.destroyAllWindows()