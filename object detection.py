import numpy as np 
import matplotlib.pyplot as mtlb
import cv2 as cv
from PIL import Image as im
from datetime import datetime
import time 
from pygame import mixer

print(cv. __version__)

#reading the network
yolo = cv.dnn.readNet(r"D:\Software Engennering\yolov3.weights",r"C:\Users\Asus\Desktop\darknet-master\cfg\yolov3.cfg") 

classes = []
with open(r"C:\Users\Asus\Desktop\darknet-master\data\coco.names",'r') as f :
    classes = f.read().splitlines()

def processing(lis={}) :
    mixer.init()

    if "tvmonitor" in lis.keys():
        if (lis["tvmonitor"]> 4):
            mixer.music.load("Computer_Lab.mp3")

    elif "bench" in lis.keys():
        if (lis["bench"]> 4):
            mixer.music.load("Classroom.mp3")     
    
    elif "chair" in lis.keys():
        if (lis["chair"]> 4):
            mixer.music.load("Auditorium.mp3") 

    elif ("person" in lis.keys() and lis["person"] >= 4) :
        mixer.music.load("Crowd.mp3")
    
    elif (("car" in lis.keys()) or ("motorbike" in lis.keys()) or ("bus" in lis.keys()) or ("truck" in lis.keys()) or ("traffic light" in lis.keys())) :
        mixer.music.load("Road.mp3")
    
    else :
        mixer.music.load("Unable.mp3")
    mixer.music.play()
    time.sleep(3)

def image_capture() : 
    current_time = datetime.now()
    print(type(current_time))
    cap=cv.VideoCapture(0)
    dic = {}

    while True :

        ret , img = cap.read() 
        #cv.imshow('Input',img)
        c= cv.waitKey(1)
    
        if c==27:
            break
    
        height,width,_=img.shape
        #converting to normal frame
        #grey scale 
        blob = cv.dnn.blobFromImage(img , 1/255 , (320,320) , (0,0,0) , swapRB=True, crop = False ) 
        #mtlb.imshow(blob) 

        #print frame0
        i = blob[0].reshape(320,320,3)
        mtlb.imshow(i)

        yolo.setInput(blob)
        output_layes_name = yolo.getUnconnectedOutLayersNames()
        layeroutput = yolo.forward(output_layes_name)

        boxs = []
        confidences = []
        class_ids = []
        for output in layeroutput :
            for detection in output :
                score = detection[5:]
                class_id = np.argmax(score)
                confidence = score[class_id]
                if confidence > 0.7 :
                    center_x = int(detection[0]*width)
                    center_y = int(detection[0]*height)
                    w = int(detection[0]*width)
                    h = int(detection[0]*height)
                    x = int(center_x - w/2) 
                    y = int(center_y - h/2)

                    boxs.append([x,y,w,h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        len(boxs)
        indexes = cv.dnn.NMSBoxes(boxs,confidences,0.5,0.4)

        font = cv.FONT_HERSHEY_COMPLEX
        colors = np.random.uniform(0,255,size=(len(boxs),3))

        dici = {}
        for i in indexes.flatten():
            x,y,w,h = boxs[i]
            label = str(classes[class_ids[i]])
            confi = str(round(confidences[i],2))
            color = colors[i]
            if (label in dic) and (label in dici)  :
                dic[label] = max(dic[label] , dici[label])
                dici[label] = dici[label] + 1    
            else :
                dici[label] =  1

            cv.rectangle(img,(x,y),(x+w,y+h),color,1)
            cv.putText(img , label +" "+confi,(x,y+20),font,2,(255,255,255),1)
            cv.imshow('video',img)
    
        for a in dici : 
            if a in dic :
                dic[a] = max(dic[a],dici[a])
            else :
                dic[a] = dici[a]

        
        print(dic)
        mtlb.imshow(img)

        print((datetime.now() - current_time).total_seconds())
        if (((datetime.now() - current_time).total_seconds())>5) :
            processing(dic)
            current_time = datetime.now()
            dic = {}

def main_task():
    image_capture() 

if __name__ == "__main__":
    main_task()