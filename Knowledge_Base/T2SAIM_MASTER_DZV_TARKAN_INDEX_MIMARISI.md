# T2SAIM MASTER DZV & TARKAN INDEX KRİZ TESPİT PLATFORMU

## Bütünleşik Sistem Mimarisi, Matematiksel Modeller, Açık Veri Boru Hattı ve Uygulama Stratejisi

Bu belge; geliştirilmiş olan **T2SAIM Master DZV Kriz Tespit Motoru** Python çekirdeği ile makroekonomik şartnamenin, davranışsal amigdala matematiğinin, kurumsal iktisat teorilerinin (Acemoğlu & Gullini) ve açık kaynaklı veri mimarisinin tek bir çatı altında birleştirilmiş nihai teknik kılavuzudur.

---

## 1. Bütünleşik DZV Mimarisi ve Epistemolojik Çerçeve

```
+----------------------------------------------------------------------------------------------------+
|                                    DZV EPISTEMOLOJİK MOTORU                                        |
+---------------------------------+----------------------------------+-------------------------------+
| DİYALEKTİK (D)                  | ZORUNLULUK (Z)                   | VARYANS (V)                   |
| Doğrusal Varlık İllüzyonu vs.   | Parabolik Borç Servisi ve        | Enformasyon Asimetrisi (Gullini)|
| Parabolik Borç Servis Çelişkisi | Rezonans Tekilliği (t* Noktası)  | ve Amigdala Stres Salınımı    |
+---------------------------------+----------------------------------+-------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
|                            HESAPLAMALI ÇEKİRDEK (Python Engine)                                    |
|  [Amnesia Kuşaksal Bellek M(t)] -> [İkili Amigdala Yükü A_load(t)] -> [Kuple Rezonans R(t)]        |
|  [Banka Kırılganlığı BFI(t)]    -> [Sistemik Rezonans SRI(t)]      -> [Birleşik Kriz İndeksi CI(t)]|
+-------------------------------------------------+--------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
|                                    AÇIK KAYNAK VERİ GİRİŞLERİ                                      |
|  * Bankacılık: BDDK Bültenleri & TCMB Bilanço (Hayalet Krediler, Likidite Karşılama)               |
|  * Makroekonomi: TCMB EVDS & Hazine İtfa (REER Sarkacı, Net Rezerv, 185 Mr $ Dış Borç)             |
|  * Siyasal/Kurumsal: KİK İhale Analizi, Resmi Gazete Volatilitesi, TCMB Beklenti Varyansı           |
|  * Toplumsal/Davranışsal: Google Trends Anksiyete Z-Skoru, MKK Yatırımcı Dinamikleri               |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Genişletilmiş Matematiksel ve Davranışsal Formülasyon

Sistemdeki tüm denklemler web arayüzünde KaTeX/MathJax tarafından dinamik olarak işlenir.

### 2.1. Kuşaksal Unutma (Amnesia) ve İkili Amigdala Stres Yükü ($A_{\text{load}}$)

Toplumların ve piyasa yapıcıların geçmiş krizleri unutma hızı üstel bozunma ile modellenir:

$$M(t) = M(t-1) \cdot (1 - \lambda_m) + \text{Shock}(t)$$

$$\lambda_m = 1 - (1 - \lambda_y)^{1/12}, \quad \lambda_y = 0.15 \quad (\text{Hafıza Yarı Ömrü } t_{1/2} \approx 4.62 \text{ Yıl})$$

$$\text{Shock}(t) = \min\left(5.0, \frac{\vert{}\text{Drawdown}_{10y}\vert{}}{15.0} + \frac{\sigma_{\text{vol, 12m}}}{15.0}\right)$$

Amigdala stres yükü; **Panik Baskısı** ile **Varlık Balonu Baskısı** arasındaki maksimum gerilimden beslenir ve hafıza erozyonu çarpanı ($Amp_{\text{amnesia}}$) ile amplifiye edilir:

$$Amp_{\text{amnesia}}(t) = 1.0 + \max\left(0, \frac{2.0 - M(t)}{2.0}\right) \cdot \widehat{\text{Bubble}}(t) \cdot 0.8$$

$$\text{Stress}_{\text{total}}(t) = \max\left(\text{Stress}_{\text{panic}}(t), \, \text{Stress}_{\text{bubble}}(t)\right) \cdot Amp_{\text{amnesia}}(t)$$

$$A_{\text{load}}(t) = \frac{1}{1 + e^{-8.0 \cdot (\text{Stress}_{\text{total}}(t) - 0.38)}}$$

---

### 2.2. Diferansiyel Borç İvmelenmesi ve Minsky Tekilliği

Borç stokunun doğrusal artışına ($S_D \sim t$) karşılık borç çevrim maliyetinin parabolik ivmelenmesi ($S_S \sim t^2$):

$$S_D(t) = \alpha \cdot (t - t_0)$$

$$S_S(t) = \frac{1}{2} \delta_S \delta_D (t - t_0)^2$$

Fiyat ve nakit akış sistemi:

$$\frac{dP(t)}{dt} = -\lambda_P \left[ V_S(t) - V_D(t) - S_D(t) + S_S(t) \right]$$

$$\frac{d^2 V_S(t)}{dt^2} = \lambda_S \frac{dP(t)}{dt}, \quad \frac{d^2 V_D(t)}{dt^2} = -\lambda_D \frac{d^2 P(t)}{dt^2}$$

* **Kritik Eşik ($t^*$):** $S_S(t) > V_S(t) - V_D(t)$ olduğu anda nakit akışları faiz yükünü karşılayamaz hale gelir; sistem Ponzi evresine geçerek rezonans kilitlenmesine uğrar.

---

### 2.3. Kuple Osilatörler, Bankacılık Kırılganlığı ve Birleşik Kriz İndeksi

$$\ddot{x}_{\text{fin}} + \gamma_1 \dot{x}_{\text{fin}} + \omega_{\text{fin}}^2 x_{\text{fin}} + \kappa (x_{\text{fin}} - x_{\text{reel}}) = F_{\text{ext}}(t)$$

$$\ddot{x}_{\text{reel}} + \gamma_2 \dot{x}_{\text{reel}} + \omega_{\text{reel}}^2 x_{\text{reel}} + \kappa (x_{\text{reel}} - x_{\text{fin}}) = 0$$

$$R(t) = \frac{\Delta_0}{\sqrt{(\omega_{\text{fin}}^2 - \omega_{\text{reel}}^2)^2 + 4 \gamma^2 \omega_{\text{reel}}^2}}$$

$$\text{BFI}(t) = \min\left(1.0, \, 0.45 \cdot \widehat{\Delta \text{Faiz}}(t) + 0.30 \cdot \widehat{\text{Değerleme}}(t) + 0.25 \cdot \widehat{\text{Volatilite}}(t)\right)$$

$$\text{SRI}(t) = \left( A_{\text{load}}(t) \cdot \text{BFI}(t) \cdot \max(0.10, \widehat{\text{Kırılganlık}}(t)) \right)^{1/3}$$

$$\text{CI}(t) = \text{clip}\left(0.35 A_{\text{load}} + 0.30 \text{BFI} + 0.20 \max(\text{DD}, \text{Bubble}) + 0.15 \text{Inf}, \, 0.0, \, 1.0\right)$$

* **Faz Kilidi Alarmı:** $\text{CI}(t) \ge 0.48 \quad \lor \quad (\text{SRI}(t) \ge 0.38 \land A_{\text{load}}(t) \ge 0.52)$

---

### 2.4. REER Sarkacı ve Faz Uzayı ($\theta, \dot{\theta}$) Alarm Mekanizması

Reel Efektif Döviz Kuru'nun uzun dönemli ortalamadan sapma açısı:

$$\theta_{\text{REER}}(t) = \frac{\text{REER}(t) - \mu_{\text{REER}}}{\sigma_{\text{REER}}}$$

* **Tersine Dönüş Koşulu:** $\dot{\theta}_{\text{REER}}(t) < 0$ ve $\theta_{\text{REER}}(t) > +1.5\sigma$
* **Sistemik Panik Tetikleyicisi:** REER sarkacının tepe noktasından sert aşağı yöneldiği anda $A_{\text{load}}(t) > 0.65$ ise sıcak para çıkışı ve likidite donması üstel hızlanır.

---

## 3. Açık Kaynak Veri Mimarisi ve Gösterge Haritası

Tüm göstergeler doğrulanabilir açık kaynaklardan çekilecek şekilde standardize edilmiştir:

```
+----------------------------------------------------------------------------------------------------+
|                                    AÇIK KAYNAK VERİ TABLOSU                                       |
+-------------------+------------------------------------+-------------------------------------------+
| KATEGORİ          | VERİ SETİ / GÖSTERGE               | AÇIK KAYNAK & YÖNTEM                      |
+-------------------+------------------------------------+-------------------------------------------+
| BANKACILIK        | * 2. Grup / Yakın İzleme Kredileri | BDDK Haftalık Bülten (Tablo 1 - Krediler) |
| SEKTÖRÜ           | * Yüzdürülen Hayalet Krediler     | BDDK Aylık Bankacılık Temel Göstergeleri  |
|                   | * Likidite Karşılama Oranı (LKO)   | BDDK Tablo: Likidite & SYR               |
|                   | * Sektör YP Net Genel Pozisyonu    | TCMB EVDS (Banka Bilançoları)             |
|                   | * Gecelik Fonlama & TPP Hacmi      | BIST & Takasbank Para Piyasası Verileri   |
+-------------------+------------------------------------+-------------------------------------------+
| ULUSAL MAKRO      | * Swap Hariç Net Rezervler         | TCMB EVDS Analitik Bilanço                |
| EKONOMİ & BORÇ    | * REER (TÜFE & ÜFE Bazlı)          | TCMB EVDS Reel Efektif Döviz Kuru         |
|                   | * 185 Mr $ Dış Borç İtfa Takvimi   | Hazine ve Maliye Bakanlığı Borç Raporları|
|                   | * İç/Dış Borç Çevirme Oranları     | Hazine Nakit Gerçekleşmeleri              |
|                   | * Çekirdek Enflasyon (B ve C)      | TÜİK Tüketici Fiyat Endeksi Bülteni       |
+-------------------+------------------------------------+-------------------------------------------+
| SİYASAL &         | * İhale Dağılım HHI (Acemoğlu)     | Kamu İhale Kurumu (KİK) İhale Bültenleri  |
| KURUMSAL GÜVEN    | * 21/b İstisnai İhale Oranı        | EKAP Kamu Alımları İstatistikleri         |
|                   | * Beklenti Dağılım Varyansı        | TCMB Piyasa Katılımcıları Anketi ($G_{def}$)|
|                   | * Mevzuat Belirsizlik İndeksi      | T.C. Resmî Gazete Günlük Değişiklik Sayısı|
+-------------------+------------------------------------+-------------------------------------------+
| TOPLUMSAL &       | * Finansal Anksiyete Z-Skoru       | Google Trends API ("dolar", "iflas" vb.)  |
| DAVRANIŞSAL       | * Bireysel Yatırımcı Giriş/Çıkışı  | MKK (Merkezi Kayıt Kuruluşu) Bültenleri   |
|                   | * Tüketici Güven Beklenti Makası   | TÜİK-TCMB Tüketici Güven Endeksi          |
+-------------------+------------------------------------+-------------------------------------------+
```

---

## 4. Sistemik Boşluklar ve İleri Analitik Modüller

```
+----------------------------------------------------------------------------------------------------+
|                               İLAVE İLERİ SEVİYE ANALİTİK MODÜLLER                                 |
+---------------------------------+----------------------------------+-------------------------------+
| 1. HAYALET KREDİ AYRIŞTIRMA     | 2. FREKANS SENKRONİZASYONU       | 3. FAZ UZAYI ÇEKİCİSİ         |
| Yakın İzleme (Stage 2) +        | TCMB Fonlama Vadesi vs.          | $(\theta, \dot{\theta})$      |
| Yapılandırmalar (Forbearance)   | Reel Nakit Döngüsü (CCC)         | Limit Döngüsü / Kaotik Çöküş  |
+---------------------------------+----------------------------------+-------------------------------+
```

### 4.1. Hayalet / Zombi Kredi Ayrıştırma Modeli

Görünür NPL oranı regülasyon esneklikleriyle düşük tutulabilir. Gerçek hayalet kredi yükü ($L_{\text{ghost}}$):

$$L_{\text{ghost}}(t) = \text{Stage2}(t) + \text{Forbearance}(t) + \text{Restructured}(t) - \text{Provision}(t)$$

$$\text{GhostRatio}(t) = \frac{L_{\text{ghost}}(t)}{\text{TotalLoans}(t)}$$

### 4.2. Finansal-Reel Frekans Senkronizasyonu

* $\omega_{\text{fin}}(t)$: TCMB fonlama kompozisyonunun ortalama vadesi ve gecelik faiz oynaklığından türetilir.
* $\omega_{\text{reel}}(t)$: Sanayi sektörünün ortalama Nakit Dönüşüm Süresi (Cash Conversion Cycle - CCC) üzerinden hesaplanır.
* $\omega_{\text{fin}} \approx \omega_{\text{reel}}$ olduğunda $R(t)$ rezonans katsayısı patlar.

### 4.3. Faz Uzayı Çekici Analizi (Phase Space Attractor)

REER sapması $\theta(t)$ ile türevi $\dot{\theta}(t)$ kartezyen düzlemde eşleştirilir. Yörüngenin sabit bir limit çevrimden çıkarak spiralleşmesi sistemik faz geçişini gösterir.

---

## 5. UI/UX ve İnteraktif Görselleştirme Şartnamesi

```
+----------------------------------------------------------------------------------------------------+
| T2SAIM KRİZ MERKEZİ                                                           [ 18 Kasım 2026 ]    |
| REZONANS TEPE NOKTASINA KALAN SÜRE: [ 88 Gün | 10 Saat | 07 Dk | 12 Sn ]                           |
+----------------------------------------------------------------------------------------------------+
| [TAM GENİŞLİK 700 GÜNLÜK ZAMAN SERİSİ GRAFİĞİ]                                                     |
| [ - | + ] Zoom | Modlar: [700 Günlük Görünüm] [126 Yıllık 13 Kriz Modu] [52 Gösterge Katmanı]      |
|                                                                                                    |
|  * Seriler: Likidite Koridoru + Net Rezerv + Hayalet Kredi Yükü + Birleşik Kriz İndeksi (CI)       |
|  * İnteraktif Özellik: Her veri noktasına tıklandığında EVDS/BDDK ham veri döküm paneli           |
+----------------------------------------------------------------------------------------------------+
| [REER SARKAÇ GERİLİMİ VE AMİGDALA STRES YÜKÜ ($A_{\text{load}}$)]                                   |
|                                                                                                    |
|  Sol Eksen: REER Sarkaç Açısı (\theta)  |  Sağ Eksen: Amigdala Stresi (A_load) ve Amnesia M(t)     |
|  [Geçmiş Gerçek Veri] ------ [ŞU AN (Ağustos 2026)] ...... [Model Projeksiyonu ($t^*$ Eşiği)]      |
|  ALARM EŞİĞİ: Sarkaç Dönüşü + $A_{\text{load}} > 0.65$ -> [SİSTEMİK FAZ KİLİTLENMESİ ALARMI]       |
+----------------------------------------------------------------------------------------------------+
| 52 MAKRO GÖSTERGE & KURUMSAL KIRILGANLIK KARTLARI                                                  |
| +---------------------+ +---------------------+ +--------------------+ +-------------------------+|
| | TCMB Swap Net Rezerv| | Hayalet Kredi Yükü  | | 185 Mr $ Dış Borç  | | Gullini & Acemoğlu      ||
| | -$42.1 Mr $ [KRİTİK]| | %11.8 (Stage 2 Dahil| | Q4-2026 İtfa Tepe  | | Güven Erozyonu: 0.78    ||
| +---------------------+ +---------------------+ +--------------------+ +-------------------------+|
+----------------------------------------------------------------------------------------------------+
```

---

## 6. Uygulama ve Entegrasyon Yol Haritası (Roadmap)

```
[Faz 1: Veri Hattı] ----> [Faz 2: Python Motoru] ----> [Faz 3: UI & Grafikler] ----> [Faz 4: Doğrulama]
- EVDS / BDDK / KİK       - DZV & Amnesia Entegr.      - 700 Günlük Full-Width        - 13 Tarihsel Kriz
- Web Scraping Pipeline   - Diferansiyel Denklem Çöz.  - REER/Amigdala Çift Panel     - Backtest Kalibrasyonu
```

1. **Faz 1 - Otomatik Veri Boru Hattı:** TCMB EVDS API, BDDK bülten ayrıştırıcıları, Hazine itfa takvimi ve KİK ihale kazıma araçlarının kurularak PostgreSQL/TimescaleDB veri tabanına bağlanması.
2. **Faz 2 - Hesaplama Çekirdeği Entegrasyonu:** Mevcut `T2SAIMMasterCrisisEngine` sınıfının FastAPI mikroservisine dönüştürülmesi; Minsky diferansiyel denklemleri ve Runge-Kutta çözücüsü ile gerçek zamanlı $t^*$ hesaplaması.
3. **Faz 3 - Ön Yüz & Görselleştirme:** React / Next.js, Tailwind CSS ve Highcharts/ECharts kullanılarak tam genişlikli 700 günlük grafik, çift eksenli REER/Amigdala grafiği ve dinamik geri sayım sayacının inşası.
4. **Faz 4 - Kalibrasyon ve Canlı İzleme:** Model parametrelerinin ($\lambda_P, \lambda_S, \lambda_m, \kappa, \gamma$) 1907-2023 arası 52, 8-13 krizlik tarihsel veri üzerinde optimize edilmesi ve canlı alarm bildirim sisteminin devreye alınması.
