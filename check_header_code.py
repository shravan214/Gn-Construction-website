import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('part_header.html', 'r', encoding='utf-8') as f:
    header = f.read()

print("Header length:", len(header))
# print first 1500 chars of header
print("Header snippet:\n", header[:1500])
