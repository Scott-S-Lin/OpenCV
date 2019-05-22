# -*- coding: utf-8 -*-
import numpy as np
import cv2
#主函數
if __name__ == "__main__":
    #黑色畫板 400 x 400
    s = 400
    I = np.zeros((s,s),np.uint8)
    #隨機生成 橫縱坐標均在 100 至 300 的座標點
    n=80#隨機生成 n 個座標點，每一行存儲一個座標
    points = cv2.imread('img7/hand.jpg',cv2.IMREAD_GRAYSCALE)
    #把上述點集處的灰度值設置為 255,單個白色圖元點不容易觀察，用一個小圓標注一下
    for i in range(n):
        cv2.circle(I,(points[i,0],points[i,1]),2,255,2)
    #求點集 points 的凸包
    convexhull = cv2.convexHull(points,clockwise=False)
    # ----- 列印凸包的資訊 ----
    print (type(convexhull))
    print (convexhull.shape)
    #連接凸包的各個點
    k = convexhull.shape[0]
    for i in range(k-1):
        cv2.line(I,(convexhull[i,0,0],convexhull[i,0,1]),(convexhull[i+1,0,0],convexhull[i+1,0,1]),255,2)
    #首尾相接
    cv2.line(I,(convexhull[k-1,0,0],convexhull[k-1,0,1]),(convexhull[0,0,0],convexhull[0,0,1]),255,2)
    #顯示圖片
    cv2.imshow("I",I)
    cv2.imwrite("I.jpg",I)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
