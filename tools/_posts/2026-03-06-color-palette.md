---
layout: default
title: "CHROMIQ – Color Palette Generator | HEX RGB Gradient & Export"
excerpt: "Generate beautiful random color palettes, gradients, and HEX/RGB codes. Lock colors, export palettes, copy codes, and preview UI cards instantly."
date: 2026-03-06
categories: tools
permalink: /tools/color-palette/
logo_svg: /assets/images/tools/logos/color-palette.svg
description: "Generate beautiful color palettes instantly. Get HEX and RGB values, random themes, and save your favorite palettes."
keywords: ["color palette generator", "hex color tool", "random palette generator", "UI color picker", "design color combinations"]
tags: [color, design, palette, gradient, utility]
---

<style>
:root{--primary:#8b5cf6;--primary-dark:#7c3aed;--accent:#f59e0b;--success:#10b981;--bg:#faf5ff;--card:#fff;--text:#1e1b4b;--muted:#6b7280;--border:#ddd6fe;--shadow:0 8px 32px rgba(139,92,246,0.10);}
[data-theme="dark"]{--bg:#0d0b1e;--card:#160f2e;--text:#ede9fe;--muted:#a78bfa;--border:#4c1d95;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;transition:background 0.3s,color 0.3s;}
.chromiq{max-width:1000px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:40px 20px 32px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),#c084fc);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:800;background:linear-gradient(135deg,var(--primary),#c084fc,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}
.hero p{color:var(--muted);font-size:1.05rem;max-width:560px;margin:0 auto;}
.toolbar{display:flex;justify-content:space-between;gap:10px;margin-bottom:16px;flex-wrap:wrap;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);color:var(--primary);}
.card{background:var(--card);border-radius:16px;padding:28px;box-shadow:var(--shadow);border:1px solid var(--border);margin-bottom:24px;}
.card-title{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:20px;display:flex;align-items:center;gap:8px;}
.palette-strip{display:flex;gap:0;border-radius:16px;overflow:hidden;height:120px;margin-bottom:20px;box-shadow:var(--shadow);}
.palette-swatch{flex:1;position:relative;cursor:pointer;transition:flex 0.3s;display:flex;flex-direction:column;justify-content:flex-end;padding:10px 8px;}
.palette-swatch:hover{flex:1.5;}
.swatch-code{font-size:0.75rem;font-weight:700;padding:4px 8px;border-radius:6px;background:rgba(0,0,0,0.4);color:#fff;text-align:center;backdrop-filter:blur(4px);}
.lock-btn{position:absolute;top:8px;right:8px;background:rgba(0,0,0,0.4);border:none;color:#fff;width:26px;height:26px;border-radius:50%;cursor:pointer;font-size:0.8rem;display:flex;align-items:center;justify-content:center;transition:background 0.2s;}
.lock-btn:hover{background:rgba(0,0,0,0.7);}
.lock-btn.locked{background:rgba(255,255,255,0.3);}
.palette-cards{display:flex;gap:12px;margin-bottom:20px;flex-wrap:wrap;}
.color-card{background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:14px;min-width:160px;flex:1;}
.color-swatch-sm{width:100%;height:60px;border-radius:8px;margin-bottom:10px;transition:transform 0.2s;}
.color-swatch-sm:hover{transform:scale(1.03);}
.color-codes{display:flex;flex-direction:column;gap:4px;}
.code-row{display:flex;justify-content:space-between;align-items:center;font-size:0.78rem;}
.code-label{color:var(--muted);font-weight:600;}
.code-val{font-family:'Courier New',monospace;font-weight:700;color:var(--text);}
.copy-chip{padding:2px 8px;background:var(--border);border:none;border-radius:10px;cursor:pointer;font-size:0.7rem;font-weight:600;color:var(--primary);}
.copy-chip:hover{background:var(--primary);color:#fff;}
.tab-row{display:flex;gap:8px;margin-bottom:18px;}
.tab-btn{padding:8px 18px;border-radius:20px;border:1.5px solid var(--border);background:var(--bg);color:var(--muted);font-size:0.85rem;font-weight:600;cursor:pointer;transition:all 0.2s;}
.tab-btn.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.tab-panel{display:none;}
.tab-panel.active{display:block;}
.gradient-preview{width:100%;height:80px;border-radius:12px;margin-bottom:14px;transition:all 0.3s;}
.gradient-controls{display:flex;gap:12px;align-items:center;flex-wrap:wrap;}
.gradient-controls label{font-size:0.82rem;font-weight:600;color:var(--muted);}
.gradient-controls input[type="color"]{width:40px;height:36px;border:none;border-radius:8px;cursor:pointer;padding:2px;}
.gradient-controls select{padding:8px 14px;border:1.5px solid var(--border);border-radius:8px;background:var(--bg);color:var(--text);font-size:0.9rem;}
.hex-converter{display:grid;grid-template-columns:1fr 40px 1fr;gap:12px;align-items:center;}
@media(max-width:600px){.hex-converter{grid-template-columns:1fr;}}
.conv-field label{font-size:0.82rem;font-weight:600;color:var(--muted);display:block;margin-bottom:6px;}
.conv-field input{width:100%;padding:10px 14px;border:1.5px solid var(--border);border-radius:10px;background:var(--bg);color:var(--text);font-size:1rem;font-family:'Courier New',monospace;}
.conv-field input:focus{outline:none;border-color:var(--primary);}
.conv-preview{width:50px;height:50px;border-radius:10px;border:2px solid var(--border);margin:18px auto 0;}
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

<div class="chromiq">
  <div class="hero">
    <div class="hero-badge">🎨 CHROMIQ</div>
    <h1>Color Palette Generator</h1>
    <p>Generate beautiful color palettes, gradients, and convert between HEX and RGB — lock your favorites.</p>
  </div>

  <div class="toolbar">
    <div style="display:flex;gap:8px;flex-wrap:wrap;">
      <button class="btn btn-primary" onclick="generatePalette()">🎲 New Palette</button>
      <button class="btn btn-ghost" onclick="exportPalette()">📥 Export</button>
      <button class="btn btn-ghost" onclick="sharePalette()">📤 Share</button>
    </div>
    <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Toggle Theme</button>
  </div>

  <div class="card">
    <div class="card-title">🎨 Palette (click swatch to copy, 🔒 to lock)</div>
    <div class="palette-strip" id="palette-strip"></div>
    <div class="palette-cards" id="palette-cards"></div>
    <p style="font-size:0.82rem;color:var(--muted);">Press Space or click New Palette to regenerate. Locked colors stay fixed.</p>
  </div>

  <div class="card">
    <div class="card-title">🛠️ Tools</div>
    <div class="tab-row">
      <button class="tab-btn active" onclick="setTab('gradient',this)">🌈 Gradient</button>
      <button class="tab-btn" onclick="setTab('converter',this)">🔄 HEX ↔ RGB</button>
    </div>

    <div id="tab-gradient" class="tab-panel active">
      <div class="gradient-preview" id="gradient-preview"></div>
      <div class="gradient-controls">
        <label>Color 1</label>
        <input type="color" id="g-c1" value="#8b5cf6" oninput="updateGradient()">
        <label>Color 2</label>
        <input type="color" id="g-c2" value="#ec4899" oninput="updateGradient()">
        <label>Direction</label>
        <select id="g-dir" onchange="updateGradient()">
          <option value="to right">→ Left to Right</option>
          <option value="to bottom">↓ Top to Bottom</option>
          <option value="135deg">↘ Diagonal</option>
          <option value="circle">○ Radial</option>
        </select>
        <button class="btn btn-ghost" onclick="copyGradientCSS()">📋 Copy CSS</button>
      </div>
      <div style="margin-top:12px;padding:10px 14px;background:var(--bg);border-radius:8px;font-family:'Courier New',monospace;font-size:0.82rem;color:var(--muted);" id="gradient-css"></div>
    </div>

    <div id="tab-converter" class="tab-panel">
      <div class="hex-converter">
        <div class="conv-field">
          <label>HEX Color</label>
          <input type="text" id="hex-in" placeholder="#8b5cf6" oninput="hexToRgb()" maxlength="7">
        </div>
        <div style="text-align:center;padding-top:28px;font-size:1.2rem;color:var(--muted);">⇄</div>
        <div class="conv-field">
          <label>RGB Color</label>
          <input type="text" id="rgb-in" placeholder="139, 92, 246" oninput="rgbToHex()">
        </div>
      </div>
      <div class="conv-preview" id="conv-preview"></div>
      <div style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap;">
        <button class="btn btn-ghost" onclick="copyHex()">📋 Copy HEX</button>
        <button class="btn btn-ghost" onclick="copyRgb()">📋 Copy RGB</button>
      </div>
    </div>
  </div>

  <div class="seo-block">
    <h2>About CHROMIQ Color Palette Generator</h2>
    <p>CHROMIQ generates harmonious color palettes using color theory algorithms. Each generated palette ensures perceptual balance across hue, saturation, and brightness. Lock colors you love and regenerate the rest for infinite design exploration.</p>
    <h3>Color Theory Basics</h3>
    <ul>
      <li><strong>Complementary</strong> – Colors opposite on the color wheel (e.g., blue and orange)</li>
      <li><strong>Analogous</strong> – Colors adjacent on the wheel — harmonious and pleasing</li>
      <li><strong>Triadic</strong> – Three evenly-spaced colors — vibrant and balanced</li>
      <li><strong>Monochromatic</strong> – Different shades/tints of the same hue — elegant and cohesive</li>
    </ul>
    <h3>HEX vs RGB Color Formats</h3>
    <p>HEX colors use a 6-digit hexadecimal string (#RRGGBB) where each pair represents red, green, blue intensity (0–255). RGB uses three decimal numbers (rgb(R, G, B)). Both represent the same colors — HEX is more compact for CSS; RGB is more readable for programmatic manipulation.</p>
    <h3>Choosing a Color Palette for Your Brand</h3>
    <ul>
      <li>Start with your primary brand color, then generate complementary or analogous colors</li>
      <li>Ensure sufficient contrast ratios for accessibility (WCAG 2.1 requires 4.5:1 for normal text)</li>
      <li>Limit your palette to 3–5 colors for clean, professional design</li>
      <li>Test colors on both light and dark backgrounds</li>
    </ul>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">How do I convert HEX to RGB? <span>+</span></div>
      <div class="faq-a hidden">Parse the HEX string into three 2-digit pairs and convert each from base 16 to base 10. Example: #8b5cf6 → R=0x8b=139, G=0x5c=92, B=0xf6=246 → rgb(139, 92, 246). Use CHROMIQ's converter tab for instant results.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">What makes a good color palette for a website? <span>+</span></div>
      <div class="faq-a hidden">A good web palette has: 1 primary brand color, 1 secondary/accent color, neutral grays for text and backgrounds, and at least 1 semantic color (green for success, red for errors). Ensure all text/background combinations meet WCAG contrast requirements.</div>
    </div>
    <div class="related-grid">
      <a href="/tools/qr-generator/" class="related-card"><div class="rc-emoji">📱</div><div class="rc-name">QR Generator</div></a>
      <a href="/tools/image-compressor/" class="related-card"><div class="rc-emoji">🖼️</div><div class="rc-name">Image Compressor</div></a>
      <a href="/tools/json-formatter/" class="related-card"><div class="rc-emoji">{ }</div><div class="rc-name">JSON Formatter</div></a>
      <a href="/tools/base64/" class="related-card"><div class="rc-emoji">🔢</div><div class="rc-name">Base64 Encoder</div></a>
    </div>
  </div>
</div>

<script>
let palette = [];
let locked = [false,false,false,false,false];

function randHex() {
  const h = Math.floor(Math.random()*0xffffff).toString(16).padStart(6,'0');
  return '#' + h;
}

function generatePalette() {
  palette = palette.map((c,i) => locked[i] ? c : randHex());
  if (!palette.length) palette = Array.from({length:5}, randHex);
  renderPalette();
}

function hexToRgbArr(hex) {
  const r = parseInt(hex.slice(1,3),16);
  const g = parseInt(hex.slice(3,5),16);
  const b = parseInt(hex.slice(5,7),16);
  return [r,g,b];
}

function getContrastColor(hex) {
  const [r,g,b] = hexToRgbArr(hex);
  return (0.299*r + 0.587*g + 0.114*b) > 128 ? '#000' : '#fff';
}

function renderPalette() {
  const strip = document.getElementById('palette-strip');
  const cards = document.getElementById('palette-cards');
  strip.innerHTML = palette.map((c,i) => `
    <div class="palette-swatch" style="background:${c}" onclick="copyColor('${c}')">
      <button class="lock-btn ${locked[i]?'locked':''}" onclick="event.stopPropagation();toggleLock(${i})" title="${locked[i]?'Unlock':'Lock'}">${locked[i]?'🔒':'🔓'}</button>
      <div class="swatch-code">${c.toUpperCase()}</div>
    </div>`).join('');
  cards.innerHTML = palette.map((c,i) => {
    const [r,g,b] = hexToRgbArr(c);
    return `<div class="color-card">
      <div class="color-swatch-sm" style="background:${c}" onclick="copyColor('${c}')"></div>
      <div class="color-codes">
        <div class="code-row"><span class="code-label">HEX</span><span class="code-val">${c.toUpperCase()}</span><button class="copy-chip" onclick="copyColor('${c}')">Copy</button></div>
        <div class="code-row"><span class="code-label">RGB</span><span class="code-val">${r},${g},${b}</span><button class="copy-chip" onclick="navigator.clipboard.writeText('rgb(${r},${g},${b})')">Copy</button></div>
        <div class="code-row"><span class="code-label">CSS</span><span class="code-val">rgb(${r},${g},${b})</span></div>
      </div>
    </div>`;
  }).join('');
}

function toggleLock(i) { locked[i] = !locked[i]; renderPalette(); }

function copyColor(hex) {
  navigator.clipboard.writeText(hex.toUpperCase());
  const btn = event.target;
  const orig = btn.textContent;
  if (btn.textContent === 'Copy') { btn.textContent = '✓'; setTimeout(()=>btn.textContent='Copy',1200); }
}

function setTab(tab, btn) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.getElementById('tab-'+tab).classList.add('active');
  if (tab === 'gradient') updateGradient();
}

function updateGradient() {
  const c1 = document.getElementById('g-c1').value;
  const c2 = document.getElementById('g-c2').value;
  const dir = document.getElementById('g-dir').value;
  const isRadial = dir === 'circle';
  const css = isRadial ? `radial-gradient(circle, ${c1}, ${c2})` : `linear-gradient(${dir}, ${c1}, ${c2})`;
  document.getElementById('gradient-preview').style.background = css;
  document.getElementById('gradient-css').textContent = `background: ${css};`;
}

function copyGradientCSS() {
  const css = document.getElementById('gradient-css').textContent;
  navigator.clipboard.writeText(css).then(()=>alert('CSS copied!'));
}

function hexToRgb() {
  let hex = document.getElementById('hex-in').value.trim();
  if (!hex.startsWith('#')) hex = '#' + hex;
  if (hex.length !== 7) return;
  const [r,g,b] = hexToRgbArr(hex);
  if (isNaN(r)) return;
  document.getElementById('rgb-in').value = `${r}, ${g}, ${b}`;
  document.getElementById('conv-preview').style.background = hex;
}

function rgbToHex() {
  const val = document.getElementById('rgb-in').value;
  const parts = val.split(',').map(s => parseInt(s.trim()));
  if (parts.length !== 3 || parts.some(isNaN)) return;
  const hex = '#' + parts.map(v => Math.max(0,Math.min(255,v)).toString(16).padStart(2,'0')).join('');
  document.getElementById('hex-in').value = hex;
  document.getElementById('conv-preview').style.background = hex;
}

function copyHex() { navigator.clipboard.writeText(document.getElementById('hex-in').value).then(()=>alert('HEX copied!')); }
function copyRgb() { navigator.clipboard.writeText('rgb(' + document.getElementById('rgb-in').value + ')').then(()=>alert('RGB copied!')); }

function exportPalette() {
  const data = palette.map((c,i) => { const [r,g,b] = hexToRgbArr(c); return `${c.toUpperCase()} | rgb(${r},${g},${b})`; }).join('\n');
  const blob = new Blob([`CHROMIQ Palette\n${'='.repeat(30)}\n${data}`], {type:'text/plain'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'chromiq-palette.txt'; a.click();
}

function sharePalette() {
  const text = `🎨 My CHROMIQ palette: ${palette.map(c=>c.toUpperCase()).join(', ')}\n${window.location.href}`;
  if (navigator.share) navigator.share({title:'CHROMIQ Palette',text}); else navigator.clipboard.writeText(text).then(()=>alert('Palette link copied!'));
}

function toggleTheme() { const d=document.documentElement; d.setAttribute('data-theme',d.getAttribute('data-theme')==='dark'?'light':'dark'); }
function toggleFaq(el) { const a=el.nextElementSibling; const s=el.querySelector('span'); a.classList.toggle('hidden'); s.textContent=a.classList.contains('hidden')?'+':'−'; }

document.addEventListener('keydown', e => { if (e.code === 'Space' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') { e.preventDefault(); generatePalette(); } });
generatePalette();
updateGradient();
</script>
