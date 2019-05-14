# -*- coding: utf-8 -*-
import numpy as np

#冪指數
x1 = range(6)
print('x1^2 = ',np.power(x1, 2))

#冪指數的資料類型，對於power回傳的值影響很大
src = np.array([[25,40],[10,100]],np.uint8)
dst1 = np.power(src,2)
print('dst1:',dst1,sep='\n')
print(dst_a.dtype)
dst2 = np.power(src,2.0)
print('dst2:',dst2,sep='\n')
print(dst_a.dtype)
