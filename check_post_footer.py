with open('part_post_footer.html', 'r', encoding='utf-8') as f:
    pf = f.read()

import re
print("Post footer length:", len(pf))
scripts = re.findall(r'<script.*?</script>', pf, re.DOTALL)
print("Scripts count in post footer:", len(scripts))
total_script_len = sum(len(s) for s in scripts)
print("Total script length:", total_script_len)

# What is non-script in post-footer?
non_script = re.sub(r'<script.*?</script>', '', pf, flags=re.DOTALL).strip()
print("Non-script content length:", len(non_script))
print("Non-script content preview:\n", non_script[:1000])

# Also check pre_header
with open('arsahomes_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m = re.search(r'(<body[^>]*>)', html)
print("Body tag:", m.group(1) if m else "None")
