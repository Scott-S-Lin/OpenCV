# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal
import cv2

def roberts(I,_boundary='fill',_fillvalue=0):
    #圖像的高、寬
    H1,W1=I.shape[0:2]
    #卷積核的尺寸
    H2,W2=2,2
    #卷積核 1 及 錨點的位置
    R1 = np.array([[1,0],[0,-1]],np.float32)
    kr1,kc1=0,0
    #計算 fuLl 卷積
    IconR1 = signal.convolve2d(I,R1,mode='full',boundary = _boundary,fillvalue=_fillvalue)
    IconR1=IconR1[H2-kr1-1:H1+H2-kr1-1,W2-kc1-1:W1+W2-kc1-1]
    #卷積核2
    R2 = np.array([[0,1],[-1,0]],np.float32)
    #先計算 full 卷積
    IconR2 = signal.convolve2d(I,R2,mode='full',boundary = _boundary,fillvalue=_fillvalue)
    #錨點的位置
    kr2,kc2 = 0,1
    #根據錨點的位置，截取 full卷積，從而得到 same 卷積
    IconR2=IconR2[H2-kr2-1:H1+H2-kr2-1,W2-kc2-1:W1+W2-kc2-1]
    return (IconR1,IconR2)


image = cv2.imread('img6/robert.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",image)
#卷積，注意邊界擴充一般採用 " symm "
IconR1,IconR2 = roberts(image,'symm')
#45度方向上的邊緣強度的灰度級顯示
IconR1 = np.abs(IconR1)
edge_45 = IconR1.astype(np.uint8)
cv2.imshow("edge_45",edge_45)
cv2.imwrite("img3_robert_135_edge.jpg",edge_45)
#135度方向上的邊緣強度
IconR2 = np.abs(IconR2)
edge_135 = IconR2.astype(np.uint8)
cv2.imshow("edge_135",edge_135)
cv2.imwrite("img3_robert_45_edge.jpg",edge_135)
#用平方和的開方衡量最後的輸出邊緣
edge = np.sqrt(np.power(IconR1,2.0) + np.power(IconR2,2.0))
edge = np.round(edge)
edge[edge>255] = 255
edge = edge.astype(np.uint8)
#顯示邊緣
cv2.imshow("edge",edge)
cv2.imwrite("img3_robert_edge.jpg",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
