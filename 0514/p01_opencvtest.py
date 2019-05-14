# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:46:13 2019

@author: User
"""

import cv2

image2 = cv2.imread('spyder.jpg')
 
cv2.imshow('image',image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
