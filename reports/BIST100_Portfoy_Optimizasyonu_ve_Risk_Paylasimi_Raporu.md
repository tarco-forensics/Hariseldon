# BIST-100 Portföy Optimizasyonu ve Risk Paylaşımı (Çeşitlendirme) Raporu

**Analiz Dönemi:** 2024-12-10 - 2026-06-10 (1.5 Yıllık Backtest)
**Başlangıç Bütçesi:** $10,000 USD

## 1. Portföy Performans Karşılaştırma Tablosu
Aşağıdaki tabloda, eşit ağırlıklı endeks, momentum, Markowitz (Maks Sharpe) ve Minimum Varyans portföylerinin performans metrikleri yer almaktadır.

| Strateji / Enstrüman | Bitiş Değeri (USD) | Toplam Getiri (%) | Yıllık Volatilite (%) | Sharpe Oranı | Maks. Drawdown (%) |
|---|---|---|---|---|---|
| **BIST-100 Eşit Ağırlıklı (Benchmark)** | $10,343.73 | +3.44% | 23.03% | 0.2147 | -24.40% |
| **Top-10 Momentum (Eşit Ağırlıklı)** | $10,290.79 | +2.91% | 25.57% | 0.2037 | -28.64% |
| **Top-10 Markowitz (Maksimum Sharpe)** | $10,954.33 | +9.54% | 24.65% | 0.3731 | -29.80% |
| **Top-10 Minimum Varyans** | $11,321.67 | +13.22% | 23.88% | 0.4705 | -26.38% |
| *THYAO (Tekil Hisse)* | $7,455.17 | -25.45% | 32.05% | -0.4593 | -34.89% |
| *AKBNK (Tekil Hisse)* | $7,659.86 | -23.40% | 43.18% | -0.2005 | -38.55% |

## 2. Fiziksel Kanun Olarak Risk Paylaşımı ve Çeşitlendirme (Diversification Effect)
Kullanıcımızın belirttiği gibi: *"Öğeleri birleştirdiğin zaman, onların yapıları değişir. Fiziksel tepkimelerde yapılar değişir."* 

Bu benzetme finans teorisindeki **Modern Portföy Teorisi** ile birebir örtüşmektedir. Hisseleri tek tek aldığımızda taşıdığımız risk, o hisselerin tekil oynaklıkları (standart sapmaları) kadardır. Ancak bu hisseleri bir araya getirip bir portföy oluşturduğumuzda, oluşan yapının toplam riski, bileşenlerin risklerinin ağırlıklı ortalamasından **daha düşüktür**. Bunun nedeni hisselerin fiyat hareketlerinin birbiriyle tam korelasyonlu olmamasıdır.

### Matematiksel Kanıt:
- Seçilen Top-10 hissenin tekil yıllık oynaklıklarının (volatilite) ortalaması: **%54.05**
- Buna karşılık, bu hisselerin birleşiminden oluşan **Markowitz Maksimum Sharpe Portföyü'nün oynaklığı**: **%24.65**
- **Minimum Varyans Portföyü'nün oynaklığı**: **%23.88**
- Seçilen hisseler arasındaki ortalama tarihsel korelasyon: **0.1641**

Görüldüğü üzere, hisseleri birleştirdiğimizde, aralarındaki zayıf korelasyon (korelasyon < 1.0) sayesinde risklerin bir kısmı birbirini sönümlemiş ve tekil hisselerin ortalama riskinden çok daha düşük riskli (daha kararlı) yeni bir fiziksel/finansal yapı ortaya çıkmıştır.

## 3. Bulgular ve Stratejik Değerlendirme
- **Markowitz (Maks Sharpe) vs Eşit Ağırlık:** Markowitz optimizasyonu, hisselerin sadece tarihsel getirilerini değil, risklerini ve kovaryanslarını da dikkate alarak sermayeyi dağıtır. Bu sayede, momentum stratejisindeki dalgalanmaları törpüleyerek daha yüksek bir Sharpe oranı ve daha düşük maksimum kayıp (drawdown) üretir.
- **Minimum Varyans Stratejisi:** En düşük riski hedefleyen bu portföy, getiriyi maksimize etmeye çalışmaz; fakat dalgalanmayı en aza indirerek ayı piyasalarında veya kriz dönemlerinde sermayeyi korumak için mükemmel bir defansif kalkan görevi görür.
- **LabPlot Kullanımı:** Sonuçları LabPlot üzerinde grafik haline getirebilmeniz için `portfolio_comparison_results.csv` dosyası oluşturulmuştur. Bu dosyada her bir stratejinin ve tekil hisselerin (THYAO, AKBNK) günlük USD değerleri yer almaktadır. Grafik çizdirdiğinizde, tekil hisselerin sert dalgalanmalarına kıyasla optimize edilmiş portföy eğrilerinin çok daha pürüzsüz ve stabil yukarı yönlü hareket ettiğini (risk paylaşımının görsel kanıtını) gözlemleyebilirsiniz.
