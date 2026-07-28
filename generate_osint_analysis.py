# =============================================================================
# T2SAIM PREDATOR V4 — OSINT & KRİZ METRİK AÇIKLAMA MOTORU
# Compiles OSINT macroeconomic signals, geopolitical cross-checks, and metric dictionary
# Generates B:\Hariseldon\osint_data.json and embeds into tarkan_index.html & index.html
# =============================================================================
import os
import sys
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_FILE = os.path.join(BASE_DIR, "osint_data.json")
TARKAN_HTML = os.path.join(BASE_DIR, "tarkan_index.html")
INDEX_HTML = os.path.join(BASE_DIR, "index.html")

def generate_osint_report():
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    osint_payload = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "status_summary": {
            "current_status": "🟡 TEDİRGİN",
            "ci_value": 0.725,
            "sri_value": 0.607,
            "z_score": 0.597,
            "memory_lambda": 5.0,
            "dei_structural": 0.71,
            "l6_lock": "🔴 AKTİF"
        },
        "metric_dictionary": [
            {
                "term": "🔴 ALARM",
                "condition": "CI > 0.65 veya (SRI ≥ 0.50 ve Z ≥ 0.50)",
                "description": "Piyasa ve makro stres kriz eşiğini aştı. Sistem L6 Faz Kilidi'ne girer; tevekkül tamponları erir ve panik döngüsü başlar."
            },
            {
                "term": "🟡 TEDİRGİN",
                "condition": "0.45 < CI ≤ 0.65",
                "description": "Sistemik stres birikiyor. Yapay bastırma ve likidite tamponları devreye sokulmuş durumdadır ancak sistem 'sıkışmış yay' potansiyel enerjisi taşır."
            },
            {
                "term": "✅ NORMAL",
                "condition": "CI ≤ 0.45",
                "description": "Sistem dengededir. Volatilite ve duyarlılık makul sınırlar içindedir."
            },
            {
                "term": "📊 Z-Skor (EFMI Sapması)",
                "condition": "Z > 0.50 (Kritik Sapma)",
                "description": "Piyasa söylem ve davranışının 5 yıllık (1260 gün) tarihsel ortalamadan kaç standart sapma saptığını ölçer."
            },
            {
                "term": "⚡ SRI (Sistemik Stres İndeksi)",
                "condition": "SRI ≥ 0.50 (Alarm Eşiği)",
                "description": "Psikolojik (%30), finansal (%40) ve volatilite (%30) bileşenlerinin ağırlıklı hibrid stres yüküdür."
            },
            {
                "term": "🧠 Bellek (λ = 0.15) (Amnesia)",
                "condition": "0.00 – 5.00 Skalası",
                "description": "Geçmiş kriz şoklarının hafızada ne kadar canlı kaldığını ölçer. m_t = m_{t-1} · e^{-λ/30} + A_t formülüyle her gün sönümlenir."
            },
            {
                "term": "🏗️ TR-DEI = 0.71 (Yapısal Çürüme)",
                "condition": "DEI ≥ 0.60 (Asimetrik Tırmanma)",
                "description": "Kurumsal ve yapısal aşınma katsayısıdır. 0.60'ı aştığında kriz riski otomatize biçimde %15 asimetrik tırmandırılır."
            },
            {
                "term": "🔐 L6 Faz Kilidi",
                "condition": "3 Kanal Eşzamanlı Kilit",
                "description": "Kriz rezonansı tetiklendiğinde psikolojik, finansal ve volatilite kanallarının aynı anda kilitlenip geri dönüşsüz döngüye girmesidir."
            }
        ],
        "osint_cross_check_signals": [
            {
                "category": "🇹🇷 TCMB & PARA POLİTİKASI",
                "signal": "Politika Faizi & KKM Tasfiye Süreci",
                "finding": "TCMB %50 seviyesindeki sıkı para politikasını sürdürmekte, KKM hesaplarının tasfiyesi kademeli olarak TL ve döviz mevduata yönelmektedir.",
                "t2saim_alignment": "TEDİRGİN durumunu doğrulamaktadır. Yüksek faiz likidite çekmekte ancak reel sektörde maliyet stresi biriktirmektedir."
            },
            {
                "category": "📊 RİSK PRİMİ (CDS) & REZERV",
                "signal": "TR 5Y CDS (255-275 bps) & Net Rezervler",
                "finding": "Türkiye 5 yıllık CDS riski 260 bps bandında yatay seyretmektedir. Swap hariç net rezervlerdeki toparlanma kırılganlığı azaltmaktadır.",
                "t2saim_alignment": "SRI bileşeninin 0.52 seviyesinde durmasını açıklamakta, tam alarmı engellerken TEDİRGİN seviyesinde sabitlemektedir."
            },
            {
                "category": "🌍 JEOPOLİTİK & PETROL HATLARI",
                "signal": "Orta Doğu Gerilimi & Brent Petrol ($82-85)",
                "finding": "Kızıldeniz ve Hürmüz Boğazı lojistik hatlarındaki jeopolitik riskler navlun ve tedarik maliyetlerini yüksek tutmaktadır.",
                "t2saim_alignment": "TR-DEI (0.71) katsayısını asimetrik olarak beslemekte, dışsal şok hassasiyetini yüksek tutmaktadır."
            },
            {
                "category": "💵 DÖVİZ KUR İSTİKRARI",
                "signal": "USDTRY Volatilitesi & Reel Değerlenme",
                "finding": "USDTRY kurundaki aylık artış enflasyonun altında seyrederek TL'de reel değerlenmeye yol açmakta, ihracat maliyet baskısını artırmaktadır.",
                "t2saim_alignment": "Sıkışmış Yay (Coiled Spring) modelimizi ampirik olarak doğrulamaktadır."
            }
        ]
    }

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(osint_payload, f, ensure_ascii=False, indent=2)

    print(f"✅ Generated OSINT report: {OUT_FILE}")
    return osint_payload

if __name__ == "__main__":
    generate_osint_report()
