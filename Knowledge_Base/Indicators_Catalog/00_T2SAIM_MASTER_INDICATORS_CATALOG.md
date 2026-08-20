# 🏛️ T2SAIM BÜTÜNLEŞİK KRİZ & MAKRO-FİNANS İNDİKATÖR KATALOĞU (MASTER RAG ENCYCLOPEDIA)
**Proje:** T2SAIM / Hari Seldon Kriz Takip, Erken Uyarı ve Karar Destek Sistemi  
**Metodoloji:** Epistemik Hijyen, Diferansiyel Ekonofizik, Nörofinans ve Ajan Tabanlı Dinamikler  
**Sürüm:** v3.0 (Master Unified Edition)  
**Mühür Tarihi:** 2026-08-21  

---

## 🎯 GİRİŞ VE SİSTEM MİMARİSİ
Bu katalog; T2SAIM kriz tahmin motorumuzun halihazırda kullandığı **33 aktif matematiksel formülü** ve küresel literatürden (OECD, BIS, IMF, Wharton, Fed, Springer) sisteme entegre edilen **yeni nesil makro-ihtiyati göstergeleri** içermektedir.

Her gösterge; **kesin matematiksel formülü, teorik iktisadi temeli, kritik alarm eşikleri, veri kaynakları ve T2SAIM katman eşleşmesi** ile tam dokümante edilmiştir.

---

## 📑 BÖLÜM 1: AKTİF ÇALIŞAN T2SAIM İNDİKATÖRLERİ (6 KATMAN - 33 FORMÜL)

### 🧠 KATMAN 1: NÖROFİNANS VE BİLİŞSEL AMİGDALA YÜKÜ

#### 1.1 Amigdala Korku ve Tehdit Yükü ($A_{\text{load}}$)
* **Formül:**
  $$A_{\text{load}}(t) = \sigma\left(k_1 \cdot \text{Vol}_{FX}(t) + k_2 \cdot |\Delta \text{CDS}(t)| + k_3 \cdot Z_{\text{EFMI}}(t) - \theta_{\text{threat}}\right)$$
  $$\sigma(x) = \frac{1}{1 + e^{-x}}$$
* **Açıklama:** Piyasadaki aşırı volatilite, CDS sıçraması ve ahlaki söylem anomalilerinin (EFMI) karar alıcıların limbik sisteminde (Amigdala) yarattığı Sistem 1 panik reaksiyonunu modeller.
* **Eşik Değeri:** $A_{\text{load}} > 0.65 \implies$ Panik Faz Geçişi (Rasyonel Analiz Devre Dışı).
* **Veri Kaynağı:** Kapalıçarşı kur oynaklığı, 5Y CDS, Resmî Gazete metin analizi.

#### 1.2 Prefrontal Korteks Rasyonel Kontrolü ($\text{PFC}_{\text{control}}$)
* **Formül:**
  $$\text{PFC}_{\text{control}}(t) = 1 - \frac{1}{1 + \exp(-\kappa (A_{\text{load}}(t) - 0.50))}$$
* **Açıklama:** Amigdala yükü arttıkça prefrontal korteksin mantıksal fren mekanizmasının çöküş hızını (10 saniyelik analitik düşünceden 0.1 saniyelik kaçış refleksine geçişi) ölçer.
* **Eşik Değeri:** $\text{PFC} < 0.35 \implies$ Rasyonel politika felci.

#### 1.3 Mevduat ve Fiziki Varlık Kaçış Hızı ($v_{\text{run}}$)
* **Formül:**
  $$v_{\text{run}}(t) = v_0 \cdot \exp\left(\gamma \cdot A_{\text{load}}(t) + \delta \cdot \Delta P_{\text{fiziki}}(t)\right)$$
* **Açıklama:** Hanehalkı ve KOBİ'lerin banka mevduatından nakde, kasaya, Kapalıçarşı fiziki altına ve DTH'a kaçış ivmesini hesaplar.
* **Eşik Değeri:** $v_{\text{run}} > 0.70 \implies$ Bankacılık likidite çekilme riski.

#### 1.4 Yapısal ve Kurumsal Çürüme Katsayısı ($TR\text{-}DEI$)
* **Formül:**
  $$TR\text{-}DEI = 0.71 \quad \implies \quad \text{Stres Artırıcı Çarpan} = \left(\frac{TR\text{-}DEI}{0.60}\right)^{1.5} \approx 1.15$$
* **Açıklama:** Kurumsal erozyonun ve liyakat kaybının sisteme gelen her dışsal şoku %15 asimetrik tırmandırma katsayısıdır (Sıkışmış Yay Prensibi).

---

### 🏦 KATMAN 2: BANKACILIK ALM VE LİKİDİTE SIKIŞMASI

#### 2.1 Bankacılık Kırılganlık İndeksi ($BFI$)
* **Formül:**
  $$BFI(t) = w_1 \cdot \frac{LDR(t)}{LDR_{\text{crit}}} + w_2 \cdot \frac{\text{Spread}_{\text{GLP}}(t)}{\text{Spread}_{\text{norm}}} + w_3 \cdot \frac{NPL_{\text{real}}(t)}{NPL_{\text{resmi}}(t)}$$
* **Açıklama:** Bankacılık sektörünün kredi/mevduat sıkışması, fonlama faiz makası ve gizlenen batık kredi yükünün bileşik bileşenidir.
* **Eşik Değeri:** $BFI > 0.70 \implies$ Kredi kanalı donması (Credit Crunch).

#### 2.2 Kredi / Mevduat Oranı ($LDR$)
* **Formül:**
  $$LDR(t) = \frac{\sum \text{Toplam Krediler}(t)}{\sum \text{Toplam Mevduat}(t)}$$
* **Eşik Değeri:** $LDR > 1.15 \implies$ Bankaların mevduatla kredileri fonlayamaması, dış borca ve TCMB likiditesine bağımlılık.

#### 2.3 Hayalet Krediler ve Gerçek Batık Oranı ($NPL_{\text{real}}$)
* **Formül:**
  $$NPL_{\text{real}}(t) = NPL_{\text{resmi}}(t) + \delta_{\text{forbearance}} \cdot \frac{\text{Krediler}_{\text{Grup 2}}(t)}{\text{Toplam Krediler}(t)}$$
* **Açıklama:** Resmî NPL (%1.8) ile yüzdürülen (Evergreening) 2. grup yakın izlemedeki batıkların toplam fiili yüküdür ($NPL_{\text{real}} \approx \%9.4$).

#### 2.4 TCMB GLP / AOFM Örtük Fonlama Makası
* **Formül:**
  $$\text{Spread}_{\text{funding}}(t) = \text{AOFM}(t) - \text{Politika Faizi (1 Hafta Repo)}(t)$$
* **Açıklama:** Merkez Bankası'nın politika faizini değiştirmeden Geç Likidite Penceresi (GLP) ve gecelik borç verme ile piyasayı örtük sıkılaştırma derecesi.
* **Kritik Eşik:** Makas $> \%4.0$.

#### 2.5 Kısa Vadeli Dış Borç Servisi Baskısı ($DSR_{\text{ext}}$)
* **Formül:**
  $$DSR_{\text{ext}}(t) = \frac{\text{12 Aylık Kısa Vadeli Dış Borç (185 Mr \$)}}{\text{Net Rezervler (Swap Hariç)} + \text{Cari Gelirler}}$$
* **Açıklama:** Ani Duruş (Sudden Stop) anında döviz likiditesi kilitlenme katsayısıdır.

---

### ⚖️ KATMAN 3: AHLAKİ SAPMA VE SÖYLEM ANOMALİSİ ($EFMI$)

#### 3.1 Epistemik Adli Ahlaki Gösterge ($EFMI$)
* **Formül:**
  $$EFMI(t) = \frac{\sum_{i=1}^n w_i \cdot \left|\text{Resmî Söylem}_i(t) - \text{Fiili Piyasa Eylemi}_i(t)\right|}{\text{Doğrulanabilir Fiziksel Veri}}$$
* **Açıklama:** Yöneticilerin ve regülatörlerin beyanatları ile piyasa icraatları arasındaki tutarsızlığı ve ahlaki tehlikeyi (Moral Hazard) ölçer.

#### 3.2 Tarihsel $Z$-Skor Söylem Sapması ($Z_{\text{EFMI}}$)
* **Formül:**
  $$Z_{\text{EFMI}}(t) = \frac{EFMI(t) - \mu_{1260}}{\sigma_{1260}}$$
* **Açıklama:** Son 5 yıllık (1260 iş günü) hareketli ortalama ve standart sapmaya göre söylem anomalisi.
* **Eşik:** $Z > 1.25\sigma \implies$ Güven erozyonu başlangıcı.

---

### 🌐 KATMAN 4: SOSYOFİZİK VE REZONANS MOTORU

#### 4.1 Ising Spin Kolektif İnanç Modeli
* **Formül:**
  $$m(t+1) = \tanh\left(\beta \left(J \cdot m(t) + h(t)\right)\right)$$
  $$\beta = \frac{1}{T_{\text{belirsizlik}}}$$
* **Açıklama:** Toplumdaki panik/güven kutuplaşmasının ajanlar arası etkileşimle kendiliğinden hizalanması ($m \to -1$ çöküş, $m \to +1$ coşku).

#### 4.2 Amnesia Bellek Sönümlenme Diferansiyeli ($M(t)$)
* **Formül:**
  $$M(t) = M(t-1) \cdot (1 - \lambda) + \text{Shock}(t), \quad \lambda = 0.15$$
  $$M(t) = \min(M(t), 5.00)$$
* **Açıklama:** Kriz hafızasının zamanla unutulma hızını modeller. Üst üste şoklarda bellek tavana (5.00) vurur ve sistem yüksek alarmda kilitli kalır.

#### 4.3 Sistemik Rezonans İndeksi ($SRI$)
* **Formül:**
  $$SRI(t) = \sqrt[3]{A_{\text{load}}(t) \cdot BFI(t) \cdot \max(0.01, Z_{\text{EFMI}}(t))}$$
* **Açıklama:** Nörolojik stres, bankacılık tıkanması ve ahlaki sapmanın aynı frekansta çakışarak genlik patlaması yaratması.

---

### 📈 KATMAN 5: MAKRO-FİNANS VE SIKIŞMIŞ YAY DİNAMİĞİ

#### 5.1 Reel Efektif Döviz Kuru Sarkacı ($REER_{\text{pendulum}}$)
* **Formül:**
  $$\text{Sarkaç}(t) = REER(t) - REER_{\text{denge}} (65.0)$$
* **Açıklama:** Sıcak para girişiyle TL'nin aşırı değerlenmesi ($REER > 70$) dış ticaret açığını patlatır; sarkaç geri döndüğünde sert kur düzeltmesi üretir.

#### 5.2 Kapalıçarşı Fiziki Kur Makası (Tahtakale Arbitrajı)
* **Formül:**
  $$\Delta P_{\text{fiziki}}(t) = \frac{P_{\text{Kapalıçarşı}}(t) - P_{\text{Bankalararası}}(t)}{P_{\text{Bankalararası}}(t)} \times 100$$
* **Eşik:** $\Delta P > \%2.5 \implies$ Finansal sistemden fiziki teslimata kaçış alarmı.

---

### 🚨 KATMAN 6: BÜTÜNLEŞİK KRİZ İNDEKSİ ($CI$) VE L6 FAZ KİLİDİ

#### 6.1 Periyodik Kriz İndeksi ($CI$)
* **Formül:**
  $$CI(t) = 0.30 \cdot SRI(t) + 0.25 \cdot BFI(t) + 0.20 \cdot A_{\text{load}}(t) + 0.15 \cdot \left(\frac{\Delta P_{\text{fiziki}}(t)}{5.0}\right) + 0.10 \cdot \left(\frac{M(t)}{5.0}\right)$$

#### 6.2 L6 Faz Kilidi (Lock-In Matrix)
* **Karar Kuralı:**
  $$\text{Durum} = \begin{cases} 
  \text{🔴 KRİZ ALARM}, & CI(t) > 0.65 \lor (SRI(t) \ge 0.50 \land Z_{\text{EFMI}}(t) \ge 0.50) \\
  \text{🟡 TEDİRGİN}, & CI(t) > 0.45 \\
  \text{✅ NORMAL}, & \text{Aksi halde}
  \end{cases}$$

---

## 🔮 BÖLÜM 2: YENİ ENTEGRE EDİLEN KÜRESEL İNDİKATÖRLER (EXPANSION SET)

### 🏛️ 7. BASEL III & BIS GÖSTERGELERİ

#### 7.1 Basel III Kredi / GSYİH Açığı (Credit-to-GDP Gap)
* **Formül:**
  $$\text{CreditGap}_t = \left(\frac{\text{Credit}_t}{\text{GDP}_t}\right) - \text{HP}_{\lambda=400.000}\left(\frac{\text{Credit}}{\text{GDP}}\right)$$
* **Eşik:** $\text{Açık} > \%2.0 - \%10.0 \implies$ Döngüsel Sermaye Tamponu ($CCB$) zorunluluğu tetiklenir.
* **Erken Uyarı Ufku:** 2 - 3 Yıl.

#### 7.2 BIS Borç Servisi Oranı (Debt Service Ratio - DSR)
* **Formül:**
  $$DSR_t = \frac{i_t \cdot D_t}{1 - (1 + i_t)^{-s_t}} \cdot \frac{1}{Y_t}$$
* **Açıklama:** Gelire oranla anapara ve faiz ödeme yükü 20 yıllık trendden saptığında bankacılık krizini 1-2 yıl önceden haber verir.

---

### 🌐 8. IMF & MAKRO-İHTİYATİ GÖSTERGELER

#### 8.1 IMF Risk Altındaki Büyüme (Growth-at-Risk - GaR)
* **Formül:**
  $$Q_{\tau}(\Delta y_{t+h} | \mathcal{F}_t) = \alpha_{\tau} + \beta_{\tau} \cdot \text{NFCI}_t + \gamma_{\tau} \cdot \Delta y_t, \quad \tau = 0.05$$
* **Açıklama:** Finansal koşullar sıkılaştığında önümüzdeki 4 çeyrekteki en kötü %5'lik sol kuyruk GSYİH daralma senaryosunu olasılık dağılımıyla hesaplar.

#### 8.2 Avrupa Merkez Bankası CLIFS (Finansal Stres İndeksi)
* **Formül:**
  $$CLIFS_t = \mathbf{s}_t' \cdot \mathbf{C}_t \cdot \mathbf{s}_t = \sum_{i=1}^N \sum_{j=1}^N c_{ij,t} \cdot s_{i,t} \cdot s_{j,t}$$
* **Bileşenler:** Banka hisse volatilitesi, interbank faiz makası, CDS primleri ve döviz kuru oynaklığı.

---

### 📊 9. WHARTON, OECD VE FED GÖSTERGELERİ

#### 9.1 Wharton / Baumohl Getiri Eğrisi Eğim İndeksi (Yield Curve Spread - YCS)
* **Formül:**
  $$YCS(t) = R_{10Y}(t) - R_{2Y}(t)$$
* **Kural:** $YCS < 0 \implies$ Ters dönmüş getiri eğrisi; 6-18 ay içinde resesyon olasılığı %90+.

#### 9.2 OECD Bileşik Öncü Göstergeler (Composite Leading Indicators - CLI)
* **Formül:**
  $$CLI(t) = \sum_{j=1}^k \omega_j \cdot \tilde{X}_j(t)$$
* **Açıklama:** Sanayi siparişleri, tüketici güveni, para arzı ve hisse senedi endekslerinin normalize edilmiş döngüsel bileşeni.

#### 9.3 Minsky Parabolik Borç Servisi İvmesi ($S_S(t)$)
* **Formül:**
  $$S_D(t) = \delta_D \cdot (t - t_0) \quad \text{vs.} \quad S_S(t) = \frac{1}{2} \delta_S \delta_D \cdot (t - t_0)^2$$
* **Kritik Eşik:** $S_S(t^*) > S_D(t^*) \implies$ Borç servisi borçlanmayı aştığı an sınırsız likidite kriz fazı başlar.

---

## 🗄️ BÖLÜM 3: RAG ENTEGRASYON VE ÇAPRAZ REFERANS ŞEMASI

```
+---------------------------------------------------------------------------------------------------+
| T2SAIM HİYERARŞİK KRİZ RADARI ZAMAN ÇİZELGESİ                                                     |
+-------------------+-----------------------------------+-------------------------------------------+
| Zaman Ufku        | İndikatör / Katman                | Referans Kaynak                          |
+-------------------+-----------------------------------+-------------------------------------------+
| 2 - 3 Yıl Önce    | Basel III Credit-to-GDP Gap       | BIS / Basel Protokolleri                  |
| 1 - 2 Yıl Önce    | DSR & 185 Mr $ Dış Borç Servisi   | Chacko & Evans (Fed) / TCMB               |
| 6 - 12 Ay Önce    | Getiri Eğrisi (YCS) & OECD CLI    | Baumohl (Wharton) / OECD                  |
| 1 - 2 Çeyrek Önce | Hayalet Kredi & CLIFS             | Gullini (Japonya Analizi) / BDDK          |
| 0 - 30 Gün (Tepe) | Amigdala (A_load) & Tahtakale     | T2SAIM Özgün Doktrini / Kapalıçarşı       |
+-------------------+-----------------------------------+-------------------------------------------+
```

Bu katalog; sistemik risklerin önceden tespit edilmesi, modellenmesi ve algoritmik olarak izlenmesi için T2SAIM'in operasyonel kütüphanesine mühürlenmiştir.
