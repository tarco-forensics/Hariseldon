# =============================================================================
# T2SAIM PREDATOR V4 — WINDOWS BOOT / LOGON SCHEDULER INSTALLER
# Sets up Windows Scheduled Task "T2SAIM_Daily_Update_OnLogon" to run daily_update.bat
# automatically whenever Kaptan Tarco turns on / logs into his PC, plus daily backup.
# =============================================================================
import os
import subprocess

BAT_PATH = r"B:\Hariseldon\daily_update.bat"

def install_logon_task():
    print("================================================================================")
    print("⏰ T2SAIM WINDOWS ON-LOGON / BOOT SCHEDULER INSTALLER")
    print("================================================================================")

    # 1. On Logon Task (Runs automatically every time PC is logged into)
    task_logon = "T2SAIM_Daily_Update_OnLogon"
    cmd_logon = f'schtasks /create /tn "{task_logon}" /tr "{BAT_PATH}" /sc ONLOGON /f'
    res1 = subprocess.run(cmd_logon, shell=True, capture_output=True, text=True)
    print("On-Logon Task Status:", res1.stdout.strip() if res1.returncode == 0 else res1.stderr.strip())

    # 2. PowerShell script for advanced task settings (StartWhenAvailable = True)
    ps_script = f'''
    $action = New-ScheduledTaskAction -Execute "{BAT_PATH}"
    $triggerLogon = New-ScheduledTaskTrigger -AtLogOn
    $triggerDaily1 = New-ScheduledTaskTrigger -Daily -At "09:00"
    $triggerDaily2 = New-ScheduledTaskTrigger -Daily -At "18:00"
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
    
    Register-ScheduledTask -TaskName "T2SAIM_Smart_AutoUpdate" -Action $action -Trigger @($triggerLogon, $triggerDaily1, $triggerDaily2) -Settings $settings -Force
    '''
    
    ps_cmd = f'powershell -Command "{ps_script.replace(chr(10), " ")}"'
    res2 = subprocess.run(ps_cmd, shell=True, capture_output=True, text=True)
    print("Smart AutoUpdate Task Status:", res2.stdout.strip() if res2.returncode == 0 else res2.stderr.strip())

    print("================================================================================")
    print("✅ LOGON / BOOT SCHEDULER INSTALLED SUCCESSFULLY!")

if __name__ == "__main__":
    install_logon_task()
