INSERT INTO tracks (
    id, name, popularity, explicit, duration_ms,
    release_date, year, decade, tempo_class, mood_cluster
)
SELECT
    id, name, popularity, explicit, duration_ms,
    CASE
        WHEN LENGTH(release_date) = 4 THEN (release_date || '-01-01')::DATE
        WHEN LENGTH(release_date) = 7 THEN (release_date || '-01')::DATE
        ELSE release_date::DATE
    END,
    year, decade, tempo_class, mood_cluster
FROM raw_tracks;
