# -*- coding: utf-8 -*-
import numpy as np
import cv2

def calcGrayHist(image):#計算圖像灰度長條圖
    #灰度圖像矩陣的寬高
    rows,cols = image.shape
    #儲存灰度長條圖
    grayHist = np.zeros([256],np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] +=1
    return grayHist
#返回閾值和二值化的影像

def threshTwoPeaks(image):
    histogram = calcGrayHist(image)#計算圖像灰度長條圖
    #找到灰度長條圖的最大峰值對應的灰度值
    maxLoc = np.where(histogram==np.max(histogram))
    firstPeak = maxLoc[0]
    print(maxLoc[0])
 
    #尋找灰度長條圖的 " 第二個峰值 " 對應的灰度值
    measureDists = np.zeros([256],np.float32)
    for k in range(256):
        measureDists[k] = pow(k-firstPeak,2)*histogram[k]
    maxLoc2 = np.where(measureDists==np.max(measureDists))
    secondPeak = maxLoc2[0]

    #找到兩個峰值之間的最小值對應的灰度值，作為閾值(THRESH_TIANGLE類似)
    thresh = 0
    if firstPeak > secondPeak:#第一個峰值在第二個峰值的右側
        temp = histogram[int(secondPeak):int(firstPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = secondPeak + minLoc[0]+1
    else:#第一個峰值在第二個峰值的左側
        temp = histogram[int(firstPeak):int(secondPeak)]
        minLoc = np.where( temp == np.min(temp))
        thresh = firstPeak + minLoc[0]+1

    #找到閾值後進行閾值處理，得到二值圖
    threshImage_out = image.copy()
    threshImage_out[threshImage_out > thresh] = 255
    threshImage_out[threshImage_out <= thresh] = 0
    return (thresh,threshImage_out)

image = cv2.imread('img4/img.jpg',cv2.IMREAD_GRAYSCALE)
thresh,threshImage_out = threshTwoPeaks(image)
#輸出長條圖技術得到的閾值
print(thresh)
#顯示原圖和閾值化得到的二值圖
cv2.imshow("image",image)
cv2.imshow("threshTwoPeaks",threshImage_out)
cv2.imwrite("twoPeaks.jpg",threshImage_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
