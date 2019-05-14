# -*- coding: utf-8 -*-


import cv2

img = cv2.imread('spyder.JPG')
print(type(img))
print(img.shape)

# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)
cv2.imshow('My Image', img)
img_gray = cv2.imread('spyder.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('My GRAYSCALE Image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()