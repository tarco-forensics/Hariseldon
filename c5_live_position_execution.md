# 🚀 T2SAIM Canlı Pozisyon İşletim Kaydı (C5-001)

**Pozisyon ID:** C5-001  
**Maden / Emtia:** Bakır (Copper - `HG=F`)  
**İşlem Yönü:** AL (LONG)  
**Yıldız Tarihi:** 2026.167 (16 Haziran 2026)  
**Güvenlik Protokolü:** Sızdırmaz Yapı (Block 13 Kilitli)  

---

## 1. İşlem Parametreleri ve Pozisyon Detayı

Aşağıdaki parametreler, C5 Engine tarafından en son AutoResearch kalibrasyon döngüsünde (`hurst_th = 0.60`) üretilen sinyaller uyarınca kilitlenmiştir:

```
╔═══════════════════════════════════════════════════════════╗
║  POZİSYON #C5-001 DETAYLARI                               ║
╠═══════════════════════════════════════════════════════════╣
║  Varlık / Ticker  : Bakır (Copper) / HG=F                 ║
║  Giriş Fiyatı     : $6.48                                 ║
║  Pozisyon Tutarı  : $1,500 USD                            ║
║  Kullanılan Stake : %15.00 (1/4 Kelly Limitli)            ║
║  Dinamik Stop-Loss: $6.12 (Girişten -%5.55)               ║
║  Optimal Ufuk     : D+5 (5 İş Günü)                       ║
║  Güven Derecesi   : %97.43 (Delta Hata: %2.57)            ║
║  Kasa Durumu      : $8,500 Nakit (%85)                     ║
║  Mühür Kodu       : Block 13 — 989fbb5f9a59...            ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 2. Kantitatif Gerekçeler ve Filtre Durumu

Pozisyonun açılmasında etkili olan T2SAIM filtre çıktıları:
1.  **Hurst persistence ($H_{copper}$):** `1.0797` (Eşik `0.60` değerinin oldukça üzerinde olup, yönlü trend kalıcılığını doğrular).
2.  **Kısa Vadeli Getiri Filtresi:** Son 20 günlük log-getiri ortalaması pozitif faza geçmiş ve trendin yukarı yönlü momentumu onaylanmıştır.
3.  **Makro Betalar:** DXY (-0.75), TIPS (+0.55), SPY (+0.96). Bakır, sanayi büyümesine (SPY) duyarlılığı ve faiz artış korumasıyla (TIPS) asimetrik getiri sunmaktadır.

---

## 3. Risk ve İzleme Yönergeleri

*   **Günlük Kapanış Takibi:** Bakır günlük bar kapanışı **\$6.12** veya daha altına indiği takdirde, rebalans günü beklenmeksizin pozisyon **STOP-LOSS** olarak anında kapatılacaktır.
*   **Rebalans Tarihi:** T+20 iş günü sonunda (14 Temmuz 2026 civarı) pozisyonun kâr/zarar durumu kapatılarak nakde çekilecek ve C5 Engine yeni sinyal matrisine göre re-organize edilecektir.

---

**"İşlem kilitlendi, mühürlendi ve takibe alındı."**

**— DATA & Spock, Starship Verity**
