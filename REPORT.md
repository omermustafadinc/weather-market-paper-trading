========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-20T21:38:27.120216Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          43668
  orderbook seviyesi     2338580
  tahmin snapshot          29736
  karar                     8934
  simüle fill               2330
  çözümlenmiş kova           996

## Brier skoru  (düşük = iyi, 954 kova)
  model                  0.1307
  piyasa (mid)           0.1354   n=954
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0047  ±0.0040  %95 [-0.0031, +0.0125]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=138  0.1449 / 0.2121   fark +0.0672
    CHI   n=132  0.1295 / 0.1171   fark -0.0124
    DEN   n=138  0.1500 / 0.2095   fark +0.0594
    LAX   n=132  0.1143 / 0.0961   fark -0.0181
    MIA   n=138  0.1346 / 0.1166   fark -0.0180
    NY    n=138  0.1080 / 0.0826   fark -0.0254
    PHL   n=138  0.1327 / 0.1112   fark -0.0215
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       342         0.035         0.053   +0.017
  0.1-0.2       255         0.152         0.188   +0.037
  0.2-0.3       210         0.246         0.257   +0.011
  0.3-0.4       102         0.344         0.235   -0.109
  0.4-0.5        33         0.432         0.242   -0.190
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2247)
  işlem sayısı                    2247
  kazanan                          896  (%40)
  ort. İDDİA EDİLEN edge       +15.26p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.75p   ±0.9p  %95 [+0.1p, +3.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2270.02 $
  PnL fee ÖNCESİ             +15054.70 $
  PnL fee SONRASI            +12784.68 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -5597.01 $   %90 aralık [-11653.10, +391.32]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1354 (model 0.1307)

  bizim (fee sonrası)            +12784.68 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
