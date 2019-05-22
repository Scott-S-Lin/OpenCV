# -*- coding: utf-8 -*-

import cv2
import numpy as np

I = cv2.imread('img5/dilate_bin.JPG',cv2.IMREAD_GRAYSCALE)
cv2.imshow("I",I)
#結構元長和寬度,反覆運算次數
r,i = 1,1
MAX_R,MAX_I = 20,20
#顯示膨脹效果的視窗

cv2.namedWindow("dilate",1)
def nothing(*arg):
    pass
cv2.createTrackbar("i","dilate",i,MAX_I,nothing)#調節反覆運算次數

while True:
    i= cv2.getTrackbarPos('i','dilate')#得到當前的i值
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    #膨脹圖像
    d = cv2.dilate(I,kernal,iterations=i)
    #顯示膨脹效果
    cv2.imshow("dilate",d)
    cv2.imwrite("dilate.jpg",d)
    ch = cv2.waitKey(1)
    if ch == 27:    #按下"Esc"鍵退出迴圈
        break
cv2.destroyAllWindows()
