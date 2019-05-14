import numpy as np
import cv2

#加法運算-1
src1 = np.array([[1,2,3],[4,5,6]],np.uint8)
src2 = np.array([[1,1,1],[2,2,2]],np.uint8)
dst = src1+src2
print('dst1:',dst)
print(dst.dtype)

#加法運算-2
src3 = np.array([[23,123,90],[100,250,0]],np.uint8)
src4 = np.array([[125,150,60],[100,10,40]],np.uint8)
dst2 = src3+src4
# array對大於255的uchar類型，將該數255取模運算後減1
# 273 % 255 - 1 = 17
print('dst2:',dst2)
print(dst2.dtype)

#加法運算-3
src3 = np.array([[23,123,90],[100,250,0]],np.uint8)
src4 = np.array([[125,150,60],[100,10,40]],np.float32)
dst3 = src3+src4
print('dst3:',dst3)
print(dst3.dtype)

#加法運算-4
dst4 = cv2.add(src3,src4,dtype=cv2.CV_32F)
print('dst4:',dst4)
print(dst4.dtype)
