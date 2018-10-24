import cv2
import numpy as np
import pandas as pd
import os
def ds_fun():
    f_c=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    #id=input('Enter your id ')
    id=0;
    name=input('Enter your Name ')
    name_id=pd.DataFrame({'Name':[name],'ID':[id]})
    if not os.path.isfile('name_id'):
        fl=open('name_id','w')
        name_id.to_csv('name_id')
    else :
        dataset = pd.read_csv('name_id')
        id=(int)(dataset.iloc[-1,-2])
        id=id+1
        name_id=pd.DataFrame({'Name':[name],'ID':[id]})
        name_id.to_csv('name_id',mode='a',header=False)
    
    no=0
    while True:
        ret,img=cap.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=f_c.detectMultiScale(gray,1.3,3)
        for(x,y,w,h) in faces:
            no=no+1;
            cv2.imwrite("Dataset/user."+str(id)+"."+str(no)+".jpg",gray[y:y+h,x:x+h])
            cv2.rectangle(img, (x,y) , (x+w , y+h) ,(255,0,0 ), 2)
            cv2.waitKey(100)
        cv2.imshow('img',img)
        k=cv2.waitKey(30) & 0xFF
        if(k==113 or no==80):
            break;
    cap.release()
    cv2.destroyAllWindows()