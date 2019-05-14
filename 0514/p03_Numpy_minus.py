import numpy as np
import cv2

#減法運算-1
src1 = np.array([[23,123,90],[100,250,0]],np.uint8)
src2 = np.array([[125,150,60],[100,10,40]],np.uint8)
dst = src1-src2
print('dst:',dst)
print(dst.dtype)
# Numpy的處理方式，將該數255取模運算後加1
# -102 % 255 + 1 = 154

#Mat處理轉為uchar類型時，數值自動截斷為0
#[[0,0,30][0,240,0]]

#減法運算-2
src1 = np.array([[23,123,90],[100,250,0]],np.uint8)
src2 = np.array([[125,150,60],[100,10,40]],np.uint8)
dst2 = cv2.subtract(src1,src2)
print('dst2:',dst2)
print(dst2.dtype)

#減法運算-3
dst3 = cv2.subtract(src1,src2,dtype = cv2.CV_32F)
print('dst3:',dst3)
print(dst3.dtype)