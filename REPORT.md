========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-08T06:25:29.975066Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          19374
  orderbook seviyesi     1039791
  tahmin snapshot          13986
  karar                     3798
  simüle fill                986
  çözümlenmiş kova           462

## Brier skoru  (düşük = iyi, 420 kova)
  model                  0.1255
  piyasa (mid)           0.1286   n=420
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0031  ±0.0058  %95 [-0.0083, +0.0145]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 60  0.1481 / 0.2020   fark +0.0539
    CHI   n= 60  0.1261 / 0.1020   fark -0.0241
    DEN   n= 60  0.1443 / 0.2085   fark +0.0642
    LAX   n= 60  0.1040 / 0.0906   fark -0.0134
    MIA   n= 60  0.1225 / 0.1116   fark -0.0109
    NY    n= 60  0.1065 / 0.0810   fark -0.0256
    PHL   n= 60  0.1270 / 0.1045   fark -0.0225
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       158         0.034         0.038   +0.004
  0.1-0.2       105         0.151         0.190   +0.040
  0.2-0.3        91         0.244         0.275   +0.031
  0.3-0.4        46         0.350         0.261   -0.089
  0.4-0.5        11         0.443         0.091   -0.352
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (905)
  işlem sayısı                     905
  kazanan                          358  (%40)
  ort. İDDİA EDİLEN edge       +14.12p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.32p   ±1.3p  %95 [-2.8p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    901.00 $
  PnL fee ÖNCESİ              +1186.50 $
  PnL fee SONRASI              +285.50 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1666.88 $   %90 aralık [-5259.86, +1392.69]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1286 (model 0.1255)

  bizim (fee sonrası)              +285.50 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
