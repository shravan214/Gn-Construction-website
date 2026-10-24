import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('part_header.html', 'r', encoding='utf-8') as f:
    header = f.read()

# find buttons or nav items inside header
nav_m = re.findall(r'<button[^>]*>.*?</button>|<a[^>]*class="[^"]*nav[^"]*"[^>]*>.*?</a>', header, re.DOTALL)
print("Nav buttons/links count:", len(nav_m))
for n in nav_m[:10]:
    print(" ", re.sub(r'<[^>]+>', ' ', n).strip())

# Look for 'Services', 'Areas', 'Tools'
for term in ['Services', 'Areas', 'Tools', 'Arsa AI', 'Projects', 'Guides', 'मराठी', 'Plan a visit']:
    pos = header.find(term)
    if pos != -1:
        print(f"Found '{term}':", header[pos-50:pos+120].replace('\n', ' '))
