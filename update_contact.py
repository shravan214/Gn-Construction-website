from pathlib import Path
root = Path(r'C:\Users\nwabl\Downloads\Gn Construction website')
count = 0
for path in root.rglob('*.html'):
    text = path.read_text(encoding='utf-8', errors='ignore')
    new = text
    replacements = [
        ('tel:+91 98765 43210', 'tel:+91 9527660870'),
        ('tel:+91 9876543210', 'tel:+91 9527660870'),
        ('href="mailto:contact@gngroup.in"', 'href="mailto:gnconstruction2016@gmail.com"'),
        ('mailto:contact@gngroup.in', 'mailto:gnconstruction2016@gmail.com'),
        ('contact@gngroup.in', 'gnconstruction2016@gmail.com'),
        ('+91 98765 43210', '9527660870'),
        ('+91 9876543210', '9527660870'),
        ('919876543210', '919527660870'),
        ('98765 43210', '9527660870'),
        ('+91 98765 43210', '9527660870'),
    ]
    for old, new_value in replacements:
        new = new.replace(old, new_value)
    if new != text:
        path.write_text(new, encoding='utf-8')
        count += 1
print(f'Updated {count} HTML files')
