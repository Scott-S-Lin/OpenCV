# -*- coding: utf-8 -*-

import numpy as np
x = np.array([[1,2,3],[4,5,6]], dtype=np.uint8)
y = np.array([[6,5],[4,3],[2,1]], dtype=np.uint8)
z = np.dot(x,y)
print('np.dot(x,y):',z,sep='\n')
print(z.dtype)

y = np.array([[6,5],[4,3],[2,1]], dtype=np.float32)
z = np.dot(x,y)
print('np.dot(x,y):',z,sep='\n')
print(z.dtype)
#傳回的資料型態與數值範圍大的類型相同

