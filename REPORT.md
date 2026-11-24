========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-24T16:50:50.194076Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         130404
  orderbook seviyesi     6901935
  tahmin snapshot          87129
  karar                    26976
  simüle fill               6923
  çözümlenmiş kova          3708

## Brier skoru  (düşük = iyi, 3606 kova)
  model                  0.1335
  piyasa (mid)           0.1240   n=3606
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0095  ±0.0027  %95 [-0.0148, -0.0042]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=522  0.1192 / 0.1906   fark +0.0714
    CHI   n=516  0.1455 / 0.1033   fark -0.0422
    DEN   n=522  0.1395 / 0.1924   fark +0.0529
    LAX   n=516  0.1201 / 0.0886   fark -0.0315
    MIA   n=510  0.1389 / 0.1007   fark -0.0382
    NY    n=510  0.1181 / 0.0926   fark -0.0255
    PHL   n=510  0.1534 / 0.0970   fark -0.0564
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1479         0.031         0.060   +0.030
  0.1-0.2       800         0.150         0.196   +0.047
  0.2-0.3       646         0.247         0.262   +0.014
  0.3-0.4       408         0.345         0.240   -0.105
  0.4-0.5       177         0.440         0.288   -0.151
  0.5-0.6        61         0.547         0.344   -0.202
  0.6-0.7        23         0.635         0.391   -0.244
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6882)
  işlem sayısı                    6882
  kazanan                         2702  (%39)
  ort. İDDİA EDİLEN edge       +19.18p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.53p   ±0.5p  %95 [+0.5p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6987.73 $
  PnL fee ÖNCESİ             +49550.34 $
  PnL fee SONRASI            +42562.61 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16579.93 $   %90 aralık [-26960.75, -6459.77]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1240 (model 0.1335)

  bizim (fee sonrası)            +42562.61 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
