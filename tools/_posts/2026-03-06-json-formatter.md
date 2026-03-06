---
layout: default
title: "JSONIQ – JSON Formatter | Validator, Minifier & Collapsible Tree View"
excerpt: "Format, validate, minify, and explore JSON with syntax highlighting, collapsible tree view, error highlighting, and instant copy/download. Load sample JSON to get started."
date: 2026-03-06
categories: tools
permalink: /tools/json-formatter/
logo_svg: /assets/images/tools/logos/json-formatter.svg
description: "Free online JSON formatter and validator. Beautify, minify, validate and copy JSON instantly."
keywords: ["json formatter", "json beautifier", "json validator", "minify json", "format json online"]
tags: [JSON, developer, formatter, validator, utility]
---

<style>
:root{--primary:#0891b2;--primary-dark:#0e7490;--accent:#f59e0b;--success:#10b981;--danger:#ef4444;--bg:#ecfeff;--card:#fff;--text:#083344;--muted:#6b7280;--border:#a5f3fc;--shadow:0 8px 32px rgba(8,145,178,0.10);}
[data-theme="dark"]{--bg:#020f14;--card:#061a24;--text:#cffafe;--muted:#94a3b8;--border:#164e63;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;transition:background 0.3s,color 0.3s;}
.jsoniq{max-width:1100px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:40px 20px 32px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),#22d3ee);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:800;background:linear-gradient(135deg,var(--primary),#22d3ee,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}
.hero p{color:var(--muted);font-size:1.05rem;max-width:560px;margin:0 auto;}
.toolbar{display:flex;justify-content:space-between;gap:10px;margin-bottom:16px;flex-wrap:wrap;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:8px;border:none;cursor:pointer;font-size:0.88rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);color:var(--primary);}
.btn-danger{background:var(--danger);color:#fff;}
.btn-success{background:var(--success);color:#fff;}
.card{background:var(--card);border-radius:16px;padding:24px;box-shadow:var(--shadow);border:1px solid var(--border);margin-bottom:24px;}
.card-title{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:16px;display:flex;align-items:center;gap:8px;}
.editor-layout{display:grid;grid-template-columns:1fr 1fr;gap:20px;}
@media(max-width:800px){.editor-layout{grid-template-columns:1fr;}}
.panel-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;flex-wrap:wrap;gap:8px;}
.panel-title{font-size:0.85rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;}
textarea.code-area{width:100%;min-height:400px;padding:16px;background:#0f172a;color:#e2e8f0;font-family:'Courier New',Consolas,monospace;font-size:0.88rem;line-height:1.6;border:1.5px solid var(--border);border-radius:12px;resize:vertical;transition:border-color 0.2s;}
textarea.code-area:focus{outline:none;border-color:var(--primary);}
textarea.code-area.error{border-color:var(--danger);}
.output-area{width:100%;min-height:400px;padding:16px;background:#0f172a;color:#e2e8f0;font-family:'Courier New',Consolas,monospace;font-size:0.88rem;line-height:1.6;border:1.5px solid var(--border);border-radius:12px;overflow:auto;white-space:pre;}
.status-bar{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;margin-bottom:12px;font-size:0.85rem;font-weight:600;}
.status-valid{background:#f0fdf4;color:var(--success);border:1px solid #bbf7d0;}
.status-error{background:#fef2f2;color:var(--danger);border:1px solid #fecaca;}
.status-idle{background:var(--bg);color:var(--muted);border:1px solid var(--border);}
[data-theme="dark"] .status-valid{background:#052e16;}.
[data-theme="dark"] .status-error{background:#450a0a;}
[data-theme="dark"] .status-idle{background:var(--card);}
.tree-view{min-height:400px;padding:16px;background:#0f172a;border-radius:12px;border:1.5px solid var(--border);overflow:auto;font-family:'Courier New',monospace;font-size:0.85rem;line-height:1.7;}
.tree-key{color:#7dd3fc;}
.tree-string{color:#86efac;}
.tree-number{color:#fcd34d;}
.tree-bool{color:#f9a8d4;}
.tree-null{color:#94a3b8;}
.tree-toggle{cursor:pointer;user-select:none;}
.tree-toggle:hover{opacity:0.7;}
.tree-collapsed{display:none;}
.sample-bar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;}
.sample-btn{font-size:0.78rem;padding:5px 12px;background:#e0f2fe;color:var(--primary);border:none;border-radius:6px;cursor:pointer;font-weight:600;}
.sample-btn:hover{background:#bae6fd;}
.view-tabs{display:flex;gap:6px;margin-bottom:12px;}
.view-tab{padding:6px 14px;border-radius:6px;border:1px solid var(--border);background:var(--bg);font-size:0.82rem;font-weight:600;cursor:pointer;color:var(--muted);}
.view-tab.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.stats-row{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:12px;}
.stat-chip{background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:6px 12px;font-size:0.8rem;}
.stat-chip strong{color:var(--primary);}
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

<div class="jsoniq">
  <div class="hero">
    <div class="hero-badge">{ } JSONIQ</div>
    <h1>JSON Formatter</h1>
    <p>Format, validate, minify, and explore JSON with syntax highlighting and collapsible tree view.</p>
  </div>

  <div class="toolbar">
    <div style="display:flex;gap:8px;flex-wrap:wrap;">
      <button class="btn btn-primary" onclick="formatJSON()">✨ Format</button>
      <button class="btn btn-ghost" onclick="minifyJSON()">📦 Minify</button>
      <button class="btn btn-ghost" onclick="validateJSON()">✅ Validate</button>
      <button class="btn btn-ghost" onclick="clearAll()">↺ Clear</button>
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;">
      <button class="btn btn-ghost" onclick="copyOutput()">📋 Copy</button>
      <button class="btn btn-ghost" onclick="downloadJSON()">⬇️ Download</button>
      <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Theme</button>
    </div>
  </div>

  <div id="status-bar" class="status-bar status-idle">📄 Paste or type JSON to get started</div>

  <div class="stats-row" id="stats-row" style="display:none;">
    <div class="stat-chip">Keys: <strong id="st-keys">0</strong></div>
    <div class="stat-chip">Depth: <strong id="st-depth">0</strong></div>
    <div class="stat-chip">Size: <strong id="st-size">0 B</strong></div>
    <div class="stat-chip">Arrays: <strong id="st-arrays">0</strong></div>
    <div class="stat-chip">Objects: <strong id="st-objects">0</strong></div>
  </div>

  <div class="card">
    <div class="sample-bar">
      <span style="font-size:0.78rem;color:var(--muted);align-self:center;">Sample:</span>
      <button class="sample-btn" onclick="loadSample('simple')">Simple Object</button>
      <button class="sample-btn" onclick="loadSample('array')">Array</button>
      <button class="sample-btn" onclick="loadSample('nested')">Nested</button>
      <button class="sample-btn" onclick="loadSample('api')">API Response</button>
    </div>
    <div class="editor-layout">
      <div>
        <div class="panel-header">
          <span class="panel-title">Input JSON</span>
          <button class="btn btn-ghost" style="font-size:0.78rem;padding:4px 10px;" onclick="pasteFromClipboard()">📋 Paste</button>
        </div>
        <textarea class="code-area" id="input-json" placeholder='{"key": "value"}' oninput="onInput()" spellcheck="false"></textarea>
      </div>
      <div>
        <div class="panel-header">
          <span class="panel-title">Output</span>
          <div class="view-tabs">
            <button class="view-tab active" onclick="setView('formatted',this)">Formatted</button>
            <button class="view-tab" onclick="setView('tree',this)">Tree</button>
          </div>
        </div>
        <div id="formatted-view">
          <pre class="output-area" id="output-json"></pre>
        </div>
        <div id="tree-view-panel" class="hidden">
          <div class="tree-view" id="tree-view"></div>
        </div>
      </div>
    </div>
  </div>

  <div class="seo-block">
    <h2>About JSONIQ JSON Formatter</h2>
    <p>JSON (JavaScript Object Notation) is the most widely used data interchange format on the web. JSONIQ provides a comprehensive toolkit for working with JSON — formatting raw or minified JSON for readability, validating syntax, minifying for production use, and exploring complex structures through an interactive tree view.</p>
    <h3>What is JSON?</h3>
    <p>JSON is a lightweight text-based format for structured data exchange. It supports six data types: strings, numbers, booleans, null, objects (key-value pairs), and arrays. JSON is language-independent and used by virtually every REST API, configuration file, and data storage system.</p>
    <h3>Common JSON Errors</h3>
    <ul>
      <li>Missing or extra comma (trailing commas are not allowed in strict JSON)</li>
      <li>Unquoted keys (all keys must be double-quoted strings)</li>
      <li>Single quotes instead of double quotes for strings</li>
      <li>Comments in JSON (not supported — use JSON5 instead)</li>
      <li>Undefined or NaN values (not valid JSON values)</li>
    </ul>
    <h3>When to Minify JSON</h3>
    <p>Minified JSON removes all whitespace and newlines, reducing file size. This is ideal for API responses, configuration files in production, and embedded data in web pages. For human-readable config files and development, always use formatted JSON.</p>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">What is the difference between JSON and JavaScript objects? <span>+</span></div>
      <div class="faq-a hidden">JSON is a strict text format — all keys must be quoted strings, and only specific value types are allowed. JavaScript objects are more flexible and can contain functions, undefined values, and unquoted keys. JSON is a subset of JavaScript object notation.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">Can I use this tool for large JSON files? <span>+</span></div>
      <div class="faq-a hidden">JSONIQ processes JSON entirely in your browser using JavaScript. For most use cases (up to ~5MB of JSON), it works well. Very large files may be slow due to browser memory limitations. For production parsing of very large JSON, consider streaming parsers.</div>
    </div>
    <div class="related-grid">
      <a href="/tools/base64/" class="related-card"><div class="rc-emoji">🔢</div><div class="rc-name">Base64 Encoder</div></a>
      <a href="/tools/markdown-converter/" class="related-card"><div class="rc-emoji">📄</div><div class="rc-name">Markdown Converter</div></a>
      <a href="/tools/password-generator/" class="related-card"><div class="rc-emoji">🔐</div><div class="rc-name">Password Generator</div></a>
      <a href="/tools/word-counter/" class="related-card"><div class="rc-emoji">📝</div><div class="rc-name">Word Counter</div></a>
    </div>
  </div>
</div>

<script>
const SAMPLES = {
  simple: '{\n  "name": "JSONIQ",\n  "version": "1.0",\n  "author": "rkoots",\n  "active": true,\n  "score": 98.5\n}',
  array: '[\n  {"id": 1, "city": "Mumbai", "country": "India"},\n  {"id": 2, "city": "New York", "country": "USA"},\n  {"id": 3, "city": "London", "country": "UK"}\n]',
  nested: '{\n  "user": {\n    "id": 101,\n    "name": "Rahul Kumar",\n    "address": {\n      "street": "MG Road",\n      "city": "Bangalore",\n      "pin": "560001"\n    },\n    "tags": ["developer", "blogger", "trader"]\n  }\n}',
  api: '{\n  "status": "success",\n  "data": {\n    "items": [\n      {"id": "a1", "title": "Item One", "price": 99.99, "inStock": true},\n      {"id": "a2", "title": "Item Two", "price": 149.99, "inStock": false}\n    ],\n    "total": 2,\n    "page": 1\n  },\n  "meta": {"timestamp": "2026-03-06T12:00:00Z", "version": "2.1"}\n}'
};

let currentView = 'formatted';
let parsedData = null;

function loadSample(type) { document.getElementById('input-json').value = SAMPLES[type]; onInput(); formatJSON(); }

function onInput() {
  const raw = document.getElementById('input-json').value.trim();
  if (!raw) { setStatus('idle', '📄 Paste or type JSON to get started'); document.getElementById('stats-row').style.display='none'; return; }
  try {
    parsedData = JSON.parse(raw);
    setStatus('valid', '✅ Valid JSON');
    updateStats(raw, parsedData);
    document.getElementById('input-json').classList.remove('error');
    if (currentView === 'tree') renderTree();
  } catch(e) {
    parsedData = null;
    setStatus('error', '❌ ' + e.message);
    document.getElementById('input-json').classList.add('error');
    document.getElementById('stats-row').style.display='none';
  }
}

function formatJSON() {
  const raw = document.getElementById('input-json').value.trim();
  if (!raw) return;
  try {
    const obj = JSON.parse(raw);
    const formatted = JSON.stringify(obj, null, 2);
    document.getElementById('output-json').textContent = formatted;
    document.getElementById('input-json').value = formatted;
    document.getElementById('input-json').classList.remove('error');
    parsedData = obj;
    setStatus('valid', '✅ Formatted successfully');
    updateStats(formatted, obj);
    if (currentView === 'tree') renderTree();
  } catch(e) { setStatus('error', '❌ ' + e.message); }
}

function minifyJSON() {
  const raw = document.getElementById('input-json').value.trim();
  if (!raw) return;
  try {
    const obj = JSON.parse(raw);
    const minified = JSON.stringify(obj);
    document.getElementById('output-json').textContent = minified;
    setStatus('valid', `✅ Minified — ${formatBytes(minified.length)} (saved ${formatBytes(raw.length - minified.length)})`);
  } catch(e) { setStatus('error', '❌ ' + e.message); }
}

function validateJSON() {
  const raw = document.getElementById('input-json').value.trim();
  if (!raw) { setStatus('idle', '📄 Nothing to validate'); return; }
  try { JSON.parse(raw); setStatus('valid', '✅ Valid JSON — no errors found'); }
  catch(e) { setStatus('error', '❌ Invalid JSON: ' + e.message); }
}

function setStatus(type, msg) {
  const el = document.getElementById('status-bar');
  el.className = 'status-bar status-' + type;
  el.textContent = msg;
}

function updateStats(raw, obj) {
  document.getElementById('stats-row').style.display = 'flex';
  document.getElementById('st-size').textContent = formatBytes(new Blob([raw]).size);
  document.getElementById('st-keys').textContent = countKeys(obj);
  document.getElementById('st-depth').textContent = getDepth(obj);
  document.getElementById('st-arrays').textContent = countType(obj, 'array');
  document.getElementById('st-objects').textContent = countType(obj, 'object');
}

function countKeys(obj) {
  if (obj === null || typeof obj !== 'object') return 0;
  let count = Array.isArray(obj) ? 0 : Object.keys(obj).length;
  for (const v of Object.values(obj)) count += countKeys(v);
  return count;
}

function getDepth(obj, d=0) {
  if (obj === null || typeof obj !== 'object') return d;
  return Math.max(d+1, ...Object.values(obj).map(v => getDepth(v, d+1)));
}

function countType(obj, type) {
  if (obj === null) return 0;
  let c = 0;
  if (type === 'array' && Array.isArray(obj)) c = 1;
  else if (type === 'object' && !Array.isArray(obj) && typeof obj === 'object') c = 1;
  if (typeof obj === 'object') for (const v of Object.values(obj)) c += countType(v, type);
  return c;
}

function setView(view, btn) {
  currentView = view;
  document.querySelectorAll('.view-tab').forEach(t => t.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('formatted-view').classList.toggle('hidden', view !== 'formatted');
  document.getElementById('tree-view-panel').classList.toggle('hidden', view !== 'tree');
  if (view === 'tree' && parsedData !== null) renderTree();
}

function renderTree() {
  const el = document.getElementById('tree-view');
  el.innerHTML = buildTree(parsedData, 0);
}

function buildTree(val, depth) {
  if (val === null) return `<span class="tree-null">null</span>`;
  if (typeof val === 'boolean') return `<span class="tree-bool">${val}</span>`;
  if (typeof val === 'number') return `<span class="tree-number">${val}</span>`;
  if (typeof val === 'string') return `<span class="tree-string">"${escHtml(val)}"</span>`;
  if (Array.isArray(val)) {
    if (!val.length) return `<span style="color:#94a3b8">[]</span>`;
    const id = 'node_' + Math.random().toString(36).slice(2);
    const items = val.map((v,i) => `<div style="padding-left:20px"><span style="color:#6b7280">[${i}]: </span>${buildTree(v, depth+1)}</div>`).join('');
    return `<span class="tree-toggle" onclick="toggleNode('${id}')">▾</span> <span style="color:#94a3b8">[${val.length}]</span><div id="${id}">${items}</div>`;
  }
  const entries = Object.entries(val);
  if (!entries.length) return `<span style="color:#94a3b8">{}</span>`;
  const id = 'node_' + Math.random().toString(36).slice(2);
  const items = entries.map(([k,v]) => `<div style="padding-left:20px"><span class="tree-key">"${escHtml(k)}"</span><span style="color:#94a3b8">: </span>${buildTree(v, depth+1)}</div>`).join('');
  return `<span class="tree-toggle" onclick="toggleNode('${id}')">▾</span> <span style="color:#94a3b8">{${entries.length}}</span><div id="${id}">${items}</div>`;
}

function toggleNode(id) {
  const el = document.getElementById(id);
  if (!el) return;
  el.classList.toggle('tree-collapsed');
  const btn = el.previousElementSibling.previousElementSibling;
  if (btn) btn.textContent = el.classList.contains('tree-collapsed') ? '▸' : '▾';
}

function escHtml(s) { return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function formatBytes(b) { if (b<1024) return b+' B'; if (b<1048576) return (b/1024).toFixed(1)+' KB'; return (b/1048576).toFixed(2)+' MB'; }

function copyOutput() {
  const text = document.getElementById('output-json').textContent;
  if (text) navigator.clipboard.writeText(text).then(()=>alert('Copied!'));
}

function downloadJSON() {
  const text = document.getElementById('output-json').textContent;
  if (!text) return;
  const blob = new Blob([text], {type:'application/json'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'jsoniq-output.json'; a.click();
}

async function pasteFromClipboard() {
  try { const text = await navigator.clipboard.readText(); document.getElementById('input-json').value = text; onInput(); }
  catch(e) { alert('Clipboard access denied. Please paste manually.'); }
}

function clearAll() {
  document.getElementById('input-json').value = '';
  document.getElementById('output-json').textContent = '';
  document.getElementById('tree-view').innerHTML = '';
  document.getElementById('input-json').classList.remove('error');
  parsedData = null;
  setStatus('idle', '📄 Paste or type JSON to get started');
  document.getElementById('stats-row').style.display = 'none';
}

function toggleTheme() { const d=document.documentElement; d.setAttribute('data-theme',d.getAttribute('data-theme')==='dark'?'light':'dark'); }
function toggleFaq(el) { const a=el.nextElementSibling; const s=el.querySelector('span'); a.classList.toggle('hidden'); s.textContent=a.classList.contains('hidden')?'+':'−'; }
loadSample('nested');
</script>
