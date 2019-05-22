# -*- coding: utf-8 -*-

import numpy as np
import cv2

image = cv2.imread('img4/img.jpg',cv2.IMREAD_GRAYSCALE)
#手動設置閾值 #cow.jpg(134) dog.jpg ship.jpg
thresh = 100
maxval = 255
threshImage_out = image.copy()
threshImage_out[threshImage_out > thresh] = 255
threshImage_out[threshImage_out <= thresh] = 0
dst = cv2.threshold(image,thresh,maxval,cv2.THRESH_BINARY)

cv2.imshow("image",image)
cv2.imshow("threshTwoPeaks",threshImage_out)
cv2.waitKey(0)
cv2.destroyAllWindows()