@echo off
:: T2SAIM Günlük Kriz Verisi Güncelleme
:: Her sabah 08:00 otomatik çalışır

set LOG=B:\Hariseldon\logs\daily_update.log
set PYTHON=python

echo. >> %LOG%
echo ================================================ >> %LOG%
echo %DATE% %TIME% — T2SAIM Gunluk Guncelleme >> %LOG%
echo ================================================ >> %LOG%

:: 1. Eksik USDTRY günlerini çek
echo [1/3] USDTRY verisi cekiliyor... >> %LOG%
%PYTHON% B:\Hariseldon\fetch_latest_usdtry.py >> %LOG% 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo HATA: USDTRY verisi cekme basarisiz >> %LOG%
    goto END
)

:: 2. Kriz indeksini yeniden hesapla
echo [2/3] Kriz indeksi hesaplaniyor... >> %LOG%
%PYTHON% B:\Hariseldon\generate_crisis_data.py >> %LOG% 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo HATA: Kriz indeksi hesaplama basarisiz >> %LOG%
    goto END
)

:: 3. GitHub'a push et
echo [3/3] GitHub push... >> %LOG%
cd /d B:\Hariseldon
git add crisis_data.json >> %LOG% 2>&1
git commit -m "data: daily update %DATE%" >> %LOG% 2>&1
git push origin main >> %LOG% 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo UYARI: Git push basarisiz (ag sorunu olabilir) >> %LOG%
) else (
    echo BASARILI: Guncelleme tamamlandi >> %LOG%
)

:END
echo Bitis: %TIME% >> %LOG%
