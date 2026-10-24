import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('part_sec_4.html', 'r', encoding='utf-8') as f:
    sec4 = f.read()

print("Sec 4 length:", len(sec4))
print(sec4[:1500])
