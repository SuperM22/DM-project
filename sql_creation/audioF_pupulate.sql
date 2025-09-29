INSERT INTO audio_features (
    track_id, danceability, energy, key, loudness, mode,
    speechiness, acousticness, instrumentalness, liveness,
    valence, tempo, time_signature
)
SELECT
    id, danceability, energy, key, loudness, mode,
    speechiness, acousticness, instrumentalness, liveness,
    valence, tempo, time_signature
FROM raw_tracks;
