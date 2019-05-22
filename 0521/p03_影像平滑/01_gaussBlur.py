# -*- coding: utf-8 -*-
import gaussKernel #導入構建高斯核的包
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


image = cv2.imread('img3/cat.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",image)
cv2.imwrite("img4.jpg",image)
# 3 11 11 9 25 25
blurImage = gaussBlur(image,5,51,51,'symm')
#如果輸入的圖像是8點陣圖,輸出的
blurImage = np.round(blurImage)
blurImage = blurImage.astype(np.uint8)
cv2.imshow("gaussBlur",blurImage)
cv2.imwrite("gaussBlur.png",blurImage)
#如果輸入的圖像資料類型是浮點型，且圖元值歸一到[0,1]
image_0_1 = image/255.0
blurImage_0_1 = gaussBlur(image_0_1,4,5,5,'symm')
#cv2.imshow("gaussBlur-0-1",blurImage_0_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
