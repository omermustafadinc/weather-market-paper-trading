"""Ensemble tahminden olasılık dağılımı ve kova olasılıkları.

Nokta tahmini değil dağılım üretiyoruz. Üç adım:

  1. **Üyeleri topla.** ~180 üye, 6 modelden. Karar anından ÖNCE çekilmiş en
     yeni snapshot kullanılır — sonrasını görmek lookahead olurdu.
  2. **Dağılıma çevir.** Üyeler ham örnek olarak değil, Gauss çekirdekle
     "giydirilerek" (kernel dressing) kullanılıyor. Nedeni aşağıda.
  3. **Kovalara integre et.** Kalshi kovaları TAM SAYI derece üzerinden
     tanımlı; sürekli dağılımdan geçerken ±0.5 düzeltmesi şart.

Üç tasarım kararı ve gerekçeleri
--------------------------------

**Neden model başına eşit ağırlık, üye başına değil.** ECMWF 51, BOM 18 üye
veriyor. Üye başına eşit ağırlık ECMWF'e %28, BOM'a %10 pay verir — ama üye
sayısı bir *hesaplama tercihi*, beceri ölçüsü değil. Bir modelin daha çok üye
koşturması onu daha doğru yapmaz. Varsayılan: her model eşit ağırlıklı, ağırlığı
kendi üyelerine eşit dağıtılır. `weighting="member"` ile diğeri seçilebilir.

**Neden ham ampirik dağılım değil.** Ham üyelerle çalışırsak ensemble aralığının
dışındaki kovalara olasılık 0 çıkar. O zaman 2 sentlik bir kontrat için model
"%0" der ve strateji sonsuz edge görür — tam da hayali edge'in doğduğu yer.
Ayrıca ensemble'lar bilinen biçimde **dar saçılımlıdır** (underdispersed).

**Neden Silverman bant genişliği.** Elle bir sayı seçmek serbest parametre
eklemek olurdu ve o parametreyi sonuca bakarak ayarlama baskısı doğardı.
Silverman kuralı bant genişliğini verinin kendisinden türetir — ayarlanacak bir
şey yok. Kuralın varsayımı (iid örnek) ensemble üyeleri için tam geçerli değil;
bu bilinen bir yaklaşıklık, canlı veri birikince kalibrasyon eğrisiyle
ölçülecek ve gerekirse yerini veriden fit edilmiş bir değere bırakacak.

Kalibre EDİLMEMİŞ olduğu için sonuçlar buna göre okunmalı — `Distribution`
nesnesi hangi ayarlarla kurulduğunu taşır ve karar defterine yazılır.
"""

from __future__ import annotations

import json
import math
import sqlite3
from dataclasses import dataclass, field
from typing import Iterable, Literal, Sequence

Weighting = Literal["model", "member"]

#: Olasılık tabanı/tavanı. Ham ensemble uçlarda 0 üretir; 0 olasılık "imkânsız"
#: demektir ve Kelly'yi patlatır. Hiçbir hava tahmini o kadar kesin değil.
PROB_FLOOR = 0.001

#: Kalshi sıcaklık kovaları tam sayı derece üzerinden çözümlenir (NWS CLI raporu
#: tam derece verir). Sürekli dağılımdan tam sayıya geçerken yarım derece.
HALF_DEGREE = 0.5


class ModelError(ValueError):
    pass


# ---------------------------------------------------------------------------
# Kovalar
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Bucket:
    """Bir Kalshi kovası ve karşılık geldiği sürekli aralık.

    Üretim verisinden doğrulanmış eşleme:
        less,  cap=79            -> "78° or below"  -> T_int <= 78
        between, floor=79 cap=80 -> "79° to 80°"    -> 79 <= T_int <= 80
        greater, floor=86        -> "87° or above"  -> T_int >= 87
    """

    ticker: str
    kind: str                      # 'less' | 'between' | 'greater'
    floor_strike: float | None
    cap_strike: float | None
    subtitle: str = ""

    def int_bounds(self) -> tuple[int | None, int | None]:
        """Kovanın kapsadığı TAM SAYI derece aralığı (dahil, dahil)."""
        if self.kind == "less":
            if self.cap_strike is None:
                raise ModelError(f"{self.ticker}: 'less' kovasında cap_strike yok")
            return (None, int(self.cap_strike) - 1)
        if self.kind == "greater":
            if self.floor_strike is None:
                raise ModelError(f"{self.ticker}: 'greater' kovasında floor_strike yok")
            return (int(self.floor_strike) + 1, None)
        if self.kind == "between":
            if self.floor_strike is None or self.cap_strike is None:
                raise ModelError(f"{self.ticker}: 'between' kovasında sınır eksik")
            return (int(self.floor_strike), int(self.cap_strike))
        raise ModelError(f"{self.ticker}: bilinmeyen strike_type {self.kind!r}")

    def continuous_bounds(self) -> tuple[float, float]:
        """Sürekli dağılımda integre edilecek aralık (±0.5 düzeltmesiyle)."""
        lo_i, hi_i = self.int_bounds()
        lo = -math.inf if lo_i is None else lo_i - HALF_DEGREE
        hi = math.inf if hi_i is None else hi_i + HALF_DEGREE
        return lo, hi

    def contains_int(self, t: int) -> bool:
        lo, hi = self.int_bounds()
        return (lo is None or t >= lo) and (hi is None or t <= hi)

    @classmethod
    def from_market(cls, market: dict) -> "Bucket":
        return cls(
            ticker=market["ticker"],
            kind=str(market.get("strike_type") or ""),
            floor_strike=_f(market.get("floor_strike")),
            cap_strike=_f(market.get("cap_strike")),
            subtitle=str(market.get("yes_sub_title") or ""),
        )


def _f(v: object) -> float | None:
    return None if v is None else float(v)  # type: ignore[arg-type]


def check_ladder(buckets: Sequence[Bucket]) -> None:
    """Kovalar birbirini dışlamalı ve tüm tam sayıları kapsamalı.

    Kalshi olayı `mutually_exclusive: true` diyor; bunu doğrulamak bedava bir
    tutarlılık kontrolü. Kova yapısı sessizce değişirse burası uyarır.
    """
    if not buckets:
        raise ModelError("kova listesi boş")
    lo = min((b.int_bounds()[0] for b in buckets if b.int_bounds()[0] is not None),
             default=0)
    hi = max((b.int_bounds()[1] for b in buckets if b.int_bounds()[1] is not None),
             default=0)
    for t in range(int(lo) - 5, int(hi) + 6):
        hits = [b.ticker for b in buckets if b.contains_int(t)]
        if len(hits) != 1:
            raise ModelError(
                f"{t}° tam sayısı {len(hits)} kovaya düşüyor ({hits}); "
                "kovalar birbirini dışlamıyor veya boşluk var"
            )


# ---------------------------------------------------------------------------
# Ensemble örneği
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class EnsembleSample:
    """Bir (şehir, hedef gün) için model başına üye değerleri."""

    location_key: str
    target_date: str
    by_model: dict[str, list[float]]
    #: Kullanılan snapshot'ların en yenisi — kararın `data_asof`'una girer.
    data_asof_us: int = 0
    snapshot_ids: tuple[int, ...] = ()

    @property
    def model_count(self) -> int:
        return sum(1 for v in self.by_model.values() if v)

    @property
    def member_count(self) -> int:
        return sum(len(v) for v in self.by_model.values())

    def all_members(self) -> list[float]:
        return [x for v in self.by_model.values() for x in v]

    def weighted_members(self, weighting: Weighting = "model") -> list[tuple[float, float]]:
        """(değer, ağırlık) çiftleri; ağırlıklar toplamı 1."""
        live = {m: v for m, v in self.by_model.items() if v}
        if not live:
            raise ModelError(f"{self.location_key}/{self.target_date}: üye yok")
        out: list[tuple[float, float]] = []
        if weighting == "member":
            n = sum(len(v) for v in live.values())
            for vals in live.values():
                out += [(x, 1.0 / n) for x in vals]
        else:
            per_model = 1.0 / len(live)
            for vals in live.values():
                w = per_model / len(vals)
                out += [(x, w) for x in vals]
        return out


# ---------------------------------------------------------------------------
# Dağılım
# ---------------------------------------------------------------------------


def _norm_cdf(z: float) -> float:
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def silverman_bandwidth(values: Sequence[float]) -> float:
    """Silverman'ın temel kuralı: h = 0.9 · min(σ, IQR/1.34) · n^(-1/5).

    Elle seçilmiş bir sayı değil — veriden türetiliyor, dolayısıyla sonuca
    bakarak ayarlanacak bir serbest parametre yok.
    """
    n = len(values)
    if n < 2:
        return 1.0
    mean = sum(values) / n
    sd = math.sqrt(sum((x - mean) ** 2 for x in values) / (n - 1))
    s = sorted(values)
    q1 = s[int(0.25 * (n - 1))]
    q3 = s[int(0.75 * (n - 1))]
    scale = min(sd, (q3 - q1) / 1.34) if q3 > q1 else sd
    if scale <= 0:
        scale = sd if sd > 0 else 1.0
    return max(0.9 * scale * n ** (-0.2), 0.05)


@dataclass(frozen=True, slots=True)
class Distribution:
    """Kernel ile giydirilmiş öngörü dağılımı.

    Nasıl kurulduğunu taşır: karar defterine yazılacak ve sonuç yeniden
    üretilebilecek.
    """

    points: tuple[tuple[float, float], ...]   # (değer, ağırlık)
    bandwidth: float
    weighting: Weighting
    bias: float = 0.0

    def cdf(self, x: float) -> float:
        if self.bandwidth <= 0:
            return sum(w for v, w in self.points if v + self.bias <= x)
        return sum(w * _norm_cdf((x - (v + self.bias)) / self.bandwidth)
                   for v, w in self.points)

    def interval_prob(self, lo: float, hi: float) -> float:
        a = 0.0 if lo == -math.inf else self.cdf(lo)
        b = 1.0 if hi == math.inf else self.cdf(hi)
        return max(0.0, b - a)

    def mean(self) -> float:
        return sum(w * (v + self.bias) for v, w in self.points)

    def quantile(self, p: float, lo: float = -60.0, hi: float = 160.0) -> float:
        for _ in range(60):
            mid = (lo + hi) / 2
            if self.cdf(mid) < p:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    def describe(self) -> dict:
        return {"bandwidth": round(self.bandwidth, 4), "weighting": self.weighting,
                "bias": round(self.bias, 4), "n_points": len(self.points),
                "mean": round(self.mean(), 3),
                "p10": round(self.quantile(0.10), 2),
                "p50": round(self.quantile(0.50), 2),
                "p90": round(self.quantile(0.90), 2)}


def build_distribution(
    sample: EnsembleSample, *, weighting: Weighting = "model",
    bandwidth: float | None = None, bias: float = 0.0,
) -> Distribution:
    pts = sample.weighted_members(weighting)
    h = silverman_bandwidth([v for v, _ in pts]) if bandwidth is None else bandwidth
    return Distribution(tuple(pts), h, weighting, bias)


# ---------------------------------------------------------------------------
# Kova olasılıkları
# ---------------------------------------------------------------------------


def bucket_probabilities(
    dist: Distribution, buckets: Sequence[Bucket], *, validate: bool = True,
) -> dict[str, float]:
    """Her kova için olasılık. Toplamı 1'e normalize edilir.

    Normalizasyon meşru: kovalar birbirini dışlıyor ve tüm sonuç uzayını
    kapsıyor (`check_ladder` bunu doğruluyor), dolayısıyla toplam zaten 1
    olmalı. Sapma yalnızca sayısal integrasyondan gelir.
    """
    if validate:
        check_ladder(buckets)

    raw = {}
    for b in buckets:
        lo, hi = b.continuous_bounds()
        raw[b.ticker] = dist.interval_prob(lo, hi)

    total = sum(raw.values())
    if total <= 0:
        raise ModelError("tüm kova olasılıkları sıfır — dağılım kovaların dışında")

    out = {}
    for t, p in raw.items():
        p = p / total
        out[t] = min(1.0 - PROB_FLOOR, max(PROB_FLOOR, p))

    # Taban/tavan uygulandıktan sonra toplam 1'den kayar; yeniden normalize et.
    s = sum(out.values())
    return {t: p / s for t, p in out.items()}


# ---------------------------------------------------------------------------
# Veritabanından örnek kurma — lookahead'e kapalı
# ---------------------------------------------------------------------------


def load_ensemble_sample(
    conn: sqlite3.Connection, location_key: str, target_date: str, *,
    as_of_us: int, variable: str = "temperature_2m_max",
) -> EnsembleSample:
    """`as_of_us` anına kadar çekilmiş EN YENİ tahmini model başına topla.

    `fetched_at_us <= as_of_us` koşulu lookahead'e karşı buradaki savunma:
    karar anından sonra gelen bir tahmin hiç görülmez.
    """
    rows = conn.execute(
        """SELECT f.model, f.raw_json, f.fetched_at_us, f.id
           FROM forecast_snapshots f
           JOIN (SELECT model, max(fetched_at_us) AS mx
                 FROM forecast_snapshots
                 WHERE location_key = ? AND target_date = ? AND variable = ?
                   AND fetched_at_us <= ?
                 GROUP BY model) latest
             ON latest.model = f.model AND latest.mx = f.fetched_at_us
           WHERE f.location_key = ? AND f.target_date = ? AND f.variable = ?
             AND f.fetched_at_us <= ?""",
        (location_key, target_date, variable, as_of_us,
         location_key, target_date, variable, as_of_us),
    ).fetchall()

    by_model: dict[str, list[float]] = {}
    asof = 0
    ids: list[int] = []
    for r in rows:
        vals = extract_members(json.loads(r["raw_json"]), target_date, variable)
        if not vals:
            continue
        by_model[r["model"]] = vals
        asof = max(asof, int(r["fetched_at_us"]))
        ids.append(int(r["id"]))

    return EnsembleSample(location_key, target_date, by_model, asof, tuple(sorted(ids)))


def extract_members(payload: dict, target_date: str, variable: str) -> list[float]:
    """Open-Meteo yanıtından hedef güne ait üye değerleri."""
    daily = payload.get("daily") or {}
    times = daily.get("time") or []
    if target_date not in times:
        return []
    i = times.index(target_date)
    out = []
    for k, series in daily.items():
        if k == "time" or not k.startswith(variable):
            continue
        try:
            v = series[i]
        except (IndexError, TypeError):
            continue
        if v is not None:
            out.append(float(v))
    return out


def load_buckets(conn: sqlite3.Connection, event_ticker: str,
                 *, as_of_us: int) -> list[Bucket]:
    """Bir olayın kovalarını, `as_of_us`'a kadarki en yeni metadata'dan kur."""
    rows = conn.execute(
        """SELECT market_ticker, raw_market_json, max(fetched_at_us)
           FROM market_snapshots
           WHERE event_ticker = ? AND fetched_at_us <= ?
           GROUP BY market_ticker ORDER BY market_ticker""",
        (event_ticker, as_of_us),
    ).fetchall()
    return [Bucket.from_market(json.loads(r["raw_market_json"])) for r in rows]
