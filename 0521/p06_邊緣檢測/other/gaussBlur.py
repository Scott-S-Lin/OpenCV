# -*- coding: utf-8 -*-
import gaussKernel #導入構建高斯核的包
import sys
import numpy as np
from scipy import signal
import cv2
#高斯平滑，返回的資料類型為浮點型
def gaussBlur(image,sigma,H,W,_boundary = 'fill',_fillvalue = 0):
    '''
    #構建HxW的高斯平滑運算元
    gaussKernelxy = gaussKernel.getGaussKernel(sigma,H,W)
    #圖像矩陣和高斯卷積核卷積
    gaussBlur_xy = signal.convolve2d(image,gaussKernelxy,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    return gaussBlur_xy
    '''
    #因為高斯核是可分解的，根據卷積的結合律
    #先進行水準方向的卷積，然後再進行垂直方向的卷積
    gaussKenrnel_x = gaussKernel.getGaussKernel(sigma,1,W)
    gaussBlur_x = signal.convolve2d(image,gaussKenrnel_x,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    gaussKenrnel_y = gaussKernel.getGaussKernel(sigma,H,1)
    gaussBlur_xy = signal.convolve2d(gaussBlur_x,gaussKenrnel_y,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    return gaussBlur_xy


