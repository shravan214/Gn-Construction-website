import re

with open('arsahomes_original.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Search for color variables like --paper, --ink, etc.
color_vars = re.findall(r'--[a-zA-Z0-9_-]*(?:paper|ink|forest|gold|safe|z-)[a-zA-Z0-9_-]*:[^;]+;', css)
print("Color & specific vars count:", len(color_vars))
for v in color_vars:
    print(" ", v)

# Let's search for :root definition
root_defs = re.findall(r':root\s*\{[^}]+\}', css)
print("\n:root blocks:", len(root_defs))
for r in root_defs[:3]:
    print(" ", r[:300])
