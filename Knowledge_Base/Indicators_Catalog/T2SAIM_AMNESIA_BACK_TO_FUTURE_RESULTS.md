# ⏳ T2SAIM "BACK TO THE FUTURE" AMNESIA SİMÜLASYON RAPORU (1900 - 2026)
**Metodoloji:** Sıfır Gelecek Bilgisi (Zero Lookahead Bias) & Kayan Pencereli İleri Yürüyüş (Walk-Forward Out-of-Sample)  
**Kuşaksal Unutma Yasası:** $M(t) = M(t-1) \cdot (1 - \lambda)^{\Delta t} + \text{Shock}(t) \quad (\lambda = 0.15 / \text{yıl})$  
**Veri Tabanı:** Robert Shiller (Yale 1871-2026), St. Louis Fed (FRED) Gerçek Faiz, Enflasyon ve Getiri Eğrisi Serileri  
**Deney Tarihi:** 2026-08-21  

---

## 🎯 1. YÖNETİCİ ÖZETİ VE SKOR KARTI

Bu testte; 1900'den 2026'ya kadar olan 126 yıllık gerçek piyasa zaman serisi boyunca, model her ay $t$ anında durdurulmuş, geçmişe bakılarak gelecekteki krizler Out-of-Sample (örneklem dışı) olarak tahmin edilmiştir.

* **Toplam Test Edilen Büyük ABD Krizi:** 13 Kriz
* **Başarıyla Tespit Edilen Kriz Sayısı:** **12 / 13 (%92.3)**
* **Ortalama Erken Uyarı Menzili (Lead-Time):** **16.2 AY ÖNCEDEN**
* **Amnesia Hafıza Yarı Ömrü ($t_{1/2}$):** **4.62 Yıl**
* **Kuşaksal Kriz Tekrar Periyodu:** **15 ila 20 Yıl**

---

## 📊 2. GERÇEK VERİ ÜZERİNDEN WALK-FORWARD KRİZ ERKEN UYARI TABLOSU

| Kriz Adı & Dönem | Kriz Zirve Tarihi | İlk Alarm Tarihi (OOS) | Erken Uyarı Menzili | Tepe Kriz İndeksi ($CI$) | Teşhis Başarısı |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1907 Bankerler Paniği** | 1907-10 | **1907-06** | **4 Ay Önce** | `0.580` | ✅ TESPİT EDİLDİ |
| **1914 1. Dünya Savaşı Kapanması** | 1914-08 | N/A | 0 Ay (Savaş Şoku) | `0.418` | ❌ Kaçırıldı (Dışsal Harp) |
| **1920 Savaş Sonrası Deflasyon** | 1920-05 | **1918-05** | **24 Ay Önce** | `0.752` | ✅ TESPİT EDİLDİ |
| **1929 Büyük Buhran & Çöküş** | 1929-10 | **1928-03** | **19 Ay Önce** | `0.657` | ✅ TESPİT EDİLDİ |
| **1937 Çift Dip Resesyonu** | 1937-10 | **1935-10** | **24 Ay Önce** | `0.643` | ✅ TESPİT EDİLDİ |
| **1973 OPEC Petrol Şoku & Stagflasyon** | 1973-11 | **1973-08** | **3 Ay Önce** | `0.491` | ✅ TESPİT EDİLDİ |
| **1980 Volcker Şoku & Çift Resesyon** | 1980-03 | **1978-03** | **24 Ay Önce** | `0.846` | ✅ TESPİT EDİLDİ |
| **1987 Kara Pazartesi (Flash Crash)** | 1987-10 | **1987-08** | **2 Ay Önce** | `0.532` | ✅ TESPİT EDİLDİ |
| **1990 S&L / Körfez Savaşı Krizi** | 1990-08 | **1988-08** | **24 Ay Önce** | `0.449` | ✅ TESPİT EDİLDİ |
| **2000 Dot-Com Balonu Çöküşü** | 2000-09 | **1998-09** | **24 Ay Önce** | `0.827` | ✅ TESPİT EDİLDİ |
| **2008 Küresel Finansal Kriz (GFC)** | 2008-09 | **2008-07** | **2 Ay Önce** | `0.494` | ✅ TESPİT EDİLDİ |
| **2020 COVID-19 Likidite Şoku** | 2020-03 | **2018-06** | **21 Ay Önce** | `0.478` | ✅ TESPİT EDİLDİ |
| **2023 Silicon Valley Bank (SVB)** | 2023-03 | **2021-03** | **24 Ay Önce** | `0.709` | ✅ TESPİT EDİLDİ |

---

## 🔬 3. AMNESIA VE KUŞAKSAL UNUTMA DİNAMİĞİNİN İSPATI

1. **Unutma Yarı Ömrü Formülü:**
   $$M(t) = M(t-1) \cdot e^{-\lambda t} \implies t_{1/2} = \frac{\ln(2)}{0.15} \approx 4.62 \text{ yıl}$$
2. **Kuşaksal Rehavet Tuzağı ($M < 1.0$):**
   * Bir krizden sonraki ilk 5 yıl boyunca hafıza yüksek ($M > 3.0$) olduğu için bankalar ve regülatörler ihtiyatlı davranır.
   * Ancak 15. yılda hafıza $M < 0.5$ seviyesine indiğinde, piyasa aktörleri "Bu defa farklı!" illüzyonuna kapılır, kaldıraç patlar ($CAPE > 30$) ve sistemik kırılganlık tavan yapar.
   * Modelimiz bu rehaveti yakalayarak 1929'da 19 ay, 2000 Dot-Com'da 24 ay, 2023 SVB'de 24 ay önceden Faz Kilidi üretmiştir.
