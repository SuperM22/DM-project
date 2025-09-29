
import pandas as pd
import ast

# Load the cleaned track CSV
df = pd.read_csv("tracks_clean.csv")

# Prepare containers
artist_set = set()
track_artist_links = []

# Process each row
for _, row in df.iterrows():
    try:
        ids = ast.literal_eval(row['id_artists'])
        names = ast.literal_eval(row['artists'])
        if len(ids) != len(names):
            continue  # Skip mismatched rows
        for artist_id, artist_name in zip(ids, names):
            artist_set.add((artist_id, artist_name))
            track_artist_links.append((row['id'], artist_id))
    except:
        continue  # Skip if there's any parsing error

# Create DataFrames
df_artists = pd.DataFrame(list(artist_set), columns=['id', 'name'])
df_track_artists = pd.DataFrame(track_artist_links, columns=['track_id', 'artist_id'])

# Save to CSV
df_artists.to_csv("artists.csv", index=False)
df_track_artists.to_csv("track_artists.csv", index=False)

print("Exported artists.csv and track_artists.csv successfully.")
