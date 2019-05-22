# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
from fastMeanBlur import fastMeanBlur
#導向濾波
def guidedFilter(I,p,winSize,eps):
    #輸入圖像的寬高
    rows,cols = I.shape
    # I 的均值平滑
    mean_I = fastMeanBlur(I,winSize,cv2.BORDER_DEFAULT)
    # p 的均值平滑
    mean_p = fastMeanBlur(p,winSize,cv2.BORDER_DEFAULT)
    # I.*p 的均值平滑
    Ip = I*p
    mean_Ip = fastMeanBlur(Ip,winSize,cv2.BORDER_DEFAULT)
    #協方差
    cov_Ip = mean_Ip - mean_I*mean_p
    mean_II = fastMeanBlur(I*I,winSize,cv2.BORDER_DEFAULT)
    #方差
    var_I = mean_II - mean_I*mean_I
    a = cov_Ip/(var_I+eps)
    b = mean_p - a*mean_I
    # 對 a 和 b進行均值平滑
    mean_a = fastMeanBlur(a,winSize,cv2.BORDER_DEFAULT)
    mean_b = fastMeanBlur(b,winSize,cv2.BORDER_DEFAULT)
    q = mean_a*I + mean_b
    return q
#主函數
if __name__ =="__main__":

    I = cv2.imread('img3/img7.jpg',cv2.IMREAD_COLOR)
    p = cv2.imread('img3/img7.jpg',cv2.IMREAD_GRAYSCALE)
    #將圖像歸一化
    image_0_1 = I/255.0
    p = p/255.0
    #顯示原圖
    cv2.imshow("image_0_1",image_0_1)
    #導向濾波
    result = np.zeros(I.shape)
    result[:,:,0] = guidedFilter(image_0_1[:,:,0],image_0_1[:,:,0],(17,17),pow(0.2,2.0))
    result[:,:,1] = guidedFilter(image_0_1[:,:,1],image_0_1[:,:,1],(17,17),pow(0.2,2.0))
    result[:,:,2] = guidedFilter(image_0_1[:,:,2],image_0_1[:,:,2],(17,17),pow(0.2,2.0))
    cv2.imshow("guidedFilter",result)
    #保存導向濾波的結果
    result = result*255
    result[result>255] = 255
    result = np.round(result)
    result = result.astype(np.uint8)
    cv2.imwrite("guidedFilter.jpg",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
