# S-Player | Gelişmiş Müzik Çalar

Bu proje, Ostim Teknik Üniversitesi için geliştirilmiş, modüler ve Nesne Yönelimli (OOP) mimariye sahip bir müzik çalar uygulamasıdır.

## 🛠 Teknik Özellikler
- **Modüler Mimari:** Uygulama mantığı (`modules/`) ve arayüz (`main.py`) birbirinden ayrılarak kodun sürdürülebilirliği sağlanmıştır.
- **Hata Yönetimi:** `try-except` blokları kullanılarak dosya okuma ve ses işleme süreçlerinde oluşabilecek çökmeler engellenmiştir.
- **OOP Yapısı:** `MusicPlayer` sınıfı ile müzik işleme süreçleri merkezi bir sınıfa taşınmıştır.
- **Geri Bildirim:** Şarkı süresi, anlık ilerleme ve parça bilgisi arayüz üzerinden gerçek zamanlı izlenebilir.

## 🚀 Kurulum ve Çalıştırma

### 1. Gereksinimler
- Python 3.x yüklü olmalıdır.
- İnternet bağlantınızın olması (Flet kütüphanesini indirmek için) önerilir.

### 2. Gerekli Kütüphaneler
Terminali (CMD/PowerShell) proje klasöründe açın ve şu komutu çalıştırın:
```bash
pip install flet mutagen