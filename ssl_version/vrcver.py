#!/usr/bin/env python
# coding: utf-8


import socket
import cv2
import time
import numpy as np
import os
import sys
import termios
from skimage.transform import resize
import ssl
HOST = '127.0.0.1'
PORT = 12200

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
# 生成SSL上下文
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# 加载信任根证书
context.load_verify_locations('./cert.pem')

old_settings = None
old_settings = termios.tcgetattr(sys.stdin)
new_settings = termios.tcgetattr(sys.stdin)
new_settings[3]= (new_settings[3] & ~(termios.ECHO | termios.ICANON))
new_settings[6][termios.VMIN] = 0
new_settings[6][termios.VTIME] = 0
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_settings)
q = 1
a = 0
with context.wrap_socket(sock, server_hostname='final_project') as s:
    # vidNum = 0
    while True:
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
            elif(ch_set[0] == 'a'): #full size
                a = 1
            elif(ch_set[0] == 'n'): #normal size
                a = 0
        
        if a == 1 and q == 0:
            width = 960
            height = 720
        elif a == 0:
            width = 640
            height = 480

        # if ch_set
        # if vidNum > 10:
        #     break
        # s.send(cmd.encode())
        
        s.send((str(q)+' '+str(f)).encode())
        rlen = s.recv(1024)
        print("rlen = ", rlen)
        shape = int(rlen.decode())
        vid = ''.encode()
        while(shape>0):
            data = s.recv(shape)
            vid += data
            shape -= len(data)
        T = time.time()
        print('image size = ', len(vid))
        # f = open("op"+str(vidNum)+".mp4", 'wb')
        try:
            os.rename("TEMP.mp4", "op0.mp4")
        except:
            print("first")
        f = open("TEMP1.mp4",'wb')
        f.write(vid)
        f.close()

        videoCapture = cv2.VideoCapture('./TEMP1.mp4')
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        output_movie_2 = cv2.VideoWriter('./TEMP.mp4', fourcc, 10, (width, height))
        success, frame = videoCapture.read()
        while success :
            frame = resize(frame, (height , width))
            frame = 255 * frame
            frame = frame.astype(np.uint8)
            print(frame.shape)
            print(type(frame[0][0][0]))
            output_movie_2.write(frame)
            cv2.imshow('windows', frame)
            #output_movie_2.write(frame)
            success, frame = videoCapture.read()
            #success, frame = videoCapture.read()
        #vidNum+=1
        dt = time.time() - T
        print(dt)
s.close()
cv2.destroyAllWindows()