========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-02T02:55:21.230034Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         107070
  orderbook seviyesi     5715404
  tahmin snapshot          71127
  karar                    22152
  simüle fill               5728
  çözümlenmiş kova          2772

## Brier skoru  (düşük = iyi, 2688 kova)
  model                  0.1296
  piyasa (mid)           0.1251   n=2688
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0044  ±0.0029  %95 [-0.0102, +0.0013]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=384  0.1209 / 0.1967   fark +0.0758
    CHI   n=384  0.1389 / 0.1056   fark -0.0333
    DEN   n=384  0.1404 / 0.1900   fark +0.0496
    LAX   n=384  0.1197 / 0.0865   fark -0.0332
    MIA   n=384  0.1352 / 0.1010   fark -0.0342
    NY    n=384  0.1055 / 0.0906   fark -0.0149
    PHL   n=384  0.1465 / 0.1055   fark -0.0410
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1061         0.032         0.053   +0.020
  0.1-0.2       634         0.150         0.186   +0.036
  0.2-0.3       501         0.247         0.261   +0.015
  0.3-0.4       319         0.345         0.245   -0.101
  0.4-0.5       118         0.439         0.339   -0.100
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7         9         0.637         0.556   -0.082
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5665)
  işlem sayısı                    5665
  kazanan                         2230  (%39)
  ort. İDDİA EDİLEN edge       +18.16p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.84p   ±0.5p  %95 [+0.8p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5790.74 $
  PnL fee ÖNCESİ             +47276.01 $
  PnL fee SONRASI            +41485.27 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14774.10 $   %90 aralık [-24240.57, -6360.62]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1251 (model 0.1296)

  bizim (fee sonrası)            +41485.27 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
