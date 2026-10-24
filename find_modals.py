import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('arsahomes_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# search for dialogs or search modal
dialogs = re.findall(r'<div[^>]*role="dialog"[^>]*>.*?</div>', html, re.DOTALL)
print("Dialogs with role='dialog':", len(dialogs))

# search for ⌘K or search modal
modal_m = re.findall(r'aria-modal="true"[^>]*>.*?(?=</dialog>|</div>\s*</div>\s*</div>)', html, re.DOTALL)
print("Aria modal matches:", len(modal_m))

# search for 'Search tools, guides' in raw html
for m in re.finditer(r'Search tools, guides', html):
    pos = m.start()
    print(f"Match at {pos}:", html[pos-100:pos+200])
