CREATE TABLE tracks (
    id TEXT PRIMARY KEY,
    name TEXT,
    popularity INTEGER,
    explicit BOOLEAN,
    duration_ms INTEGER,
    release_date DATE,
    year INTEGER,
    decade TEXT,
    tempo_class TEXT,
    mood_cluster TEXT
);

CREATE TABLE audio_features (
    track_id TEXT PRIMARY KEY REFERENCES tracks(id) ON DELETE CASCADE,
    danceability FLOAT,
    energy FLOAT,
    key INTEGER,
    loudness FLOAT,
    mode INTEGER,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    time_signature INTEGER
);

CREATE TABLE artists (
    id TEXT PRIMARY KEY,
    name TEXT
);

CREATE TABLE track_artists (
    track_id TEXT REFERENCES tracks(id) ON DELETE CASCADE,
    artist_id TEXT REFERENCES artists(id) ON DELETE CASCADE,
    PRIMARY KEY (track_id, artist_id)
);
