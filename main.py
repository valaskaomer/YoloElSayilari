# Gerekli kütüphaneleri koda aktarmak
from ultralytics import YOLO
import cv2
import time
import torch
import os

# Model seçimi ve cihaz işlemleri
assert os.path.exists("elSayilariYolo11nv2.pt"), "Model dosyası bulunamadı!"
model = YOLO("elSayilariYolo11nv2.pt")
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
print(f"Model is using device: {device}")

# Kamera işlermleri
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

prev_time = time.time()
predict_every_n_frames = 2
frame_count = 0
fps_list = []
last_result = None

# Görüntü yakalanacak olan yer
try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Fps hesaplama
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        fps_list.append(fps)
        if len(fps_list) > 30:
            fps_list.pop(0)
        avg_fps = sum(fps_list) / len(fps_list)

        # Yakalanan görüntü üzerindeki işlemler ve doğruluğun belirlnmesi
        if frame_count % predict_every_n_frames == 0:
            with torch.no_grad():
                results = model.predict(source=frame, imgsz=640, conf=0.5, stream=True)
                last_result = next(results)

        frame_count += 1
        annotated_frame = last_result.plot() if last_result else frame

        # Fps gösterimi ve başlık gösterimi
        cv2.putText(annotated_frame, f"FPS: {int(avg_fps)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("YOLOv11 Ile El Sayilari", annotated_frame)

        # q tuşuna basılana kadar açık kalsın
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Yapılan işlemleri ramden silmek
finally:
    cap.release()
    cv2.destroyAllWindows()
