$action   = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument '/c B:\Hariseldon\daily_update.bat'
$trigger  = New-ScheduledTaskTrigger -Daily -At '08:00AM'
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -RunOnlyIfNetworkAvailable -WakeToRun
Register-ScheduledTask `
    -TaskName    'T2SAIM_DailyUpdate' `
    -Action      $action `
    -Trigger     $trigger `
    -Settings    $settings `
    -Description 'T2SAIM Gunluk Kriz Verisi: USDTRY cek, kriz indeksi hesapla, GitHub push' `
    -RunLevel    Highest `
    -Force
Write-Host "BASARILI: T2SAIM_DailyUpdate gorevi olusturuldu"
Get-ScheduledTask -TaskName 'T2SAIM_DailyUpdate' | Select-Object TaskName, State
