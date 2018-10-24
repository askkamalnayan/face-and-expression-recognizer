# -*- coding: utf-8 -*-
import os
import numpy as np
from PIL import Image
import cv2
def tr_fun():
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    path='Dataset'
    def getImageList(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faces=[]
        IDs=[]
        for i_p in imagePaths:
            faceImage=Image.open(i_p);
            faceNp=np.array(faceImage,'uint8')
            ID=int(os.path.split(i_p)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            #cv2.imshow('faces',faceNp)
            #print(ID)
            cv2.waitKey(10)
        return np.array(IDs),faces
    IDs,faces=getImageList(path)
    recognizer.train(faces,IDs)
    recognizer.save('recognizer/trainData.yml')
    cv2.destroyAllWindows()
