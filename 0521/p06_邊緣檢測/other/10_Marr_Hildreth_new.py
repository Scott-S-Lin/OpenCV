# -*- coding: utf-8 -*-
import numpy as np
import cv2
from scipy import signal
#非歸一化的高斯卷積
def gaussConv(I,size,sigma):
    #卷積核的高和寬
    H,W = size
    #構造水準方向上非歸一化的高斯卷積核
    xr,xc = np.mgrid[0:1,0:W]
    xc = np.array(xc, dtype=np.float64)
    xc -= (W-1)/2
    xk = np.exp(-np.power(xc,2.0)/(2.0*pow(sigma,2)))
    # I 與 xk 卷積
    I_xk = signal.convolve2d(I,xk,'same','symm')
    #構造垂直方向上的非歸一化的高斯卷積核
    yr,yc = np.mgrid[0:H,0:1]
    yr = np.array(yr, dtype=np.float64)
    yr -= (H-1)/2
    yk = np.exp(-np.power(yr,2.0)/(2.0*pow(sigma,2.0)))
    # I_xk 與 yk 卷積
    I_xk_yk = signal.convolve2d(I_xk,yk,'same','symm')
    I_xk_yk *= 1.0/(2*np.pi*pow(sigma,2.0))
    return I_xk_yk
#高斯差分
def DoG(I,size,sigma,k=1.1):
    #標準差為 sigma 的非歸一化的高斯卷積
    Is = gaussConv(I,size,sigma)
    #標準差為 k*sigma 的非歸一化高斯卷積
    Isk = gaussConv(I,size,k*sigma)
    #兩個高斯卷積的差分
    doG = Isk - Is
    doG /= (pow(sigma,2.0)*(k-1))
    return doG
#零交叉點：方法1
def zero_cross_default(doG):
    zero_cross = np.zeros(doG.shape,np.uint8)
    rows,cols = doG.shape
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            # 左 / 右方向
            if doG[r][c-1]*doG[r][c+1] < 0:
                zero_cross[r][c] = 255
                continue
            #上 / 下方向
            if doG[r-1][c]*doG[r+1][c] < 0:
                zero_cross[r][c] = 255
                continue
            #左上 / 右下方向
            if doG[r-1][c-1]*doG[r+1][c+1] < 0:
                zero_cross[r][c] = 255
                continue
            #右上 / 左下方向
            if doG[r-1][c+1]*doG[r+1][c-1] < 0:
                zero_cross[r][c] = 255
                continue
    return zero_cross
#零交叉點：方法2
def zero_cross_mean(doG):
    zero_cross = np.zeros(doG.shape,np.uint8)
    #存儲左上，右上，左下，右下方向
    fourMean = np.zeros(4,np.float32)
    rows,cols = doG.shape
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            #左上方的均值
            leftTopMean = np.mean(doG[r-1:r+1,c-1:c+1])
            fourMean[0] = leftTopMean
            #右上方的均值
            rightTopMean = np.mean(doG[r-1:r+1,c:c+2])
            fourMean[1] = rightTopMean
            #左下方的均值
            leftBottomMean = np.mean(doG[r:r+2,c-1:c+1])
            fourMean[2] = leftBottomMean
            #右下方的均值
            rightBottomMean = np.mean(doG[r:r+2,c:c+2])
            fourMean[3] = rightBottomMean
            if(np.min(fourMean)*np.max(fourMean)<0):
                zero_cross[r][c] = 255
    return zero_cross
# Marr_Hildreth 邊緣檢測演算法
def Marr_Hildreth(image,size,sigma,k=1.1,crossType="ZERO_CROSS_DEFAULT"):
    #高斯差分
    doG = DoG(image,size,sigma,k)
    #過零點
    if crossType == "ZERO_CROSS_DEFAULT":
        zero_cross = zero_cross_default(doG)
    elif  crossType == "ZERO_CROSS_MEAN":
        zero_cross = zero_cross_mean(doG)
    else:
        print("no crossType")
    return zero_cross

#獲得比DoG更加細化的邊緣
image = cv2.imread('img6/flower.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",image)
# Marr-Hilreth 邊緣檢測演算法
result = Marr_Hildreth(image,(37,37),6,1.1,"ZERO_CROSS_MEAN")
cv2.imshow("Marr-Hildreth",result)
cv2.imwrite("MH.jpg",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

