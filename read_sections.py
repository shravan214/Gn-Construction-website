import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

for i in range(10):
    with open(f'part_sec_{i}.html', 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"\n--- Section {i} (Length {len(c)}) ---")
    # print snippet of text
    text_only = re.sub(r'<[^>]+>', ' ', c)
    text_only = ' '.join(text_only.split())
    print("Text preview:", text_only[:300])
