#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import cv2
import time
import numpy as np
HOST = '127.0.0.1'
PORT = 12200

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
vidNum = 0
while True:
    # if vidNum > 10:
    #     break
    # s.send(cmd.encode())
    rlen = s.recv(1024)
    print("rlen = ", rlen)
    shape = int(rlen.decode())
    vid = ''.encode()
    while(shape>0):
        data = s.recv(shape)
        vid += data
        shape -= len(data)

    print('image size = ', len(vid))
    f = open("op"+str(vidNum)+".mp4", 'wb')
    f.write(vid)
    vidNum+=1
s.close()
cv2.destroyAllWindows()
