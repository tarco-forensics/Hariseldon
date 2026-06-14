#!/bin/bash
# HARISELDON — Günlük T2SAIM Motor Koşusu
# Tarih: $(date +%Y-%m-%d)
# Amnesia λ=0.15 | Zero Future Leakage

HARISELDON="/c/Users/tarka/Hariseldon"
LOG="$HARISELDON/logs/daily_$(date +%Y%m%d).log"
mkdir -p "$HARISELDON/logs"

echo "========================================" >> "$LOG"
echo "HARISELDON GUNLUK KOSU — $(date)" >> "$LOG"
echo "========================================" >> "$LOG"

# 1. BIST MFDFA Motoru
echo "[1/3] BIST-100 MFDFA Motoru..." >> "$LOG"
cd "/b/T2SAIM_Spock_Hermes/00_Success"
python btf_run_max_profit_html_mfdfa.py 2>&1 >> "$LOG"
echo "  => BIST tamamlandi" >> "$LOG"

# 2. Global MFDFA Motoru
echo "[2/3] Global MFDFA Motoru..." >> "$LOG"
python global_btf_amnesia_engine.py 2>&1 >> "$LOG"
echo "  => Global tamamlandi" >> "$LOG"

# 3. TR Telegram Amigdala
echo "[3/3] TR Telegram Amigdala..." >> "$LOG"
python turkiye_amigdala_dedektoru.py 2>&1 >> "$LOG"
echo "  => Amigdala tamamlandi" >> "$LOG"

# 4. Sonuçları Hariseldon'a kopyala
echo "[KOPYALA] Sonuclar Hariseldon'a..." >> "$LOG"
cp "/b/T2SAIM_James_Projects/07-Sonuclar/BIST100_BTF_Amnesia_Max_Profit_Dashboard.html" "$HARISELDON/dashboards/BIST100_Amnesia_Dashboard.html"
cp "/b/T2SAIM_James_Projects/07-Sonuclar/GLOBAL_Amnesia_Max_Profit_Dashboard.html" "$HARISELDON/dashboards/"
cp "/b/T2SAIM_James_Projects/07-Sonuclar/SAYFA2_Kuresel_Karsilastirma_Dashboard.html" "$HARISELDON/dashboards/"
cp "/b/T2SAIM_James_Projects/07-Sonuclar/SAYFA3_Kripto_Amnesia_TR_Amigdala_Dashboard.html" "$HARISELDON/dashboards/"
cp "/b/T2SAIM_James_Projects/07-Sonuclar/turkiye_amigdala_"*.json "$HARISELDON/amigdala/"

# 5. Git commit ve push
echo "[GIT] Commit ve push..." >> "$LOG"
cd "$HARISELDON"
git add -A
git commit -m "gunluk kosu $(date +%Y-%m-%d)" >> "$LOG" 2>&1
# git push origin main >> "$LOG" 2>&1  # GitHub token gerekiyor

echo "========================================" >> "$LOG"
echo "KOSU TAMAMLANDI — $(date)" >> "$LOG"
echo "========================================" >> "$LOG"

cat "$LOG"
