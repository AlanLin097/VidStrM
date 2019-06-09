import os
import cv2
import time
 
# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.
length = 20
 
# Create an output movie file (make sure resolution/frame rate matches input video!)
#fourcc = cv2.VideoWriter_fourcc(*'MP4V')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
output_movie = cv2.VideoWriter('output.mp4', fourcc, length, (320, 240))

cap = cv2.VideoCapture(0)
cap.open(0)
##########################
cap.set(3,320) # width
cap.set(4,240) # length
##########################


vidNum = 0
while(True):
    if vidNum > 10:
        break
    output_movie = cv2.VideoWriter('output'+str(vidNum)+'.mp4', fourcc, length, (320, 240))
    frame_number = 0
    frameBuffer = []
    T = time.time()
    while (True):
        if frame_number == 100:
            break
        ret, frame = cap.read()
        if ret == False:
            print('f')
            continue
        frameBuffer.append(frame)

        # Grab a single frame of video
        
        frame_number += 1


    print(time.time() - T)
    for frame in frameBuffer:
        cv2.imshow('frame', frame)
        # print(f, end = ' ')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Write the resulting image to the output video file
        output_movie.write(frame)
    print("end write of"+ str(vidNum))

    vidNum+=1
# All done!

cv2.destroyAllWindows()
