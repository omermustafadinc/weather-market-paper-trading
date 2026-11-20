========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-20T23:44:33.105754Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         127002
  orderbook seviyesi     6726981
  tahmin snapshot          84987
  karar                    26280
  simüle fill               6750
  çözümlenmiş kova          3564

## Brier skoru  (düşük = iyi, 3462 kova)
  model                  0.1339
  piyasa (mid)           0.1242   n=3462
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0097  ±0.0028  %95 [-0.0151, -0.0042]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=498  0.1212 / 0.1930   fark +0.0717
    CHI   n=498  0.1453 / 0.1044   fark -0.0410
    DEN   n=498  0.1404 / 0.1935   fark +0.0531
    LAX   n=492  0.1204 / 0.0879   fark -0.0324
    MIA   n=492  0.1393 / 0.1011   fark -0.0382
    NY    n=492  0.1174 / 0.0919   fark -0.0255
    PHL   n=492  0.1530 / 0.0963   fark -0.0567
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1417         0.031         0.060   +0.029
  0.1-0.2       773         0.150         0.197   +0.047
  0.2-0.3       619         0.247         0.267   +0.019
  0.3-0.4       392         0.345         0.235   -0.110
  0.4-0.5       174         0.439         0.293   -0.146
  0.5-0.6        54         0.547         0.333   -0.214
  0.6-0.7        21         0.636         0.333   -0.303
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6708)
  işlem sayısı                    6708
  kazanan                         2618  (%39)
  ort. İDDİA EDİLEN edge       +19.15p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.44p   ±0.5p  %95 [+0.4p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6827.12 $
  PnL fee ÖNCESİ             +49598.52 $
  PnL fee SONRASI            +42771.40 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16366.10 $   %90 aralık [-26995.72, -5102.05]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1242 (model 0.1339)

  bizim (fee sonrası)            +42771.40 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
