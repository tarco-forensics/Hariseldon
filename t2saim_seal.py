# -*- coding: utf-8 -*-
"""
T2SAIM Kriptografik Mühürleme ve Versiyon Defteri Sistemi
============================================================
Bu araç, T2SAIM yerel kod tabanındaki kritik dosyaların (HTML, Python, JSON)
dijital parmak izlerini (SHA-256) hesaplar ve bunları zincirleme bir kriptografik
deftere (Blockchain mantığıyla) kaydeder.

Defter tamamen yerel (private) sürücüde saklanır ve asla harici sunuculara gitmez.
Her yeni blok, bir önceki bloğun hash değerini içerir; bu sayede geçmişe dönük
değişiklik yapılması matematiksel olarak engellenir ve tarihsel ispat oluşturulur.
"""

import os
import sys
import json
import hashlib
from datetime import datetime

# Hedef dosyalar listesi
TARGET_FILES = [
    "index.html",
    "tarkan_index.html",
    "kriz_raporu.html",
    "spor_edge.html",
    "generate_crisis_data.py",
    "fetch_latest_usdtry.py",
    "crisis_data.json",
    "market_data.json"
]

# Defter dosyasının saklanacağı yerel (private) yol
LEDGER_DIR = r"B:\T2SAIM_James_Projects\00_Success\WEBSITESI_KODLAR"
LEDGER_PATH = os.path.join(LEDGER_DIR, "t2saim_history_ledger.json")

def get_file_sha256(filepath):
    """Bir dosyanın SHA-256 hash değerini hesaplar."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def verify_ledger_integrity(ledger):
    """Defterin bütünlüğünü doğrular."""
    if not ledger:
        return True, "Defter henüz boş."
    
    for i in range(len(ledger)):
        block = ledger[i]
        
        # 1. Bloğun kendi hash bütünlüğünü doğrula
        block_copy = block.copy()
        if "block_hash" in block_copy:
            del block_copy["block_hash"]
            
        calculated_hash = hashlib.sha256(
            json.dumps(block_copy, sort_keys=True, ensure_ascii=False).encode('utf-8')
        ).hexdigest()
        
        if block.get("block_hash") != calculated_hash:
            return False, f"Blok {i} hash butunlugu bozulmus! Dosya degistirilmis."
            
        # 2. Zincir bağlantısını doğrula (Genesis blok hariç)
        if i > 0:
            prev_block = ledger[i-1]
            if block.get("previous_hash") != prev_block.get("block_hash"):
                return False, f"Blok {i} ile Blok {i-1} arasindaki zincir halkasi kopuk!"
                
    return True, "Tum defter butunlugu dogrulanmistir. Gecmis kayitlar orijinaldir."

def main():
    # Windows konsolunda Türkçe karakter hatası almamak için ASCII-safe mesajlar kullanıyoruz.
    print("=" * 60)
    print("      T2SAIM KRIPTOGRAFIK MUHURLEME VE TARIHSEL ISPAT SISTEMI")
    print("=" * 60)
    
    # Hedef klasörün varlığını kontrol et
    if not os.path.exists(LEDGER_DIR):
        try:
            os.makedirs(LEDGER_DIR)
        except Exception as e:
            print(f"[-] Hata: Yedekleme dizini olusturulamadi: {e}")
            sys.exit(1)

    # 1. Mevcut Defteri Yükle ve Doğrula
    ledger = []
    if os.path.exists(LEDGER_PATH):
        try:
            with open(LEDGER_PATH, "r", encoding="utf-8") as f:
                ledger = json.load(f)
            
            # Defterin bütünlüğünü kontrol et
            is_valid, msg = verify_ledger_integrity(ledger)
            if not is_valid:
                print(f"[!] KRITIK UYARI: {msg}")
                choice = input("[?] Butunluk hatasina ragmen devam edilsin mi? (e/h): ").lower()
                if choice != 'e':
                    sys.exit(1)
            else:
                print(f"[+] Mevcut Defter Yuklendi. Butunluk Durumu: {msg}")
                print(f"[+] Toplam Kayitli Blok Sayisi: {len(ledger)}")
        except Exception as e:
            print(f"[-] Defter okuma hatasi: {e}")
            sys.exit(1)
    else:
        print("[+] Yeni muhurleme defteri olusturuluyor (Genesis Blok kurulacak).")

    # 2. Kullanıcıdan Değişiklik Mesajı Al
    change_msg = ""
    if len(sys.argv) > 1:
        change_msg = " ".join(sys.argv[1:])
    else:
        change_msg = input("\n[?] Yapilan degisikliklerin ozetini yazin: ").strip()
        while not change_msg:
            change_msg = input("[!] Lutfen gecerli bir aciklama yazin: ").strip()

    # 3. Dosyaların Güncel Hash'lerini Topla
    current_hashes = {}
    print("\nDosyalar taraniyor ve dijital parmak izleri cikariliyor:")
    for filename in TARGET_FILES:
        filepath = filename
        file_hash = get_file_sha256(filepath)
        if file_hash:
            current_hashes[filename] = file_hash
            print(f"  [+] {filename:<25} : {file_hash[:16]}...{file_hash[-8:]}")
        else:
            print(f"  [-] {filename:<25} : Bulunamadi (Atlandi)")

    if not current_hashes:
        print("[-] Hata: Muhurlenecek hicbir dosya bulunamadi!")
        sys.exit(1)

    # 4. Yeni Blok Oluştur (Chaining)
    block_index = len(ledger)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if block_index == 0:
        prev_hash = "0" * 64  # Genesis blok
    else:
        prev_hash = ledger[-1]["block_hash"]

    new_block = {
        "index": block_index,
        "timestamp": timestamp,
        "description": change_msg,
        "file_hashes": current_hashes,
        "previous_hash": prev_hash
    }

    # Bloğun SHA-256 Hash'ini hesapla
    block_hash = hashlib.sha256(
        json.dumps(new_block, sort_keys=True, ensure_ascii=False).encode('utf-8')
    ).hexdigest()
    
    new_block["block_hash"] = block_hash

    # 5. Defteri Güncelle ve Diske Yaz
    ledger.append(new_block)
    
    try:
        with open(LEDGER_PATH, "w", encoding="utf-8") as f:
            json.dump(ledger, f, indent=4, ensure_ascii=False)
        
        print("\n" + "=" * 60)
        print("                MUHURLEME ISLEMI BASARIYLA TAMAMLANDI")
        print("=" * 60)
        print(f" Blok Indeksi   : {block_index}")
        print(f" Tarih / Saat   : {timestamp}")
        print(f" Aciklama       : {change_msg}")
        print(f" Blok Hash'i    : {block_hash}")
        print(f" Onceki Hash    : {prev_hash[:16]}...")
        print(f" Kayit Adresi   : {LEDGER_PATH}")
        print("-" * 60)
        print("[*] Dijital muhur basildi. Defter butunlugu korunuyor.")
        print("=" * 60)
        
    except Exception as e:
        print(f"[-] Deftere yazma hatasi gerceklesti: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
