import cv2

# 選擇哪隻攝影機
cap = cv2.VideoCapture(0)

while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()

  # 顯示圖片
  cv2.imshow('frame', frame)

  # Operations on the frame 
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
