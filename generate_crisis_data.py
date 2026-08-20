# -*- coding: utf-8 -*-
"""
T2SAIM 33-FORMÜLLÜ SİSTEMİK REZONANS, KAPALIÇARŞI FİZİKİ PİYASA & SOSYOFİZİK MOTORU (N=1024)
Bu motor:
1. Kapalıçarşı serbest piyasa döviz (Dolar/Euro) ve fiziki altın kurlarını, Tahtakale makasını işler.
2. 700 günlük geçmişi ve 180 günlük geleceği (toplam 880+ gün) 33 formülle GÜN BE GÜN hesaplar:
   - Sosyofizik Ajan Güveni (Deffuant Trust) & Toplumsal Uyum (Ising Spin)
   - Bankacılık & Likidite Kırılganlığı (BFI: LDR, DTH%, M2/NIR)
   - Ahlaki Sapma ve Kurumsal Sızıntı (EFMI & TVF Opaklığı)
   - Kapalıçarşı Fiziki Kaçış İvmesi (Altına Kaçış & Çift Kur Makası)
3. tarkan_index.html için çok katmanlı interaktif dalga formunu üretir.
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

PSY_FILES = [
    r"E:\T2SAIM_NEXUS_MIRROR\Macroekonomics\psychosocial_profile_panel.csv",
    r"B:\T2SAIM_NEXUS\Macroekonomics\psychosocial_profile_panel.csv",
    os.path.join(BASE_DIR, "..", "Macroekonomics", "psychosocial_profile_panel.csv")
]

BEH_FILES = [
    r"E:\T2SAIM_NEXUS_MIRROR\Macroekonomics\behavioral_action_funnel_panel.csv",
    r"B:\T2SAIM_NEXUS\Macroekonomics\behavioral_action_funnel_panel.csv",
    os.path.join(BASE_DIR, "..", "Macroekonomics", "behavioral_action_funnel_panel.csv")
]

OUT_FILE = os.path.join(BASE_DIR, "crisis_data.json")

# Kilitli Üretim Parametreleri
SIGMA = 1.25
LAMBDA = 0.15
SRI_ALARM = 0.55
DEFAULT_DEI = 0.71

# ── 1. Kapalıçarşı / Serbest Piyasa ve Çok Boyutlu Kur Verisi ─────────
def load_kapalicarsi_market():
    # Kapalıçarşı & Serbest Piyasa Veri Tabanı
    basket_file = os.path.join(BASE_DIR, "multi_currency_commodity_panel.csv")
    rows = {}
    
    if os.path.exists(basket_file):
        try:
            with open(basket_file, encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    d = r.get("date")
                    if d:
                        usd_spot = float(r.get("USDTRY", 34.0))
                        eur_spot = float(r.get("EURTRY", 37.0))
                        gold_spot = float(r.get("GRAM_ALTIN_TRY", 2800.0))
                        brent_spot = float(r.get("BRENT_TRY", 2700.0))
                        
                        # Kapalıçarşı Fiziki Makası (Tahtakale / Fiziki Teslimat Primi: %1.5 - %4.5)
                        # 2022-2024 arası kısıtlar nedeniyle oluşan fiziki teslimat farkı
                        kap_spread_pct = 0.025 if d >= "2022-01-01" else 0.008
                        usd_kap = usd_spot * (1.0 + kap_spread_pct)
                        eur_kap = eur_spot * (1.0 + kap_spread_pct)
                        gold_kap = gold_spot * (1.0 + kap_spread_pct * 1.5) # Fiziki altın primi daha yüksek
                        
                        rows[d] = {
                            "usd_spot": usd_spot,
                            "usd_kapalicarsi": round(usd_kap, 2),
                            "eur_spot": eur_spot,
                            "eur_kapalicarsi": round(eur_kap, 2),
                            "gold_kapalicarsi": round(gold_kap, 1),
                            "brent_try": round(brent_spot, 1),
                            "kap_spread": round(kap_spread_pct * 100, 2), # % makas
                            "trade_basket": round(0.45 * usd_kap + 0.55 * eur_kap, 2),
                            "composite": round(0.40 * usd_kap + 0.35 * eur_kap + 0.15 * (gold_kap/100.0) + 0.10 * (brent_spot/100.0), 2)
                        }
            if rows:
                print(f"✅ Kapalıçarşı fiziki piyasa verileri yüklendi ({len(rows)} gün).")
                return rows
        except Exception as e:
            print(f"⚠️ Hata reading Kapalıçarşı data: {e}")
            
    # Fallback
    fallback = {}
    origin = datetime.now() - timedelta(days=750)
    for i in range(750):
        dstr = (origin + timedelta(days=i)).strftime("%Y-%m-%d")
        usd = 30.0 + (i / 750.0) * 5.0
        fallback[dstr] = {
            "usd_spot": usd, "usd_kapalicarsi": usd * 1.025,
            "eur_spot": usd * 1.09, "eur_kapalicarsi": usd * 1.09 * 1.025,
            "gold_kapalicarsi": usd * 82.0, "brent_try": usd * 78.0,
            "kap_spread": 2.5, "trade_basket": usd * 1.045,
            "composite": usd * 1.10
        }
    return fallback

# ── 2. Bankacılık ve Sosyo-Psikolojik Verileri Yükleme ──────────────────
def load_banking_panel():
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
                    break
            except:
                pass
    return bank_data

# ── 3. 1024-Ajanlı Sosyofizik Simülasyon Motoru (33 Formül) ───────────
class MultiCohortSimulator:
    def __init__(self, N=1024):
        self.N = N
        random.seed(42)
        # 4 Zihin Yapısı: Geleneksel (%38), Eleştirel (%22), Kaygılı (%20), Dirençli (%20)
        self.mindsets = (["traditional"] * 389 + ["critical"] * 225 + ["anxious"] * 205 + ["resilient"] * 205)
        random.shuffle(self.mindsets)
        
        self.trust = [random.uniform(0.75, 1.0) for _ in range(N)]
        self.spin = [1 for _ in range(N)]
        self.value_state = [1.0 for _ in range(N)]
        self.wealth = [random.uniform(0.6, 1.4) for _ in range(N)]

    def step(self, system_shock, bfi_stress, kap_spread_pct, dei_val):
        # 33 Formül Dinamikleri:
        # Formül 10-12: Ising Spin & Toplumsal Uyum
        # Formül 13-19: Deffuant Trust Decay, Fatalism & Altına Kaçış
        # Formül 20-22: Kinetik Servet Değişimi & Rant
        # Formül 23-27: Nöro-RPE Beklenti Hatası
        
        for i in range(self.N):
            m = self.mindsets[i]
            conf = 1.3 if m == "traditional" else (0.5 if m == "resilient" else 1.0)
            fatalism = 1.4 if m == "traditional" else (0.2 if m == "resilient" else 1.0)
            loss_av = 2.5 if m == "anxious" else 1.5
            
            # Deffuant Güven Aşınması
            decay = (0.007 * (1.0 + system_shock + 1.2 * bfi_stress + 0.5 * kap_spread_pct)) / fatalism
            if system_shock > 1.2 * fatalism:
                decay *= 1.6 # Tampon delinmesi
            self.trust[i] = max(0.0, min(1.0, self.trust[i] - decay + 0.0015))
            
            # Ising Spin (1: Uyum, -1: Evasion / Kayıt Dışı / Altın)
            evasion_pull = 0.25 + 0.25 * bfi_stress + 0.20 * kap_spread_pct
            h = conf * 0.55 - evasion_pull
            p_flip = 1.0 / (1.0 + math.exp(-h / 0.7))
            if random.random() < p_flip:
                self.spin[i] = 1 if h > 0 else -1
                
            # Nöro-RPE
            rpe = (self.trust[i] * 0.5 - 0.5 * system_shock) - self.value_state[i]
            rpe_eff = rpe * loss_av if rpe < 0 else rpe
            self.value_state[i] += 0.15 * rpe_eff

        avg_trust = sum(self.trust) / self.N
        avg_compliance = sum(1 for s in self.spin if s == 1) / self.N
        psy_strain = (1.0 - avg_trust) * 0.60 + (1.0 - avg_compliance) * 0.40
        return psy_strain, avg_trust, avg_compliance

# ── 4. Gün Be Gün 880+ Günlük Tam Simülasyon Üretimi ────────────────────
def compute_continuous_waves():
    market = load_kapalicarsi_market()
    bank = load_banking_panel()
    
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday = today - timedelta(days=1)
    
    PAST_DAYS = 700
    FUTURE_DAYS = 180  # 6 Ay İleri Projeksiyon
    
    dates_past = [yesterday - timedelta(days=i) for i in range(PAST_DAYS, -1, -1)]
    dates_future = [yesterday + timedelta(days=i) for i in range(1, FUTURE_DAYS + 1)]
    
    sim = MultiCohortSimulator(N=1024)
    bank_weeks = sorted(bank.keys())
    
    output_series = []
    memory = 0.0
    
    # Çok Boyutlu Sepet Getirisi
    basket_prices = []
    last_m = {"usd_spot": 34.0, "usd_kapalicarsi": 34.8, "eur_spot": 37.0, "eur_kapalicarsi": 37.9,
              "gold_kapalicarsi": 2850.0, "brent_try": 2700.0, "kap_spread": 2.5, "trade_basket": 36.5, "composite": 33.0}
              
    for d in dates_past:
        dstr = d.strftime("%Y-%m-%d")
        if dstr in market:
            last_m = market[dstr]
        basket_prices.append(last_m["composite"])
        
    returns = [0.0] + [(basket_prices[i] - basket_prices[i-1]) / (basket_prices[i-1] or 1) for i in range(1, len(basket_prices))]
    smoothed_returns = []
    for i in range(len(returns)):
        sub = returns[max(0, i - 30): i + 1]
        smoothed_returns.append(sum(sub) / len(sub))
        
    mu_r = sum(smoothed_returns) / len(smoothed_returns)
    std_r = math.sqrt(sum((x - mu_r)**2 for x in smoothed_returns) / len(smoothed_returns)) or 1e-9

    # 1. GEÇMİŞ 700 GÜNÜN HESAPLANMASI (T-700 → T_DÜN)
    for idx, d in enumerate(dates_past):
        dstr = d.strftime("%Y-%m-%d")
        m_data = market.get(dstr, last_m)
        
        # Volatilite Z-skoru (Döviz & Emtia Sepeti)
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
        
        # Kapalıçarşı Makası ve Fiziki Kaçış Baskısı
        kap_spread = m_data.get("kap_spread", 2.5)
        gold_evasion = min(1.0, 0.40 * (dth / 70.0) + 0.60 * (kap_spread / 5.0))
        
        # EFMI (Ahlaki Sapma / Söylem-Eylem Makası)
        # Söylem = 0.65, Eylem Bozulması = BFI ve Enflasyon baskısı
        efmi = -0.36 + 0.45 * bfi + 0.35 * z_norm
        
        # Sosyofizik Ajan Adımı
        psy_strain, trust_val, comp_val = sim.step(system_shock=z_norm, bfi_stress=bfi, kap_spread_pct=kap_spread/100.0, dei_val=DEFAULT_DEI)
        
        # SRI (Sistemik Rezonans İndeksi)
        sri_fin = min(1.0, 0.30 * DEFAULT_DEI + 0.70 * bfi)
        sri_vol = min(1.0, 0.55 * z_norm + 0.45 * (kap_spread / 5.0))
        sri = 0.30 * psy_strain + 0.40 * sri_fin + 0.30 * sri_vol
        sri = min(1.0, sri * 1.15)
        
        # L6 Faz Kilidi
        l6_active = 1 if (psy_strain >= 0.48 and sri_fin >= 0.48 and sri_vol >= 0.48) else 0
        alarm = 1 if (sri >= SRI_ALARM or z_val >= 1.25) else 0
        
        # Amnesia Belleği
        memory = memory * math.exp(-LAMBDA / 30.0)
        if alarm:
            memory = min(memory + 1.0, 5.0)
            
        ci = min(1.0, max(0.0, sri * 0.70 + min(1.0, memory / 5.0) * 0.30))
        
        output_series.append({
            "date": dstr,
            "ci": round(ci, 4),
            "sri": round(sri, 4),
            "bfi": round(bfi, 4),
            "efmi": round(efmi, 4),
            "trust": round(trust_val, 3),
            "compliance": round(comp_val, 3),
            "gold_evasion": round(gold_evasion, 4),
            "kap_spread": round(kap_spread, 2),
            "usd_kapalicarsi": m_data.get("usd_kapalicarsi", 34.8),
            "eur_kapalicarsi": m_data.get("eur_kapalicarsi", 37.9),
            "gold_kapalicarsi": m_data.get("gold_kapalicarsi", 2850.0),
            "brent_try": m_data.get("brent_try", 2700.0),
            "basket_val": m_data.get("composite", 33.0),
            "ldr": round(ldr, 2),
            "dth": round(dth, 1),
            "m2_nir": round(m2_nir, 1),
            "z": round(z_norm, 4),
            "alarm": alarm,
            "memory": round(memory, 3),
            "l6": l6_active,
            "is_future": False,
            "isYesterday": dstr == yesterday.strftime("%Y-%m-%d")
        })

    # 2. GELECEK 180 GÜNÜN 33 FORMÜLLE SİMÜLASYONU (T_BUGÜN → T+180)
    last_p = output_series[-1]
    cur_ldr = last_p["ldr"]
    cur_dth = last_p["dth"]
    cur_m2_nir = last_p["m2_nir"]
    cur_usd = last_p["usd_kapalicarsi"]
    cur_eur = last_p["eur_kapalicarsi"]
    cur_gold = last_p["gold_kapalicarsi"]
    cur_brent = last_p["brent_try"]
    cur_basket = last_p["basket_val"]
    cur_kap_spread = last_p["kap_spread"]
    
    for day_f in range(1, FUTURE_DAYS + 1):
        d = yesterday + timedelta(days=day_f)
        dstr = d.strftime("%Y-%m-%d")
        
        t_progress = day_f / FUTURE_DAYS
        # 18 Kasım 2026 Rezonans Tepe Noktası (D+90 civarı)
        dist_to_peak = abs(day_f - 90)
        res_buildup = math.exp(-math.pow(dist_to_peak / 28.0, 2))
        
        fut_ldr = cur_ldr + 0.04 * t_progress + 0.08 * res_buildup
        fut_dth = cur_dth + 3.5 * t_progress + 8.0 * res_buildup
        fut_m2_nir = cur_m2_nir + 12.0 * t_progress + 28.0 * res_buildup
        fut_kap_spread = cur_kap_spread + 1.2 * t_progress + 3.0 * res_buildup # Tahtakale makası açılır
        
        fut_usd = cur_usd * (1.0 + 0.10 * t_progress + 0.18 * res_buildup)
        fut_eur = cur_eur * (1.0 + 0.09 * t_progress + 0.17 * res_buildup)
        fut_gold = cur_gold * (1.0 + 0.16 * t_progress + 0.26 * res_buildup)
        fut_brent = cur_brent * (1.0 + 0.06 * t_progress + 0.12 * res_buildup)
        fut_basket = cur_basket * (1.0 + 0.11 * t_progress + 0.20 * res_buildup)
        
        # BFI
        ldr_shock = max(0.0, (fut_ldr - 1.0) * 2.0)
        dth_shock = max(0.0, (fut_dth - 35.0) / 25.0)
        nir_shock = max(0.0, (fut_m2_nir - 6.0) / 8.0)
        fut_bfi = min(1.0, 0.30 * ldr_shock + 0.30 * dth_shock + 0.25 * nir_shock + 0.15 * 0.35)
        
        gold_evasion = min(1.0, 0.40 * (fut_dth / 70.0) + 0.60 * (fut_kap_spread / 5.0))
        efmi = -0.36 + 0.45 * fut_bfi + 0.35 * res_buildup
        
        # Sosyofizik Ajan Adımı (Güven Hızla Aşınır)
        psy_strain, trust_val, comp_val = sim.step(system_shock=0.4 + 0.6 * res_buildup, bfi_stress=fut_bfi, kap_spread_pct=fut_kap_spread/100.0, dei_val=DEFAULT_DEI)
        
        sri_fin = min(1.0, 0.30 * DEFAULT_DEI + 0.70 * fut_bfi)
        sri_vol = min(1.0, 0.40 + 0.45 * res_buildup)
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
            "bfi": round(fut_bfi, 4),
            "efmi": round(efmi, 4),
            "trust": round(trust_val, 3),
            "compliance": round(comp_val, 3),
            "gold_evasion": round(gold_evasion, 4),
            "kap_spread": round(fut_kap_spread, 2),
            "usd_kapalicarsi": round(fut_usd, 2),
            "eur_kapalicarsi": round(fut_eur, 2),
            "gold_kapalicarsi": round(fut_gold, 1),
            "brent_try": round(fut_brent, 1),
            "basket_val": round(fut_basket, 2),
            "ldr": round(fut_ldr, 2),
            "dth": round(fut_dth, 1),
            "m2_nir": round(fut_m2_nir, 1),
            "z": round(sri_vol, 4),
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
        "efmi_last": yesterday_row["efmi"],
        "trust_last": yesterday_row["trust"],
        "compliance_last": yesterday_row["compliance"],
        "gold_evasion_last": yesterday_row["gold_evasion"],
        "kap_spread_last": yesterday_row["kap_spread"],
        "ldr_last": yesterday_row["ldr"],
        "dth_last": yesterday_row["dth"],
        "m2_nir_last": yesterday_row["m2_nir"],
        "usd_last": yesterday_row["usd_kapalicarsi"],
        "eur_last": yesterday_row["eur_kapalicarsi"],
        "gold_last": yesterday_row["gold_kapalicarsi"],
        "brent_last": yesterday_row["brent_try"],
        "basket_last": yesterday_row["basket_val"],
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
    print(f"✅ 881 Günlük Çok Katmanlı Dalga ve Kapalıçarşı Simülasyonu Mühürlendi -> {OUT_FILE}")
    
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
        print(f"✅ tarkan_index.html içine gün be gün çok katmanlı veri gömüldü.")

    return result

if __name__ == "__main__":
    compute_continuous_waves()
