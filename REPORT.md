========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-31T15:25:53.457694Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         104718
  orderbook seviyesi     5590721
  tahmin snapshot          69615
  karar                    21648
  simüle fill               5600
  çözümlenmiş kova          2700

## Brier skoru  (düşük = iyi, 2616 kova)
  model                  0.1300
  piyasa (mid)           0.1258   n=2616
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0041  ±0.0030  %95 [-0.0100, +0.0017]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=378  0.1212 / 0.1966   fark +0.0754
    CHI   n=372  0.1397 / 0.1051   fark -0.0346
    DEN   n=378  0.1395 / 0.1899   fark +0.0504
    LAX   n=372  0.1204 / 0.0880   fark -0.0324
    MIA   n=372  0.1355 / 0.1027   fark -0.0328
    NY    n=372  0.1071 / 0.0915   fark -0.0156
    PHL   n=372  0.1465 / 0.1050   fark -0.0415
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1025         0.032         0.054   +0.021
  0.1-0.2       622         0.150         0.186   +0.037
  0.2-0.3       495         0.247         0.263   +0.016
  0.3-0.4       307         0.346         0.238   -0.108
  0.4-0.5       116         0.439         0.336   -0.103
  0.5-0.6        37         0.547         0.351   -0.196
  0.6-0.7         9         0.637         0.556   -0.082
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5509)
  işlem sayısı                    5509
  kazanan                         2156  (%39)
  ort. İDDİA EDİLEN edge       +18.19p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.76p   ±0.6p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5645.01 $
  PnL fee ÖNCESİ             +45321.91 $
  PnL fee SONRASI            +39676.90 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13730.95 $   %90 aralık [-22962.55, -3565.45]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1258 (model 0.1300)

  bizim (fee sonrası)            +39676.90 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
