# =============================================================================
# T2SAIM Hariseldon Automatic Scheduled Tasks Generator
# Trigger 1: PC Logged on + 2 Hours Delay
# Trigger 2: Daily at 18:00 (6:00 PM)
# =============================================================================
$action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument '/c B:\Hariseldon\daily_update.bat'

# Trigger 1: On User Logon with 2 hours delay (PT2H)
$trigger1 = New-ScheduledTaskTrigger -AtLogon
$trigger1.Delay = 'PT2H'

# Trigger 2: Daily at 18:00 (6:00 PM)
$trigger2 = New-ScheduledTaskTrigger -Daily -At '18:00'

$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -RunOnlyIfNetworkAvailable -WakeToRun

Register-ScheduledTask `
    -TaskName 'T2SAIM_Hariseldon_AutoUpdate' `
    -Action $action `
    -Trigger @($trigger1, $trigger2) `
    -Settings $settings `
    -Description 'T2SAIM Hariseldon Otomatik Gunluk Veri Guncelleme: Bilgisayar acildiktan 2 saat sonra ve her gun 18:00' `
    -Force

Write-Host "================================================================================"
Write-Host "✅ T2SAIM_Hariseldon_AutoUpdate ZAMANLANMIŞ GÖREVLERİ BAŞARIYLA TESCİL EDİLDİ!"
Write-Host "================================================================================"
Get-ScheduledTask -TaskName 'T2SAIM_Hariseldon_AutoUpdate' | Format-List TaskName, State
