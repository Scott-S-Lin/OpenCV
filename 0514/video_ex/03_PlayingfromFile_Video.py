# -*- coding: utf-8 -*-

import cv2

cap = cv2.VideoCapture('output.avi') 

waitTime = 1
if cap.get(5) != 0:
    waitTime = int(1000.0 / cap.get(5))

while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break
    else:
        cv2.imshow("output.avi", frame)
        k = cv2.waitKey(waitTime) & 0xFF
        if k == 27: #esc key
            break

cap.release()
cv2.destroyAllWindows()
