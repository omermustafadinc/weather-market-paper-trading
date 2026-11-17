========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-17T04:20:34.743260Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         123642
  orderbook seviyesi     6559476
  tahmin snapshot          82845
  karar                    25608
  simüle fill               6587
  çözümlenmiş kova          3402

## Brier skoru  (düşük = iyi, 3318 kova)
  model                  0.1327
  piyasa (mid)           0.1245   n=3318
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0081  ±0.0028  %95 [-0.0135, -0.0027]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=474  0.1210 / 0.1915   fark +0.0705
    CHI   n=474  0.1416 / 0.1067   fark -0.0350
    DEN   n=474  0.1410 / 0.1924   fark +0.0514
    LAX   n=474  0.1205 / 0.0893   fark -0.0312
    MIA   n=474  0.1386 / 0.1023   fark -0.0363
    NY    n=474  0.1147 / 0.0928   fark -0.0220
    PHL   n=474  0.1512 / 0.0968   fark -0.0544
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1357         0.031         0.057   +0.026
  0.1-0.2       742         0.150         0.195   +0.045
  0.2-0.3       596         0.247         0.267   +0.020
  0.3-0.4       376         0.345         0.239   -0.106
  0.4-0.5       165         0.440         0.309   -0.131
  0.5-0.6        50         0.547         0.340   -0.207
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6547)
  işlem sayısı                    6547
  kazanan                         2569  (%39)
  ort. İDDİA EDİLEN edge       +18.93p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.73p   ±0.5p  %95 [+0.7p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6670.97 $
  PnL fee ÖNCESİ             +51061.55 $
  PnL fee SONRASI            +44390.58 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15376.38 $   %90 aralık [-24845.89, -5810.59]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1245 (model 0.1327)

  bizim (fee sonrası)            +44390.58 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
