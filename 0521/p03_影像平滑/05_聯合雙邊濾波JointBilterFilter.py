# -*- coding: utf-8 -*-
import sys
import numpy as np
import cv2
import math
#基於空間距離的權重範本 ( 和計算高斯運算元的過程是一樣的 )
def getClosenessWeight(sigma_g,H,W):
    r,c = np.mgrid[0:H:1, 0:W:1]
    r -= (H-1)//2
    c -= (W-1)//2
    closeWeight = np.exp(-0.5*(np.power(r,2.0)+np.power(c,2.0))/math.pow(sigma_g,2.0))
    return closeWeight
def jointBLF(I,H,W,sigma_g,sigma_d,borderType=cv2.BORDER_DEFAULT):
    #構建空間距離的權重範本
    closenessWeight = getClosenessWeight(sigma_g,H,W)
    #對 I 進行高斯平滑
    Ig = cv2.GaussianBlur(I,(W,H),sigma_g)
    #範本的中心點位置
    cH = (H -1)//2
    cW = (W -1)//2
    #對原圖和高斯平滑的結果擴充邊界
    Ip=cv2.copyMakeBorder(I,cH,cH,cW,cW,borderType)
    Igp=cv2.copyMakeBorder(Ig,cH,cH,cW,cW,borderType)
    #圖像矩陣的行數和列數
    rows,cols = I.shape
    i,j=0,0
    #聯合雙邊濾波結果
    jblf = np.zeros(I.shape,np.float64)        
    for r in np.arange(cH,cH+rows,1):
        for c in np.arange(cW,cW+cols,1):
            #當前位置的值
            pixel = Igp[r][c]
            #當前位置的鄰域
            rTop,rBottom = r-cH,r+cH
            cLeft,cRight = c-cW,c+cW
            #從 Igp 中截取該鄰域，用於構建相似性權重
            region= Igp[rTop:rBottom+1,cLeft:cRight+1]
            #通過上述鄰域,構建該位置的相似性權重範本
            similarityWeight = np.exp(-0.5*np.power(region -pixel,2.0)/math.pow(sigma_d,2.0))
            #相似性權重範本和空間距離權重範本形成
            weight = closenessWeight*similarityWeight
            #將權重範本歸一化
            weight = weight/np.sum(weight)
            #權重範本和鄰域對應位置相乘並求和
            jblf[i][j] = np.sum(Ip[rTop:rBottom+1,cLeft:cRight+1]*weight)
            j += 1
        j = 0
        i += 1
    return jblf

if __name__ =="__main__":
    I = cv2.imread('img3/img3.jpg',cv2.IMREAD_GRAYSCALE)
    #將 8 點陣圖轉換為 浮點型
    fI = I.astype(np.float64)
    #聯合雙邊濾波，返回值的資料類型為浮點型
    jblf = jointBLF(fI,33,33,7,2)
    #轉換為 8 點陣圖
    jblf = np.round(jblf)
    jblf = jblf.astype(np.uint8)
    cv2.imshow("jblf",jblf)
    #保存結果
    #cv2.imwrite("jblf1.png",jblf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
