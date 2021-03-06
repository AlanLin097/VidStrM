#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import cv2
import time
import numpy as np
import os
import sys
import termios
HOST = '127.0.0.1'
PORT = 12200

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

old_settings = None
old_settings = termios.tcgetattr(sys.stdin)
new_settings = termios.tcgetattr(sys.stdin)
new_settings[3]= (new_settings[3] & ~(termios.ECHO | termios.ICANON))
new_settings[6][termios.VMIN] = 0
new_settings[6][termios.VTIME] = 0
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_settings)

# vidNum = 0
while True:
    q = 1
    f = -2
    ch_set = ''
    ch = os.read(sys.stdin.fileno(),1)
    while((ch!=None) and len(ch)>0):
        ch_set += chr(ch[0])
        ch = os.read(sys.stdin.fileno(),1)
    print(ch_set)
    if len(ch_set) > 0:
        if (ch_set[0] == 'q'):
            q = int(ch_set[2])
        elif(ch_set[0]=='f'):
            f = int(ch_set[2])
        elif(ch_set[0] == 'l'):
            f = -1
    # if ch_set
    # if vidNum > 10:
    #     break
    # s.send(cmd.encode())
    T = time.time()
    s.send((str(q)+' '+str(f)).encode())
    rlen = s.recv(1024)
    print("rlen = ", rlen)
    shape = int(rlen.decode())
    vid = ''.encode()
    while(shape>0):
        data = s.recv(shape)
        vid += data
        shape -= len(data)

    print('image size = ', len(vid))
    # f = open("op"+str(vidNum)+".mp4", 'wb')
    try:
        os.rename("TEMP.mp4", "op0.mp4")
    except:
        print("first")
    f = open("TEMP.mp4",'wb')
    f.write(vid)
    # vidNum+=1
    dt = time.time() - T
    print(dt)
s.close()
cv2.destroyAllWindows()
