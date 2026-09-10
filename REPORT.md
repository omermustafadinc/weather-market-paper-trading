========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-10T18:50:14.309495Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          23946
  orderbook seviyesi     1278415
  tahmin snapshot          16758
  karar                     4740
  simüle fill               1225
  çözümlenmiş kova           558

## Brier skoru  (düşük = iyi, 516 kova)
  model                  0.1253
  piyasa (mid)           0.1300   n=516
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0047  ±0.0053  %95 [-0.0058, +0.0151]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 78  0.1515 / 0.2074   fark +0.0559
    CHI   n= 72  0.1253 / 0.0989   fark -0.0264
    DEN   n= 78  0.1448 / 0.2120   fark +0.0671
    LAX   n= 72  0.0971 / 0.0907   fark -0.0063
    MIA   n= 72  0.1215 / 0.1113   fark -0.0102
    NY    n= 72  0.1050 / 0.0809   fark -0.0241
    PHL   n= 72  0.1282 / 0.0954   fark -0.0328
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       199         0.032         0.035   +0.003
  0.1-0.2       120         0.151         0.192   +0.041
  0.2-0.3       115         0.247         0.296   +0.048
  0.3-0.4        53         0.346         0.245   -0.101
  0.4-0.5        18         0.438         0.111   -0.326
  0.5-0.6         7         0.552         0.429   -0.123
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1097)
  işlem sayısı                    1097
  kazanan                          426  (%39)
  ort. İDDİA EDİLEN edge       +14.55p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.13p   ±1.2p  %95 [-2.5p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1100.48 $
  PnL fee ÖNCESİ              +1873.10 $
  PnL fee SONRASI              +772.62 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1695.49 $   %90 aralık [-5758.44, +2093.25]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1300 (model 0.1253)

  bizim (fee sonrası)              +772.62 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
