========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-21T20:22:29.081845Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         127842
  orderbook seviyesi     6771849
  tahmin snapshot          85491
  karar                    26448
  simüle fill               6790
  çözümlenmiş kova          3582

## Brier skoru  (düşük = iyi, 3480 kova)
  model                  0.1337
  piyasa (mid)           0.1244   n=3480
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0093  ±0.0028  %95 [-0.0147, -0.0039]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=504  0.1203 / 0.1918   fark +0.0715
    CHI   n=498  0.1453 / 0.1044   fark -0.0410
    DEN   n=504  0.1405 / 0.1937   fark +0.0532
    LAX   n=498  0.1202 / 0.0890   fark -0.0312
    MIA   n=492  0.1393 / 0.1011   fark -0.0382
    NY    n=492  0.1174 / 0.0919   fark -0.0255
    PHL   n=492  0.1530 / 0.0963   fark -0.0567
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1421         0.031         0.060   +0.029
  0.1-0.2       780         0.150         0.196   +0.047
  0.2-0.3       625         0.247         0.266   +0.018
  0.3-0.4       392         0.345         0.235   -0.110
  0.4-0.5       174         0.439         0.293   -0.146
  0.5-0.6        55         0.547         0.345   -0.202
  0.6-0.7        21         0.636         0.333   -0.303
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6714)
  işlem sayısı                    6714
  kazanan                         2624  (%39)
  ort. İDDİA EDİLEN edge       +19.15p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.49p   ±0.5p  %95 [+0.5p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6830.83 $
  PnL fee ÖNCESİ             +49733.32 $
  PnL fee SONRASI            +42902.49 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16371.48 $   %90 aralık [-26785.54, -6829.72]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1244 (model 0.1337)

  bizim (fee sonrası)            +42902.49 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
