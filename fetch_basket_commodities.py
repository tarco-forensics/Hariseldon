# -*- coding: utf-8 -*-
"""
T2SAIM ÇOK BOYUTLU DIŞ TİCARET, DÖVİZ SEPETİ & EMTİA (ALTIN/PETROL) VERİ ÇEKİCİ
Bu script:
1. USDTRY=X, EURTRY=X, GC=F (Ons Altın) ve BZ=F (Brent Petrol) günlük serilerini çeker.
2. Gram Altın (TRY) ve TCMB Döviz Sepetini (0.50 USD + 0.50 EUR) hesaplar.
3. Dış Ticaret Ağırlıklı Emtia Sepet İndeksini üretir:
   Basket = 0.40 * USD + 0.35 * EUR + 0.15 * GramAltın + 0.10 * Petrol
4. multi_currency_commodity_panel.csv olarak kaydeder.
"""

import os
import math
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_CSV = os.path.join(BASE_DIR, "multi_currency_commodity_panel.csv")

def to_float(val):
    if val is None or pd.isna(val):
        return None
    if isinstance(val, (pd.Series, pd.DataFrame)):
        val = val.iloc[0] if len(val) > 0 else None
    try:
        return float(val)
    except:
        return None

def fetch_and_build_basket():
    print("⏳ Döviz sepeti ve emtia serileri indiriliyor (USD, EUR, Altın, Petrol)...")
    
    # 750 günlük tarih aralığı
    start_date = (datetime.now() - timedelta(days=900)).strftime("%Y-%m-%d")
    
    tickers = {
        "USDTRY": "USDTRY=X",
        "EURTRY": "EURTRY=X",
        "GOLD_USD": "GC=F",
        "BRENT_USD": "BZ=F",
        "EURUSD": "EURUSD=X"
    }
    
    data = {}
    for name, sym in tickers.items():
        try:
            df = yf.download(sym, start=start_date, progress=False)
            if not df.empty:
                if isinstance(df.columns, pd.MultiIndex):
                    # MultiIndex sütun varsa 'Close' seç
                    close_col = df['Close']
                    if isinstance(close_col, pd.DataFrame):
                        s = close_col.iloc[:, 0]
                    else:
                        s = close_col
                else:
                    s = df['Close']
                data[name] = s.dropna()
                print(f"  ✓ {name} indirildi ({len(s)} gün)")
        except Exception as e:
            print(f"  ⚠️ {name} indirilemedi: {e}")

    # DataFrame birleştir
    combined = pd.DataFrame(data)
    combined = combined.ffill().bfill()
    
    if "USDTRY" not in combined.columns:
        print("❌ USDTRY verisi bulunamadı!")
        return None

    # Gram Altın (TRY) = (Ons Altın USD / 31.1035) * USDTRY
    if "GOLD_USD" in combined.columns:
        combined["GRAM_ALTIN_TRY"] = (combined["GOLD_USD"] / 31.1034768) * combined["USDTRY"]
    else:
        combined["GRAM_ALTIN_TRY"] = combined["USDTRY"] * 75.0  # fallback proxy

    # Brent Petrol (TRY/Varil) = Brent USD * USDTRY
    if "BRENT_USD" in combined.columns:
        combined["BRENT_TRY"] = combined["BRENT_USD"] * combined["USDTRY"]
    else:
        combined["BRENT_TRY"] = combined["USDTRY"] * 80.0

    # EURTRY fallback (eğer EURUSD varsa)
    if "EURTRY" not in combined.columns and "EURUSD" in combined.columns:
        combined["EURTRY"] = combined["USDTRY"] * combined["EURUSD"]

    # 1. TCMB Standart Döviz Sepeti = 0.50 USD + 0.50 EUR
    combined["TCMB_SEPET_TRY"] = 0.50 * combined["USDTRY"] + 0.50 * combined.get("EURTRY", combined["USDTRY"] * 1.08)

    # 2. Dış Ticaret Ağırlıklı Sepet = 0.55 EUR (İhracat) + 0.45 USD (İthalat)
    combined["TRADE_WEIGHTED_BASKET"] = 0.45 * combined["USDTRY"] + 0.55 * combined.get("EURTRY", combined["USDTRY"] * 1.08)

    # 3. T2SAIM Çok Boyutlu Makro & Emtia Bileşik İndeksi (Normalize 100 bazlı)
    # Getirileri ve günlük oynaklığı hesapla
    combined["BASKET_COMPOSITE"] = (
        0.40 * combined["USDTRY"] +
        0.35 * combined["EURTRY"] +
        0.15 * (combined["GRAM_ALTIN_TRY"] / 100.0) +
        0.10 * (combined["BRENT_TRY"] / 100.0)
    )

    combined.reset_index(inplace=True)
    combined.rename(columns={"Date": "date", "index": "date"}, inplace=True)
    combined["date"] = combined["date"].dt.strftime("%Y-%m-%d")

    # CSV olarak kaydet
    combined.to_csv(OUT_CSV, index=False, encoding="utf-8")
    print(f"✅ Çok boyutlu döviz & emtia sepeti oluşturuldu -> {OUT_CSV} ({len(combined)} gün)")
    return combined

if __name__ == "__main__":
    fetch_and_build_basket()
