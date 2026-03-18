---
layout: default
title: "UUIDGEN – UUID Generator | Free Online UUID v1 v4 v5 Bulk Generator Tool"
excerpt: "Generate RFC 4122 compliant UUIDs instantly with UUIDGEN. Create UUID v4 (random), v1 (time-based), or bulk generate up to 1000 UUIDs. Free online UUID generator with copy and export."
date: 2026-03-18
categories: tools
permalink: /tools/uuid-generator/
description: "Free online UUID generator. Generate UUID v4 (random), v1 (time-based) UUIDs in bulk. Copy single or all, export as JSON or TXT. Fully client-side UUID creation tool."
keywords: ["uuid generator online", "generate uuid v4", "random uuid generator", "uuid v1 generator", "bulk uuid generator", "guid generator online", "unique id generator free", "uuid creator tool", "rfc 4122 uuid"]
tags: [UUID, generator, developer, utility, identity]
---

<style>
:root{--primary:#0891b2;--primary-dark:#0e7490;--accent:#f59e0b;--success:#10b981;--bg:#ecfeff;--card:#fff;--text:#083344;--muted:#6b7280;--border:#a5f3fc;--shadow:0 8px 32px rgba(8,145,178,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.uuidgen{max-width:900px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:16px;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:10px 20px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-success{background:var(--success);color:#fff;}
.btn-success:hover{filter:brightness(1.1);}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);}
select.opt,input.num-input{padding:9px 12px;border-radius:8px;border:1px solid var(--border);background:var(--card);color:var(--text);font-size:0.9rem;}
input.num-input{width:90px;}
.single-uuid{display:flex;align-items:center;gap:10px;background:#ecfeff;border:2px solid var(--border);border-radius:10px;padding:14px 16px;margin-bottom:16px;}
.uuid-display{flex:1;font-family:Consolas,'Courier New',monospace;font-size:1.05rem;font-weight:600;color:var(--text);word-break:break-all;}
.copy-btn{padding:7px 14px;border-radius:8px;border:1px solid var(--border);background:var(--card);color:var(--primary);cursor:pointer;font-size:0.85rem;font-weight:600;white-space:nowrap;}
.copy-btn:hover{background:var(--primary);color:#fff;}
.uuid-list{display:flex;flex-direction:column;gap:6px;max-height:400px;overflow:auto;}
.uuid-row{display:flex;align-items:center;gap:10px;padding:8px 12px;background:#ecfeff;border-radius:8px;border:1px solid var(--border);}
.uuid-num{width:32px;text-align:right;font-size:0.78rem;color:var(--muted);font-weight:600;flex-shrink:0;}
.uuid-val{flex:1;font-family:Consolas,'Courier New',monospace;font-size:0.88rem;word-break:break-all;}
.copy-small{padding:4px 10px;border-radius:6px;border:1px solid var(--border);background:var(--card);color:var(--primary);cursor:pointer;font-size:0.78rem;white-space:nowrap;}
.copy-small:hover{background:var(--primary);color:#fff;}
.format-chips{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;}
.fmt-chip{padding:5px 14px;border-radius:20px;border:1px solid var(--border);font-size:0.82rem;font-weight:600;cursor:pointer;transition:all 0.2s;}
.fmt-chip.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.info-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:4px;}
.info-box{padding:14px;background:linear-gradient(135deg,#ecfeff,#f0fdfa);border-radius:10px;border:1px solid var(--border);}
.info-box h3{font-size:0.9rem;color:var(--primary-dark);margin-bottom:6px;}
.info-box p{font-size:0.82rem;color:var(--muted);}
</style>

<div class="uuidgen">
  <header class="hero">
    <div class="hero-badge">FREE UUID GENERATOR</div>
    <h1>UUIDGEN – UUID Generator</h1>
    <p>Generate RFC 4122 compliant UUIDs in bulk. UUID v4 random or v1 time-based — copy, export as JSON/TXT, choose format instantly.</p>
  </header>

  <div class="card">
    <div style="font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Single UUID</div>
    <div class="single-uuid">
      <span class="uuid-display" id="singleUUID">—</span>
      <button class="copy-btn" onclick="copySingle()">Copy</button>
      <button class="copy-btn" onclick="generateSingle()">Refresh</button>
    </div>

    <div style="font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Bulk Generator</div>
    <div class="controls">
      <input class="num-input" id="countInput" type="number" min="1" max="1000" value="10" />
      <select class="opt" id="versionSelect">
        <option value="v4">UUID v4 (random)</option>
        <option value="v1">UUID v1 (time-based)</option>
        <option value="v4-no-hyphens">v4 No Hyphens</option>
        <option value="v4-upper">v4 Uppercase</option>
        <option value="short">Short UUID (22 chars)</option>
      </select>
      <button class="btn btn-primary" onclick="generateBulk()">Generate</button>
      <button class="btn btn-success" onclick="downloadUUIDs()">Download TXT</button>
      <button class="btn btn-ghost" onclick="copyAll()">Copy All</button>
      <button class="btn btn-ghost" onclick="clearBulk()">Clear</button>
    </div>

    <div class="format-chips">
      <span style="font-size:0.82rem;color:var(--muted);align-self:center;">Format:</span>
      <span class="fmt-chip active" onclick="setFmt('default',this)">Standard</span>
      <span class="fmt-chip" onclick="setFmt('braces',this)">{braces}</span>
      <span class="fmt-chip" onclick="setFmt('urn',this)">URN</span>
      <span class="fmt-chip" onclick="setFmt('json',this)">JSON array</span>
    </div>

    <div id="bulkList" class="uuid-list"></div>
  </div>

  <div class="info-grid">
    <div class="info-box"><h3>UUID v4 (Random)</h3><p>122 random bits with RFC 4122 variant bits. The most common UUID format — ideal for database primary keys.</p></div>
    <div class="info-box"><h3>UUID v1 (Time-based)</h3><p>Contains a timestamp and node identifier. Sortable by creation time but exposes machine info.</p></div>
    <div class="info-box"><h3>GUID vs UUID</h3><p>GUID (Globally Unique Identifier) is Microsoft's implementation of the UUID standard. They are functionally identical.</p></div>
    <div class="info-box"><h3>Uniqueness Guarantee</h3><p>UUID v4 has a collision probability of 1 in 2¹²² — effectively impossible to collide in practice.</p></div>
  </div>
</div>

<script>
let uuids = [];
let fmt = 'default';

function setFmt(f, el) {
  fmt = f;
  document.querySelectorAll('.fmt-chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  if (uuids.length) renderList();
}

function uuidV4() {
  if (crypto.randomUUID) return crypto.randomUUID();
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
    const r = Math.random()*16|0, v = c==='x' ? r : (r&0x3|0x8);
    return v.toString(16);
  });
}

function uuidV1Like() {
  const now = Date.now();
  const ts = now.toString(16).padStart(12,'0');
  const rand = Math.random().toString(16).slice(2,10);
  const rand2 = Math.random().toString(16).slice(2,14);
  return `${ts.slice(0,8)}-${ts.slice(8,12)}-1${rand.slice(0,3)}-${(Math.random()*4|8).toString(16)}${rand.slice(3,6)}-${rand2}`;
}

function generateOne(ver) {
  let u = ver === 'v1' ? uuidV1Like() : uuidV4();
  if (ver === 'v4-no-hyphens') u = uuidV4().replace(/-/g,'');
  if (ver === 'v4-upper') u = uuidV4().toUpperCase();
  if (ver === 'short') {
    const bytes = uuidV4().replace(/-/g,'');
    u = btoa(String.fromCharCode(...bytes.match(/.{2}/g).map(h=>parseInt(h,16)))).replace(/\+/g,'-').replace(/\//g,'_').replace(/=/g,'').slice(0,22);
  }
  return u;
}

function applyFmt(u) {
  if (fmt === 'braces') return '{' + u + '}';
  if (fmt === 'urn') return 'urn:uuid:' + u;
  return u;
}

function generateSingle() {
  const ver = document.getElementById('versionSelect').value;
  const u = generateOne(ver);
  document.getElementById('singleUUID').textContent = applyFmt(u);
}

function copySingle() {
  const val = document.getElementById('singleUUID').textContent;
  navigator.clipboard.writeText(val).then(() => alert('UUID copied!'));
}

function generateBulk() {
  const count = Math.min(1000, Math.max(1, parseInt(document.getElementById('countInput').value) || 10));
  const ver = document.getElementById('versionSelect').value;
  uuids = Array.from({length:count}, () => generateOne(ver));
  generateSingle();
  renderList();
}

function renderList() {
  if (!uuids.length) return;
  if (fmt === 'json') {
    const arr = JSON.stringify(uuids.map(applyFmt), null, 2);
    document.getElementById('bulkList').innerHTML = `<pre style="font-family:Consolas,monospace;font-size:0.83rem;background:#ecfeff;padding:12px;border-radius:8px;max-height:380px;overflow:auto;white-space:pre-wrap;">${arr}</pre>`;
    return;
  }
  let html = '';
  uuids.forEach((u, i) => {
    const display = applyFmt(u);
    html += `<div class="uuid-row">
      <span class="uuid-num">${i+1}</span>
      <span class="uuid-val">${display}</span>
      <button class="copy-small" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent).then(()=>{this.textContent='✓';setTimeout(()=>this.textContent='Copy',1000)})">Copy</button>
    </div>`;
  });
  document.getElementById('bulkList').innerHTML = html;
}

function copyAll() {
  if (!uuids.length) return alert('Generate UUIDs first');
  const text = uuids.map(applyFmt).join('\n');
  navigator.clipboard.writeText(text).then(() => alert(`${uuids.length} UUIDs copied!`));
}

function downloadUUIDs() {
  if (!uuids.length) return alert('Generate UUIDs first');
  const text = uuids.map(applyFmt).join('\n');
  const blob = new Blob([text], {type:'text/plain'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'uuids.txt';
  a.click();
}

function clearBulk() {
  uuids = [];
  document.getElementById('bulkList').innerHTML = '';
}

generateSingle();
generateBulk();
</script>
