import os
import shutil
import json

print("=" * 90)
print("🚀 T2SAIM AUTO VAULT SYNCHRONIZATION AND BACKUP ENGINE")
print("=" * 90)

# Source directories in B:\Hariseldon
src_dirs = [
    r"B:\Hariseldon\Knowledge_Base",
    r"B:\Hariseldon\data\US_Historical_1900_2026"
]

src_files = [
    r"B:\Hariseldon\crisis_data.json",
    r"B:\Hariseldon\back_to_the_future_amnesia_test.py",
    r"B:\Hariseldon\us_crisis_historical_backtest.py",
    r"B:\Hariseldon\build_us_master_dataset.py",
    r"B:\Hariseldon\data_fetch_us_1900_2026.py",
    r"B:\Hariseldon\tarkan_index.html"
]

# Destination Hubs across the system
target_hubs = [
    r"E:\010101_HERMES_KARARGAHLAR\Hermes_Karargah\Knowledge_Base\T2SAIM_Crisis_Vault",
    r"E:\AI_RAG\Knowledge_Base\T2SAIM_Crisis_Vault",
    r"B:\T2SAIM_NEXUS\Knowledge_Base\T2SAIM_Crisis_Vault",
    r"E:\T2SAIM_NEXUS_MIRROR\0A0A0_ENGINE_ROOM\LİBRARY_T2SAIM\50_Works\T2SAIM_Total_Vault\E_Tarco_Main\T2SAIM_US_Vault"
]

sync_stats = {}

for hub in target_hubs:
    print(f"\n📂 Syncing to Target Hub: {hub}")
    os.makedirs(hub, exist_ok=True)
    count = 0
    size_bytes = 0
    
    # 1. Sync Knowledge Base directory
    kb_src = r"B:\Hariseldon\Knowledge_Base"
    kb_dst = os.path.join(hub, "Knowledge_Base")
    if os.path.exists(kb_src):
        for root, dirs, files in os.walk(kb_src):
            rel = os.path.relpath(root, kb_src)
            dest_dir = os.path.join(kb_dst, rel)
            os.makedirs(dest_dir, exist_ok=True)
            for f in files:
                s_file = os.path.join(root, f)
                d_file = os.path.join(dest_dir, f)
                shutil.copy2(s_file, d_file)
                count += 1
                size_bytes += os.path.getsize(d_file)
                
    # 2. Sync US Historical Datasets directory
    data_src = r"B:\Hariseldon\data\US_Historical_1900_2026"
    data_dst = os.path.join(hub, "US_Historical_1900_2026")
    if os.path.exists(data_src):
        os.makedirs(data_dst, exist_ok=True)
        for f in os.listdir(data_src):
            s_file = os.path.join(data_src, f)
            d_file = os.path.join(data_dst, f)
            if os.path.isfile(s_file):
                shutil.copy2(s_file, d_file)
                count += 1
                size_bytes += os.path.getsize(d_file)
                
    # 3. Sync Core Scripts & Engines
    code_dst = os.path.join(hub, "Engines")
    os.makedirs(code_dst, exist_ok=True)
    for sf in src_files:
        if os.path.exists(sf):
            fname = os.path.basename(sf)
            d_file = os.path.join(code_dst, fname)
            shutil.copy2(sf, d_file)
            count += 1
            size_bytes += os.path.getsize(d_file)
            
    sync_stats[hub] = {"files": count, "size_mb": size_bytes / (1024 * 1024)}
    print(f"  ✅ Replicated {count} files ({size_bytes / (1024 * 1024):.2f} MB)")

print("\n" + "=" * 90)
print("📊 AUTO VAULT SYNCHRONIZATION SUMMARY:")
for hub, stat in sync_stats.items():
    print(f"  * {hub} -> {stat['files']} files ({stat['size_mb']:.2f} MB)")
print("=" * 90)
