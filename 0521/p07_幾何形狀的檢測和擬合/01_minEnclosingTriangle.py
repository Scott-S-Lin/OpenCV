# -*- coding: utf-8 -*-
import numpy as np
import cv2
#主函數
if __name__ == "__main__":
    points = np.array ([[[1,1]],[[5,10]],[[5,1]],[[1,10]],[[2,5]]] ,np.float32)
    #points = np.array ([[1,1],[5,10],[5,1],[1,10],[2,5]] ,np.float32)
    #最小外包直立矩形
    area,triangle = cv2.minEnclosingTriangle(points)
    #cv2.boundingRect(points)
    #列印面積
    print(area)
    #列印三角形的三個頂點
    print(triangle)
   # print type(triangle)
   # print triangle.dtype
     
