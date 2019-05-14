# -*- coding: utf-8 -*-

import cv2

# Create a VideoCapture object to capture the video from the in-built camera
cap = cv2.VideoCapture(0) # 0 represents the in-built camera (It can also be changed to the name of a video file or other camera)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() #ret is boolean value (True for frame reading correctly otherwise False)

    #print('ret',ret)
    #print('frame', frame)
    # Operations on the frame 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Change the video into black and grey

    # Display the resulting frame
    cv2.imshow('frame',gray) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
