import cv2

I = cv2.imread('img5/OC.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow("I",I)
#結構元半徑，反覆運算次數
r, i= 1,1
MAX_R,MAX_I = 20,20

cv2.namedWindow("morphology_CLOSE",1)
def nothing(*arg):
    pass
cv2.createTrackbar("r","morphology_CLOSE",r,MAX_R,nothing)
cv2.createTrackbar("i","morphology_CLOSE",i,MAX_I,nothing)
while True:
    r = cv2.getTrackbarPos('r', 'morphology_CLOSE')
    i = cv2.getTrackbarPos('i','morphology_CLOSE')
    s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r,r))
    d = cv2.morphologyEx(I,cv2.MORPH_CLOSE,s,iterations=i)
    #顯示效果
    cv2.imshow("morphology_CLOSE",d)
    cv2.imwrite("close.jpg",d)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
cv2.destroyAllWindows()
#底帽運算MORPH_BLACKHAT可以把骰子抽取出來 'img5/close.jpg'
#影像減去閉運算