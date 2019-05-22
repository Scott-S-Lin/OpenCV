# -*- coding: utf-8 -*-
import sys
import numpy as np
import cv2
import math
#基於空間距離的權重因數 ( 和計算高斯運算元的過程是一樣的 )
def getClosenessWeight(sigma_g,H,W):
    #第一步：構建高斯矩陣gaussMatrix
    gaussMatrix = np.zeros([H,W],np.float32)
    #得到中心點的位置
    cH = (H-1)/2
    cW = (W-1)/2
    for r in range(H):
        for c in range(W):
            norm2 = math.pow(r-cH,2.0) + math.pow(c-cW,2.0)
            gaussMatrix[r][c] = math.exp(-norm2/(2*math.pow(sigma_g,2.0)))
    #第二步：計算高斯矩陣的和
    sumGM = np.sum(gaussMatrix)
    #第三步：歸一化，gaussMatrix/sumGM
    gaussMatrix = gaussMatrix/sumGM
    return gaussMatrix
# BilateralFiltering 雙邊濾波，返回的資料類型為浮點型
def bfltGray(image,winH,winW,sigma_g,sigma_d):
    #構建空間距離的權重因數
    closenessWeight = getClosenessWeight(sigma_g,winH,winW)
    #得到卷積核的中心點座標
    halfWinH = (winH -1)/2
    halfWinW = (winW -1)/2
    #圖像矩陣的行數和列數
    rows,cols = image.shape
    #雙邊濾波後的結果
    bfltGrayImage = np.zeros(image.shape,np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel = image[r][c]
            #判斷邊界
            rTop =int( 0 if r-halfWinH < 0 else r-halfWinH)
            rBottom = int(rows-1 if r+halfWinH > rows-1 else r+halfWinH)
            cLeft =int(0 if c-halfWinW < 0 else c-halfWinW)
            cRight = int(cols-1 if c+halfWinW > cols-1 else c+halfWinW)
            #核作用的區域
            region = image[int(rTop):int(rBottom)+1,int(cLeft):int(cRight)+1]
            #構建灰度值相似性的權重因數
            similarityWeightTemp = np.exp(-0.5*pow(region -pixel,2.0)/pow(sigma_d,2.0))#錯誤
            closenessWeightTemp = closenessWeight[int(rTop-r+halfWinH):int(rBottom-r+halfWinH)+1,int(cLeft-c+halfWinW):int(cRight-c+halfWinW)+1]
            #兩個核相乘
            weightTemp = similarityWeightTemp*closenessWeightTemp
            weightTemp = weightTemp/np.sum(weightTemp)
            bfltGrayImage[r][c] = np.sum(region*weightTemp)
    return bfltGrayImage
#主函數
if __name__ =="__main__":
    
    image = cv2.imread('img3/golf.png',cv2.IMREAD_GRAYSCALE)
    cv2.imshow("image",image)
    #雙邊濾波
    image = image.astype(np.float32)
    bfltImage = bfltGray(image,21,21,30,30)
    bfltImage = bfltImage/255.0
    #顯示雙邊濾波的結果
    bfltImage = bfltImage.astype(np.float32)
    cv2.imshow("BilateralFiltering",bfltImage)
    #因為雙邊濾波返回的是資料類型是浮點型的,可以轉換為 8 點陣圖
   # bfltImage = bfltImage*255.0
    #bfltImage = np.round(bfltImage)
    #bfltImage = bfltImage.astype(np.uint8)
    #保存雙邊濾波的結果
    cv2.imwrite("BilateralFiltering.jpg",bfltImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
