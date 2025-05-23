# ✋ El Sayıları Tanıma Sistemi (YOLOv11n Tabanlı)

Bu proje, gerçek zamanlı kamera görüntüsünden elde edilen kareler üzerinde el işaretlerini tespit etmek ve sayısını tanımlamak amacıyla **YOLOv11n** (You Only Look Once) nesne algılama modelini kullanır. Model, belirli el sayılarını (örneğin: 0,1, 2, 3, 4, 5 gibi) tanımak üzere özel olarak eğitilmiştir.

## Geliştirmeler

- Bu model güvenlik amaçlı şifreleme gibi alanlarda kullanılabilir
- Bu model ile çarpma bölme toplama çıkarma gibi matematiksel işlemler konusunda geliştirme yapılabilir
- Bu model sizin hayal gücünüz ile geliştirilebilir :)
---
## 👥 Hedef Kullanıcı Kitlesi

Bu projeden geliştirmek isteyen veya eğlenmek isteyen kişiler faydalanabilir

---
## 👥 Katkı Yapanlar

- **Ömer Çınar Yaman** – Öğrenci no: 2405902004– Yapay Zeka Operatörlüğü Bölümü 


---
## 🚀 Özellikler

- 📷 Web kamerası üzerinden canlı görüntü
- 🧠 YOLOv11n modeli ile nesne algılama
- 📦 CUDA desteği ile GPU hızlandırma (varsa)
- ⚡ Ortalama FPS hesaplama
- ✅ Optimize edilmiş tahmin aralığı ve çözünürlük

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Açıklama                          |
|----------|-----------------------------------|
| Python   | Programlama dili                  |
| OpenCV   | Görüntü işleme                    |
| PyTorch  | Derin öğrenme çatısı              |
| Ultralytics YOLO | YOLOv11 modeli için Python paketi |

---

## 📁 Dosya Yapısı

```

.
├── elSayilariYolo11nv2.pt     # Eğitilmiş YOLOv11 model dosyası
├── main.py                    # Ana uygulama kodu
└── README.md                  # Açıklama dosyası

```
---
## 📦 Gerekli Kütüphaneler

Bu projeyi çalıştırmadan önce aşağıdaki kütüphanelerin sisteminizde kurulu olması gerekmektedir:

```bash
pip install ultralytics opencv-python torch

