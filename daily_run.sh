#!/bin/bash
# HARISELDON — Günlük T2SAIM Motor Koşusu
# Kaptan Tarco | SPOCK | Amnesia λ=0.15 | Zero Future Leakage
# Takvim: Çift gün BIST, Tek gün Global, Her gün Amigdala

HARISELDON="/b/Hariseldon"
LOG="$HARISELDON/logs/daily_$(date +%Y%m%d).log"
mkdir -p "$HARISELDON/logs"

GUN=$(date +%d)
GUN_MOD=$((10#$GUN % 2))

echo "========================================" >> "$LOG"
echo "HARISELDON GUNLUK KOSU — $(date)" >> "$LOG"
echo "Gun mod: $GUN_MOD (cift=0 BIST, tek=1 Global)" >> "$LOG"
echo "========================================" >> "$LOG"

cd /b/T2SAIM_Spock_Hermes/00_Success

# Her gun: TR Telegram Amigdala
echo "[1] TR Telegram Amigdala..." >> "$LOG"
python turkiye_amigdala_dedektoru.py 2>&1 >> "$LOG"
echo "  => Amigdala tamamlandi" >> "$LOG"

# Cift gun (0): BIST, Tek gun (1): Global
if [ $GUN_MOD -eq 0 ]; then
    echo "[3] BIST-100 MFDFA Motoru (Hurst=0.52)..."
    python btf_run_max_profit_html_mfdfa.py 2>&1 >> "$LOG"
    echo "  => BIST tamamlandi" >> "$LOG"
else
    echo "[3] Global MFDFA Motoru (optimize Hurst)..."
    python global_btf_amnesia_engine.py 2>&1 >> "$LOG"
    echo "  => Global tamamlandi" >> "$LOG"
fi

# Sonuclari Hariseldon'a kopyala
echo "[KOPYALA] Sonuclar..." >> "$LOG"
cp "/b/T2SAIM_James_Projects/07-Sonuclar/BIST100_BTF_Amnesia_Max_Profit_Dashboard.html" "$HARISELDON/dashboards/BIST100_Amnesia_Dashboard.html"
cp "/b/T2SAIM_James_Projects/07-Sonuclar/GLOBAL_Amnesia_Max_Profit_Dashboard.html" "$HARISELDON/dashboards/"
cp "/b/T2SAIM_James_Projects/07-Sonuclar/SAYFA2_Kuresel_Karsilastirma_Dashboard.html" "$HARISELDON/dashboards/"
cp "/b/T2SAIM_James_Projects/07-Sonuclar/SAYFA3_Kripto_Amnesia_TR_Amigdala_Dashboard.html" "$HARISELDON/dashboards/"
cp /b/T2SAIM_James_Projects/07-Sonuclar/turkiye_amigdala_*.json "$HARISELDON/amigdala/"

# Git commit ve push
echo "[GIT] Commit ve push..." >> "$LOG"
cd "$HARISELDON"
git add -A
git commit -m "gunluk kosu $(date +%Y-%m-%d)" >> "$LOG" 2>&1
git push origin main >> "$LOG" 2>&1

echo "========================================" >> "$LOG"
echo "KOSU TAMAMLANDI — $(date)" >> "$LOG"
echo "========================================" >> "$LOG"

cat "$LOG"
