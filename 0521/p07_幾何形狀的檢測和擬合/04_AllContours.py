# -*- coding: utf-8 -*-
import numpy as np
import cv2
#主函數
if __name__ =="__main__":
    img = cv2.imread('img7/control.jpg',cv2.IMREAD_GRAYSCALE)
    #第二步：邊緣檢測 或者 閾值處理 生成一張二值圖
    img = cv2.GaussianBlur(img,(3,3),0.5)#高斯平滑處理
    binaryImg = cv2.Canny(img,50,200)
    cv2.imshow("binaryImg",binaryImg)
    #第三步：邊緣的輪廓，返回的 contours 是一個 list 列表
    hc = cv2.findContours(binaryImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = hc[1]
    #輪廓的數量
    n =  len(contours)
    contoursImg = []
    #畫出找到的輪廓
    for i in range(n):
        #創建一個黑色畫布
        temp = np.zeros(binaryImg.shape,np.uint8)
        contoursImg.append(temp)
        #在第 i 個黑色畫布上，畫第 i 個輪廓
        img = cv2.drawContours(img,contours,i,255,2)
    cv2.imshow("contour-",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
     

