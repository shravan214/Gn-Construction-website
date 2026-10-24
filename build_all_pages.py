import re
import urllib.parse
import os

pages = [
    ('services/index.html', 1),
    ('services/bungalow-construction.html', 1),
    ('services/residential-building-construction.html', 1),
    ('services/turnkey-construction.html', 1),
    ('services/architectural-planning-elevation.html', 1),
    ('services/renovation-redevelopment.html', 1),
    ('services/site-supervision-interior-coordination.html', 1),
    ('projects/index.html', 1),
    ('projects/courtyard-bungalow-baramati.html', 1),
    ('areas/index.html', 1),
    ('areas/baramati.html', 1),
    ('tools/index.html', 1),
    ('about/index.html', 1),
    ('why-arsa/index.html', 1),
    ('methodology/index.html', 1),
    ('materials/index.html', 1),
    ('contact/index.html', 1),
    ('arsa-ai/index.html', 1),
    ('privacy-policy/index.html', 1),
    ('terms/index.html', 1)
]

def clean_html(raw_html, page_depth=0):
    html = raw_html
    # Brand translation
    html = html.replace('Arsa Construction', 'GN Construction')
    html = html.replace('ARSA Construction', 'GN Construction')
    html = html.replace('Arsa Associates', 'GN Associates')
    html = html.replace('ARSA Associates', 'GN Associates')
    html = html.replace('Arsa AI', 'GN AI')
    html = html.replace('ARSA AI', 'GN AI')
    html = html.replace('Arsa', 'GN')
    html = html.replace('ARSA', 'GN')
    html = html.replace('arsa_associates', 'gn_construction')
    html = html.replace('hello@arsahomes.in', 'contact@gnconstruction.com')
    html = html.replace('arsahomes.in', 'gnconstruction.com')

    prefix = '../' * page_depth if page_depth > 0 else './'

    # Stylesheet replacement
    html = re.sub(r'<link\s+rel="stylesheet"\s+href="/_next/static/css/[^"]+"[^>]*>', f'<link rel="stylesheet" href="{prefix}css/style.css"/>', html)
    # Remove Next.js script bundles
    html = re.sub(r'<script\s+src="/_next/[^"]+"[^>]*></script>', '', html)
    html = re.sub(r'<link\s+rel="preload"\s+as="script"[^>]*>', '', html)

    # Normalize image paths
    def repl_img(m):
        val = m.group(1)
        if 'url=' in val:
            u_match = re.search(r'url=([^&"\']+)', val)
            if u_match:
                decoded = urllib.parse.unquote(u_match.group(1)).lstrip('/')
                return f'src="{prefix}{decoded}"'
        clean_path = val.lstrip('/')
        return f'src="{prefix}{clean_path}"'

    html = re.sub(r'src="(/_next/image/\?[^"]+)"', repl_img, html)
    html = re.sub(r'srcSet="[^"]*"', '', html)
    html = re.sub(r'srcset="[^"]*"', '', html)
    html = re.sub(r'imageSrcSet="[^"]*"', '', html)

    # Replace absolute root paths with relative paths for css, js, fonts, images
    if page_depth > 0:
        html = html.replace('href="/fonts/', f'href="{prefix}fonts/')
        html = html.replace('src="/images/', f'src="{prefix}images/')

    # Attach local main.js before </body>
    if f'<script src="{prefix}js/main.js"></script>' not in html:
        html = html.replace('</body>', f'<script src="{prefix}js/main.js"></script></body>')

    return html

# Process all subpages
for dest_path, depth in pages:
    safe_name = dest_path.replace('/', '__')
    raw_file = f'raw_pages/{safe_name}'
    if os.path.exists(raw_file):
        with open(raw_file, 'r', encoding='utf-8', errors='ignore') as f:
            raw_content = f.read()
        cleaned = clean_html(raw_content, page_depth=depth)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f'Generated: {dest_path} ({len(cleaned)} bytes)')
    else:
        print(f'Missing raw file: {raw_file}')

print('All pages generated!')
