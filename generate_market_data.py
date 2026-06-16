"""
T2SAIM Market Data Generator
Günlük piyasa özetini yFinance'dan çeker, market_data.json üretir.
index.html'in günlük tablosu ve live chart bu JSON'ı kullanır.
"""
import json, math, sys
from datetime import datetime, timedelta

# Ensure UTF-8 output encoding
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

try:
    import yfinance as yf
    import numpy as np
except ImportError:
    print("pip install yfinance numpy")
    sys.exit(1)

OUT_FILE = r"B:\Hariseldon\market_data.json"

MARKETS = [
    {"key": "bist",   "flag": "TR", "name": "BIST-100",     "ticker": "XU100.IS",   "bench": "XU100.IS",  "hurst": 0.52, "roi": 59.84, "alpha": 68.20, "sharpe": 1.99, "stop": 8,   "trades": 42,  "dashboard": "dashboards/BIST100_Amnesia_Dashboard.html", "horizon": "30 Gün (D+30)"},
    {"key": "sp500",  "flag": "US", "name": "S&P 500",      "ticker": "^GSPC",      "bench": "^GSPC",     "hurst": 0.46, "roi": 80.02, "alpha": 58.53, "sharpe": 2.41, "stop": 3,   "trades": 35,  "dashboard": "dashboards/GLOBAL_Amnesia_Max_Profit_Dashboard.html", "horizon": "30 Gün (D+30)"},
    {"key": "ftse",   "flag": "GB", "name": "FTSE 100",     "ticker": "^FTSE",      "bench": "^FTSE",     "hurst": 0.57, "roi": 72.48, "alpha": 48.29, "sharpe": 1.52, "stop": 12,  "trades": 28,  "dashboard": "dashboards/GLOBAL_Amnesia_Max_Profit_Dashboard.html", "horizon": "30 Gün (D+30)"},
    {"key": "stoxx",  "flag": "EU", "name": "Euro Stoxx 50","ticker": "^STOXX50E",  "bench": "^STOXX50E", "hurst": 0.60, "roi": 40.58, "alpha": 23.03, "sharpe": 0.89, "stop": 47,  "trades": 52,  "dashboard": "dashboards/GLOBAL_Amnesia_Max_Profit_Dashboard.html", "horizon": "30 Gün (D+30)"},
    {"key": "nikkei", "flag": "JP", "name": "Nikkei 225",   "ticker": "^N225",      "bench": "^N225",     "hurst": 0.55, "roi": 72.31, "alpha": 15.04, "sharpe": 2.18, "stop": 2,   "trades": 18,  "dashboard": "dashboards/GLOBAL_Amnesia_Max_Profit_Dashboard.html", "horizon": "30 Gün (D+30)"},
    {"key": "hsi",    "flag": "HK", "name": "Hang Seng",    "ticker": "^HSI",       "bench": "^HSI",      "hurst": 0.52, "roi": 49.18, "alpha": 14.53, "sharpe": 1.21, "stop": 18,  "trades": 44,  "dashboard": "dashboards/GLOBAL_Amnesia_Max_Profit_Dashboard.html", "horizon": "30 Gün (D+30)"},
    {"key": "btc",    "flag": "COIN","name": "Kripto (BTC)", "ticker": "BTC-USD",    "bench": "BTC-USD",   "hurst": 0.60, "roi": 297.02,"alpha": 174.22,"sharpe": 3.12, "stop": 100, "trades": 68,  "dashboard": "dashboards/SAYFA3_Kripto_Amnesia_TR_Amigdala_Dashboard.html", "horizon": "30 Gün (D+30)"},
    {"key": "emtia",  "flag": "MTL", "name": "Değerli Metaller", "ticker": "GC=F",   "bench": "GC=F",      "hurst": 0.60, "roi": 85.87, "alpha": 16.95, "sharpe": 0.84, "stop": 5,   "trades": 24,  "dashboard": "dashboards/commodity_dashboard.html", "horizon": "5 Gün (D+5)"},
]

PORTFOLIO_BASE = 10000  # her piyasa için başlangıç sermayesi

def hurst_signal(h):
    """Hurst exponent → strateji tipi"""
    if h > 0.55:   return "Trend"
    elif h < 0.45: return "Mean-Rev"
    else:          return "Neutral"

def fetch_market(m):
    try:
        df = yf.download(m["ticker"], period="5d", interval="1d",
                         auto_adjust=True, progress=False)
        if df.empty or len(df) < 2:
            return None
        # Son iki kapanış
        closes = df["Close"].dropna()
        if hasattr(closes, 'iloc'):
            prev  = float(closes.iloc[-2])
            last  = float(closes.iloc[-1])
        else:
            return None
        daily_pct = (last - prev) / prev * 100
        last_date = df.index[-1].strftime("%Y-%m-%d")
        return {
            "close_prev": round(prev, 2),
            "close_last": round(last, 2),
            "daily_pct":  round(daily_pct, 2),
            "last_date":  last_date,
            "ok": True
        }
    except Exception as e:
        print(f"  HATA {m['ticker']}: {e}")
        return None

def main():
    today = datetime.now()
    yesterday = (today - timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"T2SAIM Market Data Generator — {today.strftime('%Y-%m-%d %H:%M')}")

    results = []
    total_portfolio = 0
    total_profit    = 0
    total_trades    = 0

    for m in MARKETS:
        print(f"  Cekiliyor: {m['name']} ({m['ticker']})...")
        live = fetch_market(m)

        portfolio_value = round(PORTFOLIO_BASE * (1 + m["roi"] / 100), 2)
        total_portfolio += portfolio_value
        total_profit    += portfolio_value - PORTFOLIO_BASE
        total_trades    += m["trades"]

        entry = {
            "key":       m["key"],
            "flag":      m["flag"],
            "name":      m["name"],
            "ticker":    m["ticker"],
            "hurst":     m["hurst"],
            "signal":    hurst_signal(m["hurst"]),
            "roi":       m["roi"],
            "alpha":     m["alpha"],
            "sharpe":    m["sharpe"],
            "stop":      m["stop"],
            "trades":    m["trades"],
            "dashboard": m["dashboard"],
            "horizon":   m.get("horizon", "30 Gün (D+30)"),
            "portfolio": portfolio_value,
            "profit":    round(portfolio_value - PORTFOLIO_BASE, 2),
            # Canlı veri
            "live_ok":    live is not None and live.get("ok", False),
            "close_prev": live["close_prev"] if live else None,
            "close_last": live["close_last"] if live else None,
            "daily_pct":  live["daily_pct"]  if live else None,
            "last_date":  live["last_date"]  if live else yesterday,
        }
        results.append(entry)
        if live:
            print(f"    OK: {live['last_date']} close={live['close_last']} ({live['daily_pct']:+.2f}%)")
        else:
            print(f"    Veri alinamadi, backtest degerleri kullaniliyor")

    summary = {
        "generated":       today.strftime("%Y-%m-%d %H:%M"),
        "yesterday":       yesterday,
        "total_portfolio": round(total_portfolio, 2),
        "total_profit":    round(total_profit, 2),
        "total_roi_pct":   round(total_profit / (len(MARKETS) * PORTFOLIO_BASE) * 100, 2),
        "markets_count":   len(MARKETS),
        "live_count":      sum(1 for r in results if r["live_ok"]),
        "total_roi_sum":   round(sum(m["roi"] for m in MARKETS), 2),
        "total_alpha_sum": round(sum(m["alpha"] for m in MARKETS), 2),
        "total_trades":    total_trades,
    }

    output = {"summary": summary, "markets": results}
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nOK: {len(results)} piyasa -> {OUT_FILE}")
    print(f"   Portfoy: ${total_portfolio:,.0f} | Kar: ${total_profit:,.0f} | Canli: {summary['live_count']}/{len(MARKETS)}")

if __name__ == "__main__":
    main()
