@echo off
set LOG=B:\Hariseldon\logs\daily_update.log
set PYTHON=python
echo. >> %LOG%
echo ================================================ >> %LOG%
echo %DATE% %TIME% - T2SAIM Gunluk Guncelleme >> %LOG%
echo ================================================ >> %LOG%

echo [1/4] USDTRY verisi cekiliyor... >> %LOG%
%PYTHON% B:\Hariseldon\fetch_latest_usdtry.py >> %LOG% 2>&1

echo [2/4] Kriz indeksi hesaplaniyor... >> %LOG%
%PYTHON% B:\Hariseldon\generate_crisis_data.py >> %LOG% 2>&1

echo [3/4] Canli piyasa verileri cekiliyor... >> %LOG%
%PYTHON% B:\Hariseldon\generate_market_data.py >> %LOG% 2>&1

echo [3.5/4] C5 Emtia Motoru kosturuluyor... >> %LOG%
%PYTHON% B:\T2SAIM_NEXUS\000_Shadow\00_Success\08_Utilities_and_Core_V17\global_btf_amnesia_engine.py >> %LOG% 2>&1

echo [3.8/4] T2SAIM Gunluk Portfoy Olusturuluyor... >> %LOG%
%PYTHON% B:\Hariseldon\generate_crypto_market_data.py >> %LOG% 2>&1
%PYTHON% B:\T2SAIM_NEXUS\000_Shadow\00_Success\05_Simons_Selective_V18\t2saim_daily_portfolio_generator.py >> %LOG% 2>&1
if %ERRORLEVEL% EQU 0 (
    copy /y B:\T2SAIM_NEXUS\000_Shadow\00_Success\t2saim_web_dashboard_data_V17.json B:\Hariseldon\t2saim_web_dashboard_data.json >> %LOG% 2>&1
    copy /y B:\T2SAIM_NEXUS\000_Shadow\00_Success\t2saim_model_selector_V17.json B:\Hariseldon\t2saim_model_selector.json >> %LOG% 2>&1
    copy /y B:\T2SAIM_NEXUS\000_Shadow\00_Success\t2saim_stock_selection_results_V17.json B:\Hariseldon\t2saim_stock_selection_results.json >> %LOG% 2>&1
)

echo [4/4] GitHub push... >> %LOG%
cd /d B:\Hariseldon
git add crisis_data.json market_data.json t2saim_web_dashboard_data.json t2saim_model_selector.json t2saim_stock_selection_results.json t2saim_dashboard.html t2saim_asset_details.html t2saim_crypto_dashboard.html spor_edge.html index.html tarkan_index.html .github/workflows/daily_update.yml >> %LOG% 2>&1
git commit -m "data: daily update with new models" >> %LOG% 2>&1
git push origin main >> %LOG% 2>&1
git push origin main:gh-pages --force >> %LOG% 2>&1

echo Bitis: %TIME% >> %LOG%
