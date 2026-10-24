#!/usr/bin/env python3
"""
GN Construction Website Builder
Generates a complete, authentic, multi-page website for GN Construction.
Replaces all traces of Arsa Homes with verified GN Construction information from PPT.
"""

import os
from pathlib import Path

# Base directory is current workspace
BASE_DIR = Path(r"C:\Users\nwabl\Downloads\Gn Construction website")

# Import verified GN data
from gn_data import (
    GN_BRAND, GN_ABOUT, GN_FOUNDERS, GN_ASSOCIATES, GN_CLIENTS,
    GN_PROJECTS, GN_ASSETS, GN_SERVICES
)

def rel_path(path_str, depth=0):
    """Adjust relative path based on directory depth."""
    if not path_str:
        return ""
    if path_str.startswith("http://") or path_str.startswith("https://") or path_str.startswith("tel:") or path_str.startswith("mailto:") or path_str.startswith("#"):
        return path_str
    prefix = "../" * depth
    clean = path_str.lstrip("/")
    return prefix + clean

def get_header_html(active_nav="", depth=0):
    r = lambda p: rel_path(p, depth)
    
    return f'''
  <!-- Top Utility Bar (Desktop Only) -->
  <div class="hidden lg:block overflow-hidden border-b border-ink/10 bg-paper-warm/50 py-2 text-[12px] text-ink-muted">
    <div class="container flex items-center justify-between gap-6">
      <div class="flex items-center gap-6">
        <span class="inline-flex items-center gap-1.5 font-medium text-ink-soft">
          <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-map-pin text-forest"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"></path><circle cx="12" cy="10" r="3"></circle></svg>
          Salisbury Park · Pune · Maharashtra
        </span>
        <a href="tel:{GN_BRAND['phone']}" class="hover:text-forest transition flex items-center gap-1.5" title="Direct Phone">
          <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-phone text-forest"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          {GN_BRAND['phone']}
        </a>
        <a href="mailto:{GN_BRAND['email']}" class="hover:text-forest transition flex items-center gap-1.5" title="Direct Email">
          <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-mail text-forest"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
          {GN_BRAND['email']}
        </a>
      </div>
      <div class="flex items-center gap-4 text-ink-muted">
        <span>Mon–Sat · 09:00–18:30</span>
        <span class="inline-flex items-center gap-1 rounded-full bg-forest/10 px-2.5 py-0.5 text-[11px] font-semibold text-forest">
          <svg xmlns="http://www.w3.org/2000/svg" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-sparkles"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
          Established 2013 · Pune
        </span>
      </div>
    </div>
  </div>

  <!-- Main Navigation Header -->
  <header class="sticky top-0 z-50 transition-all duration-300 bg-paper/95 backdrop-blur-md border-b border-ink/10">
    <div class="container flex items-center justify-between py-3.5">
      <!-- Logo -->
      <a href="{r('index.html')}" class="flex items-center gap-3 group" aria-label="GN Construction Home">
        <div class="w-10 h-10 rounded-lg bg-ink text-paper flex items-center justify-center font-bold font-serif text-xl tracking-tighter group-hover:bg-forest transition shadow-sm border border-gold/30">
          GN
        </div>
        <div class="flex flex-col leading-tight">
          <span class="font-bold text-lg text-ink font-serif tracking-tight group-hover:text-forest transition">GN CONSTRUCTION</span>
          <span class="text-[10px] uppercase font-semibold text-gold tracking-widest">Group of Companies</span>
        </div>
      </a>

      <!-- Desktop Nav Items -->
      <nav class="hidden lg:flex items-center gap-7 text-[14px] font-medium text-ink-soft" aria-label="Primary Navigation">
        <!-- Services Dropdown -->
        <div class="relative group nav-dropdown-group">
          <button type="button" class="flex items-center gap-1 hover:text-forest py-2 transition {'text-forest font-semibold' if active_nav == 'services' else ''}" aria-expanded="false" aria-haspopup="true">
            Services
            <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down opacity-60 transition group-hover:rotate-180"><path d="m6 9 6 6 6-6"></path></svg>
          </button>
          <div class="absolute left-0 top-full pt-2 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-200 z-50">
            <div class="w-[300px] bg-paper rounded-xl shadow-xl border border-ink/10 p-2.5 space-y-1">
              <a href="{r('services/index.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] font-semibold text-forest border-b border-ink/5">All Services Overview &rarr;</a>
              <a href="{r('services/civil-construction.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Civil & RCC Construction</a>
              <a href="{r('services/residential-construction.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Residential Building Construction</a>
              <a href="{r('services/commercial-construction.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Commercial Complex Construction</a>
              <a href="{r('services/turnkey-construction.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Turnkey Construction</a>
              <a href="{r('services/institutional-construction.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Institutional & Infra Projects</a>
              <a href="{r('services/development-works.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Development & Amenity Works</a>
            </div>
          </div>
        </div>

        <!-- Projects Dropdown -->
        <div class="relative group nav-dropdown-group">
          <button type="button" class="flex items-center gap-1 hover:text-forest py-2 transition {'text-forest font-semibold' if active_nav == 'projects' else ''}" aria-expanded="false" aria-haspopup="true">
            Projects
            <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down opacity-60 transition group-hover:rotate-180"><path d="m6 9 6 6 6-6"></path></svg>
          </button>
          <div class="absolute left-0 top-full pt-2 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-200 z-50">
            <div class="w-[340px] bg-paper rounded-xl shadow-xl border border-ink/10 p-2.5 space-y-1">
              <a href="{r('projects/index.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] font-semibold text-forest border-b border-ink/5">View All 7 Projects &rarr;</a>
              <a href="{r('projects/konark-business-centre.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">
                <span class="font-medium">Konark Business Centre</span>
                <span class="block text-[11px] text-ink-muted">Mundhwa · 26,000 sqft · Turnkey</span>
              </a>
              <a href="{r('projects/tanishka-jadhavar-college.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">
                <span class="font-medium">Jadhavar College Building</span>
                <span class="block text-[11px] text-ink-muted">Narhe · 85,000 sqft · Institutional</span>
              </a>
              <a href="{r('projects/godrej-greens-undri.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">
                <span class="font-medium">Godrej Greens</span>
                <span class="block text-[11px] text-ink-muted">Undri · Clubhouse, Pool & Retaining Wall</span>
              </a>
              <a href="{r('projects/kolte-patil-24k.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">
                <span class="font-medium">Kolte Patil 24K</span>
                <span class="block text-[11px] text-ink-muted">Wakad · Phytroid Wall & 13.7L Ltr Tank</span>
              </a>
              <a href="{r('projects/jade-regency-wagholi.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">
                <span class="font-medium">JADE Regency</span>
                <span class="block text-[11px] text-ink-muted">Wagholi · 30,000 sqft · Wadhwa Group</span>
              </a>
            </div>
          </div>
        </div>

        <a href="{r('clients/index.html')}" class="hover:text-forest transition {'text-forest font-semibold' if active_nav == 'clients' else ''}">Clients</a>

        <!-- About Dropdown -->
        <div class="relative group nav-dropdown-group">
          <button type="button" class="flex items-center gap-1 hover:text-forest py-2 transition {'text-forest font-semibold' if active_nav == 'about' else ''}" aria-expanded="false" aria-haspopup="true">
            About Us
            <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down opacity-60 transition group-hover:rotate-180"><path d="m6 9 6 6 6-6"></path></svg>
          </button>
          <div class="absolute left-0 top-full pt-2 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-200 z-50">
            <div class="w-[280px] bg-paper rounded-xl shadow-xl border border-ink/10 p-2.5 space-y-1">
              <a href="{r('about/index.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Company & Leadership</a>
              <a href="{r('why-gn/index.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Why GN Construction</a>
              <a href="{r('materials/index.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Machinery & Plant Assets</a>
              <a href="{r('methodology/index.html')}" class="block px-3 py-2 rounded-lg hover:bg-paper-warm text-[13px] text-ink hover:text-forest">Methodology & CQRA Standards</a>
            </div>
          </div>
        </div>

        <a href="{r('tools/index.html')}" class="hover:text-forest transition {'text-forest font-semibold' if active_nav == 'tools' else ''}">Estimator</a>
        <a href="{r('gn-ai/index.html')}" class="hover:text-forest transition flex items-center gap-1.5 {'text-forest font-semibold' if active_nav == 'ai' else ''}">
          <span class="w-2 h-2 rounded-full bg-forest animate-pulse"></span>
          GN AI
        </a>
        <a href="{r('contact/index.html')}" class="hover:text-forest transition {'text-forest font-semibold' if active_nav == 'contact' else ''}">Contact</a>
      </nav>

      <!-- Right Action Items -->
      <div class="flex items-center gap-3">
        <!-- Search Trigger Button -->
        <button type="button" class="p-2 rounded-lg hover:bg-paper-warm text-ink-muted hover:text-ink transition border border-transparent hover:border-ink/10" aria-label="Search the site">
          <svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-search"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.3-4.3"></path></svg>
        </button>

        <!-- CTA Button -->
        <a href="{r('contact/index.html')}" class="hidden sm:inline-flex btn-primary rounded-full px-5 py-2.5 text-[13.5px] font-semibold shadow-sm items-center gap-2">
          <span>Enquire Project</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
        </a>

        <!-- Mobile Menu Toggle Button -->
        <button type="button" class="lg:hidden p-2 rounded-lg hover:bg-paper-warm text-ink transition border border-ink/15" data-menu-toggle aria-label="Toggle Navigation Menu">
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-menu"><line x1="4" x2="20" y1="12" y2="12"></line><line x1="4" x2="20" y1="6" y2="6"></line><line x1="4" x2="20" y1="18" y2="18"></line></svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Backdrop -->
  <div id="mobile-drawer-backdrop" class="fixed inset-0 bg-black/60 z-[99] opacity-0 pointer-events-none transition-opacity duration-300"></div>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-drawer" class="fixed inset-y-0 right-0 w-[85vw] max-w-[340px] bg-paper z-[100] transform translate-x-full transition-transform duration-300 overflow-y-auto p-6 flex flex-col justify-between shadow-2xl">
    <div>
      <div class="flex items-center justify-between pb-5 border-b border-ink/10">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded bg-ink text-paper flex items-center justify-center font-bold font-serif text-sm">GN</div>
          <span class="font-bold text-sm text-ink font-serif tracking-tight">GN CONSTRUCTION</span>
        </div>
        <button type="button" class="p-1.5 rounded-lg hover:bg-paper-warm text-ink-muted hover:text-ink" data-menu-close aria-label="Close Menu">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-x"><path d="M18 6 6 18"></path><path d="m6 6 12 12"></path></svg>
        </button>
      </div>

      <nav class="py-5 space-y-3 text-[15px] font-medium text-ink">
        <a href="{r('index.html')}" class="block py-2 hover:text-forest">Home</a>
        <a href="{r('services/index.html')}" class="block py-2 hover:text-forest">Services</a>
        <a href="{r('projects/index.html')}" class="block py-2 hover:text-forest">Projects</a>
        <a href="{r('clients/index.html')}" class="block py-2 hover:text-forest">Clients</a>
        <a href="{r('about/index.html')}" class="block py-2 hover:text-forest">About Company</a>
        <a href="{r('why-gn/index.html')}" class="block py-2 hover:text-forest">Why GN Construction</a>
        <a href="{r('materials/index.html')}" class="block py-2 hover:text-forest">Plant & Machinery</a>
        <a href="{r('methodology/index.html')}" class="block py-2 hover:text-forest">Methodology & Quality</a>
        <a href="{r('tools/index.html')}" class="block py-2 hover:text-forest">Cost Estimator</a>
        <a href="{r('gn-ai/index.html')}" class="block py-2 hover:text-forest flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-forest animate-pulse"></span>
          GN AI Assistant
        </a>
        <a href="{r('contact/index.html')}" class="block py-2 hover:text-forest">Contact</a>
      </nav>
    </div>

    <div class="pt-6 border-t border-ink/10 text-xs text-ink-muted space-y-3">
      <div>
        <p class="font-semibold text-ink">Salisbury Park Office</p>
        <p>Sr. No. 585, Plot No. 88/90, Salisbury Park, Pune - 411038</p>
      </div>
      <p>Tel: {GN_BRAND['phone']}</p>
      <a href="{r('contact/index.html')}" class="btn-primary w-full justify-center rounded-lg py-2.5 text-xs">Enquire Now</a>
    </div>
  </div>
'''

def get_footer_html(depth=0):
    r = lambda p: rel_path(p, depth)
    return f'''
  <!-- Footer -->
  <footer class="bg-ink text-paper pt-16 pb-12 border-t border-paper/10">
    <div class="container">
      <!-- Footer Top CTA Banner -->
      <div class="bg-paper/5 border border-paper/10 rounded-2xl p-8 mb-14 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div>
          <span class="text-xs uppercase font-mono text-gold font-semibold tracking-wider">Start the conversation</span>
          <h3 class="text-2xl md:text-3xl font-serif text-paper mt-1">Ready to build your next landmark structure?</h3>
          <p class="text-sm text-paper/70 mt-1 max-w-xl">Consult with our directors and civil engineering team for turnkey proposals, civil execution tenders, and technical reviews.</p>
        </div>
        <a href="{r('contact/index.html')}" class="btn-gold rounded-full px-7 py-3 text-sm font-semibold shrink-0">
          Request Project Proposal
        </a>
      </div>

      <!-- Main Footer Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-12 border-b border-paper/10 text-sm">
        <!-- Brand Column -->
        <div class="lg:col-span-2 space-y-4">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-lg bg-paper text-ink flex items-center justify-center font-bold font-serif text-xl">
              GN
            </div>
            <div>
              <p class="font-bold text-lg text-paper font-serif tracking-tight">GN CONSTRUCTION</p>
              <p class="text-xs uppercase tracking-widest text-gold font-semibold">GN Group of Companies</p>
            </div>
          </div>
          <p class="text-paper/70 text-sm leading-relaxed max-w-sm">
            Reliable and efficient civil and building construction in Pune. Directed by seasoned civil engineers with 25+ years of execution excellence.
          </p>
          <div class="text-xs text-paper/60 space-y-1.5 pt-2">
            <p><strong class="text-paper">Registered Address:</strong> Sr. No. 585, Plot No. 88/90, Salisbury Park, Pune - 411038</p>
            <p><strong class="text-paper">Associates:</strong> GN Construction · GN Infra Project · Prisha Enterprises</p>
            <p><strong class="text-paper">Established:</strong> 2013</p>
            <p><strong class="text-paper">Phone:</strong> {GN_BRAND['phone']} | <strong class="text-paper">Email:</strong> {GN_BRAND['email']}</p>
          </div>
        </div>

        <!-- Services Links -->
        <div class="space-y-3">
          <p class="font-serif text-base font-semibold text-paper">Services</p>
          <ul class="space-y-2 text-paper/70 text-xs">
            <li><a href="{r('services/civil-construction.html')}" class="hover:text-gold transition">Civil & RCC Construction</a></li>
            <li><a href="{r('services/residential-construction.html')}" class="hover:text-gold transition">Residential Buildings</a></li>
            <li><a href="{r('services/commercial-construction.html')}" class="hover:text-gold transition">Commercial Complexes</a></li>
            <li><a href="{r('services/turnkey-construction.html')}" class="hover:text-gold transition">Turnkey Execution</a></li>
            <li><a href="{r('services/institutional-construction.html')}" class="hover:text-gold transition">Institutional Projects</a></li>
            <li><a href="{r('services/development-works.html')}" class="hover:text-gold transition">Development & Amenities</a></li>
          </ul>
        </div>

        <!-- Featured Projects Links -->
        <div class="space-y-3">
          <p class="font-serif text-base font-semibold text-paper">Key Projects</p>
          <ul class="space-y-2 text-paper/70 text-xs">
            <li><a href="{r('projects/konark-business-centre.html')}" class="hover:text-gold transition">Konark Business Centre</a></li>
            <li><a href="{r('projects/tanishka-jadhavar-college.html')}" class="hover:text-gold transition">Jadhavar College Building</a></li>
            <li><a href="{r('projects/godrej-greens-undri.html')}" class="hover:text-gold transition">Godrej Greens Undri</a></li>
            <li><a href="{r('projects/kolte-patil-24k.html')}" class="hover:text-gold transition">Kolte Patil 24K Wakad</a></li>
            <li><a href="{r('projects/jade-regency-wagholi.html')}" class="hover:text-gold transition">JADE Regency Wagholi</a></li>
            <li><a href="{r('projects/amba-prestige-point.html')}" class="hover:text-gold transition">Prestige Point Bajirao Rd</a></li>
            <li><a href="{r('projects/konark-virtue-tower4.html')}" class="hover:text-gold transition">Konark Virtue Tower 4</a></li>
          </ul>
        </div>

        <!-- Company & Tools Links -->
        <div class="space-y-3">
          <p class="font-serif text-base font-semibold text-paper">Company</p>
          <ul class="space-y-2 text-paper/70 text-xs">
            <li><a href="{r('about/index.html')}" class="hover:text-gold transition">About & Founders</a></li>
            <li><a href="{r('why-gn/index.html')}" class="hover:text-gold transition">Why Choose GN</a></li>
            <li><a href="{r('clients/index.html')}" class="hover:text-gold transition">Clients & Developers</a></li>
            <li><a href="{r('materials/index.html')}" class="hover:text-gold transition">Machinery & Assets</a></li>
            <li><a href="{r('methodology/index.html')}" class="hover:text-gold transition">CQRA Quality Standards</a></li>
            <li><a href="{r('tools/index.html')}" class="hover:text-gold transition">Cost Estimator</a></li>
            <li><a href="{r('gn-ai/index.html')}" class="hover:text-gold transition">GN AI Assistant</a></li>
            <li><a href="{r('contact/index.html')}" class="hover:text-gold transition">Salisbury Park Office</a></li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-paper/50">
        <p>&copy; 2026 GN Construction (GN Group of Companies). All rights reserved.</p>
        <div class="flex items-center gap-6">
          <a href="{r('privacy-policy/index.html')}" class="hover:text-paper transition">Privacy Policy</a>
          <a href="{r('terms/index.html')}" class="hover:text-paper transition">Terms of Service</a>
          <span>Pune, Maharashtra</span>
        </div>
      </div>
    </div>
  </footer>

  <!-- Floating WhatsApp Action -->
  <a href="https://wa.me/919876543210?text=Hello%20GN%20Construction,%20I%20would%20like%20to%20enquire%20about%20a%20project." target="_blank" rel="noopener noreferrer" class="fixed bottom-6 right-6 z-40 bg-[#25D366] text-white p-3.5 rounded-full shadow-xl hover:scale-110 active:scale-95 transition-all duration-200 flex items-center justify-center" aria-label="WhatsApp GN Construction">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-message-circle"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"></path></svg>
  </a>

  <!-- Search Modal Backdrop -->
  <div id="search-modal-backdrop" class="fixed inset-0 bg-black/60 z-[110] opacity-0 pointer-events-none transition-opacity duration-200 flex items-start justify-center pt-20 px-4">
    <div class="bg-paper rounded-2xl shadow-2xl border border-ink/15 w-full max-w-xl overflow-hidden transform scale-95 transition-all duration-200">
      <div class="p-4 border-b border-ink/10 flex items-center gap-3">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-search text-ink-muted"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.3-4.3"></path></svg>
        <input type="text" id="search-input" placeholder="Search GN projects, services, equipment, or areas..." class="w-full bg-transparent border-0 focus:outline-none text-sm text-ink placeholder-ink-muted/70">
        <button type="button" id="search-close-btn" class="p-1 rounded text-ink-muted hover:text-ink text-xs font-mono">ESC</button>
      </div>
      <div id="search-results" class="max-h-[360px] overflow-y-auto p-3 space-y-1 text-xs">
        <!-- Results rendered by js/main.js -->
      </div>
    </div>
  </div>
'''

def wrap_page(title, description, body_content, active_nav="", depth=0):
    r = lambda p: rel_path(p, depth)
    header = get_header_html(active_nav, depth)
    footer = get_footer_html(depth)
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | GN Construction</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="{r('css/style.css')}">
  <meta property="og:title" content="{title} | GN Construction">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏢</text></svg>">
</head>
<body class="bg-paper text-ink font-sans antialiased selection:bg-forest selection:text-paper">
  {header}

  <main>
    {body_content}
  </main>

  {footer}

  <script src="{r('js/main.js')}"></script>
</body>
</html>
'''

print("Header, footer, and page wrapper functions defined.")
