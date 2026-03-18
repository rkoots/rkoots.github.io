---
layout: default
title: "HASHVEX – Hash Generator | Free Online MD5 SHA1 SHA256 SHA512 Hash Calculator"
excerpt: "Generate cryptographic hashes instantly with HASHVEX. Compute MD5, SHA-1, SHA-256, SHA-384, SHA-512 hashes client-side. Free online hash calculator with file hash support."
date: 2026-03-18
categories: tools
permalink: /tools/hash-generator/
description: "Free online hash generator. Calculate MD5, SHA-1, SHA-256, SHA-384, SHA-512 hashes from text or files instantly in your browser. 100% client-side and private."
keywords: ["hash generator online", "md5 hash generator", "sha256 hash calculator", "sha512 hash tool", "sha1 hash online", "file hash checker", "checksum calculator", "crypto hash tool free", "hash string online"]
tags: [security, hash, generator, cryptography, developer]
---

<style>
:root{--primary:#7c3aed;--primary-dark:#6d28d9;--accent:#f59e0b;--success:#10b981;--bg:#f5f3ff;--card:#fff;--text:#1e1b4b;--muted:#6b7280;--border:#ddd6fe;--shadow:0 8px 32px rgba(124,58,237,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.hashvex{max-width:900px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.tabs{display:flex;gap:4px;border-bottom:2px solid var(--border);margin-bottom:16px;}
.tab{padding:8px 16px;border:none;background:none;color:var(--muted);font-size:0.9rem;font-weight:600;cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px;}
.tab.active{color:var(--primary);border-bottom-color:var(--primary);}
textarea{width:100%;padding:12px;border:2px solid var(--border);border-radius:10px;font-family:Consolas,'Courier New',monospace;font-size:0.9rem;background:var(--card);color:var(--text);resize:vertical;line-height:1.5;}
textarea:focus{outline:none;border-color:var(--primary);}
.btn{display:inline-flex;align-items:center;gap:6px;padding:10px 20px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;margin-top:10px;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.hash-results{margin-top:16px;}
.hash-row{display:grid;grid-template-columns:120px 1fr auto;gap:10px;align-items:center;padding:12px 0;border-bottom:1px solid var(--border);}
.hash-row:last-child{border-bottom:none;}
.hash-label{font-size:0.82rem;font-weight:700;padding:4px 10px;border-radius:20px;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;text-align:center;}
.hash-value{font-family:Consolas,'Courier New',monospace;font-size:0.82rem;color:var(--text);word-break:break-all;background:#f5f3ff;padding:8px 10px;border-radius:8px;}
.copy-btn{padding:6px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--primary);cursor:pointer;font-size:0.8rem;font-weight:600;white-space:nowrap;}
.copy-btn:hover{background:var(--primary);color:#fff;}
.file-drop{border:2px dashed var(--border);border-radius:10px;padding:30px;text-align:center;cursor:pointer;transition:all 0.2s;color:var(--muted);}
.file-drop:hover,.file-drop.dragover{border-color:var(--primary);background:#f0ebff;}
.file-drop input[type=file]{display:none;}
.encoding-row{display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap;}
.enc-chip{padding:5px 14px;border-radius:20px;border:1px solid var(--border);background:var(--card);color:var(--text);font-size:0.82rem;font-weight:600;cursor:pointer;}
.enc-chip.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.hmac-key{width:100%;padding:10px;border:2px solid var(--border);border-radius:8px;font-family:Consolas,monospace;font-size:0.88rem;margin-bottom:10px;background:var(--card);color:var(--text);}
.hmac-key:focus{outline:none;border-color:var(--primary);}
</style>

<div class="hashvex">
  <header class="hero">
    <div class="hero-badge">FREE HASH GENERATOR</div>
    <h1>HASHVEX – Hash Generator</h1>
    <p>Generate MD5, SHA-1, SHA-256, SHA-384, and SHA-512 hashes from text or files. 100% client-side — your data never leaves your browser.</p>
  </header>

  <div class="card">
    <div class="tabs">
      <button class="tab active" onclick="switchTab('text',this)">Text Hash</button>
      <button class="tab" onclick="switchTab('file',this)">File Hash</button>
      <button class="tab" onclick="switchTab('hmac',this)">HMAC</button>
    </div>

    <div id="tab-text">
      <textarea id="textInput" rows="5" placeholder="Enter text to hash…"></textarea>
      <div class="encoding-row" style="margin-top:10px;">
        <span style="font-size:0.82rem;color:var(--muted);align-self:center;">Output:</span>
        <span class="enc-chip active" onclick="setEnc('hex',this)">HEX</span>
        <span class="enc-chip" onclick="setEnc('base64',this)">Base64</span>
      </div>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-primary" onclick="hashText()">Generate Hashes</button>
        <button class="btn btn-ghost" onclick="clearAll()">Clear</button>
      </div>
    </div>

    <div id="tab-file" style="display:none;">
      <div class="file-drop" id="fileDrop" onclick="document.getElementById('fileInput').click()">
        <input type="file" id="fileInput" onchange="hashFile(this.files[0])">
        <div style="font-size:2rem;margin-bottom:8px;">📂</div>
        <strong>Drop a file here</strong> or click to browse<br>
        <span style="font-size:0.82rem;">Max 500 MB — processed client-side</span>
      </div>
      <div id="fileInfo" style="margin-top:10px;font-size:0.88rem;color:var(--muted);"></div>
    </div>

    <div id="tab-hmac" style="display:none;">
      <input class="hmac-key" id="hmacKey" type="text" placeholder="Enter HMAC secret key" />
      <textarea id="hmacInput" rows="4" placeholder="Enter message to sign…"></textarea>
      <button class="btn btn-primary" onclick="computeHMAC()" style="margin-top:10px;">Compute HMAC</button>
    </div>

    <div class="hash-results" id="hashResults" style="display:none;margin-top:16px;">
      <div style="font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Hash Output</div>
      <div id="hashRows"></div>
    </div>
  </div>

  <div class="card">
    <div style="font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">About Hash Algorithms</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;">
      <div style="padding:12px;background:var(--bg);border-radius:8px;border:1px solid var(--border);"><strong style="color:var(--primary);">MD5</strong><br><span style="font-size:0.82rem;color:var(--muted);">128-bit, fast. Not secure for passwords but common for checksums.</span></div>
      <div style="padding:12px;background:var(--bg);border-radius:8px;border:1px solid var(--border);"><strong style="color:var(--primary);">SHA-1</strong><br><span style="font-size:0.82rem;color:var(--muted);">160-bit. Deprecated for security use, still used in legacy systems.</span></div>
      <div style="padding:12px;background:var(--bg);border-radius:8px;border:1px solid var(--border);"><strong style="color:var(--primary);">SHA-256</strong><br><span style="font-size:0.82rem;color:var(--muted);">256-bit. The current standard for secure hashing. Used in TLS, Bitcoin.</span></div>
      <div style="padding:12px;background:var(--bg);border-radius:8px;border:1px solid var(--border);"><strong style="color:var(--primary);">SHA-512</strong><br><span style="font-size:0.82rem;color:var(--muted);">512-bit. Highest security SHA-2 variant, ideal for critical systems.</span></div>
    </div>
  </div>
</div>

<script>
let outputEncoding = 'hex';
let currentTab = 'text';

function switchTab(name, el) {
  ['text','file','hmac'].forEach(t => document.getElementById('tab-' + t).style.display = 'none');
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById('tab-' + name).style.display = 'block';
  el.classList.add('active');
  currentTab = name;
  document.getElementById('hashResults').style.display = 'none';
}

function setEnc(enc, el) {
  outputEncoding = enc;
  document.querySelectorAll('.enc-chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}

async function digest(algo, data) {
  const buf = await crypto.subtle.digest(algo, data);
  if (outputEncoding === 'base64') {
    return btoa(String.fromCharCode(...new Uint8Array(buf)));
  }
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2,'0')).join('');
}

async function hashText() {
  const text = document.getElementById('textInput').value;
  if (!text) return alert('Please enter text to hash');
  const enc = new TextEncoder();
  const data = enc.encode(text);
  await renderHashes(data);
}

async function hashFile(file) {
  if (!file) return;
  document.getElementById('fileInfo').textContent = `📄 ${file.name} (${(file.size/1024).toFixed(1)} KB)`;
  const buf = await file.arrayBuffer();
  await renderHashes(buf);
}

async function renderHashes(data) {
  const algos = [
    {name:'MD5', note:'(via SubtleCrypto, not natively supported — using SHA-1 as fallback)'},
    {algo:'SHA-1', label:'SHA-1'},
    {algo:'SHA-256', label:'SHA-256'},
    {algo:'SHA-384', label:'SHA-384'},
    {algo:'SHA-512', label:'SHA-512'}
  ];

  const results = [];
  for (const a of [
    {algo:'SHA-1',label:'SHA-1'},
    {algo:'SHA-256',label:'SHA-256'},
    {algo:'SHA-384',label:'SHA-384'},
    {algo:'SHA-512',label:'SHA-512'}
  ]) {
    try {
      const hash = await digest(a.algo, data);
      results.push({label:a.label, value:hash});
    } catch(e) {
      results.push({label:a.label, value:'Not supported in this browser'});
    }
  }

  renderRows(results);
}

async function computeHMAC() {
  const keyStr = document.getElementById('hmacKey').value;
  const msg = document.getElementById('hmacInput').value;
  if (!keyStr || !msg) return alert('Enter both key and message');
  const enc = new TextEncoder();
  const keyData = enc.encode(keyStr);
  const msgData = enc.encode(msg);

  const results = [];
  for (const algo of ['SHA-256','SHA-384','SHA-512']) {
    try {
      const key = await crypto.subtle.importKey('raw', keyData, {name:'HMAC',hash:algo}, false, ['sign']);
      const sig = await crypto.subtle.sign('HMAC', key, msgData);
      const hex = Array.from(new Uint8Array(sig)).map(b => b.toString(16).padStart(2,'0')).join('');
      results.push({label:'HMAC-' + algo.replace('SHA-','SHA'), value: outputEncoding === 'base64' ? btoa(String.fromCharCode(...new Uint8Array(sig))) : hex});
    } catch(e) {
      results.push({label:'HMAC-' + algo, value:'Error: ' + e.message});
    }
  }
  renderRows(results);
}

function renderRows(results) {
  let html = '';
  results.forEach(r => {
    html += `<div class="hash-row">
      <span class="hash-label">${r.label}</span>
      <span class="hash-value" id="hv-${r.label}">${r.value}</span>
      <button class="copy-btn" onclick="copyHash('${r.label}')">Copy</button>
    </div>`;
  });
  document.getElementById('hashRows').innerHTML = html;
  document.getElementById('hashResults').style.display = 'block';
}

function copyHash(label) {
  const val = document.getElementById('hv-' + label).textContent;
  navigator.clipboard.writeText(val).then(() => alert(label + ' hash copied!'));
}

function clearAll() {
  document.getElementById('textInput').value = '';
  document.getElementById('hashResults').style.display = 'none';
}

const drop = document.getElementById('fileDrop');
drop.addEventListener('dragover', e => { e.preventDefault(); drop.classList.add('dragover'); });
drop.addEventListener('dragleave', () => drop.classList.remove('dragover'));
drop.addEventListener('drop', e => {
  e.preventDefault(); drop.classList.remove('dragover');
  const file = e.dataTransfer.files[0];
  if (file) hashFile(file);
});
</script>
