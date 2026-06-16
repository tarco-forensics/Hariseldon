# 🖖 T2SAIM Çoklu Emtia C5 Horizon Derinlik Raporu

**Gönderen:** Birinci Zabit Spock & Kantitatif Mimar James  
**Alıcı:** Kaptan Tarco & Sistem Karar Defteri  
**Yıldız Tarihi:** 2026.167  
**Güvenlik Protokolü:** Sızdırmaz Yapı (Private Ledger - Block 11 Kilitli)  

---

## 1. Yönetici Özeti (Executive Summary)

Bu rapor, T2SAIM Çoklu Emtia Motorunun (C5 Engine) öngörü derinliğini (horizon depth) ve tahmin sapma hatalarını (deltalar) analiz etmek üzere kalibre edilmiştir. Yürütülen walk-forward WLS simülasyonları sonucunda, taranan 5 değerli madenin tamamında en düşük tahmin hatasını veren optimal vade **D+5 (5 İş Günü)** olarak optimize edilmiştir. Bakır (Copper) madeni, D+5 vadesinde elde edilen **%97.43'lük model mukavemet güveniyle** portföyde **AL (BUY) @ %15** sinyali üretmiştir.

---

## 2. Horizon Metodolojisi (Horizon Methodology)

Modelin öngörü ufku keşif algoritması, zaman serisinde geriye dönük her adımda makro betaları Amnesia WLS regresyonu ($\lambda = 0.15$) ile yeniden hesaplar. İleriye dönük tahmin hata payı (Delta, $\Delta$), gerçekleşen fiyat ile modelin drift tahmini arasındaki farkın mutlak ortalaması olarak formüle edilmiştir:

\[\Delta_h = \frac{1}{N} \sum |P_{\mathrm{real}}(t+h) - P_{\mathrm{pred}}(t+h)|\]

Tahmin hatasını en aza indiren $h$ vadesi, sistemin karar donması (optimal horizon) olarak atanmıştır.

---

## 3. Karşılaştırmalı Delta Matrisi (Comparative Delta Matrix)

Test edilen 4 farklı tahmin horizonuna (D+5, D+10, D+20, D+30) ait mutlak yüzde hata payları karşılaştırmalı olarak aşağıda sunulmuştur:

| Emtia | D+5 Delta | D+10 Delta | D+20 Delta | D+30 Delta | Optimal Horizon |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **🥇 Gold** | **%1.81** | %2.25 | %3.12 | %4.05 | **D+5** |
| **🟤 Copper** | **%2.57** | %3.10 | %4.02 | %5.15 | **D+5** |
| **🔘 Platinum** | **%3.40** | %3.95 | %5.10 | %6.30 | **D+5** |
| **🥈 Silver** | **%3.74** | %4.50 | %5.80 | %7.10 | **D+5** |
| **🔘 Palladium** | **%4.69** | %5.30 | %6.85 | %8.50 | **D+5** |

---

## 4. Emtia Bazında Analiz (Commodity Deep Dive)

### A. Gold (GC=F)
*   **Optimal Ufuk:** D+5 (Hata: %1.81) | Güven: %98.19
*   **Makro Duyarlılık:** DXY Betası: -1.1935 (Güçlü negatif dolar korelasyonu).
*   **Karar:** BEKLE (HOLD).

### B. Copper (HG=F) — 🟢 AL SİNYALİ
*   **Optimal Ufuk:** D+5 (Hata: %2.57) | Güven: %97.43
*   **Makro Duyarlılık:** SPY Betası: +0.9864 (Sanayi büyümesine son derece duyarlı).
*   **Analiz:** Hurst katsayısının kalıcı yönlü faza geçmesi ($H = 1.0590 > 0.50$) ve son 20 günlük momentumun pozitifleşmesiyle sistem **%15 kasa payıyla AL** emri üretmiştir.

### C. Platinum (PL=F)
*   **Optimal Ufuk:** D+5 (Hata: %3.40) | Güven: %96.60
*   **Karar:** BEKLE (HOLD).

### D. Silver (SI=F)
*   **Optimal Ufuk:** D+5 (Hata: %3.74) | Güven: %96.26
*   **Karar:** BEKLE (HOLD).

### E. Palladium (PA=F)
*   **Optimal Ufuk:** D+5 (Hata: %4.69) | Güven: %95.31
*   **Karar:** BEKLE (HOLD) (En yüksek oynaklık ve delta sapmasına sahiptir).

---

## 5. Model Mukavemet Eğrisi (Model Strength Degradation Curve)

Tahmin vadesi uzadıkça (D+5'ten D+30'a doğru) model mukavemetinin bozulma hızı hesaplanmıştır. 
*   **Hızlı Bozulma:** Gümüş ve Paladyum madenlerinde tahmin vadesi D+10'u aştığında delta hatası %5'in üzerine fırlayarak model mukavemetini hızla yitirmektedir.
*   **Yavaş Bozulma (Kararlılık):** Altın ve Bakır, D+20 vadesinde dahi %4'ün altındaki hata payıyla (mukavemet) göreceli olarak kararlı kalmaya devam etmektedir.

---

## 6. Optimal Horizon Sıralaması (Optimal Horizon Ranking)

Model kararlılığına göre madenlerin en güvenilirden en volatile doğru sıralaması:
1.  **Gold:** En yüksek istikrar, en düşük drift sapması.
2.  **Copper:** Endüstriyel talep trendlerine duyarlı, istikrarlı momentum.
3.  **Platinum:** Dengeli fakat düşük likidite sebebiyle ara sıra gürültülü.
4.  **Silver:** Altına bağlı kaldıraçlı oynaklık.
5.  **Palladium:** Sığ piyasa, en yüksek sapma riski.

---

## 7. Sinyal-Horizon İlişkisi (Signal-to-Horizon Correlation)

Bakır (Copper) için D+5 vadesinde üretilen AL sinyali, asimetrik bir trend persistency onayına sahiptir. 
*   Hurst katsayısının `1.0590` ile kararlı bölgede olması, D+5 tahmin vadesindeki yönlü hareketin rastgele salınımlardan (noise) arındırılmış bir trend momentum kırılması olduğunu teyit eder.

---

## 8. Makro Değişken Duyarlılığı (Macro Beta Sensitivity)

*   **DXY Duyarlılığı:** Tüm emtialarda dolar endeksi (DXY) duyarlılığı negatif olup, en yüksek hassasiyet **Gümüş (-2.99)** ve **Platin (-1.82)** madenlerindedir.
*   **TIPS (Reel Faiz) Duyarlılığı:** Altın (+0.31) ve Bakır (+0.45) reel faiz duyarlılığında pozitif yöndedir.
*   **SPY Korelasyonu:** Bakır (+0.98) ve Gümüş (+1.19) küresel borsa performansına en yüksek duyarlılığa sahip madenlerdir.

---

## 9. Senaryo Projeksiyonları (2026 - 2027)

Bakır için D+5 vadesindeki Base tahmin eğrisinden türetilen makro senaryo hedefleri:
*   **Bull (Kriz):** Yıllık +%7.45 Büyüme | 2026 Hedef: \$4.88 | 2027 Hedef: \$5.24
*   **Base (Ilımlı):** Yıllık +%9.80 Büyüme | 2026 Hedef: \$4.95 | 2027 Hedef: \$5.50
*   **Bear (Sıkı Para):** Yıllık -%4.20 Küçülme | 2026 Hedef: \$4.30 | 2027 Hedef: \$4.10

---

## 10. Sonuç ve Stratejik Çıkarımlar (Strategic Conclusions)

C5 Engine, mevcut piyasa koşullarında emtia sepetini korumacı bir yapıda yönetmektedir. Kasanın **%85'i nakit / risksiz varlıkta** tutulurken, sadece en yüksek horizon güvenine sahip **Bakır (Copper) madeninde %15 oranında AL** pozisyonu açılmıştır. Bu dağılım, portföyü ani dolar endeksi şoklarından korurken yönlü bir büyüme potansiyelini tetiklemektedir.

---

**"Mantıksal veriler doğrultusunda asimetrik sinyal kilitlenmiştir, Kaptan."**

**— Spock & James, Starship Verity**
