# -*- coding: utf-8 -*-

#引入python模組
import numpy as np
import cv2

#OpenCV 本身就有提供讀取圖片檔的函數可用
#讀取一般圖檔，只要呼叫cv2.imread
img = cv2.imread('spyder.JPG')

#cv2.imread 讀進來的資料
#會儲存成一個 NumPy 的陣列，可以使用 type 查看一下
print(type(img))

#NumPy 陣列的前兩個維度分別是圖片的高度與寬度
#第三個維度則是圖片的 channel
#（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）
print(img.shape)

# 以灰階的方式讀取圖檔
img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 顯示圖片
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)
cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()

# 關閉 'My Image' 視窗
#cv2.destroyWindow('My Image') 