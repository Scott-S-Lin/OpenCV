# -*- coding: utf-8 -*-
import numpy as np
import cv2

image = cv2.imread('img1.jpg',cv2.IMREAD_COLOR)

#顯示原圖
cv2.imshow("image",image)
#圖像歸一化，轉換成浮點數
fImg = image.astype(np.float32)
fImg = fImg/255.0
#顏色空間轉換
hlsImg = cv2.cvtColor(fImg,cv2.COLOR_BGR2HLS)
l = 100 
s = 100
MAX_VALUE = 100
cv2.namedWindow("l and s",cv2.WINDOW_AUTOSIZE)

def nothing(*arg):
    pass

cv2.createTrackbar("l","l and s",l,MAX_VALUE,nothing)
cv2.createTrackbar("s","l and s",s,MAX_VALUE,nothing)
#調整飽和度和亮度後的效果
lsImg = np.zeros(image.shape,np.float32)
#調整飽和度和亮度
while True:  #複製
    hlsCopy = np.copy(hlsImg)
    #得到 l 和 s 的值
    l = cv2.getTrackbarPos('l', 'l and s')
    s = cv2.getTrackbarPos('s', 'l and s')
    #調整飽和度和亮度的控制項（線性變換）
    hlsCopy[:,:,1] = (1.0+l/float(MAX_VALUE))*hlsCopy[:,:,1]
    hlsCopy[:,:,1][hlsCopy[:,:,1]>1] = 1
    hlsCopy[:,:,2] = (1.0+s/float(MAX_VALUE))*hlsCopy[:,:,2]
    hlsCopy[:,:,2][hlsCopy[:,:,2]>1] = 1
    # HLS2BGR
    lsImg = cv2.cvtColor(hlsCopy,cv2.COLOR_HLS2BGR)
    #顯示調整後的效果
    cv2.imshow("l and s",lsImg)
    #儲存結果
    lsImg = lsImg*255
    lsImg = lsImg.astype(np.uint8)
    cv2.imwrite("lsImg.jpg",lsImg)
    ch = cv2.waitKey(5) #Esc key to stop
    if ch == 27:
        break
cv2.destroyAllWindows()
	
