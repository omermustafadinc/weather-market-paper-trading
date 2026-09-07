========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-07T23:31:45.241062Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          18834
  orderbook seviyesi     1010506
  tahmin snapshot          13608
  karar                     3696
  simüle fill                959
  çözümlenmiş kova           456

## Brier skoru  (düşük = iyi, 414 kova)
  model                  0.1273
  piyasa (mid)           0.1301   n=414
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0028  ±0.0059  %95 [-0.0087, +0.0144]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 60  0.1481 / 0.2020   fark +0.0539
    CHI   n= 60  0.1261 / 0.1020   fark -0.0241
    DEN   n= 60  0.1443 / 0.2085   fark +0.0642
    LAX   n= 54  0.1151 / 0.0981   fark -0.0170
    MIA   n= 60  0.1225 / 0.1116   fark -0.0109
    NY    n= 60  0.1065 / 0.0810   fark -0.0256
    PHL   n= 60  0.1270 / 0.1045   fark -0.0225
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       153         0.035         0.039   +0.005
  0.1-0.2       105         0.151         0.190   +0.040
  0.2-0.3        91         0.244         0.275   +0.031
  0.3-0.4        46         0.350         0.261   -0.089
  0.4-0.5        11         0.443         0.091   -0.352
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (902)
  işlem sayısı                     902
  kazanan                          355  (%39)
  ort. İDDİA EDİLEN edge       +14.15p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.39p   ±1.3p  %95 [-2.9p, +2.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    900.19 $
  PnL fee ÖNCESİ              +1172.60 $
  PnL fee SONRASI              +272.41 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1336.28 $   %90 aralık [-5346.14, +2599.91]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1301 (model 0.1273)

  bizim (fee sonrası)              +272.41 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
