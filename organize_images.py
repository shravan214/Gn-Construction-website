"""
Organize and copy GN Construction PPT images into the website's images folder with descriptive names.
"""
from PIL import Image
import os, shutil, json

SRC = r"C:\Users\nwabl\Downloads\Gn Construction website\gn_ppt_assets\images"
DST_BASE = r"C:\Users\nwabl\Downloads\Gn Construction website\images"

os.makedirs(os.path.join(DST_BASE, "projects"), exist_ok=True)
os.makedirs(os.path.join(DST_BASE, "team"), exist_ok=True)
os.makedirs(os.path.join(DST_BASE, "places"), exist_ok=True)

# Map: source file -> (dest folder, dest name, description)
IMAGE_MAP = {
    "slide02_img01.jpg": ("projects", "gn-hero-construction.jpg", "GN Construction premium building project"),
    "slide08_img02.jpg": ("projects", "konark-business-centre-keshav-nagar.jpg", "Konark Business Centre, Keshav Nagar, Mundhwa - Karia Properties"),
    "slide09_img03.jpg": ("projects", "pt-shuttering-cuplock.jpg", "PT Shuttering using cuplock material at GN Construction project"),
    "slide10_img04.jpg": ("projects", "kolte-patil-24k-wakad.jpg", "Kolte Patil 24k Wakad - Phytroid wall and UGWT construction"),
    "slide10_img05.jpg": ("projects", "kolte-patil-24k-wakad-2.jpg", "Kolte Patil 24k Wakad site progress"),
    "slide11_img06.jpg": ("projects", "jade-regency-wagholi.jpg", "JADE Regency, Wagholi - Wadhwa Group residential building 30000 sqft"),
    "slide12_img07.jpg": ("projects", "tanishka-jadhavar-college-narhe.jpg", "Tanishka Reality - Jadhavar College Building, Narhe, 85000 sqft"),
    "slide12_img08.jpg": ("projects", "tanishka-jadhavar-college-narhe-2.jpg", "Tanishka Reality College Building interior progress"),
    "slide14_img09.jpg": ("projects", "konark-business-centre-turnkey.jpg", "KBC Konark Business Centre turnkey project, 26000 sqft"),
    "slide15_img10.jpg": ("projects", "amba-prestige-point-bajirao.jpg", "Amba Group Prestige Point, Bajirao Road, 68000 sqft commercial"),
    "slide16_img11.jpg": ("projects", "konark-virtue-t4-karia.jpg", "Konark Virtue Tower 4, Karia Builder"),
    "slide19_img12.jpg": ("projects", "konark-virtue-tower4-progress.jpg", "Konark Virtue Tower 4 site progress"),
    "slide20_img13.jpg": ("projects", "konark-virtue-cqra-software.jpg", "CQRA project management at Konark Virtue"),
    "slide21_img14.jpg": ("projects", "godrej-greens-undri-clubhouse.jpg", "Godrej Greens Undri - Club House and Swimming Pool"),
    "slide21_img15.jpg": ("projects", "godrej-greens-undri-dev.jpg", "Godrej Properties Godrej Greens development works"),
    "slide22_img16.jpg": ("projects", "godrej-greens-development.jpg", "Godrej Greens development work, Undri Pune"),
    "slide23_img17.jpg": ("projects", "playtor-sawardari-project.jpg", "Playtor Sawardari Project site"),
    "slide24_img18.jpg": ("projects", "pgd-pinacle-shuttering.jpg", "PGD Pinnacle 6m height shuttering work"),
    "slide27_img19.jpg": ("projects", "punit-developer-shukrawar-peth.jpg", "Punit Developer 502 Shukrawar Peth"),
    "slide33_img20.jpg": ("projects", "playtor-work-order-1.jpg", "Playtor Developers work order document"),
    "slide33_img21.jpg": ("projects", "playtor-work-order-2.jpg", "Playtor Developers work order document"),
    "slide36_img22.jpg": ("places", "gn-construction-equipment-machinery.jpg", "GN Construction heavy machinery and equipment"),
}

copied = 0
for src_name, (folder, dst_name, desc) in IMAGE_MAP.items():
    src_path = os.path.join(SRC, src_name)
    dst_path = os.path.join(DST_BASE, folder, dst_name)
    if os.path.exists(src_path):
        # Copy and optionally resize large images
        try:
            img = Image.open(src_path)
            w, h = img.size
            # Resize if very large (wider than 1920px)
            if w > 1920:
                ratio = 1920 / w
                img = img.resize((1920, int(h * ratio)), Image.LANCZOS)
            img.save(dst_path, quality=88, optimize=True)
            print(f"Copied: {src_name} -> {folder}/{dst_name} ({img.size})")
            copied += 1
        except Exception as e:
            shutil.copy2(src_path, dst_path)
            print(f"Raw copy: {src_name} -> {folder}/{dst_name} (error: {e})")
            copied += 1
    else:
        print(f"MISSING: {src_path}")

print(f"\nTotal images ready: {copied}")
