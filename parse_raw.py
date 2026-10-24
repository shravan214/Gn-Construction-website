import re

with open('arsahomes_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print("File size:", len(html))

# Find title
title_m = re.search(r'<title>(.*?)</title>', html)
print("Title:", title_m.group(1) if title_m else "N/A")

# Find style tags
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print("Styles count:", len(styles))
for i, s in enumerate(styles):
    print(f"Style {i} (len {len(s)}): {s[:120].strip()}...")

# Find all headings
headings = re.findall(r'<(h[1-6])[^>]*>(.*?)</\1>', html, re.DOTALL)
print(f"\nTotal headings: {len(headings)}")
for tag, text in headings:
    # clean tags
    clean_text = re.sub(r'<[^>]+>', ' ', text).strip()
    clean_text = ' '.join(clean_text.split())
    print(f"  {tag}: {clean_text[:90]}")

# Find section tags
sections = re.findall(r'<section([^>]*)>', html)
print(f"\nTotal sections: {len(sections)}")
for s in sections:
    print("  <section", s[:100], "...>")

# Let's inspect CSS classes used
classes = re.findall(r'class="([^"]+)"', html)
all_tokens = set()
for c in classes:
    for token in c.split():
        all_tokens.add(token)

print(f"\nTotal unique classes: {len(all_tokens)}")
# check if tailwind classes exist
tw_samples = [c for c in all_tokens if any(c.startswith(p) for p in ['bg-', 'text-', 'flex', 'grid', 'py-', 'px-', 'rounded', 'border'])]
print(f"Tailwind-like classes count: {len(tw_samples)}")
print("Sample Tailwind classes:", sorted(tw_samples)[:30])
