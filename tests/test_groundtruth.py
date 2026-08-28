"""Ground truth ve bias yardımcılarının testi."""

from __future__ import annotations

import pytest

from wxbot.bias import daily_max_from_hourly, _stats
from wxbot.groundtruth import parse_cli

REAL_CLI = """
000
CDUS41 KOKX 280657
CLINYC

CLIMATE REPORT
NATIONAL WEATHER SERVICE NEW YORK, NY
257 AM EDT FRI AUG 28 2026

...THE CENTRAL PARK NY CLIMATE SUMMARY FOR AUGUST 27 2026...

WEATHER ITEM   OBSERVED TIME   RECORD YEAR NORMAL DEPARTURE LAST
                VALUE   (LST)  VALUE       VALUE  FROM      YEAR
...................................................................
TEMPERATURE (F)
 YESTERDAY
  MAXIMUM         77    250 PM 101    1948  82     -5       75
  MINIMUM         68    941 PM  50    1885  68      0       61
  AVERAGE         73                        75     -2       68
"""


def test_cli_hedef_gunu_metinden_okur() -> None:
    """Rapor sabah yayınlanıp ÖNCEKİ günü özetliyor; hedef günü yayın
    tarihinden çıkarmak bir gün kaydırırdı."""
    assert parse_cli(REAL_CLI) == ("2026-08-27", 77)


def test_cli_eksi_dereceyi_okur() -> None:
    txt = REAL_CLI.replace("MAXIMUM         77", "MAXIMUM        -12")
    assert parse_cli(txt) == ("2026-08-27", -12)


@pytest.mark.parametrize("txt", ["", "boş metin", "CLIMATE SUMMARY FOR SMARCH 3 2026"])
def test_cli_cozumlenemezse_none(txt) -> None:
    assert parse_cli(txt) is None


def test_cli_maksimum_yoksa_none() -> None:
    txt = REAL_CLI.replace("  MAXIMUM         77", "  MAKSIMUM        77")
    assert parse_cli(txt) is None


# ---------------------------------------------------------------------------


def test_gunluk_maksimum_yerel_gune_gore() -> None:
    times = ["2026-08-27T22:00", "2026-08-27T23:00",
             "2026-08-28T00:00", "2026-08-28T14:00", "2026-08-28T15:00"]
    vals = [70.0, 71.0, 60.0, 85.0, 84.0]
    assert daily_max_from_hourly(times, vals) == {"2026-08-27": 71.0, "2026-08-28": 85.0}


def test_gunluk_maksimum_none_atlar() -> None:
    times = ["2026-08-28T00:00", "2026-08-28T14:00"]
    assert daily_max_from_hourly(times, [None, 85.0]) == {"2026-08-28": 85.0}
    assert daily_max_from_hourly(times, [None, None]) == {}


def test_hata_istatistikleri() -> None:
    st = _stats([2.0, -2.0, 2.0, -2.0])
    assert st["bias"] == pytest.approx(0.0)      # işaretli ortalama
    assert st["mae"] == pytest.approx(2.0)       # mutlak hata
    assert st["rmse"] == pytest.approx(2.0)
    assert st["n"] == 4


def test_bias_isareti_tahmin_eksi_gozlem() -> None:
    """Pozitif bias = model sıcak tahmin ediyor. İşaret ters olsaydı
    düzeltme yanlış yöne uygulanırdı."""
    assert _stats([3.0, 3.0])["bias"] == pytest.approx(3.0)
