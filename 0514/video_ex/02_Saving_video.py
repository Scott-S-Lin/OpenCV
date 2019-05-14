# -*- coding: utf-8 -*-

import cv2

cap = cv2.VideoCapture(0) # Reading from the in-built camera

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480)) # Saving the recorded video into avi file type name output

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        #flip the frame of the video
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)
        
        #show the recorded video to the user
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
