# -*- coding: utf-8 -*-
import cv2
import sys
import numpy as np
#主函數
if __name__ =="__main__":
    img = cv2.imread('img7/dog.jpg',cv2.IMREAD_GRAYSCALE)
    #第一步：閾值化，生成二值圖
    #圖像平滑
    dst = cv2.GaussianBlur(img,(3,3),0.5)
    # Otsu 閾值分割
    OtsuThresh = 0
    OtsuThresh,dst = cv2.threshold(dst,OtsuThresh,255,cv2.THRESH_OTSU)
    # --- 形態學開運算（ 消除細小白點 ）
    #創建結構元
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    dst = cv2.morphologyEx(dst,cv2.MORPH_OPEN,s,iterations=2)
    #第二步：尋找二值圖的輪廓，返回值是一個元組，hc[1] 代表輪廓
    hc= cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = hc[1]
    #列印輪廓的屬性
    print(type(contours))
    #第三步：畫出找到的輪廓並用多邊形擬合輪廓
    #輪廓的數量
    n =  len(hc[1])
    #將輪廓畫在該黑板上
    contoursImg = np.zeros(img.shape,np.uint8)
    for i in range(n):
        #畫出輪廓
        cv2.drawContours(contoursImg,contours,i,255,2)
        #畫出輪廓的最小外包圓
        circle = cv2.minEnclosingCircle(contours[i])
        cv2.circle(img,(int(circle[0][0]),int(circle[0][1])),int(circle[1]),0,5)
        #多邊形逼近（注意與凸包區別）
        approxCurve = cv2.approxPolyDP(contours[i],0.3,True)
        #多邊形頂點個數
        k = approxCurve.shape[0]
        #頂點連接，繪製多邊形
        for i in range(k-1):
            cv2.line(img,(approxCurve[i,0,0],approxCurve[i,0,1]),(approxCurve[i+1,0,0],approxCurve[i+1,0,1]),0,5)
        #首尾相接
        cv2.line(img,(approxCurve[k-1,0,0],approxCurve[k-1,0,1]),(approxCurve[0,0,0],approxCurve[0,0,1]),0,5)
    #顯示輪廓
    cv2.imshow("contours",contoursImg)
    #顯示擬合的多邊形
    cv2.imshow("dst",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
