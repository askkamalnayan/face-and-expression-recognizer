# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np
f_c=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
e_c=cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=f_c.detectMultiScale(gray,1.3,10)
    for(x,y,w,h) in faces:
        cv2.rectangle(gray, (x,y) , (x+w , y+h) ,(255,0,0 ), 2)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color = img[y:y+h ,x:x+w]
        eyes = e_c.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_gray, (ex,ey), (ex+ew,ey+eh) ,(0,255,0), 2)
    cv2.imshow('img',gray)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
