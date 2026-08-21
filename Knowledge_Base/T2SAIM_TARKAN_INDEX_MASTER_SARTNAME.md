# T2SAIM / Tarkan Index: Kriz Takip ve Erken Uyarı Platformu

## Sistem Mimarisi, Matematiksel Modeller ve Teknik Şartname

Bu belge; **T2SAIM (Tarkan Index)** makroekonomik kriz takip, rezonans simülasyonu ve erken uyarı sisteminin web/arayüz platformuna dönüştürülmesi için hazırlanan bilimsel, analitik ve modüler teknik talimat setidir.

---

## 1. Sistem Mimarisi ve Zaman Çerçevesi

```
+-----------------------------------------------------------------------------------+
|                           VERİ KATMANI (Data Pipeline)                            |
|  [TCMB EVDS API] -- [BDDK Haftalık Bülten] -- [TÜİK] -- [Hazine] -- [BIS / FRED]  |
|               (Sıfır Sentetik Veri / Otomatik Doğrulama ve Senkronizasyon)        |
+-----------------------------------------+-----------------------------------------+
                                          |
+-----------------------------------------v-----------------------------------------+
|                        HESAPLAMA VE ANALİTİK MOTOR                               |
|  +--------------------+  +----------------------+  +---------------------------+  |
|  | Ekonofizik & Borç  |  | Davranışsal Stres    |  | Kurumsal & Yapısal Kırıl. |  |
|  | İvmelenmesi Motoru |  | ($A_{\text{load}}$ & |  | (Gullini Güvensizlik &    |  |
|  | (Coupled Oscil.)   |  | REER Sarkacı)        |  | Acemoğlu Metrikleri)      |  |
|  +--------------------+  +----------------------+  +---------------------------+  |
+-----------------------------------------+-----------------------------------------+
                                          |
+-----------------------------------------v-----------------------------------------+
|                         GÖRSELLEŞTİRME VE UI KATMANI                              |
|  [Geri Sayım & Rezonans] - [700 Günlük Ana Grafik] - [REER/Amigdala Alt Grafiği]  |
|       [52 Makro Gösterge Matrisi] - [TCMB Likidite Koridoru & Hayalet Krediler]   |
+-----------------------------------------------------------------------------------+
```

### Zaman Projeksiyonu ve Kritik Çapalar

* **Güncel Zaman Çapası:** Ağustos 2026
* **Kritik Rezonans ve Sarkaç Dönüş Eşiği ($t^*$):** 18 Kasım 2026
* **Dinamik Geri Sayım:** Sistemin $t^*$ rezonans tepe noktasına kalan süreyi (Gün / Saat / Dakika / Saniye) canlı hesaplayan sayaç bileşeni.

---

## 2. Matematiksel Formülasyon ve Ekonofizik Motoru

Sistemdeki tüm matematiksel denklemler arayüzde MathJax/KaTeX motoruyla render edilir.

### 2.1. Diferansiyel Borç İvmelenmesi ve Minsky Faz Geçişi

Sistemik borç dinamiği, doğrusal borç birikimi ile parabolik borç servisi arasındaki makas açılması üzerinden modellenir:

$$S_D(t) \sim \alpha \cdot (t - t_0)$$

$$S_S(t) = \frac{1}{2} \delta_S \delta_D (t - t_0)^2$$

Fiyat ve hacim dinamiklerini yöneten diferansiyel denklem sistemi:

$$\frac{dP(t)}{dt} = -\lambda_P \left[ V_S(t) - V_D(t) - S_D(t) + S_S(t) \right]$$

$$\frac{d^2 V_S(t)}{dt^2} = \lambda_S \frac{dP(t)}{dt}$$

$$\frac{d^2 V_D(t)}{dt^2} = -\lambda_D \frac{d^2 P(t)}{dt^2}$$

* **Analitik Yorum:** Borç anaparasının doğrusal ($S_D \sim t$), borç servis maliyetinin ise faiz bileşkesiyle parabolik ($S_S \sim t^2$) artması, finansman yapısının **Hedge $\rightarrow$ Spekülatif $\rightarrow$ Ponzi** aşamalarına evrilmesini sağlar.
* **Kritik Eşik ($t^*$):** $S_S(t^*) > V_S(t^*) - V_D(t^*)$ koşulunun sağlandığı ve nakit akışlarının anapara bir yana sadece faiz yükünü karşılamaya yetmediği tekillik noktasıdır.

```
Finansal
Yük
 ^                                             / Parabolik Borç Servisi: S_S(t) ~ t^2
 |                                            /  [Ponzi Finansmanı]
 |                                           /
 |                                          / <- Rezonans / Kilitlenme Eşiği (t*)
 |                                         /
 |                      ------------------/--- Doğrusal Borç: S_D(t) ~ t
 |                     /                 /     [Spekülatif Finansman]
 |                    /                 /
 |                   /                 /
 |   ---------------/------------------        [Hedge Finansmanı]
 +--------------------------------------------> Zaman (t)
```

---

### 2.2. Piyasalar Arası Rezonans (Coupled Oscillators)

Finansal sektör likidite salınımları ($\omega_{\text{fin}}$) ile reel sektörün nakit döngüsü ve üretim frekansının ($\omega_{\text{reel}}$) etkileşimi:

$$\ddot{x}_{\text{fin}} + \gamma_1 \dot{x}_{\text{fin}} + \omega_{\text{fin}}^2 x_{\text{fin}} + \kappa (x_{\text{fin}} - x_{\text{reel}}) = F_{\text{ext}}(t)$$

$$\ddot{x}_{\text{reel}} + \gamma_2 \dot{x}_{\text{reel}} + \omega_{\text{reel}}^2 x_{\text{reel}} + \kappa (x_{\text{reel}} - x_{\text{fin}}) = 0$$

Burada $\kappa$ piyasalar arası kuplaj katsayısı, $\gamma$ sönümleme faktörüdür. Dış borç çevrim şoku ($\Delta_0$) sisteme girdiğinde rezonans genlik fonksiyonu $R(t)$ zaman serisi olarak hesaplanır:

$$R(t) = \frac{\Delta_0}{\sqrt{(\omega_{\text{fin}}^2 - \omega_{\text{reel}}^2)^2 + 4 \gamma^2 \omega_{\text{reel}}^2}}$$

* $\omega_{\text{fin}} \to \omega_{\text{reel}}$ durumunda $R(t) \to \infty$ (Rezonans Felaketi).

---

### 2.3. Davranışsal Amigdala Yükü ($A_{\text{load}}$) ve REER Sarkaç Modeli

* **REER Sarkaç Açısı ($\theta_{\text{REER}}$):** Reel Efektif Döviz Kuru'nun uzun dönemli denge değerinden sapma genliği:

$$\theta_{\text{REER}}(t) = \frac{\text{REER}(t) - \overline{\text{REER}}}{\sigma_{\text{REER}}}$$

* **Amigdala Stres Yükü ($A_{\text{load}}$):** Piyasa katılımcılarının risk algısı, CDS primleri, mevduat dolarizasyon hızı ve Google Trends finansal anksiyete verilerinin normalize edilmiş bileşkesi ($0 \le A_{\text{load}} \le 1.00$):

$$A_{\text{load}}(t) = w_1 \cdot \widehat{\text{CDS}}(t) + w_2 \cdot \widehat{\Delta \text{Dolarizasyon}}(t) + w_3 \cdot \widehat{\text{Likidite Primi}}(t) + w_4 \cdot \widehat{\text{Anksiyete}}(t)$$

* **Kritik Alarm Eşiği:** $\theta_{\text{REER}}$ zirveden aşağı kırıldığı anda $A_{\text{load}} > 0.65$ ise sistemik panik ve likidite çekilmesi üstel hızlanır.

---

## 3. Kurumsal ve Davranışsal Teorik Modüller

```
+-----------------------------------------------------------------------------------+
|                        TEORİK ÇERÇEVE VE YAPISAL ANALİZ                           |
+-----------------------------------------+-----------------------------------------+
|  Emilio Gullini:                        |  Daron Acemoğlu:                        |
|  GÜVENSİZLİK VE ENFORMASYON ASİMETRİSİ  |  KURUMSAL KALİTE VE BÖLÜŞÜM DİNAMİĞİ    |
|  - Güven Erozyon İndeksi ($G_{\text{def}}$)|  - Kapsayıcı vs. Sömürücü Kurum Skoru    |
|  - Politika Kredibilite Sapması         |  - Rant / Üretken Sermaye Oranı         |
|  - Bankalararası Güvensizlik Primi      |  - Yargı Bağımsızlığı & Mülkiyet Güvencesi|
+-----------------------------------------+-----------------------------------------+
```

### 3.1. Emilio Gullini Modülü (*Economic Crises as a Result of Distrust*)

Piyasa mekanizmalarının çöküşünü sadece parasal büyüklüklerle değil, sözleşme güvenilirliğinin kaybolmasıyla açıklayan gösterge seti:

1. **Güven Erozyon Katsayısı ($G_{\text{def}}$):** Enflasyon beklentileri ile TCMB hedefleri arasındaki sapmanın varyansı.
2. **Kredi Kanallarında Güvensizlik Primi:** Tahvil faizleri ile banka kredi faizleri arasındaki asimetrik makas.
3. **Mevzuat Öngörülebilirlik Endeksi:** Resmi Gazete'de yayımlanan anlık finansal regülasyon değişikliklerinin frekansı.

### 3.2. Daron Acemoğlu Modülü (Kurumsal İktisat & Türkiye Kırılganlık Analizi)

Kaynak tahsisindeki bozulmaları ve düşük verimlilik krizini ölçen yapısal göstergeler:

1. **Kapsayıcı / Sömürücü Kurum Dengesi:** İhale dağılımlarında yoğunlaşma katsayısı (Herfindahl-Hirschman İndeksi).
2. **Verimsiz Sektörel Kredi Tahsisi:** İmalat sanayiine giden kredilerin toplam kredilere oranı / İnşaat-Gayrimenkul rant sektörüne aktarılan kaynak oranı.
3. **Toplam Faktör Verimliliği (TFP) İvmesi:** Dış borç büyümesi ile reel verimlilik artışı arasındaki negatif korelasyon takibi.

---

## 4. 52 Makro Gösterge Seti ve Veri Pipeline Mimarisi

Sistemde tahmini veya sentetik veri kullanılmaz; tüm grafikler doğrudan resmi kaynakların API ve veri tabanlarına bağlıdır.

```
                               VERİ AKIŞ ŞEMASI
+------------------+     +-------------------+     +--------------------+
| TCMB EVDS API    | --> |                   |     |                    |
+------------------+     |                   |     |                    |
| BDDK Bültenleri  | --> | Veri Temizleme,   | --> | 52 Zaman Serisi    |
+------------------+     | Senkronizasyon ve |     | Gösterge Matrisi   |
| TÜİK / Hazine    | --> | Ekonometrik Motor |     |                    |
+------------------+     |                   |     |                    |
| BIS / FRED / BIST| --> |                   |     |                    |
+------------------+     +-------------------+     +--------------------+
```

### 4.1. Veri Kaynakları

* **TCMB EVDS:** Rezervler, Analitik Bilanço, Likidite, Para Tabanı, REER, TÜFE/ÜFE, Swap Stoku.
* **BDDK Veri Tabanı:** Kredi/Mevduat hacmi, Takipteki Krediler (NPL), Yakın İzlemedeki Krediler (Stage 2), Yabancı Para Pozisyon Açığı.
* **Hazine ve Maliye Bakanlığı:** İç/Dış Borç Stoku, Borç Çevirme Oranları, İtfa Takvimi ($185 Mr $ Dış Borç Servisi bileşenleri).
* **BIST & Takasbank:** Para Piyasası Fonlama Hacmi, Yabancı Payı, CDS Primi.

### 4.2. Gösterge Kategorizasyonu (52 Parametre)

1. **Dış Kırılganlık & Rezerv (1-10):** Brüt Rezerv, Net Rezerv (Swap hariç), Kısa Vadeli Dış Borç Stoku, Cari Denge / GSYH, CDS (5 Yıllık), Dış Finansman İhtiyacı vb.
2. **Likidite, Para Politikası & Fonlama (11-20):** TCMB AOFM, Likidite Koridoru Alt/Üst Bantları, Açık Piyasa İşlemleri (APİ), Ters Repo / Depo hacimleri vb.
3. **Bankacılık & Kredi Dinamikleri (21-32):** Kredi Büyüme Hızı (13 haftalık kurdan arındırılmış), Kredi/Mevduat Oranı, Yüzdürülen Krediler (Stage 2), Hayalet Kredi Yükü, NPL Oranı.
4. **Enflasyon & Fiyatlama Davranışı (33-40):** Çekirdek TÜFE (C), İktisadi Yönelim Anketi Enflasyon Beklentileri, REER Sapması, ÜFE-TÜFE Makası.
5. **Reel Sektör & Güvensizlik (41-52):** Kapasite Kullanım Oranı, PMI, Güven Endeksleri, Gullini Güvensizlik Skoru, Acemoğlu Kurumsal Kalite Endeksi.

---

## 5. UI / UX ve İnteraktif Görselleştirme Şartnamesi

```
+-----------------------------------------------------------------------------------+
| T2SAIM KRİZ TAKİP MERKEZİ                                    [ 18 Kasım 2026 ]    |
| REZONANS TEPE NOKTASINA KALAN SÜRE: [ 88 Gün | 10 Saat | 07 Dk | 12 Sn ]         |
+-----------------------------------------------------------------------------------+
| [700 GÜNLÜK TÜM GENİŞLİK ZAMAN SERİSİ GRAFİĞİ]                                    |
| [ - | + ] Zoom Kontrolü | Çözünürlük: [Günlük] [Haftalık] [8 Kriz] [52 Gösterge]  |
|                                                                                   |
|  (Gerçek Veri Akışı: TCMB Likidite Koridoru + Net Rezerv + Hayalet Krediler)       |
|                                                                                   |
|  * Her veri noktası tıklanabilir: Detaylı kaynak dökümü ve filtreleme paneli      |
+-----------------------------------------------------------------------------------+
| [REER SARKAÇ GERİLİMİ VE AMİGDALA STRES YÜKÜ ($A_{\text{load}}$)]                 |
|                                                                                   |
|  Sol Eksen: REER Sarkaç Sapması (\theta) | Sağ Eksen: Amigdala Stres İndeksi     |
|  [Geçmiş Veri (Gerçek)] -------- [ŞU AN (Ağustos 2026)] ........ [Projeksiyon]   |
|                                                                                   |
|  UYARI BÖLGESİ: $A_{\text{load}} > 0.65$ ve \theta Dönüşü -> [SİSTEMİK ALARM]     |
+-----------------------------------------------------------------------------------+
| 52 MAKRO GÖSTERGE VE SİNYAL MATRİSİ (Sıralı Hiyerarşik Kartlar & Sparkline)       |
| +-------------------+ +--------------------+ +--------------------+ +-----------+ |
| | TCMB Swap Net Rez | | Hayalet Krediler   | | 185 Mr $ Dış Borç  | | Gullini   | |
| | -$42.1 Mr $ [RED] | | %11.8 (Yakın İzleme| | İtfa Tepe: Q4-2026 | | Güven:0.78| |
| +-------------------+ +--------------------+ +--------------------+ +-----------+ |
+-----------------------------------------------------------------------------------+
```

### 5.1. 700 Günlük Ana Grafik Bileşeni

* **Yerleşim:** Sayfanın tüm yatay genişliğini kaplar (100% Full-Width Container).
* **Zoom & Pan:** `+ / -` butonları ve mouse-wheel ile zaman ekseninde dinamik yakınlaşma/uzaklaşma.
* **Makro Kriz Katmanları (8+52 Modu):** Uzaklaşıldığında Türkiye'nin geçmiş 8 büyük kriz dönemi (1994, 2001, 2008, 2018, 2020 vb.) arka plan referans bantları olarak görünür.
* **Etkileşim (Drill-down):** Grafikteki herhangi bir seriye (ör. "Hayalet Krediler", "APİ Fonlaması") tıklandığında, altta verinin EVDS/BDDK ham kodlarını, son 10 yıllık dağılımını ve hesaplama metodolojisini açan modal panel.

### 5.2. REER Sarkacı vs. Amigdala Stres Yükü ($A_{\text{load}}$) Grafiği

* **Konum:** 700 günlük ana grafiğin hemen altında yer alan ikincil senkronize grafik.
* **Üçlü Faz Yapısı:**
1. *Geçmiş:* Gerçekleşen REER ve hesaplanan geçmiş $A_{\text{load}}$ serisi.
2. *Şu An (Ağustos 2026):* Mevcut sarkaç gerilim noktası ve anlık stres katsayısı.
3. *Projeksiyon (Model Tahmini):* $t^*$ (18 Kasım 2026) rezonans tepe noktasına giden dinamik simülasyon konisi.
* **Görsel Alarm Eşiği:** $A_{\text{load}} > 0.65$ bandı kırmızı taralı alan olarak vurgulanır.

---

## 6. Sisteme Eklenen İleri Seviye Bilimsel Modüller

Sayfanın rasyonel ve öngörü gücünü artırmak amacıyla mimariye eklenen analitik bileşenler:

```
+-----------------------------------------------------------------------------------+
|                     İLAVE İLERİ SEVİYE ANALİTİK BİLEŞENLER                        |
+-------------------------+-------------------------------+-------------------------+
| FAZ UZAYI YÖRÜNGESİ     | FİNANSAL BULAŞMA AĞI          | MONTE CARLO STRES       |
| (Phase Space Attractor) | (Network Contagion Graph)     | SİMÜLASYONU             |
| $(\theta, \dot{\theta})$| Bankalar ve reel sektör arası | Merton Jump-Diffusion   |
| Kaotik çekici analizi   | likidite şok yayılım matrisi  | ile $t^*$ olasılık dağı.|
+-------------------------+-------------------------------+-------------------------+
```

1. **Faz Uzayı Çekici Analizi (Phase Space Attractor):**
* REER sapması ($\theta$) ile değişim hızı ($\dot{\theta}$) faz uzayında 2D düzlemde çizilir. Sistemin stabil bir limit döngüsünde mi yoksa kaotik bir kriz çekicisine (chaotic attractor) mi girdiği takip edilir.

2. **Finansal Bulaşma Ağı (Interbank Network Contagion):**
* BDDK konsolide verileri üzerinden bankaların birbirlerine ve TCMB'ye olan bağımlılık matrisi (Ağ grafı) oluşturulur. Bir bankanın likidite sıkışıklığının tüm sisteme yayılma katsayısı hesaplanır.

3. **Merton Jump-Diffusion ile Monte Carlo Stres Testi:**
* Dış borç servisi ($185 Mr $) ve döviz kuru patikasında ani sıçramalar (jump process) modellenerek 18 Kasım 2026 eşiğinde sistemik kilitlenme olasılık dağılım eğrisi çıkarılır.

---

## 7. Geliştirme ve Uygulama Adımları (Roadmap)

1. **Faz 1 - Veri Entegrasyonu:** EVDS, BDDK ve Hazine API servislerinin kurulması; 52 serinin gerçek zamanlı ETL boru hattına bağlanması.
2. **Faz 2 - Matematik Motoru:** Diferansiyel borç denklemleri, kuple osilatörler ve $A_{\text{load}}$ algoritmalarının Python/FastAPI arka yüzünde analitik servise dönüştürülmesi.
3. **Faz 3 - Ön Yüz & Görselleştirme:** React / Tailwind / Highcharts (veya D3.js) mimarisiyle 700 günlük interaktif grafik, REER/Amigdala paneli ve geri sayım bileşeninin inşası.
4. **Faz 4 - Kalibrasyon:** Geçmiş kriz verileriyle (1994, 2001, 2018, 2021) model parametrelerinin ($\lambda_P, \lambda_S, \kappa, \gamma$) geriye dönük test edilmesi (Backtesting) ve doğrulanması.
