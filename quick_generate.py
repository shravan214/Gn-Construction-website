import glob
import os

pages_map = {
    'raw_pages/about__index.html': ('about/index.html', 1),
    'raw_pages/areas__baramati.html': ('areas/baramati.html', 1),
    'raw_pages/areas__index.html': ('areas/index.html', 1),
    'raw_pages/arsa-ai__index.html': ('arsa-ai/index.html', 1),
    'raw_pages/contact__index.html': ('contact/index.html', 1),
    'raw_pages/materials__index.html': ('materials/index.html', 1),
    'raw_pages/methodology__index.html': ('methodology/index.html', 1),
    'raw_pages/privacy-policy__index.html': ('privacy-policy/index.html', 1),
    'raw_pages/projects__courtyard-bungalow-baramati.html': ('projects/courtyard-bungalow-baramati.html', 1),
    'raw_pages/projects__index.html': ('projects/index.html', 1),
    'raw_pages/services__architectural-planning-elevation.html': ('services/architectural-planning-elevation.html', 1),
    'raw_pages/services__bungalow-construction.html': ('services/bungalow-construction.html', 1),
    'raw_pages/services__index.html': ('services/index.html', 1),
    'raw_pages/services__renovation-redevelopment.html': ('services/renovation-redevelopment.html', 1),
    'raw_pages/services__residential-building-construction.html': ('services/residential-building-construction.html', 1),
    'raw_pages/services__site-supervision-interior-coordination.html': ('services/site-supervision-interior-coordination.html', 1),
    'raw_pages/services__turnkey-construction.html': ('services/turnkey-construction.html', 1),
    'raw_pages/terms__index.html': ('terms/index.html', 1),
    'raw_pages/tools__index.html': ('tools/index.html', 1),
    'raw_pages/why-arsa__index.html': ('why-arsa/index.html', 1)
}

for src, (dst, depth) in pages_map.items():
    if not os.path.exists(src):
        continue
    with open(src, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Brand replacements
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

    prefix = '../' * depth

    # Fix CSS
    # Find link rel="stylesheet"
    import re
    html = re.sub(r'<link\s+rel="stylesheet"\s+href="/_next/static/css/[^"]+"[^>]*>', f'<link rel="stylesheet" href="{prefix}css/style.css"/>', html)
    html = re.sub(r'<script\s+src="/_next/[^"]+"[^>]*></script>', '', html)
    html = re.sub(r'<link\s+rel="preload"\s+as="script"[^>]*>', '', html)

    # Fix images
    html = html.replace('/_next/image/?url=%2F', f'{prefix}')
    html = re.sub(r'&amp;w=\d+&amp;q=\d+', '', html)
    html = re.sub(r'&w=\d+&q=\d+', '', html)
    html = re.sub(r'srcSet="[^"]*"', '', html)
    html = re.sub(r'srcset="[^"]*"', '', html)

    # Relative asset paths
    html = html.replace('href="/css/', f'href="{prefix}css/')
    html = html.replace('href="/fonts/', f'href="{prefix}fonts/')
    html = html.replace('src="/images/', f'src="{prefix}images/')

    # Add main.js
    if f'<script src="{prefix}js/main.js"></script>' not in html:
        html = html.replace('</body>', f'<script src="{prefix}js/main.js"></script></body>')

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Wrote {dst}')

print('Done writing all pages!')
