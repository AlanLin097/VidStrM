import socket
import cv2
import numpy as np
# Specify the IP addr and port number 
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
# TODO start
HOST, PORT = '127.0.0.1', 12200
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.bind ( ( HOST , PORT ) )
s.listen ( 5 ) 
# TODO end

while(True):
    # Listen for any request
    # TODO start
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.bind ( ( HOST , PORT ) )
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
        cap = cv2.VideoCapture(0)

        currentFrame = 0
        try:
            while (True):
                if currentFrame == 200:
                    break
                ret, frame = cap.read()
                if ret == False:
                    print('f')
                    continue
                #data = 
                frame = cv2.flip(frame,1)
                print(frame.shape)
                print(type(frame))
                print(type(frame[0,0,0]))
                print(len(frame[0,0,:].tostring()))
                # client.send(b"Welcom to the calculator server. Input your problem ?\n")
                frame = frame.flatten()
                bstr = frame.tostring()
                print(len(bstr))
                fimg = np.fromstring(bstr, np.uint8)
                print(fimg.shape)
                client.send(frame.tostring())
                print(currentFrame)
                currentFrame+=1

                # Recieve the data from the client and send the answer back to the client
                # Ask if the client want to terminate the process
                # Terminate the process or continue
                # TODO start
                #s.connect((HOST,PORT))
                # data = client.recv(1024)
                # print(data)
                # parse = data.decode().split()
                # ans = 0
                # invalid = False
                # print("calculating")
                # if len(parse) == 3:
                #     if parse[1] == '+':
                #         ans = int(parse[0])+int(parse[2])
                #     elif parse[1] == '-':
                #         ans = int(parse[0])-int(parse[2])
                #     elif parse[1] == '*':
                #         ans = int(parse[0])*int(parse[2])
                #     elif parse[1] == '/':
                #         ans = int(parse[0])*1.0/int(parse[2])
                #     else:
                #         invalid = True
                # else:
                #     invalid = True
                # print("calculated")
                # if invalid == True:
                #     client.send("Invalid input!\nAny other question?(Y/N)\n".encode())
                # else:
                #     client.send(("ANS = "+str(ans)+'\n'+"Any other question?(Y/N)\n").encode())
                # print("ans = ", ans)
                # data = client.recv(1024)
                # #client.send("server received you message.".encode())
                # while True:
                #     if ((data.decode() =='N') | (data.decode() =='n')) :
                #         client.send("terminate".encode())
                #         break
                #     elif ((data.decode() =='Y') | (data.decode() =='y')) :
                #         break
                #     else:
                #         client.send("Invalid input!\nAny other question?(Y/N)\n".encode())
                #         data = client.recv(1024)
                # if ((data.decode() =='N') | (data.decode() =='n')) :
                #     break
                # # TODO end
        except ValueError:
            print("except")
            client.close()
    client.close()
s.close()
