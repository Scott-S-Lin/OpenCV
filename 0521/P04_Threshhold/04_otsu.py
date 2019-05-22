# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math
#計算圖像灰度長條圖
def calcGrayHist(image):
    #灰度圖像矩陣的寬高
    rows,cols = image.shape
    #存儲灰度長條圖
    grayHist = np.zeros([1,256],np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[0][image[r][c]] +=1
    return grayHist 
def ostu(image):
    rows,cols = image.shape
    #計算圖像的灰度長條圖
    grayHist = calcGrayHist(image)
    #歸一化灰度長條圖
    uniformGrayHist = grayHist/float(rows*cols)
    #計算零階累積矩和一階累積矩
    zeroCumuMoment = np.zeros([1,256],np.float32)
    oneCumuMoment = np.zeros([1,256],np.float32)
    for k in range(256):
        if k == 0:
            zeroCumuMoment[0][k] = uniformGrayHist[0][0]
            oneCumuMoment[0][k] = (k+1)*uniformGrayHist[0][0]
        else:
            zeroCumuMoment[0][k] = zeroCumuMoment[0][k-1] + uniformGrayHist[0][k]
            oneCumuMoment[0][k] = oneCumuMoment[0][k-1] + k*uniformGrayHist[0][k]
    #計算類間方差 
    variance = np.zeros([1,256],np.float32)
    for k in range(255):
        if zeroCumuMoment[0][k] == 0:
            variance[0][k] = 0
        else:
            variance[0][k] = math.pow(oneCumuMoment[0][255]*zeroCumuMoment[0][k] - oneCumuMoment[0][k],2)/(zeroCumuMoment[0][k]*(1.0-zeroCumuMoment[0][k]))
    #找到閾值
    threshLoc = np.where(variance[0][0:255] == np.max(variance[0][0:255]))
    thresh = threshLoc[0]
    #閾值處理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold <= thresh] = 0
    return threshold

#(cow ship dog)ok  (image3 & image4)no ok
image = cv2.imread('img4/dog.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",image)
#閾值演算法
ostu_threshold = ostu(image)
#顯示閾值處理的結果
cv2.imshow("ostu_threshold",ostu_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

