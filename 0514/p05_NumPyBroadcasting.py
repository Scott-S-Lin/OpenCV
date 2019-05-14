# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:37:04 2019

@author: User
"""

import numpy as np
c = np.array([1.0, 2.0, 3.0])
d = 2
dst = c * d
print(dst)

#線代概念
x = np.arange(4)
print('x:',x,sep='\n')
x2 = x.reshape(4,1)
print('x2:',x2,sep='\n')
y = np.ones(5)
print('y:',y,sep='\n')
print('x2+y:',x2+y,sep='\n')