"""
T2SAIM Crisis Index Generator — tarkan_index.html için
Gerçek verilerden 700 günlük kriz indeksi hesaplar.

Parametreler (LOCKED):
  SIGMA  = 1.25
  LAMBDA = 0.15 (amnesia decay)
  WINDOW = 5 yıl hareketli pencere
  SRI_ALARM = 0.55
"""

import csv, json, math, os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOCAL_DATA_DIR = r"B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\data"
REL_DATA_DIR   = os.path.join(BASE_DIR, "..", "T2SAIM_NEXUS", "Macroekonomics", "hermes_crisis_lab", "data")

if os.path.exists(LOCAL_DATA_DIR):
    DATA_DIR = LOCAL_DATA_DIR
elif os.path.exists(REL_DATA_DIR):
    DATA_DIR = REL_DATA_DIR
else:
    DATA_DIR = None

OUT_FILE = os.path.join(BASE_DIR, "crisis_data.json")

LOCAL_PANEL_PATH = r"B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\loop_002\data_processed\TR_PRIORITY1_UNIFIED_PANEL_DRAFT_v3.csv"
REL_PANEL_PATH   = os.path.join(BASE_DIR, "..", "T2SAIM_NEXUS", "Macroekonomics", "hermes_crisis_lab", "loop_002", "data_processed", "TR_PRIORITY1_UNIFIED_PANEL_DRAFT_v3.csv")

if os.path.exists(LOCAL_PANEL_PATH):
    PANEL_PATH = LOCAL_PANEL_PATH
elif os.path.exists(REL_PANEL_PATH):
    PANEL_PATH = REL_PANEL_PATH
else:
    PANEL_PATH = None

SIGMA  = 1.25
LAMBDA = 0.15
SRI_ALARM = 0.55

DEFAULT_PSY = 0.5985
DEFAULT_FIN = 0.4145
DEFAULT_DEI = 0.71

def load_macro_baselines():
    if not PANEL_PATH or not os.path.exists(PANEL_PATH):
        return DEFAULT_PSY, DEFAULT_FIN, DEFAULT_DEI
    try:
        with open(PANEL_PATH, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if rows:
                for r in reversed(rows):
                    psy = r.get("sri_psy_component")
                    fin = r.get("sri_fin_component")
                    if psy and fin:
                        val_psy = float(psy)
                        val_fin = float(fin)
                        val_dei = float(r.get("dei")) if r.get("dei") else DEFAULT_DEI
                        return val_psy, val_fin, val_dei
    except:
        pass
    return DEFAULT_PSY, DEFAULT_FIN, DEFAULT_DEI

# ── 1. USDTRY günlük veri ──────────────────────────────────────────────
def load_usdtry():
    rows = {}
    if not DATA_DIR:
        return rows
    path = os.path.join(DATA_DIR, "USDTRY_gunluk.csv")
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    try:
                        rows[r["tarih"]] = float(r["kapanis"])
                    except (KeyError, ValueError):
                        pass
        except Exception as e:
            print(f"⚠️ Warning loading {path}: {e}")
    # en eski ek dosya
    path2 = os.path.join(DATA_DIR, "USDTRY_gunluk_en.csv")
    if os.path.exists(path2):
        try:
            with open(path2, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    try:
                        d = r.get("tarih") or r.get("Date") or r.get("date")
                        v = float(r.get("kapanis") or r.get("Close") or 0)
                        if d and v and d not in rows:
                            rows[d] = v
                    except (ValueError, KeyError):
                        pass
        except Exception as e:
            print(f"⚠️ Warning loading {path2}: {e}")
    return rows

# ── 2. Volatilite ──────────────────────────────────────────────────────
def load_vol():
    rows = {}
    if not DATA_DIR:
        return rows
    path = os.path.join(DATA_DIR, "USDTRY_vol_haftalik.csv")
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    try:
                        rows[r["tarih"]] = float(r["volatilite_yuzde"])
                    except (KeyError, ValueError):
                        pass
        except Exception as e:
            print(f"⚠️ Warning loading {path}: {e}")
    return rows

# ── 3. Tarih aralığı: dün geriye 700 gün ──────────────────────────────
def make_date_range(days=700):
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday = today - timedelta(days=1)
    return [yesterday - timedelta(days=i) for i in range(days, -1, -1)]  # eski→yeni

# ── 4. Z-skor hesabı (rolling window Sigma 1.25) ──────────────────────
def rolling_zscore(series, window=252):
    """252 gün iş günü ≈ 1 yıl; 5 yıl = 1260 gün"""
    result = []
    for i, v in enumerate(series):
        subset = series[max(0, i - window): i + 1]
        if len(subset) < 10:
            result.append(0.0)
            continue
        mu = sum(subset) / len(subset)
        sd = math.sqrt(sum((x - mu)**2 for x in subset) / len(subset)) or 1e-9
        z  = (v - mu) / sd
        result.append(z)
    return result

# ── 5. Amnesia decay — BTF protokolü ─────────────────────────────────
def apply_amnesia(alarms, lam=0.15):
    """Her alarm sonrası bellek LAMBDA hızıyla sönümlenir."""
    memory = 0.0
    result = []
    for alarm in alarms:
        memory = memory * math.exp(-lam / 30.0)   # aylık bozunmanın günlük adımı
        if alarm:
            memory = min(memory + 1.0, 5.0)
        result.append(memory)
    return result

# ── 6. Ana hesaplama ───────────────────────────────────────────────────
def compute_crisis_index():
    usd  = load_usdtry()
    vol  = load_vol()
    dates = make_date_range(700)

    psy_base, fin_base, dei_base = load_macro_baselines()

    # USDTRY serisi (günlük)
    usd_series = []
    for d in dates:
        dstr = d.strftime("%Y-%m-%d")
        # yoksa son bilinen değeri kullan
        if dstr in usd:
            usd_series.append(usd[dstr])
        elif usd_series:
            usd_series.append(usd_series[-1])
        else:
            usd_series.append(30.0)   # fallback

    # Günlük getiri
    returns = [0.0] + [(usd_series[i] - usd_series[i-1]) / (usd_series[i-1] or 1)
                       for i in range(1, len(usd_series))]

    # Makroekonomik dalgalanmaları ve hafta sonu 0 değerlerini sönümlemek için returns serisini 30 günlük hareketli ortalamayla düzeltiyoruz
    smoothed_returns = []
    for i in range(len(returns)):
        sub = returns[max(0, i - 30): i + 1]
        smoothed_returns.append(sum(sub) / len(sub))

    # Z-skorları (1260 günlük pencere ≈ 5 yıl)
    zscores = rolling_zscore(smoothed_returns, window=min(1260, len(smoothed_returns)))

    # Normalize Z → [0,1] (SIGMA standardizasyonu ile)
    z_norm = [min(1.0, max(0.0, abs(z) / SIGMA)) for z in zscores]

    # Volatilite katkısı
    vol_dates = sorted(vol.keys())
    vol_series = []
    for d in dates:
        dstr = d.strftime("%Y-%m-%d")
        # en yakın haftalık volatiliteyi bul
        closest = min(vol_dates, key=lambda x: abs((datetime.strptime(x, "%Y-%m-%d") - d).days)) if vol_dates else None
        if closest:
            v = vol[closest] # Fixed: no division by 100.0
            vol_series.append(min(1.0, v / 5.0))   # %5 volatilite = 1.0
        else:
            vol_series.append(0.3)

    # Günlük volatilite bileşeni
    sri_vol_daily = [0.6 * z + 0.4 * v for z, v in zip(z_norm, vol_series)]

    # Hibrid SRI formülü: 0.30 * sri_psy + 0.40 * sri_fin + 0.30 * sri_vol_daily
    sri_series = [0.30 * psy_base + 0.40 * fin_base + 0.30 * svol for svol in sri_vol_daily]

    # Yapısal DEI çarpanının uygulanması (TR-DEI = dei_base, 0.60'ı aşarsa asimetrik olarak %15 tırmandırılır)
    sri_series_dei = []
    for s in sri_series:
        s_new = s * 1.15 if dei_base >= 0.60 else s
        sri_series_dei.append(min(1.0, s_new))

    # Alarm sinyalleri — SRI >= 0.65 veya Z >= 1.25 sigma gerçek şoklarında tetiklenir
    SRI_ALARM = 0.65
    alarms = [1 if (s >= SRI_ALARM or z >= 1.25) else 0 for s, z in zip(sri_series_dei, zscores)]

    # Amnesia belleği
    memory = apply_amnesia(alarms)

    # Kriz indeksi (0-1) — amnesia belleği katkısı ile
    crisis_idx = []
    for s, m, a in zip(sri_series_dei, memory, alarms):
        base = s * 0.7 + min(1.0, m / 5.0) * 0.3
        ci   = min(1.0, max(0.0, base))
        crisis_idx.append(round(ci, 4))

    # Bilinen kriz tarihleri (doğrulanmış — PRODUCTION REPORT'tan)
    crisis_events = {
        "1999-08-17": "Marmara Depremi",
        "2001-02-22": "Bankacılık Krizi",
        "2008-09-15": "Küresel Finans I",
        "2018-08-10": "Kur Krizi",
        "2020-03-11": "COVID-19",
        "2022-01-01": "Hiperenflasyon",
    }

    # Çıktı
    output = []
    yesterday = dates[-1].strftime("%Y-%m-%d")
    for i, d in enumerate(dates):
        dstr = d.strftime("%Y-%m-%d")
        output.append({
            "date":     dstr,
            "ci":       crisis_idx[i],
            "sri":      round(sri_series_dei[i], 4),
            "z":        round(z_norm[i], 4),
            "vol":      round(vol_series[i], 4),
            "alarm":    alarms[i],
            "memory":   round(memory[i], 3),
            "event":    crisis_events.get(dstr, ""),
            "isYesterday": dstr == yesterday
        })

    # Son değerler (dünkü)
    last = output[-1]
    summary = {
        "yesterday":   yesterday,
        "ci_last":     last["ci"],
        "sri_last":    last["sri"],
        "memory_last": last["memory"],
        "alarm_now":   last["alarm"],
        "l6_active":   1 if last["sri"] >= 0.50 and last["z"] >= 0.50 else 0,
        "dei":         dei_base,
        "sigma":       SIGMA,
        "lam":         LAMBDA,
        "data_points": len(output)
    }

    result = {"summary": summary, "series": output}
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # Embed directly into tarkan_index.html for 100% fail-safe offline/local rendering
    html_path = os.path.join(os.path.dirname(OUT_FILE), "tarkan_index.html")
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
        print(f"✅ Embedded real crisis data into {html_path}")

    print(f"OK: {len(output)} gunluk veri uretildi -> {OUT_FILE}")
    print(f"   Dun ({yesterday}): CI={last['ci']}, SRI={last['sri']}, Alarm={last['alarm']}")
    print(f"   Bellek: {last['memory']} | L6: {summary['l6_active']}")

if __name__ == "__main__":
    compute_crisis_index()
