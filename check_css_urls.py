with open('arsahomes_original.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
print("Urls in css:")
urls = re.findall(r'url\([^)]+\)', css)
for u in set(urls):
    print(" ", u)
