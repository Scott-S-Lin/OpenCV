# -*- coding: utf-8 -*-
import cv2
import numpy as np
src1 = np.array([[255,0,255]])
src2 = np.array([[255,0,0]])
#與運算
dst_and = cv2.bitwise_and(src1,src2)
#或運算
dst_or = cv2.bitwise_or(src1,src2)
print("與運算的結果：")
print(dst_and)
print("或運算的結果：")
print(dst_or)
