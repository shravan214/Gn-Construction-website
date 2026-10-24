/**
 * GN Construction - Main Interactive JavaScript
 * High-performance interactive components, search modal, and GN AI assistant.
 */

document.addEventListener('DOMContentLoaded', () => {
 initStickyHeader();
 initMobileMenu();
 initDropdowns();
 initTiltCards();
 initScrollReveal();
 initFaqAccordion();
 initSearchModal();
 initGNAI();
});

/* ==========================================================================
  1. Sticky Header
  ========================================================================== */
function initStickyHeader() {
 const header = document.querySelector('header');
 if (!header) return;

 const handleScroll = () => {
  if (window.scrollY > 30) {
   header.classList.add('shadow-md', 'bg-paper/98');
   header.classList.remove('bg-paper/95');
  } else {
   header.classList.remove('shadow-md', 'bg-paper/98');
   header.classList.add('bg-paper/95');
  }
 };

 window.addEventListener('scroll', handleScroll, { passive: true });
 handleScroll();
}

/* ==========================================================================
  2. Mobile Menu Drawer
  ========================================================================== */
function initMobileMenu() {
 const menuButtons = document.querySelectorAll('[data-menu-toggle]');
 const drawerBackdrop = document.querySelector('#mobile-drawer-backdrop');
 const drawer = document.querySelector('#mobile-drawer');
 const closeButtons = document.querySelectorAll('[data-menu-close]');

 function setMenuState(isOpen) {
  if (!drawer || !drawerBackdrop) return;

  drawerBackdrop.classList.toggle('opacity-100', isOpen);
  drawerBackdrop.classList.toggle('opacity-0', !isOpen);
  drawerBackdrop.classList.toggle('pointer-events-none', !isOpen);
  drawerBackdrop.style.opacity = isOpen ? '1' : '0';
  drawerBackdrop.style.visibility = isOpen ? 'visible' : 'hidden';
  drawerBackdrop.style.pointerEvents = isOpen ? 'auto' : 'none';

  drawer.classList.toggle('translate-x-0', isOpen);
  drawer.classList.toggle('translate-x-full', !isOpen);
  drawer.classList.toggle('pointer-events-none', !isOpen);
  drawer.classList.toggle('invisible', !isOpen);
  drawer.classList.toggle('opacity-0', !isOpen);
  drawer.classList.toggle('opacity-100', isOpen);

  drawer.style.display = isOpen ? 'flex' : 'none';
  drawer.style.transform = isOpen ? 'translateX(0)' : 'translateX(100%)';
  drawer.style.visibility = isOpen ? 'visible' : 'hidden';
  drawer.style.opacity = isOpen ? '1' : '0';
  drawer.style.pointerEvents = isOpen ? 'auto' : 'none';
  drawer.setAttribute('aria-hidden', String(!isOpen));

  document.body.style.overflow = isOpen ? 'hidden' : '';
  document.body.classList.toggle('overflow-hidden', isOpen);
  menuButtons.forEach(btn => btn.setAttribute('aria-expanded', String(isOpen)));
 }

 function openMenu() {
  setMenuState(true);
 }

 function closeMenu() {
  setMenuState(false);
 }

 closeMenu();

 menuButtons.forEach(btn => {
  btn.addEventListener('click', (e) => {
   e.preventDefault();
   const isOpen = drawer && drawer.getAttribute('aria-hidden') === 'false';
   if (isOpen) {
    closeMenu();
   } else {
    openMenu();
   }
  });
 });

 closeButtons.forEach(btn => {
  btn.addEventListener('click', closeMenu);
 });

 if (drawerBackdrop) {
  drawerBackdrop.addEventListener('click', (e) => {
   if (e.target === drawerBackdrop) closeMenu();
  });
 }

 document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && drawer && !drawer.classList.contains('translate-x-full')) {
   closeMenu();
  }
 });
}

/* ==========================================================================
  3. Navigation Dropdowns
  ========================================================================== */
function initDropdowns() {
 const dropdownGroups = document.querySelectorAll('.nav-dropdown-group');

 dropdownGroups.forEach(group => {
  const trigger = group.querySelector('button');
  const menu = group.querySelector('.absolute');
  if (!trigger || !menu) return;

  // Accessibility
  trigger.addEventListener('focus', () => {
   menu.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-2');
   menu.classList.add('opacity-100', 'pointer-events-auto', 'translate-y-0');
  });

  group.addEventListener('mouseleave', () => {
   menu.classList.add('opacity-0', 'pointer-events-none', 'translate-y-2');
   menu.classList.remove('opacity-100', 'pointer-events-auto', 'translate-y-0');
  });
 });
}

/* ==========================================================================
  4. 3D Tilt Cards Effect
  ========================================================================== */
function initTiltCards() {
 const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
 if (isTouchDevice) return;

 const tiltCards = document.querySelectorAll('.tilt-card');
 tiltCards.forEach(card => {
  const mouseMoveHandler = (e) => {
   const rect = card.getBoundingClientRect();
   const x = e.clientX - rect.left;
   const y = e.clientY - rect.top;
   const centerX = rect.width / 2;
   const centerY = rect.height / 2;
   const rotateX = ((y - centerY) / centerY) * -4;
   const rotateY = ((x - centerX) / centerX) * 4;

   card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.01, 1.01, 1.01)`;
  };

  const mouseLeaveHandler = () => {
   card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
   card.style.transition = 'transform 0.4s ease-out';
  };

  const mouseEnterHandler = () => {
   card.style.transition = 'transform 0.1s ease-out';
  };

  card.addEventListener('mouseenter', mouseEnterHandler);
  card.addEventListener('mousemove', mouseMoveHandler);
  card.addEventListener('mouseleave', mouseLeaveHandler);
 });
}

/* ==========================================================================
  5. Scroll Reveal with IntersectionObserver
  ========================================================================== */
function initScrollReveal() {
 const revealElements = document.querySelectorAll('.reveal-item, [data-reveal]');
 if (!revealElements.length) return;

 if (!('IntersectionObserver' in window)) {
  revealElements.forEach(el => el.classList.add('is-revealed'));
  return;
 }

 const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
   if (entry.isIntersecting) {
    entry.target.classList.add('is-revealed');
    entry.target.style.opacity = '1';
    entry.target.style.transform = 'translateY(0)';
    observer.unobserve(entry.target);
   }
  });
 }, { rootMargin: '0px 0px -40px 0px', threshold: 0.1 });

 revealElements.forEach(el => observer.observe(el));
}

/* ==========================================================================
  6. FAQ Accordion
  ========================================================================== */
function initFaqAccordion() {
 const detailsList = document.querySelectorAll('details.faq-item');
 detailsList.forEach(detail => {
  const summary = detail.querySelector('summary');
  if (!summary) return;

  summary.addEventListener('click', () => {
   detailsList.forEach(other => {
    if (other !== detail && other.open) {
     other.removeAttribute('open');
    }
   });
  });
 });
}

/* ==========================================================================
  7. Search Modal (⌘K / Ctrl+K)
  ========================================================================== */
const searchableItems = [
 // Services
 { title: "Civil & RCC Construction", category: "Services", desc: "Complete RCC framing, excavations, and slab staging.", url: "services/civil-construction.html" },
 { title: "Residential Building Construction", category: "Services", desc: "Multi-storey high-rise towers, apartments, and villas.", url: "services/residential-construction.html" },
 { title: "Commercial Complex Construction", category: "Services", desc: "Turnkey commercial complexes and corporate business hubs.", url: "services/commercial-construction.html" },
 { title: "Turnkey Construction", category: "Services", desc: "Single contract responsibility from excavation to handover.", url: "services/turnkey-construction.html" },
 { title: "Institutional & Infra Projects", category: "Services", desc: "Educational campuses and colleges up to 85,000 sqft.", url: "services/institutional-construction.html" },
 { title: "Development & Amenity Works", category: "Services", desc: "Clubhouses, swimming pools, and retaining walls.", url: "services/development-works.html" },
 
 // Projects
 { title: "Konark Business Centre (KBC)", category: "Projects", desc: "Keshav Nagar, Mundhwa &bull; 26,000 sqft turnkey commercial &bull; ", url: "projects/konark-business-centre.html" },
 { title: "Jadhavar College Building", category: "Projects", desc: "Narhe, Pune &bull; 85,000 sqft institutional campus &bull; ", url: "projects/tanishka-jadhavar-college.html" },
 { title: "Godrej Greens Undri", category: "Projects", desc: "Clubhouse, swimming pool & retaining wall for Godrej Properties.", url: "projects/godrej-greens-undri.html" },
 { title: "Kolte Patil 24K Wakad", category: "Projects", desc: "Phytroid wall and underground water tank (UGWT).", url: "projects/kolte-patil-24k-wakad.html" },
 { title: "JADE Regency Wagholi", category: "Projects", desc: "30,000 sqft residential building for Wadhwa Group.", url: "projects/jade-regency-wagholi.html" },
 { title: "Prestige Point Bajirao Road", category: "Projects", desc: "68,000 sqft commercial complex for Amba Group", url: "projects/amba-prestige-point.html" },
 { title: "Konark Virtue Tower 4", category: "Projects", desc: "High-rise structural RCC managed on CQRA quality platform.", url: "projects/konark-virtue-t4.html" },

 // Company & Leadership
 { title: "Company Founders & Leadership", category: "About", desc: "Mr. Nitin Wable (25 yrs) & Mr. Hermeetsingh Hoda (14 yrs) &bull; B.E. Civil", url: "about/index.html" },
 { title: "Developer Client Partners", category: "Clients", desc: "Godrej Properties, Kolte Patil, Karia Properties, Wadhwa Group, Amba Group.", url: "clients/index.html" },
 ];

function initSearchModal() {
 const searchButtons = document.querySelectorAll('[aria-label="Search the site"]');
 const modalBackdrop = document.querySelector('#search-modal-backdrop');
 const searchInput = document.querySelector('#search-input');
 const searchResults = document.querySelector('#search-results');
 const closeBtn = document.querySelector('#search-close-btn');

 if (!modalBackdrop || !searchInput) return;

 function openSearch() {
  modalBackdrop.classList.remove('opacity-0', 'pointer-events-none');
  modalBackdrop.classList.add('opacity-100');
  const modal = modalBackdrop.querySelector('div');
  if (modal) modal.classList.remove('scale-95');
  document.body.style.overflow = 'hidden';
  setTimeout(() => {
   searchInput.value = '';
   searchInput.focus();
   renderResults('');
  }, 50);
 }

 function closeSearch() {
  modalBackdrop.classList.add('opacity-0', 'pointer-events-none');
  modalBackdrop.classList.remove('opacity-100');
  const modal = modalBackdrop.querySelector('div');
  if (modal) modal.classList.add('scale-95');
  document.body.style.overflow = '';
 }

 searchButtons.forEach(btn => {
  btn.addEventListener('click', (e) => {
   e.preventDefault();
   openSearch();
  });
 });

 if (closeBtn) closeBtn.addEventListener('click', closeSearch);

 modalBackdrop.addEventListener('click', (e) => {
  if (e.target === modalBackdrop) closeSearch();
 });

 document.addEventListener('keydown', (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
   e.preventDefault();
   if (!modalBackdrop.classList.contains('pointer-events-none')) {
    closeSearch();
   } else {
    openSearch();
   }
  }
  if (e.key === 'Escape' && !modalBackdrop.classList.contains('pointer-events-none')) {
   closeSearch();
  }
 });

 searchInput.addEventListener('input', (e) => {
  renderResults(e.target.value.trim());
 });

 function renderResults(query) {
  if (!searchResults) return;

  let filtered = searchableItems;
  if (query) {
   const q = query.toLowerCase();
   filtered = searchableItems.filter(item => 
    item.title.toLowerCase().includes(q) ||
    item.desc.toLowerCase().includes(q) ||
    item.category.toLowerCase().includes(q)
   );
  }

  if (filtered.length === 0) {
   searchResults.innerHTML = `
    <div class="p-6 text-center text-ink-muted">
     <p class="text-sm">No results found for "${query}"</p>
     <p class="text-xs mt-1 text-ink-soft">Try searching for "turnkey", "karia", "godrej", "props", or "salisbury"</p>
    </div>
   `;
   return;
  }

  // Determine current path depth to format links correctly
  const isSubdir = window.location.pathname.includes('/services/') || 
           window.location.pathname.includes('/projects/') || 
           window.location.pathname.includes('/about/') || 
           window.location.pathname.includes('/clients/') || 
           window.location.pathname.includes('/materials/') || 
           window.location.pathname.includes('/methodology/') || 
           window.location.pathname.includes('/tools/') || 
           window.location.pathname.includes('/gn-ai/') || 
           window.location.pathname.includes('/contact/') || 
           window.location.pathname.includes('/why-gn/');

  const prefix = isSubdir ? '../' : '';

  searchResults.innerHTML = filtered.map(item => `
   <a href="${prefix + item.url}" class="flex items-center justify-between p-3 rounded-xl hover:bg-paper-warm transition border border-transparent hover:border-ink/10 group">
    <div class="min-w-0 pr-3">
     <div class="flex items-center gap-2">
      <span class="text-[10px] uppercase font-mono px-2 py-0.5 rounded-full bg-forest/10 text-forest font-semibold">${item.category}</span>
      <span class="text-sm font-medium text-ink group-hover:text-forest transition">${item.title}</span>
     </div>
     <p class="text-xs text-ink-soft mt-1 truncate">${item.desc}</p>
    </div>
    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-up-right text-ink-muted group-hover:text-forest transition shrink-0"><path d="M7 7h10v10"></path><path d="m7 17 17-7"></path></svg>
   </a>
  `).join('');
 }
}

/* ==========================================================================
  8. GN AI Technical Assistant (Interactive)
  ========================================================================== */
const gnKnowledge = [
 {
  triggers: ["residential building construction cost", "residential construction cost", "per sqft cost", "cost per sqft", "construction cost per sqft", "house construction cost", "building cost per square foot", "cost of residential building", "residential building rate", "residential sqft rate", "rate per sqft residential"],
  answer: "For a general public estimate, residential building construction in India often falls in the range of **₹1,800 to ₹4,500 per sq ft**, depending on city, soil, structural system, finish level, and design complexity.\n\n• **Standard finish:** around **₹1,800–₹2,800 / sq ft**\n• **Premium finish:** around **₹3,000–₹4,500+ / sq ft**\n\nFor a more accurate budget, the key factors are plot location, number of floors, structural design, labor cost, materials, and the final finishing specification."
 },
 {
  triggers: ["what does gn construction do", "services", "what do you do", "scope", "civil", "commercial", "project"],
  answer: "GN Construction provides general civil execution services within residential, commercial, and institutional project delivery, including RCC framing, structural execution, site supervision, project coordination, and turnkey execution support.\n\nThis is general public information and may vary by site, project scope, and local conditions."
 },
 {
  triggers: ["founder", "director", "nitin", "wable", "hoda", "hermeetsingh", "leadership", "qualification", "experience", "team", "engineer"],
  answer: "GN Construction is a civil contractor focused on project execution, engineering supervision, and delivery across residential, commercial, and institutional builds.\n\nThis is general public information and may vary by project, team structure, and local requirements."
 },
 {
  triggers: ["karia", "konark", "kbc", "mundhwa", "turnkey", "keshav nagar", "godrej", "undri", "greens", "clubhouse", "swimming pool", "retaining wall", "tanishka", "jadhavar", "college", "narhe", "institutional", "kolte", "patil", "24k", "wakad", "water tank", "ugwt", "phytroid"],
  answer: "GN Construction has worked across residential, commercial, and institutional project scopes, including turnkey execution, amenity works, RCC structural package delivery, and specialized infrastructure elements such as retaining walls and underground tanks.\n\nThis is general public information and may vary by site, schedule, and local building conditions."
 },
 {
  triggers: ["equipment", "shuttering", "props", "machinery", "asset", "spans", "cuplock", "mixer", "materials", "concrete", "steel"],
  answer: "GN Construction can discuss standard site execution practices, equipment planning, concrete work, reinforcement detailing, shuttering, and quality checks.\n\nThis is general public information and may vary by project, site conditions, and equipment availability."
 },
 {
  triggers: ["company", "finance", "private", "confidential", "sensitive", "official", "records", "general info"],
  answer: "I can answer general questions about construction practices, regulations, permits, project planning, and public industry information.\n\nThis is general public information and may vary by project type, site conditions, and local rules."
 },
 {
  triggers: ["cqra", "quality", "cube", "audit", "strength", "standard", "permit", "rera", "government", "maharashtra", "news", "latest", "internet", "general", "public", "industry"],
  answer: "I can provide general public information about construction practices, municipal and government rules, quality checks, and industry news from reliable public sources.\n\nThis is general public information and may vary by municipal norms, material availability, and site conditions."
 },
 {
  triggers: ["office", "address", "location", "salisbury", "phone", "email", "contact", "call", "whatsapp"],
  answer: "You can contact GN Construction at:\n\n📞 **Phone:** +91 9527660870\n✉️ **Email:** gnconstruction2016@gmail.com\n\nFor project discussions, share your requirement, site location, or drawings and we can respond with a relevant project discussion.\n\nThis is general public information and may vary by project scope and discussion requirements."
 }
];

function initGNAI() {
 const chatMessages = document.querySelector('#ai-chat-messages');
 const chatInput = document.querySelector('#ai-chat-input');
 const chatForm = document.querySelector('#ai-chat-form');

 if (!chatMessages) return;

 window.askAi = function(query) {
  if (chatInput) chatInput.value = query;
  window.submitAiMessage();
 };

 window.submitAiMessage = function() {
  if (!chatInput) return;
  const query = chatInput.value.trim();
  if (!query) return;

  // Add user message
  appendChatMessage(query, 'user');
  chatInput.value = '';

  // Show typing indicator
  const typingId = showTyping();

  setTimeout(() => {
   removeTyping(typingId);
   const answer = getAnswer(query);
   appendChatMessage(answer, 'ai');
  }, 450);
 };

 function appendChatMessage(text, sender) {
  const msgDiv = document.createElement('div');
  msgDiv.className = `flex ${sender === 'user' ? 'justify-end' : 'items-start gap-2.5 sm:gap-3'}`;

  if (sender === 'user') {
   msgDiv.innerHTML = `
    <div class="max-w-[85%] rounded-2xl px-4 py-2.5 text-xs bg-forest text-paper rounded-br-sm shadow">
     <p class="whitespace-pre-wrap">${escapeHTML(text)}</p>
    </div>
   `;
  } else {
   const formatted = formatMarkdown(text);
   msgDiv.innerHTML = `
    <div class="w-6 h-6 sm:w-7 sm:h-7 rounded-full bg-forest text-paper flex items-center justify-center text-[10px] shrink-0 font-bold">GN</div>
    <div class="bg-paper/10 p-3 sm:p-4 rounded-2xl rounded-tl-sm max-w-[85%] text-paper/90 text-xs leading-relaxed border border-paper/10 space-y-1.5">
     ${formatted}
    </div>
   `;
  }

  chatMessages.appendChild(msgDiv);
  chatMessages.scrollTo({ top: chatMessages.scrollHeight, behavior: 'smooth' });
 }

 function showTyping() {
  const id = 'typing-' + Date.now();
  const div = document.createElement('div');
  div.id = id;
  div.className = 'flex items-start gap-2.5';
  div.innerHTML = `
   <div class="w-6 h-6 rounded-full bg-forest text-paper flex items-center justify-center text-[10px] shrink-0 font-bold">GN</div>
   <div class="p-3 rounded-2xl text-[11px] bg-paper/10 text-gold flex items-center gap-2 border border-paper/10">
    <span class="w-1.5 h-1.5 rounded-full bg-gold animate-ping"></span>
    <span>GN Engineering AI is analyzing verified project records...</span>
   </div>
  `;
  chatMessages.appendChild(div);
  chatMessages.scrollTo({ top: chatMessages.scrollHeight, behavior: 'smooth' });
  return id;
 }

 function removeTyping(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
 }

 function getAnswer(query) {
  const qLower = query.toLowerCase();

  const costRelated = ["cost", "budget", "rate", "sqft", "per sqft", "price", "estimator"]; 
  const buildingRelated = ["residential", "house", "villa", "apartment", "building", "construction"]; 

  if (costRelated.some(k => qLower.includes(k)) && buildingRelated.some(k => qLower.includes(k))) {
   return "For a general public estimate, residential building construction in India often falls in the range of **₹1,800 to ₹4,500 per sq ft**, depending on city, soil, structural system, finish level, and design complexity.\n\n• **Standard finish:** around **₹1,800–₹2,800 / sq ft**\n• **Premium finish:** around **₹3,000–₹4,500+ / sq ft**\n\nFor a more accurate budget, the key factors are plot location, number of floors, structural design, labor cost, materials, and the final finishing specification.\n\nThis is general public information and may vary by location, material costs, and project scope.";
  }

  for (const item of gnKnowledge) {
   if (item.triggers.some(t => qLower.includes(t))) {
    return item.answer;
   }
  }

  if (typeof window !== 'undefined') {
   const webQuery = encodeURIComponent(query);
   window.open(`https://duckduckgo.com/?q=${webQuery}`, '_blank', 'noopener,noreferrer');
  }
  return `Regarding "${query}":\n\nI can answer general construction, planning, or public-industry questions using public information.\n\nFor a project-specific discussion, send the site details, scope, or drawings and I can provide a relevant general answer.\n\nContact: **+91 9527660870** | **gnconstruction2016@gmail.com**\n\nThis is general public information and may vary by project type, site conditions, and local rules.`;
 }

 function formatMarkdown(text) {
  return text
   .replace(/\*\*(.*?)\*\*/g, '<strong class="text-paper font-semibold">$1</strong>')
   .replace(/\n\n/g, '<br><br>')
   .replace(/\n• /g, '<br>&bull; ')
   .replace(/\n1\. /g, '<br>1. ')
   .replace(/\n2\. /g, '<br>2. ')
   .replace(/\n3\. /g, '<br>3. ');
 }

 function escapeHTML(str) {
  return str.replace(/[&<>'"]/g, tag => ({
   '&': '&amp;',
   '<': '&lt;',
   '>': '&gt;',
   "'": '&#39;',
   '"': '&quot;'
  }[tag] || tag));
 }
}
