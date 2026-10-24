import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('arsahomes_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

queries = [
    "No brand substitutions",
    "Recent work",
    "Your plot",
    "Five movements",
    "What we use",
    "UltraTech",
    "Tata Steel",
    "Plan a free site visit",
    "What the government changed this week"
]

for q in queries:
    pos = html.find(q)
    print(f"'{q}': found at pos {pos}")
    if pos != -1:
        start = max(0, pos - 150)
        end = min(len(html), pos + 250)
        print("  Snippet:", html[start:end].replace('\n', ' '))
