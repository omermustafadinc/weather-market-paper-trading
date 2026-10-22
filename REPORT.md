========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-22T01:19:55.723602Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          90018
  orderbook seviyesi     4802321
  tahmin snapshot          59787
  karar                    18582
  simüle fill               4815
  çözümlenmiş kova          2304

## Brier skoru  (düşük = iyi, 2220 kova)
  model                  0.1322
  piyasa (mid)           0.1294   n=2220
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0028  ±0.0031  %95 [-0.0090, +0.0033]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=318  0.1280 / 0.2025   fark +0.0745
    CHI   n=318  0.1392 / 0.1089   fark -0.0303
    DEN   n=318  0.1493 / 0.2007   fark +0.0513
    LAX   n=312  0.1201 / 0.0894   fark -0.0307
    MIA   n=318  0.1359 / 0.1031   fark -0.0328
    NY    n=318  0.1074 / 0.0896   fark -0.0179
    PHL   n=318  0.1452 / 0.1105   fark -0.0347
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       854         0.033         0.062   +0.029
  0.1-0.2       545         0.150         0.189   +0.039
  0.2-0.3       435         0.247         0.257   +0.010
  0.3-0.4       252         0.345         0.214   -0.131
  0.4-0.5        93         0.439         0.312   -0.127
  0.5-0.6        29         0.548         0.345   -0.203
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4728)
  işlem sayısı                    4728
  kazanan                         1822  (%39)
  ort. İDDİA EDİLEN edge       +17.72p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.78p   ±0.6p  %95 [-0.4p, +1.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4810.52 $
  PnL fee ÖNCESİ             +29185.95 $
  PnL fee SONRASI            +24375.43 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11202.50 $   %90 aralık [-18294.96, -3258.86]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1294 (model 0.1322)

  bizim (fee sonrası)            +24375.43 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
