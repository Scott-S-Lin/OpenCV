# -*- coding: utf-8 -*-import sys
import numpy as np
import cv2
def adaptiveThresh(I,winSize,ratio=0.15):
    #第一步：對圖像矩陣進行均值平滑
    I_smooth = cv2.boxFilter(I,cv2.CV_32FC1,winSize)
    #I_smooth = cv2.medianBlur(I,cv2.CV_32FC1,winSize)
    #第二步：原圖像矩陣與平滑結果做差
    out = I - (1.0-ratio)*I_smooth
    #第三步：對 out 進行全域閾值處理，差值大於等於零，輸出值為255，反之為零
    out[out>=0] = 255
    out[out<0] = 0
    out = out.astype(np.uint8)
    return out

#Test(image4.jpg)
image = cv2.imread('img4/image3.png',cv2.IMREAD_GRAYSCALE)
out = adaptiveThresh(image,(31,31),0.15)
cv2.imshow("out",out)
cv2.imwrite("adTh.jpg",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
