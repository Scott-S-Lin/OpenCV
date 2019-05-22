# -*- coding: utf-8 -*-
import cv2
import numpy as np
#點集
contour = np.array([[0,0],[50,30],[100,100],[100,0]],np.float32)
#判斷三個點和點集構成的輪廓的關係
dist1 = cv2.pointPolygonTest(contour,(80,40),False)
dist2 = cv2.pointPolygonTest(contour,(50,0),False)
dist3 = cv2.pointPolygonTest(contour,(40,80),False)
#列印結果(輪廓內、外、上)
print(dist1,dist2,dist3)
