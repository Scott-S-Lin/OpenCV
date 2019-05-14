# -*- coding: utf-8 -*-
import cv2
import os

a = int(input('請輸入選項(1.錄製新影像,2.開啟舊影像,3.轉換影像為圖檔)：'))
while True:
    if a ==1:
        cap = cv2.VideoCapture(0) # Reading from the in-built camera
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
        # Saving the recorded video into avi file type name output
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                out.write(frame)
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
    elif a==2:
        cap = cv2.VideoCapture('output.avi') # Create a VideoCapture object to open the video named output

        waitTime = 1
        if cap.get(5) != 0:
            waitTime = int(1000.0 / cap.get(5))

        while cap.isOpened():
            ret, frame = cap.read()
            if frame is None:
                break
            else:
                cv2.imshow("output.avi", frame)
                # 注意wait的時間必須是int
                k = cv2.waitKey(waitTime) & 0xFF
                if k == 27:
                    break
        # Release everything if job is finished
        cap.release()
        cv2.destroyAllWindows()

    elif a==3:
        video_file_name='output' 
        vidcap = cv2.VideoCapture(video_file_name+'.avi')
        success,image = vidcap.read() 

        if success:
            if not os.path.exists(video_file_name): 
                os.makedirs(video_file_name)
        count = 0;
        while success:
          success,image = vidcap.read()
          cv2.imwrite(video_file_name+"/frame%d.jpg" % count, image)
          if cv2.waitKey(10) == 27:
              break
          count += 1
        
    else:
        print('選項輸入錯誤，請重新輸入')
    ex = input('是否要離開程式(Y/N)？')
    if ex=='Y':
        break
    else:
        a = int(input('請輸入選項(1.錄製新影像,2.開啟舊影像,3.轉換影像為圖檔 )：'))
