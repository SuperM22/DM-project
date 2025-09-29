# DM-Spotify Dataset: Comparative Study of MongoDB vs PostgreSQL

This project implements and benchmarks the **Spotify Tracks dataset (1921–2020)** in two different database paradigms:
- **MongoDB** (document-oriented)
- **PostgreSQL** (relational)

The dataset is available here:  
👉 [Spotify Dataset 1921–2020 (Kaggle)](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks/data?select=tracks.csv)

The goal is to compare performance, query expressiveness, and data modeling trade-offs between the two systems.  
Both raw query times and execution statistics have been analyzed.

---

## 1. Data Preprocessing


Data preparation was carried out using the Python scripts provided in this repository:
- **`data_processing.py`** — Cleans, formats, and derives new attributes.  
- **`flatten_artists.py`** — Flattens the artist list field for relational schema compatibility.  

Steps performed:
- **Cleaning and type conversion**: fixed missing values, ensured correct data types (e.g., `year` as integer, `popularity` as numeric).  
- **Derived attributes**:
  - `decade`: computed from `year` (e.g., 1970s, 1980s).  
  - `tempo_class`: tempo bucketed into categorical classes (slow/medium/fast).  
  - `mood_cluster`: mood grouping derived from audio features (`valence`, `energy`).  
- **Restructuring**:
  - For **PostgreSQL**: flattened `id_artists` array into a separate `track_artists` table (many-to-many relationship).  
  - For **MongoDB**: preserved denormalized structure with embedded `audio_features`.  

This means preprocessing not only cleaned the dataset but also performed **feature engineering** and **schema reshaping** to support both relational and document-oriented models.
 

---

## 2. Database Creation

### PostgreSQL
- Normalized schema with **4 main tables**:  
  - `tracks`, `artists`, `track_artists` (join table), `audio_features`.  
- Enforced **primary/foreign keys**.  
- Added **indexes** on key attributes (`decade`, `tempo_class`, `popularity`, `artist_id`).  

### MongoDB
- Single collection: **`tracks`**.  
- Flat fields (e.g., `popularity`, `duration_ms`, `decade`, `mood_cluster`) plus inline audio features.  
- Artist relationships stored in fields (`artists` as string, `id_artists` as string list).  
- Field types sometimes vary (e.g., doubles stored as numbers or as `$numberDouble`).  
- Indexes created for query support (`decade+tempo_class`, `id_artists`, `decade+popularity`, `decade+mood_cluster`).  

---

## 3. Queries

The project implements five analytical queries (Q1–Q5), covering distribution, aggregation, ranking, and collaboration metrics.  

- **Both PostgreSQL and MongoDB implementations are provided.**  
- Each query was tested **without indexes (baseline)** and **with indexes (optimized)**.  
- All SQL and MongoDB versions of the queries, along with their execution plans, are detailed in [`Plans.txt`](query_eval/Plans.txt).  

---

## 4. Analysis Methodology

- **PostgreSQL**:
  - Used `EXPLAIN (ANALYZE, BUFFERS, WAL, VERBOSE, SUMMARY, FORMAT JSON)`.  
  - Tracked execution time, row counts, buffer activity, disk usage, and WAL impact.  
  - Disabled JIT (`SET jit = off`) and enabled I/O timing (`SET track_io_timing = on`) for consistency.  

- **MongoDB**:
  - Used `.explain("executionStats")` on aggregation pipelines.  
  - Collected: execution time, rows returned, documents/keys examined, disk usage, and memory spills.  
  - Used `allowDiskUse: true` when needed.  

**Comparison criteria**:  
Execution time, memory vs disk use, index exploitation, join strategies (PostgreSQL hash/merge joins vs MongoDB `$unwind`/`$lookup`), and aggregation complexity.

---

## Conclusion

This project demonstrates the **trade-offs** between relational and document-oriented paradigms:
- **PostgreSQL**: excels in **complex joins**, **window functions**, and efficient index use.  
- **MongoDB**: provides **flexible pipelines** and simplicity with denormalized data, but may require full scans without carefully designed indexes.  

Through preprocessing, schema design, query formulation, and systematic plan analysis, the project delivers a structured performance comparison across both paradigms.
