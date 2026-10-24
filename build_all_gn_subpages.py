#!/usr/bin/env python3
"""
GN Construction Subpages Generator
Generates all subpages: Services, Projects, About, Why GN, Clients, Materials, Methodology, Tools, AI, Contact, Legal.
"""

import os
from pathlib import Path
from generate_gn_website import wrap_page, rel_path
from gn_data import (
    GN_BRAND, GN_ABOUT, GN_FOUNDERS, GN_ASSOCIATES, GN_CLIENTS,
    GN_PROJECTS, GN_ASSETS, GN_SERVICES
)

BASE_DIR = Path(r"C:\Users\nwabl\Downloads\Gn Construction website")

def write_page(relative_file_path, html_content):
    out_file = BASE_DIR / relative_file_path
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated: {relative_file_path}")

# ==============================================================================
# 2. SERVICES OVERVIEW (services/index.html)
# ==============================================================================
def build_services_index():
    r = lambda p: rel_path(p, 1)
    
    cards_html = ""
    for s in GN_SERVICES:
        cards_html += f'''
        <div class="bg-paper rounded-2xl p-8 border border-ink/10 shadow-sm hover:shadow-md hover:border-forest/40 transition flex flex-col justify-between group tilt-card">
          <div class="space-y-4">
            <span class="inline-block text-[11px] font-semibold uppercase tracking-wider text-forest font-mono">{s['tagline']}</span>
            <h3 class="text-2xl font-serif text-ink group-hover:text-forest transition">{s['name']}</h3>
            <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">{s['desc']}</p>
          </div>
          <div class="mt-8 pt-4 border-t border-ink/10 flex items-center justify-between">
            <span class="text-[11px] text-ink-muted">B.E. Civil Supervised</span>
            <a href="{r(s['link'])}" class="inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
              <span>Explore Detailed Brief</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
          </div>
        </div>
        '''
        
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Services</span>
      </div>
    </div>

    <!-- Header Section -->
    <section class="py-16 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-4">
        <span class="eyebrow text-forest">Civil &amp; Commercial Capabilities</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          One Engineering Standard. Across Every Scale.
        </h1>
        <p class="text-base text-ink-soft leading-relaxed max-w-2xl">
          From turnkey commercial complexes to multi-storey residential towers, our services are structured around qualified civil engineering leadership, owned shuttering assets, and rigorous milestone accountability.
        </p>
      </div>
    </section>

    <!-- Services Grid -->
    <section class="section bg-paper">
      <div class="container space-y-12">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {cards_html}
        </div>
      </div>
    </section>

    <!-- Bottom Equipment Banner -->
    <section class="py-12 bg-ink text-paper border-t border-paper/10">
      <div class="container flex flex-col md:flex-row items-center justify-between gap-6">
        <div>
          <h3 class="text-xl font-serif font-bold text-paper">Backed by 6,000+ Owned Shuttering Props &amp; Plant Assets</h3>
          <p class="text-xs text-paper/70 mt-1">We maintain our own yard and equipment fleet, eliminating subcontractor bottlenecks on all active sites.</p>
        </div>
        <a href="{r('materials/index.html')}" class="btn-gold rounded-full px-6 py-2.5 text-xs font-semibold shrink-0">
          Inspect Plant &amp; Machinery &rarr;
        </a>
      </div>
    </section>
    '''
    
    html = wrap_page("Construction Services | Civil, Residential, Commercial & Turnkey", 
                     "Comprehensive civil engineering and building construction services in Pune by GN Construction. Commercial, residential, turnkey, and institutional projects.", 
                     body, active_nav="services", depth=1)
    write_page("services/index.html", html)

# ==============================================================================
# 3. INDIVIDUAL SERVICE PAGES
# ==============================================================================
def build_service_details():
    services_data = [
        {
            "id": "civil-construction",
            "name": "Civil Construction",
            "tagline": "Structural RCC Excellence",
            "lead": "Complete RCC framed civil construction for residential, commercial, and institutional structures across Pune — executed from excavation to slab casting by our experienced B.E. Civil engineers.",
            "hero_img": "images/projects/konark-virtue-t4-karia.jpg",
            "features": [
                ("Deep Foundation Execution", "Open excavations, isolated footings, combined rafts, and bored under-reamed piles based on soil test strata reports."),
                ("Precision Formwork & Shuttering", "Utilising our inventory of 6,000 props, 1,600 spans, and 8,000 sqft of cuplock scaffolding for zero-deflection casting."),
                ("Reinforcement & Grade Verification", "Strict bar-bending schedules, cover block inspections, and manufacturer test certificates for all steel lots."),
                ("Designed-Mix Concrete & Testing", "Mix design compliance with compulsory 7-day and 28-day cube compressive strength tests logged per pour.")
            ],
            "related_project": "Konark Virtue — Tower 4",
            "related_link": "projects/konark-virtue-tower4.html"
        },
        {
            "id": "residential-construction",
            "name": "Residential Building Construction",
            "tagline": "From G+1 Walk-Ups to High-Rise Towers",
            "lead": "Constructing multi-storey residential towers, apartment complexes, and high-spec homes with developer-grade standards, structural longevity, and disciplined site scheduling.",
            "hero_img": "images/projects/jade-regency-wagholi.jpg",
            "features": [
                ("Developer-Grade Standards", "Constructed to meet rigorous developer quality norms such as CQRA third-party auditing."),
                ("Full Floor-Cycle Optimization", "Organised staging and formwork rotation ensuring predictable floor-to-floor cycle times without compromising curing."),
                ("Internal Masonry & Plaster", "High-density AAC block work or wire-cut brick masonry with plumb-line river-sand or gypsum plastering."),
                ("Waterproofing Integrity", "Multi-layer crystalline waterproofing in basements, podiums, sunken slabs, and terrace areas with water-ponding tests.")
            ],
            "related_project": "JADE Regency (30,000 sqft)",
            "related_link": "projects/jade-regency-wagholi.html"
        },
        {
            "id": "commercial-construction",
            "name": "Commercial Complex Construction",
            "tagline": "Business-Grade Buildings & Corporate Hubs",
            "lead": "Construction of high-traffic commercial complexes, corporate offices, and mixed-use business hubs designed for heavy occupant loads, basements, and modern exterior facades.",
            "hero_img": "images/projects/konark-business-centre-turnkey.jpg",
            "features": [
                ("Basement & Earth Retention", "Basement excavations, diaphragm and retaining walls, and sub-soil drainage systems designed for heavy water tables."),
                ("Large-Span Column Grids", "Structural RCC column spacing engineered to accommodate modern corporate floor plans and retail showrooms."),
                ("Integrated Core Services", "Pre-planned conduits, shafts, and provisions for commercial HVAC, elevators, fire suppression, and data raceways."),
                ("Façade & Finishing Readiness", "Structural tolerance engineered to support curtain wall glazing, ACP panelling, and premium stone cladding.")
            ],
            "related_project": "Konark Business Centre (Keshav Nagar)",
            "related_link": "projects/konark-business-centre.html"
        },
        {
            "id": "turnkey-construction",
            "name": "Turnkey Construction",
            "tagline": "Single Contract, Concept to Handover",
            "lead": "Complete end-to-end turnkey delivery under a single point of accountability — handling architectural coordination, RCC structural construction, services MEP, finishing, and final handover.",
            "hero_img": "images/projects/konark-business-centre-keshav-nagar.jpg",
            "features": [
                ("Single Point of Responsibility", "One line-item contract eliminating friction between architects, structural consultants, and finishing trades."),
                ("Transparent Line-Item Quotation", "Every component from excavation volume to electrical conduits itemised with exact brand and grade commitments."),
                ("Milestone-Linked Execution", "Structured cash-flow and milestone delivery schedule with weekly progress reporting and photo verification."),
                ("As-Built Documentation", "Complete as-built MEP line diagrams, warranties, and maintenance manuals delivered at final handover.")
            ],
            "related_project": "Konark Business Centre (Turnkey Commercial)",
            "related_link": "projects/konark-business-centre.html"
        },
        {
            "id": "institutional-construction",
            "name": "Institutional & Infrastructure Projects",
            "tagline": "Scale, Precision & Community Impact",
            "lead": "Construction of large-scale educational institutions, college campuses, and civic infrastructure built to withstand heavy public usage and stringent institutional safety guidelines.",
            "hero_img": "images/projects/tanishka-jadhavar-college-narhe.jpg",
            "features": [
                ("Large Floor-Plate Engineering", "Constructing expansive classroom wings, auditoriums, and laboratory spaces up to 85,000 sqft."),
                ("High Live-Load Calculations", "Reinforced floor slabs engineered for institutional dynamic loads, library stack weights, and assembly halls."),
                ("Heavy Cuplock Scaffolding", "Multi-tiered scaffolding arrangements engineered for tall floor heights and double-height entrance foyers."),
                ("Rapid Institutional Timelines", "Accelerated casting cycles organised around academic terms and institutional commencement deadlines.")
            ],
            "related_project": "Jadhavar College Building (85,000 sqft)",
            "related_link": "projects/tanishka-jadhavar-college.html"
        },
        {
            "id": "development-works",
            "name": "Development & Amenity Works",
            "tagline": "Clubhouses, Pools, Retaining Walls & Infrastructure",
            "lead": "Specialised external civil works, amenity structures, clubhouses, swimming pools, retaining walls, and underground water reservoirs for premier township developers.",
            "hero_img": "images/projects/godrej-greens-undri-clubhouse.jpg",
            "features": [
                ("Township Amenity Construction", "Complete construction of community clubhouses, multipurpose celebration halls, and gymnasiums."),
                ("Swimming Pools & Water Bodies", "RCC pool shells cast with water-tight concrete, PVC waterstops, and pressure-tested pool plumbing."),
                ("Massive Underground Water Tanks", "Execution of high-capacity water reservoirs such as our 13.7 Lakh litre UGWT at Kolte Patil 24K."),
                ("Engineered Retaining Walls", "Reinforced concrete and Phytroid earth-retaining walls designed for steep slope retention and site grading.")
            ],
            "related_project": "Godrej Greens Undri & Kolte Patil 24K",
            "related_link": "projects/godrej-greens-undri.html"
        }
    ]

    for s in services_data:
        r = lambda p: rel_path(p, 1)
        
        features_html = ""
        for title, desc in s['features']:
            features_html += f'''
            <div class="p-6 rounded-xl bg-paper border border-ink/10 space-y-2">
              <h4 class="font-serif text-lg font-bold text-ink">{title}</h4>
              <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">{desc}</p>
            </div>
            '''
            
        body = f'''
        <!-- Breadcrumb -->
        <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
          <div class="container flex items-center gap-2">
            <a href="{r('index.html')}" class="hover:text-forest">Home</a>
            <span>&rsaquo;</span>
            <a href="{r('services/index.html')}" class="hover:text-forest">Services</a>
            <span>&rsaquo;</span>
            <span class="text-ink font-medium">{s['name']}</span>
          </div>
        </div>

        <!-- Hero -->
        <section class="py-16 bg-paper-warm/40 border-b border-ink/10">
          <div class="container">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
              <div class="lg:col-span-7 space-y-4">
                <span class="eyebrow text-forest">{s['tagline']}</span>
                <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">{s['name']}</h1>
                <p class="text-base text-ink-soft leading-relaxed max-w-2xl">{s['lead']}</p>
                <div class="pt-2 flex flex-wrap gap-4">
                  <a href="{r('contact/index.html')}" class="btn-primary rounded-full px-6 py-3 text-xs font-semibold">Request Service Consultation</a>
                  <a href="{r(s['related_link'])}" class="btn-ghost rounded-full px-6 py-3 text-xs font-semibold">View Case Study &rarr;</a>
                </div>
              </div>
              <div class="lg:col-span-5">
                <div class="rounded-2xl overflow-hidden border border-ink/15 shadow-xl bg-ink/10">
                  <img src="{r(s['hero_img'])}" alt="{s['name']}" class="w-full h-auto object-cover max-h-[360px]">
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Features / Capabilities -->
        <section class="section bg-paper">
          <div class="container space-y-8">
            <div class="max-w-2xl space-y-2">
              <span class="eyebrow text-forest">Technical Scope</span>
              <h2 class="text-2xl sm:text-3xl font-serif text-ink">Engineering &amp; Execution Highlights</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              {features_html}
            </div>
          </div>
        </section>

        <!-- Project Reference Banner -->
        <section class="py-12 bg-paper-warm/50 border-t border-ink/10">
          <div class="container flex flex-col md:flex-row items-center justify-between gap-6">
            <div>
              <span class="text-xs font-mono uppercase text-gold font-semibold">Featured Proof of Capability</span>
              <h3 class="text-xl font-serif font-bold text-ink mt-1">Delivered: {s['related_project']}</h3>
              <p class="text-xs text-ink-soft mt-1">Read how GN Construction executed this project within strict technical specifications.</p>
            </div>
            <a href="{r(s['related_link'])}" class="btn-gold rounded-full px-6 py-2.5 text-xs font-semibold shrink-0">
              Read Project Case Study &rarr;
            </a>
          </div>
        </section>
        '''
        
        html = wrap_page(f"{s['name']} | Services", s['lead'], body, active_nav="services", depth=1)
        write_page(f"services/{s['id']}.html", html)

# ==============================================================================
# 4. PROJECTS PORTFOLIO (projects/index.html)
# ==============================================================================
def build_projects_index():
    r = lambda p: rel_path(p, 1)
    
    project_cards = ""
    for p in GN_PROJECTS:
        project_cards += f'''
        <div class="group rounded-2xl overflow-hidden border border-ink/10 bg-paper-warm/30 hover:border-forest/40 transition shadow-sm flex flex-col justify-between" data-category="{p['tag'].lower()}">
          <div>
            <div class="relative h-60 overflow-hidden bg-ink/10">
              <img src="{r(p['image'])}" alt="{p['name']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 left-3 bg-ink/80 text-paper text-[10px] font-mono uppercase font-semibold px-2.5 py-1 rounded-full backdrop-blur">
                {p['tag']} &bull; {p['area_sqft']} sqft
              </span>
              <div class="absolute bottom-3 right-3">
                <span class="bg-forest text-paper text-[11px] font-semibold px-2.5 py-0.5 rounded-full">{p['type']}</span>
              </div>
            </div>
            <div class="p-6 space-y-2.5">
              <p class="text-xs font-semibold text-gold font-mono uppercase">Client: {p['client']} &bull; {p['location']}</p>
              <h3 class="text-xl font-serif text-ink group-hover:text-forest transition">{p['name']}</h3>
              <p class="text-xs text-ink-soft leading-relaxed line-clamp-3">{p['description']}</p>
            </div>
          </div>
          <div class="p-6 pt-0 border-t border-ink/5 mt-4 flex items-center justify-between">
            <span class="text-[11px] text-ink-muted">{p['type']}</span>
            <a href="{r(f"projects/{p['id']}.html")}" class="inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
              <span>View Case Study</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
          </div>
        </div>
        '''
        
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Projects</span>
      </div>
    </div>

    <!-- Header Section -->
    <section class="py-16 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-4">
        <span class="eyebrow text-forest">Verified Track Record</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          Executed Projects Portfolio Across Pune.
        </h1>
        <p class="text-base text-ink-soft leading-relaxed max-w-2xl">
          A showcase of our landmark commercial, residential, institutional, and amenity projects executed for prominent developers and institutions.
        </p>
      </div>
    </section>

    <!-- Projects Grid -->
    <section class="section bg-paper">
      <div class="container space-y-10">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {project_cards}
        </div>
      </div>
    </section>

    <!-- Bottom Proposal CTA -->
    <section class="py-16 bg-ink text-paper border-t border-paper/10 text-center">
      <div class="container max-w-3xl space-y-5">
        <h3 class="text-2xl sm:text-4xl font-serif text-paper">Have a Commercial or Residential Tender?</h3>
        <p class="text-sm text-paper/70">Our directors and structural estimating team are available to review architectural drawings and submit competitive line-item quotations.</p>
        <a href="{r('contact/index.html')}" class="btn-gold rounded-full px-8 py-3.5 text-sm font-semibold inline-block">
          Submit Project Drawings &rarr;
        </a>
      </div>
    </section>
    '''
    
    html = wrap_page("Executed Projects Portfolio | GN Construction Pune", 
                     "Explore landmark projects executed by GN Construction in Pune: Konark Business Centre, Jadhavar College, Godrej Greens, Kolte Patil 24K, JADE Regency, and more.", 
                     body, active_nav="projects", depth=1)
    write_page("projects/index.html", html)

# ==============================================================================
# 5. INDIVIDUAL PROJECT DETAIL PAGES (7 PROJECTS)
# ==============================================================================
def build_project_details():
    for p in GN_PROJECTS:
        r = lambda path: rel_path(path, 1)
        
        img2_html = ""
        if p.get('image2'):
            img2_html = f'''
            <div class="rounded-2xl overflow-hidden border border-ink/15 shadow-md bg-ink/5 mt-6">
              <img src="{r(p['image2'])}" alt="{p['name']} Progress Photo" class="w-full h-auto object-cover max-h-[440px]">
              <div class="p-3 bg-paper border-t border-ink/10 text-[11px] text-ink-muted">Site Progress Documentation &bull; {p['name']}</div>
            </div>
            '''
            
        body = f'''
        <!-- Breadcrumb -->
        <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
          <div class="container flex items-center gap-2">
            <a href="{r('index.html')}" class="hover:text-forest">Home</a>
            <span>&rsaquo;</span>
            <a href="{r('projects/index.html')}" class="hover:text-forest">Projects</a>
            <span>&rsaquo;</span>
            <span class="text-ink font-medium">{p['name']}</span>
          </div>
        </div>

        <!-- Project Hero Header -->
        <section class="py-14 bg-paper-warm/40 border-b border-ink/10">
          <div class="container">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
              <div class="lg:col-span-8 space-y-4">
                <div class="flex flex-wrap items-center gap-2">
                  <span class="eyebrow text-forest">{p['type']}</span>
                  <span class="text-ink-muted">&bull;</span>
                  <span class="text-xs font-mono font-semibold text-gold">{p['location']}</span>
                </div>
                <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">{p['name']}</h1>
                <p class="text-base text-ink-soft leading-relaxed">{p['description']}</p>
              </div>

              <!-- Metadata Box -->
              <div class="lg:col-span-4 p-6 rounded-2xl bg-paper border border-ink/15 shadow-sm space-y-4 text-xs">
                <p class="font-serif text-base font-bold text-ink border-b border-ink/10 pb-2">Project Specifications</p>
                <div class="space-y-2">
                  <div class="flex justify-between py-1 border-b border-ink/5">
                    <span class="text-ink-muted">Client / Developer:</span>
                    <strong class="text-ink text-right">{p['client']}</strong>
                  </div>
                  <div class="flex justify-between py-1 border-b border-ink/5">
                    <span class="text-ink-muted">Location:</span>
                    <strong class="text-ink text-right">{p['location']}</strong>
                  </div>
                  <div class="flex justify-between py-1 border-b border-ink/5">
                    <span class="text-ink-muted">Built-Up Area / Scale:</span>
                    <strong class="text-ink text-right">{p['area_sqft']} sqft</strong>
                  </div>
                  <div class="flex justify-between py-1">
                    <span class="text-ink-muted">Contract Scope:</span>
                    <strong class="text-ink text-right">{p['scope']}</strong>
                  </div>
                </div>
                <a href="{r('contact/index.html')}" class="btn-primary w-full justify-center rounded-xl py-2.5 text-xs">Enquire Similar Build</a>
              </div>
            </div>
          </div>
        </section>

        <!-- Project Media & Detailed Scope -->
        <section class="section bg-paper">
          <div class="container space-y-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
              <!-- Left: Project Images -->
              <div class="lg:col-span-7 space-y-6">
                <div class="rounded-2xl overflow-hidden border border-ink/15 shadow-lg bg-ink/10">
                  <img src="{r(p['image'])}" alt="{p['name']}" class="w-full h-auto object-cover max-h-[500px]">
                  <div class="p-3 bg-paper border-t border-ink/10 text-xs text-ink-muted">Primary Site View &bull; {p['name']}</div>
                </div>
                {img2_html}
              </div>

              <!-- Right: Execution Brief -->
              <div class="lg:col-span-5 space-y-6">
                <div class="space-y-3">
                  <span class="eyebrow text-forest">Execution Methodology</span>
                  <h3 class="text-2xl font-serif text-ink">Engineering Scope &amp; Quality Standards</h3>
                  <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">
                    This project was executed under the direct oversight of GN Construction's civil engineering directors, deploying our own shuttering systems, dedicated site supervisors, and structured progress schedules.
                  </p>
                </div>

                <div class="space-y-4 pt-2">
                  <div class="p-4 rounded-xl bg-paper-warm/50 border border-ink/10 space-y-1">
                    <p class="text-xs font-bold text-ink uppercase font-mono">Structural RCC Framework</p>
                    <p class="text-xs text-ink-soft">Engineered formwork staging using props and cuplock scaffolding, ensuring continuous concrete pours and uniform slab surface finish.</p>
                  </div>
                  <div class="p-4 rounded-xl bg-paper-warm/50 border border-ink/10 space-y-1">
                    <p class="text-xs font-bold text-ink uppercase font-mono">Quality Auditing &amp; Testing</p>
                    <p class="text-xs text-ink-soft">Reinforcement spacing, concrete cover blocks, and compressive cube crushing tests conducted and documented at every structural stage.</p>
                  </div>
                  <div class="p-4 rounded-xl bg-paper-warm/50 border border-ink/10 space-y-1">
                    <p class="text-xs font-bold text-ink uppercase font-mono">Client Coordination</p>
                    <p class="text-xs text-ink-soft">Transparent milestone billing verified with joint site measurements and compliance with {p['client']}'s design specifications.</p>
                  </div>
                </div>

                <div class="pt-4 border-t border-ink/10">
                  <a href="{r('projects/index.html')}" class="inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-left"><path d="m12 19-7-7 7-7"></path><path d="M19 12H5"></path></svg>
                    <span>Back to All Projects</span>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </section>
        '''
        
        html = wrap_page(f"{p['name']} | Case Study", p['description'], body, active_nav="projects", depth=1)
        write_page(f"projects/{p['id']}.html", html)

# ==============================================================================
# 6. ABOUT COMPANY & LEADERSHIP (about/index.html)
# ==============================================================================
def build_about_page():
    r = lambda p: rel_path(p, 1)
    
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">About Us</span>
      </div>
    </div>

    <!-- Hero Header -->
    <section class="py-16 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-4">
        <span class="eyebrow text-forest">Company Background</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          A Group of Seasoned Civil Engineers, Building Since 2013.
        </h1>
        <p class="text-base text-ink-soft leading-relaxed max-w-2xl">
          {GN_ABOUT['intro']}
        </p>
      </div>
    </section>

    <!-- Mission & Goal -->
    <section class="section bg-paper">
      <div class="container">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="p-8 rounded-2xl bg-forest/5 border border-forest/20 space-y-3">
            <span class="text-xs uppercase font-mono font-bold text-forest tracking-wider">Our Core Mission</span>
            <p class="font-serif text-xl sm:text-2xl text-ink leading-snug">
              "{GN_ABOUT['mission']}"
            </p>
            <p class="text-xs text-ink-soft leading-relaxed pt-2">
              We focus on structural integrity, truthful client communication, and rigorous site work to provide predictable execution on every undertaking.
            </p>
          </div>

          <div class="p-8 rounded-2xl bg-gold/10 border border-gold/30 space-y-3">
            <span class="text-xs uppercase font-mono font-bold text-gold-deep tracking-wider">Our Primary Goal</span>
            <p class="font-serif text-xl sm:text-2xl text-ink leading-snug">
              "{GN_ABOUT['goal']}"
            </p>
            <p class="text-xs text-ink-soft leading-relaxed pt-2">
              Every job offered to GN Construction is completed within agreed milestone windows and adhering strictly to developer specifications and engineering norms.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Directors Leadership Profile -->
    <section class="section bg-paper-warm/40 border-t border-ink/10">
      <div class="container space-y-12">
        <div class="max-w-2xl space-y-2">
          <span class="eyebrow text-forest">Company Leadership</span>
          <h2 class="text-3xl sm:text-4xl font-serif text-ink tracking-tight">The Founding Directors</h2>
          <p class="text-sm text-ink-soft">Over 39 years of collective civil engineering expertise in residential and commercial sectors.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <!-- Director 1 -->
          <div class="p-8 rounded-2xl bg-paper border border-ink/10 shadow-sm space-y-4">
            <div class="flex items-center gap-4">
              <div class="w-16 h-16 rounded-2xl bg-forest text-paper flex items-center justify-center font-serif text-2xl font-bold shadow-md">
                NW
              </div>
              <div>
                <h3 class="text-2xl font-serif font-bold text-ink">{GN_FOUNDERS[0]['name']}</h3>
                <p class="text-xs font-semibold text-gold font-mono uppercase">{GN_FOUNDERS[0]['role']}</p>
                <p class="text-xs text-forest font-semibold">{GN_FOUNDERS[0]['qualification']}</p>
              </div>
            </div>
            <div class="pt-2 border-t border-ink/10 space-y-2">
              <p class="text-xs text-ink font-semibold uppercase font-mono">Professional Background</p>
              <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">
                {GN_FOUNDERS[0]['experience']} He leads the company's structural planning, tender evaluation, developer client partnerships, and large-scale project execution across Pune.
              </p>
            </div>
          </div>

          <!-- Director 2 -->
          <div class="p-8 rounded-2xl bg-paper border border-ink/10 shadow-sm space-y-4">
            <div class="flex items-center gap-4">
              <div class="w-16 h-16 rounded-2xl bg-ink text-paper flex items-center justify-center font-serif text-2xl font-bold shadow-md">
                HH
              </div>
              <div>
                <h3 class="text-2xl font-serif font-bold text-ink">{GN_FOUNDERS[1]['name']}</h3>
                <p class="text-xs font-semibold text-gold font-mono uppercase">{GN_FOUNDERS[1]['role']}</p>
                <p class="text-xs text-gold font-semibold">{GN_FOUNDERS[1]['qualification']}</p>
              </div>
            </div>
            <div class="pt-2 border-t border-ink/10 space-y-2">
              <p class="text-xs text-ink font-semibold uppercase font-mono">Professional Background</p>
              <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">
                {GN_FOUNDERS[1]['experience']} He directs on-site operations, formwork systems, quality software implementation (CQRA), concrete batching, and site team supervision.
              </p>
            </div>
          </div>
        </div>

        <!-- Staff Roster -->
        <div class="p-8 rounded-2xl bg-paper border border-ink/10 space-y-6">
          <div>
            <h3 class="font-serif text-xl font-bold text-ink">Site Engineering &amp; Supervision Staff</h3>
            <p class="text-xs text-ink-muted mt-1">Our qualified on-site team managing daily casting, bar-bending, safety, and level surveys.</p>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 text-xs">
            {"".join([f"<div class='p-3.5 rounded-xl bg-paper-warm/50 border border-ink/10 font-medium text-ink flex items-center gap-2.5'><span class='w-2 h-2 rounded-full bg-forest shrink-0'></span>{st}</div>" for st in GN_STAFF])}
          </div>
        </div>
      </div>
    </section>

    <!-- Associates & Registration Info -->
    <section class="section bg-paper">
      <div class="container">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
          <div class="lg:col-span-6 space-y-4">
            <span class="eyebrow text-forest">Group Structure</span>
            <h3 class="text-2xl font-serif text-ink">GN Group of Companies</h3>
            <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">
              GN Construction operates in synergy with our sister entities to provide specialized infrastructure, material procurement, and civil engineering capabilities.
            </p>
            <div class="space-y-2 pt-2">
              {"".join([f"<div class='p-3 rounded-lg bg-paper-warm/40 border border-ink/10 font-serif text-sm font-semibold text-ink flex items-center justify-between'><span>{a}</span><span class='text-xs font-mono text-forest font-normal'>Registered Entity</span></div>" for a in GN_ASSOCIATES])}
            </div>
          </div>

          <div class="lg:col-span-6 space-y-4">
            <span class="eyebrow text-gold">Location &amp; Registry</span>
            <h3 class="text-2xl font-serif text-ink">Registered Office</h3>
            <div class="p-6 rounded-2xl bg-paper-warm/50 border border-ink/10 space-y-3 text-xs leading-relaxed">
              <p><strong class="text-ink">Registered Address:</strong><br>{GN_BRAND['address']}</p>
              <p><strong class="text-ink">Establishment Year:</strong> 2013</p>
              <p><strong class="text-ink">Primary Operating Territory:</strong> Pune Metropolitan Region &amp; Maharashtra</p>
              <p><strong class="text-ink">Direct Enquiries:</strong> {GN_BRAND['phone']} | {GN_BRAND['email']}</p>
              <div class="pt-3">
                <a href="{r('contact/index.html')}" class="btn-primary rounded-full px-5 py-2 text-xs">Contact Headquarters &rarr;</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    '''
    
    html = wrap_page("About GN Construction | Founders & Company Profile", 
                     "Learn about GN Construction, founded in 2013 by civil engineers Mr. Nitin Wable and Mr. Hermeetsingh Hoda. Salisbury Park, Pune.", 
                     body, active_nav="about", depth=1)
    write_page("about/index.html", html)

# ==============================================================================
# 7. WHY GN CONSTRUCTION (why-gn/index.html)
# ==============================================================================
def build_why_gn():
    r = lambda p: rel_path(p, 1)
    
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Why GN Construction</span>
      </div>
    </div>

    <!-- Header Section -->
    <section class="py-16 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-4">
        <span class="eyebrow text-forest">The Contractor Difference</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          Why Leading Pune Developers Rely on GN Construction.
        </h1>
        <p class="text-base text-ink-soft leading-relaxed max-w-2xl">
          In an industry often marred by subcontracting layers and delayed formwork, GN Construction operates as a self-resourced, engineer-led civil contractor.
        </p>
      </div>
    </section>

    <!-- 6 Core Differentiators -->
    <section class="section bg-paper">
      <div class="container space-y-12">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div class="p-8 rounded-2xl bg-paper-warm/30 border border-ink/10 space-y-3 hover:border-forest/40 transition">
            <span class="text-2xl font-serif font-bold text-forest">01</span>
            <h3 class="text-xl font-serif text-ink font-bold">Engineering Leadership</h3>
            <p class="text-xs text-ink-soft leading-relaxed">
              Our company is founded and actively directed by B.E. Civil engineers with 25 and 14 years of hands-on experience, not financial middlemen.
            </p>
          </div>

          <div class="p-8 rounded-2xl bg-paper-warm/30 border border-ink/10 space-y-3 hover:border-forest/40 transition">
            <span class="text-2xl font-serif font-bold text-forest">02</span>
            <h3 class="text-xl font-serif text-ink font-bold">Self-Owned Formwork Fleet</h3>
            <p class="text-xs text-ink-soft leading-relaxed">
              We own 6,000 props, 1,600 spans, and 8,000 sqft of cuplock scaffolding. We never stall casting schedules waiting for rented formwork.
            </p>
          </div>

          <div class="p-8 rounded-2xl bg-paper-warm/30 border border-ink/10 space-y-3 hover:border-forest/40 transition">
            <span class="text-2xl font-serif font-bold text-forest">03</span>
            <h3 class="text-xl font-serif text-ink font-bold">CQRA Monitored Quality</h3>
            <p class="text-xs text-ink-soft leading-relaxed">
              We are experienced working with third-party quality auditors and digital platforms like CQRA to log reinforcement and slump test clearances.
            </p>
          </div>

          <div class="p-8 rounded-2xl bg-paper-warm/30 border border-ink/10 space-y-3 hover:border-forest/40 transition">
            <span class="text-2xl font-serif font-bold text-forest">04</span>
            <h3 class="text-xl font-serif text-ink font-bold">Tier-1 Developer Trust</h3>
            <p class="text-xs text-ink-soft leading-relaxed">
              Trusted by 15+ established developers including Godrej Properties, Kolte Patil, Karia Properties, and Wadhwa Group.
            </p>
          </div>

          <div class="p-8 rounded-2xl bg-paper-warm/30 border border-ink/10 space-y-3 hover:border-forest/40 transition">
            <span class="text-2xl font-serif font-bold text-forest">05</span>
            <h3 class="text-xl font-serif text-ink font-bold">Multi-Crore Financial Strength</h3>
            <p class="text-xs text-ink-soft leading-relaxed">
              With proven turnover reaching ₹7.65 Crore annually, we maintain healthy credit lines and reliable cash flow to fund rapid materials procurement.
            </p>
          </div>

          <div class="p-8 rounded-2xl bg-paper-warm/30 border border-ink/10 space-y-3 hover:border-forest/40 transition">
            <span class="text-2xl font-serif font-bold text-forest">06</span>
            <h3 class="text-xl font-serif text-ink font-bold">Honest &amp; Timely Handover</h3>
            <p class="text-xs text-ink-soft leading-relaxed">
              Built on our motto: "Quality, Honesty &amp; Hard Work." We strictly honor line-item contract terms and project completion milestones.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Call to action -->
    <section class="py-14 bg-forest text-paper text-center">
      <div class="container max-w-3xl space-y-4">
        <h3 class="text-2xl sm:text-3xl font-serif text-paper">Ready to discuss your project specifications?</h3>
        <p class="text-xs sm:text-sm text-paper/80">Connect with our directors for a technical review of your structural drawings.</p>
        <a href="{r('contact/index.html')}" class="btn-gold rounded-full px-8 py-3 text-xs font-semibold inline-block">
          Contact Our Engineering Team &rarr;
        </a>
      </div>
    </section>
    '''
    
    html = wrap_page("Why GN Construction | Engineering Excellence & Developer Trust", 
                     "Discover the 6 key differentiators of GN Construction: civil leadership, owned shuttering, CQRA quality, and Tier-1 developer experience.", 
                     body, active_nav="about", depth=1)
    write_page("why-gn/index.html", html)

# ==============================================================================
# 8. CLIENTS PAGE (clients/index.html)
# ==============================================================================
def build_clients_page():
    r = lambda p: rel_path(p, 1)
    
    client_cards = ""
    for c in GN_CLIENTS:
        client_cards += f'''
        <div class="p-6 rounded-2xl bg-paper border border-ink/10 shadow-sm hover:border-forest/40 transition flex items-center justify-between group">
          <div class="space-y-1">
            <h3 class="font-serif text-lg font-bold text-ink group-hover:text-forest transition">{c}</h3>
            <p class="text-xs text-ink-muted">Valued Construction Partner &bull; Pune / Mumbai</p>
          </div>
          <span class="w-8 h-8 rounded-full bg-forest/10 text-forest flex items-center justify-center font-bold text-xs">
            &check;
          </span>
        </div>
        '''
        
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Clients</span>
      </div>
    </div>

    <!-- Header Section -->
    <section class="py-16 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-4">
        <span class="eyebrow text-forest">Partnerships Built on Performance</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          Trusted by Prominent Developers &amp; Corporate Clients.
        </h1>
        <p class="text-base text-ink-soft leading-relaxed max-w-2xl">
          Over 12 years, GN Construction has proudly executed civil and structural contracts for premier real estate developers, hospitality groups, and educational trusts across Pune and Maharashtra.
        </p>
      </div>
    </section>

    <!-- Clients Grid -->
    <section class="section bg-paper">
      <div class="container space-y-8">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {client_cards}
        </div>
      </div>
    </section>
    '''
    
    html = wrap_page("Our Clients & Developer Partners | GN Construction", 
                     "View the list of 15+ premier developers and clients partnering with GN Construction: Godrej Properties, Kolte Patil, Karia Properties, Wadhwa Group, and more.", 
                     body, active_nav="clients", depth=1)
    write_page("clients/index.html", html)

# ==============================================================================
# 9. MATERIALS & MACHINERY (materials/index.html)
# ==============================================================================
def build_materials_page():
    r = lambda p: rel_path(p, 1)
    
    asset_rows = ""
    for item, qty in GN_ASSETS.items():
        asset_rows += f'''
        <tr class="border-b border-ink/10 hover:bg-forest/5 transition">
          <td class="py-3 px-4 font-medium text-ink">{item}</td>
          <td class="py-3 px-4 text-forest font-mono font-bold text-right">{qty}</td>
          <td class="py-3 px-4 text-xs text-ink-muted">Owned Asset / Ready for Deployment</td>
        </tr>
        '''
        
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Plant &amp; Machinery</span>
      </div>
    </div>

    <!-- Header Section -->
    <section class="py-16 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-4">
        <span class="eyebrow text-forest">Capital Strength</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          Owned Shuttering Systems, Heavy Plant &amp; Equipment.
        </h1>
        <p class="text-base text-ink-soft leading-relaxed max-w-2xl">
          We maintain an extensive, self-owned fleet of formwork materials, batching machines, and lifting systems to ensure our projects run with uninterrupted momentum.
        </p>
      </div>
    </section>

    <!-- Machinery Inventory Table -->
    <section class="section bg-paper">
      <div class="container">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
          <div class="lg:col-span-8 space-y-6">
            <h2 class="text-2xl font-serif text-ink font-bold">Formwork, Scaffolding &amp; Machinery Assets</h2>
            <div class="overflow-x-auto rounded-2xl border border-ink/15 shadow-sm bg-paper">
              <table class="w-full text-left text-xs sm:text-sm">
                <thead class="bg-paper-warm border-b border-ink/10 text-ink-muted uppercase font-mono text-[11px]">
                  <tr>
                    <th class="py-3.5 px-4 font-semibold">Equipment / Asset Description</th>
                    <th class="py-3.5 px-4 font-semibold text-right">Owned Quantity</th>
                    <th class="py-3.5 px-4 font-semibold">Status</th>
                  </tr>
                </thead>
                <tbody>
                  {asset_rows}
                </tbody>
              </table>
            </div>
          </div>

          <!-- Right Column: Site Photos -->
          <div class="lg:col-span-4 space-y-6">
            <div class="rounded-2xl overflow-hidden border border-ink/15 shadow-md bg-paper">
              <img src="{r('images/places/gn-construction-equipment-machinery.jpg')}" alt="GN Construction Yard & Equipment" class="w-full h-auto object-cover">
              <div class="p-4 bg-paper text-xs text-ink-muted space-y-1">
                <p class="font-bold text-ink">GN Equipment Yard</p>
                <p>Central inventory depot supporting active sites across Pune.</p>
              </div>
            </div>

            <div class="rounded-2xl overflow-hidden border border-ink/15 shadow-md bg-paper">
              <img src="{r('images/projects/pt-shuttering-cuplock.jpg')}" alt="Cuplock Staging System on Site" class="w-full h-auto object-cover">
              <div class="p-4 bg-paper text-xs text-ink-muted space-y-1">
                <p class="font-bold text-ink">Cuplock Scaffolding in Operation</p>
                <p>Heavy duty staging providing rigid slab support.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    '''
    
    html = wrap_page("Owned Machinery & Shuttering Assets | GN Construction", 
                     "Inventory of owned plant and machinery at GN Construction: 6,000 props, cuplock systems, concrete mixers, weigh batchers, and vibrators.", 
                     body, active_nav="about", depth=1)
    write_page("materials/index.html", html)

# ==============================================================================
# 10. METHODOLOGY (methodology/index.html)
# ==============================================================================
def build_methodology_page():
    r = lambda p: rel_path(p, 1)
    
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Methodology</span>
      </div>
    </div>

    <!-- Header Section -->
    <section class="py-16 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-4">
        <span class="eyebrow text-forest">Execution Lifecycle</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          Systematic Engineering &amp; Quality Management.
        </h1>
        <p class="text-base text-ink-soft leading-relaxed max-w-2xl">
          How GN Construction translates architectural drawings into robust physical structures through disciplined milestone staging and CQRA quality compliance.
        </p>
      </div>
    </section>

    <!-- Stages Timeline -->
    <section class="section bg-paper">
      <div class="container max-w-4xl space-y-8">
        <div class="space-y-6">
          <div class="p-6 rounded-2xl bg-paper-warm/40 border border-ink/10 flex flex-col sm:flex-row gap-5 items-start">
            <span class="w-12 h-12 rounded-xl bg-forest text-paper flex items-center justify-center font-serif text-lg font-bold shrink-0">1</span>
            <div class="space-y-1">
              <h3 class="text-xl font-serif text-ink font-bold">Soil Investigation &amp; Foundation Engineering</h3>
              <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">
                Standard Penetration Tests (SPT) to identify safe bearing capacity (SBC) and strata depth. Designing foundation formwork based on load requirements (isolated, raft, or bored piles).
              </p>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-paper-warm/40 border border-ink/10 flex flex-col sm:flex-row gap-5 items-start">
            <span class="w-12 h-12 rounded-xl bg-forest text-paper flex items-center justify-center font-serif text-lg font-bold shrink-0">2</span>
            <div class="space-y-1">
              <h3 class="text-xl font-serif text-ink font-bold">Formwork Staging &amp; Reinforcement Binding</h3>
              <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">
                Staging using our own cuplock systems, props, and spans. Checking bar-bending schedules, lap lengths, and cover block placements before casting.
              </p>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-paper-warm/40 border border-ink/10 flex flex-col sm:flex-row gap-5 items-start">
            <span class="w-12 h-12 rounded-xl bg-forest text-paper flex items-center justify-center font-serif text-lg font-bold shrink-0">3</span>
            <div class="space-y-1">
              <h3 class="text-xl font-serif text-ink font-bold">Concrete Pouring &amp; Vibration Quality</h3>
              <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">
                Supervised pour using weigh batchers and mechanical vibrators to eliminate honeycombing. Casting standard test cubes for 7-day and 28-day crushing audits.
              </p>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-paper-warm/40 border border-ink/10 flex flex-col sm:flex-row gap-5 items-start">
            <span class="w-12 h-12 rounded-xl bg-forest text-paper flex items-center justify-center font-serif text-lg font-bold shrink-0">4</span>
            <div class="space-y-1">
              <h3 class="text-xl font-serif text-ink font-bold">Superstructure Masonry &amp; MEP Integration</h3>
              <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">
                High-density block work and brick masonry with embedded electrical conduits and plumbing sleeves pre-planned to avoid hacking structural concrete.
              </p>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-paper-warm/40 border border-ink/10 flex flex-col sm:flex-row gap-5 items-start">
            <span class="w-12 h-12 rounded-xl bg-forest text-paper flex items-center justify-center font-serif text-lg font-bold shrink-0">5</span>
            <div class="space-y-1">
              <h3 class="text-xl font-serif text-ink font-bold">Handover &amp; As-Built Certification</h3>
              <p class="text-xs sm:text-sm text-ink-soft leading-relaxed">
                Final punch-list rectification, joint site measurements, delivery of as-built drawings, and formal completion certification.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    '''
    
    html = wrap_page("Construction Methodology & Quality Auditing | GN Construction", 
                     "Learn about GN Construction's structured civil execution methodology: foundation engineering, cuplock staging, concrete vibration, and CQRA compliance.", 
                     body, active_nav="about", depth=1)
    write_page("methodology/index.html", html)

# ==============================================================================
# 11. ESTIMATOR / TOOLS (tools/index.html)
# ==============================================================================
def build_tools_page():
    r = lambda p: rel_path(p, 1)
    
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Tools &amp; Estimator</span>
      </div>
    </div>

    <!-- Header Section -->
    <section class="py-16 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-4">
        <span class="eyebrow text-forest">Technical Estimating Desk</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          Construction Cost &amp; Built-up Estimator.
        </h1>
        <p class="text-base text-ink-soft leading-relaxed max-w-2xl">
          Quickly compute preliminary budget estimates for your commercial complex, residential building, or turnkey development based on Pune construction norms.
        </p>
      </div>
    </section>

    <!-- Interactive Estimator -->
    <section class="section bg-paper">
      <div class="container max-w-3xl">
        <div class="p-8 rounded-2xl bg-paper-warm/50 border border-ink/15 shadow-sm space-y-6">
          <div class="space-y-2">
            <h3 class="text-2xl font-serif text-ink font-bold">Project Cost Calculator</h3>
            <p class="text-xs text-ink-muted">Enter your approximate built-up area and select the project type for indicative budgeting.</p>
          </div>

          <div class="space-y-4 text-xs">
            <div>
              <label class="block font-semibold text-ink mb-1">Built-Up Area (sq. ft.)</label>
              <input type="number" id="calc-area" value="10000" class="w-full bg-paper border border-ink/20 rounded-xl px-4 py-2.5 text-ink text-sm font-semibold focus:border-forest focus:outline-none" oninput="calculateEstimate()">
            </div>

            <div>
              <label class="block font-semibold text-ink mb-1">Project Construction Typology</label>
              <select id="calc-type" class="w-full bg-paper border border-ink/20 rounded-xl px-4 py-2.5 text-ink text-sm font-semibold focus:border-forest focus:outline-none" onchange="calculateEstimate()">
                <option value="2200">Civil &amp; RCC Structural Only (~₹2,200/sqft)</option>
                <option value="2600" selected>Residential Building Standard (~₹2,600/sqft)</option>
                <option value="2900">Commercial Complex Turnkey (~₹2,900/sqft)</option>
                <option value="3400">Institutional &amp; Campus Building (~₹3,400/sqft)</option>
              </select>
            </div>

            <div class="pt-4 border-t border-ink/10 space-y-3">
              <div class="p-5 rounded-xl bg-forest/10 border border-forest/20 flex items-center justify-between">
                <div>
                  <p class="text-xs uppercase font-mono text-forest font-semibold">Estimated Budget Range</p>
                  <p id="calc-total" class="text-2xl sm:text-3xl font-serif font-bold text-forest mt-0.5">₹2.60 Crore</p>
                </div>
                <div class="text-right text-[11px] text-ink-muted">
                  <p>Subject to architectural drawings &amp; soil strata</p>
                </div>
              </div>

              <div class="grid grid-cols-2 gap-3 text-[11px] text-ink-soft">
                <div class="p-3 rounded-lg bg-paper border border-ink/10">
                  <span class="font-bold text-ink">Estimated Steel Required:</span>
                  <p id="calc-steel" class="font-mono text-forest mt-0.5">~35 Metric Tonnes</p>
                </div>
                <div class="p-3 rounded-lg bg-paper border border-ink/10">
                  <span class="font-bold text-ink">Estimated Cement Required:</span>
                  <p id="calc-cement" class="font-mono text-forest mt-0.5">~4,000 Bags</p>
                </div>
              </div>
            </div>

            <div class="pt-4 text-center">
              <a href="{r('contact/index.html')}" class="btn-primary rounded-full px-8 py-3 text-xs font-semibold">
                Request Line-Item Quotation &rarr;
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <script>
      function calculateEstimate() {{
        const area = parseFloat(document.getElementById('calc-area').value) || 0;
        const rate = parseFloat(document.getElementById('calc-type').value) || 0;
        const total = area * rate;
        
        let totalStr = "";
        if (total >= 10000000) {{
          totalStr = "₹" + (total / 10000000).toFixed(2) + " Crore";
        }} else if (total >= 100000) {{
          totalStr = "₹" + (total / 100000).toFixed(2) + " Lakh";
        }} else {{
          totalStr = "₹" + total.toLocaleString('en-IN');
        }}
        
        document.getElementById('calc-total').innerText = totalStr;
        
        // Indicative material consumption rules of thumb
        const steelTonnes = (area * 3.5 / 1000).toFixed(1);
        const cementBags = Math.round(area * 0.4);
        document.getElementById('calc-steel').innerText = "~" + steelTonnes + " Metric Tonnes";
        document.getElementById('calc-cement').innerText = "~" + cementBags.toLocaleString('en-IN') + " Bags";
      }}
    </script>
    '''
    
    html = wrap_page("Construction Cost Estimator | GN Construction Pune", 
                     "Interactive construction cost calculator for Pune commercial and residential builds. Calculate budget ranges, steel, and cement requirements.", 
                     body, active_nav="tools", depth=1)
    write_page("tools/index.html", html)

# ==============================================================================
# 12. GN AI TECHNICAL ASSISTANT PAGE (gn-ai/index.html)
# ==============================================================================
def build_ai_page():
    r = lambda p: rel_path(p, 1)
    
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">GN AI Assistant</span>
      </div>
    </div>

    <!-- Header Section -->
    <section class="py-14 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-3">
        <span class="eyebrow text-forest">Technical Civil Knowledge Engine</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          GN AI Engineering Assistant.
        </h1>
        <p class="text-sm sm:text-base text-ink-soft leading-relaxed max-w-2xl">
          Interact directly with our knowledge base covering GN Construction's project track record, owned shuttering assets, foundation engineering principles, and Pune construction standards.
        </p>
      </div>
    </section>

    <!-- Chat Console Section -->
    <section class="section bg-paper">
      <div class="container max-w-4xl">
        <div class="rounded-2xl bg-ink text-paper border border-ink shadow-2xl overflow-hidden flex flex-col h-[520px]">
          <div class="p-4 bg-ink border-b border-paper/10 flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-9 h-9 rounded-full bg-gradient-to-tr from-forest to-gold flex items-center justify-center font-bold text-xs text-paper">
                GN
              </div>
              <div>
                <p class="font-serif text-base font-semibold text-paper">GN Construction Engineering AI</p>
                <p class="text-[11px] text-paper/60">Trained on Verified GN Project Data &bull; Pune</p>
              </div>
            </div>
            <span class="text-[10px] font-mono text-gold uppercase px-2.5 py-1 rounded bg-gold/10">Active Session</span>
          </div>

          <!-- Message History -->
          <div id="ai-chat-messages" class="flex-1 p-5 overflow-y-auto space-y-4 text-xs leading-relaxed" aria-label="GN AI conversation">
            <div class="flex items-start gap-3">
              <div class="w-7 h-7 rounded-full bg-forest text-paper flex items-center justify-center text-[10px] shrink-0 font-bold">GN</div>
              <div class="bg-paper/10 p-4 rounded-2xl rounded-tl-sm max-w-[85%] text-paper/90 space-y-2">
                <p>Welcome! I am GN Construction's AI assistant. You can ask me questions such as:</p>
                <ul class="list-disc pl-4 space-y-1 text-paper/70">
                  <li>What landmark projects has GN Construction completed?</li>
                  <li>Who are the directors and what is their civil engineering qualification?</li>
                  <li>What formwork and machinery assets does GN Construction own?</li>
                  <li>What scope did GN execute at Konark Business Centre and Godrej Greens?</li>
                  <li>What are typical RCC construction rates in Pune?</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Chat Input Bar -->
          <form id="ai-chat-form" class="p-3.5 bg-ink/90 border-t border-paper/10 flex items-center gap-2" onsubmit="event.preventDefault(); submitAiMessage();">
            <input type="text" id="ai-chat-input" placeholder="Type your engineering or project question..." class="flex-1 bg-paper/10 border border-paper/15 rounded-xl px-4 py-2.5 text-xs text-paper placeholder-paper/40 focus:outline-none focus:border-gold">
            <button type="submit" class="bg-forest text-paper px-4 py-2.5 rounded-xl hover:bg-forest-deep transition flex items-center gap-1.5 text-xs font-semibold">
              <span>Send</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-send"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
          </form>
        </div>
      </div>
    </section>
    '''
    
    html = wrap_page("GN AI Technical Assistant | Construction Intelligence", 
                     "Interactive engineering assistant answering questions about GN Construction's projects, formwork assets, directors, and civil construction norms.", 
                     body, active_nav="ai", depth=1)
    write_page("gn-ai/index.html", html)

# ==============================================================================
# 13. CONTACT PAGE (contact/index.html)
# ==============================================================================
def build_contact_page():
    r = lambda p: rel_path(p, 1)
    
    body = f'''
    <!-- Breadcrumb -->
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Contact</span>
      </div>
    </div>

    <!-- Header Section -->
    <section class="py-16 bg-paper-warm/50 border-b border-ink/10">
      <div class="container max-w-4xl space-y-4">
        <span class="eyebrow text-forest">Connect With Our Engineering Team</span>
        <h1 class="text-3xl sm:text-5xl font-serif text-ink tracking-tight">
          Direct Access to Civil Directors.
        </h1>
        <p class="text-base text-ink-soft leading-relaxed max-w-2xl">
          Whether you are tendering a commercial parcel, planning an institutional campus, or seeking a reliable civil contractor in Pune, we welcome your enquiry.
        </p>
      </div>
    </section>

    <!-- Contact Grid -->
    <section class="section bg-paper">
      <div class="container">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
          <!-- Left: Address & Details -->
          <div class="lg:col-span-5 space-y-6">
            <div class="p-8 rounded-2xl bg-paper-warm/50 border border-ink/10 space-y-5 text-xs">
              <div>
                <p class="eyebrow text-forest">Headquarters</p>
                <h3 class="font-serif text-2xl font-bold text-ink mt-1">Salisbury Park Office</h3>
              </div>

              <div class="space-y-3 text-ink-soft leading-relaxed pt-2">
                <div class="flex items-start gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-map-pin text-forest shrink-0 mt-0.5"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"></path><circle cx="12" cy="10" r="3"></circle></svg>
                  <div>
                    <strong class="text-ink">Office Address:</strong><br>
                    {GN_BRAND['address']}
                  </div>
                </div>

                <div class="flex items-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-phone text-forest shrink-0"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                  <div>
                    <strong class="text-ink">Telephone:</strong> {GN_BRAND['phone']}
                  </div>
                </div>

                <div class="flex items-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-mail text-forest shrink-0"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
                  <div>
                    <strong class="text-ink">Email:</strong> {GN_BRAND['email']}
                  </div>
                </div>

                <div class="flex items-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-clock text-forest shrink-0"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                  <div>
                    <strong class="text-ink">Working Hours:</strong> Mon–Sat &bull; 09:00–18:30
                  </div>
                </div>
              </div>

              <div class="pt-3 border-t border-ink/10 text-[11px] text-ink-muted">
                <p><strong>Note for Clients:</strong> Phone and email provided are initial communication points. To confirm direct lines or schedule an on-site consultation, submit the enquiry form.</p>
              </div>
            </div>
          </div>

          <!-- Right: Interactive Enquiry Form -->
          <div class="lg:col-span-7">
            <div class="p-8 rounded-2xl bg-paper-warm/30 border border-ink/15 shadow-sm space-y-6">
              <div class="space-y-1">
                <h3 class="font-serif text-2xl font-bold text-ink">Submit Project Enquiry / Tender</h3>
                <p class="text-xs text-ink-muted">Share your project specifications for a structured technical response from our directors.</p>
              </div>

              <form class="space-y-4 text-xs" onsubmit="event.preventDefault(); alert('Thank you for reaching out to GN Construction. Our engineering directors will review your enquiry promptly.');">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="block font-semibold text-ink mb-1">Your Full Name *</label>
                    <input type="text" required placeholder="e.g. Rajesh Patil" class="w-full bg-paper border border-ink/20 rounded-xl px-4 py-2.5 text-ink focus:border-forest focus:outline-none">
                  </div>
                  <div>
                    <label class="block font-semibold text-ink mb-1">Organization / Developer Name</label>
                    <input type="text" placeholder="e.g. Patil Properties" class="w-full bg-paper border border-ink/20 rounded-xl px-4 py-2.5 text-ink focus:border-forest focus:outline-none">
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="block font-semibold text-ink mb-1">Phone Number *</label>
                    <input type="tel" required placeholder="+91 98765 43210" class="w-full bg-paper border border-ink/20 rounded-xl px-4 py-2.5 text-ink focus:border-forest focus:outline-none">
                  </div>
                  <div>
                    <label class="block font-semibold text-ink mb-1">Email Address *</label>
                    <input type="email" required placeholder="name@company.com" class="w-full bg-paper border border-ink/20 rounded-xl px-4 py-2.5 text-ink focus:border-forest focus:outline-none">
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="block font-semibold text-ink mb-1">Project Typology *</label>
                    <select required class="w-full bg-paper border border-ink/20 rounded-xl px-4 py-2.5 text-ink focus:border-forest focus:outline-none">
                      <option value="">Select project type</option>
                      <option value="commercial">Commercial Complex / Turnkey</option>
                      <option value="residential">Residential Building / High-Rise</option>
                      <option value="civil">Civil &amp; RCC Structural Contract</option>
                      <option value="institutional">Institutional / Educational Campus</option>
                      <option value="development">Development / Amenities / Retaining Wall</option>
                    </select>
                  </div>
                  <div>
                    <label class="block font-semibold text-ink mb-1">Estimated Built-Up Area (sq. ft.)</label>
                    <input type="text" placeholder="e.g. 25,000 sqft" class="w-full bg-paper border border-ink/20 rounded-xl px-4 py-2.5 text-ink focus:border-forest focus:outline-none">
                  </div>
                </div>

                <div>
                  <label class="block font-semibold text-ink mb-1">Project Location / Scope Details *</label>
                  <textarea rows="4" required placeholder="Describe your site location, status of structural drawings, expected start date, and specific requirements..." class="w-full bg-paper border border-ink/20 rounded-xl px-4 py-2.5 text-ink focus:border-forest focus:outline-none"></textarea>
                </div>

                <button type="submit" class="btn-primary rounded-full px-8 py-3 text-xs font-semibold shadow">
                  Submit Technical Enquiry &rarr;
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
    '''
    
    html = wrap_page("Contact GN Construction | Salisbury Park, Pune Office", 
                     "Get in touch with GN Construction headquarters at Salisbury Park, Pune. Submit project drawings and commercial tenders directly to our civil directors.", 
                     body, active_nav="contact", depth=1)
    write_page("contact/index.html", html)

# ==============================================================================
# 14. PRIVACY POLICY & TERMS OF SERVICE
# ==============================================================================
def build_legal_pages():
    r = lambda p: rel_path(p, 1)
    
    # Privacy Policy
    privacy_body = f'''
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Privacy Policy</span>
      </div>
    </div>
    <section class="section bg-paper">
      <div class="container max-w-3xl space-y-6 text-xs sm:text-sm text-ink-soft leading-relaxed">
        <h1 class="text-3xl font-serif text-ink font-bold">Privacy Policy</h1>
        <p class="text-ink-muted text-xs">Last updated: January 2026</p>
        <p>This privacy policy applies to GN Construction (GN Group of Companies), headquartered at Sr. No. 585, Plot No. 88/90, Salisbury Park, Pune - 411038.</p>
        <h3 class="text-lg font-serif font-bold text-ink pt-2">1. Information Collection</h3>
        <p>We collect information you provide directly through our contact forms, estimator inquiries, and telephone communications, including your name, contact phone number, email address, developer entity, and architectural project specifications.</p>
        <h3 class="text-lg font-serif font-bold text-ink pt-2">2. Use of Information</h3>
        <p>Information shared is used exclusively for evaluating tender proposals, providing line-item estimates, responding to technical questions, and communicating regarding active or proposed construction contracts.</p>
        <h3 class="text-lg font-serif font-bold text-ink pt-2">3. Confidentiality</h3>
        <p>Architectural plans, structural engineering drawings, and developer commercial terms shared with GN Construction are treated with strict professional confidentiality.</p>
      </div>
    </section>
    '''
    write_page("privacy-policy/index.html", wrap_page("Privacy Policy", "GN Construction Privacy Policy", privacy_body, depth=1))

    # Terms of Service
    terms_body = f'''
    <div class="border-b border-ink/10 bg-paper-warm/30 py-3 text-xs text-ink-muted">
      <div class="container flex items-center gap-2">
        <a href="{r('index.html')}" class="hover:text-forest">Home</a>
        <span>&rsaquo;</span>
        <span class="text-ink font-medium">Terms of Service</span>
      </div>
    </div>
    <section class="section bg-paper">
      <div class="container max-w-3xl space-y-6 text-xs sm:text-sm text-ink-soft leading-relaxed">
        <h1 class="text-3xl font-serif text-ink font-bold">Terms of Service</h1>
        <p class="text-ink-muted text-xs">Last updated: January 2026</p>
        <p>Welcome to the official website of GN Construction (GN Group of Companies).</p>
        <h3 class="text-lg font-serif font-bold text-ink pt-2">1. Informational Content</h3>
        <p>The project information, equipment capacities, and preliminary cost estimators on this website are provided for informational and preliminary planning purposes. Formal contract terms are governed solely by signed line-item agreements.</p>
        <h3 class="text-lg font-serif font-bold text-ink pt-2">2. Intellectual Property</h3>
        <p>All project photographs, descriptions, and corporate materials belonging to GN Construction and its project clients are protected by applicable intellectual property regulations.</p>
      </div>
    </section>
    '''
    write_page("terms/index.html", wrap_page("Terms of Service", "GN Construction Terms of Service", terms_body, depth=1))

# ==============================================================================
# 15. REDIRECTS FOR OLD FOLDERS
# ==============================================================================
def build_redirects():
    redirects = [
        ("why-arsa/index.html", "../why-gn/index.html", "Why GN Construction"),
        ("arsa-ai/index.html", "../gn-ai/index.html", "GN AI Assistant"),
        ("areas/index.html", "../projects/index.html", "GN Construction Projects in Pune"),
        ("areas/baramati.html", "../projects/index.html", "GN Construction Projects")
    ]
    for rel_f, target, title in redirects:
        r_html = f'''<!DOCTYPE html>
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
        write_page(rel_f, r_html)

if __name__ == "__main__":
    print("Building all GN Construction subpages...")
    build_services_index()
    build_service_details()
    build_projects_index()
    build_project_details()
    build_about_page()
    build_why_gn()
    build_clients_page()
    build_materials_page()
    build_methodology_page()
    build_tools_page()
    build_ai_page()
    build_contact_page()
    build_legal_pages()
    build_redirects()
    print("All subpages generated successfully!")
