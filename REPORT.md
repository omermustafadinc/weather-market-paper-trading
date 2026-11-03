========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-03T17:55:06.490046Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         108414
  orderbook seviyesi     5785188
  tahmin snapshot          72135
  karar                    22404
  simüle fill               5790
  çözümlenmiş kova          2826

## Brier skoru  (düşük = iyi, 2742 kova)
  model                  0.1293
  piyasa (mid)           0.1253   n=2742
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0041  ±0.0029  %95 [-0.0098, +0.0017]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=396  0.1211 / 0.1974   fark +0.0763
    CHI   n=390  0.1381 / 0.1045   fark -0.0335
    DEN   n=396  0.1381 / 0.1895   fark +0.0514
    LAX   n=390  0.1199 / 0.0857   fark -0.0342
    MIA   n=390  0.1361 / 0.1027   fark -0.0334
    NY    n=390  0.1055 / 0.0903   fark -0.0152
    PHL   n=390  0.1466 / 0.1047   fark -0.0419
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1085         0.032         0.053   +0.020
  0.1-0.2       645         0.150         0.183   +0.033
  0.2-0.3       508         0.247         0.266   +0.019
  0.3-0.4       325         0.345         0.246   -0.099
  0.4-0.5       122         0.439         0.336   -0.103
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        11         0.633         0.545   -0.088
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5734)
  işlem sayısı                    5734
  kazanan                         2251  (%39)
  ort. İDDİA EDİLEN edge       +18.12p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.79p   ±0.5p  %95 [+0.7p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5859.86 $
  PnL fee ÖNCESİ             +48581.00 $
  PnL fee SONRASI            +42721.14 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14938.24 $   %90 aralık [-22621.09, -4447.69]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1253 (model 0.1293)

  bizim (fee sonrası)            +42721.14 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
