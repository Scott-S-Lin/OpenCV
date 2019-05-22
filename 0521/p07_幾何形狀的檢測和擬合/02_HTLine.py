# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#霍夫極座標變換：直線檢測
def HTLine (image,stepTheta=1,stepRho=1):
    #寬、高
    rows,cols = image.shape
    #圖像中可能出現的最大垂線的長度
    L =  round(math.sqrt(pow(rows-1,2.0)+pow(cols-1,2.0)))+1
    #初始化投票器
    numtheta = int(180.0/stepTheta)
    numRho = int(2*L/stepRho + 1)
    accumulator = np.zeros((numRho,numtheta),np.int32)
    #建立字典
    accuDict={}
    for k1 in range(numRho):
        for k2 in range(numtheta):
            accuDict[(k1,k2)]=[]
    #投票計數
    for y in range(rows):
        for x  in range(cols):
            if(image[y][x] == 255):#只對邊緣點做霍夫變換
                for m in range(numtheta):
                    #對每一個角度，計算對應的 rho 值
                    rho = x*math.cos(stepTheta*m/180.0*math.pi)+y*math.sin(stepTheta*m/180.0*math.pi)
                    #計算投票哪一個區域
                    n = int(round(rho+L)/stepRho)
                    #投票加 1
                    accumulator[n,m] += 1
                    #記錄該點
                    accuDict[(n,m)].append((x,y))
    return accumulator,accuDict


I = cv2.imread('img7/road.jpg',cv2.IMREAD_GRAYSCALE)
#canny 邊緣檢測
edge = cv2.Canny(I,50,200)
#顯示二值化邊緣
cv2.imshow("edge",edge)
#霍夫直線檢測
accumulator,accuDict = HTLine(edge,1,1)
#計數器的二維長條圖方式顯示
rows,cols = accumulator.shape
fig = plt.figure()
ax = fig.gca(projection='3d')
X,Y = np.mgrid[0:rows:1, 0:cols:1]
surf = ax.plot_wireframe(X,Y,accumulator,cstride=1, rstride=1,color='gray')
ax.set_xlabel(u"$\\rho$")
ax.set_ylabel(u"$\\theta$")
ax.set_zlabel("accumulator")
ax.set_zlim3d(0,np.max(accumulator))
#計數器的灰度級顯示
grayAccu = accumulator/float(np.max(accumulator))
grayAccu = 255*grayAccu
grayAccu = grayAccu.astype(np.uint8)
#只畫出投票數大於 60 直線
voteThresh = 60
for r in range(rows):
    for c in range(cols):
        if accumulator[r][c] > voteThresh:
            points = accuDict[(r,c)]
            cv2.line(I,points[0],points[len(points)-1],(255),2)
cv2.imshow('accumulator',grayAccu)

#顯示原圖
cv2.imshow("I",I)
plt.show()
cv2.imwrite('accumulator.jpg',grayAccu)
cv2.imwrite('I.jpg',I)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
