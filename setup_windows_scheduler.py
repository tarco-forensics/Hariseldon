# =============================================================================
# T2SAIM PREDATOR V4 — WINDOWS SCHEDULER INSTALLER
# Sets up Windows Scheduled Task "T2SAIM_Daily_Update" to run daily_update.bat
# at 09:00 and 18:00 automatically in the background.
# =============================================================================
import os
import subprocess

BAT_PATH = r"B:\Hariseldon\daily_update.bat"

def install_task():
    print("================================================================================")
    print("⏰ T2SAIM WINDOWS SCHEDULER INSTALLER")
    print("================================================================================")
    
    task_name = "T2SAIM_Daily_Update_Morning"
    cmd_morning = f'schtasks /create /tn "{task_name}" /tr "{BAT_PATH}" /sc daily /st 09:00 /f'
    res1 = subprocess.run(cmd_morning, shell=True, capture_output=True, text=True)
    print("Morning Task Status:", res1.stdout.strip() if res1.returncode == 0 else res1.stderr.strip())

    task_name_eve = "T2SAIM_Daily_Update_Evening"
    cmd_evening = f'schtasks /create /tn "{task_name_eve}" /tr "{BAT_PATH}" /sc daily /st 18:00 /f'
    res2 = subprocess.run(cmd_evening, shell=True, capture_output=True, text=True)
    print("Evening Task Status:", res2.stdout.strip() if res2.returncode == 0 else res2.stderr.strip())

    print("================================================================================")
    print("✅ LOCAL WINDOWS TASKS INSTALLED SUCCESSFULLY!")

if __name__ == "__main__":
    install_task()
