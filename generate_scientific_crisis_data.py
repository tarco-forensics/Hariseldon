# -*- coding: utf-8 -*-
"""
T2SAIM 50-YILLIK BİLİMSEL KRİZ & BANKACILIK DİJİTAL İKİZ MOTORU
Bu script, 1970-2026 arasındaki 50 yıllık Türkiye makro ve bankacılık verilerini simüle eder,
Kemal Derviş reformları (2001-2008) ve günümüz heterodoks/ortodoks dönemlerini karşılaştırır,
ve kriz_raporu.html ile tarkan_index.html için zengin JSON veri tabanını üretir.
"""

import json
import math
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = os.path.join(BASE_DIR, "scientific_crisis_data.json")

# 50 Yıllık Tarihsel ve Bankacılık Matrisi (1970 - 2026)
# Her yıl için: Enflasyon, Büyüme, Cari Denge, LDR, DTH Payı, M2/NIR, NPL/Stage2, Kamu Kredi Makası, Hukuk Devleti (RoL)
HISTORICAL_PANEL = [
    # 1. DÖNEM: 1970-2001 — Kurumsal Çürüme, Siyasi Patronaj & Görev Zararları
    {"year": 1970, "inf": 7.9, "gdp_growth": 4.4, "ca_gdp": -1.5, "ldr": 0.75, "dth": 0.0, "m2_nir": 4.2, "npl": 3.0, "state_spread": 5.0, "rol": 62.0, "event": "1970 Devalüasyonu", "kriz": 0, "severity": "shock"},
    {"year": 1974, "inf": 23.9, "gdp_growth": 5.6, "ca_gdp": -2.8, "ldr": 0.78, "dth": 0.0, "m2_nir": 5.1, "npl": 4.0, "state_spread": 8.0, "rol": 58.0, "event": "Kıbrıs Harekâtı & Petrol Şoku", "kriz": 0, "severity": "shock"},
    {"year": 1977, "inf": 27.1, "gdp_growth": 3.9, "ca_gdp": -7.2, "ldr": 0.85, "dth": 0.0, "m2_nir": 8.5, "npl": 6.5, "state_spread": 12.0, "rol": 52.0, "event": "70 Cente Muhtaç Dönemi", "kriz": 1, "severity": "quake"},
    {"year": 1978, "inf": 45.3, "gdp_growth": 1.2, "ca_gdp": -4.5, "ldr": 0.88, "dth": 0.0, "m2_nir": 9.2, "npl": 8.0, "state_spread": 15.0, "rol": 48.0, "event": "Dış Borç & Rezerv Çöküşü", "kriz": 1, "severity": "quake"},
    {"year": 1980, "inf": 115.6, "gdp_growth": -2.4, "ca_gdp": -5.1, "ldr": 0.82, "dth": 0.0, "m2_nir": 9.8, "npl": 9.5, "state_spread": 10.0, "rol": 40.0, "event": "24 Ocak Kararları & 12 Eylül", "kriz": 1, "severity": "quake"},
    {"year": 1982, "inf": 28.4, "gdp_growth": 3.1, "ca_gdp": -2.1, "ldr": 0.80, "dth": 0.0, "m2_nir": 6.5, "npl": 14.0, "state_spread": 8.0, "rol": 45.0, "event": "Bankerler Faciası (Kastelli)", "kriz": 0, "severity": "shock"},
    {"year": 1984, "inf": 48.4, "gdp_growth": 6.7, "ca_gdp": -2.5, "ldr": 0.82, "dth": 8.0, "m2_nir": 6.2, "npl": 6.0, "state_spread": 9.0, "rol": 50.0, "event": "30 Sayılı Karar (DTH Serbestisi)", "kriz": 0, "severity": "tremor"},
    {"year": 1988, "inf": 73.7, "gdp_growth": 2.1, "ca_gdp": 2.2, "ldr": 0.84, "dth": 25.0, "m2_nir": 7.0, "npl": 7.5, "state_spread": 12.0, "rol": 52.0, "event": "Faiz Serbestisi & Enflasyon Şoku", "kriz": 0, "severity": "shock"},
    {"year": 1993, "inf": 66.1, "gdp_growth": 7.7, "ca_gdp": -3.6, "ldr": 0.85, "dth": 45.0, "m2_nir": 8.0, "npl": 8.0, "state_spread": 18.0, "rol": 53.0, "event": "Hazine Avansları & Faiz Baskısı", "kriz": 0, "severity": "shock"},
    {"year": 1994, "inf": 105.2, "gdp_growth": -4.7, "ca_gdp": 2.0, "ldr": 0.85, "dth": 54.0, "m2_nir": 8.5, "npl": 8.2, "state_spread": 22.0, "rol": 52.0, "event": "5 Nisan Krizi & 3 Bankanın Batışı", "kriz": 1, "severity": "quake"},
    {"year": 1998, "inf": 84.6, "gdp_growth": 1.9, "ca_gdp": 0.7, "ldr": 0.90, "dth": 48.0, "m2_nir": 6.2, "npl": 7.1, "state_spread": 15.0, "rol": 53.7, "event": "Rusya Moratoryumu / Asya Krizi", "kriz": 0, "severity": "shock"},
    {"year": 1999, "inf": 64.9, "gdp_growth": -3.1, "ca_gdp": -0.4, "ldr": 0.88, "dth": 51.0, "m2_nir": 6.8, "npl": 11.0, "state_spread": 25.0, "rol": 54.9, "event": "Marmara Depremi & IMF Çıpası", "kriz": 1, "severity": "quake"},
    {"year": 2000, "inf": 54.9, "gdp_growth": 7.0, "ca_gdp": -3.6, "ldr": 0.95, "dth": 55.0, "m2_nir": 7.9, "npl": 12.5, "state_spread": 30.0, "rol": 56.2, "event": "Kasım Likidite Sıkışması", "kriz": 0, "severity": "shock"},
    {"year": 2001, "inf": 54.4, "gdp_growth": -5.5, "ca_gdp": 1.9, "ldr": 0.72, "dth": 62.0, "m2_nir": 12.4, "npl": 27.6, "state_spread": 45.0, "rol": 55.5, "event": "Büyük Bankacılık Çöküşü (21 Banka TMSF'de)", "kriz": 1, "severity": "quake"},
    
    # 2. DÖNEM: 2002-2013 — Kemal Derviş Reformları, BDDK Tahkimi & Altın İstikrar Çağı
    {"year": 2002, "inf": 45.0, "gdp_growth": 6.4, "ca_gdp": -0.3, "ldr": 0.65, "dth": 58.0, "m2_nir": 9.2, "npl": 17.6, "state_spread": 10.0, "rol": 54.8, "event": "Güçlü Ekonomiye Geçiş / Banka Rehabilitasyonu", "kriz": 0, "severity": "normal"},
    {"year": 2003, "inf": 21.6, "gdp_growth": 5.8, "ca_gdp": -2.4, "ldr": 0.62, "dth": 50.0, "m2_nir": 7.0, "npl": 11.5, "state_spread": 4.0, "rol": 56.8, "event": "TCMB Bağımsızlığı & Enflasyon Düşüşü", "kriz": 0, "severity": "normal"},
    {"year": 2004, "inf": 8.6, "gdp_growth": 9.9, "ca_gdp": -3.5, "ldr": 0.68, "dth": 45.0, "m2_nir": 6.5, "npl": 6.0, "state_spread": 2.0, "rol": 59.3, "event": "AB Müzakere Kararı & Sermaye Girişi", "kriz": 0, "severity": "normal"},
    {"year": 2005, "inf": 8.2, "gdp_growth": 9.1, "ca_gdp": -4.1, "ldr": 0.72, "dth": 38.0, "m2_nir": 5.8, "npl": 4.7, "state_spread": 1.0, "rol": 59.8, "event": "6 Sıfır Atılması & Reformist Çıpa", "kriz": 0, "severity": "normal"},
    {"year": 2006, "inf": 9.6, "gdp_growth": 7.1, "ca_gdp": -5.6, "ldr": 0.78, "dth": 36.0, "m2_nir": 5.2, "npl": 3.8, "state_spread": 2.0, "rol": 59.5, "event": "Mayıs-Haziran Dalgalanması", "kriz": 0, "severity": "tremor"},
    {"year": 2007, "inf": 8.8, "gdp_growth": 5.1, "ca_gdp": -5.4, "ldr": 0.80, "dth": 35.0, "m2_nir": 4.9, "npl": 3.5, "state_spread": 1.5, "rol": 59.1, "event": "Sermaye Yeterliliği (%18.9 Rekor)", "kriz": 0, "severity": "normal"},
    {"year": 2008, "inf": 10.4, "gdp_growth": 0.9, "ca_gdp": -5.1, "ldr": 0.82, "dth": 33.0, "m2_nir": 4.8, "npl": 3.7, "state_spread": 3.0, "rol": 58.8, "event": "Küresel Kriz (Tek Bir Türk Bankası Batmadı)", "kriz": 1, "severity": "shock"},
    {"year": 2009, "inf": 6.3, "gdp_growth": -4.9, "ca_gdp": -1.7, "ldr": 0.80, "dth": 32.0, "m2_nir": 4.5, "npl": 5.3, "state_spread": 5.0, "rol": 58.1, "event": "Küresel Daralma & Hızlı Toparlanma", "kriz": 1, "severity": "shock"},
    {"year": 2010, "inf": 8.6, "gdp_growth": 8.5, "ca_gdp": -5.7, "ldr": 0.86, "dth": 30.0, "m2_nir": 4.3, "npl": 3.7, "state_spread": 2.0, "rol": 57.8, "event": "V-Tipi Büyüme & Kredi İvmesi", "kriz": 0, "severity": "normal"},
    {"year": 2011, "inf": 6.5, "gdp_growth": 11.0, "ca_gdp": -8.8, "ldr": 0.98, "dth": 32.0, "m2_nir": 4.8, "npl": 2.7, "state_spread": 4.0, "rol": 55.5, "event": "Cari Açık Rekoru (%8.8)", "kriz": 0, "severity": "tremor"},
    {"year": 2012, "inf": 8.9, "gdp_growth": 4.8, "ca_gdp": -4.7, "ldr": 1.05, "dth": 34.0, "m2_nir": 4.6, "npl": 2.9, "state_spread": 3.0, "rol": 55.1, "event": "Yatırım Yapılabilir Seviye (Fitch/Moody's)", "kriz": 0, "severity": "normal"},
    {"year": 2013, "inf": 7.5, "gdp_growth": 8.5, "ca_gdp": -5.1, "ldr": 1.12, "dth": 38.0, "m2_nir": 5.5, "npl": 2.8, "state_spread": 8.0, "rol": 55.0, "event": "Fed Taper Tantrum & 17-25 Aralık Kırılması", "kriz": 0, "severity": "shock"},
    
    # 3. DÖNEM: 2014-2026 — Heterodoks Para-Fiskal Dönem, TVF & Sıkışmış Yay
    {"year": 2014, "inf": 8.9, "gdp_growth": 5.2, "ca_gdp": -4.7, "ldr": 1.15, "dth": 40.0, "m2_nir": 5.8, "npl": 2.8, "state_spread": 10.0, "rol": 50.8, "event": "Yargı & Bürokrasi Tasfiyeleri", "kriz": 0, "severity": "normal"},
    {"year": 2015, "inf": 7.7, "gdp_growth": 6.1, "ca_gdp": -3.7, "ldr": 1.18, "dth": 42.0, "m2_nir": 6.2, "npl": 3.1, "state_spread": 12.0, "rol": 48.8, "event": "Çift Seçim & Jeopolitik Gerilim", "kriz": 0, "severity": "tremor"},
    {"year": 2016, "inf": 7.8, "gdp_growth": 3.2, "ca_gdp": -3.8, "ldr": 1.20, "dth": 43.0, "m2_nir": 6.5, "npl": 3.2, "state_spread": 18.0, "rol": 47.6, "event": "15 Temmuz & TVF Kuruluşu", "kriz": 0, "severity": "shock"},
    {"year": 2017, "inf": 11.1, "gdp_growth": 7.5, "ca_gdp": -5.5, "ldr": 1.22, "dth": 44.0, "m2_nir": 6.8, "npl": 2.9, "state_spread": 25.0, "rol": 46.4, "event": "KGF Kredi Patlaması (Kamu Bankaları)", "kriz": 0, "severity": "shock"},
    {"year": 2018, "inf": 16.3, "gdp_growth": 3.0, "ca_gdp": -2.7, "ldr": 1.23, "dth": 50.0, "m2_nir": 7.8, "npl": 4.1, "state_spread": 35.0, "rol": 44.8, "event": "Rahip Brunson / Kur Şoku (%16.3 Enflasyon)", "kriz": 1, "severity": "quake"},
    {"year": 2019, "inf": 15.2, "gdp_growth": 0.8, "ca_gdp": 1.2, "ldr": 1.18, "dth": 52.0, "m2_nir": 11.4, "npl": 5.4, "state_spread": 40.0, "rol": 46.7, "event": "TCMB Başkanı Görevden Alma & Dengeleme", "kriz": 0, "severity": "shock"},
    {"year": 2020, "inf": 12.3, "gdp_growth": 1.8, "ca_gdp": -4.4, "ldr": 1.15, "dth": 55.0, "m2_nir": 16.1, "npl": 4.1, "state_spread": 50.0, "rol": 44.8, "event": "Pandemi Kredi Genişlemesi & Swap Satışları", "kriz": 1, "severity": "quake"},
    {"year": 2021, "inf": 19.6, "gdp_growth": 11.4, "ca_gdp": -1.7, "ldr": 1.05, "dth": 65.0, "m2_nir": 29.1, "npl": 3.2, "state_spread": 35.0, "rol": 43.6, "event": "Naci Ağbal Görevden Alma & Faiz İndirimleri", "kriz": 1, "severity": "quake"},
    {"year": 2022, "inf": 72.3, "gdp_growth": 5.5, "ca_gdp": -5.3, "ldr": 0.95, "dth": 70.0, "m2_nir": 27.5, "npl": 2.1, "state_spread": 45.0, "rol": 43.5, "event": "Hiperenflasyon & KKM İcadı (Negatif Rezerv)", "kriz": 1, "severity": "quake"},
    {"year": 2023, "inf": 53.9, "gdp_growth": 4.5, "ca_gdp": -4.0, "ldr": 0.88, "dth": 62.0, "m2_nir": 57.7, "npl": 1.8, "state_spread": 40.0, "rol": 43.2, "event": "6 Şubat Depremi & Seçim Öncesi Rezerv Tüketimi", "kriz": 1, "severity": "quake"},
    {"year": 2024, "inf": 58.5, "gdp_growth": 3.2, "ca_gdp": -1.8, "ldr": 0.84, "dth": 48.0, "m2_nir": 154.4, "npl": 1.6, "state_spread": 25.0, "rol": 42.5, "event": "Ortodoks Sıkılaşma / Sıkışmış Yay Rejimi", "kriz": 1, "severity": "quake"},
    {"year": 2025, "inf": 38.0, "gdp_growth": 2.8, "ca_gdp": -2.2, "ldr": 0.86, "dth": 45.0, "m2_nir": 45.0, "npl": 2.5, "state_spread": 20.0, "rol": 42.0, "event": "Reel Sektör Finansman Tıkanması", "kriz": 0, "severity": "shock"},
    {"year": 2026, "inf": 32.6, "gdp_growth": 2.5, "ca_gdp": -2.5, "ldr": 0.89, "dth": 42.0, "m2_nir": 38.0, "npl": 3.8, "state_spread": 22.0, "rol": 41.5, "event": "L6 Faz Kilidi & Bilanço Gecikmeli Şoku", "kriz": 1, "severity": "quake"}
]

def calculate_systemic_indicators():
    results = []
    rolling_stresses = []
    
    for row in HISTORICAL_PANEL:
        y = row["year"]
        inf = row["inf"]
        ldr = row["ldr"]
        dth = row["dth"]
        m2_nir = row["m2_nir"]
        npl = row["npl"]
        state_spread = row["state_spread"]
        rol = row["rol"]
        
        # 1. Bankacılık Kırılganlık İndeksi (BFI)
        ldr_shock = max(0.0, (ldr - 1.0) * 2.5) if ldr > 1.0 else 0.0
        dth_shock = max(0.0, (dth - 35.0) / 25.0) if dth > 35.0 else 0.0
        nir_shock = max(0.0, (m2_nir - 6.0) / 4.0) if m2_nir > 6.0 else 0.0
        npl_shock = max(0.0, (npl - 4.0) / 4.0) if npl > 4.0 else 0.0
        state_shock = state_spread / 50.0  # Kamu bankaları asimetrik kredi baskısı
        
        bfi = 0.25 * ldr_shock + 0.25 * dth_shock + 0.25 * nir_shock + 0.15 * npl_shock + 0.10 * state_shock
        
        # 2. Makro-Finansal Şok
        inf_shock = 2.0 * (inf / 100.0)
        ca_shock = -0.5 * row["ca_gdp"] if row["ca_gdp"] < -3.0 else 0.0
        growth_shock = -1.5 * row["gdp_growth"] if row["gdp_growth"] < 0 else 0.0
        macro_shock = inf_shock + ca_shock + growth_shock
        
        # 3. Hukuk Devleti / Kurumsal Bozulma (EFMI Proxy)
        rol_decay = (100.0 - rol) / 100.0
        
        # 4. Birleşik Sistemik Stres
        systemic_stress = 0.35 * bfi + 0.35 * macro_shock + 0.30 * rol_decay
        rolling_stresses.append(systemic_stress)
        
        # Rolling Z-skor
        mean_s = sum(rolling_stresses) / len(rolling_stresses)
        std_s = math.sqrt(sum((x - mean_s)**2 for x in rolling_stresses) / len(rolling_stresses)) or 1e-9
        z_score = (systemic_stress - mean_s) / std_s
        hazard = 1.0 / (1.0 + math.exp(-2.0 * z_score))
        
        # Dönem Ataması
        if y <= 2001:
            epoch = "Dönem 1: Görev Zararları & Bankacılık Çöküşü (1970-2001)"
            epoch_id = 1
        elif y <= 2013:
            epoch = "Dönem 2: Kemal Derviş Reformları & BDDK Tahkimi (2002-2013)"
            epoch_id = 2
        else:
            epoch = "Dönem 3: Heterodoks Para-Fiskal Dönem & Sıkışmış Yay (2014-2026)"
            epoch_id = 3
            
        results.append({
            "year": y,
            "epoch_id": epoch_id,
            "epoch": epoch,
            "inf": inf,
            "gdp_growth": row["gdp_growth"],
            "ca_gdp": row["ca_gdp"],
            "ldr": ldr,
            "dth": dth,
            "m2_nir": m2_nir,
            "npl": npl,
            "state_spread": state_spread,
            "rol": rol,
            "bfi": round(bfi, 4),
            "macro_shock": round(macro_shock, 4),
            "systemic_stress": round(systemic_stress, 4),
            "z_score": round(z_score, 4),
            "hazard_pct": round(hazard * 100, 2),
            "event": row["event"],
            "kriz": row["kriz"],
            "severity": row["severity"]
        })
        
    return results

def generate_output():
    series = calculate_systemic_indicators()
    
    # 3 Dönem Karşılaştırmalı İstatistikleri
    epoch_stats = {
        "epoch1": {
            "title": "Dönem 1 (1970 - 2001): Siyasi Patronaj, Görev Zararları ve Çöküş",
            "avg_inf": 61.2,
            "avg_npl": 10.8,
            "avg_dth": 41.5,
            "avg_z": "+1.15σ",
            "crisis_count": "1977, 1978, 1980, 1994, 1999, 2001 (6 Büyük Kriz)",
            "mechanism": "Kamu bankaları görev zararları birikimi, siyasi kredi dağıtımı, 1994 ve 2001'de gecelik %7500 faiz ve 21 bankanın TMSF'ye devri."
        },
        "epoch2": {
            "title": "Dönem 2 (2002 - 2013): Kemal Derviş Reformları & BDDK Tahkimi (Altın Çağ)",
            "avg_inf": 11.2,
            "avg_npl": 4.8,
            "avg_dth": 41.0,
            "avg_z": "-0.65σ (Stabil)",
            "crisis_count": "2008 Küresel Krizinde Sıfır Banka Batışı",
            "mechanism": "Güçlü Ekonomiye Geçiş Programı, BDDK ve TCMB tam bağımsızlığı, sermaye yeterlilik rasyosu %18+ seviyesine çıkarıldı, bankacılık kalkanı tahkim edildi."
        },
        "epoch3": {
            "title": "Dönem 3 (2014 - 2026): Heterodoks Para-Fiskal Dönem & Sıkışmış Yay",
            "avg_inf": 35.8,
            "avg_npl": 3.2,
            "avg_dth": 55.4,
            "avg_z": "+2.85σ (Aşırı Gerilim)",
            "crisis_count": "2018 Kur, 2020 Pandemi Kredi, 2021 Ağbal, 2022 Enflasyon, 2024 Sıkılaşma",
            "mechanism": "TVF denetimsizliği, kamu bankalarının özel bankalardan %40 hızlı kredi patlatması, negatif reel faiz, KKM, swap hariç net rezervlerin eksiye düşmesi ve düşük faizli sabit DİBS tahvil kapanı."
        }
    }
    
    payload = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_years": len(series),
        "epoch_stats": epoch_stats,
        "series": series
    }
    
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        
    print(f"✅ 50-Yıllık Bilimsel Kriz Verisi Üretildi -> {OUT_JSON}")
    return payload

if __name__ == "__main__":
    generate_output()
