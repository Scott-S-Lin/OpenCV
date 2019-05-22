# -*- coding: utf-8 -*-
import numpy as np
import cv2
#主函數
src = np.array([[123,234,68],[33,51,17],[48,98,234],
                [129,89,27],[45,167,134]],np.uint8)
#手動設置閾值
the = 150
maxval = 255
dst = cv2.threshold(src,the,maxval,cv2.THRESH_BINARY)
# Otsu 閾值處理 
otsuThe = 0
otsuThe,dst_Otsu = cv2.threshold(src,otsuThe,maxval,cv2.THRESH_OTSU)
print(otsuThe)
print(dst_Otsu)
# TRIANGLE 閾值處理
triThe = 0
triThe,dst_tri = cv2.threshold(src,triThe,maxval,cv2.THRESH_TRIANGLE)
print(triThe)
print(dst_tri)