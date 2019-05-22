# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread('img7/img.jpg')

ret,thresh = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),127,255,0)
_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#得到轮廓信息
cnt = contours[0]#取第一条轮廓
M = cv2.moments(cnt)#计算第一条轮廓的矩

imgnew = cv2.drawContours(img, contours, -1, (0,255,0), 3)#把所有轮廓画出来
print (M)
#这两行是计算中心点坐标
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
else:
    # set values as what you need in the situation
    cX, cY = 0, 0
#计算轮廓所包含的面积
area = cv2.contourArea(cnt)

#计算轮廓的周长
perimeter = cv2.arcLength(cnt,True)


#轮廓的近似
epsilon = 0.02*perimeter
approx = cv2.approxPolyDP(cnt,epsilon,True)
imgnew1 = cv2.drawContours(img, approx, -1, (0,0,255), 3)

cv2.imshow('lunkuo',imgnew)
cv2.imshow('approx_lunkuo',imgnew1)
cv2.waitKey(0)
cv2.destroyAllWindows()