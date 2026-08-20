import os
import urllib.request
import pandas as pd
import numpy as np

data_dir = r"B:\Hariseldon\data\US_Historical_1900_2026"
os.makedirs(data_dir, exist_ok=True)

print("=" * 80)
print("DOWNLOADING US HISTORICAL DATASETS (1900 - 2026)")
print("=" * 80)

# 1. Robert Shiller Master Dataset (1871 - 2026)
shiller_url = "http://www.econ.yale.edu/~shiller/data/ie_data.xls"
shiller_dest = os.path.join(data_dir, "shiller_ie_data.xls")

try:
    print("Downloading Robert Shiller US Dataset (1871-2026)...")
    req = urllib.request.Request(
        shiller_url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req, timeout=30) as response, open(shiller_dest, 'wb') as out_file:
        out_file.write(response.read())
    print(f"  Downloaded: {shiller_dest} ({os.path.getsize(shiller_dest)/1024:.1f} KB)")
except Exception as e:
    print(f"  Shiller download error: {e}")

# 2. FRED (St. Louis Fed) Key Historical Series (1900 - 2026)
fred_series = {
    # Interest Rates & Yields
    "GS10": "10-Year Treasury Constant Maturity Rate",
    "TB3MS": "3-Month Treasury Bill Secondary Market Rate",
    "FEDFUNDS": "Federal Funds Effective Rate",
    "BAA10Y": "Moody's Seasoned Baa Corporate Bond Yield Relative to 10Y Treasury (Credit Spread)",
    "AAA": "Moody's Seasoned Aaa Corporate Bond Yield",
    "BAA": "Moody's Seasoned Baa Corporate Bond Yield",
    # Inflation & Prices
    "CPIAUCNS": "Consumer Price Index for All Urban Consumers (CPI)",
    "WTISPLC": "Spot Crude Oil Price: West Texas Intermediate (WTI)",
    # Macro & Production
    "INDPRO": "Industrial Production Index",
    "UNRATE": "Unemployment Rate",
    "GDPC1": "Real Gross Domestic Product",
    # Money & Banking
    "M2SL": "M2 Money Stock",
    "TOTBKCR": "Bank Credit, All Commercial Banks",
    "BUSLOANS": "Commercial and Industrial Loans, All Commercial Banks",
    "DPSACBW027SBOG": "Deposits, All Commercial Banks",
    "GFDEGDQ188S": "Federal Debt: Total Public Debt as Percent of GDP",
    # NBER Historical Long Series (1850s-1970s)
    "M0892AUSM156SNBR": "NBER Historical Short-Term Interest Rates (1857-1970)",
    "M04051USM324NNBR": "NBER Index of Wholesale Prices (1890-1951)"
}

for series_id, name in fred_series.items():
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    dest = os.path.join(data_dir, f"{series_id}.csv")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=20) as response, open(dest, 'wb') as out_file:
            out_file.write(response.read())
        sz = os.path.getsize(dest)
        print(f"  [FRED] {series_id} ({sz/1024:.1f} KB) -> {name}")
    except Exception as e:
        print(f"  [FRED] Failed {series_id}: {e}")

print("\nDownload batch completed! Checking files in data directory...")
for f in os.listdir(data_dir):
    p = os.path.join(data_dir, f)
    print(f"  - {f} ({os.path.getsize(p)/1024:.1f} KB)")
