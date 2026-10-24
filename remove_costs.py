from pathlib import Path
import re

root = Path(r'C:\Users\nwabl\Downloads\Gn Construction website')

patterns = [
    (r'\s*·\s*₹?\d+(?:\.\d+)?\s*(?:Crore|Cr|Lakh|Litre|litre|Ltr|ltr)\s*·?', ' · '),
    (r'₹\s*\d+(?:\.\d+)?\s*(?:Crore|Cr|Lakh|Litre|litre|Ltr|ltr)', ''),
    (r'\b\d+\.\d+\s*(?:Lakh|lakh|Ltr|ltr)\s*(?:Litre|litre)?\b', ''),
    (r'\b13\.7\s*(?:Lakh|lakh|Ltr|ltr)\s*(?:Litre|litre)?\b', ''),
    (r'\bWakad\s*·\s*Phytroid Wall\s*&\s*13\.7\s*(?:L|l)tr\s*Tank\b', 'Wakad · Phytroid Wall'),
    (r'\bMundhwa\s*·\s*₹?\d+(?:\.\d+)?\s*(?:Crore|Cr)\s*·\s*Turnkey\b', 'Mundhwa · Turnkey'),
    (r'\bKeshav Nagar, Mundhwa &bull; 26,000 sqft turnkey commercial &bull; ₹?\d+(?:\.\d+)?\s*(?:Crore|Cr)\b', 'Keshav Nagar, Mundhwa &bull; 26,000 sqft turnkey commercial'),
    (r'\bNarhe, Pune &bull; 85,000 sqft institutional campus &bull; ₹?\d+(?:\.\d+)?\s*(?:Crore|Cr)\b', 'Narhe, Pune &bull; 85,000 sqft institutional campus'),
    (r'\bPhytroid wall and \d+\.\d+\s*(?:Lakh|lakh)\s*(?:Litre|litre)\s*underground water tank \(UGWT\)\.', 'Phytroid wall and underground water tank (UGWT).'),
    (r'\bUnderground Water Tank \(UGWT\):\s*\d+\.\d+\s*(?:Lakh|lakh)\s*(?:Litre|litre)\s*capacity water reservoir cast with leak-proof designed concrete\.', 'Underground Water Tank (UGWT): water reservoir cast with leak-proof designed concrete.'),
    (r'\bContract:\s*₹?\d+(?:\.\d+)?\s*(?:Crore|Cr|Lakh|lakh)\b', 'Contract:'),
    (r'\bOrder Value:\s*₹?\d+(?:\.\d+)?\s*(?:Crore|Cr|Lakh|lakh)\b', ''),
]

for path in list(root.rglob('*.html')) + [root / 'js' / 'main.js']:
    text = path.read_text(encoding='utf-8')
    new = text
    for pattern, replacement in patterns:
        new = re.sub(pattern, replacement, new)
    if new != text:
        path.write_text(new, encoding='utf-8')

print('Removed remaining cost figures and tank-capacity values from the site.')
