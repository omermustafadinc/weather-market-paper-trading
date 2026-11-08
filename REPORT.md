========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-08T22:32:03.165955Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         114870
  orderbook seviyesi     6111496
  tahmin snapshot          76545
  karar                    23784
  simüle fill               6142
  çözümlenmiş kova          3054

## Brier skoru  (düşük = iyi, 2970 kova)
  model                  0.1305
  piyasa (mid)           0.1247   n=2970
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0058  ±0.0028  %95 [-0.0114, -0.0002]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=426  0.1225 / 0.1954   fark +0.0729
    CHI   n=420  0.1373 / 0.1059   fark -0.0313
    DEN   n=426  0.1403 / 0.1918   fark +0.0515
    LAX   n=420  0.1199 / 0.0855   fark -0.0343
    MIA   n=426  0.1372 / 0.1022   fark -0.0349
    NY    n=426  0.1074 / 0.0912   fark -0.0162
    PHL   n=426  0.1490 / 0.0999   fark -0.0491
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1195         0.032         0.051   +0.019
  0.1-0.2       676         0.150         0.195   +0.045
  0.2-0.3       547         0.247         0.269   +0.022
  0.3-0.4       347         0.345         0.242   -0.103
  0.4-0.5       143         0.440         0.301   -0.139
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        14         0.632         0.500   -0.132
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6071)
  işlem sayısı                    6071
  kazanan                         2377  (%39)
  ort. İDDİA EDİLEN edge       +18.38p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.82p   ±0.5p  %95 [+0.8p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6200.37 $
  PnL fee ÖNCESİ             +49409.62 $
  PnL fee SONRASI            +43209.25 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15720.63 $   %90 aralık [-25213.13, -5205.80]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1247 (model 0.1305)

  bizim (fee sonrası)            +43209.25 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
