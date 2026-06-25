import cv2 as cv
import os

# 1. 素材影片
video_path = 'demo_video.mp4' 

# 確認有沒有檔案
if not os.path.exists('haarcascade_fullbody.xml'):
    print("錯誤：找不到模型檔")
    exit()

cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')


cap = cv.VideoCapture(video_path)

print("偵測系統已啟動...按 ESC 鍵離開")

while True:
    ret, frame = cap.read()
    if not ret: 
        print("影片播放結束或讀取失敗")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in rects:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow('YuanZe Project', frame)

    if cv.waitKey(30) == 27: # 這裡加了 delay 讓影片播放順暢一點
        break

cap.release()
cv.destroyAllWindows()
