========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-02T20:27:48.610805Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         107574
  orderbook seviyesi     5742166
  tahmin snapshot          71631
  karar                    22236
  simüle fill               5748
  çözümlenmiş kova          2784

## Brier skoru  (düşük = iyi, 2700 kova)
  model                  0.1295
  piyasa (mid)           0.1255   n=2700
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0040  ±0.0029  %95 [-0.0098, +0.0018]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=390  0.1209 / 0.1969   fark +0.0760
    CHI   n=384  0.1389 / 0.1056   fark -0.0333
    DEN   n=390  0.1395 / 0.1900   fark +0.0505
    LAX   n=384  0.1197 / 0.0865   fark -0.0332
    MIA   n=384  0.1352 / 0.1010   fark -0.0342
    NY    n=384  0.1055 / 0.0906   fark -0.0149
    PHL   n=384  0.1465 / 0.1055   fark -0.0410
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1065         0.032         0.053   +0.020
  0.1-0.2       638         0.150         0.185   +0.035
  0.2-0.3       503         0.247         0.262   +0.015
  0.3-0.4       321         0.345         0.246   -0.099
  0.4-0.5       118         0.439         0.339   -0.100
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7         9         0.637         0.556   -0.082
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5677)
  işlem sayısı                    5677
  kazanan                         2237  (%39)
  ort. İDDİA EDİLEN edge       +18.16p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.91p   ±0.5p  %95 [+0.8p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5804.57 $
  PnL fee ÖNCESİ             +48682.34 $
  PnL fee SONRASI            +42877.77 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14686.17 $   %90 aralık [-24492.37, -4869.75]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1255 (model 0.1295)

  bizim (fee sonrası)            +42877.77 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
