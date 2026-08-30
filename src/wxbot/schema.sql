-- Hava durumu kâğıt-işlem ajanı — SQLite şeması
--
-- İki tasarım ilkesi:
--   1. HAM VERİ APPEND-ONLY. raw_json sütunları asla UPDATE edilmez. Türetilmiş
--      alanlar kolaylık içindir; anlaşmazlıkta ham veri kazanır.
--   2. LOOKAHEAD DB SEVİYESİNDE İMKÂNSIZ. Zaman kuralları CHECK kısıtı olarak
--      burada; uygulama hatası veriyi kirletemez. Testler bunun üstüne gelir.

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------------
-- Meta
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- Her koşu. Çökme sonrası kaldığı yerden devam ve idempotanlık buna dayanıyor.
CREATE TABLE IF NOT EXISTS runs (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    run_uid        TEXT    NOT NULL UNIQUE,   -- dışarıdan verilen (GH run id vb.)
    slot_id        INTEGER NOT NULL,          -- floor(epoch_s / slot_seconds)
    slot_seconds   INTEGER NOT NULL,
    started_at_us  INTEGER NOT NULL,
    finished_at_us INTEGER,
    status         TEXT    NOT NULL DEFAULT 'running'
                   CHECK (status IN ('running', 'ok', 'failed')),
    error          TEXT,
    CHECK (finished_at_us IS NULL OR finished_at_us >= started_at_us)
);
CREATE INDEX IF NOT EXISTS idx_runs_slot ON runs (slot_id);

-- ---------------------------------------------------------------------------
-- Ham piyasa verisi (append-only)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS market_snapshots (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id          INTEGER NOT NULL REFERENCES runs (id),
    slot_id         INTEGER NOT NULL,
    -- 'decision' = karar anındaki kitap, 'fill' = gecikme sonrası ikinci kitap.
    -- İkisi ayrı tutuluyor ki fill gerçekten sonraki fiyata karşı hesaplansın.
    purpose         TEXT    NOT NULL CHECK (purpose IN ('decision', 'fill')),

    venue           TEXT    NOT NULL,
    series_ticker   TEXT    NOT NULL,
    event_ticker    TEXT    NOT NULL,
    market_ticker   TEXT    NOT NULL,

    fetched_at_us   INTEGER NOT NULL,   -- data_asof'un TEK kaynağı (yanıt alınma anı)
    fetched_at_iso  TEXT    NOT NULL,
    source_url      TEXT    NOT NULL,
    raw_market_json TEXT    NOT NULL,   -- ham; asla üzerine yazılmaz
    raw_book_json   TEXT    NOT NULL,   -- ham orderbook; asla üzerine yazılmaz

    -- Türetilmiş kolaylık alanları. Fiyatlar DESİ-SENT (1/1000 dolar) tamsayı:
    -- hava piyasaları uçlarda 0.1 sent adımla hareket ediyor (tapered_deci_cent),
    -- sent'e yuvarlamak ucuz kontratlarda hayali edge üretirdi.
    yes_bid_dcents  INTEGER,
    yes_ask_dcents  INTEGER,
    volume          REAL,
    open_interest   REAL,

    -- Aynı slot + aynı amaç için tek satır -> collector idempotent.
    UNIQUE (venue, market_ticker, slot_id, purpose)
);
CREATE INDEX IF NOT EXISTS idx_ms_ticker_time
    ON market_snapshots (market_ticker, fetched_at_us);
CREATE INDEX IF NOT EXISTS idx_ms_slot ON market_snapshots (slot_id, purpose);

-- Orderbook seviyeleri, snapshot'tan normalize. TÜM seviyeler, mid değil.
CREATE TABLE IF NOT EXISTS orderbook_levels (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id  INTEGER NOT NULL REFERENCES market_snapshots (id) ON DELETE CASCADE,
    side         TEXT    NOT NULL CHECK (side IN ('yes', 'no')),
    price_dcents INTEGER NOT NULL CHECK (price_dcents BETWEEN 0 AND 1000),
    quantity     REAL    NOT NULL CHECK (quantity >= 0),
    level_rank   INTEGER NOT NULL,   -- 0 = en iyi fiyat
    UNIQUE (snapshot_id, side, price_dcents)
);
CREATE INDEX IF NOT EXISTS idx_obl_snap ON orderbook_levels (snapshot_id, side, level_rank);

-- ---------------------------------------------------------------------------
-- Ham tahmin verisi (append-only)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS forecast_snapshots (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id         INTEGER NOT NULL REFERENCES runs (id),
    slot_id        INTEGER NOT NULL,

    provider       TEXT    NOT NULL,   -- 'open-meteo'
    model          TEXT    NOT NULL,   -- 'ecmwf_ifs025' vb.
    location_key   TEXT    NOT NULL,   -- 'NY', 'CHI', ...
    latitude       REAL    NOT NULL,
    longitude      REAL    NOT NULL,
    variable       TEXT    NOT NULL,   -- 'temperature_2m_max'
    target_date    TEXT    NOT NULL,   -- yerel hedef gün (YYYY-MM-DD)

    fetched_at_us  INTEGER NOT NULL,
    fetched_at_iso TEXT    NOT NULL,
    source_url     TEXT    NOT NULL,
    raw_json       TEXT    NOT NULL,   -- ham; asla üzerine yazılmaz

    member_count   INTEGER NOT NULL CHECK (member_count >= 0),

    UNIQUE (provider, model, location_key, variable, target_date, slot_id)
);
CREATE INDEX IF NOT EXISTS idx_fs_lookup
    ON forecast_snapshots (location_key, target_date, fetched_at_us);

-- ---------------------------------------------------------------------------
-- Kararlar — HER karar loglanır, işlem yapmama dahil
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS decisions (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id             INTEGER NOT NULL REFERENCES runs (id),
    slot_id            INTEGER NOT NULL,

    venue              TEXT    NOT NULL,
    market_ticker      TEXT    NOT NULL,
    event_ticker       TEXT    NOT NULL,
    target_date        TEXT    NOT NULL,

    -- ===== LOOKAHEAD YASAĞININ KALBİ =====
    -- data_asof: karara giren TÜM girdilerin en YENİSİNİN zamanı.
    -- decision_at: kararın verildiği an.
    data_asof_us       INTEGER NOT NULL,
    data_asof_iso      TEXT    NOT NULL,
    decision_at_us     INTEGER NOT NULL,
    decision_at_iso    TEXT    NOT NULL,
    -- Kararın, PİYASANIN KENDİ zaman dilimindeki günü.
    --
    -- Neden ayrı sütun: hedef gün (target_date) yereldir, decision_at_iso ise
    -- UTC. İkisini doğrudan karşılaştırmak, ABD şehirlerinde 00:00-04:00Z
    -- aralığında yapılan MEŞRU ertesi-gün kararlarını ihlal sanır. Bu hata
    -- bir kez yapıldı ve boru hattını ~15 saat durdurdu.
    decision_local_date TEXT   NOT NULL,

    market_snapshot_id INTEGER NOT NULL REFERENCES market_snapshots (id),
    forecast_basis     TEXT    NOT NULL,   -- kullanılan forecast_snapshot id'leri, JSON dizi

    action             TEXT    NOT NULL
                       CHECK (action IN ('buy_yes', 'buy_no', 'no_trade')),
    -- Gerekçe zorunlu ve boş olamaz: "neden işlem yapmadım" da kayda geçsin.
    -- trim() varsayılanı yalnızca boşluk siler; tab/newline'ı da elemek için
    -- karakter kümesini açıkça veriyoruz.
    reason             TEXT    NOT NULL
                       CHECK (length(trim(reason, char(32) || char(9) || char(10)
                                                 || char(13))) > 0),

    model_prob         REAL    NOT NULL CHECK (model_prob BETWEEN 0.0 AND 1.0),
    market_prob        REAL             CHECK (market_prob IS NULL OR market_prob BETWEEN 0.0 AND 1.0),
    edge               REAL,
    kelly_fraction     REAL,
    target_contracts   REAL    NOT NULL DEFAULT 0 CHECK (target_contracts >= 0),
    limits_json        TEXT    NOT NULL DEFAULT '{}',

    -- Veri karardan sonra gelmiş olamaz. Tek satır ihlal etse INSERT reddedilir.
    CHECK (data_asof_us <= decision_at_us),

    UNIQUE (venue, market_ticker, slot_id)
);
CREATE INDEX IF NOT EXISTS idx_dec_time ON decisions (decision_at_us);
CREATE INDEX IF NOT EXISTS idx_dec_market ON decisions (market_ticker, target_date);

-- ---------------------------------------------------------------------------
-- Simüle fill'ler
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS sim_fills (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    decision_id         INTEGER NOT NULL REFERENCES decisions (id),

    -- Fill, karardan SONRA çekilmiş ikinci kitaba karşı hesaplanır.
    fill_snapshot_id    INTEGER NOT NULL REFERENCES market_snapshots (id),
    decision_at_us      INTEGER NOT NULL,
    book_asof_us        INTEGER NOT NULL,   -- fill'de kullanılan kitabın zamanı
    filled_at_us        INTEGER NOT NULL,
    filled_at_iso       TEXT    NOT NULL,

    side                TEXT    NOT NULL CHECK (side IN ('yes', 'no')),
    requested_contracts REAL    NOT NULL CHECK (requested_contracts >= 0),
    filled_contracts    REAL    NOT NULL CHECK (filled_contracts >= 0),
    -- Ortalama fill fiyatı seviyeler arası ağırlıklı ortalama olduğu için
    -- ızgaraya oturmayabilir; bu yüzden REAL.
    avg_price_dcents    REAL             CHECK (avg_price_dcents IS NULL
                                                OR avg_price_dcents BETWEEN 0 AND 1000),
    fee_dcents          REAL    NOT NULL DEFAULT 0 CHECK (fee_dcents >= 0),
    levels_consumed     TEXT    NOT NULL DEFAULT '[]',  -- hangi seviyeler yendi, JSON
    fill_status         TEXT    NOT NULL
                        CHECK (fill_status IN ('full', 'partial', 'none')),
    notes               TEXT    NOT NULL DEFAULT '',

    -- Kısmi fill dahil, istenen kadardan fazlası doldurulamaz.
    CHECK (filled_contracts <= requested_contracts),
    -- Karar ile fill arasında en az 30 saniye olmak ZORUNDA.
    CHECK (filled_at_us - decision_at_us >= 30000000),
    -- Fill'de kullanılan kitap karardan sonra çekilmiş olmalı; aksi hâlde
    -- "gecikme koydum" demek olur ama aslında eski fiyattan doldurmuş oluruz.
    CHECK (book_asof_us >= decision_at_us),
    UNIQUE (decision_id)
);
CREATE INDEX IF NOT EXISTS idx_fill_dec ON sim_fills (decision_id);

-- ---------------------------------------------------------------------------
-- Ground truth / çözümleme
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS settlements (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    venue           TEXT    NOT NULL,
    market_ticker   TEXT    NOT NULL,
    event_ticker    TEXT    NOT NULL,
    target_date     TEXT    NOT NULL,

    -- Gözlemin YAYINLANDIĞI an. Bir karar bundan önce verildiyse bu değeri
    -- kullanamaz — değerlendirme kodu bunu kontrol eder.
    observed_at_us  INTEGER NOT NULL,
    observed_at_iso TEXT    NOT NULL,

    source          TEXT    NOT NULL,   -- 'nws_cli', 'kalshi_result', ...
    source_url      TEXT    NOT NULL,
    raw_json        TEXT    NOT NULL,

    outcome         INTEGER          CHECK (outcome IN (0, 1)),
    observed_value  REAL,
    UNIQUE (venue, market_ticker, source)
);
CREATE INDEX IF NOT EXISTS idx_settle_lookup ON settlements (market_ticker, target_date);
