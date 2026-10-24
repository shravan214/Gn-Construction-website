import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('part_sec_2.html', 'r', encoding='utf-8') as f:
    sec2 = f.read()

print("Sec 2 length:", len(sec2))
print(sec2)
