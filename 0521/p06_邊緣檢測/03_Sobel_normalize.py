# -*- coding: utf-8 -*-
import numpy as np
import math
import cv2
from scipy import signal

#二項式展開式的係數，即平滑係數
def pascalSmooth(n):
    pascalSmooth = np.zeros([1,n],np.float32)
    for i in range(n):
        pascalSmooth[0][i] = math.factorial(n -1)/(math.factorial(i)*math.factorial(n-1-i))
    return pascalSmooth
def pascalDiff(n):
    pascalDiff = np.zeros([1,n],np.float32)
    pascalSmooth_previous = pascalSmooth(n-1)
    for i in range(n):
        if i ==0:
            pascalDiff[0][i] = pascalSmooth_previous[0][i]
        elif i == n-1:
            pascalDiff[0][i] = -pascalSmooth_previous[0][i-1]
        else:
            pascalDiff[0][i] = pascalSmooth_previous[0][i] - pascalSmooth_previous[0][i-1]
    return pascalDiff

#通過平滑係數和差分係數的卷積運算計算卷積核
def getSobelKernel(winSize):
     pascalSmoothKernel = pascalSmooth(winSize)
     pascalDiffKernel = pascalDiff(winSize)
     sobelKernel_x = signal.convolve2d(pascalSmoothKernel.transpose(),pascalDiffKernel,mode='full')
     sobelKernel_y = signal.convolve2d(pascalSmoothKernel,pascalDiffKernel.transpose(),mode='full')
     return (sobelKernel_x,sobelKernel_y)
 
# sobel 邊緣檢測
def sobel(image,winSize):
    rows,cols = image.shape
    pascalSmoothKernel = pascalSmooth(winSize)
    pascalDiffKernel = pascalDiff(winSize)
    # --- 與水準方向的卷積核卷積 ----
    image_sobel_x = np.zeros(image.shape,np.float32)
    image_sobel_x = signal.convolve2d(image,pascalSmoothKernel.transpose(),mode='same')
    image_sobel_x = signal.convolve2d(image_sobel_x,pascalDiffKernel,mode='same')
    # --- 與垂直方向上的卷積核卷積 --- 
    image_sobel_y = np.zeros(image.shape,np.float32)
    image_sobel_y = signal.convolve2d(image,pascalSmoothKernel,mode='same')
    image_sobel_y = signal.convolve2d(image_sobel_y,pascalDiffKernel.transpose(),mode='same')
    return (image_sobel_x,image_sobel_y)

image = cv2.imread('img6/sobel.jpg',cv2.IMREAD_GRAYSCALE)  
#卷積
image_sobel_x,image_sobel_y = sobel(image,7)
#平方和開方的方式
edge = np.sqrt(np.power(image_sobel_x,2.0) + np.power(image_sobel_y,2.0))
#邊緣強度的灰度級顯示
edge =edge/np.max(edge)
edge*=255
edge = np.power(edge,0)
edge = edge.astype(np.uint8)
cv2.imshow("sobel edge",edge)
cv2.imwrite("sobel.jpg",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
