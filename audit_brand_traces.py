from pathlib import Path
import re

base = Path(".")
excluded_dirs = {".git", ".system_generated", "raw_pages", "inspected_pages", "gn_ppt_assets", ".user_uploaded", "archive"}

html_files = [p for p in base.rglob("*.html") if not any(ex in p.parts for ex in excluded_dirs)]
js_files = [p for p in base.rglob("*.js") if not any(ex in p.parts for ex in excluded_dirs)]

all_files = html_files + js_files

search_terms = [
    r"\barsa\b",
    r"\barsahomes\b",
    r"95949\s*40991",
    r"hello@arsahomes\.in",
    r"Sairaj Complex",
    r"Behind Dhanesh Suzuki",
    r"Tapkiree State"
]

findings = []

for file_path in all_files:
    try:
        content = file_path.read_text(encoding="utf-8")
        for term in search_terms:
            matches = list(re.finditer(term, content, re.IGNORECASE))
            if matches:
                findings.append((file_path, term, len(matches)))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

print(f"Scanned {len(all_files)} files.")
if not findings:
    print("SUCCESS: Zero traces of Arsa Homes branding found across all active site files!")
else:
    print(f"FOUND {len(findings)} potential traces:")
    for f, t, c in findings:
        print(f"  {f} : pattern '{t}' ({c} matches)")
