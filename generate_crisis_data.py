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

DATA_DIR = r"B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\data"
OUT_FILE = r"B:\Hariseldon\crisis_data.json"

SIGMA  = 1.25
LAMBDA = 0.15
SRI_ALARM = 0.55

# ── 1. USDTRY günlük veri ──────────────────────────────────────────────
def load_usdtry():
    rows = {}
    path = os.path.join(DATA_DIR, "USDTRY_gunluk.csv")
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                rows[r["tarih"]] = float(r["kapanis"])
            except (KeyError, ValueError):
                pass
    # en eski ek dosya
    path2 = os.path.join(DATA_DIR, "USDTRY_gunluk_en.csv")
    if os.path.exists(path2):
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
    return rows

# ── 2. Volatilite ──────────────────────────────────────────────────────
def load_vol():
    rows = {}
    path = os.path.join(DATA_DIR, "USDTRY_vol_haftalik.csv")
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                rows[r["tarih"]] = float(r["volatilite_yuzde"])
            except (KeyError, ValueError):
                pass
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
        memory = memory * math.exp(-lam / 12)   # aylık bozunma → günlük yaklaşım
        if alarm:
            memory = min(memory + 1.0, 5.0)
        result.append(memory)
    return result

# ── 6. Ana hesaplama ───────────────────────────────────────────────────
def compute_crisis_index():
    usd  = load_usdtry()
    vol  = load_vol()
    dates = make_date_range(700)

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

    # Z-skorları (1260 günlük pencere ≈ 5 yıl)
    zscores = rolling_zscore(returns, window=min(1260, len(returns)))

    # Normalize Z → [0,1]
    z_norm = [min(1.0, max(0.0, abs(z) / (SIGMA * 2))) for z in zscores]

    # Volatilite katkısı
    vol_dates = sorted(vol.keys())
    vol_series = []
    for d in dates:
        dstr = d.strftime("%Y-%m-%d")
        # en yakın haftalık volatiliteyi bul
        closest = min(vol_dates, key=lambda x: abs((datetime.strptime(x, "%Y-%m-%d") - d).days)) if vol_dates else None
        if closest:
            v = vol[closest] / 100.0
            vol_series.append(min(1.0, v / 5.0))   # %5 volatilite = 1.0
        else:
            vol_series.append(0.3)

    # SRI = 0.6 * z_norm + 0.4 * volatilite
    sri_series = [0.6 * z + 0.4 * v for z, v in zip(z_norm, vol_series)]

    # Alarm sinyalleri
    alarms = [1 if s >= SRI_ALARM else 0 for s in sri_series]

    # Amnesia belleği
    memory = apply_amnesia(alarms)

    # Kriz indeksi (0-1) — amnesia belleği de dahil
    # Yüksek bellek → sistem tehlikeye çok yakın bir dönemde
    crisis_idx = []
    for s, m, a in zip(sri_series, memory, alarms):
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
            "sri":      round(sri_series[i], 4),
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
        "dei":         0.71,   # statik (yapısal bozunma — ayrı modelden)
        "sigma":       SIGMA,
        "lam":         LAMBDA,
        "data_points": len(output)
    }

    result = {"summary": summary, "series": output}
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"OK: {len(output)} gunluk veri uretildi -> {OUT_FILE}")
    print(f"   Dun ({yesterday}): CI={last['ci']}, SRI={last['sri']}, Alarm={last['alarm']}")
    print(f"   Bellek: {last['memory']} | L6: {summary['l6_active']}")

if __name__ == "__main__":
    compute_crisis_index()
