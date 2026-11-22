========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-22T00:32:02.355360Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         128178
  orderbook seviyesi     6787514
  tahmin snapshot          85743
  karar                    26532
  simüle fill               6800
  çözümlenmiş kova          3606

## Brier skoru  (düşük = iyi, 3504 kova)
  model                  0.1337
  piyasa (mid)           0.1242   n=3504
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0095  ±0.0027  %95 [-0.0149, -0.0041]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=504  0.1203 / 0.1918   fark +0.0715
    CHI   n=504  0.1455 / 0.1042   fark -0.0414
    DEN   n=504  0.1405 / 0.1937   fark +0.0532
    LAX   n=498  0.1202 / 0.0890   fark -0.0312
    MIA   n=498  0.1388 / 0.1008   fark -0.0380
    NY    n=498  0.1181 / 0.0923   fark -0.0258
    PHL   n=498  0.1523 / 0.0962   fark -0.0561
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1430         0.031         0.060   +0.029
  0.1-0.2       785         0.150         0.195   +0.045
  0.2-0.3       631         0.247         0.265   +0.018
  0.3-0.4       395         0.345         0.238   -0.107
  0.4-0.5       174         0.439         0.293   -0.146
  0.5-0.6        56         0.547         0.339   -0.208
  0.6-0.7        21         0.636         0.333   -0.303
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6770)
  işlem sayısı                    6770
  kazanan                         2644  (%39)
  ort. İDDİA EDİLEN edge       +19.17p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.41p   ±0.5p  %95 [+0.4p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6879.56 $
  PnL fee ÖNCESİ             +49219.06 $
  PnL fee SONRASI            +42339.50 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16297.07 $   %90 aralık [-25484.42, -6709.89]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1242 (model 0.1337)

  bizim (fee sonrası)            +42339.50 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
