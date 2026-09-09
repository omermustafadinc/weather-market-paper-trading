========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-09T12:19:45.336524Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          21402
  orderbook seviyesi     1149796
  tahmin snapshot          15498
  karar                     4182
  simüle fill               1084
  çözümlenmiş kova           504

## Brier skoru  (düşük = iyi, 462 kova)
  model                  0.1258
  piyasa (mid)           0.1281   n=462
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0023  ±0.0055  %95 [-0.0086, +0.0131]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 66  0.1524 / 0.2046   fark +0.0522
    CHI   n= 66  0.1258 / 0.1000   fark -0.0258
    DEN   n= 66  0.1441 / 0.2085   fark +0.0644
    LAX   n= 66  0.1038 / 0.0963   fark -0.0075
    MIA   n= 66  0.1229 / 0.1076   fark -0.0153
    NY    n= 66  0.1040 / 0.0799   fark -0.0241
    PHL   n= 66  0.1274 / 0.0995   fark -0.0278
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       175         0.033         0.040   +0.007
  0.1-0.2       112         0.151         0.188   +0.037
  0.2-0.3       101         0.244         0.277   +0.033
  0.3-0.4        50         0.348         0.260   -0.088
  0.4-0.5        15         0.441         0.133   -0.307
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (986)
  işlem sayısı                     986
  kazanan                          386  (%39)
  ort. İDDİA EDİLEN edge       +14.20p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.52p   ±1.2p  %95 [-2.9p, +1.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    981.77 $
  PnL fee ÖNCESİ               +602.40 $
  PnL fee SONRASI              -379.37 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1515.67 $   %90 aralık [-5361.98, +2365.69]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1281 (model 0.1258)

  bizim (fee sonrası)              -379.37 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
