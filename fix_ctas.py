from pathlib import Path
import re

root = Path(r"c:\Users\nwabl\Downloads\Gn Construction website")
pattern = re.compile(
    r'href=(?P<quote>["\'])(?:\.\./)?contact/index\.html(?P=quote)\s*class=(?P<classquote>["\'])(?P<class>[^"\']*btn-gold[^"\']*)(?P=classquote)>\s*Request Project Proposal\s*</a>',
    re.IGNORECASE,
)

count = 0
for path in root.rglob("*.html"):
    text = path.read_text(encoding="utf-8")
    def repl(match):
        return f'href="https://wa.me/919527660870?text=Hello%20GN%20Construction%2C%20I%20would%20like%20to%20request%20a%20project%20proposal." class="{match.group("class")}">Request Project Proposal</a>'

    new_text, n = pattern.subn(repl, text)
    if n:
        path.write_text(new_text, encoding="utf-8")
        count += n

print(f"updated {count} Request Project Proposal buttons")
