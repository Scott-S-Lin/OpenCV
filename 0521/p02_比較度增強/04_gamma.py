# -*- coding: utf-8 -*-
import cv2
import numpy as np


image = cv2.imread('img2/img_gama.jpg',cv2.IMREAD_GRAYSCALE)
MAX_VALUE = 200
value = 40
segValue = float(value)
#伽馬調整需要先將圖像歸一化
image_0_1 = image/255.0
#伽馬調整後的圖像顯示視窗
cv2.namedWindow("gamma_contrast",cv2.WND_PROP_AUTOSIZE)
#調整 gamma 值，觀察圖像的變換
def callback_contrast(_value):
    gamma = float(_value)/segValue
    contrastImage = np.power(image_0_1,gamma)
    cv2.imshow("gamma_contrast",contrastImage)
    #保存伽馬調整的結果
    contrastImage*=255
    contrastImage = np.round(contrastImage)
    contrastImage = contrastImage.astype(np.uint8)
    cv2.imwrite("gamma.jpg",contrastImage)
callback_contrast(value)
cv2.createTrackbar("value","gamma_contrast",value,MAX_VALUE,callback_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
