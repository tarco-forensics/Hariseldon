import os
import json
import numpy as np
import pandas as pd

# ==============================================================================
# T2SAIM "BACK TO THE FUTURE" AMNESIA DİNAMİK MODEL (1900 - 2026) - TAM FORMÜLASYON
# ==============================================================================

data_path = r"B:\Hariseldon\data\US_Historical_1900_2026\US_MASTER_MACRO_TIME_SERIES_1900_2026.csv"
fred_dir = r"E:\T2SAIM_NEXUS_MIRROR\0A0A0_ENGINE_ROOM\LİBRARY_T2SAIM\50_Works\T2SAIM_Total_Vault\B_James_Projects\James_Work_Rescue\Kalibrasyon\ABD kalibrasyon"

df = pd.read_csv(data_path)
df['Date'] = pd.to_datetime(df['Date_Str']).astype('datetime64[ns]')
df = df.sort_values('Date').reset_index(drop=True)

# Integrate FRED yield spread if available
t10y2y_file = os.path.join(fred_dir, "T10Y2Y_fred.txt")
if os.path.exists(t10y2y_file):
    try:
        df_spread = pd.read_csv(t10y2y_file, sep=r'\s+', names=['Date_Str', 'Yield_Spread_10Y2Y'], skiprows=1)
        df_spread['Date'] = pd.to_datetime(df_spread['Date_Str'], errors='coerce').astype('datetime64[ns]')
        df_spread['Yield_Spread_10Y2Y'] = pd.to_numeric(df_spread['Yield_Spread_10Y2Y'], errors='coerce')
        df_spread = df_spread.dropna(subset=['Date']).sort_values('Date')
        df_spread_m = df_spread.set_index('Date').resample('MS').mean().reset_index()
        df = pd.merge_asof(df, df_spread_m, on='Date', direction='backward')
    except Exception as e:
        pass

if 'Yield_Spread_10Y2Y' not in df.columns:
    df['Yield_Spread_10Y2Y'] = np.nan

LAMBDA_YEARLY = 0.15
LAMBDA_MONTHLY = 1.0 - (1.0 - LAMBDA_YEARLY) ** (1.0 / 12.0)

memory_series = []
a_load_oos = []
bfi_oos = []
sri_oos = []
ci_oos = []
alarm_oos = []

current_memory = 2.0

known_us_crises = [
    {"start": "1907-03-01", "crash": "1907-10-01", "name": "1907 Bankerler Paniği"},
    {"start": "1913-12-01", "crash": "1914-08-01", "name": "1914 1. Dünya Savaşı Borsa Kapanması"},
    {"start": "1919-08-01", "crash": "1920-05-01", "name": "1920-1921 Savaş Sonrası Deflasyon"},
    {"start": "1929-01-01", "crash": "1929-10-01", "name": "1929 Büyük Buhran & Borsa Çöküşü"},
    {"start": "1937-03-01", "crash": "1937-10-01", "name": "1937-1938 Çift Dip Resesyonu"},
    {"start": "1973-01-01", "crash": "1973-11-01", "name": "1973 OPEC Petrol Şoku & Stagflasyon"},
    {"start": "1979-06-01", "crash": "1980-03-01", "name": "1980-1982 Volcker Şoku & Çift Resesyon"},
    {"start": "1987-05-01", "crash": "1987-10-01", "name": "1987 Kara Pazartesi (Flash Crash)"},
    {"start": "1990-01-01", "crash": "1990-08-01", "name": "1990 S&L / Körfez Savaşı Krizi"},
    {"start": "2000-01-01", "crash": "2000-09-01", "name": "2000-2002 Dot-Com Balonu Çöküşü"},
    {"start": "2007-07-01", "crash": "2008-09-01", "name": "2007-2008 Küresel Finansal Kriz (GFC)"},
    {"start": "2020-01-01", "crash": "2020-03-01", "name": "2020 COVID-19 Likidite Şoku"},
    {"start": "2022-06-01", "crash": "2023-03-01", "name": "2023 Silicon Valley Bank (SVB) Krizi"}
]

print("=" * 90)
print("🚀 RUNNING BACK TO THE FUTURE WALK-FORWARD SIMULATION WITH FULL T2SAIM MATRIX")
print("=" * 90)

for i in range(len(df)):
    row = df.iloc[i]
    
    # 1. Strictly Out-Of-Sample Data Slicing (Only past history up to i)
    past_prices = df.iloc[max(0, i-120):i+1]['Real_Price'].values
    past_cpi = df.iloc[max(0, i-120):i+1]['CPI'].values
    past_rates = df.iloc[max(0, i-120):i+1]['Rate_GS10'].values
    past_cape = df.iloc[max(0, i-360):i+1]['CAPE'].values
    
    past_peak = np.max(past_prices)
    curr_price = row['Real_Price']
    drawdown_pct = (curr_price - past_peak) / past_peak * 100.0 if past_peak > 0 else 0.0
    
    # Realized Volatility
    if len(past_prices) > 12:
        returns = np.diff(past_prices[-13:]) / past_prices[-13:-1]
        vol_12m = np.std(returns) * np.sqrt(12) * 100.0
    else:
        vol_12m = 15.0
        
    # Inflation YoY
    if len(past_cpi) > 12:
        infl_yoy = (past_cpi[-1] - past_cpi[-13]) / past_cpi[-13] * 100.0
    else:
        infl_yoy = 2.0
        
    # 10Y Rate Delta
    if len(past_rates) > 12:
        rate_delta = past_rates[-1] - past_rates[-13]
    else:
        rate_delta = 0.0
        
    # Out-of-sample CAPE Valuation Z-score
    curr_cape = row['CAPE']
    if len(past_cape) >= 60 and not np.isnan(curr_cape):
        cape_mean = np.nanmean(past_cape)
        cape_std = np.nanstd(past_cape)
        cape_z = (curr_cape - cape_mean) / cape_std if cape_std > 0 else 0.0
    else:
        cape_z = 0.0
        
    # 2. Amnesia Memory Dynamics: M(t) = M(t-1)*(1-lambda) + Shock(t)
    shock_intensity = 0.0
    if drawdown_pct < -15.0 or vol_12m > 25.0 or abs(infl_yoy) > 8.0:
        shock_intensity = min(5.0, abs(drawdown_pct) / 15.0 + vol_12m / 15.0)
        current_memory = min(5.0, current_memory + shock_intensity * 0.35)
    else:
        # Amnesia Decay: Memory fades smoothly over time
        current_memory = max(0.1, current_memory * (1.0 - LAMBDA_MONTHLY))
    
    memory_series.append(current_memory)
    
    # 3. Dual-Mode A_load: Panic Mode OR Euphoria/Bubble Fragility Mode
    v_norm = min(1.0, vol_12m / 35.0)
    dd_norm = min(1.0, abs(drawdown_pct) / 50.0)
    inf_norm = min(1.0, max(0.0, infl_yoy) / 12.0)
    bubble_norm = min(1.0, max(0.0, cape_z) / 2.2) # CAPE Z-Score > 2.0
    
    # When memory is nearly zero (M < 1.0) and Bubble is high -> Systemic Fragility is amplified
    amnesia_bubble_amplifier = 1.0 + max(0.0, (2.0 - current_memory) / 2.0) * bubble_norm * 0.8
    
    panic_stress = 0.40 * v_norm + 0.40 * dd_norm + 0.20 * inf_norm
    bubble_stress = 0.65 * bubble_norm + 0.35 * min(1.0, max(0.0, rate_delta) / 2.0)
    
    total_stress = max(panic_stress, bubble_stress) * amnesia_bubble_amplifier
    a_load = float(1.0 / (1.0 + np.exp(-8.0 * (total_stress - 0.38))))
    a_load_oos.append(a_load)
    
    # 4. Out-Of-Sample BFI
    yield_spread = row.get('Yield_Spread_10Y2Y', np.nan)
    if pd.isna(yield_spread):
        spread_stress = min(1.0, max(0.0, rate_delta) / 2.0)
    else:
        # Inverted yield curve (T10Y2Y < 0) is a massive banking/ALM alarm
        spread_stress = min(1.0, max(0.0, -yield_spread) / 0.6) if yield_spread < 0 else 0.1
        
    bfi = min(1.0, 0.45 * spread_stress + 0.30 * bubble_norm + 0.25 * v_norm)
    bfi_oos.append(bfi)
    
    # 5. Composite Crisis Index (CI) & Systemic Resonance (SRI)
    sri = (a_load * bfi * max(0.10, max(dd_norm, bubble_norm))) ** (1.0 / 3.0)
    sri_oos.append(sri)
    
    ci = np.clip(0.35 * a_load + 0.30 * bfi + 0.20 * max(dd_norm, bubble_norm) + 0.15 * inf_norm, 0.0, 1.0)
    ci_oos.append(ci)
    
    # Phase Lock Trigger Check
    is_alarm = (ci >= 0.48) or (sri >= 0.38 and a_load >= 0.52)
    alarm_oos.append(1 if is_alarm else 0)

df['Memory_M'] = memory_series
df['A_load_OOS'] = a_load_oos
df['BFI_OOS'] = bfi_oos
df['SRI_OOS'] = sri_oos
df['CI_OOS'] = ci_oos
df['Alarm_OOS'] = alarm_oos

# 3. Evaluate Lead Time & Detection for Each Known Crisis
crisis_eval = []
for kc in known_us_crises:
    c_crash = pd.to_datetime(kc['crash'])
    
    # Window 24 months before crash to crash date
    search_start = c_crash - pd.DateOffset(months=24)
    slice_df = df[(df['Date'] >= search_start) & (df['Date'] <= c_crash)]
    
    alarm_rows = slice_df[slice_df['Alarm_OOS'] == 1]
    if len(alarm_rows) > 0:
        first_alarm_date = alarm_rows.iloc[0]['Date']
        lead_months = (c_crash.year - first_alarm_date.year) * 12 + (c_crash.month - first_alarm_date.month)
        detected = True
        peak_ci = slice_df['CI_OOS'].max()
        peak_a_load = slice_df['A_load_OOS'].max()
    else:
        first_alarm_date = None
        lead_months = 0
        detected = False
        peak_ci = slice_df['CI_OOS'].max() if len(slice_df) > 0 else 0.0
        peak_a_load = slice_df['A_load_OOS'].max() if len(slice_df) > 0 else 0.0
        
    crisis_eval.append({
        "name": kc['name'],
        "crash_date": kc['crash'],
        "first_alarm_date": first_alarm_date.strftime('%Y-%m') if first_alarm_date else "N/A",
        "lead_time_months": lead_months,
        "peak_CI": round(float(peak_ci), 3),
        "peak_A_load": round(float(peak_a_load), 3),
        "detected": detected
    })

df_eval = pd.DataFrame(crisis_eval)

print("\n" + "=" * 90)
print("📊 BACK TO THE FUTURE: 126 YILLIK AMNESIA KRİZ ERKEN UYARI PERFORMANSI")
print("=" * 90)
print(df_eval[["name", "crash_date", "first_alarm_date", "lead_time_months", "peak_CI", "detected"]].to_string(index=False))

# Accuracy & Metrics
total_c = len(crisis_eval)
detected_c = sum(1 for r in crisis_eval if r['detected'])
avg_lead = np.mean([r['lead_time_months'] for r in crisis_eval if r['detected']])

print("\n" + "=" * 60)
print("🎯 MODEL DOĞRULAMA METRİKLERİ:")
print(f"Toplam Test Edilen Büyük ABD Krizi: {total_c}")
print(f"Başarıyla Tespit Edilen Kriz Sayısı: {detected_c} / {total_c} (%{detected_c/total_c*100.0:.1f})")
print(f"Ortalama Erken Uyarı Menzili (Lead-Time): {avg_lead:.1f} AY ÖNCEDEN")
print(f"Amnesia Yarı Ömrü (t_half): 4.62 Yıl | Kuşaksal Unutma Katsayısı (lambda): 0.15/yıl")
print("=" * 60)

# Save result JSON
out_results_json = r"B:\Hariseldon\Knowledge_Base\Indicators_Catalog\T2SAIM_AMNESIA_BACK_TO_FUTURE_RESULTS.json"
out_results_md = r"B:\Hariseldon\Knowledge_Base\Indicators_Catalog\T2SAIM_AMNESIA_BACK_TO_FUTURE_RESULTS.md"

with open(out_results_json, "w", encoding="utf-8") as f:
    json.dump(crisis_eval, f, indent=4, ensure_ascii=False)

print(f"\nSaved Back-to-Future results to: {out_results_json}")
