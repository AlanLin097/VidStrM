#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import cv2
import time
import numpy as np
HOST = '10.42.0.1'
PORT = 12200

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
#print(data.decode())
f = 0
while True:
    # s.send(cmd.encode())
    print("recved:")
    shape = 1024
    # if f!=0:
    #     while(shape>0):
    #         data = s.recv(480*640*3)
    # #cv2.imshow('frame',data)
    #         #print(len(data))
    #         #print(type(data))
    # #data.decode()
    #         image += data
    #         #print(data.decode('utf-8'))
    #         shape -= len(data)
    image = s.recv(shape)
    fimg = np.fromstring(image, np.uint8)
    #fimg.resize((5,1))
    print('image size = ', len(fimg))
    print(fimg)
    # npimg = np.zeros(shape,dtype = np.uint8)
    # try:
    #     npimg = np.fromstring(image, np.uint8)
    # except:
    #     print('invalid form')
    # npimg.resize(480,640,3)
    # print(npimg.shape)
    # cv2.imshow('img', npimg) 
    #print(npimg)
    #print(type(image.split()))
    #print(len(image.split()))
    print(f)
    #print(data)
    if (len(image) != 0):
        f+=1
    if(len(data) == 0):
        time.sleep(10)
    if(data == 0):
        time.sleep(10)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
s.close()
cv2.destroyAllWindows()
