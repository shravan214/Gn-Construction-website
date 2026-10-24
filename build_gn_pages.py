#!/usr/bin/env python3
"""
GN Construction - Complete HTML Page Generator
Builds authentic, clean HTML pages for GN Construction.
"""

import os
from pathlib import Path
from generate_gn_website import wrap_page, rel_path
from gn_data import (
    GN_BRAND, GN_ABOUT, GN_FOUNDERS, GN_ASSOCIATES, GN_CLIENTS,
    GN_PROJECTS, GN_ASSETS, GN_SERVICES
)

BASE_DIR = Path(r"C:\Users\nwabl\Downloads\Gn Construction website")

# ==============================================================================
# 1. HOMEPAGE (index.html)
# ==============================================================================
def generate_homepage():
    r = lambda p: rel_path(p, 0)
    
    # Marquee items
    marquee_clients = " &nbsp;&bull;&nbsp; ".join([f"<span class='text-forest font-semibold'>{c}</span>" for c in GN_CLIENTS])
    
    body = f'''
    <!-- Hero Section -->
    <section class="relative min-h-[90vh] flex items-center bg-ink text-paper overflow-hidden py-20">
      <!-- Background Image with Gradient Overlay -->
      <div class="absolute inset-0 z-0">
        <img src="{r('images/projects/jade-regency-wagholi.jpg')}" alt="GN Construction Project" class="w-full h-full object-cover opacity-25 scale-105 transition-transform duration-1000 ease-out" id="hero-bg-img">
        <div class="absolute inset-0 bg-gradient-to-r from-ink via-ink/90 to-ink/60"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-ink via-transparent to-transparent"></div>
      </div>

      <div class="container relative z-10">
        <div class="max-w-3xl space-y-6">
          <div class="inline-flex items-center gap-2 rounded-full border border-gold/40 bg-gold/10 px-4 py-1.5 text-xs font-semibold text-gold tracking-wide">
            <span class="w-2 h-2 rounded-full bg-gold animate-pulse"></span>
            GN Group of Companies &bull; Founded 2013 &bull; Salisbury Park, Pune
          </div>

          <h1 class="text-3xl sm:text-5xl lg:text-6xl font-serif text-paper leading-[1.15] tracking-tight">
            Engineering-Led Civil, Residential &amp; Commercial Construction.
          </h1>

          <p class="text-base sm:text-lg text-paper/80 font-normal leading-relaxed max-w-2xl">
           Established in 2013, GN Construction undertakes residential, commercial and institutional construction projects. From turnkey commercial buildings to residential developments, we believe in honest work, quality construction and taking responsibility for every project we undertake.
          </p>

          <div class="flex flex-wrap items-center gap-4 pt-2">
            <a href="{r('projects/index.html')}" class="btn-gold rounded-full px-7 py-3.5 text-sm font-semibold shadow-lg hover:scale-105 transition-transform flex items-center gap-2">
              <span>View Executed Projects</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
            <a href="{r('contact/index.html')}" class="btn-ghost text-paper border-paper/30 hover:bg-paper/10 rounded-full px-7 py-3.5 text-sm font-semibold transition flex items-center gap-2">
              <span>Request Project Proposal</span>
            </a>
          </div>

          <!-- Quick Stats Row -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-6 pt-10 border-t border-paper/15 text-paper">
            <div>
              <p class="font-serif text-3xl font-bold text-gold">12+</p>
              <p class="text-xs text-paper/70 uppercase tracking-wider mt-0.5 font-medium">Years in Industry</p>
              <p class="text-[11px] text-paper/50">Founded in 2013</p>
            </div>
            <div>
              <p class="font-serif text-3xl font-bold text-gold">7+</p>
              <p class="text-xs text-paper/70 uppercase tracking-wider mt-0.5 font-medium">Landmark Builds</p>
              <p class="text-[11px] text-paper/50">Commercial &amp; Residential</p>
            </div>
            <div>
              <p class="font-serif text-3xl font-bold text-gold">15+</p>
              <p class="text-xs text-paper/70 uppercase tracking-wider mt-0.5 font-medium">Developer Clients</p>
              <p class="text-[11px] text-paper/50">Godrej, Kolte Patil, Karia</p>
            </div>
            <div>
              <p class="font-serif text-3xl font-bold text-gold">100%</p>
              <p class="text-xs text-paper/70 uppercase tracking-wider mt-0.5 font-medium">Quality Compliance</p>
              <p class="text-[11px] text-paper/50">CQRA Monitored Execution</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Developer Clients Marquee Ticker -->
    <section class="border-y border-ink/10 bg-paper-warm py-4 overflow-hidden">
      <div class="container flex items-center gap-6">
        <span class="text-xs uppercase tracking-widest font-mono text-ink-muted shrink-0 font-bold border-r border-ink/15 pr-6 hidden sm:inline-block">
          Trusted By
        </span>
        <div class="overflow-hidden whitespace-nowrap w-full">
          <div class="inline-block animate-marquee-slow text-sm text-ink-soft">
            {marquee_clients} &nbsp;&bull;&nbsp; {marquee_clients}
          </div>
        </div>
      </div>
    </section>

    <!-- Company Trust & Mission Section -->
    <section class="section bg-paper">
      <div class="container">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <!-- Left Column: Story & Philosophy -->
          <div class="lg:col-span-7 space-y-6">
            <span class="eyebrow text-forest">About GN Group</span>
            <h2 class="text-3xl sm:text-4xl font-serif text-ink tracking-tight">
              Founded by Engineers. Driven by Quality, Honesty &amp; Hard Work.
            </h2>
            <p class="text-base text-ink-soft leading-relaxed">
              {GN_ABOUT['intro']}
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-5 pt-2">
              <div class="p-5 rounded-xl bg-forest/5 border border-forest/15 space-y-2">
                <span class="text-xs uppercase font-mono font-bold text-forest tracking-wider">Our Mission</span>
                <p class="text-xs text-ink-soft leading-relaxed italic">
                  "{GN_ABOUT['mission']}"
                </p>
              </div>
              <div class="p-5 rounded-xl bg-gold/10 border border-gold/25 space-y-2">
                <span class="text-xs uppercase font-mono font-bold text-gold-deep tracking-wider">Our Goal</span>
                <p class="text-xs text-ink-soft leading-relaxed italic">
                  "{GN_ABOUT['goal']}"
                </p>
              </div>
            </div>

            <div class="pt-2 flex items-center gap-6 text-xs text-ink-muted">
              <span><strong>Group Associates:</strong> GN Construction, GN Infra Project, Prisha Enterprises</span>
            </div>
          </div>

          <!-- Right Column: Metric Grid Cards -->
          <div class="lg:col-span-5 grid grid-cols-2 gap-4">
            <div class="p-6 rounded-2xl bg-paper-warm border border-ink/10 text-center space-y-1 hover:border-forest/40 transition">
              <p class="text-3xl sm:text-4xl font-serif font-bold text-forest">25</p>
              <p class="text-xs font-semibold text-ink uppercase tracking-wider">Years Experience</p>
              <p class="text-[11px] text-ink-muted">Founder Civil Leadership</p>
            </div>
            <div class="p-6 rounded-2xl bg-paper-warm border border-ink/10 text-center space-y-1 hover:border-gold/40 transition">
              <p class="text-3xl sm:text-4xl font-serif font-bold text-gold">15+</p>
              <p class="text-xs font-semibold text-ink uppercase tracking-wider">Pune &amp; Mumbai Clients</p>
              <p class="text-[11px] text-ink-muted">Established Developers</p>
            </div>
            <div class="p-6 rounded-2xl bg-paper-warm border border-ink/10 text-center space-y-1 hover:border-forest/40 transition">
              <p class="text-3xl sm:text-4xl font-serif font-bold text-forest">6,000</p>
              <p class="text-xs font-semibold text-ink uppercase tracking-wider">Shuttering Props</p>
              <p class="text-[11px] text-ink-muted">Owned Machinery Assets</p>
            </div>
            <div class="p-6 rounded-2xl bg-paper-warm border border-ink/10 text-center space-y-1 hover:border-gold/40 transition">
              <p class="text-3xl sm:text-4xl font-serif font-bold text-gold">CQRA</p>
              <p class="text-xs font-semibold text-ink uppercase tracking-wider">Quality Audits</p>
              <p class="text-[11px] text-ink-muted">Software Managed Sites</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Grid Section -->
    <section class="section bg-paper-warm/40 border-t border-ink/10" id="services">
      <div class="container space-y-10">
        <div class="max-w-2xl space-y-3">
          <span class="eyebrow text-forest">Our Core Disciplines</span>
          <h2 class="text-3xl sm:text-4xl font-serif text-ink tracking-tight">
            Specialized Civil &amp; Building Construction Solutions.
          </h2>
          <p class="text-sm sm:text-base text-ink-soft">
            Every project runs on verified engineering principles: qualified B.E. Civil site supervisors, owned heavy shuttering systems, and disciplined milestone execution.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- 6 Service Cards -->
          <div class="bg-paper rounded-2xl p-7 border border-ink/10 shadow-sm hover:shadow-md hover:border-forest/40 transition-all flex flex-col justify-between group tilt-card">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-xl bg-forest/10 text-forest flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-building-2"><path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"></path><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"></path><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"></path><path d="M10 6h4"></path><path d="M10 10h4"></path><path d="M10 14h4"></path><path d="M10 18h4"></path></svg>
              </div>
              <span class="inline-block text-[11px] font-semibold uppercase tracking-wider text-forest font-mono">Structural RCC</span>
              <h3 class="text-xl font-serif text-ink group-hover:text-forest transition">Civil Construction</h3>
              <p class="text-xs text-ink-soft leading-relaxed">
                Complete RCC framed civil construction for residential, commercial, and institutional projects — from excavation and foundation to multi-storey slabs.
              </p>
            </div>
            <a href="{r('services/civil-construction.html')}" class="mt-6 inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
              <span>Read Scope Brief</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
          </div>

          <div class="bg-paper rounded-2xl p-7 border border-ink/10 shadow-sm hover:shadow-md hover:border-forest/40 transition-all flex flex-col justify-between group tilt-card">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-xl bg-gold/15 text-gold-deep flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-home"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
              </div>
              <span class="inline-block text-[11px] font-semibold uppercase tracking-wider text-gold-deep font-mono">Multi-Storey &amp; Villas</span>
              <h3 class="text-xl font-serif text-ink group-hover:text-forest transition">Residential Buildings</h3>
              <p class="text-xs text-ink-soft leading-relaxed">
                High-rise towers, multi-family apartment walk-ups, and luxury residential projects executed with developer-grade safety and precision shuttering.
              </p>
            </div>
            <a href="{r('services/residential-construction.html')}" class="mt-6 inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
              <span>Read Scope Brief</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
          </div>

          <div class="bg-paper rounded-2xl p-7 border border-ink/10 shadow-sm hover:shadow-md hover:border-forest/40 transition-all flex flex-col justify-between group tilt-card">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-xl bg-forest/10 text-forest flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-briefcase"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
              </div>
              <span class="inline-block text-[11px] font-semibold uppercase tracking-wider text-forest font-mono">Corporate &amp; Retail</span>
              <h3 class="text-xl font-serif text-ink group-hover:text-forest transition">Commercial Complexes</h3>
              <p class="text-xs text-ink-soft leading-relaxed">
                Construction of commercial centres and corporate business hubs with high-traffic circulation, basements, and modern exterior facades.
              </p>
            </div>
            <a href="{r('services/commercial-construction.html')}" class="mt-6 inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
              <span>Read Scope Brief</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
          </div>

          <div class="bg-paper rounded-2xl p-7 border border-ink/10 shadow-sm hover:shadow-md hover:border-forest/40 transition-all flex flex-col justify-between group tilt-card">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-xl bg-gold/15 text-gold-deep flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-key"><circle cx="7.5" cy="15.5" r="5.5"></circle><path d="m21 2-9.6 9.6"></path><path d="m15.5 7.5 3 3L22 7l-3-3"></path></svg>
              </div>
              <span class="inline-block text-[11px] font-semibold uppercase tracking-wider text-gold-deep font-mono">Single Contract</span>
              <h3 class="text-xl font-serif text-ink group-hover:text-forest transition">Turnkey Construction</h3>
              <p class="text-xs text-ink-soft leading-relaxed">
                End-to-end responsibility from site excavation and RCC framing to electrical, plumbing, finishing, and key handover under one line-item contract.
              </p>
            </div>
            <a href="{r('services/turnkey-construction.html')}" class="mt-6 inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
              <span>Read Scope Brief</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
          </div>

          <div class="bg-paper rounded-2xl p-7 border border-ink/10 shadow-sm hover:shadow-md hover:border-forest/40 transition-all flex flex-col justify-between group tilt-card">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-xl bg-forest/10 text-forest flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-graduation-cap"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
              </div>
              <span class="inline-block text-[11px] font-semibold uppercase tracking-wider text-forest font-mono">Scale &amp; Precision</span>
              <h3 class="text-xl font-serif text-ink group-hover:text-forest transition">Institutional &amp; Infra</h3>
              <p class="text-xs text-ink-soft leading-relaxed">
                Campuses, educational buildings, colleges (up to 85,000 sqft), and civil infrastructure like Phytroid walls and massive underground water tanks.
              </p>
            </div>
            <a href="{r('services/institutional-construction.html')}" class="mt-6 inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
              <span>Read Scope Brief</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
          </div>

          <div class="bg-paper rounded-2xl p-7 border border-ink/10 shadow-sm hover:shadow-md hover:border-forest/40 transition-all flex flex-col justify-between group tilt-card">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-xl bg-gold/15 text-gold-deep flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-waves"><path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"></path><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"></path><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"></path></svg>
              </div>
              <span class="inline-block text-[11px] font-semibold uppercase tracking-wider text-gold-deep font-mono">Amenities &amp; Landscape</span>
              <h3 class="text-xl font-serif text-ink group-hover:text-forest transition">Development &amp; Amenities</h3>
              <p class="text-xs text-ink-soft leading-relaxed">
                Clubhouses, swimming pools, multipurpose community halls, retaining walls, podium developments, and boundary infrastructures.
              </p>
            </div>
            <a href="{r('services/development-works.html')}" class="mt-6 inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
              <span>Read Scope Brief</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Projects Showcase Section -->
    <section class="section bg-paper" id="projects">
      <div class="container space-y-10">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-6">
          <div class="max-w-2xl space-y-3">
            <span class="eyebrow text-forest">Executed Portfolio</span>
            <h2 class="text-3xl sm:text-4xl font-serif text-ink tracking-tight">
              Landmark Structures Across Pune.
            </h2>
            <p class="text-sm sm:text-base text-ink-soft">
              Real projects delivered for prominent developers and institutions, verified with actual site documentation.
            </p>
          </div>
          <a href="{r('projects/index.html')}" class="btn-primary rounded-full px-6 py-2.5 text-xs font-semibold shrink-0">
            <span>View All 7 Projects</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-up-right"><path d="M7 7h10v10"></path><path d="m7 17 17-7"></path></svg>
          </a>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <!-- Project 1: Konark Business Centre -->
          <div class="group rounded-2xl overflow-hidden border border-ink/10 bg-paper-warm/40 hover:border-forest/40 transition shadow-sm flex flex-col justify-between">
            <div>
              <div class="relative h-64 sm:h-72 overflow-hidden bg-ink/10">
                <img src="{r('images/projects/konark-business-centre-turnkey.jpg')}" alt="Konark Business Centre" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <span class="absolute top-4 left-4 bg-ink/80 text-paper text-[10px] font-mono uppercase font-semibold px-2.5 py-1 rounded-full backdrop-blur">
                  Turnkey Commercial &bull; 26,000 sqft
                </span>
                <span class="absolute bottom-4 right-4 bg-forest text-paper text-[11px] font-semibold px-3 py-1 rounded-full shadow">
                  Turnkey Commercial
                </span>
              </div>
              <div class="p-6 space-y-3">
                <p class="text-xs font-semibold text-gold font-mono uppercase">Client: Karia Properties &bull; Keshav Nagar, Mundhwa</p>
                <h3 class="text-2xl font-serif text-ink group-hover:text-forest transition">Konark Business Centre (KBC)</h3>
                <p class="text-xs text-ink-soft leading-relaxed">
                  Turnkey construction of Basement + Ground + 3 upper floors. Full structural RCC framework, civil masonry, external facades, and complete commercial finishing.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="{r('projects/konark-business-centre.html')}" class="inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
                <span>View Full Project Case Study</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
              </a>
            </div>
          </div>

          <!-- Project 2: Jadhavar College Building -->
          <div class="group rounded-2xl overflow-hidden border border-ink/10 bg-paper-warm/40 hover:border-forest/40 transition shadow-sm flex flex-col justify-between">
            <div>
              <div class="relative h-64 sm:h-72 overflow-hidden bg-ink/10">
                <img src="{r('images/projects/tanishka-jadhavar-college-narhe.jpg')}" alt="Jadhavar College Building Narhe" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <span class="absolute top-4 left-4 bg-ink/80 text-paper text-[10px] font-mono uppercase font-semibold px-2.5 py-1 rounded-full backdrop-blur">
                  Institutional &bull; 85,000 sqft
                </span>
                <span class="absolute bottom-4 right-4 bg-forest text-paper text-[11px] font-semibold px-3 py-1 rounded-full shadow">
                  Institutional Campus
                </span>
              </div>
              <div class="p-6 space-y-3">
                <p class="text-xs font-semibold text-gold font-mono uppercase">Client: Tanishka Reality &bull; Narhe, Pune</p>
                <h3 class="text-2xl font-serif text-ink group-hover:text-forest transition">Jadhavar College Building</h3>
                <p class="text-xs text-ink-soft leading-relaxed">
                  Massive 85,000 sqft educational campus building executed with heavy cuplock shuttering and structured RCC slabs to support institutional live loads.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="{r('projects/tanishka-jadhavar-college.html')}" class="inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
                <span>View Full Project Case Study</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
              </a>
            </div>
          </div>

          <!-- Project 3: Godrej Greens Undri -->
          <div class="group rounded-2xl overflow-hidden border border-ink/10 bg-paper-warm/40 hover:border-forest/40 transition shadow-sm flex flex-col justify-between">
            <div>
              <div class="relative h-64 sm:h-72 overflow-hidden bg-ink/10">
                <img src="{r('images/projects/godrej-greens-undri-clubhouse.jpg')}" alt="Godrej Greens Undri Clubhouse" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <span class="absolute top-4 left-4 bg-ink/80 text-paper text-[10px] font-mono uppercase font-semibold px-2.5 py-1 rounded-full backdrop-blur">
                  Amenity &amp; Development Works
                </span>
                <span class="absolute bottom-4 right-4 bg-gold-deep text-paper text-[11px] font-semibold px-3 py-1 rounded-full shadow">
                  Godrej Properties
                </span>
              </div>
              <div class="p-6 space-y-3">
                <p class="text-xs font-semibold text-gold font-mono uppercase">Client: Dream World Landmark LLP (Godrej Properties) &bull; Undri</p>
                <h3 class="text-2xl font-serif text-ink group-hover:text-forest transition">Godrej Greens — Club House &amp; Amenities</h3>
                <p class="text-xs text-ink-soft leading-relaxed">
                  Construction of modern Club House, Swimming Pool, Multipurpose Community Hall, and reinforced earth retaining wall infrastructure.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="{r('projects/godrej-greens-undri.html')}" class="inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
                <span>View Full Project Case Study</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
              </a>
            </div>
          </div>

          <!-- Project 4: Kolte Patil 24K Wakad -->
          <div class="group rounded-2xl overflow-hidden border border-ink/10 bg-paper-warm/40 hover:border-forest/40 transition shadow-sm flex flex-col justify-between">
            <div>
              <div class="relative h-64 sm:h-72 overflow-hidden bg-ink/10">
                <img src="{r('images/projects/kolte-patil-24k-wakad.jpg')}" alt="Kolte Patil 24K Wakad Phytroid Wall" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <span class="absolute top-4 left-4 bg-ink/80 text-paper text-[10px] font-mono uppercase font-semibold px-2.5 py-1 rounded-full backdrop-blur">
                  Specialized Infrastructure
                </span>
                <span class="absolute bottom-4 right-4 bg-forest text-paper text-[11px] font-semibold px-3 py-1 rounded-full shadow">
                  13.7 Lakh Litre UGWT
                </span>
              </div>
              <div class="p-6 space-y-3">
                <p class="text-xs font-semibold text-gold font-mono uppercase">Client: Kolte Patil Developers &bull; Wakad, Pune</p>
                <h3 class="text-2xl font-serif text-ink group-hover:text-forest transition">Kolte Patil 24K — Phytroid Wall &amp; UGWT</h3>
                <p class="text-xs text-ink-soft leading-relaxed">
                  Specialized civil infrastructure work comprising a precision Phytroid wall and an underground water reservoir tank with 13.7 Lakh litre water capacity.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="{r('projects/kolte-patil-24k.html')}" class="inline-flex items-center gap-1.5 text-xs font-semibold text-forest hover:text-forest-deep transition">
                <span>View Full Project Case Study</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Owned Plant, Machinery & Assets Section -->
    <section class="section bg-paper-warm/40 border-t border-ink/10">
      <div class="container space-y-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          <div class="lg:col-span-6 space-y-5">
            <span class="eyebrow text-forest">Owned Capital Assets</span>
            <h2 class="text-3xl sm:text-4xl font-serif text-ink tracking-tight">
              Equipped to Execute at Scale Without Subcontractor Delays.
            </h2>
            <p class="text-sm text-ink-soft leading-relaxed">
              Unlike brokers or under-resourced contractors, GN Construction owns extensive heavy shuttering materials, batching equipment, and lifting machinery. This ensures our sites maintain unbroken casting schedules.
            </p>

            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 pt-2 text-xs">
              <div class="p-3.5 rounded-xl bg-paper border border-ink/10">
                <p class="font-bold text-forest text-lg font-serif">6,000</p>
                <p class="text-ink font-medium">Props</p>
                <p class="text-[10px] text-ink-muted">Shuttering support</p>
              </div>
              <div class="p-3.5 rounded-xl bg-paper border border-ink/10">
                <p class="font-bold text-forest text-lg font-serif">1,600</p>
                <p class="text-ink font-medium">Spans</p>
                <p class="text-[10px] text-ink-muted">Slab staging system</p>
              </div>
              <div class="p-3.5 rounded-xl bg-paper border border-ink/10">
                <p class="font-bold text-forest text-lg font-serif">8,000</p>
                <p class="text-ink font-medium">Sqft Cuplock</p>
                <p class="text-[10px] text-ink-muted">Heavy scaffolding</p>
              </div>
              <div class="p-3.5 rounded-xl bg-paper border border-ink/10">
                <p class="font-bold text-forest text-lg font-serif">3,000</p>
                <p class="text-ink font-medium">Shikanja</p>
                <p class="text-[10px] text-ink-muted">Column formwork</p>
              </div>
              <div class="p-3.5 rounded-xl bg-paper border border-ink/10">
                <p class="font-bold text-forest text-lg font-serif">400</p>
                <p class="text-ink font-medium">H-Frame Sets</p>
                <p class="text-[10px] text-ink-muted">High-reach towers</p>
              </div>
              <div class="p-3.5 rounded-xl bg-paper border border-ink/10">
                <p class="font-bold text-forest text-lg font-serif">9</p>
                <p class="text-ink font-medium">Vibrators</p>
                <p class="text-[10px] text-ink-muted">Electric &amp; Petrol</p>
              </div>
            </div>

            <div class="pt-2">
              <a href="{r('materials/index.html')}" class="btn-primary rounded-full px-6 py-2.5 text-xs font-semibold">
                <span>View Full Equipment Inventory &rarr;</span>
              </a>
            </div>
          </div>

          <div class="lg:col-span-6">
            <div class="rounded-2xl overflow-hidden border border-ink/15 shadow-xl bg-paper">
              <img src="{r('images/places/gn-construction-equipment-machinery.jpg')}" alt="GN Construction Equipment and Cuplock Shuttering System" class="w-full h-auto object-cover max-h-[460px]">
              <div class="p-4 bg-paper border-t border-ink/10 flex items-center justify-between text-xs text-ink-muted">
                <span>GN Construction Yard &amp; Site Plant</span>
                <span class="text-forest font-semibold">Self-Owned Fleet</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Leadership & Engineering Team Section -->
    <section class="section bg-paper">
      <div class="container space-y-12">
        <div class="max-w-2xl space-y-3">
          <span class="eyebrow text-forest">Directors &amp; Leadership</span>
          <h2 class="text-3xl sm:text-4xl font-serif text-ink tracking-tight">
            Qualified Civil Engineers on Every Project.
          </h2>
          <p class="text-sm sm:text-base text-ink-soft">
            GN Construction is led by credentialed civil engineers who take direct technical responsibility for structural safety and site milestones.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <!-- Founder 1 -->
          <div class="p-8 rounded-2xl bg-paper-warm/50 border border-ink/10 space-y-4 hover:border-forest/40 transition">
            <div class="flex items-center gap-4">
              <div class="w-14 h-14 rounded-full bg-forest text-paper flex items-center justify-center font-serif text-xl font-bold">
                NW
              </div>
              <div>
                <h3 class="text-xl font-serif font-bold text-ink">{GN_FOUNDERS[0]['name']}</h3>
                <p class="text-xs font-semibold text-gold font-mono uppercase">{GN_FOUNDERS[0]['role']} &bull; {GN_FOUNDERS[0]['qualification']}</p>
              </div>
            </div>
            <p class="text-xs text-ink-soft leading-relaxed">
              {GN_FOUNDERS[0]['experience']} Instrumental in guiding technical execution, developer liaising, and structural oversight across all GN Group undertakings.
            </p>
          </div>

          <!-- Founder 2 -->
          <div class="p-8 rounded-2xl bg-paper-warm/50 border border-ink/10 space-y-4 hover:border-forest/40 transition">
            <div class="flex items-center gap-4">
              <div class="w-14 h-14 rounded-full bg-ink text-paper flex items-center justify-center font-serif text-xl font-bold">
                HH
              </div>
              <div>
                <h3 class="text-xl font-serif font-bold text-ink">{GN_FOUNDERS[1]['name']}</h3>
                <p class="text-xs font-semibold text-gold font-mono uppercase">{GN_FOUNDERS[1]['role']} &bull; {GN_FOUNDERS[1]['qualification']}</p>
              </div>
            </div>
            <p class="text-xs text-ink-soft leading-relaxed">
              {GN_FOUNDERS[1]['experience']} Specialises in site operational efficiency, CQRA quality implementation, concrete batching oversight, and project handover.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- GN AI Assistant Interactive Section -->
    <section class="section bg-paper-warm/40 border-t border-ink/10" id="gn-ai">
      <div class="container">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
          <div class="lg:col-span-5 space-y-4">
            <div class="inline-flex items-center gap-2 rounded-full bg-forest/10 px-3 py-1 text-xs font-semibold text-forest">
              <span class="w-2 h-2 rounded-full bg-forest animate-pulse"></span>
              GN AI &bull; Construction Knowledge
            </div>
            <h2 class="text-3xl sm:text-4xl font-serif text-ink tracking-tight">
              Ask Anything About Our Projects &amp; Civil Engineering.
            </h2>
            <p class="text-sm text-ink-soft leading-relaxed">
              Trained on GN Construction's verified project credentials, equipment assets, shuttering capacity, and Pune municipal engineering requirements.
            </p>

            <div class="space-y-2 pt-2">
              <p class="text-xs font-bold text-ink uppercase tracking-wider">Example queries to try:</p>
              <div class="flex flex-wrap gap-2">
                <button type="button" class="text-xs bg-paper px-3 py-1.5 rounded-lg border border-ink/10 text-ink hover:border-forest hover:text-forest transition text-left" onclick="askAi('What projects has GN Construction done with Karia Properties?')">Karia Properties projects?</button>
                <button type="button" class="text-xs bg-paper px-3 py-1.5 rounded-lg border border-ink/10 text-ink hover:border-forest hover:text-forest transition text-left" onclick="askAi('What is the experience of the founders?')">Founder credentials?</button>
                <button type="button" class="text-xs bg-paper px-3 py-1.5 rounded-lg border border-ink/10 text-ink hover:border-forest hover:text-forest transition text-left" onclick="askAi('What equipment and props does GN Construction own?')">Owned shuttering equipment?</button>
                <button type="button" class="text-xs bg-paper px-3 py-1.5 rounded-lg border border-ink/10 text-ink hover:border-forest hover:text-forest transition text-left" onclick="askAi('What was the work done at Godrej Greens Undri?')">Godrej Greens scope?</button>
              </div>
            </div>
          </div>

          <!-- Chat Console -->
          <div class="lg:col-span-7">
            <div class="rounded-2xl bg-ink text-paper border border-ink shadow-xl overflow-hidden flex flex-col h-[420px]">
              <div class="p-4 bg-ink border-b border-paper/10 flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-forest to-gold flex items-center justify-center font-bold text-xs text-paper">
                    GN
                  </div>
                  <div>
                    <p class="font-serif text-sm font-semibold text-paper">GN Technical Civil Assistant</p>
                    <p class="text-[10px] text-paper/60">Live &bull; Pune Civil &amp; Commercial Knowledge</p>
                  </div>
                </div>
                <span class="text-[10px] font-mono text-gold uppercase px-2 py-0.5 rounded bg-gold/10">Interactive</span>
              </div>

              <!-- Message History -->
              <div id="ai-chat-messages" class="flex-1 p-4 overflow-y-auto space-y-3 text-xs leading-relaxed" aria-label="GN AI conversation">
                <div class="flex items-start gap-2.5">
                  <div class="w-6 h-6 rounded-full bg-forest text-paper flex items-center justify-center text-[10px] shrink-0 font-bold">GN</div>
                  <div class="bg-paper/10 p-3 rounded-2xl rounded-tl-sm max-w-[85%] text-paper/90">
                    Hello! I am GN Construction's engineering assistant. Ask me anything about our 12+ years of civil construction, our landmark projects (Konark Business Centre, Jadhavar College, Godrej Greens), or our owned shuttering assets and equipment.
                  </div>
                </div>
              </div>

              <!-- Chat Input Bar -->
              <form id="ai-chat-form" class="p-3 bg-ink/90 border-t border-paper/10 flex items-center gap-2" onsubmit="event.preventDefault(); submitAiMessage();">
                <input type="text" id="ai-chat-input" placeholder="Type your construction question..." class="flex-1 bg-paper/10 border border-paper/15 rounded-xl px-3.5 py-2 text-xs text-paper placeholder-paper/40 focus:outline-none focus:border-gold">
                <button type="submit" class="bg-forest text-paper p-2 rounded-xl hover:bg-forest-deep transition">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-send"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Accordion Section -->
    <section class="section bg-paper">
      <div class="container max-w-4xl space-y-10">
        <div class="text-center space-y-3">
          <span class="eyebrow text-forest">Frequently Asked Questions</span>
          <h2 class="text-3xl sm:text-4xl font-serif text-ink tracking-tight">
            Clear Answers for Developers &amp; Project Promoters.
          </h2>
        </div>

        <div class="space-y-4">
          <details class="faq-item group p-5 rounded-2xl bg-paper-warm/40 border border-ink/10 cursor-pointer">
            <summary class="flex items-center justify-between font-serif text-lg text-ink font-semibold list-none">
              <span>What types of projects does GN Construction undertake?</span>
              <span class="text-forest transition-transform group-open:rotate-180">&darr;</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-ink-soft leading-relaxed border-t border-ink/10 pt-3">
              GN Construction undertakes civil and structural RCC construction, turnkey commercial complexes (such as Konark Business Centre), multi-storey residential buildings (such as JADE Regency and Konark Virtue Tower 4), institutional campuses (such as Jadhavar College, 85,000 sqft), and development works including clubhouses, pools, and retaining walls (such as Godrej Greens).
            </p>
          </details>

          <details class="faq-item group p-5 rounded-2xl bg-paper-warm/40 border border-ink/10 cursor-pointer">
            <summary class="flex items-center justify-between font-serif text-lg text-ink font-semibold list-none">
              <span>How does GN Construction ensure structural quality and compliance?</span>
              <span class="text-forest transition-transform group-open:rotate-180">&darr;</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-ink-soft leading-relaxed border-t border-ink/10 pt-3">
              Our projects are managed directly by degree civil engineers (B.E. Civil &amp; D.C.E.). For developer projects like Konark Virtue, we integrate third-party quality management software platforms like CQRA to log reinforcement inspection, cube compressive strength tests, and staging clearances at every pour.
            </p>
          </details>

          <details class="faq-item group p-5 rounded-2xl bg-paper-warm/40 border border-ink/10 cursor-pointer">
            <summary class="flex items-center justify-between font-serif text-lg text-ink font-semibold list-none">
              <span>Does GN Construction own its own shuttering and machinery?</span>
              <span class="text-forest transition-transform group-open:rotate-180">&darr;</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-ink-soft leading-relaxed border-t border-ink/10 pt-3">
              Yes. We own 6,000 props, 1,600 spans, 8,000 sqft of cuplock scaffolding, 600 tie-rod weller sets, 3,000 shikanjas, 400 H-frames, concrete mixers (1-bag and 3-bag), weigh batchers, lift machines, and 9 electric/petrol vibrators. This eliminates dependence on third-party shuttering vendors.
            </p>
          </details>

          <details class="faq-item group p-5 rounded-2xl bg-paper-warm/40 border border-ink/10 cursor-pointer">
            <summary class="flex items-center justify-between font-serif text-lg text-ink font-semibold list-none">
              <span>What is the leadership background of GN Construction?</span>
              <span class="text-forest transition-transform group-open:rotate-180">&darr;</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-ink-soft leading-relaxed border-t border-ink/10 pt-3">
              GN Construction was founded in 2013 by Mr. Nitin Wable (B.E. Civil, 25 years of construction experience) and Mr. Hermeetsingh Hoda (B.E. Civil, 14 years of construction experience). Together, they bring almost four decades of civil engineering leadership.
            </p>
          </details>

          <details class="faq-item group p-5 rounded-2xl bg-paper-warm/40 border border-ink/10 cursor-pointer">
            <summary class="flex items-center justify-between font-serif text-lg text-ink font-semibold list-none">
              <span>Where is GN Construction headquartered and where do you operate?</span>
              <span class="text-forest transition-transform group-open:rotate-180">&darr;</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-ink-soft leading-relaxed border-t border-ink/10 pt-3">
              We are headquartered at Salisbury Park, Pune (Sr. No. 585, Plot No. 88/90, Salisbury Park, Pune - 411038). We execute projects throughout the Pune metropolitan region, including Keshav Nagar, Mundhwa, Narhe, Wagholi, Bajirao Road, Undri, Wakad, and beyond.
            </p>
          </details>
        </div>
      </div>
    </section>

    <!-- Bottom Contact & Proposal CTA Section -->
    <section class="section bg-ink text-paper border-t border-paper/10" id="contact">
      <div class="container">
        <div class="max-w-3xl mx-auto text-center space-y-6">
          <span class="eyebrow text-gold">Ready to build?</span>
          <h2 class="text-3xl sm:text-5xl font-serif text-paper tracking-tight">
            Consult With Our Civil Engineering Directors.
          </h2>
          <p class="text-sm sm:text-base text-paper/70 leading-relaxed">
            Whether you have a turnkey commercial parcel, an institutional building, or a multi-storey residential development, our directors will review your drawings and provide an authentic technical proposal.
          </p>

          <div class="pt-4 flex flex-wrap justify-center items-center gap-4">
            <a href="{r('contact/index.html')}" class="btn-gold rounded-full px-8 py-3.5 text-sm font-semibold shadow-lg">
              Submit Tender / Enquiry
            </a>
            <a href="tel:{GN_BRAND['phone']}" class="btn-ghost text-paper border-paper/30 hover:bg-paper/10 rounded-full px-8 py-3.5 text-sm font-semibold">
              Call: {GN_BRAND['phone']}
            </a>
          </div>

          <div class="pt-8 text-xs text-paper/50">
            <p>Office: Sr. No. 585, Plot No. 88/90, Salisbury Park, Pune - 411038</p>
          </div>
        </div>
      </div>
    </section>
    '''
    
    html = wrap_page("Building Excellence Since 2013 | Civil & Commercial Construction in Pune", 
                     "GN Construction is a premier Pune civil engineering and building construction company founded in 2013. Commercial complexes, residential high-rises, institutional campuses, and turnkey projects.", 
                     body, active_nav="home", depth=0)
    
    out_file = BASE_DIR / "index.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated: index.html")

if __name__ == "__main__":
    generate_homepage()
