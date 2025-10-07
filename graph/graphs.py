# graphs.py
# Requires: matplotlib, numpy
# Run: python graphs.py

import matplotlib.pyplot as plt
import numpy as np




categories_q = ["Q1", "Q2", "Q3", "Q4", "Q5"]


postgres_no_index = [63, 747, 1261, 76, 603]
mongo_no_index    = [342, 748, 1503, 326, 520]


postgres_indexed  = [51, 587, 142, 501, 331]
mongo_indexed     = [151, 1187, 617, 1032, 841]


categories_ud = ["U1 Update", "D1 Delete"]
pg_update_ms, pg_delete_ms       = 1341, 7213
mongo_update_ms, mongo_delete_ms = 486, 549


x = np.arange(len(categories_q))
bar_w = 0.2

plt.figure(figsize=(12, 6))


plt.bar(x - 1.5*bar_w, postgres_no_index, width=bar_w, label="PostgreSQL (No Index)")
plt.bar(x - 0.5*bar_w, postgres_indexed,  width=bar_w, label="PostgreSQL (Indexed)")
plt.bar(x + 0.5*bar_w, mongo_no_index,    width=bar_w, label="MongoDB (No Index)")
plt.bar(x + 1.5*bar_w, mongo_indexed,     width=bar_w, label="MongoDB (Indexed)")

plt.xticks(x, categories_q)
plt.ylabel("Execution Time (ms)")
plt.title("PostgreSQL vs MongoDB (Q1–Q5): Indexed vs Non-Indexed")
plt.legend()


series = [postgres_no_index, postgres_indexed, mongo_no_index, mongo_indexed]
offsets = [-1.5*bar_w, -0.5*bar_w, 0.5*bar_w, 1.5*bar_w]
ymax = max(max(s) for s in series)
for s, off in zip(series, offsets):
    for i, val in enumerate(s):
        plt.text(i + off, val + ymax*0.02, str(val), ha="center", va="bottom", fontsize=8)

plt.tight_layout()
plt.savefig("q1_q5_indexed_vs_no_indexed.png", dpi=150)

x2 = np.arange(len(categories_ud))
bar_w2 = 0.35

plt.figure(figsize=(9, 5))

pg_times    = [pg_update_ms, pg_delete_ms]
mongo_times = [mongo_update_ms, mongo_delete_ms]

plt.bar(x2 - bar_w2/2, pg_times,    width=bar_w2, label="PostgreSQL")
plt.bar(x2 + bar_w2/2, mongo_times, width=bar_w2, label="MongoDB")

plt.xticks(x2, categories_ud)
plt.ylabel("Execution Time (ms)")
plt.title("Bulk Update and Delete Performance: PostgreSQL vs MongoDB")
plt.legend()

ymax2 = max(pg_times + mongo_times)
for i, val in enumerate(pg_times):
    plt.text(i - bar_w2/2, val + ymax2*0.02, str(val), ha="center", va="bottom", fontsize=9)
for i, val in enumerate(mongo_times):
    plt.text(i + bar_w2/2, val + ymax2*0.02, str(val), ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig("update_delete_comparison.png", dpi=150)

print("Saved charts:")
print(" - q1_q5_indexed_vs_no_indexed.png")
print(" - update_delete_comparison.png")
