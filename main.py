# -*- coding: utf-8 -*-
import time
import predictor
import datasetcreator
import Trainer
while True:
    print("Choose one of them")
    k=input("1.Include your profile \n2.See Magic\n")
    if k =='1' or k=='2':
        break
    print("wrong input")
if k==2:
    k='1233'
while True:
    if k=='1':
        datasetcreator.ds_fun()
    if k=='1233':
        predictor.fun()
    elif k=='2':
        Trainer.tr_fun()
        time.sleep(3)
        predictor.fun()
    if k=='2' or k=='1233':
        break
    print("Choose one of them")
    k=input("1.Include More profile \n2.See Magic\n")
    if not (k=='1' or k=='2'):
        print("wrong input")
    