========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-26T12:02:56.756604Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         131748
  orderbook seviyesi     6974090
  tahmin snapshot          87885
  karar                    27228
  simüle fill               6987
  çözümlenmiş kova          3780

## Brier skoru  (düşük = iyi, 3660 kova)
  model                  0.1329
  piyasa (mid)           0.1237   n=3660
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0092  ±0.0027  %95 [-0.0144, -0.0039]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=528  0.1198 / 0.1910   fark +0.0713
    CHI   n=528  0.1452 / 0.1042   fark -0.0410
    DEN   n=528  0.1382 / 0.1913   fark +0.0530
    LAX   n=528  0.1201 / 0.0885   fark -0.0316
    MIA   n=516  0.1384 / 0.1011   fark -0.0373
    NY    n=516  0.1169 / 0.0919   fark -0.0250
    PHL   n=516  0.1520 / 0.0964   fark -0.0556
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1509         0.030         0.059   +0.029
  0.1-0.2       805         0.150         0.198   +0.048
  0.2-0.3       654         0.247         0.261   +0.014
  0.3-0.4       411         0.345         0.241   -0.104
  0.4-0.5       181         0.440         0.287   -0.152
  0.5-0.6        62         0.546         0.339   -0.208
  0.6-0.7        25         0.636         0.440   -0.196
  0.7-0.8         4         0.744         0.750   +0.006
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6943)
  işlem sayısı                    6943
  kazanan                         2739  (%39)
  ort. İDDİA EDİLEN edge       +19.22p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.69p   ±0.5p  %95 [+0.7p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   7053.95 $
  PnL fee ÖNCESİ             +49955.02 $
  PnL fee SONRASI            +42901.07 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16355.58 $   %90 aralık [-26265.87, -5598.99]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1237 (model 0.1329)

  bizim (fee sonrası)            +42901.07 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
