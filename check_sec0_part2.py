import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('part_sec_0.html', 'r', encoding='utf-8') as f:
    sec0 = f.read()

print(sec0[1500:4500])
