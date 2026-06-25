import cv2 as cv
import numpy as np
import glob
import os

# 1. 載入模型
# 請確保 haarcascade_fullbody.xml 與此檔案在同一目錄
cascade_path = 'haarcascade_fullbody.xml'
cascade = cv.CascadeClassifier(cascade_path)

if cascade.empty():
    print(f"錯誤：無法載入模型檔案 {cascade_path}，請檢查檔案是否存在。")
    exit()

# 2. 建立輸出資料夾
if not os.path.exists('output'):
    os.makedirs('output')

# 3. 讀取 dataset 資料夾內的所有圖片
# 如果你的圖片是 jpg，請將下方 '*.png' 改為 '*.jpg'
image_files = glob.glob('dataset/*.png') 

if not image_files:
    print("警告：在 dataset 資料夾中找不到圖片，請檢查路徑與副檔名。")
else:
    for img_path in image_files:
        # 使用 imdecode 解決中文檔名讀取失敗的問題
        img = cv.imdecode(np.fromfile(img_path, dtype=np.uint8), cv.IMREAD_COLOR)
        
        if img is None:
            print(f"警告：無法解碼圖片 {img_path}")
            continue
            
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
        # 執行偵測：參數已調整為較敏感的設定
        rects = cascade.detectMultiScale(
            gray, 
            scaleFactor=1.02, 
            minNeighbors=1, 
            minSize=(30, 30)
        )
        
        # 畫框
        for (x, y, w, h) in rects:
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # 儲存結果
        output_path = os.path.join('output', os.path.basename(img_path))
        cv.imwrite(output_path, img)
        print(f"已處理並儲存: {output_path}，共偵測到 {len(rects)} 個物件。")

print("測試完成！請查看 output 資料夾。")
