import cv2
import pandas as pd
import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json
def fun():
    f_c=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    rec=cv2.face.LBPHFaceRecognizer_create()
    rec.read('recognizer/trainData.yml')
    pr_dataset=pd.read_csv('name_id')
    name=pr_dataset.iloc[:,-1].values
    model = model_from_json(open('f_model.json','r').read())
    model.load_weights('f_model.h5')
    font=cv2.FONT_HERSHEY_DUPLEX
    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    id=0
    delta=20
    while True:
        ret,img=cap.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=f_c.detectMultiScale(gray,1.3,3)
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y) , (x+w , y+h) ,(255,0,0 ), 2)
            detected_face=img[int(y):int(y+h),int(x):int(x+w)]
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            detected_face=cv2.cvtColor(detected_face,cv2.COLOR_BGR2GRAY)
            detected_face=cv2.resize(detected_face,(48,48))
            img_pxls=image.img_to_array(detected_face)
            img_pxls=np.expand_dims(img_pxls,axis=0)
            img_pxls/=255
            predictions=model.predict(img_pxls)
            mx_indx=np.argmax(predictions[0])
            emotion=emotions[mx_indx]
            cv2.putText(img,(str(name[id])+" is "+emotion),(x,y+h+delta),font,1,(19,19,246),2)
        cv2.imshow('img',img)
        k=cv2.waitKey(30) & 0xFF
        if(k==113):
            break;
    cap.release()
    cv2.destroyAllWindows()