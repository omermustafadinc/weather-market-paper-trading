========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-21T04:37:19.145220Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         127338
  orderbook seviyesi     6744414
  tahmin snapshot          85113
  karar                    26364
  simüle fill               6770
  çözümlenmiş kova          3570

## Brier skoru  (düşük = iyi, 3468 kova)
  model                  0.1338
  piyasa (mid)           0.1243   n=3468
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0095  ±0.0028  %95 [-0.0149, -0.0041]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=498  0.1212 / 0.1930   fark +0.0717
    CHI   n=498  0.1453 / 0.1044   fark -0.0410
    DEN   n=498  0.1404 / 0.1935   fark +0.0531
    LAX   n=498  0.1202 / 0.0890   fark -0.0312
    MIA   n=492  0.1393 / 0.1011   fark -0.0382
    NY    n=492  0.1174 / 0.0919   fark -0.0255
    PHL   n=492  0.1530 / 0.0963   fark -0.0567
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1418         0.031         0.060   +0.029
  0.1-0.2       776         0.150         0.196   +0.046
  0.2-0.3       621         0.247         0.267   +0.020
  0.3-0.4       392         0.345         0.235   -0.110
  0.4-0.5       174         0.439         0.293   -0.146
  0.5-0.6        54         0.547         0.333   -0.214
  0.6-0.7        21         0.636         0.333   -0.303
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6708)
  işlem sayısı                    6708
  kazanan                         2618  (%39)
  ort. İDDİA EDİLEN edge       +19.15p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.44p   ±0.5p  %95 [+0.4p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6827.12 $
  PnL fee ÖNCESİ             +49598.52 $
  PnL fee SONRASI            +42771.40 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15913.88 $   %90 aralık [-26853.16, -5995.39]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1243 (model 0.1338)

  bizim (fee sonrası)            +42771.40 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
