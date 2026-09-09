========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-09T00:08:08.200503Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          20886
  orderbook seviyesi     1120774
  tahmin snapshot          14868
  karar                     4134
  simüle fill               1071
  çözümlenmiş kova           498

## Brier skoru  (düşük = iyi, 456 kova)
  model                  0.1261
  piyasa (mid)           0.1277   n=456
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0016  ±0.0056  %95 [-0.0093, +0.0126]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 66  0.1524 / 0.2046   fark +0.0522
    CHI   n= 66  0.1258 / 0.1000   fark -0.0258
    DEN   n= 66  0.1441 / 0.2085   fark +0.0644
    LAX   n= 60  0.1040 / 0.0906   fark -0.0134
    MIA   n= 66  0.1229 / 0.1076   fark -0.0153
    NY    n= 66  0.1040 / 0.0799   fark -0.0241
    PHL   n= 66  0.1274 / 0.0995   fark -0.0278
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       173         0.034         0.040   +0.007
  0.1-0.2       111         0.151         0.189   +0.038
  0.2-0.3        99         0.244         0.283   +0.039
  0.3-0.4        49         0.348         0.245   -0.104
  0.4-0.5        15         0.441         0.133   -0.307
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (983)
  işlem sayısı                     983
  kazanan                          383  (%39)
  ort. İDDİA EDİLEN edge       +14.21p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.66p   ±1.2p  %95 [-3.1p, +1.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    979.86 $
  PnL fee ÖNCESİ               +530.79 $
  PnL fee SONRASI              -449.07 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1894.19 $   %90 aralık [-5885.65, +1665.72]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1277 (model 0.1261)

  bizim (fee sonrası)              -449.07 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
