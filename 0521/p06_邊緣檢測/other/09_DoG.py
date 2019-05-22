# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
from scipy import signal
import math
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
    yr = np.array(xc, dtype=np.float64)
    yr -= (H-1)/2
    yk = np.exp(-np.power(yr,2.0)/(2.0*pow(sigma,2.0)))
    # I_xk 與 yk 卷積
    I_xk_yk = signal.convolve2d(I_xk,yk,'same','symm')
    I_xk_yk *= 1.0/(2*np.pi*pow(sigma,2.0))
    return I_xk_yk
    #
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
#主函數

image = cv2.imread('img6/flower.jpg',cv2.IMREAD_GRAYSCALE)  
cv2.imshow("image",image)
#高斯差分邊緣檢測
sigma = 2
k = 0.8
size = (13,13)
imageDoG = DoG(image,size,sigma,k)
#二值化邊緣，對 imageDoG 閾值處理
edge = np.copy(imageDoG)
edge[edge>0] = 255
edge[edge<=0] = 0
edge = edge.astype(np.uint8)
cv2.imshow("edge",edge)
cv2.imwrite("edge.jpg",edge)
#圖像邊緣抽象化
asbstraction = -np.copy(imageDoG)
asbstraction = asbstraction.astype(np.float32)
asbstraction[asbstraction>=0]=1.0
asbstraction[asbstraction<0] = 1.0+ np.tanh(asbstraction[asbstraction<0])
cv2.imshow("asbstraction",asbstraction)
asbstraction = asbstraction*255
asbstraction = asbstraction.astype(np.uint8)
cv2.imwrite("asbstraction.jpg",asbstraction)
cv2.waitKey(0)
cv2.destroyAllWindows() 
