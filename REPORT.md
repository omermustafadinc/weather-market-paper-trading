========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-08T15:41:13.582750Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          19878
  orderbook seviyesi     1067337
  tahmin snapshot          14238
  karar                     3882
  simüle fill               1007
  çözümlenmiş kova           474

## Brier skoru  (düşük = iyi, 432 kova)
  model                  0.1267
  piyasa (mid)           0.1311   n=432
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0044  ±0.0058  %95 [-0.0069, +0.0157]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 66  0.1524 / 0.2046   fark +0.0522
    CHI   n= 60  0.1261 / 0.1020   fark -0.0241
    DEN   n= 66  0.1441 / 0.2085   fark +0.0644
    LAX   n= 60  0.1040 / 0.0906   fark -0.0134
    MIA   n= 60  0.1225 / 0.1116   fark -0.0109
    NY    n= 60  0.1065 / 0.0810   fark -0.0256
    PHL   n= 60  0.1270 / 0.1045   fark -0.0225
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       163         0.034         0.043   +0.009
  0.1-0.2       106         0.151         0.198   +0.047
  0.2-0.3        95         0.243         0.263   +0.020
  0.3-0.4        47         0.350         0.255   -0.094
  0.4-0.5        12         0.441         0.083   -0.358
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (927)
  işlem sayısı                     927
  kazanan                          366  (%39)
  ort. İDDİA EDİLEN edge       +14.34p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.04p   ±1.3p  %95 [-2.5p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    929.65 $
  PnL fee ÖNCESİ              +1202.73 $
  PnL fee SONRASI              +273.08 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1540.35 $   %90 aralık [-5668.09, +2259.56]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1311 (model 0.1267)

  bizim (fee sonrası)              +273.08 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
