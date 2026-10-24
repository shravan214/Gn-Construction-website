import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('part_header.html', 'r', encoding='utf-8') as f:
    header = f.read()

print("Header full text length:", len(header))
print(header)
