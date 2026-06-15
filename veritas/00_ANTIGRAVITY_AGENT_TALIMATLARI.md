# ANTIGRAVITY — Alt Ajan Talimatnamesi (Kör Agent Protokolü)
**Doküman Kodu:** T2SAIM-ANTIGRAVITY-v1.0
**Tarih:** 15 Haziran 2026
**Süpervizör:** SPOCK (LM-C)
**Felsefi Temel:** Veritas Per Se — Sıfır Gelecek Sızıntısı

---

## 1. MİMARİ

```
SPOCK (Süpervizör)
├── Data Agent (Alpha-01) — Veri çekme, temizleme, senkronizasyon
├── Trader Agent (Beta-02) — MFDFA hesaplama, hisse seçimi, işlem yürütme
├── Reporter Agent (Gamma-03) — Raporlama, dashboard güncelleme
└── Audit Agent (Delta-04) — Doğrulama, etik kontrol, zaman mührü
```

## 2. TRAIDER AGENT (Beta-02) — TALİMATLAR

### 2.1 Körleştirme Protokolü

**Bu ajan HİÇBİR ZAMAN gelecekteki fiyatları görmez.** Veri seti her zaman şu şekilde sınırlandırılır:

```
Veri Aralığı: [BAŞLANGIÇ_TARİHİ] → [BUGÜN - 1 GÜN]  
Yani: Bugün 16 Haziran ise, sadece 15 Haziran'a kadar olan veriyi kullan.
```

### 2.2 Girdi Verisi

- **Format:** Günlük OHLCV (Open, High, Low, Close, Volume)
- **Kapsam:** Seçilen bölgedeki tüm likit hisseler (örn. BIST-100 için 95 hisse)
- **Horizon:** Minimum 120 iş günü, maksimum 5 yıl
- **Güncelleme:** Her sabah 07:00'de Data Agent'dan alınır

### 2.3 İşlem Adımları (Her 20 İş Gününde Bir)

```
Adım 1: t anına kadar olan tüm hisse verilerini yükle
Adım 2: Her hisse için DA-MFDFA hesapla (4 durum: UH, UL, DH, DL)
Adım 3: UH (Up-High) durumundaki Hurst üssü h(q=1)'i al
Adım 4: h(q=1) > HURST_THRESHOLD olan hisseleri seç
Adım 5: Seçilen hisselere eşit ağırlık ver
Adım 6: Stop-loss hesapla: stop = min(0.12, max(0.03, 0.03 + 0.10 × width))
Adım 7: Portföyü oluştur, işlem kaydını yaz
Adım 8: 20 gün bekle, Adım 1'e dön
```

### 2.4 Parametreler (Bölge Bazlı)

| Bölge | Hurst Eşiği | Rebalans (gün) | Stop Min | Stop Max | Amnesia λ |
|:---|---:|:---:|:---:|:---:|:---:|
| 🇹🇷 BIST-100 | 0.52 | 20 | 3% | 12% | 0.15 |
| 🇺🇸 S&P 500 | 0.46 | 20 | 5% | 12% | 0.15 |
| 🇬🇧 FTSE 100 | 0.57 | 20 | 3% | 12% | 0.15 |
| 🇪🇺 Euro Stoxx 50 | 0.60 | 20 | 3% | 12% | 0.15 |
| 🇯🇵 Nikkei 225 | 0.55 | 20 | 3% | 12% | 0.15 |
| 🇭🇰 Hang Seng | 0.52 | 20 | 3% | 12% | 0.15 |
| 🪙 Kripto (BTC) | 0.60 | 20 | 5% | 15% | 0.15 |

### 2.5 Amnesia Protokolü (λ=0.15)

Geçmiş verilerin ağırlığı zamanla üssel olarak azalır:
```
W(t) = W₀ × e^(-λ × Δt)
```
λ=0.15 ile ~7 günde eski verinin etkisi yarıya iner. Bu, piyasa rejim değişikliklerine hızlı uyum sağlar.

### 2.6 Stop-Loss Mekanizması

- Dinamik stop: MFDFA DH genişliğine bağlı
- Düşük volatilite → %3 stop
- Yüksek volatilite → %12 stop
- Stop tetiklenince: hisse satılır, o dönem tekrar alınmaz

---

## 3. DATA AGENT (Alpha-01) — TALİMATLAR

### 3.1 Veri Kaynakları
- **Günlük OHLCV:** Yahoo Finance (yfinance kütüphanesi)
- **Güncelleme Saati:** Her sabah 07:00 UTC
- **Gecikme:** D-1 (bir iş günü gecikmeli)

### 3.2 Veri Doğrulama
- Eksik gün kontrolü
- Anormal fiyat hareketi tespiti (>%20 günlük)
- Hacim anomalisi kontrolü
- Bölünme (split) düzeltmesi

---

## 4. ZAMAN MÜHRÜ VE ZİNCİR

Her işlem kaydı SHA-256 ile mühürlenir:
```
İşlem_Kaydı = {
    tarih: ISO_DATE,
    hisse: TICKER,
    işlem: AL/SAT,
    fiyat: FLOAT,
    miktar: FLOAT,
    sebep: REBALANCE/STOP,
    mühür: SHA256(önceki_kayıt + bu_kayıt)
}
```

---

## 5. ETİK GARANTİ

```
🔬 Neden D-1 Gecikmeli?

Amnesia Protokolü (λ=0.15) gereği, hiçbir zaman gelecekteki 
veriyi görmeyiz. İşlem akışı:

📅 Bugün (Pazartesi) → Piyasalar kapanır, veri oluşur
🌅 Yarın sabah 07:00 → Bugünün kapanış verisini çekeriz
⚙️ Yarın 07:15 → Motor çalışır, işlem yaparız

Bu sayede gelecekten geçmişe sızıntı SIFIR.
Bu bir hile değil, bilimsel olarak etik ve doğru yöntemdir.
```

---

**🔒 SHA-256 Mührü:** [BOŞ — İlk koşuda doldurulacak]
**Zaman Kilidi:** 15 Haziran 2026, UTC+3
**Süpervizör:** SPOCK (T2SAIM)
**Derleme:** İstanbul, Türkiye
