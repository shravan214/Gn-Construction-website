with open('arsahomes_original.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'font-family:[^;]+;', css)
for m in set(matches):
    print(" ", m)
