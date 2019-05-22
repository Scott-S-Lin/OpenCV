# -*- coding: utf-8 -*-
import sys
import numpy as np
from scipy import signal
import cv2
#prewtt卷積
def prewitt(I,_boundary='symm',):
    #因為prewitt_X是可分離卷積核,根據卷積運算的結合律,可以分兩次小卷積核運算
    #1：垂直方向的 " 平均值平滑 "
    ones_y = np.array([[1],[1],[1]],np.float32)
    i_conv_pre_x = signal.convolve2d(I,ones_y,mode='same',boundary = _boundary)
    #2：水平方向的差分
    diff_x = np.array([[1,0,-1]],np.float32)
    i_conv_pre_x = signal.convolve2d(i_conv_pre_x,diff_x,mode='same',boundary = _boundary)
    #因為prewitt_y是可分離卷積核，根據卷積運算的結合律，可以分兩次小卷積核運算
    
    #1：水平方向的"均值平滑 "
    ones_x = np.array([[1,1,1]],np.float32)
    i_conv_pre_y = signal.convolve2d(I,ones_x,mode='same',boundary = _boundary)
    #2：垂直方向的差分
    diff_y = np.array([[1],[0],[-1]],np.float32)
    i_conv_pre_y = signal.convolve2d(i_conv_pre_y,diff_y,mode='same',boundary = _boundary)
    return (i_conv_pre_x,i_conv_pre_y)

image = cv2.imread('img6/bone.png',cv2.IMREAD_GRAYSCALE) 
#圖像矩陣 和 兩個 prewitt運算元 的卷積
i_conv_pre_x,i_conv_pre_y = prewitt(image)
#取絕對值,分別得到水準方向和垂直方向的邊緣強度
abs_i_conv_pre_x = np.abs(i_conv_pre_x)
abs_i_conv_pre_y = np.abs(i_conv_pre_y)    
#水準方向和垂直方向的邊緣強度的灰度級顯示
edge_x = abs_i_conv_pre_x.copy()
edge_y = abs_i_conv_pre_y.copy()
edge_x[edge_x>255]=255
edge_y[edge_y>255]=255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)
cv2.imshow("edge_x",edge_x)
cv2.imwrite("edge_x.jpg",edge_x)
cv2.imshow("edge_y",edge_y)
cv2.imwrite("edge_y.jpg",edge_y)
#利用 abs_i_conv_pre_x 和 abs_i_conv_pre_y 求最終的邊緣強度
#求邊緣強度，有多重方式，這裡使用的是插值法(改數值看看)
edge = 0.5*abs_i_conv_pre_x + 0.5*abs_i_conv_pre_y
#邊緣強度的灰度級顯示
edge[edge>255]=255
edge = edge.astype(np.uint8)
cv2.imshow('edge',edge)
cv2.imwrite("edge.jpg",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
