========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-13T01:22:26.341078Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          29178
  orderbook seviyesi     1530928
  tahmin snapshot          20286
  karar                     5886
  simüle fill               1526
  çözümlenmiş kova           666

## Brier skoru  (düşük = iyi, 624 kova)
  model                  0.1264
  piyasa (mid)           0.1312   n=624
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0048  ±0.0047  %95 [-0.0045, +0.0140]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 90  0.1553 / 0.2098   fark +0.0544
    CHI   n= 90  0.1264 / 0.1047   fark -0.0217
    DEN   n= 90  0.1448 / 0.2102   fark +0.0654
    LAX   n= 84  0.0989 / 0.0902   fark -0.0087
    MIA   n= 90  0.1243 / 0.1161   fark -0.0082
    NY    n= 90  0.1049 / 0.0826   fark -0.0223
    PHL   n= 90  0.1286 / 0.1021   fark -0.0265
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       234         0.033         0.038   +0.005
  0.1-0.2       151         0.149         0.192   +0.043
  0.2-0.3       141         0.246         0.277   +0.031
  0.3-0.4        62         0.344         0.242   -0.102
  0.4-0.5        24         0.435         0.208   -0.226
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1414)
  işlem sayısı                    1414
  kazanan                          564  (%40)
  ort. İDDİA EDİLEN edge       +14.72p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.23p   ±1.1p  %95 [-0.9p, +3.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1440.34 $
  PnL fee ÖNCESİ              +5979.43 $
  PnL fee SONRASI             +4539.09 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2610.49 $   %90 aralık [-6735.35, +1490.78]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1312 (model 0.1264)

  bizim (fee sonrası)             +4539.09 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
