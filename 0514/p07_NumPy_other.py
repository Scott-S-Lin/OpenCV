# -*- coding: utf-8 -*-
import numpy as np


#log是以e為底
a = np.array([[6,5],[4,3]], dtype=np.uint8)
dst_a = np.log(a)
print('np.log(a):',dst_a,sep='\n')
#ndarray可以為任意資料類型，回傳值型態為float或double
print(dst_a.dtype)


x = [1,2,9,10, 16]
print("exp()---->", np.exp(x))          # e^x
print("exp2()---->", np.exp2(x))        # 2^x
print("power()---->", np.power(3, x))   # 3^x
print("log()---->", np.log(x))          # log自然對數
print("log2()---->", np.log2(x))        # 以2為基底的對數
print("log10()---->", np.log10(x))      # 以10為基底的對數



