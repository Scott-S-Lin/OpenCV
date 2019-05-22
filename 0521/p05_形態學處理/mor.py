# -*- coding: utf-8 -*-

import cv2
I = cv2.imread('img5/frame36.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("I",I)
#結構元半徑
r, i= 1,1
MAX_R,MAX_I = 20,20
cv2.namedWindow("morphology",1)
def nothing(*arg):
    pass
cv2.createTrackbar("r","morphology",r,MAX_R,nothing)
cv2.createTrackbar("i","morphology",i,MAX_I,nothing)
while True:
    r = cv2.getTrackbarPos('r', 'morphology')
    i = cv2.getTrackbarPos('i','morphology')
    #創建結構元
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(2*r+1,2*r+1))#結構元基數
    #形態學處理 型態梯度
    d = cv2.morphologyEx(I,cv2.MORPH_GRADIENT,s,iterations=i)
    cv2.imshow("morphology",d)
    cv2.imwrite("open.jpg",d)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
cv2.destroyAllWindows()
#膨脹結果-侵蝕結果,G = (I+S) - (I-S)
#很像邊緣梯度