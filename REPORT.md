========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-23T09:48:19.628743Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         129480
  orderbook seviyesi     6855446
  tahmin snapshot          86625
  karar                    26760
  simüle fill               6862
  çözümlenmiş kova          3654

## Brier skoru  (düşük = iyi, 3552 kova)
  model                  0.1338
  piyasa (mid)           0.1239   n=3552
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0099  ±0.0027  %95 [-0.0152, -0.0045]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=510  0.1196 / 0.1913   fark +0.0717
    CHI   n=510  0.1458 / 0.1037   fark -0.0421
    DEN   n=510  0.1407 / 0.1940   fark +0.0532
    LAX   n=510  0.1210 / 0.0883   fark -0.0327
    MIA   n=504  0.1394 / 0.1000   fark -0.0393
    NY    n=504  0.1171 / 0.0920   fark -0.0252
    PHL   n=504  0.1529 / 0.0970   fark -0.0559
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1451         0.031         0.060   +0.029
  0.1-0.2       796         0.150         0.197   +0.048
  0.2-0.3       638         0.247         0.263   +0.016
  0.3-0.4       398         0.345         0.236   -0.109
  0.4-0.5       176         0.440         0.290   -0.150
  0.5-0.6        59         0.547         0.339   -0.208
  0.6-0.7        22         0.635         0.364   -0.271
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6811)
  işlem sayısı                    6811
  kazanan                         2663  (%39)
  ort. İDDİA EDİLEN edge       +19.19p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.42p   ±0.5p  %95 [+0.4p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6919.85 $
  PnL fee ÖNCESİ             +48994.35 $
  PnL fee SONRASI            +42074.50 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16250.11 $   %90 aralık [-25099.79, -6002.70]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1239 (model 0.1338)

  bizim (fee sonrası)            +42074.50 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
