import socket
# import cv2
import numpy as np
import time
# Specify the IP addr and port number 
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
# TODO start
# HOST, PORT = '10.42.0.1', 12200
HOST, PORT = '127.0.0.1', 12200
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.bind ( ( HOST , PORT ) )
# TODO end

while(True):
    # Listen for any request
    # TODO start
    s.listen ( 5 ) 
    # TODO end
    print("The streaming server is running..")


    while(True):
        # Accept a new request and admit the connection
        # TODO start
        client, address = s.accept()
        print('Got connection from', address)
        # TODO end
        print(str(address)+" connected")
        vidNum = -1
        counter = 0
        qua = 1
        try:
            while (True):
                T = time.time()
                data = client.recv(1024)
                msg = data.decode().split()
                qua = int(msg[0])
                f = int(msg[1])
                qua = msg[0]
                if ( f < counter):
                    if(f == -1):
                        vidNum = counter
                    elif(f == -2):
                        vidNum +=1
                    else:
                        vidNum = f
                else:
                    print("frame does not exist")
                f = open(str(qua) + 'output'+str(vidNum)+'.mp4','rb')
                vid = f.read()
                client.send(str(len(vid)).encode())
                time.sleep(0.1)
                client.send(b"")
                client.send(vid)
                # print(currentFrame)
                # currentFrame+=1
                counter+=1
                print(str(vidNum)+"sent")
                dt = time.time()-T
                if (dt<5):
                    time.sleep(5-dt)
        except ValueError:
            print("except")
            client.close()
    client.close()
s.close()
