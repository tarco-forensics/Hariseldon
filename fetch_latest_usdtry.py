"""
T2SAIM Production Start — 2026-06-15
Eksik günleri yFinance ile tamamla, crisis_data.json'ı yenile.
"""
import csv, json, subprocess, sys, os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "T2SAIM_NEXUS", "Macroekonomics", "hermes_crisis_lab", "data")
if not os.path.exists(DATA_DIR):
    DATA_DIR = r"B:\T2SAIM_NEXUS\Macroekonomics\hermes_crisis_lab\data"
USDTRY_FILE = os.path.join(DATA_DIR, "USDTRY_gunluk.csv")

if not os.path.exists(USDTRY_FILE):
    print(f"⚠️ {USDTRY_FILE} not found. Skipping USDTRY fetch.")
    sys.exit(0)

# Son tarihi oku
with open(USDTRY_FILE, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
last_date = rows[-1]["tarih"]
print(f"Son mevcut veri: {last_date}")

# yfinance ile eksik günleri çek
try:
    import yfinance as yf
    start = (datetime.strptime(last_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    end   = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"Cekiliyor: {start} -> {end}")
    df = yf.download("USDTRY=X", start=start, end=end, interval="1d", progress=False)
    if not df.empty:
        new_rows = []
        for idx, row in df.iterrows():
            d = idx.strftime("%Y-%m-%d")
            o = float(row["Open"])
            h = float(row["High"])
            l = float(row["Low"])
            c = float(row["Close"])
            new_rows.append({"tarih": d, "acilis": round(o,4), "yuksek": round(h,4), "dusuk": round(l,4), "kapanis": round(c,4)})
        # Mevcut dosyaya ekle
        with open(USDTRY_FILE, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["tarih","acilis","yuksek","dusuk","kapanis"])
            for r in new_rows:
                writer.writerow(r)
        print(f"Eklendi: {len(new_rows)} yeni gun")
        for r in new_rows:
            print(f"  {r['tarih']}: {r['kapanis']}")
    else:
        print("Yeni veri yok (piyasa kapali olabilir)")
except ImportError:
    print("yfinance yuklu degil — pip install yfinance")
    sys.exit(1)
except Exception as e:
    print(f"Hata: {e}")
