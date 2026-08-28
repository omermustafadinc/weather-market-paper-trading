"""Strateji: edge, eşik, kesirli Kelly ve limitler.

edge = model_olasılığı − piyasa_fiyatı (aynı tarafta, aynı birimde).

Bir kovada iki yön var:
    YES al  ->  fiyat = yes_ask,  kazanma olasılığı = q
    NO  al  ->  fiyat = no_ask,   kazanma olasılığı = 1 − q

Kelly
-----
p fiyatından alınan, kazanınca 1 ödeyen bir kontrat için:
    f* = (q − p) / (1 − p) = edge / (1 − p)
Kesirli Kelly uygulanır (varsayılan 1/4, kullanıcı şartı gereği tavan da 1/4).

Eşik neden fee'nin ÜSTÜNDE
--------------------------
Kalshi taker fee'si 50 sentte kontrat başına ~1.75 sent. Fee'ye eşit bir edge
sıfır beklenen getiri demektir; üstüne marj koymazsak gürültüyü işleme çeviririz.
Marjın kendisi bir varsayım — ölçülmüş bir değer değil — ve bu yüzden HER karar
edge'iyle birlikte loglanıyor: rapor, sonucu farklı eşiklerde yeniden
hesaplayabiliyor. Böylece tek bir eşik seçip "en iyi" sonucu göstermek yerine
eşiğe duyarlılığın tamamı görülüyor.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from .fills import DOLLAR_DCENTS, taker_fee_dcents


@dataclass(frozen=True, slots=True)
class StrategyConfig:
    #: Kesirli Kelly çarpanı. Kullanıcı şartı: en fazla 1/4.
    kelly_fraction: float = 0.25

    #: Fee'nin ÜSTÜNE aranan asgari edge (olasılık puanı, 0.03 = 3 puan).
    #: Ölçülmüş değil, varsayım — bkz. modül açıklaması.
    edge_margin: float = 0.03

    #: Kâğıt üzerindeki sermaye (desi-sent). Varsayılan 1.000 $.
    bankroll_dcents: float = 1_000_000.0

    #: Tek pozisyona ayrılabilecek en yüksek sermaye oranı.
    max_position_fraction: float = 0.02

    #: Aynı anda açık toplam pozisyonun en yüksek sermaye oranı.
    max_total_exposure_fraction: float = 0.20

    #: Uçlarda işlem yapma sınırı. Model uçlarda en güvenilmez olduğu yerdir
    #: (olasılık tabanı zaten yapay); 3 sentlik bir kontratta "model %0.1 diyor"
    #: demek gerçek bir bilgi değil.
    min_price_dcents: int = 30
    max_price_dcents: int = 970

    def __post_init__(self) -> None:
        if not 0.0 < self.kelly_fraction <= 0.25:
            raise ValueError("kelly_fraction (0, 0.25] aralığında olmalı")


@dataclass(frozen=True, slots=True)
class Candidate:
    """Bir kovada bir yön için değerlendirme."""

    market_ticker: str
    side: str                 # 'yes' | 'no'
    price_dcents: int         # bu tarafı almanın maliyeti
    model_prob: float         # bu tarafın kazanma olasılığı
    edge: float               # model_prob − fiyat
    fee_per_contract: float   # desi-sent
    net_edge: float           # edge − fee (olasılık puanı cinsinden)
    kelly: float              # kesirli Kelly oranı
    contracts: float          # limitler uygulandıktan sonra hedef adet
    reason: str               # neden işlem yapıldı / yapılmadı
    #: Adedi hangi kısıt belirledi: 'kelly' | 'pozisyon_tavanı' | 'toplam_limit'.
    #: Kelly neredeyse hiç bağlamıyorsa bunu bilmek gerekir — o zaman "kesirli
    #: Kelly kullanıyoruz" demek süslemeden ibaret olur.
    binding: str = ""

    @property
    def tradeable(self) -> bool:
        return self.contracts > 0


def _fee_points(price_dcents: int, fee_multiplier: float) -> float:
    """Kontrat başına fee'yi olasılık puanına çevir (edge ile aynı birim)."""
    return taker_fee_dcents(1.0, price_dcents, multiplier=fee_multiplier) / DOLLAR_DCENTS


def evaluate(
    market_ticker: str, side: str, price_dcents: int | None, model_prob: float,
    cfg: StrategyConfig, *, fee_multiplier: float = 1.0,
    current_exposure_dcents: float = 0.0,
) -> Candidate:
    """Bir yönü değerlendir. İşlem yapılmasa da gerekçeli bir Candidate döner."""
    def no(reason: str, edge: float = 0.0, fee: float = 0.0,
           net: float = 0.0, kelly: float = 0.0) -> Candidate:
        return Candidate(market_ticker, side, price_dcents or 0, model_prob,
                         edge, fee, net, kelly, 0.0, reason, "işlem_yok")

    if price_dcents is None or price_dcents <= 0:
        return no("bu tarafta alış yok (kitap tek taraflı)")
    if price_dcents >= DOLLAR_DCENTS:
        return no("fiyat 1.00 veya üstü")
    if price_dcents < cfg.min_price_dcents:
        return no(f"fiyat {price_dcents/10:.1f}c < uç sınırı "
                  f"{cfg.min_price_dcents/10:.1f}c (modelin en güvenilmez olduğu bölge)")
    if price_dcents > cfg.max_price_dcents:
        return no(f"fiyat {price_dcents/10:.1f}c > uç sınırı "
                  f"{cfg.max_price_dcents/10:.1f}c")

    p = price_dcents / DOLLAR_DCENTS
    edge = model_prob - p
    fee = _fee_points(price_dcents, fee_multiplier)
    net = edge - fee

    if net <= 0:
        return no(f"net edge {net*100:+.2f}p <= 0 (brüt {edge*100:+.2f}p, "
                  f"fee {fee*100:.2f}p)", edge, fee, net)
    if net < cfg.edge_margin:
        return no(f"net edge {net*100:+.2f}p < eşik {cfg.edge_margin*100:.2f}p",
                  edge, fee, net)

    kelly_full = edge / (1.0 - p)
    kelly = max(0.0, kelly_full * cfg.kelly_fraction)

    # Üç aday büyüklük; en küçüğü kazanır ve hangisi olduğunu kaydediyoruz.
    stake_kelly = kelly * cfg.bankroll_dcents
    stake_cap = cfg.max_position_fraction * cfg.bankroll_dcents
    room = cfg.max_total_exposure_fraction * cfg.bankroll_dcents - current_exposure_dcents
    if room <= 0:
        return no("toplam pozisyon limiti dolu", edge, fee, net, kelly)

    stake, binding = min(
        ((stake_kelly, "kelly"), (stake_cap, "pozisyon_tavanı"), (room, "toplam_limit")),
        key=lambda x: x[0],
    )

    contracts = stake / price_dcents
    if contracts < 1.0:
        return no(f"hesaplanan adet {contracts:.2f} < 1 kontrat", edge, fee, net, kelly)

    return Candidate(
        market_ticker, side, price_dcents, model_prob, edge, fee, net, kelly,
        contracts,
        f"net edge {net*100:+.2f}p >= eşik {cfg.edge_margin*100:.2f}p; "
        f"kelly {kelly_full:.3f}×{cfg.kelly_fraction}={kelly:.3f}; "
        f"bağlayan kısıt: {binding} -> {contracts:.1f} kontrat @ {price_dcents/10:.1f}c",
        binding,
    )


def best_candidate(
    market_ticker: str, model_prob: float, yes_ask: int | None, no_ask: int | None,
    cfg: StrategyConfig, *, fee_multiplier: float = 1.0,
    current_exposure_dcents: float = 0.0,
) -> Candidate:
    """İki yönü değerlendir, işlem yapılabilir olanı (yoksa daha bilgilendirici
    gerekçeyi) döndür."""
    cands = [
        evaluate(market_ticker, "yes", yes_ask, model_prob, cfg,
                 fee_multiplier=fee_multiplier,
                 current_exposure_dcents=current_exposure_dcents),
        evaluate(market_ticker, "no", no_ask, 1.0 - model_prob, cfg,
                 fee_multiplier=fee_multiplier,
                 current_exposure_dcents=current_exposure_dcents),
    ]
    tradeable = [c for c in cands if c.tradeable]
    if tradeable:
        return max(tradeable, key=lambda c: c.net_edge)
    # İşlem yok: en yakın olanın gerekçesi daha bilgilendirici.
    return max(cands, key=lambda c: c.net_edge)
