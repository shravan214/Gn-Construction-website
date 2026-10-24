from pathlib import Path
import re

base = Path(r"C:\Users\nwabl\Downloads\Gn Construction website")
excluded_dirs = {".git", ".system_generated", "raw_pages", "inspected_pages", "gn_ppt_assets", ".user_uploaded", "archive"}

html_files = [p for p in base.rglob("*.html") if not any(ex in p.parts for ex in excluded_dirs)]

broken_links = []
broken_media = []

href_pattern = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)
src_pattern = re.compile(r'src=["\']([^"\']+)["\']', re.IGNORECASE)

for html_file in html_files:
    try:
        content = html_file.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {html_file}: {e}")
        continue

    # Check src
    for src in src_pattern.findall(content):
        if not src or src.startswith("data:") or src.startswith("http://") or src.startswith("https://") or src.startswith("#"):
            continue
        clean_src = src.split("?")[0].split("#")[0]
        if not clean_src:
            continue
        target_path = (html_file.parent / clean_src).resolve()
        if not target_path.exists():
            broken_media.append((html_file.relative_to(base), src))

    # Check href
    for href in href_pattern.findall(content):
        if not href or href.startswith("data:") or href.startswith("http://") or href.startswith("https://") or href.startswith("tel:") or href.startswith("mailto:") or href.startswith("#") or "wa.me" in href:
            continue
        clean_href = href.split("?")[0].split("#")[0]
        if not clean_href:
            continue
        target_path = (html_file.parent / clean_href).resolve()
        if not target_path.exists():
            broken_links.append((html_file.relative_to(base), href))

print(f"Verified {len(html_files)} HTML files.")
if not broken_media:
    print("MEDIA: 100% of local images, fonts, scripts, and stylesheets exist!")
else:
    print(f"BROKEN MEDIA ({len(broken_media)}):")
    for f, orig in set(broken_media):
        print(f"  In {f}: {orig}")

if not broken_links:
    print("LINKS: 100% of internal navigation links resolve to existing files!")
else:
    print(f"BROKEN LINKS ({len(broken_links)}):")
    for f, orig in set(broken_links):
        print(f"  In {f}: {orig}")
