# -*- coding: utf-8 -*-
import cv2
import numpy as np

#img1-3
image = cv2.imread("img2/img1.jpg",cv2.IMREAD_GRAYSCALE)
MAX_VALUE = 120
value = 120
#調整對比度後，圖像的效果顯示視窗
cv2.namedWindow("contrast",cv2.WND_PROP_AUTOSIZE)
#調整係數，觀察圖像的變化
def callback_contrast(_value):
    #通過線性運算，調整圖像對比度
    a = float(_value)/40.0
    contrastImage = a*image
    contrastImage[contrastImage>255]=255
    contrastImage = np.round(contrastImage)
    contrastImage = contrastImage.astype(np.uint8)
    cv2.imshow("contrast",contrastImage)
    cv2.imwrite("contrast.jpg",contrastImage)
    
callback_contrast(value)
cv2.createTrackbar("value","contrast",value,MAX_VALUE,callback_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
