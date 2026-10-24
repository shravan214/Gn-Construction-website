import re

with open('arsahomes_original.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("CSS length:", len(css))

# Look for font-face
font_faces = re.findall(r'@font-face\s*\{[^}]*\}', css)
print("Font faces count:", len(font_faces))
for ff in font_faces[:5]:
    print(" ", ff[:120])

# Look for :root variables
root_vars = re.findall(r'--[a-zA-Z0-9_-]+:[^;]+;', css)
print(f"Total CSS variables: {len(root_vars)}")
for v in root_vars[:25]:
    print(" ", v)

# Look for keyframes
keyframes = re.findall(r'@keyframes\s+([a-zA-Z0-9_-]+)', css)
print("Keyframes count:", len(keyframes))
print("Keyframe names:", keyframes)
