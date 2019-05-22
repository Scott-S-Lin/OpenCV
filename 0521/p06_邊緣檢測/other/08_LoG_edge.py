# -*- coding: utf-8 -*-
import sys
import numpy as np
import math
import cv2
from scipy import signal
#構建 LoG 運算元
def createLoGKernel(sigma,kSize):
    # LoG 運算元的寬高，且兩者均為奇數
    winH,winW = kSize
    logKernel = np.zeros(kSize,np.float32)
    #方差
    sigmaSquare = pow(sigma,2.0)
    # LoG 運算元的中心
    centerH = (winH-1)/2
    centerW = (winW-1)/2
    for r in range(winH):
        for c in range(winW):
            norm2 = pow(r-centerH,2.0) + pow(c-centerW,2.0)
            logKernel[r][c] = 1.0/sigmaSquare*(norm2/sigmaSquare - 2)*math.exp(-norm2/(2*sigmaSquare))
    return logKernel
#高斯拉普拉斯卷積，一般取 _boundary = 'symm'
def LoG(image,sigma,kSize,_boundary='fill',_fillValue = 0):
    #構建 LoG 卷積核
    loGKernel = createLoGKernel(sigma,kSize)
    #圖像與 LoG 卷積核卷積
    img_conv_log = signal.convolve2d(image,loGKernel,'same',boundary =_boundary)
    return img_conv_log

image = cv2.imread('img6/castle.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",image)
#高斯拉普拉斯卷積
img_conv_log = LoG(image,2,(13,13),'symm')
#邊緣的二值化顯示
edge_binary = np.copy(img_conv_log)
edge_binary[edge_binary>=0]=0
edge_binary[edge_binary<0]=255
edge_binary = edge_binary.astype(np.uint8)
cv2.imshow("edge_binary",edge_binary)
cv2.imwrite("edge1_binary_37_6.jpg",edge_binary)
cv2.waitKey(0)
cv2.destroyAllWindows() 
