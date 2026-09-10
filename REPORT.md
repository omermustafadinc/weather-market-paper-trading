========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-10T21:29:01.720665Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          24282
  orderbook seviyesi     1293865
  tahmin snapshot          17010
  karar                     4824
  simüle fill               1247
  çözümlenmiş kova           570

## Brier skoru  (düşük = iyi, 528 kova)
  model                  0.1257
  piyasa (mid)           0.1294   n=528
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0037  ±0.0053  %95 [-0.0066, +0.0141]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 78  0.1515 / 0.2074   fark +0.0559
    CHI   n= 72  0.1253 / 0.0989   fark -0.0264
    DEN   n= 78  0.1448 / 0.2120   fark +0.0671
    LAX   n= 72  0.0971 / 0.0907   fark -0.0063
    MIA   n= 78  0.1230 / 0.1080   fark -0.0150
    NY    n= 78  0.1077 / 0.0854   fark -0.0223
    PHL   n= 72  0.1282 / 0.0954   fark -0.0328
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       202         0.033         0.035   +0.002
  0.1-0.2       124         0.150         0.194   +0.043
  0.2-0.3       118         0.247         0.297   +0.050
  0.3-0.4        55         0.345         0.236   -0.109
  0.4-0.5        18         0.438         0.111   -0.326
  0.5-0.6         7         0.552         0.429   -0.123
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1157)
  işlem sayısı                    1157
  kazanan                          446  (%39)
  ort. İDDİA EDİLEN edge       +14.51p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.63p   ±1.2p  %95 [-2.9p, +1.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1163.55 $
  PnL fee ÖNCESİ              +1023.18 $
  PnL fee SONRASI              -140.37 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1977.52 $   %90 aralık [-6287.76, +2098.77]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1294 (model 0.1257)

  bizim (fee sonrası)              -140.37 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
