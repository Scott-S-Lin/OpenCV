# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math
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
#熵閾值法
def threshEntroy(image):
    rows,cols = image.shape
    #求灰度長條圖
    grayHist = calcGrayHist(image)
    #歸一化灰度長條圖
    normGrayHist = grayHist/float(rows*cols)
    #計算累加長條圖，也稱零階累加矩
    zeroCumuMoment = np.zeros([256],np.float32)
    for k in range(256):
        if k==0:
            zeroCumuMoment[k] = normGrayHist[k]
        else:
            zeroCumuMoment[k] = zeroCumuMoment[k-1] + normGrayHist[k]
    #計算各個灰度級的熵
    entropy = np.zeros([256],np.float32)
    for k in range(256):
        if k==0:
            if normGrayHist[k] ==0:
                entropy[k] = 0
            else:
                entropy[k] = - normGrayHist[k]*math.log10(normGrayHist[k])
        else:
            if normGrayHist[k] ==0:
                entropy[k] = entropy[k-1]
            else:
               entropy[k] = entropy[k-1] - normGrayHist[k]*math.log10(normGrayHist[k])
    #找閾值
    fT = np.zeros([256],np.float32)
    ft1,ft2 = 0.0,0.0
    totalEntroy = entropy[255]
    for k in range(255):
        #找最大值
        maxFront = np.max(normGrayHist[0:k+1])
        maxBack = np.max(normGrayHist[k+1:256])
        if(maxFront == 0 or zeroCumuMoment[k] == 0 or maxFront==1 or zeroCumuMoment[k]==1 or totalEntroy==0):
            ft1 = 0
        else:
            ft1 =entropy[k]/totalEntroy*(math.log10(zeroCumuMoment[k])/math.log10(maxFront))
        if(maxBack == 0 or 1 - zeroCumuMoment[k]==0 or maxBack == 1 or 1-zeroCumuMoment[k] ==1):
            ft2 = 0
        else:
            if totalEntroy==0:
                ft2 = (math.log10(1-zeroCumuMoment[k])/math.log10(maxBack))
            else:
                ft2 = (1-entropy[k]/totalEntroy)*(math.log10(1-zeroCumuMoment[k])/math.log10(maxBack))
        fT[k] = ft1+ft2
    #找最大值的索引，作為得到的閾值
    threshLoc = np.where(fT==np.max(fT))
    thresh = threshLoc[0][0]
    #閾值處理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold <= thresh] = 0
    return (threshold,thresh)

#每一種訊號來源符號出現的頻率 
image = cv2.imread('img4/frame36.jpg',cv2.IMREAD_GRAYSCALE)
threshold,thresh = threshEntroy(image);
#顯示閾值後的二值化圖像
cv2.imshow("threshEntroy",threshold)
print(thresh)
cv2.imwrite("entroy.jpg",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

