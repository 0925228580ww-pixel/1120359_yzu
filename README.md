# 元智大學校園人員即時偵測系統

本專題為元智大學電資學院期末專題，旨在教室場景下實現人員物件即時偵測。本專案透過實地採集 27 組校園影像，並以 XML 格式完成標註，評估傳統 Haar Cascade 模型在複雜室內環境下的偵測表現。

## 專案結構
- `/dataset`: 存放收集之 27 張現場影像及對應之 PASCAL VOC XML 標註檔。
- `/output`: 存放模型測試後之驗證影像 (含偵測結果框)。
- `main.py`: 即時影像偵測程式。
- `test_dataset.py`: 針對資料集進行批次驗證與誤判分析之程式。
- `haarcascade_fullbody.xml`: 專案基礎模型。

## 安裝與執行說明

### 1. 環境需求
請確保已安裝 Python 3.x，並安裝以下 OpenCV 相關套件：
```bash
pip install opencv-python numpy

## 參考資料
內文有測試影片及最後成果
還有資料集
