========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-07T21:18:43.026073Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          18666
  orderbook seviyesi     1001978
  tahmin snapshot          13482
  karar                     3654
  simüle fill                949
  çözümlenmiş kova           444

## Brier skoru  (düşük = iyi, 402 kova)
  model                  0.1263
  piyasa (mid)           0.1319   n=402
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0056  ±0.0059  %95 [-0.0060, +0.0171]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 60  0.1481 / 0.2020   fark +0.0539
    CHI   n= 54  0.1244 / 0.1053   fark -0.0191
    DEN   n= 60  0.1443 / 0.2085   fark +0.0642
    LAX   n= 54  0.1151 / 0.0981   fark -0.0170
    MIA   n= 60  0.1225 / 0.1116   fark -0.0109
    NY    n= 60  0.1065 / 0.0810   fark -0.0256
    PHL   n= 54  0.1214 / 0.1083   fark -0.0131
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       147         0.035         0.041   +0.006
  0.1-0.2       104         0.151         0.183   +0.032
  0.2-0.3        89         0.244         0.270   +0.026
  0.3-0.4        45         0.351         0.267   -0.084
  0.4-0.5         9         0.441         0.111   -0.330
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (867)
  işlem sayısı                     867
  kazanan                          350  (%40)
  ort. İDDİA EDİLEN edge       +14.11p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.75p   ±1.3p  %95 [-1.8p, +3.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    866.32 $
  PnL fee ÖNCESİ              +1851.50 $
  PnL fee SONRASI              +985.18 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1459.66 $   %90 aralık [-5557.34, +2116.68]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1319 (model 0.1263)

  bizim (fee sonrası)              +985.18 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
