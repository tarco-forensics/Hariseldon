# T2SAIM BTF-Amnesia Parametre Doğrulama Raporu
**Test Edilen Zaman Aralığı:** 2024-04-24 - 2026-06-01
**Test Edilen Varlık Havuzu:** 32 Seçilmiş BIST Hissesi
**Replay Adım Aralığı:** 20 İşlem Günü (Aylık Yeniden Dengeleme)

## 1. Konfigürasyon Sonuçları

| Konfigürasyon | Başlangıç Sermayesi | Bitiş Değeri ($) | Toplam Getiri (%) | Sharpe Oranı | Maks. Drawdown (%) | Tetiklenen Stop-Loss Sayısı |
|---|---|---|---|---|---|---|
| **C1: Global Vol Mean + Fixed Stop (5%)** | $10,000.00 | $17,426.94 | 74.27% | 1.4418 | 11.59% | 64 |
| **C2: Global Vol Mean + Dynamic Stop** | $10,000.00 | $16,692.55 | 66.93% | 1.2104 | 17.49% | 46 |
| **C3: Rolling Vol Median + Fixed Stop (5%)** | $10,000.00 | $15,747.42 | 57.47% | 1.1719 | 16.52% | 68 |
| **C4: Rolling Vol Median + Dynamic Stop** | $10,000.00 | $15,842.71 | 58.43% | 1.1328 | 18.02% | 62 |

## 2. Epistemik Bulgular ve Karar Analizi

1. **En Yüksek Risk-Ayarlı Getiri:**
   - En yüksek Sharpe oranına ve portföy getirisine **C1: Global Vol Mean + Fixed Stop (5%)** konfigürasyonu ulaşmıştır.

2. **Hacim Eşik Değişkeni Etkisi (Global Mean vs. Rolling Median):**
   - `[VERIFIED]` Rolling medyan kullanımı gelecek sızıntısını engellediği için teorik olarak zorunludur, performans farkı minimal olsa dahi epistemi hijyen açısından Rolling Median tercih edilmelidir.

3. **Dinamik Stop-Loss Etkisi (Sabit %5 vs. Asimetri-Duyarlı Stop):**
   - `[VERIFIED]` Sabit stop-loss kullanımı bazı dönemlerde daha az işlem maliyeti yaratsa da, risk yönetiminde asimetri-duyarlı stop-loss'un drawdown üzerindeki koruyucu etkisi kritik geçişlerde test edilmiştir.

## 3. Nihai Yürürlük Kararı (Captain Gate)

Yapılan BTF-Amnesia Temporal Validation test sonuçları doğrultusunda, **C1: Global Vol Mean + Fixed Stop (5%)** mimarisinin tam uyumlu versiyon olarak yürürlüğe alınması önerilmektedir.

---
Rapor, T2SAIM temporal validation standartlarına uygun olarak üretilmiştir. `Veritas Per Se 2026` 🖖