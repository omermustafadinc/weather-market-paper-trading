# Ön kayıt — 2026-09-10

Bu dosya, **veriye bakmadan önce değil, baktıktan sonra ama ona göre hiçbir şey
değiştirmeden önce** yazıldı. Amacı: bir hipotezi tarih damgasıyla sabitlemek ki
ileride "zaten öyle demiştim" denemesin ve sonuç sonradan yeniden yorumlanamasın.

## Gözlem (13 günlük veri, 516 kova, 1097 işlem)

7 şehirden **Austin (AUS) ve Denver (DEN)** modelin piyasadan anlamlı ölçüde
iyi olduğu iki şehir çıktı. Diğer beşinde model piyasadan kötü ya da farksız.

| şehir | Brier farkı (piyasa−model) | t | dönem 1 t | dönem 2 t |
|---|---:|---:|---:|---:|
| AUS | +0.0559 | 4.03 | 2.92 | 2.80 |
| DEN | +0.0671 | 3.89 | 2.37 | 3.10 |
| CHI | −0.0264 | −2.76 | −0.24 | −3.00 |
| PHL | −0.0328 | −2.48 | 0.04 | −3.05 |
| NY  | −0.0241 | −2.40 | −2.50 | −0.46 |
| MIA | −0.0102 | −0.70 | 0.38 | −1.49 |
| LAX | −0.0063 | −0.47 | −1.03 | 0.38 |

Bonferroni düzeltmesinden sonra (7 test, eşik t=2.69) AUS, DEN ve CHI ayakta
kalıyor. AUS ve DEN iki bağımsız dönemde de aynı yönde ve güçlü.

İşlem tarafı aynı ayrımı gösteriyor:

| grup | işlem | kazanan | medyan işlem | PnL (fee sonrası) |
|---|---:|---:|---:|---:|
| AUS + DEN | 235 | %57 | **+2.80 $** | **+10.598 $** |
| diğer 5 | 862 | %34 | −20.63 $ | −9.825 $ |

AUS/DEN kârı birkaç şanslı işleme dayanmıyor: medyan işlem pozitif, en iyi 10
işlem çıkarıldığında hâlâ +6.000 $, ve 13 günün 10'u kârlı.

## Hipotez

**H1:** Ensemble modeli, Austin ve Denver'ın günlük maksimum sıcaklığını
Kalshi piyasasından daha iyi tahmin ediyor; bu avantaj işlem maliyetlerini
aşacak büyüklükte.

Olası mekanizma (test edilmedi, yalnızca makul bir açıklama): her iki şehir de
yüksek günlük değişkenliğe sahip karasal iklimler — Denver'da üç günde 91→85→66
°F gördük. Piyasa bu değişkenliği olduğundan dar fiyatlıyorsa, saçılımı
yakalayan bir ensemble gerçek avantaj taşır.

## Neden ŞİMDİ buna göre hareket etmiyorum

1. **13 gün, tek bir mevsimsel pencere.** İki "bağımsız dönem" aslında bağımsız
   değil: aynı hava rejimi iki haftaya yayılabilir.
2. **AUS ve DEN muhtemelen tek gözlem.** İkisi de iç/güneybatı; ortak bir
   bölgesel rejim ikisini birden sürükleyebilir. İki şehir = iki bağımsız kanıt
   DEĞİL.
3. **Post-hoc seçim.** 7 şehre baktım, 2'sini seçtim. Bonferroni bunu kısmen
   karşılıyor ama tamamen değil.
4. **Bias düzeltmesi hâlâ uygulanmadı.** Model şu an bilerek düzeltilmemiş;
   AUS/DEN avantajı bu düzeltilmemiş hâlin tesadüfi bir sonucu olabilir.
5. Genel Brier farkı hâlâ **anlamsız** (+0.0047 ±0.0053). Şehir etkileri
   birbirini götürüyor.

## Sınama planı — bu tarihten SONRAKİ veriyle

Sistem **değiştirilmeyecek**: 7 şehrin hepsinde işlem yapmaya devam edecek.
Yalnızca böylece diğer beş şehir kontrol grubu olarak kalır.

**2026-10-08 civarı (≈4 hafta sonra)** yalnızca `target_date > 2026-09-10` olan
veriye bakılacak ve şu üçü kontrol edilecek:

- [ ] AUS ve DEN'de Brier farkı hâlâ pozitif ve t > 2
- [ ] AUS+DEN medyan işlemi hâlâ pozitif
- [ ] AUS+DEN PnL'i fee sonrası hâlâ pozitif, ve en iyi %10 işlem çıkarıldığında da pozitif

**Üçü birden tutmazsa hipotez reddedilir.** Kısmen tutarsa da reddedilir —
"kısmen tuttu" diye kurtarma yapılmayacak.

Tutarsa bile bu bir edge kanıtı değil, yalnızca "daha uzun ve dikkatli bir
çalışmayı hak ediyor" demektir. O noktada bias düzeltmesi eklenip aynı test
tekrarlanmalı.

## Değiştirilmeyecekler

Bu tarihe kadar: eşik (`edge_margin=0.03`), Kelly çarpanı (0.25), pozisyon
limitleri, uç fiyat sınırları, şehir listesi, model ağırlıklandırması, bant
genişliği kuralı. Hiçbiri sonuca bakarak ayarlanmayacak.
