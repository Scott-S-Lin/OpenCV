# -*- coding: utf-8 -*-
import numpy as np
import cv2
import sys
import math
#主函數
if __name__ == "__main__":
   
        #image = cv2.imread(sys.argv[1],cv2.CV_LOAD_IMAGE_GRAYSCALE)#OpenCV2.X
    image = cv2.imread("img01.jpg",cv2.IMREAD_GRAYSCALE)#OpenCV3.X

    #原圖的高寬
    h,w=image.shape[:2]
    #仿射變換矩陣，縮小兩倍
    A1 = np.array([[0.5,0,0],[0,0.5,0]],np.float32)
    #仿射函數cv2.warpAffine()接受三個參數，需要圖像、變換矩陣、變換後的大小
    d1 = cv2.warpAffine(image,A1,(w,h),borderValue=125)
    #先縮小兩倍，再平移
    A2 = np.array([[0.5,0,w/4],[0,0.5,h/4]],np.float32)
    d2 = cv2.warpAffine(d1,A2,(w,h),borderValue=255)
    #在 d2 的基礎上，繞圖像的中心點旋轉(逆時針30度)
    A3 = cv2.getRotationMatrix2D((w/2,h/2),30,1)
    d3 = cv2.warpAffine(d2,A3,(w,h),borderValue=125)
    
    cv2.imshow("image",image)
    cv2.imshow("d1",d1)
    cv2.imshow("d2",d2)
    cv2.imshow("d3",d3)
    #cv2.imwrite("d3.jpg",d3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
