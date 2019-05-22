# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal
import math
'''
    得到高斯平滑算子：
    getGaussKernel(sigma,H,W),使用过程中一般H和W一般为奇数，sigma大于零
'''

def getGaussKernel(sigma,H,W):
    '''
        第一步：构建高斯矩阵gaussMatrix
    '''
    gaussMatrix = np.zeros([H,W],np.float32)
    #得到中心点的位置
    cH = (H-1)/2
    cW = (W-1)/2
    #计算1/(2*pi*sigma^2)
    coefficient = 1.0/(2*np.pi*math.pow(sigma,2))
    #
    for r in range(H):
        for c in range(W):
            norm2 = math.pow(r-cH,2) + math.pow(c-cW,2)
            gaussMatrix[r][c] = coefficient*math.exp(-norm2/(2*math.pow(sigma,2)))
    '''
        第二步：计算高斯矩阵的和
    '''
    sumGM = np.sum(gaussMatrix)
    '''
        第三步：归一化，gaussMatrix/sumGM
    '''
    gaussKernel = gaussMatrix/sumGM
    return gaussKernel
