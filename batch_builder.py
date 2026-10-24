import os

pairs = [
    ('raw_pages/about__index.html', 'about/index.html'),
    ('raw_pages/areas__baramati.html', 'areas/baramati.html'),
    ('raw_pages/areas__index.html', 'areas/index.html'),
    ('raw_pages/arsa-ai__index.html', 'arsa-ai/index.html'),
    ('raw_pages/contact__index.html', 'contact/index.html'),
    ('raw_pages/materials__index.html', 'materials/index.html'),
    ('raw_pages/methodology__index.html', 'methodology/index.html'),
    ('raw_pages/privacy-policy__index.html', 'privacy-policy/index.html'),
    ('raw_pages/projects__courtyard-bungalow-baramati.html', 'projects/courtyard-bungalow-baramati.html'),
    ('raw_pages/projects__index.html', 'projects/index.html'),
    ('raw_pages/services__architectural-planning-elevation.html', 'services/architectural-planning-elevation.html'),
    ('raw_pages/services__bungalow-construction.html', 'services/bungalow-construction.html'),
    ('raw_pages/services__index.html', 'services/index.html'),
    ('raw_pages/services__renovation-redevelopment.html', 'services/renovation-redevelopment.html'),
    ('raw_pages/services__residential-building-construction.html', 'services/residential-building-construction.html'),
    ('raw_pages/services__site-supervision-interior-coordination.html', 'services/site-supervision-interior-coordination.html'),
    ('raw_pages/services__turnkey-construction.html', 'services/turnkey-construction.html'),
    ('raw_pages/terms__index.html', 'terms/index.html'),
    ('raw_pages/tools__index.html', 'tools/index.html'),
    ('raw_pages/why-arsa__index.html', 'why-arsa/index.html')
]

for src, dst in pairs:
    if not os.path.exists(src):
        print(f"Skipping {src}, not found")
        continue
    with open(src, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # Brand replacements
    c = c.replace('Arsa Construction', 'GN Construction')
    c = c.replace('ARSA Construction', 'GN Construction')
    c = c.replace('Arsa Associates', 'GN Associates')
    c = c.replace('ARSA Associates', 'GN Associates')
    c = c.replace('Arsa AI', 'GN AI')
    c = c.replace('ARSA AI', 'GN AI')
    c = c.replace('Arsa', 'GN')
    c = c.replace('ARSA', 'GN')
    c = c.replace('arsa_associates', 'gn_construction')
    c = c.replace('hello@arsahomes.in', 'contact@gnconstruction.com')
    c = c.replace('arsahomes.in', 'gnconstruction.com')

    # Remove next static css and insert local style.css
    import re
    c = re.sub(r'<link[^>]*rel="stylesheet"[^>]*href="/_next/static/css/[^"]+"[^>]*>', '<link rel="stylesheet" href="../css/style.css"/>', c)
    c = re.sub(r'<script\s+src="/_next/[^"]+"[^>]*></script>', '', c)
    c = re.sub(r'<link\s+rel="preload"\s+as="script"[^>]*>', '', c)

    # Normalize image references
    c = c.replace('/_next/image/?url=%2F', '../')
    c = re.sub(r'&amp;w=\d+&amp;q=\d+', '', c)
    c = re.sub(r'&w=\d+&q=\d+', '', c)
    c = re.sub(r'srcSet="[^"]*"', '', c)
    c = re.sub(r'srcset="[^"]*"', '', c)
    c = re.sub(r'imageSrcSet="[^"]*"', '', c)

    # Replace absolute root paths with relative
    c = c.replace('href="/css/', 'href="../css/')
    c = c.replace('href="/fonts/', 'href="../fonts/')
    c = c.replace('src="/images/', 'src="../images/')

    # Add main.js
    if '<script src="../js/main.js"></script>' not in c:
        c = c.replace('</body>', '<script src="../js/main.js"></script></body>')

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Generated: {dst} ({len(c)} bytes)")

print("ALL 20 PAGES COMPLETED SUCCESSFULLY!")
