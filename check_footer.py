import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('part_footer.html', 'r', encoding='utf-8') as f:
    footer = f.read()

print("Footer length:", len(footer))
# Print text summary of footer
text_only = re.sub(r'<[^>]+>', ' ', footer)
text_only = ' '.join(text_only.split())
print("Footer text preview:\n", text_only[:800])
