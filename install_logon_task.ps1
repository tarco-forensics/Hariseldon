# =============================================================================
# T2SAIM WINDOWS ON-LOGON AUTO-UPDATE INSTALLER
# =============================================================================
$batPath = "B:\Hariseldon\daily_update.bat"

$action = New-ScheduledTaskAction -Execute $batPath
$triggerLogon = New-ScheduledTaskTrigger -AtLogOn
$triggerDaily1 = New-ScheduledTaskTrigger -Daily -At "09:00"
$triggerDaily2 = New-ScheduledTaskTrigger -Daily -At "18:00"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName "T2SAIM_Smart_AutoUpdate" -Action $action -Trigger @($triggerLogon, $triggerDaily1, $triggerDaily2) -Settings $settings -Force
Write-Host "✅ T2SAIM_Smart_AutoUpdate Task Successfully Registered!"
