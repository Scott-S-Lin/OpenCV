# -*- coding: utf-8 -*-
import cv2
import os 

video_file_name='output' # The name of the video file
vidcap = cv2.VideoCapture(video_file_name+'.avi') # The default type of the video is avi (can be changed)
success,image = vidcap.read() # Success will be True if the video can be read

if success:
    if not os.path.exists(video_file_name): # Check if there exist a directory(folder) to save the files converted from the video
        os.makedirs(video_file_name) # If there is no existing direcctory to save the files converted from the video, creat one 
count = 0;
while success:
  success,image = vidcap.read()
  cv2.imwrite(video_file_name+"/frame%d.jpg" % count, image)# Save frame as JPEG file into the directory
  if cv2.waitKey(10) == 27: # Exit if Escape is hit
      break
  count += 1
