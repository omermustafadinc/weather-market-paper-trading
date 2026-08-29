"""Döngü sürücüsünün testi.

Bu dosya bir hatadan doğdu: ilk sürüm alt komutu `python -m -m wxbot.collect`
olarak kuruyordu ve hata lokalde değil, üretimde ortaya çıktı. Komut kurma
artık saf bir fonksiyon ve testi var.
"""

from __future__ import annotations

import subprocess
import sys

import pytest

from wxbot import cycle


def test_komut_tek_m_ile_kurulur() -> None:
    cmd = cycle.build_command("wxbot.collect")
    assert cmd == [sys.executable, "-m", "wxbot.collect"]
    assert cmd.count("-m") == 1, f"çift -m: {cmd}"


def test_komut_argumanlari_ekler() -> None:
    cmd = cycle.build_command("wxbot.ingest", ["--db", "/tmp/x.db", "--quiet"])
    assert cmd == [sys.executable, "-m", "wxbot.ingest", "--db", "/tmp/x.db", "--quiet"]


@pytest.mark.parametrize("module", [
    "wxbot.collect", "wxbot.ingest", "wxbot.agent",
])
def test_cagrilan_modullerin_hepsi_calistirilabilir(module: str) -> None:
    """Döngünün çağırdığı her modül gerçekten `-m` ile koşabilmeli.

    --help ile çağırmak modülü import edip argparse'ı kurar; isim hatası,
    import hatası veya eksik __main__ burada yakalanır.
    """
    r = subprocess.run(cycle.build_command(module, ["--help"]),
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 0, f"{module} --help başarısız:\n{r.stderr[:400]}"


def test_dongu_adimlari_beklenen_modulleri_cagirir(monkeypatch) -> None:
    """one_cycle'ın hangi komutları hangi sırayla çalıştırdığını sabitle."""
    calls: list[list[str]] = []
    monkeypatch.setattr(cycle.subprocess, "call", lambda cmd, **kw: calls.append(cmd) or 0)
    monkeypatch.setattr(cycle.time, "sleep", lambda s: None)

    assert cycle.one_cycle("/tmp/t.db", delay_seconds=1) is True

    modules = [c[2] for c in calls]
    assert modules == [
        "wxbot.collect",   # karar anı kitabı + tahmin
        "wxbot.ingest",    # veritabanını kur
        "wxbot.agent",     # KARAR
        "wxbot.collect",   # gecikme sonrası kitap
        "wxbot.ingest",
        "wxbot.agent",     # fill
        "wxbot.ingest",    # sıfırdan kur + lookahead denetimi
    ]
    assert calls[2][3] == "decide"
    assert calls[5][3] == "fill"
    for c in calls:
        assert c.count("-m") == 1, f"çift -m: {c}"


def test_bir_adim_patlarsa_dongu_kesilir(monkeypatch) -> None:
    """İlk adım başarısızsa sonrakiler çalışmamalı — yarım veriyle karar verme."""
    calls: list[list[str]] = []

    def fail_first(cmd, **kw):
        calls.append(cmd)
        return 1 if len(calls) == 1 else 0

    monkeypatch.setattr(cycle.subprocess, "call", fail_first)
    monkeypatch.setattr(cycle.time, "sleep", lambda s: None)

    assert cycle.one_cycle("/tmp/t.db", delay_seconds=1) is False
    assert len(calls) == 1


def test_gecikme_gercekten_bekleniyor(monkeypatch) -> None:
    """45 saniye simüle edilmiyor, gerçekten bekleniyor."""
    slept: list[float] = []
    monkeypatch.setattr(cycle.subprocess, "call", lambda cmd, **kw: 0)
    monkeypatch.setattr(cycle.time, "sleep", lambda s: slept.append(s))

    cycle.one_cycle("/tmp/t.db", delay_seconds=45)
    assert 45 in slept


def test_tum_adimlar_ayni_slotu_kullanir(monkeypatch) -> None:
    """Slot döngü başında bir kez hesaplanmalı.

    Bu test bir hatadan doğdu: her adım kendi `now()`unu kullanıyordu ve döngü
    30 dakikalık slot sınırını aştığında karar adımı boş slota bakıp SIFIR karar
    üretiyordu — hata vermeden. Burada saati adım adım ilerletip aynı şeyi
    zorluyoruz.
    """
    from wxbot import clock

    calls: list[list[str]] = []
    # Her çağrıda saat 20 dakika ilerlesin: döngü kesin slot sınırı aşar.
    t = [clock.iso_to_us("2026-08-29T05:29:00Z")]

    def advancing_now() -> int:
        t[0] += 20 * 60 * 1_000_000
        return t[0]

    monkeypatch.setattr(cycle, "now_us", advancing_now)
    monkeypatch.setattr(cycle.subprocess, "call", lambda cmd, **kw: calls.append(cmd) or 0)
    monkeypatch.setattr(cycle.time, "sleep", lambda s: None)

    cycle.one_cycle("/tmp/t.db", delay_seconds=1)

    anchors = {c[c.index("--anchor-us") + 1] for c in calls if "--anchor-us" in c}
    slots = {c[c.index("--slot") + 1] for c in calls if "--slot" in c}
    assert len(anchors) == 1, f"adımlar farklı an kullanıyor: {anchors}"
    assert len(slots) == 1, f"adımlar farklı slot kullanıyor: {slots}"

    from wxbot import config as cfg
    from wxbot.db import slot_id_for
    assert slots.pop() == str(slot_id_for(int(anchors.pop()), cfg.MARKET_SLOT_SECONDS))


def test_toplama_ve_karar_ayni_slotta_bulusur(monkeypatch) -> None:
    """collect'in yazdığı slot ile agent'ın aradığı slot aynı olmalı."""
    calls: list[list[str]] = []
    monkeypatch.setattr(cycle.subprocess, "call", lambda cmd, **kw: calls.append(cmd) or 0)
    monkeypatch.setattr(cycle.time, "sleep", lambda s: None)
    cycle.one_cycle("/tmp/t.db", delay_seconds=1)

    from wxbot import config as cfg
    from wxbot.db import slot_id_for

    collect_slots = {slot_id_for(int(c[c.index("--anchor-us") + 1]),
                                 cfg.MARKET_SLOT_SECONDS)
                     for c in calls if c[2] == "wxbot.collect"}
    agent_slots = {int(c[c.index("--slot") + 1])
                   for c in calls if c[2] == "wxbot.agent"}
    assert collect_slots == agent_slots, (
        f"collect {collect_slots} yazıyor, agent {agent_slots} arıyor")
