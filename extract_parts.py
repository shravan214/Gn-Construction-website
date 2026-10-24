import re

with open('arsahomes_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's see the body structure
# Find header
header_match = re.search(r'(<header.*?</header>)', html, re.DOTALL)
if header_match:
    print("Header found! Length:", len(header_match.group(1)))
    with open('part_header.html', 'w', encoding='utf-8') as pf:
        pf.write(header_match.group(1))

# Find footer
footer_match = re.search(r'(<footer.*?</footer>)', html, re.DOTALL)
if footer_match:
    print("Footer found! Length:", len(footer_match.group(1)))
    with open('part_footer.html', 'w', encoding='utf-8') as pf:
        pf.write(footer_match.group(1))

# Find main content
main_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
if main_match:
    main_content = main_match.group(1)
    print("Main found! Length:", len(main_content))
    # split by section
    sections = re.findall(r'(<section.*?</section>)', main_content, re.DOTALL)
    print(f"Total sections inside main: {len(sections)}")
    for i, sec in enumerate(sections):
        # find first heading or id or class
        h = re.search(r'<(h[1-6])[^>]*>(.*?)</\1>', sec, re.DOTALL)
        h_text = re.sub(r'<[^>]+>', ' ', h.group(2)).strip() if h else "No heading"
        id_m = re.search(r'id="([^"]+)"', sec)
        id_val = id_m.group(1) if id_m else "None"
        class_m = re.search(r'class="([^"]+)"', sec)
        class_val = class_m.group(1) if class_m else "None"
        print(f"Section {i}: id='{id_val}', heading='{h_text[:60]}', class='{class_val[:50]}...' (len {len(sec)})")
        with open(f'part_sec_{i}.html', 'w', encoding='utf-8') as pf:
            pf.write(sec)

# Check what else is in body (modals, floating buttons, etc.)
# everything outside header, main, footer
pre_header = html[:header_match.start()] if header_match else ""
post_footer = html[footer_match.end():] if footer_match else ""
print("Pre-header length:", len(pre_header))
print("Post-footer length:", len(post_footer))
with open('part_post_footer.html', 'w', encoding='utf-8') as pf:
    pf.write(post_footer)
