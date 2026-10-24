import sys
sys.stdout.reconfigure(encoding='utf-8')

for num in [7, 8, 9]:
    with open(f'part_sec_{num}.html', 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"\nSec {num} length: {len(c)}")
    print(c[:1200])
