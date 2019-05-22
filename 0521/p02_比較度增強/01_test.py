# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:05:46 2019

@author: User
"""

import numpy as np
I = np.array([[0,200],[23,4]],np.uint8)
O1=I*2
print(O1,O1.dtype)
O2=I*2.0
print(O2,O2.dtype)
 #所以進行線性轉換時，要特別注意不能簡單使用'*'