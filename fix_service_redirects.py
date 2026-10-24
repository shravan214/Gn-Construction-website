from pathlib import Path

base = Path("services")
redirects = {
    "bungalow-construction.html": ("residential-construction.html", "Residential Construction"),
    "residential-building-construction.html": ("residential-construction.html", "Residential Building Construction"),
    "architectural-planning-elevation.html": ("turnkey-construction.html", "Turnkey Construction"),
    "renovation-redevelopment.html": ("civil-construction.html", "Civil Construction"),
    "site-supervision-interior-coordination.html": ("civil-construction.html", "Civil Construction")
}

for fname, (target, title) in redirects.items():
    p = base / fname
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0;url={target}">
  <title>Redirecting to {title} | GN Construction</title>
</head>
<body style="font-family:sans-serif; text-align:center; padding:50px; background:#FAF6EE; color:#0A1510;">
  <p>Redirecting to <a href="{target}">{title}</a>...</p>
</body>
</html>'''
    p.write_text(html, encoding="utf-8")
    print(f"Redirect set: {fname} -> {target}")
