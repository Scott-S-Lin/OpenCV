# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
#計算圖像灰度長條圖
def calcGrayHist(image):
    #灰度圖像矩陣的寬高
    rows,cols = image.shape
    #存儲灰度長條圖
    grayHist = np.zeros([256],np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] +=1
    return grayHist
#長條圖均衡化
def equalHist(image):
    #灰度圖像矩陣的寬高
    rows,cols = image.shape
    #計算灰度長條圖
    grayHist = calcGrayHist(image)
    #計算累積灰度長條圖
    zeroCumuMoment = np.zeros([256],np.uint32)
    for p in range(256):
        if p == 0:
            zeroCumuMoment[p] = grayHist[0]
        else:
            zeroCumuMoment[p] = zeroCumuMoment[p-1] + grayHist[p]
    #根據長條圖均衡化得到的輸入灰度級和輸出灰度級的映射
    outPut_q = np.zeros([256],np.uint8)
    cofficient = 256.0/(rows*cols)
    for p in range(256):
        q = cofficient* float(zeroCumuMoment[p]) -1
        if q >= 0:
            outPut_q[p] = math.floor(q)
        else:
            outPut_q[p] = 0
    #得到長條圖均衡化後的圖像
    equalHistImage  = np.zeros(image.shape,np.uint8)
    for r in range(rows):
        for c in range(cols):
            equalHistImage[r][c] = outPut_q[image[r][c]]
    return equalHistImage
            

image = cv2.imread('img2/equal.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",image)
#長條圖均衡化
result = equalHist(image)
cv2.imshow("equalHist",result)
cv2.imwrite("equalHist.jpg",result)
#長條圖均衡話後的灰度長條圖
#組數
numberBins = 256
#計算灰度長條圖
rows,cols = image.shape
histEqualResultSeq = result.reshape([rows*cols,])
histogram,bins,patch_image= plt.hist(histEqualResultSeq,numberBins,facecolor='black',histtype='bar')
#設置坐標軸的標籤
plt.xlabel(u"gray Level")
plt.ylabel(u"number of pixels")
#設置坐標軸的範圍
y_maxValue = np.max(histogram)
plt.axis([0,255,0,y_maxValue])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
