========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-24T06:05:36.815989Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         130068
  orderbook seviyesi     6884678
  tahmin snapshot          87003
  karar                    26892
  simüle fill               6903
  çözümlenmiş kova          3696

## Brier skoru  (düşük = iyi, 3594 kova)
  model                  0.1335
  piyasa (mid)           0.1237   n=3594
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0099  ±0.0027  %95 [-0.0152, -0.0046]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=516  0.1195 / 0.1905   fark +0.0710
    CHI   n=516  0.1455 / 0.1033   fark -0.0422
    DEN   n=516  0.1394 / 0.1920   fark +0.0526
    LAX   n=516  0.1201 / 0.0886   fark -0.0315
    MIA   n=510  0.1389 / 0.1007   fark -0.0382
    NY    n=510  0.1181 / 0.0926   fark -0.0255
    PHL   n=510  0.1534 / 0.0970   fark -0.0564
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1473         0.031         0.060   +0.030
  0.1-0.2       800         0.150         0.196   +0.047
  0.2-0.3       643         0.247         0.261   +0.014
  0.3-0.4       405         0.345         0.240   -0.105
  0.4-0.5       177         0.440         0.288   -0.151
  0.5-0.6        61         0.547         0.344   -0.202
  0.6-0.7        23         0.635         0.391   -0.244
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6862)
  işlem sayısı                    6862
  kazanan                         2688  (%39)
  ort. İDDİA EDİLEN edge       +19.19p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.44p   ±0.5p  %95 [+0.5p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6965.32 $
  PnL fee ÖNCESİ             +49131.55 $
  PnL fee SONRASI            +42166.23 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15693.43 $   %90 aralık [-24890.73, -5429.70]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1237 (model 0.1335)

  bizim (fee sonrası)            +42166.23 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
