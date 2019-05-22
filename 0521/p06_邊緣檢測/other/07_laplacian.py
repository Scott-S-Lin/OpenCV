# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal
import cv2
import math
from gaussBlur import gaussBlur#高斯平滑
'''
    laplacian 邊緣檢測演算法:
    laplacian(image,_boundary='fill',_fillvalue=0)
    其中：邊緣處理的方式_boundary包括：'symm','wrap','fill',
    且當__boundary='fill'時，填充值默認為零_fillvalue=0
'''
def laplacian(image,_boundary='fill',_fillvalue=0):
    #拉普拉斯卷積核
    #laplacianKernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)
    laplacianKernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],np.float32)
    #圖像矩陣和拉普拉斯運算元卷積
    i_conv_lap = signal.convolve2d(image,laplacianKernel,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    return i_conv_lap


image = cv2.imread('img6/img.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image.jpg",image)
cv2.imwrite("image.jpg",image)
# ----- 第一種情形 ------
#圖像矩陣和拉普拉斯核進行卷積，然後進行閾值處理
i_conv_lap = laplacian(image,'symm')
i_conv_lap_copy = np.copy(i_conv_lap)
#i_conv_lap_copy[i_conv_lap_copy>0] = 255
#i_conv_lap_copy[i_conv_lap_copy<=0] = 150
i_conv_lap_copy = np.abs(i_conv_lap_copy)
i_conv_lap_copy += 125
i_conv_lap_copy[i_conv_lap_copy>255]=255
i_conv_lap_copy = i_conv_lap_copy.astype(np.uint8)
cv2.imshow("i_conv_lap",i_conv_lap_copy)
cv2.imwrite("i_cov_lap.jpg",i_conv_lap_copy)
#第五種情形

# ---- 第二種情形 ------
#對卷積結果取絕對值
i_conv_lap_abs = np.abs(i_conv_lap)
i_conv_lap_abs = np.round(i_conv_lap_abs)
i_conv_lap_abs[i_conv_lap_abs>255]=255
i_conv_lap_abs = i_conv_lap_abs.astype(np.uint8)
cv2.imshow("i_conv_lap_abs",i_conv_lap_abs)
#cv2.imwrite("i_cov_lap_abs.jpg",i_conv_lap_abs)

#圖像抽象化
rows,cols = imageBlur_conv_lap.shape
imageAbstraction = np.copy(imageBlur_conv_lap)
for r in range(rows):
    for c in range(cols):
        if imageAbstraction[r][c] > 0:
            imageAbstraction[r][c] = 1
        else:
            imageAbstraction[r][c] = 1+math.tanh(imageAbstraction[r][c])
cv2.imshow("imageAbstraction",imageAbstraction)
#轉換為 8 點陣圖，保存結果
imageAbstraction = 255*imageAbstraction
imageAbstraction = np.round(imageAbstraction)
imageAbstraction = imageAbstraction.astype(np.uint8)
cv2.imwrite("imageAbstraction.jpg",imageAbstraction)
cv2.waitKey(0)
cv2.destroyAllWindows() 
