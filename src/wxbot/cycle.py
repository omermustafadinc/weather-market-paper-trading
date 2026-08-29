"""Tam bir toplama-karar-fill döngüsü, tek komut.

Neden ayrı bir modül: GitHub'ın schedule event'i bu repoda 8.7 saatte ~35
pencereden yalnızca 1'ini tetikledi (~%3). Tetikleme sıklığını kontrol
edemiyoruz, ama her tetiklemeyi daha değerli yapabiliriz — bir koşu içinde
birden çok döngü çalıştırarak.

Bir döngü:
    1. karar anı kitabı + tahmin topla
    2. veritabanını kur, KARAR ver
    3. 45 sn bekle            <- gecikme simüle edilmiyor, yaşanıyor
    4. kitabı yeniden çek
    5. fill'i YENİ kitaba karşı hesapla
    6. sıfırdan kur + lookahead denetimi

Adımlar arasında çökülürse bir sonraki koşu kaldığı yerden devam eder:
her adım idempotent ve slot bazlı.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

from . import config as cfg
from . import db
from .clock import now_us, us_to_iso


def _run(args: list[str]) -> int:
    """Alt modülü ayrı süreçte çalıştır; biri patlarsa döngü devam etsin."""
    print(f"  $ {' '.join(args[2:])}", flush=True)
    return subprocess.call([sys.executable, "-m"] + args[1:])


def one_cycle(db_path: str, *, delay_seconds: int = cfg.FILL_DELAY_SECONDS,
              edge_margin: float | None = None) -> bool:
    """Tek döngü. Kritik bir adım başarısız olursa False döner."""
    print(f"\n=== döngü başlıyor {us_to_iso(now_us())} "
          f"(slot {db.slot_id_for(now_us(), cfg.MARKET_SLOT_SECONDS)}) ===", flush=True)

    if _run(["python", "-m", "wxbot.collect"]) != 0:
        print("  toplama hata verdi, döngü yarıda kesiliyor", file=sys.stderr)
        return False
    if _run(["python", "-m", "wxbot.ingest", "--db", db_path, "--rebuild", "--quiet"]) != 0:
        return False

    decide = ["python", "-m", "wxbot.agent", "decide", "--db", db_path]
    if edge_margin is not None:
        decide += ["--edge-margin", str(edge_margin)]
    if _run(decide) != 0:
        return False

    print(f"  … {delay_seconds} sn bekleniyor (karar -> fill gecikmesi)", flush=True)
    time.sleep(delay_seconds)

    if _run(["python", "-m", "wxbot.collect", "--purpose", "fill", "--markets-only"]) != 0:
        return False
    if _run(["python", "-m", "wxbot.ingest", "--db", db_path, "--quiet"]) != 0:
        return False
    if _run(["python", "-m", "wxbot.agent", "fill", "--db", db_path]) != 0:
        return False

    # Son söz: her şeyi sıfırdan kur ve lookahead denetiminden geçir.
    return _run(["python", "-m", "wxbot.ingest", "--db", "/tmp/verify.db",
                 "--rebuild", "--quiet"]) == 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Toplama-karar-fill döngüsü")
    ap.add_argument("--db", default="/tmp/wx.db")
    ap.add_argument("--cycles", type=int, default=1)
    ap.add_argument("--gap-seconds", type=int, default=cfg.MARKET_SLOT_SECONDS,
                    help="döngüler arası bekleme (varsayılan: bir slot)")
    ap.add_argument("--edge-margin", type=float, default=None)
    ap.add_argument("--commit-cmd", default=None,
                    help="her döngüden sonra çalıştırılacak komut (commit için)")
    args = ap.parse_args(argv)

    failures = 0
    for i in range(args.cycles):
        if not one_cycle(args.db, edge_margin=args.edge_margin):
            failures += 1
        # Veriyi her döngüden sonra kalıcı hâle getir: koşu yarıda kesilirse
        # önceki döngülerin verisi kaybolmasın.
        if args.commit_cmd:
            subprocess.call(args.commit_cmd, shell=True)
        if i + 1 < args.cycles:
            print(f"\n… bir sonraki döngüye {args.gap_seconds} sn", flush=True)
            time.sleep(args.gap_seconds)

    print(f"\n{args.cycles} döngü bitti, {failures} başarısız")
    return 1 if failures == args.cycles else 0


if __name__ == "__main__":
    raise SystemExit(main())
