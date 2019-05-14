# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('image.png',cv2.IMREAD_COLOR)
print(image.shape)   
#得到三個顏色通道
b = image[:,:,0]
g = image[:,:,1]
r = image[:,:,2]
#顯示三個顏色通道
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

#8位圖轉換為 浮點數
fImg = image/255.0
fb = fImg[:,:,0]
fg = fImg[:,:,1]
fr = fImg[:,:,2]
#顯示三個顏色
cv2.imshow("fb",fb)
cv2.imshow("fg",fg)
cv2.imshow("fr",fr)

#OpenCV分離三通道的函數split()，返回值依次是藍色、綠色和紅色通道的灰度圖
b, g, r = cv2.split(image)
cv2.imshow("Blue 1", b)
cv2.imshow("Green 1", g)
cv2.imshow("Red 1", r)

cv2.waitKey(0)
cv2.destroyAllWindows()