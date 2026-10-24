import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('part_sec_5.html', 'r', encoding='utf-8') as f:
    sec5 = f.read()

print("Sec 5 length:", len(sec5))
print("Sec 5 content:", sec5)

with open('part_sec_6.html', 'r', encoding='utf-8') as f:
    sec6 = f.read()

print("Sec 6 length:", len(sec6))
print("Sec 6 preview:", sec6[:1500])
