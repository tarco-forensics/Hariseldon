# -*- coding: utf-8 -*-
"""
T2SAIM 33-FORMÜLLÜ KRİZ & BANKACILIK DİJİTAL İKİZ MOTORU (N=1024 AJAN)
Bu motor:
1. 700 günlük geçmiş veriyi (USDTRY, Volatilite, Haftalık Bankacılık ALM, EFMI, DEI) işler.
2. Gelecek 180 günü (2026 sonuna kadar) 33 matematiksel formülle (Ising, Deffuant, Nöro-RPE, BFI, L6 Faz Kilidi) simüle eder.
3. tarkan_index.html için crisis_data.json üretir ve doğrudan HTML içine gömer.
"""

import csv
import json
import math
import os
import random
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Veri yolları
DATA_DIRS = [
    r"B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\data",
    r"E:\T2SAIM_NEXUS_MIRROR\Macroekonomics\hermes_crisis_lab\data",
    os.path.join(BASE_DIR, "..", "T2SAIM_NEXUS", "Macroekonomics", "hermes_crisis_lab", "data")
]

BANK_FILES = [
    r"E:\T2SAIM_NEXUS_MIRROR\Macroekonomics\weekly_banking_reserve_panel.csv",
    r"B:\T2SAIM_NEXUS\Macroekonomics\weekly_banking_reserve_panel.csv",
    os.path.join(BASE_DIR, "..", "Macroekonomics", "weekly_banking_reserve_panel.csv")
]

OUT_FILE = os.path.join(BASE_DIR, "crisis_data.json")

# Kilitli Üretim Parametreleri
SIGMA = 1.25
LAMBDA = 0.15
SRI_ALARM = 0.55
DEFAULT_PSY = 0.5985
DEFAULT_FIN = 0.4145
DEFAULT_DEI = 0.71

# ── 1. Çok Boyutlu Döviz Sepeti & Emtia (Altın/Petrol) Yükleyici ───────
def load_market_data():
    basket_file = os.path.join(BASE_DIR, "multi_currency_commodity_panel.csv")
    market_rows = {}
    
    if os.path.exists(basket_file):
        try:
            with open(basket_file, encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    d = r.get("date")
                    if d:
                        try:
                            market_rows[d] = {
                                "usd": float(r.get("USDTRY", 34.0)),
                                "eur": float(r.get("EURTRY", 37.0)),
                                "gold_try": float(r.get("GRAM_ALTIN_TRY", 2800.0)),
                                "brent_try": float(r.get("BRENT_TRY", 2700.0)),
                                "eurusd": float(r.get("EURUSD", 1.08)),
                                "tcmb_sepet": float(r.get("TCMB_SEPET_TRY", 35.5)),
                                "trade_basket": float(r.get("TRADE_WEIGHTED_BASKET", 35.7)),
                                "composite": float(r.get("BASKET_COMPOSITE", 33.0))
                            }
                        except (ValueError, KeyError):
                            pass
            if market_rows:
                print(f"✅ Çok boyutlu döviz & emtia sepeti yüklendi ({len(market_rows)} gün): {basket_file}")
                return market_rows
        except Exception as e:
            print(f"⚠️ Hata reading basket panel: {e}")
            
    # Fallback tekil USDTRY dosyaları
    usd_data = {}
    for d in DATA_DIRS:
        if os.path.exists(d):
            p1 = os.path.join(d, "USDTRY_gunluk.csv")
            if os.path.exists(p1) and not usd_data:
                try:
                    with open(p1, encoding="utf-8") as f:
                        for r in csv.DictReader(f):
                            val = float(r["kapanis"])
                            usd_data[r["tarih"]] = {
                                "usd": val, "eur": val * 1.08, "gold_try": val * 75.0,
                                "brent_try": val * 80.0, "eurusd": 1.08, "tcmb_sepet": val * 1.04,
                                "trade_basket": val * 1.044, "composite": val
                            }
                except:
                    pass
    return usd_data

# ── 2. Haftalık Bankacılık Paneli Yükleyici ─────────────────────────────
def load_banking_data():
    bank_data = {}
    for p in BANK_FILES:
        if os.path.exists(p):
            try:
                with open(p, encoding="utf-8") as f:
                    for r in csv.DictReader(f):
                        w = r.get("week")
                        if w:
                            try:
                                bank_data[w] = {
                                    "ldr": float(r.get("loan_to_deposit", 1.15)),
                                    "dth": float(r.get("fx_deposit_share", 48.0)),
                                    "m2_nir": float(r.get("m2_to_nir", 15.0)),
                                    "npl": float(r.get("npl_ratio", 2.5)),
                                    "car": float(r.get("car", 17.0)),
                                    "credit_growth": float(r.get("total_credit_growth", 35.0))
                                }
                            except:
                                pass
                if bank_data:
                    print(f"✅ Bankacılık verisi yüklendi ({len(bank_data)} hafta): {p}")
                    break
            except:
                pass
    return bank_data

# ── 3. 1024-Ajanlı Sosyofizik & Nöro-Ekonomi Simülatörü ────────────────
class AgentCohort:
    def __init__(self, N=1024):
        self.N = N
        random.seed(42)
        # 4 Zihin Yapısı: Geleneksel (%38), Eleştirel (%22), Kaygılı (%20), Dirençli (%20)
        self.mindsets = (["traditional"] * 389 + ["critical"] * 225 + ["anxious"] * 205 + ["resilient"] * 205)
        random.shuffle(self.mindsets)
        
        self.trust = [random.uniform(0.75, 1.0) for _ in range(N)]
        self.spin = [1 for _ in range(N)]  # 1: Uyumlu, -1: Kaçış/Evasion
        self.wanting = [1.0 for _ in range(N)]
        self.liking = [1.0 for _ in range(N)]
        self.value_state = [1.0 for _ in range(N)]

    def step(self, system_shock, bfi_stress, dei):
        # 33 Formül Adımları:
        # Formül 10-12: Ising Spin & Uyum
        # Formül 13-19: Deffuant Trust Decay & Escape
        # Formül 23-27: Nöro-RPE Wanting/Liking
        
        for i in range(self.N):
            m = self.mindsets[i]
            # Uyum katsayıları
            conf_mult = 1.3 if m == "traditional" else (0.5 if m == "resilient" else 1.0)
            fatalism = 1.4 if m == "traditional" else (0.2 if m == "resilient" else 1.0)
            loss_av = 2.5 if m == "anxious" else 1.5
            
            # 1. Güven erimesi (Deffuant)
            decay = 0.008 * (1.0 + system_shock + 1.2 * bfi_stress) / fatalism
            if system_shock > 1.2 * fatalism:
                decay *= 1.6  # Buffer piercing
            self.trust[i] = max(0.0, min(1.0, self.trust[i] - decay + 0.002))
            
            # 2. Spin & Kaçış (Ising Evasion)
            h = conf_mult * 0.5 - (0.25 + 0.20 * bfi_stress)
            prob_flip = 1.0 / (1.0 + math.exp(-h / 0.7))
            if random.random() < prob_flip:
                self.spin[i] = 1 if h > 0 else -1
                
            # 3. Nöro-RPE (TD Öğrenme)
            rpe = (self.trust[i] * 0.5 - 0.5 * system_shock) - self.value_state[i]
            rpe_eff = rpe * loss_av if rpe < 0 else rpe
            self.value_state[i] += 0.15 * rpe_eff
            if rpe < 0:
                self.wanting[i] = max(-2.0, self.wanting[i] + 0.3 * rpe_eff)
                self.liking[i] = min(1.2, self.liking[i] + 0.02)
                
        avg_trust = sum(self.trust) / self.N
        avg_compliance = sum(1 for s in self.spin if s == 1) / self.N
        psy_strain = (1.0 - avg_trust) * 0.60 + (1.0 - avg_compliance) * 0.40
        return psy_strain, avg_trust, avg_compliance

# ── 4. Birleşik 33-Formüllü Geçmiş ve Gelecek Hesaplaması ───────────────
def generate_full_digital_twin():
    market_data = load_market_data()
    bank = load_banking_data()
    
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday = today - timedelta(days=1)
    
    PAST_DAYS = 700
    FUTURE_DAYS = 180  # 2026 sonuna kadar ileri projeksiyon
    
    dates_past = [yesterday - timedelta(days=i) for i in range(PAST_DAYS, -1, -1)]
    dates_future = [yesterday + timedelta(days=i) for i in range(1, FUTURE_DAYS + 1)]
    
    cohort = AgentCohort(N=1024)
    
    # Çok Boyutlu Sepet ve Emtia Serisi
    basket_series = []
    usd_series = []
    eur_series = []
    gold_series = []
    brent_series = []
    
    last_known = {"usd": 34.0, "eur": 37.0, "gold_try": 2800.0, "brent_try": 2700.0, "eurusd": 1.08, "composite": 33.0}
    
    for d in dates_past:
        dstr = d.strftime("%Y-%m-%d")
        if dstr in market_data:
            last_known = market_data[dstr]
        usd_series.append(last_known.get("usd", 34.0))
        eur_series.append(last_known.get("eur", 37.0))
        gold_series.append(last_known.get("gold_try", 2800.0))
        brent_series.append(last_known.get("brent_try", 2700.0))
        basket_series.append(last_known.get("composite", 33.0))

    # Çok Boyutlu Sepet Getirisi ve Volatilitesi
    returns = [0.0] + [(basket_series[i] - basket_series[i-1]) / (basket_series[i-1] or 1) for i in range(1, len(basket_series))]
    smoothed_returns = []
    for i in range(len(returns)):
        sub = returns[max(0, i - 30): i + 1]
        smoothed_returns.append(sum(sub) / len(sub))
        
    mu_r = sum(smoothed_returns) / len(smoothed_returns)
    std_r = math.sqrt(sum((x - mu_r)**2 for x in smoothed_returns) / len(smoothed_returns)) or 1e-9
    
    bank_weeks = sorted(bank.keys())
    output_series = []
    memory = 0.0
    
    # 1. GEÇMİŞ GÜNLERİN HESAPLANMASI (T-700 → T_dün)
    for idx, d in enumerate(dates_past):
        dstr = d.strftime("%Y-%m-%d")
        
        # Çok Boyutlu Sepet Volatilite Z-skoru
        z_val = abs(smoothed_returns[idx] - mu_r) / std_r
        z_norm = min(1.0, max(0.0, z_val / SIGMA))
        
        # Haftalık Bankacılık Rasyoları
        iso_year, iso_week, _ = d.isocalendar()
        target_w = f"{iso_year}-W{iso_week:02d}"
        b_data = bank.get(target_w) or (bank[bank_weeks[-1]] if bank_weeks else {"ldr": 1.15, "dth": 48.0, "m2_nir": 15.0, "npl": 2.5})
        
        ldr = b_data.get("ldr", 1.15)
        dth = b_data.get("dth", 48.0)
        m2_nir = b_data.get("m2_nir", 15.0)
        npl = b_data.get("npl", 2.5)
        
        # Formül 28-31: BFI Bankacılık Kırılganlık İndeksi
        ldr_shock = max(0.0, (ldr - 1.0) * 2.0) if ldr > 1.0 else 0.0
        dth_shock = max(0.0, (dth - 35.0) / 25.0) if dth > 35.0 else 0.0
        nir_shock = max(0.0, (m2_nir - 6.0) / 8.0) if m2_nir > 6.0 else 0.0
        npl_shock = max(0.0, (npl - 3.5) / 3.5) if npl > 3.5 else 0.0
        bfi = min(1.0, 0.30 * ldr_shock + 0.30 * dth_shock + 0.25 * nir_shock + 0.15 * npl_shock)
        
        # Ajan Adımı (Sosyofizik)
        psy_strain, trust_val, comp_val = cohort.step(system_shock=z_norm, bfi_stress=bfi, dei=DEFAULT_DEI)
        
        # Formül 30: SRI Bileşik Stres İndeksi (Döviz Sepeti & Emtia Entegre)
        sri_fin = min(1.0, 0.35 * DEFAULT_FIN + 0.65 * bfi)
        sri_vol = min(1.0, 0.60 * z_norm + 0.40 * 0.35)
        sri = 0.30 * psy_strain + 0.40 * sri_fin + 0.30 * sri_vol
        if DEFAULT_DEI >= 0.60:
            sri = min(1.0, sri * 1.15)
            
        # Formül 32: L6 Faz Kilidi & Alarm
        l6_active = 1 if (psy_strain >= 0.45 and sri_fin >= 0.45 and sri_vol >= 0.45) else 0
        alarm = 1 if (sri >= SRI_ALARM or z_val >= 1.25) else 0
        
        # Formül 4: Amnesia Bellek Bozunumu
        memory = memory * math.exp(-LAMBDA / 30.0)
        if alarm:
            memory = min(memory + 1.0, 5.0)
            
        ci = min(1.0, max(0.0, sri * 0.70 + min(1.0, memory / 5.0) * 0.30))
        
        output_series.append({
            "date": dstr,
            "ci": round(ci, 4),
            "sri": round(sri, 4),
            "z": round(z_norm, 4),
            "vol": 0.35,
            "bfi": round(bfi, 4),
            "ldr": round(ldr, 2),
            "dth": round(dth, 1),
            "m2_nir": round(m2_nir, 1),
            "usd": round(usd_series[idx], 2),
            "eur": round(eur_series[idx], 2),
            "gold_try": round(gold_series[idx], 1),
            "brent_try": round(brent_series[idx], 1),
            "basket_val": round(basket_series[idx], 2),
            "trust": round(trust_val, 3),
            "compliance": round(comp_val, 3),
            "alarm": alarm,
            "memory": round(memory, 3),
            "l6": l6_active,
            "is_future": False,
            "isYesterday": dstr == yesterday.strftime("%Y-%m-%d")
        })
        
    # 2. GELECEK GÜNLERİN HESAPLANMASI (T_bugün → T+180 - 18 Kasım 2026 Rezonansı)
    last_past = output_series[-1]
    cur_ldr = last_past["ldr"]
    cur_dth = last_past["dth"]
    cur_m2_nir = last_past["m2_nir"]
    cur_usd = last_past["usd"]
    cur_eur = last_past["eur"]
    cur_gold = last_past["gold_try"]
    cur_brent = last_past["brent_try"]
    cur_basket = last_past["basket_val"]
    
    for day_f in range(1, FUTURE_DAYS + 1):
        d = yesterday + timedelta(days=day_f)
        dstr = d.strftime("%Y-%m-%d")
        
        t_progress = day_f / FUTURE_DAYS
        dist_to_peak = abs(day_f - 90)
        resonance_buildup = math.exp(-math.pow(dist_to_peak / 28.0, 2))
        
        fut_ldr = cur_ldr + 0.05 * t_progress + 0.08 * resonance_buildup
        fut_dth = cur_dth + 4.0 * t_progress + 8.0 * resonance_buildup
        fut_m2_nir = cur_m2_nir + 15.0 * t_progress + 30.0 * resonance_buildup
        
        fut_usd = cur_usd * (1.0 + 0.12 * t_progress + 0.18 * resonance_buildup)
        fut_eur = cur_eur * (1.0 + 0.11 * t_progress + 0.17 * resonance_buildup)
        fut_gold = cur_gold * (1.0 + 0.18 * t_progress + 0.25 * resonance_buildup)
        fut_brent = cur_brent * (1.0 + 0.08 * t_progress + 0.12 * resonance_buildup)
        fut_basket = cur_basket * (1.0 + 0.13 * t_progress + 0.19 * resonance_buildup)
        
        # BFI
        ldr_shock = max(0.0, (fut_ldr - 1.0) * 2.0)
        dth_shock = max(0.0, (fut_dth - 35.0) / 25.0)
        nir_shock = max(0.0, (fut_m2_nir - 6.0) / 8.0)
        fut_bfi = min(1.0, 0.30 * ldr_shock + 0.30 * dth_shock + 0.25 * nir_shock + 0.15 * 0.3)
        
        # Ajan Adımı (Güven Aşınması Hızlanır)
        psy_strain, trust_val, comp_val = cohort.step(system_shock=0.5 + 0.5 * resonance_buildup, bfi_stress=fut_bfi, dei=DEFAULT_DEI)
        
        sri_fin = min(1.0, 0.35 * DEFAULT_FIN + 0.65 * fut_bfi)
        sri_vol = min(1.0, 0.40 + 0.45 * resonance_buildup)
        sri = 0.30 * psy_strain + 0.40 * sri_fin + 0.30 * sri_vol
        sri = min(1.0, sri * 1.15)
        
        l6_active = 1 if (psy_strain >= 0.50 and sri_fin >= 0.50 and sri_vol >= 0.50) else 0
        alarm = 1 if sri >= SRI_ALARM else 0
        
        memory = memory * math.exp(-LAMBDA / 30.0)
        if alarm:
            memory = min(memory + 1.0, 5.0)
            
        ci = min(1.0, max(0.0, sri * 0.70 + min(1.0, memory / 5.0) * 0.30))
        
        output_series.append({
            "date": dstr,
            "ci": round(ci, 4),
            "sri": round(sri, 4),
            "z": round(sri_vol, 4),
            "vol": round(sri_vol, 4),
            "bfi": round(fut_bfi, 4),
            "ldr": round(fut_ldr, 2),
            "dth": round(fut_dth, 1),
            "m2_nir": round(fut_m2_nir, 1),
            "usd": round(fut_usd, 2),
            "eur": round(fut_eur, 2),
            "gold_try": round(fut_gold, 1),
            "brent_try": round(fut_brent, 1),
            "basket_val": round(fut_basket, 2),
            "trust": round(trust_val, 3),
            "compliance": round(comp_val, 3),
            "alarm": alarm,
            "memory": round(memory, 3),
            "l6": l6_active,
            "is_future": True,
            "isYesterday": False
        })

    # Summary
    yesterday_row = output_series[PAST_DAYS]
    summary = {
        "yesterday": yesterday.strftime("%Y-%m-%d"),
        "ci_last": yesterday_row["ci"],
        "sri_last": yesterday_row["sri"],
        "bfi_last": yesterday_row["bfi"],
        "ldr_last": yesterday_row["ldr"],
        "dth_last": yesterday_row["dth"],
        "m2_nir_last": yesterday_row["m2_nir"],
        "usd_last": yesterday_row["usd"],
        "eur_last": yesterday_row["eur"],
        "gold_last": yesterday_row["gold_try"],
        "brent_last": yesterday_row["brent_try"],
        "basket_last": yesterday_row["basket_val"],
        "trust_last": yesterday_row["trust"],
        "compliance_last": yesterday_row["compliance"],
        "memory_last": yesterday_row["memory"],
        "alarm_now": yesterday_row["alarm"],
        "l6_active": yesterday_row["l6"],
        "dei": DEFAULT_DEI,
        "sigma": SIGMA,
        "lam": LAMBDA,
        "data_points": len(output_series)
    }
    
    result = {"summary": summary, "series": output_series}
    
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"✅ {len(output_series)} günlük simülasyon tamamlandı ({PAST_DAYS} geçmiş + {FUTURE_DAYS} gelecek) -> {OUT_FILE}")
    
    # tarkan_index.html içine göm
    html_path = os.path.join(BASE_DIR, "tarkan_index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        json_str = json.dumps(result, ensure_ascii=False)
        embedded_stmt = f"window.EMBEDDED_CRISIS_DATA = {json_str};"
        if "window.EMBEDDED_CRISIS_DATA =" in html_content:
            import re
            html_content = re.sub(r"window\.EMBEDDED_CRISIS_DATA\s*=\s*\{.*?\};", embedded_stmt, html_content)
        else:
            html_content = html_content.replace("<script>", "<script>\n" + embedded_stmt, 1)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ tarkan_index.html içine 33-formüllü veri gömüldü.")

    return result

if __name__ == "__main__":
    generate_full_digital_twin()
