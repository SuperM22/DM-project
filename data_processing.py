
import pandas as pd
import numpy as np
import json

# Load the original CSV file
df = pd.read_csv("archive/tracks.csv")
df_clean = df.copy()

# Derive 'year' and 'decade'
df_clean['year'] = pd.to_datetime(df_clean['release_date'], errors='coerce').dt.year
df_clean['decade'] = (df_clean['year'] // 10 * 10).astype('Int64').astype('string') + "s"

# Derive 'tempo_class'
def classify_tempo(bpm):
    if pd.isnull(bpm):
        return np.nan
    elif bpm < 90:
        return 'slow'
    elif bpm <= 130:
        return 'medium'
    else:
        return 'fast'
df_clean['tempo_class'] = df_clean['tempo'].apply(classify_tempo)

# Derive 'mood_cluster'
def classify_mood(row):
    valence = row['valence']
    energy = row['energy']
    acousticness = row['acousticness']
    if pd.isnull(valence) or pd.isnull(energy) or pd.isnull(acousticness):
        return np.nan
    elif valence > 0.6 and energy > 0.6:
        return 'happy'
    elif valence < 0.4 and energy < 0.4:
        return 'sad'
    elif energy < 0.4 and acousticness > 0.5:
        return 'chill'
    else:
        return 'other'
df_clean['mood_cluster'] = df_clean.apply(classify_mood, axis=1)

# export as cleaned CSV
df_clean.to_csv("tracks_clean.csv", index=False)

# export as newline-delimited JSON for MongoDB
with open("tracks_clean.json", "w", encoding="utf-8") as f:
    for record in df_clean.to_dict(orient="records"):
        f.write(json.dumps(record) + "\n")
