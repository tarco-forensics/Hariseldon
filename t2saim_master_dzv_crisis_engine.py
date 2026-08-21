# -*- coding: utf-8 -*-
"""
====================================================================================================
T2SAIM MASTER DZV KRİZ TESPİT VE ERKEN UYARI MOTORU (1900 - 2026)
====================================================================================================
Metodoloji: Sıfır Gelecek Bilgisi (Zero Lookahead Bias) & Kayan Pencereli (Walk-Forward Out-of-Sample)
Matematiksel Çerçeve:
  1. Kuşaksal Unutma (Amnesia): M(t) = M(t-1)*(1-lambda) + Shock(t)  (lambda = 0.15/yıl)
  2. İkili Amigdala Yükü: A_load(t) = sigma(8.0 * (max(Panic, Bubble) * Amplifier - 0.38))
  3. Minsky Diferansiyel Borç: S_D(t) ~ t, S_S(t) ~ t^2, dP/dt = -lambda_P[V_S - V_D - S_D + S_S]
  4. Kuple Osilatörler Rezonansı: R(t) = Delta_0 / sqrt((w_fin^2 - w_reel^2)^2 + 4*gamma^2*w_reel^2)
  5. Sistemik Rezonans & Birleşik Kriz İndeksi: SRI(t), CI(t)
DZV Epistemolojisi:
  - Diyalektik (D): Doğrusal Varlık İllüzyonu vs. Parabolik Borç Servisi Çelişkisi
  - Zorunluluk (Z): Nakit Akışı Kilitlenmesi ve Rezonans Tekilliği (t*)
  - Varyans (V): Enformasyon Asimetrisi (G_def) ve Amigdala Stres Salınımı
====================================================================================================
"""

import os
import json
import numpy as np
import pandas as pd
from datetime import datetime

class T2SAIMMasterCrisisEngine:
    def __init__(self, data_csv_path: str, lambda_yearly: float = 0.15):
        """
        T2SAIM Master Kriz Motoru İlklendiricisi
        """
        self.data_csv_path = data_csv_path
        self.lambda_yearly = lambda_yearly
        self.lambda_monthly = 1.0 - (1.0 - lambda_yearly) ** (1.0 / 12.0)
        self.t_half = np.log(2.0) / lambda_yearly  # 4.62 Yıl
        
        self.df = None
        self.results = None
        
        self.known_crises = [
            {"start": "1907-03-01", "crash": "1907-10-01", "name": "1907 Bankerler Paniği"},
            {"start": "1913-12-01", "crash": "1914-08-01", "name": "1914 1. Dünya Savaşı Borsa Kapanması"},
            {"start": "1919-08-01", "crash": "1920-05-01", "name": "1920-1921 Savaş Sonrası Deflasyon"},
            {"start": "1929-01-01", "crash": "1929-10-01", "name": "1929 Büyük Buhran & Wall Street Çöküşü"},
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

    def load_data(self):
        """Veri tabanını yükle ve tarih formatını senkronize et"""
        if not os.path.exists(self.data_csv_path):
            raise FileNotFoundError(f"Veri dosyası bulunamadı: {self.data_csv_path}")
        
        df = pd.read_csv(self.data_csv_path)
        df['Date'] = pd.to_datetime(df['Date_Str']).astype('datetime64[ns]')
        df = df.sort_values('Date').reset_index(drop=True)
        self.df = df
        print(f"✅ Toplam Yüklenen Aylık Makro Veri Satırı: {len(self.df)} (1900-2026)")
        return self.df

    @staticmethod
    def sigmoid(x: float) -> float:
        """Lojistik Aktivasyon Fonksiyonu"""
        return float(1.0 / (1.0 + np.exp(-x)))

    @staticmethod
    def coupled_resonance(w_fin: float, w_reel: float, gamma: float = 0.12, delta_0: float = 1.0) -> float:
        """Kuple Osilatör Rezonans Genlik Fonksiyonu R(t)"""
        denom = np.sqrt((w_fin**2 - w_reel**2)**2 + 4.0 * (gamma**2) * (w_reel**2))
        return float(delta_0 / denom) if denom > 1e-6 else 100.0

    def run_walk_forward_amnesia_simulation(self):
        """
        Sıfır Gelecek Bilgisi (Zero Lookahead Bias) ile Walk-Forward Kriz Simülasyonu
        """
        if self.df is None:
            self.load_data()

        df = self.df
        n = len(df)
        
        memory_series = []
        a_load_series = []
        bfi_series = []
        sri_series = []
        ci_series = []
        alarm_series = []
        resonance_series = []
        
        current_memory = 2.0  # Başlangıç tarihsel bellek
        
        for i in range(n):
            row = df.iloc[i]
            
            # --- 1. SIFIR GELECEK BİLGİSİ İLE GEÇMİŞ VERİ PENCERESİ ---
            past_prices = df.iloc[max(0, i-120):i+1]['Real_Price'].values
            past_cpi = df.iloc[max(0, i-120):i+1]['CPI'].values
            past_rates = df.iloc[max(0, i-120):i+1]['Rate_GS10'].values
            past_cape = df.iloc[max(0, i-360):i+1]['CAPE'].values
            
            curr_price = row['Real_Price']
            past_peak = np.max(past_prices)
            drawdown_pct = (curr_price - past_peak) / past_peak * 100.0 if past_peak > 0 else 0.0
            
            # 12 Aylık Gerçekleşen Volatilite
            if len(past_prices) > 12:
                returns = np.diff(past_prices[-13:]) / past_prices[-13:-1]
                vol_12m = float(np.std(returns) * np.sqrt(12) * 100.0)
            else:
                vol_12m = 15.0
                
            # Yıllık Enflasyon (YoY)
            if len(past_cpi) > 12:
                infl_yoy = float((past_cpi[-1] - past_cpi[-13]) / past_cpi[-13] * 100.0)
            else:
                infl_yoy = 2.0
                
            # 10 Yıllık Faiz Değişimi
            if len(past_rates) > 12:
                rate_delta = float(past_rates[-1] - past_rates[-13])
            else:
                rate_delta = 0.0
                
            # Out-of-Sample CAPE Değerleme Z-Skoru
            curr_cape = row['CAPE']
            if len(past_cape) >= 60 and not np.isnan(curr_cape):
                cape_mean = np.nanmean(past_cape)
                cape_std = np.nanstd(past_cape)
                cape_z = float((curr_cape - cape_mean) / cape_std) if cape_std > 0 else 0.0
            else:
                cape_z = 0.0

            # --- 2. AMNESIA KUŞAKSAL UNUTMA DİNAMİĞİ ---
            # M(t) = M(t-1)*(1-lambda) + Shock(t)
            if drawdown_pct < -15.0 or vol_12m > 25.0 or abs(infl_yoy) > 8.0:
                shock_intensity = min(5.0, abs(drawdown_pct) / 15.0 + vol_12m / 15.0)
                current_memory = min(5.0, current_memory + shock_intensity * 0.35)
            else:
                # Hafıza zamanla üstel söner
                current_memory = max(0.1, current_memory * (1.0 - self.lambda_monthly))
            
            memory_series.append(current_memory)
            
            # --- 3. İKİLİ AMİGDALA STRES YÜKÜ (A_load) ---
            v_norm = min(1.0, max(0.0, vol_12m / 35.0))
            dd_norm = min(1.0, max(0.0, abs(drawdown_pct) / 50.0))
            inf_norm = min(1.0, max(0.0, infl_yoy) / 12.0)
            bubble_norm = min(1.0, max(0.0, cape_z) / 2.2)
            
            # Hafıza dipte (M < 1.0) ve Değerleme tepedeyse kırılganlık çarpanı patlar
            amnesia_bubble_amplifier = 1.0 + max(0.0, (2.0 - current_memory) / 2.0) * bubble_norm * 0.8
            
            panic_stress = 0.40 * v_norm + 0.40 * dd_norm + 0.20 * inf_norm
            bubble_stress = 0.65 * bubble_norm + 0.35 * min(1.0, max(0.0, rate_delta) / 2.0)
            
            total_stress = max(panic_stress, bubble_stress) * amnesia_bubble_amplifier
            a_load = self.sigmoid(8.0 * (total_stress - 0.38))
            a_load_series.append(a_load)
            
            # --- 4. BANKACILIK KIRILGANLIK İNDEKSİ (BFI) & KUPLE REZONANS ---
            spread_stress = min(1.0, max(0.0, rate_delta) / 2.0)
            bfi = min(1.0, 0.45 * spread_stress + 0.30 * bubble_norm + 0.25 * v_norm)
            bfi_series.append(bfi)
            
            # Kuple Osilatör Rezonansı R(t)
            w_fin = 1.0 + float(a_load * 0.8)
            w_reel = 1.0 - float(inf_norm * 0.4)
            r_amp = self.coupled_resonance(w_fin, w_reel)
            resonance_series.append(r_amp)
            
            # --- 5. SİSTEMİK REZONANS (SRI) VE BİRLEŞİK KRİZ İNDEKSİ (CI) ---
            sri = float((a_load * bfi * max(0.10, max(dd_norm, bubble_norm))) ** (1.0 / 3.0))
            sri_series.append(sri)
            
            ci = float(np.clip(0.35 * a_load + 0.30 * bfi + 0.20 * max(dd_norm, bubble_norm) + 0.15 * inf_norm, 0.0, 1.0))
            ci_series.append(ci)
            
            # Faz Kilidi (Phase Lock) Kriz Alarmı
            is_alarm = (ci >= 0.48) or (sri >= 0.38 and a_load >= 0.52)
            alarm_series.append(1 if is_alarm else 0)

        df['Memory_M'] = memory_series
        df['A_load'] = a_load_series
        df['BFI'] = bfi_series
        df['Resonance_R'] = resonance_series
        df['SRI'] = sri_series
        df['CI'] = ci_series
        df['Alarm'] = alarm_series
        
        self.df = df
        return df

    def evaluate_performance(self):
        """13 Büyük Kriz için Erken Uyarı Menzilini ve Doğruluğunu Hesapla"""
        if 'Alarm' not in self.df.columns:
            self.run_walk_forward_amnesia_simulation()

        df = self.df
        crisis_eval = []
        
        for kc in self.known_crises:
            c_crash = pd.to_datetime(kc['crash'])
            search_start = c_crash - pd.DateOffset(months=24)
            
            slice_df = df[(df['Date'] >= search_start) & (df['Date'] <= c_crash)]
            alarm_rows = slice_df[slice_df['Alarm'] == 1]
            
            if len(alarm_rows) > 0:
                first_alarm_date = alarm_rows.iloc[0]['Date']
                lead_months = (c_crash.year - first_alarm_date.year) * 12 + (c_crash.month - first_alarm_date.month)
                detected = True
                peak_ci = float(slice_df['CI'].max())
                peak_aload = float(slice_df['A_load'].max())
            else:
                first_alarm_date = None
                lead_months = 0
                detected = False
                peak_ci = float(slice_df['CI'].max()) if len(slice_df) > 0 else 0.0
                peak_aload = float(slice_df['A_load'].max()) if len(slice_df) > 0 else 0.0
                
            crisis_eval.append({
                "name": kc['name'],
                "crash_date": kc['crash'],
                "first_alarm_date": first_alarm_date.strftime('%Y-%m') if first_alarm_date else "N/A",
                "lead_time_months": lead_months,
                "peak_CI": round(peak_ci, 3),
                "peak_A_load": round(peak_aload, 3),
                "detected": detected
            })
            
        self.results = crisis_eval
        return pd.DataFrame(crisis_eval)

if __name__ == "__main__":
    print("=" * 90)
    print("🚀 T2SAIM MASTER DZV KRİZ MOTORU BAŞLATILIYOR (E: SÜRÜCÜSÜ)")
    print("=" * 90)
    
    csv_file = r"E:\T2SAIM_NEXUS_MIRROR\Hariseldon\data\US_Historical_1900_2026\US_MASTER_MACRO_TIME_SERIES_1900_2026.csv"
    if not os.path.exists(csv_file):
        csv_file = r"B:\Hariseldon\data\US_Historical_1900_2026\US_MASTER_MACRO_TIME_SERIES_1900_2026.csv"
        
    engine = T2SAIMMasterCrisisEngine(csv_file)
    engine.load_data()
    engine.run_walk_forward_amnesia_simulation()
    eval_df = engine.evaluate_performance()
    
    print("\n" + "=" * 90)
    print("📊 126 YILLIK AMNESIA KRİZ ERKEN UYARI PERFORMANS TABLOSU")
    print("=" * 90)
    print(eval_df[["name", "crash_date", "first_alarm_date", "lead_time_months", "peak_CI", "detected"]].to_string(index=False))
    
    total = len(eval_df)
    detected = sum(eval_df['detected'])
    avg_lead = np.mean(eval_df[eval_df['detected']]['lead_time_months'])
    
    print("\n" + "=" * 60)
    print(f"🎯 Model Doğruluk Oranı: {detected}/{total} (%{detected/total*100.0:.1f})")
    print(f"⏱️ Ortalama Erken Uyarı Menzili: {avg_lead:.1f} AY ÖNCEDEN")
    print(f"🧠 Amnesia Hafıza Yarı Ömrü: {engine.t_half:.2f} Yıl")
    print("=" * 60)
