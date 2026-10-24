import re

with open('arsahomes_original.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace local @font-face with Google Fonts @import
css = re.sub(r'@font-face\s*\{[^}]*BricolageGrotesque[^}]*\}', '', css)
css = re.sub(r'@font-face\s*\{[^}]*Figtree-Variable[^}]*\}', '', css)

font_import = """@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700&family=Figtree:ital,wght@0,300..900;1,300..900&display=swap');
"""

# Custom root variables as requested
custom_root = """
:root {
  --paper: #FAF6EE;
  --paper-warm: #F5F0E6;
  --paper-deep: #EEE5D2;
  --ink: #1F2A22;
  --ink-soft: #4A5C4E;
  --ink-muted: #7A8C7E;
  --forest: #0F8A5B;
  --forest-deep: #0A6644;
  --forest-dark: #072E1E;
  --forest-mist: #E1EFE5;
  --gold: #C99E06;
  --gold-light: #D4AE2A;
  --gold-dark: #9A7804;
  --gold-deep: #9A7804;
  --copper: #B0703C;
  --moss: #5E6D60;
  
  --font-display: 'Bricolage Grotesque', Georgia, serif;
  --font-sans: 'Figtree', system-ui, -apple-system, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, monospace;
  
  --arsa-safe: env(safe-area-inset-bottom, 0px);
  --arsa-nav-h: 64px;
  --z-base: 0;
  --z-scrim: 39;
  --z-rail: 40;
  --z-sheet: 45;
  --z-panel: 50;
  --z-search: 90;
  --z-gate: 100;
}
"""

additional_styles = """
/* === Additional Interactive & Animation Styles === */

/* Ken Burns slow zoom */
@keyframes kenburns-slow {
  0% { transform: scale(1); }
  50% { transform: scale(1.08) translate(-1%, -1%); }
  100% { transform: scale(1); }
}
.kenburns-slow {
  animation: kenburns-slow 35s ease-in-out infinite alternate;
}

/* Aurora Blobs */
@keyframes aurora-float-1 {
  0%, 100% { transform: translate(0px, 0px) scale(1); }
  50% { transform: translate(40px, -30px) scale(1.15); }
}
@keyframes aurora-float-2 {
  0%, 100% { transform: translate(0px, 0px) scale(1.1); }
  50% { transform: translate(-35px, 25px) scale(0.95); }
}
@keyframes aurora-float-3 {
  0%, 100% { transform: translate(0px, 0px) scale(1); }
  50% { transform: translate(25px, 35px) scale(1.2); }
}

.aurora-blob-1 {
  animation: aurora-float-1 18s ease-in-out infinite;
}
.aurora-blob-2 {
  animation: aurora-float-2 22s ease-in-out infinite;
}
.aurora-blob-3 {
  animation: aurora-float-3 26s ease-in-out infinite;
}

/* Dots Grid Background */
.bg-dots-grid {
  background-image: radial-gradient(rgba(250, 246, 238, 0.12) 1.2px, transparent 1.2px);
  background-size: 28px 28px;
}

/* Marquee Animation */
@keyframes marquee-scroll {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}
.animate-marquee-track {
  display: flex;
  width: max-content;
  animation: marquee-scroll 45s linear infinite;
}
.animate-marquee-track:hover {
  animation-play-state: paused;
}

/* Corner bracket decorations */
.corner-bracket {
  position: absolute;
  width: 14px;
  height: 14px;
  border-color: rgba(201, 158, 6, 0.45);
  pointer-events: none;
}
.corner-bracket-tl { top: 16px; left: 16px; border-top: 1.5px solid; border-left: 1.5px solid; }
.corner-bracket-tr { top: 16px; right: 16px; border-top: 1.5px solid; border-right: 1.5px solid; }
.corner-bracket-bl { bottom: 16px; left: 16px; border-bottom: 1.5px solid; border-left: 1.5px solid; }
.corner-bracket-br { bottom: 16px; right: 16px; border-bottom: 1.5px solid; border-right: 1.5px solid; }

/* 3D Tilt Card */
.tilt-card {
  transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.25s ease;
  transform-style: preserve-3d;
  will-change: transform;
}

/* Scroll reveal */
.reveal-item {
  opacity: 0;
  transform: translateY(22px);
  transition: opacity 0.75s cubic-bezier(0.16, 1, 0.3, 1), transform 0.75s cubic-bezier(0.16, 1, 0.3, 1);
}
.reveal-item.is-revealed {
  opacity: 1;
  transform: translateY(0);
}

/* Dropdown Menu Styles */
.nav-dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  min-width: 280px;
  background: #FAF6EE;
  border: 1px solid rgba(31, 42, 34, 0.12);
  border-radius: 1.25rem;
  padding: 0.75rem;
  box-shadow: 0 20px 40px -15px rgba(31, 42, 34, 0.18);
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: opacity 0.25s ease, transform 0.25s ease, visibility 0.25s;
  z-index: 60;
}
.nav-dropdown-group:hover .nav-dropdown-menu,
.nav-dropdown-group:focus-within .nav-dropdown-menu,
.nav-dropdown-menu.is-active {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

/* Search Modal */
.search-modal-backdrop {
  position: fixed;
  inset: 0;
  background-color: rgba(15, 22, 18, 0.65);
  backdrop-filter: blur(8px);
  z-index: 100;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.25s ease, visibility 0.25s;
}
.search-modal-backdrop.is-open {
  opacity: 1;
  visibility: visible;
}
.search-modal-content {
  opacity: 0;
  transform: translateY(16px) scale(0.98);
  transition: opacity 0.25s ease, transform 0.25s ease;
}
.search-modal-backdrop.is-open .search-modal-content {
  opacity: 1;
  transform: translateY(0) scale(1);
}

/* Mobile Menu Drawer */
.mobile-drawer-backdrop {
  position: fixed;
  inset: 0;
  background-color: rgba(15, 22, 18, 0.6);
  backdrop-filter: blur(4px);
  z-index: 80;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s;
}
.mobile-drawer-backdrop.is-open {
  opacity: 1;
  visibility: visible;
}
.mobile-drawer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  max-width: 360px;
  background-color: #FAF6EE;
  z-index: 90;
  transform: translateX(100%);
  transition: transform 0.35s cubic-bezier(0.32, 0.72, 0, 1);
  box-shadow: -10px 0 30px rgba(0,0,0,0.15);
  display: flex;
  flex-direction: column;
}
.mobile-drawer.is-open {
  transform: translateX(0);
}

/* WhatsApp Floating Button */
.whatsapp-floating {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 45;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;
}
.whatsapp-floating:hover {
  transform: scale(1.08) translateY(-2px);
}
.whatsapp-tooltip {
  position: absolute;
  right: calc(100% + 12px);
  top: 50%;
  transform: translateY(-50%) translateX(6px);
  background: #1F2A22;
  color: #FAF6EE;
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 12px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s ease, transform 0.2s ease;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.whatsapp-floating:hover .whatsapp-tooltip {
  opacity: 1;
  transform: translateY(-50%) translateX(0);
}

/* FAQ Details Smooth Transition */
details summary::-webkit-details-marker {
  display: none;
}
details[open] summary svg {
  transform: rotate(90deg);
}
details summary svg {
  transition: transform 0.25s cubic-bezier(0.32, 0.72, 0, 1);
}

/* Header sticky scrolled class */
header.is-scrolled {
  box-shadow: 0 10px 30px -10px rgba(31, 42, 34, 0.08);
  background-color: rgba(250, 246, 238, 0.94);
  backdrop-filter: blur(12px);
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
::-webkit-scrollbar-track {
  background: #FAF6EE;
}
::-webkit-scrollbar-thumb {
  background: #CBD5CE;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #A3B5A6;
}
"""

final_css = font_import + custom_root + css + additional_styles

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(final_css)

print("Created css/style.css successfully! Size:", len(final_css))
