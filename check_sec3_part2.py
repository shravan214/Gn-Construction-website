import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('part_sec_3.html', 'r', encoding='utf-8') as f:
    sec3 = f.read()

print(sec3[2000:7000])
