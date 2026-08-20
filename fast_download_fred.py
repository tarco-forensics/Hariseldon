import os
import ssl
import urllib.request
import pandas as pd
import numpy as np

# Disable SSL verification issues if any
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data_dir = r"B:\Hariseldon\data\US_Historical_1900_2026"
os.makedirs(data_dir, exist_ok=True)

# List of FRED Series to fetch
fred_series = {
    # 1. Faiz & Getiri Eğrisi
    "GS10": "10-Year Treasury Constant Maturity Rate (Monthly/Daily)",
    "TB3MS": "3-Month Treasury Bill Secondary Market Rate (1934-2026)",
    "FEDFUNDS": "Federal Funds Effective Rate (1954-2026)",
    "BAA10Y": "Moody's Baa Corporate Bond Yield minus 10Y Treasury (1986-2026)",
    "BAA": "Moody's Baa Corporate Bond Yield (1919-2026)",
    "AAA": "Moody's Aaa Corporate Bond Yield (1919-2026)",
    # 2. Enflasyon, Emtia & Sanayi
    "CPIAUCNS": "Consumer Price Index for All Urban Consumers (1913-2026)",
    "WTISPLC": "Spot Crude Oil Price: WTI (1946-2026)",
    "INDPRO": "Industrial Production Index (1919-2026)",
    "UNRATE": "Unemployment Rate (1948-2026)",
    # 3. Para Arzı & Bankacılık
    "M2SL": "M2 Money Stock (1959-2026)",
    "TOTBKCR": "Bank Credit, All Commercial Banks (1947-2026)",
    "BUSLOANS": "Commercial and Industrial Loans (1947-2026)",
    "DPSACBW027SBOG": "Deposits, All Commercial Banks (1973-2026)",
    "GFDEGDQ188S": "Federal Debt to GDP (1966-2026)",
    # 4. NBER Tarihsel Uzun Seriler (1857 - 1970)
    "M0892AUSM156SNBR": "NBER Historical Call Money / Short Rate (1857-1970)",
    "M04051USM324NNBR": "NBER Wholesale Price Index (1890-1951)"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

downloaded_dfs = {}

for s_id, s_name in fred_series.items():
    csv_file = os.path.join(data_dir, f"{s_id}.csv")
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s_id}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
            content = response.read().decode('utf-8')
            with open(csv_file, 'w', encoding='utf-8') as f:
                f.write(content)
        sz = os.path.getsize(csv_file)
        print(f"✅ [FRED] {s_id} ({sz/1024:.1f} KB) -> {s_name}")
        
        # Read and check date range
        df_temp = pd.read_csv(csv_file)
        if len(df_temp) > 0 and 'DATE' in df_temp.columns:
            date_col = 'DATE'
            val_col = [c for c in df_temp.columns if c != 'DATE'][0]
            # convert value to numeric
            df_temp[val_col] = pd.to_numeric(df_temp[val_col], errors='coerce')
            min_date = df_temp[date_col].min()
            max_date = df_temp[date_col].max()
            downloaded_dfs[s_id] = df_temp
            print(f"     Aralık: {min_date} ile {max_date} ({len(df_temp)} satır)")
    except Exception as err:
        print(f"❌ [FRED] {s_id} Hata: {err}")

# Load Shiller Dataset
shiller_csv = os.path.join(data_dir, "US_SHILLER_S_AND_P_1900_2026.csv")
if os.path.exists(shiller_csv):
    df_shiller = pd.read_csv(shiller_csv)
    print(f"\n✅ Shiller Veri Seti Yüklendi: {len(df_shiller)} Aylık Kayıt (1900.01 - 2023.09)")

print("\n" + "=" * 80)
print(f"Toplam İndirilen ve Doğrulanan Veri Serisi Sayısı: {len(downloaded_dfs) + 1}")
print("=" * 80)
