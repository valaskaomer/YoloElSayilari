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

c **Ömer Çınar Yaman** – Öğrenci no: 2405902004– Yapay Zeka Operatörlüğü Bölümü 


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

```
## ✔ ÖĞRENCİ KONTROL LİSTESİ (Hazırlık + Teknik)
- 1 Proje konusu belirlendi ve yapay zekâ yöntemine karar verildi. Haar, YOLO, Mediapipe vb. yöntemlerden biri seçildi ve README'de belirtildi. |✔|

- 2 Kodlama aşaması tamamlandı ve sistem nesne/özellik tespiti yapabiliyor. Proje kameradan veya görselden veri alabiliyor; en az bir nesneyi başarıyla tespit ediyor. |✔|

- 3 Kullanılan yöntem kod içerisinde açıkça yorumlandı. Kod içindeki açıklamalar, hangi algoritmanın nerede kullanıldığını anlatıyor. |✔|

- 4 Tespit edilen nesne/özellik ekranda işaretleniyor. (bounding box, etiket, vb.) Algoritma çıktısı görsel olarak anlamlı hale getirildi. |✔|

- 5 Çalışma çıktıları kayıt altına alındı. Ekran görüntüleri (.png, .jpg) ve/veya kısa bir tanıtım videosu hazırlandı. |✔|

- 6 GitHub reposu oluşturuldu. Proje klasörü yapılandırıldı. (kod, README, çıktıdosyaları, poster) |✔|

- 7 README.md dosyası eksiksiz hazırlandı. Proje tanıtımı, kurulum talimatları, örnek çıktı ve katkı bilgileri yer alıyor. |✔|

- 8 QR kod üretildi QR, GitHub deposuna veya çıktı görsellerini içeren demo sayfasına yönlendirilmek üzere oluşturuldu. |✔|

- 9 QR kod poster üzerine eklendi A4 veya A3 boyutundaki posterde, QR kod ve üniversite logosu görünür şekilde yer aldı. |✔|

- 10 PDF proje posteri hazırlandı. Poster, proje özeti, ekran görüntüleri, kullanılan algoritmalar ve öğrenci bilgileriyle tamamlandı. |✔|

- 11 GitHub’a poster ve çıktılar yüklendi poster.pdf ve outputs/ klasörü GitHub reposuna eklendi |✔|

- 12 Grup halinde çalışıldıysa katkılar açıkça belirtildi. Her üyenin adı ve görev paylaşımı README’de yer alıyor; her üye GitHub üzerinden en az bir katkı sağladı. |✔|

---
