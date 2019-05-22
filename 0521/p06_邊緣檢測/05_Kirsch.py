# -*- coding: utf-8 -*-
import sys
import numpy as np
from scipy import signal
import cv2
'''
    Krisch邊緣檢測演算法:
    krisch(image,_boundary='fill',_fillvalue=0)
    其中:邊緣處理的方式_boundary包括：'symm','wrap','fill',
    且當__boundary='fill'時,填充值默認為零_fillvalue=0
'''
def krisch(image,_boundary='fill',_fillvalue=0):
    '''
    第一步:8個krisch邊緣卷積運算元分別和圖像矩陣進行卷積,然後分別取絕對值得到邊緣強度
    '''
    #存儲8個方向的邊緣強度
    list_edge=[]
    #圖像矩陣和k1進行卷積,然後取絕對值（即:得到邊緣強度）
    k1 = np.array([[5,5,5],[-3,0,-3],[-3,-3,-3]])
    image_k1 = signal.convolve2d(image,k1,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k1))
    #圖像矩陣和k2進行卷積,然後取絕對值（即:得到邊緣強度）
    k2 = np.array([[-3,-3,-3],[-3,0,-3],[5,5,5]])
    image_k2 = signal.convolve2d(image,k2,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k2))
    #圖像矩陣和k3進行卷積,然後取絕對值（即:得到邊緣強度）
    k3 = np.array([[-3,5,5],[-3,0,5],[-3,-3,-3]])
    image_k3 = signal.convolve2d(image,k3,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k3))
    #圖像矩陣和k4進行卷積,然後取絕對值（即:得到邊緣強度）
    k4 = np.array([[-3,-3,-3],[5,0,-3],[5,5,-3]])
    image_k4 = signal.convolve2d(image,k4,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k4))
    #圖像矩陣和k5進行卷積,然後取絕對值（即:得到邊緣強度）
    k5 = np.array([[-3,-3,5],[-3,0,5],[-3,-3,5]])
    image_k5 = signal.convolve2d(image,k5,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k5))
    #圖像矩陣和k6進行卷積,然後取絕對值（即:得到邊緣強度）
    k6 = np.array([[5,-3,-3],[5,0,-3],[5,-3,-3]])
    image_k6 = signal.convolve2d(image,k6,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k6))
    #圖像矩陣和k7進行卷積,然後取絕對值（即:得到邊緣強度）
    k7 = np.array([[-3,-3,-3],[-3,0,5],[-3,5,5]])
    image_k7 = signal.convolve2d(image,k7,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k7))
    #圖像矩陣和k8進行卷積,然後取絕對值（即:得到邊緣強度）
    k8 = np.array([[5,5,-3],[5,0,-3],[-3,-3,-3]])
    image_k8 = signal.convolve2d(image,k8,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k8))
    '''
    第二步：對上述8個方向的邊緣強度,對應位置取最大值，作為圖像最後的邊緣強度
    '''
    edge = list_edge[0]
    for i in range(len(list_edge)):
        edge = edge*(edge>=list_edge[i]) + list_edge[i]*(edge < list_edge[i])
    return edge


image = cv2.imread('img6/kirsch.jpg',cv2.IMREAD_GRAYSCALE)
edge = krisch(image,_boundary='symm')
#邊緣強度的灰度級顯示
rows,cols = edge.shape
for r in range(rows):
    for c in range(cols):
        if edge[r][c] >255:
            edge[r][c] = 255
edge = edge.astype(np.uint8)
cv2.imshow("edge",edge)
cv2.imwrite("edge.jpg",edge)
#經過閾值處理的邊緣顯示
cv2.namedWindow("thresh_edge",1)
MAX_THRESH = 255
thresh = 255
#回呼函數，閾值處理
def callback_thresh(_thresh):
    threshEdge = edge.copy()
    threshEdge[threshEdge < _thresh] = 0
    threshEdge[threshEdge >= _thresh] = 255
    cv2.imshow("thresh_edge",threshEdge)
    cv2.imwrite("thresh_edge.jpg",threshEdge)
callback_thresh(thresh)
cv2.createTrackbar("thresh","thresh_edge",thresh,MAX_THRESH,callback_thresh)
#模擬素描
pencilSketch = edge.copy()
pencilSketch = 255 - pencilSketch
pencilSketch[pencilSketch<50] = 50
cv2.imshow("pencilSketch",pencilSketch)
cv2.imwrite("pencilSketch.jpg",pencilSketch)
cv2.waitKey(0)
cv2.destroyAllWindows() 
