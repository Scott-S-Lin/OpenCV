  # -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:36:45 2019

@author: User
"""
import cv2 
flags=[i for i in dir(cv2) if i.startswith('COLOR_')] 
print (flags)
