========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-08T22:09:17.477021Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          69528
  orderbook seviyesi     3717507
  tahmin snapshot          46620
  karar                    14346
  simüle fill               3717
  çözümlenmiş kova          1758

## Brier skoru  (düşük = iyi, 1674 kova)
  model                  0.1324
  piyasa (mid)           0.1331   n=1674
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0006  ±0.0033  %95 [-0.0059, +0.0071]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=240  0.1316 / 0.2039   fark +0.0723
    CHI   n=240  0.1361 / 0.1106   fark -0.0254
    DEN   n=240  0.1479 / 0.2010   fark +0.0531
    LAX   n=234  0.1281 / 0.1006   fark -0.0274
    MIA   n=240  0.1355 / 0.1110   fark -0.0246
    NY    n=240  0.1093 / 0.0912   fark -0.0181
    PHL   n=240  0.1385 / 0.1123   fark -0.0262
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       624         0.033         0.059   +0.026
  0.1-0.2       426         0.151         0.192   +0.041
  0.2-0.3       343         0.247         0.245   -0.002
  0.3-0.4       186         0.346         0.242   -0.104
  0.4-0.5        72         0.436         0.292   -0.144
  0.5-0.6        19         0.552         0.316   -0.236
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3677)
  işlem sayısı                    3677
  kazanan                         1469  (%40)
  ort. İDDİA EDİLEN edge       +16.34p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.35p   ±0.7p  %95 [+0.0p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3670.14 $
  PnL fee ÖNCESİ             +25503.29 $
  PnL fee SONRASI            +21833.15 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9309.07 $   %90 aralık [-15981.65, -2586.30]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1331 (model 0.1324)

  bizim (fee sonrası)            +21833.15 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
