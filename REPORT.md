========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-01T12:34:48.672058Z
lead time     : 24 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot           5982
  orderbook seviyesi      331026
  tahmin snapshot           4914
  karar                     1050
  simüle fill                266
  çözümlenmiş kova           180

## KALİBRASYON: VERİ YOK
  24 saatlik lead time'da değerlendirilebilir tahmin-sonuç çifti yok.

  Çözümlenmiş günler için ELDEKİ en uzun lead time:
    AUS   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -13.3 saat
    CHI   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -13.3 saat
    DEN   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -12.3 saat
    LAX   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -11.3 saat
    MIA   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -14.3 saat
    NY    2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -14.3 saat
    PHL   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -14.3 saat
    AUS   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 10.7 saat
    CHI   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 10.7 saat
    DEN   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 11.7 saat
    LAX   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 12.7 saat
    MIA   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 9.7 saat
    NY    2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 9.7 saat
    PHL   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 9.7 saat
    AUS   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 34.7 saat
    CHI   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 34.7 saat
    DEN   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 35.7 saat
    LAX   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 36.7 saat
    MIA   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 33.7 saat
    NY    2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 33.7 saat
    PHL   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 33.7 saat
    AUS   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 46.5 saat
    CHI   2026-08-31  en erken tahmin 2026-08-29T06:27Z  -> lead 46.5 saat
    DEN   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 47.5 saat
    LAX   2026-08-31  en erken tahmin 2026-08-29T07:06Z  -> lead 47.9 saat
    MIA   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 45.5 saat
    NY    2026-08-31  en erken tahmin 2026-08-29T06:27Z  -> lead 45.5 saat
    PHL   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 45.5 saat
    AUS   2026-09-01  en erken tahmin 2026-08-30T05:55Z  -> lead 47.1 saat
    DEN   2026-09-01  en erken tahmin 2026-08-30T06:20Z  -> lead 47.7 saat

  Daha uzun lead istiyorsak veri birikmesini beklemek gerek:
  toplama 2026-08-28 18:18Z'de başladı, o günün hedefleri için
  yeterince erken tahmin yok.

  Sayı uydurmuyoruz — biriktikçe rapor dolacak.

## İşlemler (213)
  işlem sayısı                     213
  kazanan                           67  (%31)
  ort. İDDİA EDİLEN edge       +13.26p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -6.42p   ±2.8p  %95 [-11.8p, -1.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    240.66 $
  PnL fee ÖNCESİ               -268.97 $
  PnL fee SONRASI              -509.63 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)        -254.66 $   %90 aralık [-2326.09, +1806.12]  (200 deneme)

  bizim (fee sonrası)              -509.63 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.
