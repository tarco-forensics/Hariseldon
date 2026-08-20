import os
import json
import pandas as pd
import numpy as np

data_dir = r"B:\Hariseldon\data\US_Historical_1900_2026"

print("=" * 80)
print("BUILDING UNIFIED MASTER US TIME SERIES (1900 - 2026)")
print("=" * 80)

# 1. Load Shiller Data
shiller_path = os.path.join(data_dir, "shiller_ie_data.xls")
df_shiller = pd.read_excel(shiller_path, sheet_name="Data", skiprows=7)
df_shiller = df_shiller.iloc[:, :13]
df_shiller.columns = [
    "Date_Raw", "SP_Price", "Dividend", "Earnings", "CPI", 
    "Date_Fraction", "Rate_GS10", "Real_Price", "Real_Dividend", 
    "Real_Total_Return_Price", "Real_Earnings", "Real_TR_Earnings", "CAPE"
]

def parse_shiller_date(d):
    try:
        s = f"{float(d):.2f}"
        year, month = s.split('.')
        m_int = int(month)
        if m_int == 10:
            m_str = "10"
        elif m_int == 1:
            m_str = "01"
        else:
            m_str = f"{m_int:02d}"
        return f"{year}-{m_str}-01"
    except:
        return None

df_shiller['Date'] = df_shiller['Date_Raw'].apply(parse_shiller_date)
df_shiller['Date'] = pd.to_datetime(df_shiller['Date'], errors='coerce')
df_shiller = df_shiller.dropna(subset=['Date'])
df_shiller = df_shiller[df_shiller['Date'] >= '1900-01-01'].sort_values('Date').reset_index(drop=True)

for col in ["SP_Price", "Dividend", "Earnings", "CPI", "Rate_GS10", "Real_Price", "Real_Dividend", "Real_Earnings", "CAPE"]:
    df_shiller[col] = pd.to_numeric(df_shiller[col], errors='coerce')

print(f"Shiller S&P/CPI/Rates 1900-2026: {len(df_shiller)} monthly records (From {df_shiller['Date'].min().strftime('%Y-%m')} to {df_shiller['Date'].max().strftime('%Y-%m')})")

# 2. Load Gold Prices
gold_path = os.path.join(data_dir, "US_Gold_Historical.csv")
if os.path.exists(gold_path):
    df_gold = pd.read_csv(gold_path)
    df_gold.columns = [c.strip() for c in df_gold.columns]
    date_col = [c for c in df_gold.columns if 'date' in c.lower()][0]
    val_col = [c for c in df_gold.columns if 'price' in c.lower() or 'val' in c.lower()][0]
    df_gold['Date'] = pd.to_datetime(df_gold[date_col], errors='coerce')
    df_gold['Gold_USD_oz'] = pd.to_numeric(df_gold[val_col], errors='coerce')
    df_gold = df_gold.dropna(subset=['Date']).sort_values('Date')
    df_shiller = pd.merge_asof(df_shiller, df_gold[['Date', 'Gold_USD_oz']], on='Date', direction='backward')
    print(f"Merged Gold Price: {df_shiller['Gold_USD_oz'].notnull().sum()} non-null records")

# 3. Load Oil Prices
oil_path = os.path.join(data_dir, "US_Oil_Historical.csv")
if os.path.exists(oil_path):
    df_oil = pd.read_csv(oil_path)
    df_oil.columns = [c.strip() for c in df_oil.columns]
    date_col = [c for c in df_oil.columns if 'date' in c.lower()][0]
    val_col = [c for c in df_oil.columns if 'price' in c.lower() or 'val' in c.lower()][0]
    df_oil['Date'] = pd.to_datetime(df_oil[date_col], errors='coerce')
    df_oil['Oil_WTI_bbl'] = pd.to_numeric(df_oil[val_col], errors='coerce')
    df_oil = df_oil.dropna(subset=['Date']).sort_values('Date')
    df_shiller = pd.merge_asof(df_shiller, df_oil[['Date', 'Oil_WTI_bbl']], on='Date', direction='backward')
    print(f"Merged Oil Price: {df_shiller['Oil_WTI_bbl'].notnull().sum()} non-null records")

# 4. Calculate Derived T2SAIM Metrics on Real Data:
df_shiller['CPI_YoY_Inflation'] = df_shiller['CPI'].pct_change(12) * 100.0
df_shiller['SP_Peak'] = df_shiller['Real_Price'].cummax()
df_shiller['SP_Drawdown_Pct'] = (df_shiller['Real_Price'] - df_shiller['SP_Peak']) / df_shiller['SP_Peak'] * 100.0

df_shiller['SP_MoM_Return'] = df_shiller['SP_Price'].pct_change(1)
df_shiller['SP_Realized_Vol_12M'] = df_shiller['SP_MoM_Return'].rolling(12).std() * np.sqrt(12) * 100.0
df_shiller['Rate_GS10_YoY_Delta'] = df_shiller['Rate_GS10'].diff(12)

def compute_empirical_a_load(row):
    vol_norm = min(1.0, (row['SP_Realized_Vol_12M'] if not pd.isna(row['SP_Realized_Vol_12M']) else 15.0) / 40.0)
    dd_norm = min(1.0, abs(row['SP_Drawdown_Pct'] if not pd.isna(row['SP_Drawdown_Pct']) else 0.0) / 60.0)
    inf_norm = min(1.0, max(0.0, (row['CPI_YoY_Inflation'] if not pd.isna(row['CPI_YoY_Inflation']) else 2.0)) / 15.0)
    raw = 0.40 * vol_norm + 0.40 * dd_norm + 0.20 * inf_norm
    return float(1.0 / (1.0 + np.exp(-10.0 * (raw - 0.45))))

df_shiller['Empirical_A_load'] = df_shiller.apply(compute_empirical_a_load, axis=1)
df_shiller['Empirical_PFC_control'] = (1.0 - df_shiller['Empirical_A_load']) * 100.0

df_shiller['CAPE_Roll_Mean_30Y'] = df_shiller['CAPE'].rolling(360, min_periods=60).mean()
df_shiller['CAPE_Roll_Std_30Y'] = df_shiller['CAPE'].rolling(360, min_periods=60).std()
df_shiller['CAPE_Z_Score'] = (df_shiller['CAPE'] - df_shiller['CAPE_Roll_Mean_30Y']) / df_shiller['CAPE_Roll_Std_30Y']

df_shiller['Empirical_CI'] = np.clip(
    0.35 * df_shiller['Empirical_A_load'] + 
    0.30 * (abs(df_shiller['SP_Drawdown_Pct']) / 60.0).clip(0, 1) + 
    0.20 * (df_shiller['CAPE_Z_Score'].clip(0, 3) / 3.0).fillna(0.3) + 
    0.15 * (abs(df_shiller['Rate_GS10_YoY_Delta']).clip(0, 4) / 4.0).fillna(0.2),
    0.0, 1.0
)

df_shiller['Date_Str'] = df_shiller['Date'].dt.strftime('%Y-%m-%d')

out_csv = os.path.join(data_dir, "US_MASTER_MACRO_TIME_SERIES_1900_2026.csv")
out_json = os.path.join(data_dir, "US_MASTER_MACRO_TIME_SERIES_1900_2026.json")

df_shiller.to_csv(out_csv, index=False)

records = df_shiller[['Date_Str', 'SP_Price', 'CPI', 'CPI_YoY_Inflation', 'Rate_GS10', 'CAPE', 'Gold_USD_oz', 'Oil_WTI_bbl', 'SP_Drawdown_Pct', 'SP_Realized_Vol_12M', 'Empirical_A_load', 'Empirical_PFC_control', 'Empirical_CI']].to_dict(orient='records')
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2)

print(f"\n Master Dataset successfully created!")
print(f"  CSV: {out_csv} ({os.path.getsize(out_csv)/1024:.1f} KB)")
print(f"  JSON: {out_json} ({os.path.getsize(out_json)/1024:.1f} KB)")
print(f"  Total Monthly Timestamp Count (1900-2026): {len(df_shiller)}")

# Sample key crisis moments in history
print("\n--- SAMPLE CRISIS PERIODS IN REAL DATA ---")
sample_dates = ["1907-10-01", "1929-10-01", "1932-06-01", "1973-11-01", "1980-03-01", "1987-10-01", "2000-03-01", "2008-10-01", "2020-03-01"]
for sd in sample_dates:
    row = df_shiller[df_shiller['Date_Str'] == sd]
    if len(row) > 0:
        r = row.iloc[0]
        print(f"[{sd}] SP:{r['SP_Price']:.1f} | CPI Infl:%{r['CPI_YoY_Inflation']:.1f} | 10Y:{r['Rate_GS10']:.2f}% | Drawdown:%{r['SP_Drawdown_Pct']:.1f} | A_load:{r['Empirical_A_load']:.3f} | CI:{r['Empirical_CI']:.3f}")
