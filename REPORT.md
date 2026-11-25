========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-25T01:28:24.280861Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         130740
  orderbook seviyesi     6917615
  tahmin snapshot          87381
  karar                    27060
  simüle fill               6943
  çözümlenmiş kova          3732

## Brier skoru  (düşük = iyi, 3612 kova)
  model                  0.1336
  piyasa (mid)           0.1239   n=3612
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0097  ±0.0027  %95 [-0.0150, -0.0044]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=522  0.1192 / 0.1906   fark +0.0714
    CHI   n=522  0.1461 / 0.1033   fark -0.0428
    DEN   n=522  0.1395 / 0.1924   fark +0.0529
    LAX   n=516  0.1201 / 0.0886   fark -0.0315
    MIA   n=510  0.1389 / 0.1007   fark -0.0382
    NY    n=510  0.1181 / 0.0926   fark -0.0255
    PHL   n=510  0.1534 / 0.0970   fark -0.0564
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1482         0.030         0.060   +0.030
  0.1-0.2       801         0.150         0.197   +0.048
  0.2-0.3       646         0.247         0.262   +0.014
  0.3-0.4       408         0.345         0.240   -0.105
  0.4-0.5       179         0.440         0.285   -0.155
  0.5-0.6        61         0.547         0.344   -0.202
  0.6-0.7        23         0.635         0.391   -0.244
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6901)
  işlem sayısı                    6901
  kazanan                         2705  (%39)
  ort. İDDİA EDİLEN edge       +19.20p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.47p   ±0.5p  %95 [+0.5p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   7013.14 $
  PnL fee ÖNCESİ             +49147.55 $
  PnL fee SONRASI            +42134.41 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15900.00 $   %90 aralık [-26265.37, -5103.06]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1239 (model 0.1336)

  bizim (fee sonrası)            +42134.41 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
