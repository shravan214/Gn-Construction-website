"""
GN Construction — Master Brand Replacement Builder
Builds the complete website using actual GN Construction data from PPT.
"""

# ============================================================
# GN CONSTRUCTION — COMPLETE DATA FROM PPT
# ============================================================

GN_BRAND = {
    "company_name": "GN Construction",
    "group_name": "GN Group of Companies",
    "tagline": "Building Excellence Since 2013",
    "slogan": "Quality, Honesty & Hard Work — Built Into Every Project.",
    "established": "2013",
    "phone": "+91 98765 43210",  # FLAG: not in PPT – mark for client input
    "email": "contact@gngroup.in",  # FLAG: not in PPT – mark for client input
    "address": "Sr. No. 585, Plot No. 88/90, Salisbury Park, Pune - 411038",
    "website": "gngroup.in",
    "logo_text": "GN",
    "logo_sub": "Construction",
}

GN_ABOUT = {
    "intro": "We are a group of engineers who started our own company in 2013. We have vast experience in residential as well as commercial building construction.",
    "mission": "To remain reliable and efficient for the present construction industry through quality, honesty and hard work.",
    "goal": "To satisfy the clients by giving timely completion of services for the offered job with the given specification and quality norms.",
    "established": "2013",
    "experience_years": "12+",
}

GN_FOUNDERS = [
    {
        "name": "Mr. Nitin Wable",
        "role": "Founder & Director",
        "qualification": "B.E. Civil",
        "experience": "25 years in residential and commercial building construction.",
    },
    {
        "name": "Mr. Hermeetsingh Hoda",
        "role": "Co-Founder & Director",
        "qualification": "B.E. Civil",
        "experience": "14 years in residential and commercial building construction.",
    },
]

GN_ASSOCIATES = [
    "GN Construction",
    "GN Infra Project",
    "Prisha Enterprises",
]

GN_CLIENTS = [
    "Karia Properties",
    "Amba Group",
    "Godrej Properties (Dream World Landmark LLP)",
    "Suda Infra",
    "Tanishka Reality",
    "Kolte Patil Developers",
    "OP Venture",
    "Playtor Developers Pvt. Ltd.",
    "J+W Marriott Hotel (Maintenance)",
    "Wadhwa Group, Mumbai",
    "PGD Group, Mumbai (Pinnacle)",
    "Vaibhav Laxmi Developers",
    "Saiesh Properties",
    "S.P. Constructions",
    "Sand Rock Properties LLP",
]

GN_PROJECTS = [
    {
        "id": "konark-business-centre",
        "name": "Konark Business Centre (KBC)",
        "client": "Karia Properties",
        "location": "Keshav Nagar, Mundhwa, Pune",
        "type": "Commercial Turnkey",
        "area_sqft": "26,000",
        "scope": "Basement + Ground + 3 Floors — Turnkey construction",
        "description": "Full turnkey construction of a premium commercial complex in Keshav Nagar, Mundhwa. Delivered to the highest build standards, combining RCC structural work with complete finishing.",
        "image": "images/projects/konark-business-centre-turnkey.jpg",
        "image2": "images/projects/konark-business-centre-keshav-nagar.jpg",
        "tag": "Commercial",
    },
    {
        "id": "konark-virtue-t4",
        "name": "Konark Virtue — Tower 4",
        "client": "Karia Properties",
        "location": "Pune",
        "type": "Residential High-Rise",
        "area_sqft": "Large Scale",
        "scope": "Complete RCC structural work on Tower 4, managed via CQRA quality platform",
        "description": "Structural RCC construction of Tower 4 at Konark Virtue, a premium residential complex by Karia Builder. Project quality managed using CQRA software platform.",
        "image": "images/projects/konark-virtue-t4-karia.jpg",
        "image2": "images/projects/konark-virtue-tower4-progress.jpg",
        "tag": "Residential",
    },
    {
        "id": "tanishka-jadhavar-college",
        "name": "Jadhavar College Building",
        "client": "Tanishka Reality",
        "location": "Narhe, Pune",
        "type": "Institutional Construction",
        "area_sqft": "85,000",
        "scope": "RCC construction of institutional building",
        "description": "Large-scale institutional construction at Narhe, Pune for Tanishka Reality. Structurally complex project executed with precision shuttering, RCC framework, and professional site management.",
        "image": "images/projects/tanishka-jadhavar-college-narhe.jpg",
        "image2": "images/projects/tanishka-jadhavar-college-narhe-2.jpg",
        "tag": "Institutional",
    },
    {
        "id": "jade-regency-wagholi",
        "name": "JADE Regency",
        "client": "JADE Developer (Wadhwa Group, Mumbai)",
        "location": "Wagholi, Pune",
        "type": "Residential Building",
        "area_sqft": "30,000",
        "scope": "Construction of residential building",
        "description": "Residential building construction for JADE Developer (Wadhwa Group, Mumbai) at Wagholi, Pune. A significant residential project executed with structured site management.",
        "image": "images/projects/jade-regency-wagholi.jpg",
        "image2": None,
        "tag": "Residential",
    },
    {
        "id": "amba-prestige-point",
        "name": "Prestige Point",
        "client": "Amba Group",
        "location": "Bajirao Road, Pune",
        "type": "Commercial Complex",
        "area_sqft": "68,000",
        "scope": "Construction of commercial complex",
        "description": "Large commercial complex built for Amba Group on Bajirao Road, Pune. A structurally sophisticated project completed on a landmark commercial corridor.",
        "image": "images/projects/amba-prestige-point-bajirao.jpg",
        "image2": None,
        "tag": "Commercial",
    },
    {
        "id": "godrej-greens-undri",
        "name": "Godrej Greens — Club House & Development Works",
        "client": "Godrej Properties (Dream World Landmark LLP)",
        "location": "Undri, Pune",
        "type": "Amenity & Development Works",
        "area_sqft": "N/A",
        "scope": "Club House, Swimming Pool, Multipurpose Hall, Retaining Wall — Development works",
        "description": "Development works at Godrej Greens, Undri, Pune for Godrej Properties. Included construction of Club House, Swimming Pool, Multipurpose Hall, and Retaining Wall structures.",
        "image": "images/projects/godrej-greens-undri-clubhouse.jpg",
        "image2": "images/projects/godrej-greens-development.jpg",
        "tag": "Development",
    },
    {
        "id": "kolte-patil-24k-wakad",
        "name": "Kolte Patil 24K",
        "client": "Kolte Patil Developers",
        "location": "Wakad, Pune",
        "type": "Infrastructure — RCC",
        "area_sqft": "N/A",
        "scope": "Phytroid wall and UGWT — capacity 13.7 lakh litres (labour basis)",
        "description": "Specialized civil infrastructure work for Kolte Patil Developers at their flagship 24K project in Wakad. Included construction of Phytroid wall and UGWT (underground water tank) with 13.7 lakh litre capacity.",
        "image": "images/projects/kolte-patil-24k-wakad.jpg",
        "image2": "images/projects/kolte-patil-24k-wakad-2.jpg",
        "tag": "Infrastructure",
    },
]

GN_ASSETS = {
    "Props": "6,000 nos.",
    "Span (Shuttering)": "1,600 nos.",
    "Cup-lock System": "8,000 sqft",
    "Tie Rod Weller Sets": "600 nos.",
    "Shikanja": "3,000 nos.",
    "H-Frame Sets": "400 nos.",
    "One-Bag Concrete Mixer": "1 no.",
    "Three-Bag Concrete Mixer": "2 nos.",
    "Weigh Batcher": "2 nos.",
    "Lift Machine": "2 nos.",
    "Electric Vibrator": "3 nos.",
    "Handy Gun Vibrator": "4 nos.",
    "Petrol Vibrator": "2 nos.",
}

GN_SERVICES = [
    {
        "id": "civil-construction",
        "name": "Civil Construction",
        "tagline": "Structural Excellence",
        "desc": "Complete RCC-framed civil construction for residential, commercial, and institutional buildings — from foundation to slab, managed by our qualified civil engineering team.",
        "link": "services/civil-construction.html",
    },
    {
        "id": "residential-construction",
        "name": "Residential Building Construction",
        "tagline": "From G+1 to High-Rise",
        "desc": "Construction of residential buildings across Pune, from bungalows and row-houses to multi-storey apartment complexes, with precision structural execution.",
        "link": "services/residential-construction.html",
    },
    {
        "id": "commercial-construction",
        "name": "Commercial Complex Construction",
        "tagline": "Business-Grade Builds",
        "desc": "Construction of commercial complexes, office buildings, and mixed-use developments — delivered on developer-grade timelines with structured quality controls.",
        "link": "services/commercial-construction.html",
    },
    {
        "id": "turnkey-construction",
        "name": "Turnkey Construction",
        "tagline": "One Contract, Complete Delivery",
        "desc": "End-to-end turnkey execution from concept to handover — architectural planning, structural construction, finishing, and interiors under a single, accountable contract.",
        "link": "services/turnkey-construction.html",
    },
    {
        "id": "institutional-construction",
        "name": "Institutional & Infra Construction",
        "tagline": "Scale & Precision",
        "desc": "Construction of large-scale institutional buildings including colleges, hospitals, and government infrastructure — executed with the same precision as our commercial projects.",
        "link": "services/institutional-construction.html",
    },
    {
        "id": "development-works",
        "name": "Development & Amenity Works",
        "tagline": "Landscapes, Pools & Amenities",
        "desc": "Club houses, swimming pools, multipurpose halls, retaining walls, podium landscaping, and compound infrastructure — delivering premium amenity experiences.",
        "link": "services/development-works.html",
    },
]

print("GN Construction data module loaded successfully.")
print(f"Projects: {len(GN_PROJECTS)}")
print(f"Clients: {len(GN_CLIENTS)}")
print(f"Services: {len(GN_SERVICES)}")
