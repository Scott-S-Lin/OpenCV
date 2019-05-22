# -*- coding: utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt
#長條圖正規化
#1、若輸入是 8 點陣圖 ，一般設置 O_min = 0，O_max = 255
#2、若輸入的是歸一化的圖像，一般設置 O_min = 0，O_max = 1
def histNormalized(InputImage,O_min = 0,O_max = 255):
    #得到輸入圖像的最小灰度值
    I_min = np.min(InputImage)
    #得到輸入圖像的最大灰度值
    I_max = np.max(InputImage)
    #得到輸入圖像的寬高
    rows,cols = InputImage.shape
    #輸出圖像
    OutputImage = np.zeros(InputImage.shape,np.float32)
    #輸出圖像的映射
    cofficient = float(O_max - O_min)/float(I_max - I_min)
    for r in range(rows):
        for c in range(cols):
            OutputImage[r][c] = cofficient*( InputImage[r][c] - I_min) + O_min
    return OutputImage


image = cv2.imread('img2/img_nor2.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",image)
#長條圖正規化
histNormResult = histNormalized(image)
#資料類型轉換，灰度級顯示
histNormResult = np.round(histNormResult)
histNormResult = histNormResult.astype(np.uint8)
#顯示長條圖正規化的圖片
cv2.imshow("histNormlized",histNormResult)
cv2.imwrite("histNormResult.jpg",histNormResult)
'''
#如果輸入圖像是歸一化的圖像
image_0_1 = image/255.0
#長條圖正規化
histNormResult = histNormalized(image_0_1,0,1)
#保存結果
histNormResult = 255.0*histNormResult
histNormResult = np.round(histNormResult)
histNormResult = histNormResult.astype(np.uint8)
'''
#顯示長條圖正規化後圖片的灰度長條圖
#組數
numberBins = 256
#計算灰度長條圖
rows,cols = image.shape
histNormResultSeq = histNormResult.reshape([rows*cols,])
histogram,bins,patch_image= plt.hist(histNormResultSeq,numberBins,facecolor='black',histtype='bar')
#設置坐標軸的標籤
plt.xlabel(u"gray Level")
plt.ylabel(u"number of pixels")
#設置坐標軸的範圍
y_maxValue = np.max(histogram)
plt.axis([0,255,0,y_maxValue])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows() 

