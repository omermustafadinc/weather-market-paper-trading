========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-13T16:56:18.551808Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          75192
  orderbook seviyesi     4017029
  tahmin snapshot          50085
  karar                    15456
  simüle fill               3999
  çözümlenmiş kova          1944

## Brier skoru  (düşük = iyi, 1860 kova)
  model                  0.1332
  piyasa (mid)           0.1330   n=1860
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0002  ±0.0032  %95 [-0.0065, +0.0061]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=270  0.1295 / 0.2056   fark +0.0761
    CHI   n=264  0.1406 / 0.1105   fark -0.0301
    DEN   n=270  0.1497 / 0.2014   fark +0.0517
    LAX   n=264  0.1271 / 0.0968   fark -0.0303
    MIA   n=264  0.1347 / 0.1085   fark -0.0262
    NY    n=264  0.1098 / 0.0911   fark -0.0188
    PHL   n=264  0.1404 / 0.1136   fark -0.0268
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       697         0.033         0.063   +0.030
  0.1-0.2       467         0.151         0.188   +0.038
  0.2-0.3       388         0.247         0.250   +0.003
  0.3-0.4       202         0.345         0.228   -0.118
  0.4-0.5        77         0.437         0.299   -0.138
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         4         0.652         0.500   -0.152
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3977)
  işlem sayısı                    3977
  kazanan                         1572  (%40)
  ort. İDDİA EDİLEN edge       +16.76p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.08p   ±0.6p  %95 [-0.2p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4011.66 $
  PnL fee ÖNCESİ             +24675.66 $
  PnL fee SONRASI            +20664.00 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10570.70 $   %90 aralık [-17878.30, -2828.91]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1330 (model 0.1332)

  bizim (fee sonrası)            +20664.00 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
