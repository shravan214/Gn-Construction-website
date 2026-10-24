import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('part_sec_9.html', 'r', encoding='utf-8') as f:
    sec9 = f.read()

print(sec9[1200:])
