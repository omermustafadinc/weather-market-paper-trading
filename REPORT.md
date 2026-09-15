========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-15T17:38:00.798435Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          33570
  orderbook seviyesi     1779852
  tahmin snapshot          23058
  karar                     6780
  simüle fill               1774
  çözümlenmiş kova           768

## Brier skoru  (düşük = iyi, 726 kova)
  model                  0.1283
  piyasa (mid)           0.1320   n=726
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0037  ±0.0044  %95 [-0.0049, +0.0123]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=108  0.1539 / 0.2106   fark +0.0567
    CHI   n=102  0.1282 / 0.1109   fark -0.0173
    DEN   n=108  0.1476 / 0.2094   fark +0.0618
    LAX   n=102  0.1053 / 0.0906   fark -0.0147
    MIA   n=102  0.1239 / 0.1107   fark -0.0133
    NY    n=102  0.1071 / 0.0827   fark -0.0244
    PHL   n=102  0.1291 / 0.0998   fark -0.0293
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       268         0.033         0.041   +0.008
  0.1-0.2       177         0.149         0.192   +0.043
  0.2-0.3       166         0.245         0.277   +0.032
  0.3-0.4        76         0.344         0.237   -0.107
  0.4-0.5        27         0.432         0.185   -0.247
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1681)
  işlem sayısı                    1681
  kazanan                          668  (%40)
  ort. İDDİA EDİLEN edge       +14.85p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.62p   ±1.0p  %95 [-0.3p, +3.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1723.34 $
  PnL fee ÖNCESİ             +10107.96 $
  PnL fee SONRASI             +8384.62 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3447.11 $   %90 aralık [-7766.80, +1231.77]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1320 (model 0.1283)

  bizim (fee sonrası)             +8384.62 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
