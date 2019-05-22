# -*- coding: utf-8 -*-
import numpy as np
import math
import cv2
import sobel #注意sobel邊緣檢測(sobel的if __name__)

#canny改進sobel prewitt
#1.沒有充分利用邊緣的梯度方向
#2.設定值太大損失資訊 太小雜訊很多


#邊緣檢測
#非極大值抑制!
def non_maximum_suppression_default(dx,dy):
    #邊緣強度
    edgeMag = np.sqrt(np.power(dx,2.0) + np.power(dy,2.0))
    #寬、高
    rows,cols = dx.shape
    #梯度方向
    gradientDirection = np.zeros(dx.shape)
    #邊緣強度非極大值抑制
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            #angle 的範圍 [0,180] [-180,0]
            angle = math.atan2(dy[r][c],dx[r][c])/math.pi*180
            gradientDirection[r][c] = angle
            #左 / 右方向
            if(abs(angle)<22.5 or abs(angle) >157.5):
                if(edgeMag[r][c]>edgeMag[r][c-1] and edgeMag[r][c] > edgeMag[r][c+1]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #左上 / 右下方向  
            if(angle>=22.5 and angle < 67.5 or(-angle > 112.5 and -angle <= 157.5)):
                if(edgeMag[r][c] > edgeMag[r-1][c-1] and edgeMag[r][c]>edgeMag[r+1][c+1]):
                     edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #上 / 下方向
            if((angle>=67.5 and angle<=112.5) or (angle>=-112.5 and angle<=-67.5)):
                if(edgeMag[r][c] > edgeMag[r-1][c] and edgeMag[r][c] > edgeMag[r+1][c]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #右上 / 左下方向
            if((angle>112.5 and angle<=157.5) or(-angle>=22.5 and -angle< 67.5 )):
                if(edgeMag[r][c]>edgeMag[r-1][c+1] and edgeMag[r][c] > edgeMag[r+1][c-1]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
    return edgeMag_nonMaxSup
#非極大值抑制：插值比較
def non_maximum_suppression_Inter(dx,dy):
    #邊緣強度
    edgeMag = np.sqrt(np.power(dx,2.0)+np.power(dy,2.0))
    #寬、高
    rows,cols = dx.shape
    #梯度方向
    gradientDirection = np.zeros(dx.shape)
    #邊緣強度的非極大值抑制
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            if dy[r][c] ==0 and dx[r][c] == 0:
                continue
            #angle的範圍 [0,180],[-180,0]
            angle = math.atan2(dy[r][c],dx[r][c])/math.pi*180
            gradientDirection[r][c] = angle
            #左上方和上方的插值 右下方和下方的插值
            if (angle > 45 and angle <=90) or (angle > -135 and angle <=-90):
                ratio = dx[r][c]/dy[r][c]
                leftTop_top = ratio*edgeMag[r-1][c-1]+(1-ratio)*edgeMag[r-1][c]
                rightBottom_bottom = (1-ratio)*edgeMag[r+1][c] + ratio*edgeMag[r+1][c+1]
                if edgeMag[r][c] >  leftTop_top and edgeMag[r][c] > rightBottom_bottom:
                    edgeMag_nonMaxSup[r][c]  = edgeMag[r][c]
            #右上方和上方的插值 左下方和下方的插值
            if (angle>90 and angle<=135) or (angle>-90 and angle <= -45):
                ratio = abs(dx[r][c]/dy[r][c])
                rightTop_top = ratio*edgeMag[r-1][c+1] + (1-ratio)*edgeMag[r-1][c]
                leftBottom_bottom = ratio*edgeMag[r+1][c-1] + (1-ratio)*edgeMag[r+1][c]
                if edgeMag[r][c] > rightTop_top and edgeMag[r][c] > leftBottom_bottom:
                    edgeMag_nonMaxSup[r][c]  = edgeMag[r][c]
            #左上方和左方的插值 右下方和右方的插值
            if (angle>=0 and angle <=45) or (angle>-180 and angle <= -135):
                ratio = dy[r][c]/dx[r][c]
                rightBottom_right = ratio*edgeMag[r+1][c+1]+(1-ratio)*edgeMag[r][c+1]
                leftTop_left = ratio*edgeMag[r-1][c-1]+(1-ratio)*edgeMag[r][c-1]
                if edgeMag[r][c] > rightBottom_right and edgeMag[r][c] > leftTop_left:
                    edgeMag_nonMaxSup[r][c]  = edgeMag[r][c]
            #右上方和右方的插值 左下方和左方的插值
            if(angle>135 and angle<=180) or (angle>-45 and angle <=0):
                ratio = abs(dy[r][c]/dx[r][c])
                rightTop_right = ratio*edgeMag[r-1][c+1]+(1-ratio)*edgeMag[r][c+1]
                leftBottom_left = ratio*edgeMag[r+1][c-1]+(1-ratio)*edgeMag[r][c-1]
                if edgeMag[r][c] > rightTop_right and edgeMag[r][c] > leftBottom_left:
                    edgeMag_nonMaxSup[r][c]  = edgeMag[r][c]
    return edgeMag_nonMaxSup
#判斷一個點的座標是否在圖像範圍內
def checkInRange(r,c,rows,cols):
    if r>=0 and r<rows and c>=0 and c<cols:
        return True
    else:
        return False
def trace(edgeMag_nonMaxSup,edge,lowerThresh,r,c,rows,cols):
    #大於閾值為確定邊緣點
    if edge[r][c] == 0:
        edge[r][c]=255
        for i in range(-1,2):
            for j in range(-1,2):
                if checkInRange(r+i,c+j,rows,cols) and edgeMag_nonMaxSup[r+i][c+j] >= lowerThresh:
                    trace(edgeMag_nonMaxSup,edge,lowerThresh,r+i,c+j,rows,cols)
#滯後閾值
def hysteresisThreshold(edge_nonMaxSup,lowerThresh,upperThresh):
    #寬高
    rows,cols = edge_nonMaxSup.shape
    edge = np.zeros(edge_nonMaxSup.shape,np.uint8)
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            #大於高閾值，設置為確定邊緣點，而且以該點為起始點延長邊緣
            if edge_nonMaxSup[r][c] >= upperThresh:
                trace(edgeMag_nonMaxSup,edge,lowerThresh,r,c,rows,cols)
            #小於低閾值，被剔除
            if edge_nonMaxSup[r][c]< lowerThresh:
                edge[r][c] = 0
    return edge


image = cv2.imread('img6/canny.jpg',cv2.IMREAD_GRAYSCALE)
# ------- canny 邊緣檢測 -----------
#第一步： 基於 sobel 核的卷積
image_sobel_x,image_sobel_y = sobel.sobel(image,3)
#邊緣強度：兩個卷積結果對應位置的平方和
edge = np.sqrt(np.power(image_sobel_x,2.0) + np.power(image_sobel_y,2.0))
#邊緣強度的灰度級顯示
edge[edge>255] = 255
edge = edge.astype(np.uint8)
cv2.imshow("sobel edge",edge)
#第二步：非極大值抑制
edgeMag_nonMaxSup = non_maximum_suppression_default(image_sobel_x,image_sobel_y)
edgeMag_nonMaxSup[edgeMag_nonMaxSup>255] =255
edgeMag_nonMaxSup = edgeMag_nonMaxSup.astype(np.uint8)
cv2.imshow("edgeMag_nonMaxSup",edgeMag_nonMaxSup)
#第三步：雙閾值滯後閾值處理，得到 canny 邊緣
#滯後閾值的目的就是最後決定處於高閾值和低閾值之間的是否為邊緣點
edge = hysteresisThreshold(edgeMag_nonMaxSup,60,180)
lowerThresh = 40
upperThresh = 150
cv2.imshow("canny",edge)
cv2.imwrite("canny.jpg",edge)
# -------以下是為了單閾值與滯後閾值的結果比較 ------
#大於高閾值 設置為白色 為確定邊緣
EDGE = 255
#小於低閾值的設置為黑色 表示不是邊緣，被剔除
NOEDGE = 0
#而大於等於低閾值 小於高閾值的設置為灰色，標記為可能的邊緣
POSSIBLE_EDGE = 128
tempEdge = np.copy(edgeMag_nonMaxSup)
rows,cols = tempEdge.shape
for r in range(rows):
    for c in range(cols):
        if tempEdge[r][c]>=upperThresh:
            tempEdge[r][c] = EDGE
        elif tempEdge[r][c]<lowerThresh:
            tempEdge[r][c] = NOEDGE
        else:
            tempEdge[r][c] = POSSIBLE_EDGE
cv2.imshow("tempEdge",tempEdge)
lowEdge = np.copy(edgeMag_nonMaxSup)
lowEdge[lowEdge>60] = 255
lowEdge[lowEdge<60] = 0
cv2.imshow("lowEdge",lowEdge)
upperEdge = np.copy(edgeMag_nonMaxSup)
upperEdge[upperEdge>180]=255
upperEdge[upperEdge<=180]=0
cv2.imshow("upperEdge",upperEdge)
cv2.waitKey(0)
cv2.destroyAllWindows()
         
