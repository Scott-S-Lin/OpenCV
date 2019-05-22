# -*- coding: utf-8 -*-
import cv2
import numpy as np


if __name__ =="__main__":
    #旋轉矩形
    vertices = cv2.boxPoints(((200, 200), (90, 150), -60.0))
    #四個頂點
    print(vertices.dtype)#列印資料類型
    print(vertices)#列印四個頂點
    #根據四個頂點在黑色畫板上畫出該矩形
    img=np.zeros((400,400),np.uint8)
    for i in range(4):
        #相鄰的點
        p1 = vertices[i,:]
        j = (i+1)%4
        p2 = vertices[j,:]
        #畫出直線
        cv2.line(img,(p1[0],p1[1]),(p2[0],p2[1]),255,2)
    cv2.imshow("img",img)
    cv2.imwrite("boxPoints.jpg",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
