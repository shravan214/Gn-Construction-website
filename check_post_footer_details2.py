import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('part_post_footer.html', 'r', encoding='utf-8') as f:
    pf = f.read()

non_script = re.sub(r'<script.*?</script>', '', pf, flags=re.DOTALL).strip()
print(non_script[3000:])
