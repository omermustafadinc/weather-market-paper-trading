========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-09T19:14:13.818449Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          22074
  orderbook seviyesi     1185023
  tahmin snapshot          15876
  karar                     4350
  simüle fill               1128
  çözümlenmiş kova           516

## Brier skoru  (düşük = iyi, 474 kova)
  model                  0.1261
  piyasa (mid)           0.1304   n=474
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0043  ±0.0055  %95 [-0.0066, +0.0151]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 72  0.1499 / 0.2056   fark +0.0556
    CHI   n= 66  0.1258 / 0.1000   fark -0.0258
    DEN   n= 72  0.1451 / 0.2099   fark +0.0647
    LAX   n= 66  0.1038 / 0.0963   fark -0.0075
    MIA   n= 66  0.1229 / 0.1076   fark -0.0153
    NY    n= 66  0.1040 / 0.0799   fark -0.0241
    PHL   n= 66  0.1274 / 0.0995   fark -0.0278
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       180         0.033         0.039   +0.006
  0.1-0.2       113         0.151         0.195   +0.044
  0.2-0.3       105         0.245         0.276   +0.031
  0.3-0.4        52         0.347         0.250   -0.097
  0.4-0.5        15         0.441         0.133   -0.307
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (998)
  işlem sayısı                     998
  kazanan                          394  (%39)
  ort. İDDİA EDİLEN edge       +14.24p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.12p   ±1.2p  %95 [-2.3p, +2.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    993.87 $
  PnL fee ÖNCESİ              +2655.22 $
  PnL fee SONRASI             +1661.35 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1888.33 $   %90 aralık [-5627.19, +1708.26]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1304 (model 0.1261)

  bizim (fee sonrası)             +1661.35 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
