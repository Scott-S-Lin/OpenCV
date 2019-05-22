# -*- coding: utf-8 -*-
import sys
import numpy as np
from scipy import signal
import cv2
#均值平滑
def meanBlur(image,H,W,_boundary='fill',_fillvalue=0):
    #H、W均不為零
    if H==0 or W==0:
        print( 'W or H is not zero')
        return image
    
    #-------沒有對均值平滑運算元進行分離
    #meanKernel = 1.0/(H*W)*np.ones([H,W],np.float32)
    #result = signal.convolve2d(image,meanKernel,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    #-----卷積後進行資料類型轉換,得到均值平滑的結果
    #result = result.astype(np.uint8)
    #return result
    
    #因為均值運算元是可分離的卷積核，根據卷積運算的結合律
    #可以先進行水準方向的卷積，
    #再進行垂直方向的卷積
    #首先水準方向的均值平滑
    meanKernel_x = 1.0/W*np.ones([1,W],np.float32)
    i_conv_mk_x = signal.convolve2d(image,meanKernel_x,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    #然後對得到的水準卷積的結果再進行垂直方向的卷積
    meanKernel_y = 1.0/H*np.ones([H,1],np.float32)
    i_conv_xy = signal.convolve2d(i_conv_mk_x,meanKernel_y,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    i_conv_xy = np.round(i_conv_xy)
    #卷積後的結果進行資料類型轉換，得到均值平滑的結果
    result = i_conv_xy.astype(np.uint8)
    return result

#主函數:示例
if __name__ =="__main__":
    
    image = cv2.imread('img3/cat.png',cv2.IMREAD_GRAYSCALE)
    #均值濾波卷積核的寬高均設為 2*halfWinSize+1
    halfWinSize = 1
    MAX_HALFWINSIZE = 20
    cv2.namedWindow("meanBlur",1)
    #回呼函數，均值濾波
    def callback_meanBlur(_halfWinSize):
        result = meanBlur(image,2*_halfWinSize+1,2*_halfWinSize+1,_boundary='symm',_fillvalue=0)
        cv2.imshow("meanBlur",result)
    callback_meanBlur(halfWinSize)
    cv2.createTrackbar("winSize/2","meanBlur",halfWinSize,MAX_HALFWINSIZE,callback_meanBlur)
    #
    latexImage = meanBlur(image,29,29,'symm')
    cv2.imwrite("latexImage.png",latexImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
