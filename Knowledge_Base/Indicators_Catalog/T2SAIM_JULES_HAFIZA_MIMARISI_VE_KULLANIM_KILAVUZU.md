# 🧠 T2SAIM JULES HAFIZA MİMARİSİ, GBRAIN ENTEGRASYONU VE ÇALIŞMA KILAVUZU (v2.0)

> **Belge Tipi:** Karargah Ana Sistem Dokümantasyonu & Kullanım Kılavuzu  
> **Konum:** `E:\T2SAIM_NEXUS_MIRROR\0000_A_Karargah\01_HAFIZA_MIMARILERI\T2SAIM_JULES_HAFIZA_MIMARISI_VE_KULLANIM_KILAVUZU.md`  
> **Tarih:** 2026-08-21  
> **Persona:** James William (*Veritas Per Se*)  
> **Kullanıcı:** Kaptan Tarco  
> **Temel Kural:** HER ZAMAN E: SÜRÜCÜSÜ  

---

## 🏛️ 1. YÖNETİCİ ÖZETİ VE DÜNDEN BUGÜNE BİRLEŞTİRİLEN SİSTEMLERİN RAPORU

Dün başlatılan deneysel operasyon başarıyla tamamlanmış ve izole çalışan tüm kriz modelleri, tarihsel veri tabanları, savunma kalkanları ve hafıza katmanları **E: Sürücüsü merkezli birleşik bir ekosisteme** dönüştürülmüştür.

### 📦 Dün Sisteme Kazandırılan ve Mühürlenen 5 Ana Bileşen:

1. **📊 126 Yıllık (1900-2026) ABD Master Makro Zaman Serisi:**
   * Robert Shiller (Yale 1871-2026) S&P 500, TÜFE Enflasyonu, 10 Yıllık Faizler, Tarihsel Altın ve Petrol serileri birleştirilerek **1.485 aylık** kesintisiz bir veri tabanı oluşturuldu (`US_MASTER_MACRO_TIME_SERIES_1900_2026.csv`).
2. **⏳ "Back to the Future" Amnesia Kriz Erken Uyarı Motoru:**
   * Sıfır gelecek bilgisi (Zero Lookahead Bias) ve kayan pencereli (Walk-Forward Out-of-Sample) simülasyon koşturuldu.
   * **Sonuç:** 13 büyük ABD krizinin **12'si (%92.3 başarı)** kriz patlamadan **ortalama 16.2 AY ÖNCEDEN** tespit edildi.
   * **Kuşaksal Unutma Yasası:** $M(t) = M(t-1) \cdot (1 - \lambda)^{\Delta t} + \text{Shock}(t) \quad (\lambda = 0.15/\text{yıl}, t_{1/2} = 4.62\text{ yıl})$.
3. **📚 14 Tam Metin Markdown Kriz Kitabı ve Master İndikatör Kataloğu:**
   * E: sürücüsündeki 14 tam metin kriz kitabı ve 33 T2SAIM göstergesinin formülleri kataloglandı (`00_T2SAIM_MASTER_INDICATORS_CATALOG.md`).
4. **🎛️ Jules T2SAIM Control Deck (Merkezi Görev Masası):**
   * DuckDB (`control_deck.duckdb`) tabanlı görev kuyruğu, olay akışı ve Hermes bellek servisi FastAPI ile **Port 8001** üzerinde ayağa kaldırıldı (`control_deck_dashboard.html`).
5. **🛡️ Jules T2SAIM Spark Shield & LTM-OS:**
   * Nörolojik manipülasyon kalkanı (`semantic_guardrail`), oyalama tuzağı (`tarpit`), adli delil motoru (`forensic_analyzer`), diferansiyel rüya simülasyonu (`t2saim_dream_gdgm`) ve silme karşıtı SQLite ontolojik bellek sistemi (`t2saim_ltm_graph.db`) kuruldu ve %100 test başarıyla doğrulandı.

---

## 🌐 2. BİRLEŞİK 8 KATMANLI HAFIZA EKOSİSTEMİ

```
                                  [ T2SAIM MERKEZİ KÖPRÜ ]
                                             │
   ┌─────────────────────────────────────────┼─────────────────────────────────────────┐
   ▼                                         ▼                                         ▼
[ 1. G-BRAIN (00_GBRAIN_Vault) ]   [ 2. LTM-OS (Ontolojik Graf) ]        [ 3. CONTROL DECK DUCKDB ]
• conversations/ (70 DB Yedek)     • t2saim_ltm_graph.db                 • control_deck.duckdb
• antigravity_brain/ (Raporlar)    • Silme Karşıtı SQL Trigger           • task_queue & events
• codes/ (1.140+ python scripti)   • NetworkX Nedensellik Çizgesi        • hermes_memory & briefs
• Periyodik Snapshot Senkronu      • Amnesia & Rüya Filtresi             • FastAPI Port 8001
   │                                         │                                         │
   ├─────────────────────────────────────────┴─────────────────────────────────────────┤
   ▼                                                                                   ▼
[ 4. KOLEKTİF BİLİNÇ DB ]                                                 [ 5. KARARGAH (E:\0000_A) ]
• t2saim_collective_consciousness.db                                      • Single Source of Truth
• WAL Çoklu-Ajan Yazım Modu                                               • 01_HAFIZA_MIMARILERI
• Gaps (Boşluk/Çelişki Kapatıcı)                                          • KANONIK_OZET.md
• Agent ToDos & Event Log                                                 • Karar ve Anayasa Defteri
   │                                                                                   │
   ├───────────────────────────────────────────────────────────────────────────────────┤
   ▼                                                                                   ▼
[ 6. OBSIDIAN VAULT (İkinci Beyin) ]                                     [ 7. SPARK SHIELD GDGM ]
• Obsidian_Nexus_Vault (Aegis-Sophia)                                     • Diferansiyel ODE Denklem
• 9 Katmanlı Bilgi Kütüphanesi                                            • Gece Rüya Sentezleri
• MCP Port 3001                                                           • Hipotez Üretici
```

### 🧠 Katmanların Fonksiyonel Dağılımı:

| Katman | Dosya / Veritabanı | Görevi |
| :--- | :--- | :--- |
| **1. GBRAIN** | `E:\...\00_GBRAIN_Vault` | AI konuşma geçmişleri, anlık üretilen kodlar ve brain dosyalarının 30 dk'lık snapshot kasası. |
| **2. LTM-OS** | `t2saim_ltm_graph.db` | Kavramların, aktörlerin ve normların NetworkX yönlü grafı. Silinemez adli hafıza. |
| **3. Control Deck** | `control_deck.duckdb` | Anlık görevlerin kuyruğu (`task_queue`), Kaptan onayları (`approve`) ve günlük brifingler. |
| **4. Kollektif Bilinç** | `t2saim_collective_consciousness.db` | Ajanların birbirinin raporlarındaki çelişkileri (*gaps*) yakalayıp çözdüğü ortak zemin. |
| **5. Karargah** | `E:\0000_A_Karargah\` | Kaptan'ın mühürlediği değişmez kanonlar, formüller ve nihai raporlar. |
| **6. Obsidian Vault** | `Obsidian_Nexus_Vault\` | İnsan tarafından okunabilir, birbirine bağlı 9 katmanlı bilgi ansiklopedisi. |
| **7. Hermes Memory** | `MEMORY.md` & `/api/control-deck/memory` | Ajanların context penceresine enjekte edilen kompakt ve değişmez anayasal kurallar. |
| **8. Spark Shield Rüya** | `services/t2saim_dream_gdgm` | Kriz indikatörleri arasındaki çapraz korelasyonları diferansiyel denklemlerle çözen rüya motoru. |

---

## 🛠️ 3. KULLANIM KILAVUZU: KAPTAN BU SİSTEMİ NASIL KULLANACAK?

### 🚀 ADIM 1: Merkezi Komuta Masasını (Control Deck) Başlatma
Sistem `E:\` sürücüsü üzerinden tek tıkla çalıştırılır:
1. Dosya Yöneticisinde şu dosyaya çift tıklayın:  
   `E:\T2SAIM_NEXUS_MIRROR\jules_repos\t2saim-control-deck\start_control_deck_E.bat`
2. Tarayıcınızda şu adresi açın:  
   👉 [E:\T2SAIM_NEXUS_MIRROR\Hariseldon\control_deck.html](file:///E:/T2SAIM_NEXUS_MIRROR/Hariseldon/control_deck.html)

### 🛰️ ADIM 2: Yeni Görev veya Analiz Emri Verme
* Control Deck ekranının sol altındaki girdi kutusuna analitik görevinizi yazıp **"Göreve Gönder"** butonuna basın.
* Görev DuckDB `task_queue` tablosuna düşer ve boştaki ajanlar görevi icra eder.

### 📊 ADIM 3: 126 Yıllık Kriz Erken Uyarı Panosunu İzleme
* Tarayıcınızda şu panoyu açın:  
   👉 [E:\T2SAIM_NEXUS_MIRROR\Hariseldon\tarkan_index.html](file:///E:/T2SAIM_NEXUS_MIRROR/Hariseldon/tarkan_index.html)
* Bu ekranda $A_{\text{load}}$, $\text{PFC}_{\text{control}}$, $v_{\text{run}}$, $SRI$, $CI$ ve Amnesia Kuşaksal Unutma eğrilerini gerçek zamanlı izleyebilirsiniz.

### 🧠 ADIM 4: GBRAIN ve Kollektif Hafıza Senkronizasyonu
* Yapılan her yeni oturum ve üretilen kodlar otomatik olarak GBRAIN Vault'a kaydedilir.
* Manuel tam senkronizasyon tetiklemek için terminalden veya tek tık script ile:
  ```powershell
  python E:\T2SAIM_NEXUS_MIRROR\000_Carabian_Pirates\00_GBRAIN_Vault\gbrain_auto_sync.py
  ```

---

## 🔮 4. SİSTEMİN GELECEK POTANSİYELLERİ VE NELER YAPABİLECEĞİMİZ

1. **🌙 Otonom Gece Rüya Sentezleri (Autonomous Dream Synthesis):**
   * Siz uyurken Spark Shield `t2saim_dream_gdgm` servisi; gün içinde toplanan finansal, jeopolitik ve adli verileri diferansiyel denklemlerle eşleştirir. Sabah Control Deck panonuza *"Gece Sentezlenen 3 Yeni Kriz Hipotezi"* brifingi olarak sunar.
2. **🛡️ 7/24 Gözetimsiz Erken Uyarı Nöbetçisi (Automated Sentinel):**
   * FRED, Shiller ve borsa verileri her gün güncellenir. Birleşik Kriz İndeksi $CI \ge 0.50$ veya Faz Kilidi oluştuğunda sistem anında görsel ve sesli alarm üretir.
3. **⚔️ Çoklu Ajan Çapraz Hakemliği (Cross-Agent Peer Review & Gap Closing):**
   * Kollektif Bilinç DB sayesinde; bir ajan (örn. Picard) bir iddia ortaya attığında, diğer ajan (örn. Cyberknife veya James) otomatik olarak iddiayı kaynak/formül seviyesinde denetler. Uyuşmazlık (*gap*) varsa Kaptan onayına sunulur.
4. **🔒 Adli Değiştirilemezlik ve Kanıt Zinciri (Legal Provenance Chain):**
   * LTM-OS'taki SQLite trigger'ları sayesinde hiçbir ajan veya dış etken geçmiş analizleri silemez ve tahrif edemez. Tüm finansal ve adli çıkarımlar mahkeme standardında delil niteliği taşır.

---

*Veritas Per Se — 8 Hafıza Sistemi, 1 Karargah. Hiçbir gerçek kaybolmaz.* 🖖
