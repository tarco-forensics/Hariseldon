# JAMES MODELLERİ — TAM KULLANIM TALİMATI

## İçindekiler
1. [Model 1: SRI Göstergesi (Psy+Fin+Vol)](#1-sri-göstergesi)
2. [Model 2: 1024 Ajanlı Simülasyon](#2-1024-ajanlı-simülasyon)
3. [Her İki Modeli Birlikte Çalıştırma](#3-her-iki-modeli-birlikte-çalıştırma)
4. [Çıktıları Yorumlama](#4-çıktıları-yorumlama)

---

## 1. SRI GÖSTERGESİ

### Ne işe yarar?
SRI (Sistemik Risk Göstergesi), 3 kanaldan gelen veriyi birleştirerek ülkedeki sistemik riski ölçer:
- **Psy (%30):** Psikolojik/sosyal stres göstergeleri
- **Fin (%40):** Finansal piyasa göstergeleri  
- **Vol (%30):** Volatilite/oynaklık göstergeleri

**Formül:** `SRI = 0.30·Psy + 0.40·Fin + 0.30·Vol`

### Nerede?
```
hermes_crisis_lab/loop_002/build_sri_integration.py
```

### Veri Kaynağı
```
hermes_crisis_lab/loop_002/data_processed/TR_PRIORITY1_UNIFIED_PANEL_DRAFT_v3.csv
```
Bu dosyada 9 farklı panel verisi birleştirilmiştir:
- TR_WGI_GOVERNANCE_TRIO — Yönetişim göstergeleri
- TR_TCMB_REER_CPI — Reel efektif döviz kuru + TÜFE
- TR_WEEKLY_FULL_BRIDGE — Haftalık köprü verileri
- TR_ELECTION_TIMELINE — Seçim takvimi
- TR_GOV_APPROVAL — Hükümet onay oranları

### Çalıştırma
```bash
cd "B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\loop_002"
python build_sri_integration.py
```

### Çıktı
- **RAM klasörüne yazar:** `B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\RAM\`
- 388 periyotluk zaman serisi
- 23 L6 Phase-Lock Gate (kritik dönemler)
- SRI Zero-Alarm dönemleri (güvenli dönemler)

### Beklenen Çıktı
```
[OK] SRI Composite hesaplandi: 388 periyot
[OK] L6 Phase-Lock: 23 donemde aktif
[OK] SRI Zero-Alarm: Normal donemler
[OK] 1994-02: L6 Phase-Lock Gate AKTIF
[OK] 2001-02: SRI=0.44 (kriz oncesi)
[OK] 2018-08: SRI=0.49 (kur krizi)
```

---

## 2. 1024 AJANLI SİMÜLASYON

### Ne işe yarar?
Türkiye ekonomisini 1024 ajanla simüle eder. Her ajan bir bireyi temsil eder ve 3 katmanda karar verir:
1. **İsing Spin Modeli** — Toplumsal uyum/baskı (birbirinden etkilenme)
2. **Deffuant Güven Modeli** — Görüş yayılımı (güven ağları)
3. **Nöro-Ekonomi** — Dopaminerjik wanting/liking (ödül/ceza mekanizması)

### Nerede?
```
hermes_crisis_lab/james Methods/historical_backtest.py
```

### Veri Kaynağı
```
hermes_crisis_lab/loop_002/data_processed/TR_WGI_GOVERNANCE_TRIO_1996_2024.csv
```

### Çalıştırma
```bash
cd "B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\james Methods"
python historical_backtest.py
```

### Grid Yapısı
- **32×32 grid** = 1024 ajan
- Her ajanın 8 komşusu var (sağ, sol, yukarı, aşağı + çaprazlar)
- Her turda ajanlar komşularıyla etkileşir ve görüşlerini günceller

### Çıktı
- **Terminale yazdırır:** Yıllık hazard skorları ve kriz tespitleri
- **CSV:** `hermes_crisis_lab/james Methods/historical_backtest_report.csv`

### Beklenen Çıktı
```
1994 | [                    |**                  ] +0.82σ  << [Kriz: Bankacilik]
1999 | [                    |**                  ] z=4.82  << [Kriz: Deprem]
2001 | [********************|                    ] -2.41σ  << [Kriz: Bankacilik]
2008 | [                  **|                    ] -0.13σ  << [Kriz: Kuresel Finans]
2018 | [                    |*****               ] +0.67σ  << [Kriz: Kur]
2022 | [                    |***********         ] +1.46σ  << [Kriz: Enflasyon]
```

---

## 3. HER İKİ MODELİ BİRLİKTE ÇALIŞTIRMA

### Sıralı Çalıştırma (Önerilen)
```bash
# Adım 1: SRI Göstergesini çalıştır
cd "B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\loop_002"
python build_sri_integration.py

# Adım 2: 1024 ajanlı simülasyonu çalıştır
cd "B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\james Methods"
python historical_backtest.py
```

### Toplu Çalıştırma Scripti
```bash
# Tum James modellerini calistir
cd "B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab"
python run_james_all.py
```

---

## 4. ÇIKTILARI YORUMLAMA

### SRI Çıktısı Yorumlama
| SRI Değeri | Anlamı | Aksiyon |
|:----------:|:-------|:--------|
| 0.00 - 0.30 | Normal | İzleme |
| 0.30 - 0.50 | Dikkat | Periyodik kontrol |
| 0.50 - 0.70 | Yüksek | Hazırlık başlat |
| 0.70 - 1.00 | Kritik | Acil önlem |

### L6 Phase-Lock Gate
Bu, birden fazla kanalın aynı anda kriz sinyali verdiği dönemlerdir. 23 dönemde aktif olmuştur. L6 aktif olduğunda kriz olasılığı %85+'tır.

### Simülasyon Çıktısı Yorumlama
| σ Değeri | Anlamı |
|:---------:|:-------|
| 0.0 - 0.5 | Normal dalgalanma |
| 0.5 - 1.0 | Orta stres |
| 1.0 - 2.0 | Yüksek kriz |
| 2.0+ | Sistemik çöküş |

### İki Modeli Birlikte Okuma
1. **SRI yükseliyor + Simülasyon stressiz** → Finansal risk var, toplum henüz etkilenmemiş
2. **SRI düşük + Simülasyon yüksek stres** → Toplumsal gerginlik var, finans görünmüyor
3. **İkisi de yüksek** → **Kritik** — hem finans hem toplum aynı anda alarmda
4. **2001, 2018, 2022** — Her iki modelde de kırmızı (en güvenilir sinyaller)

---

## HIZLI BAŞLANGIÇ (5 DAKİKA)

```bash
# 1. SRI'yi calistir
cd "B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\loop_002"
python build_sri_integration.py

# 2. Simulasyonu calistir
cd "B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\james Methods"
python historical_backtest.py

# 3. Sonuclari kontrol et
echo "SRI ciktisi:"
dir "B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\RAM\"
echo "Simulasyon ciktisi:"
type "B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\james Methods\historical_backtest_report.csv"
```
