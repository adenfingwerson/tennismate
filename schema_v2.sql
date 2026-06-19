CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS player_metrics (
    user_id TEXT PRIMARY KEY REFERENCES users(id),
    metrics_json TEXT,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lessons (
    id TEXT PRIMARY KEY,
    user_id TEXT REFERENCES users(id),
    lesson_date TEXT,
    raw_notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
