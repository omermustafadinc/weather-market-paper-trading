========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-22T15:29:57.619020Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         128640
  orderbook seviyesi     6813763
  tahmin snapshot          86121
  karar                    26592
  simüle fill               6821
  çözümlenmiş kova          3624

## Brier skoru  (düşük = iyi, 3522 kova)
  model                  0.1336
  piyasa (mid)           0.1243   n=3522
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0093  ±0.0027  %95 [-0.0146, -0.0039]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=510  0.1196 / 0.1913   fark +0.0717
    CHI   n=504  0.1455 / 0.1042   fark -0.0414
    DEN   n=510  0.1407 / 0.1940   fark +0.0532
    LAX   n=504  0.1203 / 0.0891   fark -0.0313
    MIA   n=498  0.1388 / 0.1008   fark -0.0380
    NY    n=498  0.1181 / 0.0923   fark -0.0258
    PHL   n=498  0.1523 / 0.0962   fark -0.0561
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1436         0.031         0.060   +0.029
  0.1-0.2       790         0.150         0.195   +0.045
  0.2-0.3       636         0.247         0.264   +0.017
  0.3-0.4       396         0.345         0.237   -0.108
  0.4-0.5       174         0.439         0.293   -0.146
  0.5-0.6        57         0.547         0.351   -0.196
  0.6-0.7        21         0.636         0.333   -0.303
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6780)
  işlem sayısı                    6780
  kazanan                         2652  (%39)
  ort. İDDİA EDİLEN edge       +19.17p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.46p   ±0.5p  %95 [+0.5p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6888.10 $
  PnL fee ÖNCESİ             +49400.98 $
  PnL fee SONRASI            +42512.88 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16082.31 $   %90 aralık [-26041.84, -6369.35]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1243 (model 0.1336)

  bizim (fee sonrası)            +42512.88 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
