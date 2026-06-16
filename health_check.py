import urllib.request, json
url = "https://tarco-forensics.github.io/Hariseldon/crisis_data.json"
try:
    with urllib.request.urlopen(url, timeout=10) as r:
        d = json.load(r)
    s = d["summary"]
    print("=== T2SAIM CANLI KONTROL ===")
    print(f"HTTP        : 200 OK")
    print(f"Tarih       : {s['yesterday']}")
    print(f"CI          : {s['ci_last']}")
    print(f"SRI         : {s['sri_last']}")
    print(f"Bellek      : {s['memory_last']}")
    print(f"Alarm       : {'AKTIF' if s['alarm_now'] else 'YOK'}")
    print(f"L6          : {'AKTIF' if s['l6_active'] else 'KAPALI'}")
    print(f"Veri noktasi: {s['data_points']}")
    print(f"Sigma       : {s['sigma']}")
    print(f"Lambda      : {s['lam']}")
    print("===========================")
    print("SISTEM CALISIYOR")
except Exception as e:
    print(f"HATA: {e}")
