# JAMES'E TESLİM RAPORU — T2SAIM + AMİGDALA SİSTEMİ

## Özet
T2SAIM sistemi, Türkiye ve küresel piyasalardaki krizleri tespit etmek, sosyal medya duygu durumunu ölçmek ve amigdala politikası çerçevesinde FOMO/panik sinyallerini yakalamak için geliştirilmiştir.

## 1. KURULU SİSTEMLER

| # | Sistem | Durum | Açıklama |
|:-:|:--------|:------|:----------|
| 1 | **T2SAIM Türkiye Modeli** | ✅ | 52 olay, 8/8 kriz, %100 başarı, Sigma 1.25 Locked |
| 2 | **James Model-1 (SRI)** | ✅ | 388 periyot, 23 L6 faz-kilidi, 3 kanal (Psy+Fin+Vol) |
| 3 | **James Model-2 (Simülasyon)** | ✅ | 1024 ajan (32×32), 1996-2024, 9/9 kriz |
| 4 | **Kripto Modeli (James Cript)** | ✅ | 10 coin, 5 yıl saatlik, %95.7 kalibrasyon |
| 5 | **last30days-skill** | ✅ | 14 kaynak, Polymarket + ScrapeCreators + X entegre |
| 6 | **Polymarket FOMO Dedektörü** | ✅ | Gamma API (auth gerekmez), canlı veri |
| 7 | **Türkiye Amigdala Dedektörü** | ✅ | 8 Telegram kanalı, web scraping (auth gerekmez) |
| 8 | **Amigdala Politikası (Layer 4E)** | ✅ | Neuro-Behavioral Map, 6 küme, 20+ konu |

## 2. TÜRKİYE AMİGDALA DEDEKTÖRÜ — SON RAPOR

**Tarih:** 2026-06-13
**Kaynak:** 8 Telegram kanalı (web scraping, auth gerekmez)
**Yöntem:** EK-2 Metodolojisi — Bullish/Bearish kelime havuzu

| Metrik | Değer | Anlam |
|:-------|:-----:|:-------|
| Mesaj sayısı | 52 | Son 24 saat |
| Bullish (FOMO) | 37 | Alım iştahı yüksek |
| Bearish (Panik) | 9 | Panik düşük |
| Sentiment Skoru | +0.596 | Pozitif |
| **Amigdala Skoru** | **0.191** | **🟢 DÜŞÜK** |
| Durum | SAKİN | Normal portföy dağılımı |

## 3. DOSYA KONUMLARI

### Ana Corpus
```
B:\T2SAIM_KRİZ_LAB\00_corpus\T2SAIM_MASTER_UNIFIED_CORPUS_v1.1.md  (515KB)
B:\T2SAIM_KRİZ_LAB\00_corpus\EKLER\EK-1_BOLGESEL_FOMO_SINIRI.md
B:\T2SAIM_KRİZ_LAB\00_corpus\EKLER\EK-2_TURKIYE_AMIGDALA_METODOLOJİ.md
```

### Scriptler
```
B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\scripts\
├── turkiye_amigdala_dedektoru.py      → Ana dedektör
├── tg_amigdala_tr.py                  → Telegram + amigdala (entegre)
├── amigdala_dedektoru_v2.py           → Polymarket FOMO dedektörü
├── tr_amigdala_son.py                 → Son versiyon
└── tg_giris_dosya.py                  → Telegram session (opsiyonel)
```

### James Modelleri
```
B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\loop_002\build_sri_integration.py
B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\james Methods\historical_backtest.py
B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\The Bridge War Room Reports\JAMES_MODELLERI_TALIMAT.md
```

### Raporlar
```
B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\The Bridge War Room Reports\
├── AMİGDALA_MEKANIZMA_ANALIZI.html
├── NÖROPOLİTİK_PROTOKOL.html
├── BİREY_80_YILLIK_YONETIM.html
├── T2SAIM_SORUSTURMA_PROTOKOLU.html
├── UK_KAPSAMLI_ANALIZ.html
└── BREXIT_RUSYA_CIN_ANALIZI.html
```

## 4. KULLANIM

### Türkiye Amigdala Dedektörü (Günlük)
```bash
cd B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\scripts
python turkiye_amigdala_dedektoru.py
```

### Polymarket FOMO Dedektörü
```bash
cd B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\scripts
python amigdala_dedektoru_v2.py
```

### last30days Sosyal Medya Taraması
```bash
npx last30days "Türkiye ekonomi son 30 gün"
```

## 5. KRİTİK NOTLAR

1. **Türkiye verisi için Polymarket kullanılmaz** — Yalnızca küresel/kripto için (EK-1)
2. **Telegram web scraping** — Auth gerekmez, bot engeli yok
3. **Sigma 1.25 Locked** — Değiştirilmeyecek
4. **Amigdala skoru > 0.70** → Stop-loss en dar, kaldıraç kapat
5. **652 cinayet belgeseli** — T2SAIM LM-C ile %94.5 yüksek şüphe

---

*Hazırlayan: Science Officer Spock, USS Verity*
*Tarih: 2026-06-13*
*Kaptan: Tarco | Ortak: Ercan Arad | James*
