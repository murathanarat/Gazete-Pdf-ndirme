# 📰 Gazete PDF İndirme (Selenium + Requests)

Bu proje, **İstanbul Üniversitesi -- Gazeteden Tarihe Bakış Projesi**
kapsamında yayınlanan gazete arşivlerini **otomatik olarak PDF
formatında indirmek** için geliştirilmiştir.

🔗 Kaynak Arşiv:\
https://nek.istanbul.edu.tr/ekos/GAZETE

Tek tek PDF indirmek zahmetli olduğu için, bu projede **Selenium** ve
**Requests** kütüphaneleri birlikte kullanılarak süreç tamamen
otomatikleştirilmiştir.

------------------------------------------------------------------------

## 🚀 Özellikler

-   Gazete kategorilerini otomatik algılar
-   Kullanıcının belirlediği **yıl aralığında** indirme yapar
-   Her gazete ve yıl için **ayrı klasör yapısı** oluşturur
-   Daha önce indirilen PDF'leri tekrar indirmez
-   Selenium ile site etkileşimi, Requests ile hızlı PDF indirme

------------------------------------------------------------------------

## 🧠 Kullanılan Teknolojiler

  Teknoloji      Versiyon
  -------------- ----------
  Python         3.8.10
  Pip            25.0.1
  Selenium       4.25.0
  Requests       2.32.3
  ChromeDriver   Güncel

------------------------------------------------------------------------

## 📂 Klasör Yapısı

    📁 PDF
     ├── 📁 Gazete_Adi_1
     │    ├── 📁 1925
     │    │    ├── gazete_1.pdf
     │    │    └── gazete_2.pdf
     │    └── 📁 1926
     ├── 📁 Gazete_Adi_2
     │    └── 📁 1930

------------------------------------------------------------------------

## ⚙️ Kurulum

``` bash
pip install selenium requests
```

Ayrıca: - Chrome tarayıcısı kurulu olmalı - Chrome sürümüne uygun
**ChromeDriver** indirilmelidir

------------------------------------------------------------------------

## 🔧 Ayarlanması Gereken Alanlar

``` python
driver_path = "C:/chromedriver-win64/chromedriver.exe"
download_path = "C:/Users/User/Desktop/PDF"
```

------------------------------------------------------------------------

## ▶️ Kullanım

Program çalıştırıldığında sizden bir yıl aralığı ister:

``` text
hangi yildan indirmeye başlamak istersin : 1925
hangi yila kadar indirmek istersin       : 1930
```

------------------------------------------------------------------------

## 🛡️ Çalışma Mantığı

1.  Ana gazete sayfasına gider\
2.  Tüm gazete kategorilerini listeler\
3.  Yıl aralığını kontrol eder\
4.  PDF bağlantılarını toplar\
5.  Requests ile indirir

------------------------------------------------------------------------

## ⚠️ Notlar

-   Selenium site yapısına bağlıdır
-   HTTPS uyarıları bastırılmıştır (`verify=False`)
-   Büyük arşivlerde işlem süresi uzayabilir

------------------------------------------------------------------------

## 👤 Geliştirici

**Murathan Arat**\
Bilgisayar Mühendisliği Öğrencisi\
Python • Web Automation • Veri Toplama
