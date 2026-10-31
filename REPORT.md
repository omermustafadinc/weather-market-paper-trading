========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-31T09:24:08.707165Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         104382
  orderbook seviyesi     5572775
  tahmin snapshot          69363
  karar                    21564
  simüle fill               5580
  çözümlenmiş kova          2688

## Brier skoru  (düşük = iyi, 2604 kova)
  model                  0.1301
  piyasa (mid)           0.1259   n=2604
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0042  ±0.0030  %95 [-0.0100, +0.0016]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=372  0.1217 / 0.1988   fark +0.0770
    CHI   n=372  0.1397 / 0.1051   fark -0.0346
    DEN   n=372  0.1398 / 0.1902   fark +0.0504
    LAX   n=372  0.1204 / 0.0880   fark -0.0324
    MIA   n=372  0.1355 / 0.1027   fark -0.0328
    NY    n=372  0.1071 / 0.0915   fark -0.0156
    PHL   n=372  0.1465 / 0.1050   fark -0.0415
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1021         0.032         0.054   +0.021
  0.1-0.2       619         0.150         0.187   +0.038
  0.2-0.3       491         0.247         0.263   +0.016
  0.3-0.4       306         0.345         0.235   -0.110
  0.4-0.5       116         0.439         0.336   -0.103
  0.5-0.6        37         0.547         0.351   -0.196
  0.6-0.7         9         0.637         0.556   -0.082
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5497)
  işlem sayısı                    5497
  kazanan                         2152  (%39)
  ort. İDDİA EDİLEN edge       +18.20p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.75p   ±0.6p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5633.69 $
  PnL fee ÖNCESİ             +44923.99 $
  PnL fee SONRASI            +39290.30 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14012.16 $   %90 aralık [-21839.56, -5602.02]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1259 (model 0.1301)

  bizim (fee sonrası)            +39290.30 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
