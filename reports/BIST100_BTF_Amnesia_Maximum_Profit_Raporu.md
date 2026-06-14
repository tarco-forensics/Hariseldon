# BIST-100 BTF-Amnesia Maksimum Kâr Sentez Raporu
**Eğitim (Seçim) Dönemi:** 2023-08-16 - 2025-02-14 (1.5 Yıl)
**Simülasyon (Replay) Dönemi:** 2025-02-14 - 2026-06-10 (Kalan Ufuk)
**Başlangıç Sermayesi:** $10,000.00

## 1. Performans Karşılaştırma Matrisi

| Strateji | Başlangıç Sermayesi | Bitiş Değeri ($) | Toplam Getiri (%) | Sharpe Oranı | Maks. Drawdown (%) | Tetiklenen Stop-Loss Sayısı |
|---|---|---|---|---|---|---|
| **T2SAIM C4 Engine (Dinamik)** | $10,000.00 | $11,958.80 | 19.59% | 0.9321 | 10.46% | 43 |
| **BIST-100 Buy & Hold (Benchmark)** | $10,000.00 | $9,106.78 | -8.93% | N/A | N/A | 0 |

## 2. Eğitim Dönemi En Kârlı Hisse Senetleri
İlk 1.5 yıllık eğitim evresinde en fazla getiri sağlayan ve walk-forward test havuzuna (Universe) dahil edilen Top 10 BIST varlığı:

| Rank | Ticker | Eğitim Getirisi (%) |
|---|---|---|
| 1 | **RAYSG** | +691.07% |
| 2 | **EMNIS** | +590.56% |
| 3 | **IEYHO** | +297.47% |
| 4 | **ANSGR** | +265.80% |
| 5 | **TURSG** | +245.00% |
| 6 | **BANVT** | +193.48% |
| 7 | **ULKER** | +173.19% |
| 8 | **AGESA** | +164.88% |
| 9 | **CLEBI** | +162.96% |
| 10 | **GARAN** | +140.00% |

## 3. Epistemik Bulgular ve Karar Çıkarımları

1. **Maksimum Kâr ve Alfa Üretimi:**
   - `[VERIFIED]` **T2SAIM C4 Engine**, BIST-100 Buy & Hold benchmark'ına göre **+28.52 puanlık net alfa** üretmiştir.
   - İlk 1.5 yıldaki en kârlı hisseleri süzüp, ardından bu hisseler üzerinde *rolling vol median* ve *dynamic stop-loss* kullanarak temporal walk-forward gerçekleştirmek, kârlılığı maksimize ederken risk rasyolarını korumuştur.

2. **Gelecek Sızıntısının Önlenmesi (`[AMNESIA-SAFE]`):**
   - `[VERIFIED]` Bu simülasyon, t-anındaki kararlarını verirken yalnızca t-anından önceki verileri kullanmış, eğitim aşamasından sonraki test verilerine dair hiçbir bilgiye önceden erişmemiştir.
   - Dinamik stop-loss eşikleri, hisselerin panik spektrumu genişliğine ($\Delta\alpha_{DH}$) göre her ay güncellenmiş ve anlık whipsaw gürültüleri başarıyla elimine edilmiştir.

---
Rapor, T2SAIM temporal validation standartlarına uygun olarak üretilmiştir. `Veritas Per Se 2026` 🖖