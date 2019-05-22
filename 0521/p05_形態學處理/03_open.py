import cv2

I = cv2.imread('img5/OC.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow("I",I)
r, i= 1,1
MAX_R,MAX_I = 20,20
#顯示形態學處理的效果的視窗
cv2.namedWindow("morphology_OPEN",1)
def nothing(*arg):
    pass
#Scrollbar
cv2.createTrackbar("r","morphology_OPEN",r,MAX_R,nothing)
cv2.createTrackbar("i","morphology_OPEN",i,MAX_I,nothing)
while True:
    r = cv2.getTrackbarPos('r', 'morphology_OPEN')
    i = cv2.getTrackbarPos('i','morphology_OPEN')
    s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r,r))
    #print(s)
    d = cv2.morphologyEx(I,cv2.MORPH_TOPHAT,s,iterations=i)
    cv2.imshow("morphology_OPEN",d)
    cv2.imwrite("open.jpg",d)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
cv2.destroyAllWindows()

#頂帽運算MORPH_TOPHAT可以把8的數字拿出來 'img5/open.jpg'
#影像減去開運算
