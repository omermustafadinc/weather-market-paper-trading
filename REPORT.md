========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-29T09:12:21.547243Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          57408
  orderbook seviyesi     3066612
  tahmin snapshot          38304
  karar                    11814
  simüle fill               3087
  çözümlenmiş kova          1344

## Brier skoru  (düşük = iyi, 1302 kova)
  model                  0.1316
  piyasa (mid)           0.1334   n=1302
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0019  ±0.0037  %95 [-0.0054, +0.0091]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=186  0.1364 / 0.2107   fark +0.0743
    CHI   n=186  0.1269 / 0.1123   fark -0.0146
    DEN   n=186  0.1458 / 0.2037   fark +0.0578
    LAX   n=186  0.1241 / 0.0971   fark -0.0270
    MIA   n=186  0.1397 / 0.1137   fark -0.0261
    NY    n=186  0.1069 / 0.0842   fark -0.0228
    PHL   n=186  0.1412 / 0.1125   fark -0.0287
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       482         0.034         0.056   +0.022
  0.1-0.2       332         0.152         0.196   +0.044
  0.2-0.3       278         0.247         0.245   -0.002
  0.3-0.4       140         0.346         0.236   -0.111
  0.4-0.5        53         0.436         0.302   -0.134
  0.5-0.6        13         0.545         0.308   -0.237
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3026)
  işlem sayısı                    3026
  kazanan                         1213  (%40)
  ort. İDDİA EDİLEN edge       +16.06p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.00p   ±0.7p  %95 [+0.5p, +3.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3044.84 $
  PnL fee ÖNCESİ             +23885.30 $
  PnL fee SONRASI            +20840.46 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8083.70 $   %90 aralık [-14299.31, -1085.04]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1334 (model 0.1316)

  bizim (fee sonrası)            +20840.46 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
