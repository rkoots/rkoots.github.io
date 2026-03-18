---
layout: default
title: "APIXOR – API Request Tester | Free Online HTTP Client & REST API Debugger"
excerpt: "Test REST APIs instantly with APIXOR – send GET, POST, PUT, DELETE requests with custom headers, body, and auth. Free online Postman alternative for developers."
date: 2026-03-18
categories: tools
permalink: /tools/api-tester/
description: "Free online API request tester and HTTP client. Send REST API requests with custom headers, JSON body, query params, and auth. Instant response viewer."
keywords: ["api tester online", "free postman alternative", "REST API debugger", "http client online", "test api requests", "api request tool", "api testing tool free", "online http request sender"]
tags: [API, developer, testing, HTTP, REST]
---

<style>
:root{--primary:#7c3aed;--primary-dark:#6d28d9;--accent:#06b6d4;--success:#10b981;--danger:#ef4444;--warn:#f59e0b;--bg:#f5f3ff;--card:#fff;--text:#1e1b4b;--muted:#6b7280;--border:#ddd6fe;--shadow:0 8px 32px rgba(124,58,237,0.10);}
[data-theme="dark"]{--bg:#0d0a1a;--card:#13102a;--text:#ede9fe;--muted:#94a3b8;--border:#3b2f6e;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.apixor{max-width:1100px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:12px;}
.method-select{padding:10px 14px;border-radius:8px;border:2px solid var(--border);background:var(--card);color:var(--text);font-weight:700;font-size:0.95rem;cursor:pointer;}
.method-select:focus{outline:none;border-color:var(--primary);}
.url-input{flex:1;padding:10px 14px;border-radius:8px;border:2px solid var(--border);background:var(--card);color:var(--text);font-size:0.95rem;}
.url-input:focus{outline:none;border-color:var(--primary);}
.btn{display:inline-flex;align-items:center;gap:6px;padding:10px 20px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:transparent;color:var(--primary);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);}
.tabs{display:flex;gap:4px;border-bottom:2px solid var(--border);margin-bottom:14px;}
.tab{padding:8px 16px;border:none;background:none;color:var(--muted);font-size:0.9rem;font-weight:600;cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px;}
.tab.active{color:var(--primary);border-bottom-color:var(--primary);}
.tab-panel{display:none;}
.tab-panel.active{display:block;}
.kv-row{display:grid;grid-template-columns:1fr 1fr auto;gap:8px;margin-bottom:6px;align-items:center;}
.kv-input{padding:8px 10px;border-radius:7px;border:1px solid var(--border);background:var(--card);color:var(--text);font-size:0.88rem;width:100%;}
.kv-input:focus{outline:none;border-color:var(--primary);}
textarea{width:100%;padding:10px;border-radius:8px;border:1px solid var(--border);background:var(--card);color:var(--text);font-size:0.88rem;font-family:Consolas,'Courier New',monospace;resize:vertical;}
textarea:focus{outline:none;border-color:var(--primary);}
.del-btn{padding:6px 10px;border:none;border-radius:6px;background:#fee2e2;color:#dc2626;cursor:pointer;font-size:0.85rem;}
.add-btn{font-size:0.85rem;color:var(--primary);background:none;border:1px dashed var(--primary);border-radius:6px;padding:5px 10px;cursor:pointer;}
.response-area{background:#0f172a;border-radius:10px;padding:16px;color:#e2e8f0;font-family:Consolas,'Courier New',monospace;font-size:0.88rem;white-space:pre-wrap;word-break:break-all;max-height:400px;overflow:auto;}
.status-bar{display:flex;gap:16px;margin-bottom:10px;flex-wrap:wrap;}
.status-chip{padding:4px 12px;border-radius:20px;font-size:0.82rem;font-weight:700;}
.s2xx{background:#dcfce7;color:#166534;}
.s4xx{background:#fef9c3;color:#854d0e;}
.s5xx{background:#fee2e2;color:#991b1b;}
.s0{background:#f1f5f9;color:#475569;}
.section-label{font-size:0.8rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;}
.loader{display:none;width:20px;height:20px;border:3px solid #ddd6fe;border-top-color:var(--primary);border-radius:50%;animation:spin 0.7s linear infinite;}
@keyframes spin{to{transform:rotate(360deg)}}
.loading .loader{display:inline-block;}
.copy-btn{float:right;font-size:0.8rem;padding:4px 10px;}
.info-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:20px;}
.info-card{background:linear-gradient(135deg,#f5f3ff,#ede9fe);border-radius:12px;padding:16px;border:1px solid var(--border);}
.info-card h3{font-size:0.95rem;color:var(--primary-dark);margin-bottom:6px;}
.info-card p{font-size:0.85rem;color:var(--muted);}
@media(max-width:640px){.row{flex-direction:column;}.kv-row{grid-template-columns:1fr auto;}.kv-row .kv-input:last-of-type{grid-column:1/-1;}}
</style>

<div class="apixor">
  <header class="hero">
    <div class="hero-badge">FREE API TESTER</div>
    <h1>APIXOR – API Request Tester</h1>
    <p>Send HTTP requests instantly. Test REST APIs with custom headers, body, params, and authentication — no install required.</p>
  </header>

  <div class="card">
    <div class="row">
      <select class="method-select" id="method">
        <option value="GET">GET</option>
        <option value="POST">POST</option>
        <option value="PUT">PUT</option>
        <option value="PATCH">PATCH</option>
        <option value="DELETE">DELETE</option>
        <option value="HEAD">HEAD</option>
        <option value="OPTIONS">OPTIONS</option>
      </select>
      <input class="url-input" id="urlInput" type="text" placeholder="https://api.example.com/endpoint" value="https://jsonplaceholder.typicode.com/posts/1" />
      <button class="btn btn-primary" id="sendBtn" onclick="sendRequest()">
        <span class="loader" id="loader"></span>
        <span id="sendLabel">Send</span>
      </button>
    </div>

    <div class="tabs">
      <button class="tab active" onclick="switchTab('params',this)">Query Params</button>
      <button class="tab" onclick="switchTab('headers',this)">Headers</button>
      <button class="tab" onclick="switchTab('body',this)">Body</button>
      <button class="tab" onclick="switchTab('auth',this)">Auth</button>
    </div>

    <div id="tab-params" class="tab-panel active">
      <div class="section-label">Query Parameters</div>
      <div id="params-list"></div>
      <button class="add-btn" onclick="addRow('params-list','param')">+ Add Parameter</button>
    </div>

    <div id="tab-headers" class="tab-panel">
      <div class="section-label">Request Headers</div>
      <div id="headers-list"></div>
      <button class="add-btn" onclick="addRow('headers-list','header')">+ Add Header</button>
    </div>

    <div id="tab-body" class="tab-panel">
      <div class="section-label">Request Body</div>
      <div style="margin-bottom:8px;">
        <select id="contentType" style="padding:7px 10px;border-radius:7px;border:1px solid var(--border);background:var(--card);color:var(--text);font-size:0.88rem;">
          <option value="application/json">application/json</option>
          <option value="application/x-www-form-urlencoded">application/x-www-form-urlencoded</option>
          <option value="text/plain">text/plain</option>
          <option value="text/xml">text/xml</option>
        </select>
      </div>
      <textarea id="bodyInput" rows="6" placeholder='{"key": "value"}'></textarea>
    </div>

    <div id="tab-auth" class="tab-panel">
      <div class="section-label">Authentication</div>
      <select id="authType" style="padding:8px 12px;border-radius:7px;border:1px solid var(--border);background:var(--card);color:var(--text);margin-bottom:10px;" onchange="toggleAuth()">
        <option value="none">No Auth</option>
        <option value="bearer">Bearer Token</option>
        <option value="basic">Basic Auth</option>
        <option value="apikey">API Key</option>
      </select>
      <div id="auth-bearer" style="display:none;">
        <input class="kv-input" id="bearerToken" type="text" placeholder="Enter Bearer Token" style="max-width:500px;" />
      </div>
      <div id="auth-basic" style="display:none;display:grid;grid-template-columns:1fr 1fr;gap:8px;max-width:500px;">
        <input class="kv-input" id="basicUser" type="text" placeholder="Username" />
        <input class="kv-input" id="basicPass" type="password" placeholder="Password" />
      </div>
      <div id="auth-apikey" style="display:none;">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;max-width:500px;">
          <input class="kv-input" id="apikeyName" type="text" placeholder="Header Name (e.g. X-API-Key)" />
          <input class="kv-input" id="apikeyValue" type="text" placeholder="API Key Value" />
        </div>
      </div>
    </div>
  </div>

  <div class="card" id="responseCard" style="display:none;">
    <div class="status-bar" id="statusBar"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
      <span class="section-label">Response Body</span>
      <button class="btn btn-ghost copy-btn" onclick="copyResponse()">Copy</button>
    </div>
    <div class="response-area" id="responseBody"></div>
    <details style="margin-top:12px;">
      <summary style="cursor:pointer;font-size:0.88rem;color:var(--primary);font-weight:600;">Response Headers</summary>
      <div class="response-area" id="responseHeaders" style="margin-top:8px;max-height:200px;"></div>
    </details>
  </div>

  <div class="info-grid">
    <div class="info-card">
      <h3>All HTTP Methods</h3>
      <p>Supports GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS for complete REST API testing.</p>
    </div>
    <div class="info-card">
      <h3>Custom Headers & Auth</h3>
      <p>Add Bearer tokens, Basic auth, API keys, or any custom headers with ease.</p>
    </div>
    <div class="info-card">
      <h3>JSON Body Editor</h3>
      <p>Send structured JSON, form-encoded, or plain text body payloads with content-type selection.</p>
    </div>
    <div class="info-card">
      <h3>Instant Response View</h3>
      <p>View formatted response body, status code, response time, and all response headers.</p>
    </div>
  </div>
</div>

<script>
function switchTab(name, el) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById('tab-' + name).classList.add('active');
  el.classList.add('active');
}

function addRow(listId, type) {
  const list = document.getElementById(listId);
  const row = document.createElement('div');
  row.className = 'kv-row';
  row.innerHTML = `<input class="kv-input" type="text" placeholder="${type === 'param' ? 'Parameter name' : 'Header name'}" />
    <input class="kv-input" type="text" placeholder="Value" />
    <button class="del-btn" onclick="this.parentElement.remove()">✕</button>`;
  list.appendChild(row);
}

function toggleAuth() {
  const type = document.getElementById('authType').value;
  ['bearer','basic','apikey'].forEach(t => {
    const el = document.getElementById('auth-' + t);
    if (el) el.style.display = t === type ? 'block' : 'none';
  });
  if (type === 'basic') document.getElementById('auth-basic').style.display = 'grid';
}

function getKVPairs(listId) {
  const pairs = {};
  document.querySelectorAll(`#${listId} .kv-row`).forEach(row => {
    const inputs = row.querySelectorAll('input');
    const k = inputs[0].value.trim(), v = inputs[1].value.trim();
    if (k) pairs[k] = v;
  });
  return pairs;
}

async function sendRequest() {
  const method = document.getElementById('method').value;
  let url = document.getElementById('urlInput').value.trim();
  if (!url) return alert('Please enter a URL');

  const params = getKVPairs('params-list');
  if (Object.keys(params).length) {
    const qs = new URLSearchParams(params).toString();
    url += (url.includes('?') ? '&' : '?') + qs;
  }

  const headers = getKVPairs('headers-list');
  const authType = document.getElementById('authType').value;
  if (authType === 'bearer') {
    const t = document.getElementById('bearerToken').value.trim();
    if (t) headers['Authorization'] = 'Bearer ' + t;
  } else if (authType === 'basic') {
    const u = document.getElementById('basicUser').value.trim();
    const p = document.getElementById('basicPass').value.trim();
    if (u || p) headers['Authorization'] = 'Basic ' + btoa(u + ':' + p);
  } else if (authType === 'apikey') {
    const n = document.getElementById('apikeyName').value.trim();
    const v = document.getElementById('apikeyValue').value.trim();
    if (n && v) headers[n] = v;
  }

  const hasBody = ['POST','PUT','PATCH'].includes(method);
  const bodyText = document.getElementById('bodyInput').value.trim();
  if (hasBody && bodyText) {
    headers['Content-Type'] = document.getElementById('contentType').value;
  }

  const btn = document.getElementById('sendBtn');
  const loader = document.getElementById('loader');
  const label = document.getElementById('sendLabel');
  btn.disabled = true; loader.style.display = 'inline-block'; label.textContent = 'Sending…';

  const t0 = Date.now();
  try {
    const opts = { method, headers };
    if (hasBody && bodyText) opts.body = bodyText;
    const res = await fetch(url, opts);
    const elapsed = Date.now() - t0;
    const text = await res.text();

    let display = text;
    try { display = JSON.stringify(JSON.parse(text), null, 2); } catch(e) {}

    const sClass = res.status < 300 ? 's2xx' : res.status < 500 ? 's4xx' : 's5xx';
    document.getElementById('statusBar').innerHTML =
      `<span class="status-chip ${sClass}">HTTP ${res.status} ${res.statusText}</span>
       <span class="status-chip s0">⏱ ${elapsed}ms</span>
       <span class="status-chip s0">Size: ${new Blob([text]).size} B</span>`;

    document.getElementById('responseBody').textContent = display || '(empty body)';

    let hdrs = '';
    res.headers.forEach((v, k) => { hdrs += `${k}: ${v}\n`; });
    document.getElementById('responseHeaders').textContent = hdrs || '(no headers)';
    document.getElementById('responseCard').style.display = 'block';
  } catch(err) {
    document.getElementById('statusBar').innerHTML = `<span class="status-chip s5xx">Request Failed</span>`;
    document.getElementById('responseBody').textContent = err.message + '\n\nNote: Cross-origin requests may be blocked by CORS policy. Try an API that allows cross-origin access.';
    document.getElementById('responseCard').style.display = 'block';
  } finally {
    btn.disabled = false; loader.style.display = 'none'; label.textContent = 'Send';
  }
}

function copyResponse() {
  const text = document.getElementById('responseBody').textContent;
  navigator.clipboard.writeText(text).then(() => alert('Copied to clipboard!'));
}

document.getElementById('urlInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') sendRequest();
});
</script>
