import cv2  
import numpy as np  
       
img = cv2.imread('img2/image.png')  
h = np.zeros((256,256,3)) #創建用於繪製直方圖的全0圖像  
       
bins = np.arange(256).reshape(256,1) #直方圖中各bin的頂點位置  
color = [ (255,0,0),(0,255,0),(0,0,255) ] #BGR三種顏色  
for ch, col in enumerate(color):  
    originHist = cv2.calcHist([img],[ch],None,[256],[0,256])  
    cv2.normalize(originHist, originHist,0,255*0.9,cv2.NORM_MINMAX)  
    hist=np.int32(np.around(originHist))  
    pts = np.column_stack((bins,hist))  
    cv2.polylines(h,[pts],False,col)  
       
h=np.flipud(h)#反轉繪製好的直方圖，因為繪製時0,0在左上角
       
cv2.imshow('colorhist',h)  
cv2.waitKey(0) 
