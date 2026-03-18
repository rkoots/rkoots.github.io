---
layout: default
title: "MINIQFY – CSS & JS Minifier | Free Online Code Minification & Compression Tool"
excerpt: "Minify CSS and JavaScript instantly with MINIQFY. Remove whitespace, comments, and redundancies. Free online code minifier with size reduction stats and download support."
date: 2026-03-18
categories: tools
permalink: /tools/css-minifier/
description: "Free online CSS and JavaScript minifier. Compress and minify CSS, JS code to reduce file size, improve page load speed, and optimize web performance. Instant results."
keywords: ["css minifier online", "javascript minifier free", "minify css online", "minify js code", "compress css tool", "js compressor online", "code minification tool", "online css compressor", "reduce css file size"]
tags: [CSS, JavaScript, minifier, performance, developer]
---

<style>
:root{--primary:#dc2626;--primary-dark:#b91c1c;--accent:#f59e0b;--success:#10b981;--bg:#fff7f7;--card:#fff;--text:#1c0a0a;--muted:#6b7280;--border:#fecaca;--shadow:0 8px 32px rgba(220,38,38,0.08);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.miniqfy{max-width:1100px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.tabs{display:flex;gap:4px;border-bottom:2px solid var(--border);margin-bottom:16px;}
.tab{padding:9px 20px;border:none;background:none;color:var(--muted);font-size:0.9rem;font-weight:700;cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px;transition:color 0.2s;}
.tab.active{color:var(--primary);border-bottom-color:var(--primary);}
.toolbar{display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap;align-items:center;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-success{background:var(--success);color:#fff;}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);}
.editors{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.editor-label{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;}
textarea{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.85rem;background:var(--card);color:var(--text);resize:vertical;line-height:1.5;}
textarea:focus{outline:none;border-color:var(--primary);}
.output-box{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.83rem;background:#fff7f7;white-space:pre-wrap;word-break:break-all;min-height:200px;max-height:400px;overflow:auto;}
.stats-bar{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-top:14px;}
.stat-box{background:linear-gradient(135deg,#fff7f7,#fee2e2);border-radius:10px;padding:14px;border:1px solid var(--border);text-align:center;}
.stat-val{font-size:1.5rem;font-weight:800;color:var(--primary);}
.stat-label{font-size:0.78rem;color:var(--muted);margin-top:4px;}
.savings{color:#059669;font-size:1.4rem;font-weight:800;}
.file-btn{padding:8px 14px;border-radius:8px;border:1px dashed var(--border);background:var(--card);color:var(--primary);cursor:pointer;font-size:0.85rem;font-weight:600;}
@media(max-width:700px){.editors{grid-template-columns:1fr;}}
</style>

<div class="miniqfy">
  <header class="hero">
    <div class="hero-badge">FREE CODE MINIFIER</div>
    <h1>MINIQFY – CSS & JS Minifier</h1>
    <p>Compress CSS and JavaScript code to boost page load performance. Remove comments, whitespace, and redundancies — with instant size reduction stats.</p>
  </header>

  <div class="card">
    <div class="tabs">
      <button class="tab active" onclick="switchLang('css',this)">CSS Minifier</button>
      <button class="tab" onclick="switchLang('js',this)">JS Minifier</button>
      <button class="tab" onclick="switchLang('html',this)">HTML Minifier</button>
    </div>

    <div class="toolbar">
      <button class="btn btn-primary" onclick="minifyCode()">Minify</button>
      <button class="btn btn-ghost" onclick="beautifyCode()">Beautify / Expand</button>
      <button class="btn btn-success" onclick="copyOutput()">Copy Output</button>
      <button class="btn btn-ghost" onclick="downloadOutput()">Download</button>
      <button class="btn btn-ghost" onclick="clearAll()">Clear</button>
      <label class="file-btn">📂 Upload File <input type="file" accept=".css,.js,.html,.htm" style="display:none;" onchange="loadFile(this)"></label>
      <label style="font-size:0.85rem;color:var(--muted);display:flex;align-items:center;gap:6px;">
        <input type="checkbox" id="removeComments" checked> Remove comments
      </label>
    </div>

    <div class="editors">
      <div>
        <div class="editor-label">Input Code</div>
        <textarea id="codeInput" rows="14" placeholder="Paste your CSS, JS, or HTML code here…"></textarea>
      </div>
      <div>
        <div class="editor-label">Minified Output</div>
        <div class="output-box" id="codeOutput">Minified output will appear here…</div>
      </div>
    </div>

    <div class="stats-bar" id="statsBar" style="display:none;">
      <div class="stat-box"><div class="stat-val" id="origSize">—</div><div class="stat-label">Original Size</div></div>
      <div class="stat-box"><div class="stat-val" id="minSize">—</div><div class="stat-label">Minified Size</div></div>
      <div class="stat-box"><div class="savings" id="savePct">—</div><div class="stat-label">Size Reduction</div></div>
      <div class="stat-box"><div class="stat-val" id="saveBytes">—</div><div class="stat-label">Bytes Saved</div></div>
    </div>
  </div>
</div>

<script>
let currentLang = 'css';
let outputText = '';

function switchLang(lang, el) {
  currentLang = lang;
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('codeInput').placeholder = `Paste your ${lang.toUpperCase()} code here…`;
}

function minifyCSS(css) {
  const removeComments = document.getElementById('removeComments').checked;
  let out = css;
  if (removeComments) out = out.replace(/\/\*[\s\S]*?\*\//g, '');
  out = out
    .replace(/\s*([{};:,>~+])\s*/g, '$1')
    .replace(/\s+/g, ' ')
    .replace(/;\s*}/g, '}')
    .replace(/\s*{\s*/g, '{')
    .replace(/\s*}\s*/g, '}')
    .replace(/:\s+/g, ':')
    .replace(/,\s+/g, ',')
    .replace(/0\.([\d])/g, '.$1')
    .replace(/([\s:,])(0)(px|em|rem|%)/gi, '$10')
    .trim();
  return out;
}

function minifyJS(js) {
  const removeComments = document.getElementById('removeComments').checked;
  let out = js;
  if (removeComments) {
    out = out.replace(/\/\*[\s\S]*?\*\//g, '');
    out = out.replace(/\/\/[^\n]*/g, '');
  }
  out = out
    .replace(/\s*([=+\-*/%&|^!<>?:,;{}()\[\]])\s*/g, '$1')
    .replace(/\s+/g, ' ')
    .replace(/\n+/g, ' ')
    .trim();
  return out;
}

function minifyHTML(html) {
  const removeComments = document.getElementById('removeComments').checked;
  let out = html;
  if (removeComments) out = out.replace(/<!--[\s\S]*?-->/g, '');
  out = out
    .replace(/\s+/g, ' ')
    .replace(/>\s+</g, '><')
    .replace(/\s*(=)\s*/g, '$1')
    .trim();
  return out;
}

function beautifyCSS(css) {
  let out = css
    .replace(/\s*{\s*/g, ' {\n  ')
    .replace(/;\s*/g, ';\n  ')
    .replace(/\s*}\s*/g, '\n}\n')
    .replace(/,\s*/g, ',\n')
    .trim();
  return out;
}

function minifyCode() {
  const code = document.getElementById('codeInput').value;
  if (!code.trim()) return;
  let result;
  if (currentLang === 'css') result = minifyCSS(code);
  else if (currentLang === 'js') result = minifyJS(code);
  else result = minifyHTML(code);
  outputText = result;
  document.getElementById('codeOutput').textContent = result;
  showStats(code, result);
}

function beautifyCode() {
  const code = document.getElementById('codeInput').value;
  if (!code.trim()) return;
  let result = currentLang === 'css' ? beautifyCSS(code) : code.replace(/;/g,';\n').replace(/{/g,'{\n  ').replace(/}/g,'\n}');
  outputText = result;
  document.getElementById('codeOutput').textContent = result;
  showStats(code, result);
}

function showStats(orig, mini) {
  const ob = new Blob([orig]).size, mb = new Blob([mini]).size;
  const pct = orig.length > 0 ? (((ob - mb) / ob) * 100).toFixed(1) : 0;
  document.getElementById('origSize').textContent = formatBytes(ob);
  document.getElementById('minSize').textContent = formatBytes(mb);
  document.getElementById('savePct').textContent = pct + '%';
  document.getElementById('saveBytes').textContent = formatBytes(Math.max(0, ob - mb));
  document.getElementById('statsBar').style.display = 'grid';
}

function formatBytes(b) {
  if (b < 1024) return b + ' B';
  return (b/1024).toFixed(1) + ' KB';
}

function copyOutput() {
  if (!outputText) return alert('Minify code first');
  navigator.clipboard.writeText(outputText).then(() => alert('Copied to clipboard!'));
}

function downloadOutput() {
  if (!outputText) return alert('Minify code first');
  const ext = currentLang;
  const blob = new Blob([outputText], {type:'text/plain'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `minified.${ext}`;
  a.click();
}

function loadFile(input) {
  const file = input.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => { document.getElementById('codeInput').value = e.target.result; };
  reader.readAsText(file);
}

function clearAll() {
  document.getElementById('codeInput').value = '';
  document.getElementById('codeOutput').textContent = 'Minified output will appear here…';
  document.getElementById('statsBar').style.display = 'none';
  outputText = '';
}
</script>
