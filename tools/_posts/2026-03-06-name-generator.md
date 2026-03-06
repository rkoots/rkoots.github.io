---
layout: default
title: "NOMINA – Random Name Generator | Startup, Brand, Domain & Fantasy Names"
excerpt: "Generate startup names, brand names, domain names, and fantasy character names. Keyword-based generation, domain availability hints, save favorites, and instant regeneration."
date: 2026-03-06
categories: tools
permalink: /tools/name-generator/
description: "Free online random name generator for startups, brands, domains, and fantasy characters. Keyword-based generation, domain hints, save favorites, and one-click regeneration."
keywords: ["name generator", "startup name generator", "brand name generator", "domain name generator", "fantasy name generator", "random name", "business name ideas", "company name generator"]
tags: [names, generator, startup, branding, domain, fantasy]
---

<style>
:root{--primary:#0d9488;--primary-dark:#0f766e;--accent:#f59e0b;--success:#10b981;--bg:#f0fdfa;--card:#fff;--text:#0d3330;--muted:#6b7280;--border:#99f6e4;--shadow:0 8px 32px rgba(13,148,136,0.10);}
[data-theme="dark"]{--bg:#041a18;--card:#062220;--text:#ccfbf1;--muted:#94a3b8;--border:#134e4a;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;transition:background 0.3s,color 0.3s;}
.nomina{max-width:960px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:40px 20px 32px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),#2dd4bf);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:800;background:linear-gradient(135deg,var(--primary),#2dd4bf,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}
.hero p{color:var(--muted);font-size:1.05rem;max-width:560px;margin:0 auto;}
.toolbar{display:flex;justify-content:flex-end;gap:10px;margin-bottom:16px;flex-wrap:wrap;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);color:var(--primary);}
.card{background:var(--card);border-radius:16px;padding:28px;box-shadow:var(--shadow);border:1px solid var(--border);margin-bottom:24px;}
.card-title{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:20px;display:flex;align-items:center;gap:8px;}
.mode-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:24px;}
.mode-card{padding:14px 10px;border-radius:12px;border:2px solid var(--border);background:var(--bg);cursor:pointer;text-align:center;transition:all 0.2s;}
.mode-card:hover,.mode-card.active{border-color:var(--primary);background:rgba(13,148,136,0.08);}
.mode-card.active{box-shadow:0 0 0 2px var(--primary);}
.mode-card .mc-emoji{font-size:1.6rem;display:block;margin-bottom:6px;}
.mode-card .mc-label{font-size:0.82rem;font-weight:700;color:var(--text);}
.field label{display:block;font-size:0.85rem;font-weight:600;color:var(--muted);margin-bottom:6px;}
.field input{width:100%;padding:11px 16px;border:1.5px solid var(--border);border-radius:10px;background:var(--bg);color:var(--text);font-size:1rem;transition:border-color 0.2s;}
.field input:focus{outline:none;border-color:var(--primary);}
.count-row{display:flex;align-items:center;gap:12px;margin-top:14px;}
.count-row label{font-size:0.85rem;font-weight:600;color:var(--muted);}
.count-row input[type="range"]{flex:1;accent-color:var(--primary);}
.count-row span{font-size:1rem;font-weight:800;color:var(--primary);min-width:30px;}
.names-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;margin-top:20px;}
.name-item{background:var(--bg);border:1.5px solid var(--border);border-radius:12px;padding:16px;display:flex;align-items:center;justify-content:space-between;gap:10px;transition:all 0.2s;}
.name-item:hover{border-color:var(--primary);}
.name-item .ni-name{font-size:1.05rem;font-weight:700;color:var(--text);flex:1;}
.name-item .ni-domain{font-size:0.72rem;color:var(--muted);margin-top:2px;}
.name-actions{display:flex;gap:6px;flex-shrink:0;}
.icon-btn{width:30px;height:30px;border-radius:8px;border:1px solid var(--border);background:var(--card);cursor:pointer;font-size:0.85rem;display:flex;align-items:center;justify-content:center;transition:all 0.2s;}
.icon-btn:hover{border-color:var(--primary);background:var(--primary);color:#fff;}
.saved-section{max-height:300px;overflow-y:auto;}
.saved-item{display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:var(--bg);border:1px solid var(--border);border-radius:8px;margin-bottom:8px;font-size:0.9rem;}
.saved-item .si-name{font-weight:700;flex:1;}
.saved-item .si-mode{font-size:0.75rem;color:var(--muted);margin-left:8px;}
.no-saved{color:var(--muted);font-size:0.9rem;text-align:center;padding:20px;}
.seo-block{margin-top:48px;padding:32px;background:var(--card);border-radius:16px;border:1px solid var(--border);}
.seo-block h2{font-size:1.5rem;font-weight:700;color:var(--primary);margin-bottom:16px;}
.seo-block h3{font-size:1.1rem;font-weight:600;margin:20px 0 8px;}
.seo-block p,.seo-block li{color:var(--muted);line-height:1.7;font-size:0.95rem;}
.seo-block ul{padding-left:20px;}
.faq-item{border-bottom:1px solid var(--border);padding:16px 0;}
.faq-q{font-weight:600;cursor:pointer;display:flex;justify-content:space-between;color:var(--text);}
.faq-a{color:var(--muted);font-size:0.9rem;line-height:1.6;padding-top:10px;}
.hidden{display:none;}
.related-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-top:16px;}
.related-card{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center;text-decoration:none;transition:all 0.2s;}
.related-card:hover{border-color:var(--primary);transform:translateY(-2px);}
.related-card .rc-emoji{font-size:1.6rem;}
.related-card .rc-name{font-size:0.85rem;font-weight:600;color:var(--text);margin-top:6px;}
</style>

<div class="nomina">
  <div class="hero">
    <div class="hero-badge">✨ NOMINA</div>
    <h1>Name Generator</h1>
    <p>Generate startup, brand, domain, and fantasy names — keyword-based, instant, and free.</p>
  </div>

  <div class="toolbar">
    <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Toggle Theme</button>
  </div>

  <div class="card">
    <div class="card-title">🎯 Name Style</div>
    <div class="mode-grid">
      <div class="mode-card active" onclick="setMode('startup',this)"><span class="mc-emoji">🚀</span><span class="mc-label">Startup</span></div>
      <div class="mode-card" onclick="setMode('brand',this)"><span class="mc-emoji">💼</span><span class="mc-label">Brand</span></div>
      <div class="mode-card" onclick="setMode('domain',this)"><span class="mc-emoji">🌐</span><span class="mc-label">Domain</span></div>
      <div class="mode-card" onclick="setMode('fantasy',this)"><span class="mc-emoji">🧙</span><span class="mc-label">Fantasy</span></div>
    </div>

    <div class="field">
      <label>Keyword (optional — inspire the names)</label>
      <input type="text" id="keyword-input" placeholder="e.g. fast, cloud, secure, dragon..." oninput="generate()">
    </div>

    <div class="count-row">
      <label>Number of names:</label>
      <input type="range" min="5" max="30" value="12" id="count-slider" oninput="document.getElementById('count-val').textContent=this.value;generate()">
      <span id="count-val">12</span>
    </div>

    <div style="margin-top:18px;display:flex;gap:10px;">
      <button class="btn btn-primary" onclick="generate()" style="flex:1;">⚡ Generate Names</button>
    </div>

    <div class="names-grid" id="names-grid"></div>
  </div>

  <div class="card">
    <div class="card-title">💾 Saved Favorites</div>
    <div class="saved-section" id="saved-section">
      <div class="no-saved">Click ♡ on any name to save it here</div>
    </div>
    <div style="margin-top:12px;display:flex;gap:10px;">
      <button class="btn btn-ghost" onclick="clearSaved()">🗑️ Clear Saved</button>
      <button class="btn btn-ghost" onclick="exportSaved()">📥 Export</button>
    </div>
  </div>

  <div class="seo-block">
    <h2>How to Name Your Startup or Brand</h2>
    <p>Choosing the right name for your business is one of the most important decisions you'll make. A great name is memorable, easy to spell, distinctive, and available as a domain. NOMINA generates names using linguistic patterns, portmanteau techniques, and semantic associations to inspire your naming process.</p>
    <h3>Naming Strategies Explained</h3>
    <ul>
      <li><strong>Startup names</strong> – Combine tech-inspired prefixes/suffixes (e.g., -ify, -io, -ly) with keywords for modern, memorable names</li>
      <li><strong>Brand names</strong> – Use evocative words that convey the brand's personality and values</li>
      <li><strong>Domain names</strong> – Short, pronounceable, domain-friendly names optimized for .com availability</li>
      <li><strong>Fantasy names</strong> – Mythological, elvish, and ancient-inspired names for characters and worlds</li>
    </ul>
    <h3>What Makes a Good Business Name?</h3>
    <ul>
      <li>Short — 1-2 syllables are easier to remember and type</li>
      <li>Unique — distinct enough to trademark and stand out</li>
      <li>Available — check domain and social media handle availability</li>
      <li>Evocative — suggests something about your product or values</li>
      <li>Globally appropriate — avoid accidental negative meanings in other languages</li>
    </ul>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">How do I check if a domain name is available? <span>+</span></div>
      <div class="faq-a hidden">NOMINA provides a quick domain availability hint by checking common patterns. For definitive availability, visit domain registrars like Namecheap, GoDaddy, or Google Domains and search for the exact domain. Check for .com, .io, and .co variants.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">Can I trademark a generated name? <span>+</span></div>
      <div class="faq-a hidden">Generated names are unregistered and may be available for trademarking. Always conduct a thorough trademark search through your country's IP office (USPTO in the US, IPIndia in India) and consult a trademark attorney before filing.</div>
    </div>
    <div class="related-grid">
      <a href="/tools/slug-generator/" class="related-card"><div class="rc-emoji">🔗</div><div class="rc-name">Slug Generator</div></a>
      <a href="/tools/word-counter/" class="related-card"><div class="rc-emoji">📝</div><div class="rc-name">Word Counter</div></a>
      <a href="/tools/password-generator/" class="related-card"><div class="rc-emoji">🔐</div><div class="rc-name">Password Generator</div></a>
      <a href="/tools/markdown-converter/" class="related-card"><div class="rc-emoji">📄</div><div class="rc-name">Markdown Converter</div></a>
    </div>
  </div>
</div>

<script>
let currentMode = 'startup';
let saved = [];

const PREFIXES = {
  startup: ['Cloud','Swift','Snap','Flux','Nex','Zap','Omni','Meta','Hyper','Ultra','Vert','Nova','Lume','Aero','Velo','Coda','Helix','Atom','Pico','Nano'],
  brand: ['Prime','Elite','Apex','Viva','Bold','Pure','Icon','Core','Peak','Vibe','Glow','Spark','Forge','Craft','Edge','Lumis','Aura','Flux','Arc','Crest'],
  domain: ['get','use','try','go','my','the','be','hi','app','web','say','hey','run','fly','top','pro','now'],
  fantasy: ['Aer','Vel','Zor','Thal','Eyr','Syl','Mor','Eld','Nar','Cal','Bel','Vor','Aeld','Zeph','Mira','Lyss','Raen','Cyph','Dael','Oph']
};
const SUFFIXES = {
  startup: ['ify','io','ly','hub','lab','ai','ux','base','core','sync','wave','link','grid','gate','flow','forge','stack','bit','byte','net'],
  brand: ['works','craft','co','world','house','studio','place','sphere','zone','space','point','line','way','ology','ness','ify','era','plus','pro'],
  domain: ['app','site','hq','co','hub','io','pro','ly','now','link','way'],
  fantasy: ['ius','ara','iel','eth','oth','orn','ael','ys','ir','ath','or','ax','en','wyn','ion','alis','ira','eus','vos','nor']
};
const MIDDLES = ['tech','cloud','data','safe','fast','live','open','web','net','soft','smart','bright','green','blue','gold','dark','light','bold','pure','real'];

function setMode(mode, el) {
  currentMode = mode;
  document.querySelectorAll('.mode-card').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  generate();
}

function capitalize(s) { return s.charAt(0).toUpperCase() + s.slice(1); }

function makeName(mode, keyword) {
  const pre = PREFIXES[mode];
  const suf = SUFFIXES[mode];
  const rand = arr => arr[Math.floor(Math.random()*arr.length)];
  const kw = keyword ? keyword.toLowerCase().replace(/\s+/g,'').slice(0,8) : '';
  const roll = Math.random();
  let name;
  if (kw && roll < 0.4) {
    const s = rand(suf);
    name = capitalize(kw) + s;
  } else if (kw && roll < 0.65) {
    const p = rand(pre).toLowerCase();
    name = capitalize(p) + capitalize(kw);
  } else if (roll < 0.8) {
    name = capitalize(rand(pre)) + rand(suf);
  } else {
    const p = rand(pre).toLowerCase();
    const m = rand(MIDDLES);
    name = capitalize(p) + m;
  }
  if (mode === 'domain') name = name.toLowerCase();
  return name;
}

function domainHint(name) {
  const clean = name.toLowerCase().replace(/[^a-z0-9]/g,'');
  const len = clean.length;
  if (len <= 5) return '✅ Short — likely available';
  if (len <= 8) return '🟡 Check .com availability';
  return '🔍 Search domain registrar';
}

function generate() {
  const keyword = document.getElementById('keyword-input').value.trim();
  const count = parseInt(document.getElementById('count-slider').value);
  const names = new Set();
  let attempts = 0;
  while (names.size < count && attempts < count * 10) {
    names.add(makeName(currentMode, keyword));
    attempts++;
  }
  const grid = document.getElementById('names-grid');
  grid.innerHTML = Array.from(names).map(name => `
    <div class="name-item">
      <div>
        <div class="ni-name">${name}</div>
        <div class="ni-domain">${currentMode === 'domain' || currentMode === 'startup' ? domainHint(name) : ''}</div>
      </div>
      <div class="name-actions">
        <button class="icon-btn" onclick="saveName('${name}')" title="Save">♡</button>
        <button class="icon-btn" onclick="navigator.clipboard.writeText('${name}').then(()=>this.textContent='✓').then(()=>setTimeout(()=>this.textContent='📋',1200))" title="Copy">📋</button>
      </div>
    </div>`).join('');
}

function saveName(name) {
  if (!saved.find(s => s.name === name)) {
    saved.push({name, mode: currentMode});
    renderSaved();
  }
}

function renderSaved() {
  const el = document.getElementById('saved-section');
  if (!saved.length) { el.innerHTML = '<div class="no-saved">Click ♡ on any name to save it here</div>'; return; }
  el.innerHTML = saved.map((s,i) => `
    <div class="saved-item">
      <span class="si-name">${s.name}</span>
      <span class="si-mode">${s.mode}</span>
      <button class="icon-btn" onclick="navigator.clipboard.writeText('${s.name}')" title="Copy">📋</button>
      <button class="icon-btn" onclick="removeSaved(${i})" title="Remove">✕</button>
    </div>`).join('');
}

function removeSaved(i) { saved.splice(i,1); renderSaved(); }
function clearSaved() { saved = []; renderSaved(); }
function exportSaved() {
  if (!saved.length) { alert('No saved names to export.'); return; }
  const text = saved.map(s => `${s.name} (${s.mode})`).join('\n');
  const blob = new Blob([`NOMINA Saved Names\n${'='.repeat(30)}\n${text}`], {type:'text/plain'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'nomina-names.txt'; a.click();
}

function toggleTheme() { const d=document.documentElement; d.setAttribute('data-theme',d.getAttribute('data-theme')==='dark'?'light':'dark'); }
function toggleFaq(el) { const a=el.nextElementSibling; const s=el.querySelector('span'); a.classList.toggle('hidden'); s.textContent=a.classList.contains('hidden')?'+':'−'; }
generate();
</script>
