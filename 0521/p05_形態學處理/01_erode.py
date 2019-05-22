# -*- coding: utf-8 -*-

import cv2

#第一步：讀入圖像
I = cv2.imread('img5/frame36.jpg',cv2.IMREAD_GRAYSCALE)
#創建結構元 cv2.MORPH_RECT=矩形shape (5,5)mask size
s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
r = cv2.erode(I,s)#腐蝕圖像

#顯示原圖和腐蝕後的結果
cv2.imshow("I",I)
cv2.imshow("erode",r)
cv2.imwrite("erode.jpg",r)
cv2.waitKey(0)
cv2.destroyAllWindows()

