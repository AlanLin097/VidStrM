import cv2
vidNum = 0
while(True):
    try:
        videoCapture = cv2.VideoCapture('./op'+str(vidNum)+'.mp4')
    except:
        print("VidStrm Error: network error!!")

    #获得码率及尺寸
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    
    
    #读帧
    success, frame = videoCapture.read()
    while success :
        cv2.imshow('windows', frame) #显示
        cv2.waitKey(int(1000/int(fps))) #延迟
        success, frame = videoCapture.read() #获取下一帧
    
    videoCapture.release()
    vidNum+=1