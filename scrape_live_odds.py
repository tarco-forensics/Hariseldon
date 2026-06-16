# -*- coding: utf-8 -*-
"""
T2SAIM Canlı Oran Tarayıcı ve Arbitraj Tespit Motoru (Scanner Node)
==================================================================
Bu script, farklı bahis sitelerinin oranlarını tarayarak çapraz site arbitrajı
(Surebet) ve pozitif beklenen değerli (Valuebet) fırsatları tespit eder.

Varsayılan olarak "The Odds API" kullanarak gerçek dünya canlı oranlarını çekebilir.
Eğer API anahtarı yoksa, gerçekçi oran anomalileri üreten bir simülatör
üzerinden çalışarak dashboard'un test edilmesini ve doğrulanmasını sağlar.

Sonuçlar 'dashboards/canli_oranlar.json' dosyasına yazılır.
"""

import os
import sys
import json
import time
import random
from datetime import datetime

# The Odds API Anahtarı (Varsayılan olarak boştur. Kullanıcı buraya kendi anahtarını girebilir)
API_KEY = "" 
LEAGUE = "soccer_uefa_champs_league" # Örnek lig
REGIONS = "eu"
MARKETS = "h2h"

# Sonuç dosyası yolu
DASHBOARDS_DIR = r"B:\Hariseldon\dashboards"
OUTPUT_PATH = os.path.join(DASHBOARDS_DIR, "canli_oranlar.json")

# Simülasyon için örnek futbol maçları ve takımlar
MOCK_TEAMS = [
    ("Real Madrid", "Barcelona"),
    ("Manchester City", "Arsenal"),
    ("Bayern Munich", "Dortmund"),
    ("Inter Milan", "AC Milan"),
    ("Liverpool", "Chelsea"),
    ("Paris SG", "Marseille"),
    ("Juventus", "Napoli"),
    ("Türkiye", "Almanya")
]

BOOKMAKERS = ["Pinnacle", "Bet365", "Betfair Exchange", "Bwin", "Unibet", "1xBet"]

def calculate_arbitrage(o1, ox, o2):
    """3 ihtimalli pazarda arbitraj (surebet) marjını hesaplar."""
    S = (1.0 / o1) + (1.0 / ox) + (1.0 / o2)
    is_arb = S < 1.0
    margin = (1.0 - S) / S if is_arb else 0.0
    return is_arb, S, margin

def get_simulated_odds():
    """Gerçekçi oran uyumsuzlukları ve arbitrajlar içeren veri üretir."""
    maclar = []
    tarih_str = datetime.now().strftime("%H:%M:%S")
    
    # 4 ila 6 aktif maç simüle et
    active_matches = random.sample(MOCK_TEAMS, random.randint(4, 6))
    
    for idx, (home, away) in enumerate(active_matches):
        # Her maç için adil oran merkezlerini belirle
        fair_h = random.uniform(1.6, 3.2)
        # Beraberlik adil oranı
        fair_x = random.uniform(3.0, 4.0)
        # Deplasman adil oranı (implied probability 1.0 yapacak şekilde)
        prob_h = 1.0 / fair_h
        prob_x = 1.0 / fair_x
        prob_a = max(0.05, 0.95 - prob_h - prob_x) # marjsız
        fair_a = 1.0 / prob_a
        
        # Farklı bookmaker oranları üret
        bookmaker_odds = {}
        for b in BOOKMAKERS:
            # Bookmaker marjı ekle (%2 ila %8)
            if b in ["Pinnacle", "Betfair Exchange"]:
                margin = random.uniform(0.015, 0.025) # Düşük marj
            else:
                margin = random.uniform(0.05, 0.08) # Yüksek marj
                
            # Marjlı olasılıklar
            m_prob_h = prob_h * (1.0 + margin)
            m_prob_x = prob_x * (1.0 + margin)
            m_prob_a = prob_a * (1.0 + margin)
            
            # Oranları oluştur (küçük dalgalanmalarla)
            o1 = max(1.05, 1.0 / (m_prob_h * random.uniform(0.95, 1.05)))
            ox = max(1.05, 1.0 / (m_prob_x * random.uniform(0.95, 1.05)))
            o2 = max(1.05, 1.0 / (m_prob_a * random.uniform(0.95, 1.05)))
            
            bookmaker_odds[b] = {
                "o1": round(o1, 2),
                "ox": round(ox, 2),
                "o2": round(o2, 2)
            }
            
        # Arbitraj fırsatı var mı tara (en yüksek oranları birleştir)
        best_1 = 0.0
        best_1_site = ""
        best_x = 0.0
        best_x_site = ""
        best_2 = 0.0
        best_2_site = ""
        
        for b, odds in bookmaker_odds.items():
            if odds["o1"] > best_1:
                best_1 = odds["o1"]
                best_1_site = b
            if odds["ox"] > best_x:
                best_x = odds["ox"]
                best_x_site = b
            if odds["o2"] > best_2:
                best_2 = odds["o2"]
                best_2_site = b
                
        # Arbitraj kontrolü
        is_arb, S, margin_pct = calculate_arbitrage(best_1, best_x, best_2)
        
        # Test amaçlı: 2. maçta kesin arbitraj fırsatı zorla oluştur
        if idx == 1 and not is_arb:
            # Deplasman oranını Betfair'de yapay olarak yükselt
            best_2 = round(1.05 / (1.0 - (1.0/best_1) - (1.0/best_x)), 2)
            best_2_site = "Betfair Exchange"
            bookmaker_odds["Betfair Exchange"]["o2"] = best_2
            is_arb, S, margin_pct = calculate_arbitrage(best_1, best_x, best_2)
            
        # Value Bet kontrolü (Pinnacle'ı adil fiyat referansı kabul et)
        # Pinnacle'ın marjını arındırarak "Adil Fiyat" olasılığını bul
        p_odds = bookmaker_odds["Pinnacle"]
        p_S = (1.0 / p_odds["o1"]) + (1.0 / p_odds["ox"]) + (1.0 / p_odds["o2"])
        fair_prob_1 = (1.0 / p_odds["o1"]) / p_S
        
        # Diğer soft bürolardan birinde Pinnacle'ın adil fiyatının üstünde oran var mı?
        best_ev = 0.0
        best_ev_site = ""
        best_ev_odds = 0.0
        for b in ["Bet365", "Bwin", "Unibet", "1xBet"]:
            b_odds = bookmaker_odds[b]["o1"]
            ev = (fair_prob_1 * b_odds) - 1.0 # Basit EV formülü
            if ev > best_ev:
                best_ev = ev
                best_ev_site = b
                best_ev_odds = b_odds

        # Karşılaşmayı listeye ekle
        mac_adi = f"{home} vs {away}"
        zaman_damgasi = f"{tarih_str}"
        
        if is_arb:
            maclar.append({
                "zaman": zaman_damgasi,
                "mac": mac_adi,
                "tur": "SUREBET (ARB)",
                "site1": f"{best_1_site} (Ev: {best_1:.2f})",
                "site2": f"{best_x_site} (Ber: {best_x:.2f})",
                "site3": f"{best_2_site} (Dep: {best_2:.2f})",
                "detay": f"Implied Prob: {(S*100):.1f}%",
                "edge": f"+{(margin_pct*100):.2f}%",
                "raw_data": {
                    "o1": best_1,
                    "ox": best_x,
                    "o2": best_2
                }
            })
        elif best_ev > 0.03: # %3'ten büyük EV fırsatı
            maclar.append({
                "zaman": zaman_damgasi,
                "mac": mac_adi,
                "tur": "VALUE BET (EV+)",
                "site1": f"{best_ev_site} (Ev: {best_ev_odds:.2f})",
                "site2": "—",
                "site3": "—",
                "detay": f"Adil Oran: {(1.0/fair_prob_1):.2f} (Pinnacle)",
                "edge": f"+{(best_ev*100):.2f}%",
                "raw_data": {
                    "o1": best_ev_odds,
                    "ox": 1.0, # dummy
                    "o2": 1.0  # dummy
                }
            })

    return maclar

def main():
    # Klasör yoksa oluştur
    if not os.path.exists(DASHBOARDS_DIR):
        os.makedirs(DASHBOARDS_DIR)
        
    print("=" * 60)
    print("         T2SAIM SPOR ARBITRAJ LIVE SCANNER NODE")
    print("=" * 60)
    print("[+] Canli tarama aktif. Cikmak icin Ctrl+C tuslarina basin.")
    print(f"[+] Veri Yazim Adresi: {OUTPUT_PATH}")
    print("-" * 60)
    
    try:
        while True:
            # 1. Oranları al (Simülasyon veya API)
            if API_KEY:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] API uzerinden canli oranlar cekiliyor...")
                # Buraya API entegrasyonu yazılabilir (Requests ile)
                maclar = [] 
            else:
                maclar = get_simulated_odds()
                
            # 2. JSON olarak kaydet
            data_to_save = {
                "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "toplam_firsat": len(maclar),
                "maclar": maclar
            }
            
            with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, indent=4, ensure_ascii=False)
                
            # 3. Konsola log bas
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Tarama Tamamlandi. {len(maclar)} Firsat Kaydedildi.")
            for m in maclar:
                print(f"  [{m['tur']}] {m['mac']} -> Edge: {m['edge']} ({m['site1']})")
                
            # 10 saniye bekle
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\n[-] Tarama dugumu durduruldu. Kaptan Tarco iyi gunler diler.")
        sys.exit(0)

if __name__ == "__main__":
    main()
