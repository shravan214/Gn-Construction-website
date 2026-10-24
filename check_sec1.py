import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('part_sec_1.html', 'r', encoding='utf-8') as f:
    sec1 = f.read()

print("Sec 1 length:", len(sec1))
print(sec1)
