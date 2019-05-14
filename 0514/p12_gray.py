# -*- coding: utf-8 -*-

import cv2
import numpy as np

image = cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)
   
#img = cv2.imread()
print(image.shape)
cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()