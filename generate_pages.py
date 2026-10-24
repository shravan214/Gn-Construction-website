import re
import urllib.parse
import os

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

    # Fix relative links
    if page_depth > 0:
        html = html.replace('href="/css/', f'href="{prefix}css/')
        html = html.replace('src="/js/', f'src="{prefix}js/')
        html = html.replace('href="/fonts/', f'href="{prefix}fonts/')

    # Attach local main.js before </body>
    if f'<script src="{prefix}js/main.js"></script>' not in html:
        html = html.replace('</body>', f'<script src="{prefix}js/main.js"></script></body>')

    return html

# Generate index.html
with open('arsahomes_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw_home = f.read()

home_html = clean_html(raw_home, page_depth=0)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(home_html)

print(f'Generated index.html: {len(home_html)} bytes')
