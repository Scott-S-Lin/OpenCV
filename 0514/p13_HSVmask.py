# -*- coding: utf-8 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    #獲取每一幀
    ret,frame = cap.read()
    RGB = cv2.cvtColor(frame,cv2.COLOR_BGRA2RGB)
    #轉換到HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #設定色彩的門檻閥值
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([255,255,255])
    #根據門檻值(threashold)做遮罩
    #mask = cv2.inRange(hsv,lower_blue,upper_blue)
    mask = cv2.inRange(RGB,lower_blue,upper_blue)
    #對原圖和mask進行運算
    res = cv2.bitwise_and(frame,frame,mask=mask)
    #顯示圖像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5)&0xFF
    if k == 27:
        break
#關閉
cv2.destroyAllWindows()

