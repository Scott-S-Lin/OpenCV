# -*- coding: utf-8 -*-
import numpy as np
import sys
import math
import cv2
from scipy import signal
#二項式展開式的係數，即平滑係數
def pascalSmooth(n):
    pascalSmooth = np.zeros([1,n],np.float32)
    for i in range(n):
        pascalSmooth[0][i] = math.factorial(n -1)/(math.factorial(i)*math.factorial(n-1-i))
    return pascalSmooth
#計算差分
def pascalDiff(n):
    pascalDiff = np.zeros([1,n],np.float32)
    pascalSmooth_previous = pascalSmooth(n-1)
    for i in range(n):
        if i ==0:
            #恒等於 1
            pascalDiff[0][i] = pascalSmooth_previous[0][i]
        elif i == n-1:
            #恒等於 -1
            pascalDiff[0][i] = -pascalSmooth_previous[0][i-1]
        else:
            pascalDiff[0][i] = pascalSmooth_previous[0][i] - pascalSmooth_previous[0][i-1]
    return pascalDiff
#通過平滑係數和差分係數的卷積運算計算卷積核
def getSobelKernel(winSize):
     pascalSmoothKernel = pascalSmooth(winSize)
     pascalDiffKernel = pascalDiff(winSize)
     #水準方向上的卷積核
     sobelKernel_x = signal.convolve2d(pascalSmoothKernel.transpose(),pascalDiffKernel,mode='full')
     #垂直方向上的卷積核
     sobelKernel_y = signal.convolve2d(pascalSmoothKernel,pascalDiffKernel.transpose(),mode='full')
     return (sobelKernel_x,sobelKernel_y)
# sobel 邊緣檢測
def sobel(image,winSize):
    rows,cols = image.shape
    pascalSmoothKernel = pascalSmooth(winSize)
    pascalDiffKernel = pascalDiff(winSize)
    # --- 與水準方向的卷積核卷積 ----
    image_sobel_x = np.zeros(image.shape,np.float32)
    #垂直方向上的平滑
    image_sobel_x = signal.convolve2d(image,pascalSmoothKernel.transpose(),mode='same')
    #水準方向上的差分
    image_sobel_x = signal.convolve2d(image_sobel_x,pascalDiffKernel,mode='same')
    # --- 與垂直方向上的卷積核卷積 --- 
    image_sobel_y = np.zeros(image.shape,np.float32)
    #水準方向上的平滑(可註解試看看)
    image_sobel_y = signal.convolve2d(image,pascalSmoothKernel,mode='same')
    #垂直方向上的差分(可註解試看看)
    image_sobel_y = signal.convolve2d(image_sobel_y,pascalDiffKernel.transpose(),mode='same')
    return (image_sobel_x,image_sobel_y)

if __name__=='__main__':
    image = cv2.imread('img6/sobel.jpg',cv2.IMREAD_GRAYSCALE)
    #得到卷積核
    sobelKernel3 = getSobelKernel(3)
    sobelKernel5 = getSobelKernel(5)
    print(sobelKernel3)
    print(sobelKernel5)
    #卷積 獲得水平方向和垂直方向的n*n運算元
    image_sobel_x,image_sobel_y = sobel(image,3)
    edge_x = np.abs(image_sobel_x)
    edge_x[ edge_x>255]=255
    edge_x=edge_x.astype(np.uint8)
    edge_y = np.abs(image_sobel_y)
    edge_y[ edge_y>255]=255
    edge_y=edge_y.astype(np.uint8)
    cv2.imwrite("img7_sobel_x_3_3.jpg",edge_x)
    cv2.imwrite("img7_sobel_y_3_3.jpg",edge_y)
    #邊緣強度：兩個卷積結果對應位置的平方和
    edge = np.sqrt(np.power(image_sobel_x,2.0) + np.power(image_sobel_y,2.0))
    #邊緣強度的灰度級顯示
    edge[edge>255] = 255
    edge = np.round(edge)
    edge = edge.astype(np.uint8)
    cv2.imshow("sobel edge",edge)
    cv2.imwrite("sobel.jpg",edge)
    #模擬素描
    pencilSketch = edge.copy()
    pencilSketch = 255 - pencilSketch
    pencilSketch[pencilSketch < 80] = 80
    cv2.imshow("pencilSketch",pencilSketch)
    cv2.imwrite("pencilSketch.jpg",pencilSketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
