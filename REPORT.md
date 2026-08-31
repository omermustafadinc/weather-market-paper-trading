========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-08-31T23:24:54.574319Z
lead time     : 24 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot           5298
  orderbook seviyesi      292144
  tahmin snapshot           4284
  karar                      960
  simüle fill                240
  çözümlenmiş kova           162

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
    MIA   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 45.5 saat
    NY    2026-08-31  en erken tahmin 2026-08-29T06:27Z  -> lead 45.5 saat
    PHL   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 45.5 saat

  Daha uzun lead istiyorsak veri birikmesini beklemek gerek:
  toplama 2026-08-28 18:18Z'de başladı, o günün hedefleri için
  yeterince erken tahmin yok.

  Sayı uydurmuyoruz — biriktikçe rapor dolacak.

## İşlemler (191)
  işlem sayısı                     191
  kazanan                           57  (%30)
  ort. İDDİA EDİLEN edge       +13.35p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -8.86p   ±2.8p  %95 [-14.3p, -3.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    216.72 $
  PnL fee ÖNCESİ              -1225.85 $
  PnL fee SONRASI             -1442.57 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)        -454.36 $   %90 aralık [-2067.42, +1263.56]  (200 deneme)

  bizim (fee sonrası)             -1442.57 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.
