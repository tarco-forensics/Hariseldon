# Piyasalarda Duygu Tespiti: Kapsamlı Algoritmik ve Bilimsel Çerçeve
## Ekonofizik, Sosyofizik ve Hesaplamalı Finans Perspektifinden Tam Referans Rehberi

***

## Yönetici Özeti

Finansal piyasalarda duygu (emotion) ve duyarlılık (sentiment) tespiti, 2024–2026 döneminde hızla olgunlaşan bir interdisipliner alan haline gelmiştir. Geleneksel teknik analiz araçlarının ötesinde; Ekonofizik'ten gelen ölçekler arası analiz metodolojileri, Sosyofizik'ten gelen fikir dinamiği modelleri, NLP/LLM tabanlı metin analizi, Topolojik Veri Analizi (TDA) ve Ajan Tabanlı Modeller (ABM) artık birbirini tamamlayan bir ekosistem oluşturmaktadır. Bu rapor, piyasalarda duygu tespitine yönelik tüm ana yöntemleri — matematiksel formülleri, algoritmik şablonları ve güncel bilimsel gelişmeleri kapsayacak şekilde — sistematik olarak ele almaktadır.[^1][^2][^3]

***

## 1. Kavramsal Temel: Duygu — Duyarlılık — Gürültü Üçgeni

"Duygu" (emotion) ve "duyarlılık" (sentiment) finans literatüründe farklı seviyeleri tanımlar:[^4]

- **L1 Duygu (Micro-emotion):** Bireysel yatırımcının anlık psikolojik durumu (korku, açgözlülük, coşku). StockTwits, Twitter/X gibi platformlarda metin olarak tezahür eder.[^5][^6]
- **L3 Duyarlılık (Aggregate Sentiment):** Piyasa katılımcılarının kolektif duygu ortalaması; anket verileri, opsiyon oranları, volatilite endeksleri ile ölçülür.[^7][^8]
- **L6 Duygu Betası / Rejim:** Belirli bir hissenin piyasa duygusuna duyarlılığı. "Emotion Beta" kavramı 2024'te Hasan, Kumar ve Taffler tarafından resmileştirilmiştir.[^9][^10]
- **L7 Sistemik Duygu Yayılımı (Contagion):** Duyguların piyasalar arasında yayılma dinamiği; TVP-VAR, Transfer Entropi ve Ağ Teorisi ile ölçülür.[^3][^11]

***

## 2. KATEGORİ I: Piyasa Fiyat/Hacim Tabanlı Yöntemler

Bu yöntemler, herhangi bir metin verisine gerek duymadan sadece işlem verilerinden duygu sinyali üretir.

### 2.1 Volatilite Endeksleri (VIX ve Türevleri)

**VIX (CBOE Volatility Index)** tarihsel olarak en yaygın "korku ölçeri" konumundadır. S&P 500 opsiyon zımni volatilitesini 30 günlük ufukta ölçer. Matematiksel çekirdek:[^12][^7]

\[
\sigma_{VIX}^2 = \frac{2}{T} \sum_i \frac{\Delta K_i}{K_i^2} e^{rT} Q(K_i) - \frac{1}{T}\left(\frac{F}{K_0} - 1\right)^2
\]

Burada \(K_i\) kullanım fiyatı, \(Q(K_i)\) opsiyon bid-ask ortası, \(F\) vadeli fiyat, \(T\) vade süresidir. CNN Fear & Greed Index bu endeksi 7 bileşenden birisi olarak kullanır.[^13][^7]

**CNN Fear & Greed Index** — 7 bileşenden oluşan kompozit endeks:[^7][^12]
1. Market Momentum (S&P 500 vs. 125-günlük MA)
2. Hisse fiyat gücü (52-hafta yüksek/düşük oranı)
3. Hisse fiyat genişliği (McClellan Hacim Özeti)
4. Put/Call Opsiyon Oranı
5. Önemsiz Tahvil Talebi (junk bond spread)
6. Market Volatilitesi (VIX)
7. Güvenli Liman Talebi (hazine-hisse getiri farkı)

Her bileşen, kendi tarihsel ortalamasından sapması oranında ağırlıklandırılır; 0–100 arası bir skora normalize edilir. 2024 akademik araştırması, endeksin S&P 500, Nasdaq ve Russell 3000 getirilerini **Granger-nedensellik** testinde anlamlı biçimde öngördüğünü ortaya koymuştur.[^14][^7]

### 2.2 Put/Call Oranı ve Opsiyon Eğrisi Analizi

Put/call oranı piyasanın net hedge pozisyonunu gösterir:

\[
PCR = \frac{\text{Açık Put Hacmi}}{\text{Açık Call Hacmi}}
\]

\(PCR > 1\) bearish duygu baskısını, \(PCR < 0.7\) aşırı boğa optimizmini işaret eder. Zımni volatilite eğrisi (skew) de duygu asimetrisini yansıtır:

\[
\text{Vol Skew} = IV_{OTM\,Put} - IV_{ATM} - (IV_{ATM} - IV_{OTM\,Call})
\]

### 2.3 Hacim Anomalisi ve Order Flow Zehirliliği

Yüksek frekanslı piyasa mikroyapısı araştırmaları, "order flow toxicity"nin — bilgilendirilmiş tüccarların piyasaya girişinin — duygusal rejim değişimlerini öngörebildiğini göstermektedir. VPIN (Volume-Synchronized Probability of Informed Trading) metriği:[^15]

\[
VPIN = \frac{|V^B - V^S|}{V}
\]

Burada \(V^B\) ve \(V^S\) sırasıyla hacim-senkronize alım ve satım emirlerini, \(V\) toplam hacmi ifade eder. VPIN değerinin yükselmesi sistematik bilgi asimetrisine (informed trading) ve bu yolla panik/coşku konjonktürüne işaret eder.[^15]

***

## 3. KATEGORİ II: NLP / LLM Tabanlı Metin Duygu Analizi

### 3.1 Kural Tabanlı Sözlükler (Lexicon Methods)

Finans literatüründe iki temel sözlük öne çıkar:

- **Loughran-McDonald Word List:** Finansal 10-K/Q belgelerine özgü ~2,700 kelimelik pozitif/negatif/belirsizlik/litigasyon listesi.
- **Harvard General Inquirer:** Genel duygu sözlüğü; finansal metinlerde yanlış sınıflandırma oranı yüksektir.

Duygu skoru hesabı:

\[
S_t = \frac{N^+ - N^-}{N^+ + N^- + N^0}
\]

Burada \(N^+\), \(N^-\), \(N^0\) sırasıyla pozitif, negatif ve nötr kelime sayılarıdır.[^16][^4]

### 3.2 Makine Öğrenmesi Tabanlı Sınıflandırma

Klasik ML pipeline'ı:[^17][^18]

```
[Ham Metin] → Tokenizasyon → TF-IDF/CountVectorizer
→ Sınıflandırıcı (Random Forest / SVM / Gradient Boosting)
→ Sentiment Skoru (Pozitif / Negatif / Nötr)
```

IEEE 2024 çalışması, Random Forest sınıflandırıcısının %85.97 doğrulukla haber başlıklarından hisse fiyat yönü tahmin edebildiğini göstermiştir. NLP+ML entegrasyonunun F1 skoru ~0.85 seviyesine ulaşabildiği raporlanmaktadır.[^18][^17]

### 3.3 BERT ve FinBERT Modelleri

**FinBERT**, genel BERT mimarisinin finansal metinler üzerine (Financial PhraseBank, Bloomberg haberleri, SEC belgeleri) fine-tune edilmiş versiyonudur. Geleneksel ML yöntemlerini RMSE, MAE ve R² metriklerinde belirgin biçimde geride bıraktığı gösterilmiştir.[^19][^20][^21]

Transformer tabanlı sentiment sınıflandırması:

\[
P(y|x) = \text{softmax}(W \cdot h_{[CLS]} + b)
\]

Burada \(h_{[CLS]}\) BERT'in [CLS] token'ının gizli durumu, \(W\) ve \(b\) fine-tune edilen ağırlıklardır.

### 3.4 LLM Çağı: GPT-4, FinGPT ve Ötesi

2024 itibarıyla GPT-4o ile yapılan deneyler, few-shot prompt engineering ile FinBERT'e yakın ya da eşit performansın yakalanabildiğini ortaya koymuştur. Lopez-Lira & Tang (2023) çalışması, GPT-4'ün haber başlıklarını sınıflandırmada yaklaşık %90 günlük isabetlilik oranı elde ettiğini raporlamıştır.[^22][^23]

**FinGPT** (AI4Finance Foundation) açık kaynaklı bir finansal LLM framework'üdür. Kullanım mimarisi:[^24]

```
Veri Kaynakları (Haberler, Forumlar, SEC Belgeleri)
      ↓
LLM Fine-tuning (LoRA ile verimli adaptasyon)
      ↓
Sentiment Çıktısı (Skaler veya olasılık dağılımı)
      ↓
Trading Sinyali Üretimi
```

### 3.5 Target-Based Financial Sentiment Analysis (TBFSA)

2025 yılında LLM'lerin hedef-odaklı sentiment analizindeki performansı sistematik biçimde kıyaslanmıştır. TBFSA, genel piyasa duygusu yerine belirli bir şirket/varlık hakkındaki duyguyu ayırt eder; bu da gürültüye karşı sinyal oranını önemli ölçüde iyileştirir.[^25][^26]

### 3.6 EmTract: Sosyal Medyadan 7 Boyutlu Duygu Çıkarımı

**EmTract** (Vamossy & Skog), finansal sosyal medyaya (StockTwits) özel geliştirilmiş açık kaynaklı araçtır. DistilBERT mimarisi üzerine inşa edilmiş; emoji/emotikon gibi sosyal medya öğelerini gömme uzayına dahil etmiştir. Her metin için 7 duygu durumu üretir:[^27][^6][^5]

> Nötr | Mutlu | Üzgün | Öfkeli | Tiksinti | Sürpriz | **Korku**

Bu boyutların, özellikle "korku" sinyalinin, günlük fiyat hareketlerini anlamlı biçimde öngörülebildiği gösterilmiştir.[^28][^5]

***

## 4. KATEGORİ III: Duygu Betası ve Piyasa Duygu Endeksi (2024–2025 Yeni Bulgular)

### 4.1 Emotion Beta Modeli

Hasan, Kumar ve Taffler (2024–2025), piyasa düzeyinde bir **Duygu Endeksi** oluşturmuş ve her şirket için bu endekse duyarlılığı ölçen "emotion beta" kavramını tanımlamıştır:[^10][^9]

\[
R_{i,t} = \alpha_i + \beta_i^{emotion} \cdot \Delta EI_t + \gamma_i \cdot X_t + \varepsilon_{i,t}
\]

Burada \(\Delta EI_t\) duygu endeksindeki değişim, \(X_t\) kontrol değişkenleri (Fama-French faktörleri, likidite vb.) vektörüdür. Yüksek emotion beta'lı hisselere uzun, düşük emotion beta'lılara kısa pozisyon açan strateji yıllıklandırılmış **%6+** alfa üretmiştir. Bu fiyat farklılığı yaklaşık 6 ay içinde kapanmaktadır.[^9][^10]

### 4.2 TVP-VAR ile Duygu Bağlantısallığı

**TVP-VAR (Time-Varying Parameter Vector Autoregression)**, duygu-fiyat ilişkisinin zamanda nasıl değiştiğini modellemek için standart araç haline gelmiştir. Temel model:[^29][^30][^3]

\[
y_t = c_t + B_{1,t} y_{t-1} + \ldots + B_{p,t} y_{t-p} + u_t
\]

\[
u_t \sim N(0, \Sigma_t)
\]

Burada \(y_t\) piyasa getirisi, volatilite ve duygu değişkenlerinden oluşan vektör, \(B_{k,t}\) zaman-değişken parametre matrislerdir. Stokastik volatilite (TVP-VAR-SV) eklentisiyle model daha sağlam hale getirilmektedir.[^30]

2025 çalışması 6 farklı piyasa türünde (hisse, tahvil, emtia, özel sermaye, gayrimenkul, kripto) TVP-VAR ile duygusal yayılımı analiz etmiş; korkunu güçlü bir kataliz olarak, kripto piyasasının ise sürekli olarak açgözlülüğün başlıca yayıcısı olduğunu ortaya koymuştur.[^3]

***

## 5. KATEGORİ IV: EKONOFİZİK YÖNTEMLERİ

Ekonofizik, istatistiksel mekanik ve karmaşıklık biliminin araçlarını finansal piyasalara uygulamaktadır. Duygu tespitindeki rolü, fiyat serisinin istatistiksel özelliklerinden psikolojik rejimler çıkarmak üzerine kuruludur.

### 5.1 Multifraktal Ayrıştırılmış Dalgalanma Analizi (MFDFA)

MFDFA, finansal zaman serilerinin fraktal özelliklerini çok ölçekli biçimde ölçer. Duygu tespiti açısından kritik içgörü: piyasa **panik/coşku rejimlerinde** multifraktal spektrumun daraldığı, spektral genişliğin \(\Delta\alpha = \alpha_{max} - \alpha_{min}\) metriğinin düştüğü gözlemlenmiştir.[^31][^32][^33]

Algoritma adımları:
1. Zaman serisini sıfır-ortalıklı birikmeli toplamına çevir: \(Y(i) = \sum_{t=1}^{i} [x_t - \langle x \rangle]\)
2. \(s\) büyüklüğünde örtüşmeyen \(N_s\) penceresine böl
3. Her pencere için \(\nu\) dereceli polinom ile de-trend et, varyans hesapla: \(F^2(s,\nu)\)
4. \(q\)-düzenlü dalgalanma fonksiyonu:

\[
F_q(s) = \left\{ \frac{1}{2N_s} \sum_{\nu=1}^{2N_s} [F^2(s,\nu)]^{q/2} \right\}^{1/q}
\]

5. Genelleştirilmiş Hurst üssü: \(F_q(s) \sim s^{h(q)}\)
6. Multifraktal spektrum: \(f(\alpha) = q \cdot \alpha - \tau(q)\)

**DA-MFDFA (Double Asymmetric MFDFA)** en güncel (2025) uzantısıdır — işlem hacmini dış asimetri değişkeni olarak multifraktal çerçeveye entegre eder, böylece güçlü boğa/ayı trendlerinde ayrı multifraktal imzalar çıkarılabilir.[^32]

### 5.2 Tsallis Entropisi ve Genişletilmiş İstatistiksel Mekanik

Standart Boltzmann-Gibbs entropisi finansal serilerin ağır kuyruk (fat-tail) davranışını yeterince yakalayamaz. **Tsallis entropisi** q-parametresi ile genişletilmiş bir çerçeve sunar:[^34][^35]

\[
S_q = \frac{1 - \sum_i p_i^q}{q - 1}
\]

\(q \rightarrow 1\) limitinde standart Shannon entropiye döner. Piyasada **aşırı korku veya coşku dönemlerinde** \(q > 1\) olması (süperdiffüzif davranış) karakteristiktir; böylece Tsallis parametresi dolaylı bir duygu rejimine işaret eder.

### 5.3 Tekrarlama Nicemleme Analizi (RQA — Recurrence Quantification Analysis)

RQA, zaman serisinin faz uzayında kendi kendine ne ölçüde döndüğünü nicel olarak saptar. Duygusal rejim değişimleri faz uzayının yapısını bozar.[^36][^37][^38]

Tekrarlama matrisi:

\[
R_{ij}(\varepsilon) = \Theta(\varepsilon - \| \mathbf{v}(i) - \mathbf{v}(j) \|), \quad i,j = 1,\ldots,N
\]

Temel RQA metrikleri:
- **RR (Recurrence Rate):** Toplam tekrarlama oranı; düşüş → kaos/panik.
- **DET (Determinism):** Çapraz çizgi uzunluğu oranı; düşüş → rastgele, gürültü baskın duygu.
- **ENT (Entropy):** Çapraz çizgi dağılımının Shannon entropisi; zirve → karmaşıklık.
- **LAM (Laminarity):** Dikey çizgi yapısı; artış → piyasanın "askıda kalması" (liquidity freeze).

BIST50 intraday verileri (Borsa İstanbul, 2019–2020) üzerinde yapılan çalışma, RQA metriklerinin gün-içi volatilite ile istatistiksel olarak anlamlı ilişki taşıdığını göstermiştir.[^37]

### 5.4 Hawkes Süreci (Self-Exciting Point Process)

**Hawkes süreci**, piyasadaki emir akışının kendi kendini hızlandıran (self-exciting) doğasını yakalar. Duygu patlamaları — panik satışı, FOMO alımı — tipik olarak Hawkes yoğunluk fonksiyonunun aniden yükselmesiyle eşleşir:[^39][^40]

\[
\lambda(t) = \mu + \sum_{t_i < t} \phi(t - t_i) = \mu + \sum_{t_i < t} \alpha \, e^{-\beta(t - t_i)}
\]

Burada \(\mu\) arka plan yoğunluğu, \(\alpha\) heyecan katsayısı (branching ratio), \(\beta\) sönüm hızıdır. Kritik eşik: \(n = \alpha/\beta < 1\) durağanlığı, \(n \rightarrow 1\) piyasa krizini (tam-ateşleme) işaret eder.[^41][^40][^39]

***

## 6. KATEGORİ V: SOSYOFİZİK YÖNTEMLERİ

### 6.1 Ising Modeli ve Fikir Dinamiği

**Ising modeli** başlangıçta manyetik spin sistemleri için geliştirilmiş olsa da yatırımcı görüşlerini binary durumlar (al=+1, sat=−1) olarak modellemede geniş uygulama alanı bulmuştur. Hamiltonyen:[^42][^43][^44]

\[
H = -J \sum_{\langle i,j \rangle} s_i s_j - h \sum_i s_i
\]

Burada \(J > 0\) komşular arası uyum eğilimi (sürü davranışı), \(h\) dışsal bilgi alanı (haber akışı), \(s_i \in \{-1, +1\}\) yatırımcı \(i\)'nin kararıdır. **Faz geçişleri** piyasa rejim değişimlerini temsil eder; kritik sıcaklık \(T_c\)'ye yakın bölge maksimum duygu volatilitesine karşılık gelir.[^43][^44]

Spin glass varyantları heterojen bağlantı yapısını modellemekte daha başarılıdır; 2026 yayını Ising ve spin glass yaklaşımlarını BRICS piyasalarındaki finansal bağımlılık için karşılaştırmıştır.[^42]

### 6.2 Ajan Tabanlı Modeller (ABM) ve Sürü Davranışı

ABM'ler piyasa dinamiklerini "aşağıdan yukarıya" üretir: her ajan kendi kural setine sahiptir ve kolektif sürü davranışı ortaya çıkar. 2026 yılında yayımlanan çalışma, sosyal medya ortamını simüle eden ABM'lerin bilişsel yanlılıkları, duygusal tepkileri ve sürü davranışını otomatik olarak ürettiğini göstermiştir.[^45][^46][^47]

Temel ajan karar kuralı:

\[
P_i(\text{al}) = \sigma\left( w_f F_i + w_c C_i + w_s S_i \right)
\]

Burada \(F_i\) fundamentalist sinyal, \(C_i\) chartist/teknik sinyal, \(S_i\) sosyal/sürü sinyali, \(w\) ağırlıklar ve \(\sigma\) sigmoid fonksiyonudur. Kirman (1993) modelinden türeyen sürü modelleri; Gilli-Winker, Alfarano-Lux-Wagner ve Franke-Westerhoff versiyonlarıyla 24 borsa endeksinde karşılaştırılmış, en iyisinin ARCH-tipi süreçlerle rekabet edebildiği sonucuna varılmıştır.[^46]

### 6.3 Ağ Teorisi ve Duygu Yayılımı (Contagion Networks)

Sosyofizik perspektifinden piyasalar arası duygu yayılımı, ağ analizi ile modellenebilir. Cardiff PhD tezi (Wu), duygu yayılım ağları ile volatilite risk bulaşma ağlarının özelliklerini birleştirerek özgün bir "ağ tabanlı duygu endeksi" önermiştir.[^48][^49]

Ağ-tabanlı duygu yoğunluk metrikleri:
- **Degree centrality:** En çok "duygu alıp-veren" düğümler/piyasalar
- **Net Connectedness (FROM / TO):** Her varlığın net duygu alıcısı mı vericisi mi olduğu
- **Total Connectedness Index (TCI):** Sistemin genel duygu bağlantısallık düzeyi[^50]

**Quantile connectedness** yaklaşımı, bağlantısallığın aşırı korku/açgözlülük dönemlerinde (dağılımın alt/üst kuyrukları) nasıl değiştiğini asimetrik biçimde ölçer.[^51][^3]

***

## 7. KATEGORİ VI: TRANSFER ENTROPİSİ VE BİLGİ AKIŞ ANALİZİ

**Transfer entropisi (TE)**, Granger nedenselliğinin doğrusal varsayımından bağımsız, bilgi teorik bir yöntemdir:[^11][^52][^51]

\[
T_{X \to Y}(\tau) = \sum p(y_{t+\tau}, y_t^{(k)}, x_t^{(l)}) \log \frac{p(y_{t+\tau} | y_t^{(k)}, x_t^{(l)})}{p(y_{t+\tau} | y_t^{(k)})}
\]

Burada \(y_t^{(k)}\) ve \(x_t^{(l)}\) k ve l gecikmeli tarih vektörleri, \(\tau\) öngörü ufkudur. TE değerinin sıfırdan anlamlı biçimde sapması, \(X\)'teki duygu/bilginin \(Y\)'nin fiyatını tahmin etmede kullanışlı olduğunu gösterir.

2022 Physica A çalışması, hisse ve kripto piyasaları arasında duygu-fiyat bilgi akışını incelemiş; Transfer Entropi'nin geleneksel VAR yöntemlerini geride bıraktığını kanıtlamıştır. 2026 SSRN çalışması TE'yi ağ teorisiyle birleştirerek duygu yayılım yoğunluğunu nicel olarak ölçmüştür.[^53][^11]

***

## 8. KATEGORİ VII: TOPOLOJİK VERİ ANALİZİ (TDA)

**TDA**, finansal zaman serilerini geometrik/topolojik yapılar olarak inceler ve geleneksel istatistiksel yöntemlerin gözden kaçırdığı örüntüleri tespit eder.[^54][^55][^56]

### 8.1 Kalıcı Homoloji (Persistent Homology)

Fiyat serisinden elde edilen nokta bulutu üzerinde, filtrasyon parametresi \(\varepsilon\) büyüdükçe topolojik özellikler (bağlı bileşenler, döngüler) doğar ve yok olur. Bu "yaşam süreleri" kalıcılık diyagramında gösterilir.

Zaman serisi delay embedding:

\[
\mathbf{v}(t) = (x_t, x_{t+\tau}, \ldots, x_{t+(m-1)\tau}) \in \mathbb{R}^m
\]

Nokta bulutu \(\{\mathbf{v}(t)\}\) üzerinde **Vietoris-Rips kompleksi** inşa edilir. Kalıcılık betti sayıları \(\beta_0\), \(\beta_1\) piyasanın "topolojik karmaşıklığını" ölçer.

2025 yılında borsada çöküş öncesi erken uyarı sinyalleri olarak kalıcılık normlarının kullanılabildiği gösterilmiştir — sistem kararsızlığını ölçmede kritik geçişleri andıran bir indikatör işlevi görür. TDA'nın piyasa rejimlerini (boğa/ayı) ayırt etmede Borsa İstanbul dahil birden fazla piyasada test edildiği raporlanmıştır.[^56][^57][^58]

***

## 9. KATEGORİ VIII: DERİN ÖĞRENME TABANLI YAKLAŞIMLAR

### 9.1 Limit Emir Defteri (LOB) Transformer

**LiT (Limit Order Book Transformer)**, LOB verisinden kısa vadeli piyasa hareketlerini tahmin eden derin mimaridir. Uzamsal (fiyat seviyesi) ve zamansal (sıra) bağımlılıkları birlikte modeller; geleneksel CNN tabanlı DeepLOB modellerini geride bırakmaktadır.[^59]

### 9.2 Duygu-Farkındalıklı Pekiştirmeli Öğrenme (SentARL)

**SentARL (Sentiment-Aware Reinforcement Learning)** duygu sinyallerini state vektörüne dahil eden bir RL alım-satım sistemidir:[^60][^61][^62]

\[
s_t = [\text{fiyat özellikleri}_t, \text{sentiment özellikleri}_{t-k:t}]
\]

\[
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha [r_t + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t)]
\]

2025 FinAI Contest sonuçları, duygu-geliştirilmiş RL ajanlarının temel RL ajanlarını belirgin biçimde geride bıraktığını doğrulamıştır.[^62]

### 9.3 Çok Kipli (Multimodal) Duygu Analizi

2025 SSRN çalışması, S&P 500 varlıklarının günlük duygu endekslerini metin, emoji ve görüntü (StockTwits görselleri) verilerini birleştirerek oluşturmuş; görüntü tabanlı duygu endekslerinin geleneksel metin tabanlı kontrollerden bile güçlü ön-görü sağladığını ortaya koymuştur. Bu bulgular gerçekçi görsellerin karikatür tarzı içeriklere kıyasla daha güçlü duygu tepkisi oluşturduğunu da göstermektedir.[^28]

***

## 10. KATEGORİ IX: KRİPTO ÖZEL DUYGU TEKNOLOJİLERİ

Kripto piyasaları için duygu tespit araçları kısmen farklı bileşenler kullanır:[^63][^64][^65]

**Crypto Fear & Greed Index** bileşenleri:
1. Volatilite (mevcut vs. 30/90 gün ortalaması)
2. Market Momentum/Hacim
3. Sosyal Medya (X'te hashtag analizi)
4. Anketler (haftalık trader anketleri)
5. Bitcoin Dominansı
6. Google Trends (arama sorgularının duygusal tonu)

**On-chain metrikler** (kripto özgün):
- **NUPL (Net Unrealized Profit/Loss):** Piyasanın ortalama al-sat kararındaki duygu rejimini gösterir
- **MVRV Z-score:** Piyasa değeri / gerçekleşmiş değer Z skoru; aşırı coşku/panik tespiti için kritik
- **Funding Rate (Perpetual futures):** Uzun/kısa pozisyon taşıma maliyeti; negatif değerler panik, aşırı pozitif değerler FOMO işaret eder

***

## 11. ENTEGRE MULTİMODAL ÇERÇEVE: Nasıl Birleştirilir?

### 11.1 Katmanlı Mimari

```
KATMAN 1: Ham Veri Akışları
├── Fiyat/Hacim verisi (tick-by-tick veya OHLCV)
├── Limit emir defteri (Level 2)
├── Haber başlıkları ve analist raporları
├── Sosyal medya (X, Reddit, StockTwits, Telegram)
└── On-chain (kripto için)

KATMAN 2: Özellik Çıkarımı
├── Teknik: VIX, PCR, VPIN, Hacim Z-skoru
├── NLP/LLM: FinBERT, EmTract, GPT-4o, FinGPT
├── Ekonofizik: MFDFA Hurst üssü, Tsallis q, RQA metrikleri
└── Ağ/Topoloji: Ağ bağlantısallığı, TDA kalıcılık normları

KATMAN 3: Birleşik Duygu Endeksi
├── Ağırlıklı ortalama veya ensemble (stacking)
└── TVP-VAR / Transfer Entropi ile zamansal dinamik

KATMAN 4: Rejim Etiketi + Sinyal Üretimi
├── Duygu rejim sınıflandırması (panik / nötr / coşku)
└── Trading sinyali veya risk uyarısı
```

### 11.2 Duygu Gürültüsü vs. Sinyal Ayrımı için Basit Python Şablonu

```python
import numpy as np

def emotion_noise_score(price_series, volume_series, sentiment_series, 
                         lookback=20, z_thresh=2.0, rv_thresh=3.0):
    """
    Duygu gürültüsü skoru hesapla.
    Returns: dict with component scores and composite noise index
    """
    # 1. Volatilite Z-skoru
    returns = np.diff(np.log(price_series))
    realized_vol = np.std(returns[-lookback:])
    hist_vol_mean = np.mean([np.std(returns[i:i+lookback]) 
                              for i in range(len(returns)-lookback)])
    hist_vol_std = np.std([np.std(returns[i:i+lookback]) 
                            for i in range(len(returns)-lookback)])
    vol_z = (realized_vol - hist_vol_mean) / (hist_vol_std + 1e-8)
    
    # 2. Hacim spike oranı
    rv = volume_series[-1] / np.mean(volume_series[-lookback-1:-1])
    
    # 3. Mean-reversion testi (ortalamaya dönüş)
    future_return = np.sum(returns[-5:])  # 5 günlük kümülatif getiri
    extreme_return = np.sum(returns[-lookback:-5])
    mean_revert = -np.sign(extreme_return) == np.sign(future_return)
    
    # 4. Sentiment ani spike
    sent_z = (sentiment_series[-1] - np.mean(sentiment_series[-lookback:])) \
             / (np.std(sentiment_series[-lookback:]) + 1e-8)
    
    # Bileşik gürültü skoru (0-1 arası)
    noise = 0.0
    if abs(vol_z) > z_thresh: noise += 0.3
    if rv > rv_thresh: noise += 0.25
    if mean_revert: noise += 0.25
    if abs(sent_z) > z_thresh: noise += 0.2
    
    return {
        "vol_z_score": vol_z,
        "volume_spike_ratio": rv,
        "mean_reversion_signal": mean_revert,
        "sentiment_z_score": sent_z,
        "composite_noise_index": min(noise, 1.0)
    }
```

***

## 12. KARŞILAŞTIRMA MATRİSİ

| Yöntem | Katman | Veri Tipi | Zaman Ölçeği | Yorumlanabilirlik | Hesap Maliyeti | 2024–2026 Güncellik |
|--------|--------|-----------|--------------|------------------|----------------|----------------------|
| VIX / Fear-Greed | L3 | Fiyat/Opsiyon | Günlük | Yüksek | Düşük | Köklü; araştırma devam ediyor[^7][^14] |
| FinBERT/LLM | L1–L3 | Metin | Dakika–Günlük | Orta | Yüksek | Aktif; GPT-4o 2024[^20][^22] |
| EmTract | L1 | Sosyal Medya | Günlük | Yüksek | Orta | Yayımlanan 2024/2025[^66][^5] |
| Emotion Beta | L6 | Fiyat+Metin | Günlük | Yüksek | Orta | Yeni; Hasan et al. 2024[^9][^10] |
| TVP-VAR | L6–L7 | Fiyat+Duygu | Haftalık+ | Orta | Orta | Aktif standart[^3][^29] |
| Transfer Entropi | L7 | Fiyat+Duygu | Günlük+ | Orta | Orta | 2022–2026 yoğun[^11][^53] |
| MFDFA / DA-MFDFA | L3 | Fiyat | Çok Ölçekli | Düşük | Orta | 2025 yeni uzantı[^32][^33] |
| Tsallis Entropisi | L3 | Fiyat | Çok Ölçekli | Düşük | Düşük | Referans yöntem[^34] |
| RQA | L3 | Fiyat | Gün-içi+ | Orta | Düşük | BIST uygulaması[^37] |
| Ising / ABM | L7 | Simülasyon | Tatil bağımsız | Düşük | Yüksek | 2026 yayın[^43][^47] |
| Hawkes Süreci | L3 | Emir Akışı | Milisaniye | Orta | Orta | HFT standart[^39][^40] |
| TDA (Pers. Homoloji) | L3–L7 | Fiyat | Çok Ölçekli | Düşük | Yüksek | 2024–2025 büyüme[^56][^57] |
| RL+Sentiment | L6 | Fiyat+Metin | Gerçek-zaman | Düşük | Çok Yüksek | 2025 FinAI[^62] |
| Ağ Teorisi | L7 | Korelasyon | Günlük+ | Orta | Orta | Aktif[^48][^49] |

***

## 13. HAKİKAT TABLОSU (Veritas Per Se Protokolü)

### Verified (Doğrulanmış)
- VIX ve CNN Fear & Greed Index, S&P 500 getirilerini Granger-nedensellik testinde anlamlı biçimde öngörmektedir (2011–2024 verisi).[^14]
- FinBERT ve domain-specific LLM'ler, RMSE/MAE/R² metriklerinde geleneksel ML ve sözlük yöntemlerini geride bırakmaktadır.[^20]
- EmTract'ın DistilBERT tabanlı 7-sınıf duygu çıkarımı, mevcut açık kaynak sınıflandırıcıları arasında en yüksek performansı sergilemektedir.[^5]
- Emotion Beta konsepti ile yüksek emotion beta'lı hisselerden oluşan portföy, 6 aylık düzeltme dönemiyle yıllık %6+ alfa üretmiştir.[^10][^9]
- TVP-VAR ile 6 piyasa türünde duygu yayılımı incelenmiş; korku güçlü bir katalizör, kripto ise ana açgözlülük yayıcısı olarak belirlenmiştir.[^3]
- DA-MFDFA (2025), işlem hacmini dış asimetri değişkeni olarak entegre eden ilk multifraktal uzantıdır.[^32]
- TDA kalıcılık normları, piyasa çöküşleri öncesinde erken uyarı sinyali üretebilmektedir.[^57][^56]
- RQA metrikleri, BIST50 verisiyle gün-içi volatilite ile anlamlı ilişki göstermiştir.[^37]
- Görüntü tabanlı duygu endeksleri, metin/emoji kontrollerine rağmen S&P 500 günlük getirilerini anlamlı ölçüde tahmin etmektedir.[^28]

### Assumed (Varsayılan)
- MFDFA ve Tsallis entropisi çıktılarının sistematik biçimde bir birleşik duygu endeksine entegre edilmesi teorik olarak mümkün; ancak literatürde tam operasyonel bir uygulama henüz sınırlı sayıdadır.
- Hawkes süreci parametresi \(n = \alpha/\beta\)'nın 1'e yaklaşmasının piyasa krizlerini önceden işaret ettiği varsayımı, ampirik çalışmalarla desteklenmekle birlikte her piyasa için genelleştirilmesi dikkat gerektirir.
- Multimodal (metin + görüntü + fiyat) birleşiminin her piyasada ve her zaman ufkunda tutarlı alfa ürettiği varsayımı doğrulanmaya devam etmektedir.

### Unverified (Doğrulanamayan)
- BIST gibi gelişmekte olan piyasalarda sosyal medya kaynaklı duygu sinyalinin fiyat varyansına toplam katkısına dair kesin nicel tahmin mevcut değildir.
- Ağ tabanlı duygu endeksleri (TDA veya ağ teorisi) ile gerçek zamanlı ticaret sinyali üretiminin net Sharpe iyileştirmesi bağımsız çalışmalarla henüz geniş ölçüde doğrulanmamıştır.
- Ising/ABM modellerinin gerçek HFT ortamlarında duygu gürültüsünü ne ölçüde önceden tespit edebildiği belirsizliğini korumaktadır.

---

## References

1. [A Paradigm Shift in Computational Finance](https://papers.ssrn.com/sol3/Delivery.cfm/9a61787e-b378-4d00-9df7-5f19278d852d-MECA.pdf?abstractid=5641713&mirid=1) - Section 2.3 explores how market sentiment, rooted in behavioural finance, enhances stock price predi...

2. [Investor Emotions and Asset Prices](https://papers.ssrn.com/sol3/Delivery.cfm/5020654.pdf?abstractid=5020654&mirid=1) - We develop a new emotion-based market-level sentiment indicator to measure the emotional state of th...

3. [Emotional Echoes: Unraveling the Emotional Dynamics Among Global Financial Markets](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5243240) - This study explores the role of emotions, specifically fear and greed, in the interconnectedness of ...

4. [Financial Sentiment Analysis: Techniques and Applications](https://dl.acm.org/doi/full/10.1145/3649451) - This article defines a clearer scope for FSA studies and conceptualizes the FSA-investor sentiment-m...

5. [EmTract: Investor Emotions and Market Behavior](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3975884) - Using EmTract, we explore the relationship between investor emotions expressed on social media and a...

6. [EmTract: Extracting Emotions from Social Media Text ...](https://github.com/dvamossy/EmTract) - EmTract is a tool that extracts emotions from social media text. It incorporates key aspects of soci...

7. [Fear and Greed Index - Investor Sentiment](https://www.cnn.com/markets/fear-and-greed) - CNN's Fear & Greed Index is a way to gauge stock market movements and whether stocks are fairly pric...

8. [The CNN Fear and Greed Index as a predictor of US equity ...](https://www.sciencedirect.com/science/article/abs/pii/S1544612324015216) - This paper assesses the ability of the CNN Fear and Greed Index to predict the returns of asset clas...

9. [Investor Emotions and Asset Prices](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5020654) - Abstract. We develop a new emotion-based market-level sentiment indicator to measure the emotional s...

10. [Investor emotions and asset prices](https://centaur.reading.ac.uk/122581/) - A trading strategy that takes a Long (Short) position in high- (low-) emotion beta stocks generates ...

11. [Sentiment spillover and price dynamics: Information flow in ...](https://www.sciencedirect.com/science/article/abs/pii/S0378437122000747) - Transfer Entropy outperforms traditional VAR methods. This study examines the sentiment–returns rela...

12. [What is CNN's Fear and Greed Index, and how does it work?](https://www.cnn.com/2025/04/07/business/what-is-cnn-fear-and-greed-index) - It is wise for investors 'to be fearful when others are greedy and to be greedy only when others are...

13. [How CNN's Fear & Greed Index Impacts Investor Sentiment](https://www.investopedia.com/terms/f/fear-and-greed-index.asp) - Key Takeaways. The Fear & Greed Index tracks emotional drivers in stock market prices. Composed of s...

14. [The Cnn Fear and Greed Index as a Predictor of Us Equity ...](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4912111) - We assess whether the CNN “Fear and Greed” Index can be used to predict returns on equity indices an...

15. [Market Microstructure: Insights Gained from High- ...](https://www.linkedin.com/pulse/market-microstructure-insights-gained-from-data-lisa-d-majmin-phd--lfuof) - One key area of focus in high-frequency data analytics is the study of order flow toxicity, which re...

16. [Financial News Sentiment Analysis Using NLP and Machine ...](https://vfast.org/journals/index.php/VTSE/article/view/2165) - Forecasting market movements in stocks, gold, and crude oil requires a deep understanding of how fin...

17. [Utilizing Sentiment Analysis and Machine Learning to Forecast Stock Price Changes from Financial News](https://ieeexplore.ieee.org/document/10961794/)

18. [NLP and ML for real-time sentiment analysis in Finance](https://ieeexplore.ieee.org/document/10763733/)

19. [Large language models in finance : what is financial ...](https://arxiv.org/pdf/2503.03612.pdf) - We examine how BERT-based models, such as RoBERTa and FinBERT, are optimized for structured sentimen...

20. [Financial News Sentiment Analysis and Market ...](https://www.gbspress.com/index.php/JCSSR/article/view/473) - This study investigates the application of large language models (LLMs) to financial news sentiment ...

21. [LLM (large language models) in finance](https://sci-bot.ru/llm-large-language-models-in-fcb2) - FinBERT has been shown to significantly outperform generic BERT on financial sentiment analysis task...

22. [Financial Sentiment Analysis on News and Reports Using Large Language Models and FinBERT](https://arxiv.org/abs/2410.01987) - Financial sentiment analysis (FSA) is crucial for evaluating market sentiment and making well-inform...

23. [Can LLMs Beat FinBERT for Stock Sentiment Trading?](https://tommijohnsen.substack.com/p/can-llms-beat-finbert-for-stock-sentiment) - Lopez-Lira and Tang (2023) found GPT-4 achieves roughly 90% portfolio day hit rates for classifying ...

24. [FinGPT: Open-Source Financial Large Language Models ...](https://github.com/AI4Finance-Foundation/FinGPT) - FinGPT is an open-source financial large language model project developed and maintained by the AI4F...

25. [Benchmarking Large Language Models for Target-Based ...](https://aclanthology.org/2025.clicit-1.74.pdf) - This study advances target-based financial sentiment analysis (TBFSA) by rigorously evaluating the e...

26. [Benchmarking Large Language Models for Target-Based ...](https://clic2025.unica.it/wp-content/uploads/2025/09/73_main_long.pdf) - This study advances target-based financial sentiment analysis (TBFSA) by rigorously evaluating the e...

27. [EmTract: Extracting Emotions from Social Media](https://arxiv.org/abs/2112.03868) - We develop an open-source tool (EmTract) that extracts emotions from social media text tailed for fi...

28. [investor emotions and stock returns - Enlighten Theses](https://theses.gla.ac.uk/id/eprint/84857) - The findings suggest that image-based emotion indices are robust predictors of stock market returns,...

29. [Novel findings from TVP-VAR-SV technique](https://www.sciencedirect.com/science/article/pii/S2110701725000010) - We are the first to create a sentiment index for investors in Vietnamese stock market. •. We use a T...

30. [Novel findings from TVP-VAR-SV technique](https://ideas.repec.org/a/eee/inteco/v181y2025ics2110701725000010.html) - Our article employs a time-varying parameter structural vector autoregression (TVP-VAR) with stochas...

31. [THE EFFECT OF MULTIFRACTAL DETRENDED ...](https://repofeb.undip.ac.id/13776/) - By examining these aspects, the research aims to gain insights into weak and semi- strong form effic...

32. [Double asymmetric multifractal detrended fluctuation ...](https://www.sciencedirect.com/science/article/abs/pii/S037843712500679X) - This paper introduces Double Asymmetric Multifractal Detrended Fluctuation Analysis (DA-MFDFA), a no...

33. [Stock Market Efficiency of the BRICS Countries Pre-, During](https://ideas.repec.org/a/kap/compec/v65y2025i3d10.1007_s10614-024-10607-3.html) - In this study, we applied the multifractal detrended fluctuation analysis model to compare the multi...

34. [Entropy-Based portfolio optimization under Varma–Tsallis ...](https://www.sciencedirect.com/science/article/abs/pii/S106294082600001X) - In this paper, we propose a novel entropic portfolio model inspired by Cover's universal portfolio f...

35. [Rui Menezes](https://ideas.repec.org/f/pme337.html) - "Stock market volatility: An approach based on Tsallis entropy," Papers 0809.4570, arXiv.org. Andrei...

36. [Recurrence Quantification Analysis of Financial Markets](https://www.irma-international.org/viewtitle/70883/?isxn=9781466625099)

37. [Intraday Seasonality and Volatility Pattern: An Explanation with Recurrence Quantification Analysis](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4400054) - The Recurrence Quantification Analysis (RQA), a pattern recognition-based time series analysis metho...

38. [Recurrence quantification analysis of global stock markets](https://cemapre.iseg.ulisboa.pt/archive/preprints/417.pdf)

39. [Price Impact of Large Orders Using Hawkes Processes](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3368618_code1916836.pdf?abstractid=2874042&mirid=1) - We will investigate large-order impact when market prices are modelled as a linear combination of se...

40. [Forecasting high frequency order flow imbalance using ...](https://arxiv.org/html/2408.03594v1) - This paper uses Hawkes processes to estimate the OFI while accounting for the lagged dependence in t...

41. [Rakeshks7/hawkes-process-hft-microstructure: A ...](https://github.com/Rakeshks7/hawkes-process-hft-microstructure) - A high-performance implementation of univariate Hawkes Processes for modeling self-exciting order fl...

42. [Sociophysics models inspired by the Ising model](https://ouci.dntb.gov.ua/en/works/lxLvw0y2/) - This paper analyzes financial market interdependence from a statistical-physics perspective by compa...

43. [Sociophysics models inspired by the Ising model](https://arxiv.org/html/2506.23837v1) - In this review, we explore how Ising and Ising-like models have been successfully adapted to socioph...

44. [Ising-Type Opinion Dynamics](https://www.emergentmind.com/topics/ising-type-opinion-dynamics) - Ising-type opinion dynamics are models that map binary opinions to spin states, offering a framework...

45. [Exploring Herding Behavior in financial markets using ...](https://www.linkedin.com/pulse/exploring-herding-behavior-financial-market-using-modeling-pardesi) - The aim of this article is to explore a model of herding behavior and to simulate herding behavior i...

46. [Direct comparison of agent-based models of herding in ...](https://kar.kent.ac.uk/58181/) - The present paper tests a new model comparison methodology by comparing multiple calibrations of thr...

47. [Agent-Based modeling in financial markets](https://www.aimspress.com/article/doi/10.3934/nhm.2026043?viewType=HTML) - Agents interact through a simulated social-media environment, and the model generates cognitive bias...

48. [Network-based Approaches in Modelling Financial Contagion](https://orca.cardiff.ac.uk/id/eprint/187016/1/FanWu_PhDThesis_Finalv.pdf) - We take the properties from the sentiment spillover networks and the volatility risk contagion netwo...

49. [Reviewing Literature on Financial Contagion: Bibliometric ...](https://journals.sagepub.com/doi/10.1177/09711023261438301) - They concluded that financial contagion dilutes the diversification advantages of digital currencies...

50. [A TVP-VAR modeling and dynamic system-wise analysis](https://www.ijirss.com/index.php/ijirss/article/view/7512) - This study investigates the interconnectedness among maritime companies, gold, and Bitcoin markets u...

51. [Assessing causal relationships between cryptocurrencies ...](https://ideas.repec.org/a/eee/finlet/v50y2022ics1544612322005293.html) - "Using transfer entropy to measure information flows between financial markets," Studies in Nonlinea...

52. [Tail Risk Spillover Between Global Stock Markets Based on ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC12110966/) - Compared with other measures of information entropy, transfer entropy describes the direction in whi...

53. [Do News and Social Media Tell the Same Story? ...](https://arxiv.org/html/2604.26811v2) - In this study, we combine the transfer entropy modelling technique with network theory to quantify t...

54. [Enhancing financial time series forecasting through ...](https://d-nb.info/1370140673/34) - TDA, employing persistent homology, introduces a new approach to examining financial markets [12]. I...

55. [Using Topology to Create Alpha in Financial Markets](https://www.linkedin.com/pulse/using-topology-create-alpha-financial-markets-singh-cqf-nit-jsr-kiwcc) - This paper explores the application of topological data analysis (TDA) to identify and exploit persi...

56. [Why topological data analysis detects financial bubbles?](https://www.sciencedirect.com/science/article/abs/pii/S1007570423005865) - We present a heuristic argument for the propensity of Topological Data Analysis (TDA) to detect earl...

57. [Topological Time Series Analysis of Market Crashes](https://dl.acm.org/doi/full/10.1145/3745533.3745634) - Norms of Persistent Homology, introduced in topological data analysis, are indicators of system inst...

58. [exploring applications of topological data analysis in stock ...](https://arxiv.org/html/2411.13881v1) - Using topological data analysis (TDA) and persistent homology to analyze the stock markets in Singap...

59. [LiT: limit order book transformer](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1616485/full) - In this work, we introduce Limit Order Book Transformer (LiT), a novel deep learning architecture fo...

60. [A Sentiment-Aware Reinforcement Learning Approach](https://arxiv.org/abs/2112.02095) - We propose the Sentiment-Aware RL (SentARL) intelligent trading system that improves profit stabilit...

61. [Cracking Alpha in 2025: Sentiment, AI, and a Market Gone ...](https://www.linkedin.com/pulse/cracking-alpha-2025-sentiment-ai-market-gone-rogue-jessica-mcdonald-xdcne) - Picture 2025's financial markets as a runaway train—geopolitical squabbles, supply chain snarls, and...

62. [FinAI-Trader: Sentiment-Enhanced Reinforcement ...](https://www.computer.org/csdl/proceedings-article/cscloud/2025/878100a358/2c7r6Rvv5ra) - The work provides a comprehensive benchmark for FinAI Contest 2025 Task 1, showing that sentiment-en...

63. [March 2025: Crypto Fear & Greed Index](https://trustwallet.com/blog/cryptocurrency/march-2025-crypto-fear-greed-index) - The Crypto Fear & Greed Index is a widely-used tool that measures market sentiment on a scale from 0...

64. [Crypto Fear and Greed Index: Live Market Sentiment](https://delta.app/en/fear-greed-index) - This index analyzes key factors like market volatility, trading volume, and social media trends to r...

65. [Evolution of the research of cryptocurrency, social media ...](https://www.sciencedirect.com/science/article/pii/S105905602600523X) - The study outlines the developmental trajectories of the research on cryptocurrencies and social med...

66. [EmTract: Extracting emotions from social media](https://ideas.repec.org/a/eee/finana/v97y2025ics1057521924007014.html) - Downloadable (with restrictions)! We developed EmTract, an open-source tool designed to extract inve...

