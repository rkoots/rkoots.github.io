---
layout: default
title: "ENCODIQ – URL Encoder & Decoder | Free Online Percent Encoding & Decoding Tool"
excerpt: "Encode and decode URLs, query strings, and special characters instantly with ENCODIQ. Supports percent encoding, Base64, HTML entities, and query parameter parsing. Free online tool."
date: 2026-03-18
categories: tools
permalink: /tools/url-encoder/
description: "Free online URL encoder and decoder. Encode/decode URLs, query strings, Base64, and HTML entities. Parse and build query parameters with instant results. 100% client-side."
keywords: ["url encoder online", "url decoder free", "percent encoding tool", "encode url online", "decode url string", "query string encoder", "uri encoder decoder", "base64 url encode", "html entity encoder"]
tags: [URL, encoder, developer, utility, web]
---

<style>
:root{--primary:#0284c7;--primary-dark:#0369a1;--accent:#f59e0b;--success:#10b981;--bg:#f0f9ff;--card:#fff;--text:#0c4a6e;--muted:#6b7280;--border:#bae6fd;--shadow:0 8px 32px rgba(2,132,199,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.encodiq{max-width:960px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.tabs{display:flex;gap:4px;border-bottom:2px solid var(--border);margin-bottom:16px;flex-wrap:wrap;}
.tab{padding:8px 16px;border:none;background:none;color:var(--muted);font-size:0.88rem;font-weight:700;cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px;}
.tab.active{color:var(--primary);border-bottom-color:var(--primary);}
.btn{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-success{background:var(--success);color:#fff;}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);}
.toolbar{display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap;}
textarea{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.88rem;background:var(--card);color:var(--text);resize:vertical;line-height:1.5;}
textarea:focus{outline:none;border-color:var(--primary);}
.output-box{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.88rem;background:#f0f9ff;white-space:pre-wrap;word-break:break-all;min-height:100px;max-height:300px;overflow:auto;}
.editors{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.editor-label{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;}
.swap-btn{display:flex;justify-content:center;align-items:center;padding:6px 12px;border:1px solid var(--border);border-radius:8px;background:var(--card);color:var(--primary);cursor:pointer;font-size:1.1rem;}
.swap-btn:hover{background:var(--primary);color:#fff;}
.qp-table{width:100%;border-collapse:collapse;font-size:0.85rem;}
.qp-table th{background:#e0f2fe;color:var(--primary-dark);padding:8px 12px;border:1px solid var(--border);font-weight:700;text-align:left;}
.qp-table td{padding:8px 12px;border:1px solid var(--border);font-family:Consolas,monospace;}
.qp-table tr:nth-child(even) td{background:#f0f9ff;}
.url-input{width:100%;padding:12px 16px;border:2px solid var(--border);border-radius:10px;font-family:Consolas,'Courier New',monospace;font-size:0.9rem;background:var(--card);color:var(--text);}
.url-input:focus{outline:none;border-color:var(--primary);}
.url-parts{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin-top:12px;}
.url-part{padding:10px 12px;background:#e0f2fe;border-radius:8px;border:1px solid var(--border);}
.url-part-label{font-size:0.72rem;font-weight:700;color:var(--primary-dark);text-transform:uppercase;margin-bottom:4px;}
.url-part-val{font-family:Consolas,monospace;font-size:0.85rem;word-break:break-all;}
@media(max-width:650px){.editors{grid-template-columns:1fr;}}
</style>

<div class="encodiq">
  <header class="hero">
    <div class="hero-badge">FREE URL TOOL</div>
    <h1>ENCODIQ – URL Encoder & Decoder</h1>
    <p>Encode, decode, and parse URLs instantly. Supports percent-encoding, Base64 URL, HTML entities, and query parameter breakdown.</p>
  </header>

  <div class="card">
    <div class="tabs">
      <button class="tab active" onclick="switchTab('url',this)">URL Encode/Decode</button>
      <button class="tab" onclick="switchTab('base64',this)">Base64</button>
      <button class="tab" onclick="switchTab('html',this)">HTML Entities</button>
      <button class="tab" onclick="switchTab('parse',this)">URL Parser</button>
      <button class="tab" onclick="switchTab('qp',this)">Query Params</button>
    </div>

    <div id="tab-url">
      <div class="toolbar">
        <button class="btn btn-primary" onclick="encodeURL()">Encode</button>
        <button class="btn btn-ghost" onclick="decodeURL()">Decode</button>
        <button class="btn btn-success" onclick="copyURL()">Copy Output</button>
        <button class="btn btn-ghost" onclick="clearURL()">Clear</button>
        <label style="font-size:0.85rem;color:var(--muted);display:flex;align-items:center;gap:6px;">
          <input type="checkbox" id="encodeAll"> Encode all chars
        </label>
      </div>
      <div class="editors">
        <div>
          <div class="editor-label">Input</div>
          <textarea id="urlInput" rows="5" placeholder="Enter URL or text to encode/decode…"></textarea>
        </div>
        <div>
          <div class="editor-label">Output</div>
          <div class="output-box" id="urlOutput">Result will appear here…</div>
        </div>
      </div>
    </div>

    <div id="tab-base64" style="display:none;">
      <div class="toolbar">
        <button class="btn btn-primary" onclick="encodeB64()">Encode to Base64</button>
        <button class="btn btn-ghost" onclick="decodeB64()">Decode from Base64</button>
        <button class="btn btn-success" onclick="copyB64()">Copy Output</button>
        <button class="btn btn-ghost" onclick="clearB64()">Clear</button>
        <label style="font-size:0.85rem;color:var(--muted);display:flex;align-items:center;gap:6px;">
          <input type="checkbox" id="urlSafeB64"> URL-safe (- and _)
        </label>
      </div>
      <div class="editors">
        <div>
          <div class="editor-label">Input</div>
          <textarea id="b64Input" rows="5" placeholder="Enter text to encode or Base64 to decode…"></textarea>
        </div>
        <div>
          <div class="editor-label">Output</div>
          <div class="output-box" id="b64Output">Result will appear here…</div>
        </div>
      </div>
    </div>

    <div id="tab-html" style="display:none;">
      <div class="toolbar">
        <button class="btn btn-primary" onclick="encodeHTML()">Encode HTML Entities</button>
        <button class="btn btn-ghost" onclick="decodeHTML()">Decode HTML Entities</button>
        <button class="btn btn-success" onclick="copyHTML()">Copy Output</button>
      </div>
      <div class="editors">
        <div>
          <div class="editor-label">Input</div>
          <textarea id="htmlInput" rows="5" placeholder='Enter HTML like <div class="test"> or &amp; entities…'></textarea>
        </div>
        <div>
          <div class="editor-label">Output</div>
          <div class="output-box" id="htmlOutput">Result will appear here…</div>
        </div>
      </div>
    </div>

    <div id="tab-parse" style="display:none;">
      <div class="toolbar">
        <button class="btn btn-primary" onclick="parseURL()">Parse URL</button>
        <button class="btn btn-ghost" onclick="clearParse()">Clear</button>
      </div>
      <input class="url-input" id="parseInput" type="text" placeholder="https://api.example.com:8080/users/search?q=hello&page=2#results" />
      <div class="url-parts" id="urlParts" style="margin-top:12px;display:none;"></div>
    </div>

    <div id="tab-qp" style="display:none;">
      <div class="toolbar">
        <button class="btn btn-primary" onclick="parseQP()">Parse Query String</button>
        <button class="btn btn-ghost" onclick="buildQP()">Build Query String</button>
        <button class="btn btn-ghost" onclick="clearQP()">Clear</button>
      </div>
      <textarea id="qpInput" rows="3" placeholder="?key=value&name=Alice&city=New+York or full URL"></textarea>
      <div id="qpResult" style="margin-top:12px;display:none;"></div>
    </div>
  </div>
</div>

<script>
function switchTab(name, el) {
  ['url','base64','html','parse','qp'].forEach(t => document.getElementById('tab-' + t).style.display = 'none');
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById('tab-' + name).style.display = 'block';
  el.classList.add('active');
}

// URL encode/decode
function encodeURL() {
  const val = document.getElementById('urlInput').value;
  const all = document.getElementById('encodeAll').checked;
  const result = all ? encodeURIComponent(val) : encodeURI(val);
  document.getElementById('urlOutput').textContent = result;
}
function decodeURL() {
  const val = document.getElementById('urlInput').value;
  try { document.getElementById('urlOutput').textContent = decodeURIComponent(val.replace(/\+/g, ' ')); }
  catch(e) { document.getElementById('urlOutput').textContent = 'Error: ' + e.message; }
}
function copyURL() { navigator.clipboard.writeText(document.getElementById('urlOutput').textContent).then(() => alert('Copied!')); }
function clearURL() { document.getElementById('urlInput').value = ''; document.getElementById('urlOutput').textContent = 'Result will appear here…'; }

// Base64
function encodeB64() {
  try {
    let result = btoa(unescape(encodeURIComponent(document.getElementById('b64Input').value)));
    if (document.getElementById('urlSafeB64').checked) result = result.replace(/\+/g,'-').replace(/\//g,'_').replace(/=/g,'');
    document.getElementById('b64Output').textContent = result;
  } catch(e) { document.getElementById('b64Output').textContent = 'Error: ' + e.message; }
}
function decodeB64() {
  try {
    let val = document.getElementById('b64Input').value.replace(/-/g,'+').replace(/_/g,'/');
    while (val.length % 4) val += '=';
    document.getElementById('b64Output').textContent = decodeURIComponent(escape(atob(val)));
  } catch(e) { document.getElementById('b64Output').textContent = 'Error: invalid Base64 — ' + e.message; }
}
function copyB64() { navigator.clipboard.writeText(document.getElementById('b64Output').textContent).then(() => alert('Copied!')); }
function clearB64() { document.getElementById('b64Input').value=''; document.getElementById('b64Output').textContent='Result will appear here…'; }

// HTML entities
function encodeHTML() {
  const val = document.getElementById('htmlInput').value;
  const result = val.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  document.getElementById('htmlOutput').textContent = result;
}
function decodeHTML() {
  const val = document.getElementById('htmlInput').value;
  const el = document.createElement('textarea');
  el.innerHTML = val;
  document.getElementById('htmlOutput').textContent = el.value;
}
function copyHTML() { navigator.clipboard.writeText(document.getElementById('htmlOutput').textContent).then(() => alert('Copied!')); }

// URL parser
function parseURL() {
  const raw = document.getElementById('parseInput').value.trim();
  if (!raw) return;
  try {
    const url = new URL(raw.includes('://') ? raw : 'https://' + raw);
    const parts = [
      {label:'Protocol', val: url.protocol},
      {label:'Hostname', val: url.hostname},
      {label:'Port', val: url.port || '(default)'},
      {label:'Path', val: url.pathname},
      {label:'Query String', val: url.search || '(none)'},
      {label:'Fragment / Hash', val: url.hash || '(none)'},
      {label:'Origin', val: url.origin},
      {label:'Full URL', val: url.href}
    ];
    document.getElementById('urlParts').innerHTML = parts.map(p =>
      `<div class="url-part"><div class="url-part-label">${p.label}</div><div class="url-part-val">${escHtml(p.val)}</div></div>`
    ).join('');
    document.getElementById('urlParts').style.display = 'grid';
  } catch(e) {
    document.getElementById('urlParts').innerHTML = `<div style="color:#dc2626;padding:10px;">Invalid URL: ${e.message}</div>`;
    document.getElementById('urlParts').style.display = 'block';
  }
}
function clearParse() { document.getElementById('parseInput').value=''; document.getElementById('urlParts').style.display='none'; }

// Query params
function parseQP() {
  let val = document.getElementById('qpInput').value.trim();
  try {
    if (val.includes('://')) val = new URL(val).search;
    const params = new URLSearchParams(val.startsWith('?') ? val.slice(1) : val);
    let html = '<table class="qp-table"><thead><tr><th>Key</th><th>Value (decoded)</th></tr></thead><tbody>';
    let count = 0;
    params.forEach((v,k) => { html += `<tr><td>${escHtml(k)}</td><td>${escHtml(v)}</td></tr>`; count++; });
    html += `</tbody></table><div style="margin-top:8px;font-size:0.82rem;color:var(--muted);">${count} parameter${count!==1?'s':''}</div>`;
    document.getElementById('qpResult').innerHTML = html;
    document.getElementById('qpResult').style.display = 'block';
  } catch(e) {
    document.getElementById('qpResult').innerHTML = `<div style="color:#dc2626;">Error: ${e.message}</div>`;
    document.getElementById('qpResult').style.display = 'block';
  }
}
function buildQP() {
  const val = document.getElementById('qpInput').value.trim();
  try {
    const lines = val.split('\n').filter(l=>l.includes('='));
    const params = new URLSearchParams();
    lines.forEach(l => { const [k,...v] = l.split('='); if(k.trim()) params.append(k.trim(), v.join('=').trim()); });
    document.getElementById('qpResult').innerHTML = `<div class="output-box">?${params.toString()}</div>`;
    document.getElementById('qpResult').style.display = 'block';
  } catch(e) { alert(e.message); }
}
function clearQP() { document.getElementById('qpInput').value=''; document.getElementById('qpResult').style.display='none'; }

function escHtml(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

document.getElementById('parseInput').addEventListener('keydown', e => { if(e.key==='Enter') parseURL(); });
</script>
