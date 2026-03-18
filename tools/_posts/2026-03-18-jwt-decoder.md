---
layout: default
title: "JWTDEX – JWT Decoder & Debugger | Free Online JSON Web Token Inspector"
excerpt: "Decode and debug JWT tokens instantly with JWTDEX. Inspect header, payload, and signature. Verify expiry, issued-at claims, and algorithm. Free online JWT decoder tool."
date: 2026-03-18
categories: tools
permalink: /tools/jwt-decoder/
description: "Free online JWT decoder and debugger. Decode JWT header, payload, verify expiry and claims, inspect signature algorithm. No data sent to server — 100% client-side."
keywords: ["jwt decoder online", "json web token decoder", "jwt debugger", "decode jwt token free", "jwt inspector", "jwt header payload decoder", "verify jwt token online", "jwt claims viewer", "jwt tool free"]
tags: [JWT, security, developer, authentication, utility]
---

<style>
:root{--primary:#7c3aed;--primary-dark:#6d28d9;--accent:#f59e0b;--success:#10b981;--danger:#ef4444;--bg:#f5f3ff;--card:#fff;--text:#1e1b4b;--muted:#6b7280;--border:#ddd6fe;--shadow:0 8px 32px rgba(124,58,237,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.jwtdex{max-width:960px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.token-input{width:100%;padding:12px 16px;border:2px solid var(--border);border-radius:10px;font-family:Consolas,'Courier New',monospace;font-size:0.88rem;background:var(--card);color:var(--text);resize:vertical;line-height:1.5;min-height:80px;}
.token-input:focus{outline:none;border-color:var(--primary);}
.btn{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;margin-top:10px;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.jwt-visual{display:flex;gap:4px;flex-wrap:wrap;padding:12px;background:#f5f3ff;border-radius:10px;font-family:Consolas,monospace;font-size:0.82rem;word-break:break-all;margin-top:12px;}
.jwt-header-seg{color:#e11d48;font-weight:600;}
.jwt-payload-seg{color:#7c3aed;font-weight:600;}
.jwt-sig-seg{color:#0891b2;font-weight:600;}
.jwt-dot{color:#374151;font-weight:700;}
.parts-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px;}
.part-card{background:var(--card);border-radius:12px;padding:16px;border:1px solid var(--border);}
.part-label{font-size:0.75rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;}
.header-label{color:#e11d48;}
.payload-label{color:#7c3aed;}
.sig-label{color:#0891b2;}
pre.json-display{background:#0f172a;color:#e2e8f0;padding:12px;border-radius:8px;font-size:0.82rem;overflow:auto;max-height:250px;white-space:pre-wrap;word-break:break-all;}
.claims-table{width:100%;border-collapse:collapse;font-size:0.85rem;margin-top:8px;}
.claims-table th{background:#f5f3ff;color:var(--primary-dark);padding:8px 12px;border-bottom:2px solid var(--border);text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.5px;}
.claims-table td{padding:8px 12px;border-bottom:1px solid var(--border);word-break:break-all;}
.claims-table tr:last-child td{border-bottom:none;}
.claim-name{font-family:Consolas,monospace;font-size:0.83rem;font-weight:600;color:var(--primary);}
.badge-ok{display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:12px;background:#dcfce7;color:#166534;font-size:0.78rem;font-weight:700;}
.badge-warn{background:#fef9c3;color:#854d0e;}
.badge-err{background:#fee2e2;color:#991b1b;}
.badge-info{background:#e0f2fe;color:#0369a1;}
.error-msg{background:#fee2e2;border-left:4px solid var(--danger);border-radius:8px;padding:12px;color:#991b1b;font-size:0.9rem;margin-top:10px;}
.algo-info{display:inline-block;padding:4px 10px;background:#ede9fe;color:var(--primary);border-radius:8px;font-size:0.82rem;font-weight:700;font-family:Consolas,monospace;}
@media(max-width:650px){.parts-grid{grid-template-columns:1fr;}}
</style>

<div class="jwtdex">
  <header class="hero">
    <div class="hero-badge">FREE JWT DECODER</div>
    <h1>JWTDEX – JWT Decoder & Debugger</h1>
    <p>Instantly decode and inspect JSON Web Tokens. View header, payload claims, expiry status, and algorithm — entirely client-side. Your token never leaves your browser.</p>
  </header>

  <div class="card">
    <div style="font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Paste JWT Token</div>
    <textarea class="token-input" id="jwtInput" placeholder="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"></textarea>
    <div style="display:flex;gap:8px;margin-top:10px;">
      <button class="btn btn-primary" onclick="decodeJWT()">Decode Token</button>
      <button class="btn btn-ghost" onclick="loadSample()">Load Sample</button>
      <button class="btn btn-ghost" onclick="clearAll()">Clear</button>
    </div>
    <div id="jwtVisual" style="display:none;"></div>
    <div id="errorMsg" style="display:none;" class="error-msg"></div>
  </div>

  <div id="resultCard" style="display:none;">
    <div class="card">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:14px;">
        <div style="font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;">Token Analysis</div>
        <div id="algoDisplay"></div>
      </div>
      <div id="statusBadges" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px;"></div>
      <div class="parts-grid">
        <div class="part-card">
          <div class="part-label header-label">Header</div>
          <pre class="json-display" id="headerDisplay"></pre>
        </div>
        <div class="part-card">
          <div class="part-label payload-label">Payload</div>
          <pre class="json-display" id="payloadDisplay"></pre>
        </div>
      </div>
    </div>

    <div class="card" id="claimsCard">
      <div style="font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Registered Claims (RFC 7519)</div>
      <table class="claims-table" id="claimsTable"></table>
    </div>
  </div>
</div>

<script>
const SAMPLE_JWT = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyXzEyMzQ1IiwibmFtZSI6IkFsaWNlIEpvaG5zb24iLCJlbWFpbCI6ImFsaWNlQGV4YW1wbGUuY29tIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzQyMjU3MjAwLCJleHAiOjE3NDIzNDM2MDAsIm5iZiI6MTc0MjI1NzIwMCwiaXNzIjoiaHR0cHM6Ly9hdXRoLmV4YW1wbGUuY29tIiwiYXVkIjoiaHR0cHM6Ly9hcGkuZXhhbXBsZS5jb20ifQ.dummy_signature';

function loadSample() {
  document.getElementById('jwtInput').value = SAMPLE_JWT;
  decodeJWT();
}

function b64UrlDecode(str) {
  str = str.replace(/-/g, '+').replace(/_/g, '/');
  while (str.length % 4) str += '=';
  return atob(str);
}

function decodeJWT() {
  const token = document.getElementById('jwtInput').value.trim();
  const errorDiv = document.getElementById('errorMsg');
  const resultCard = document.getElementById('resultCard');
  const visual = document.getElementById('jwtVisual');
  errorDiv.style.display = 'none';
  resultCard.style.display = 'none';
  visual.style.display = 'none';

  if (!token) return;

  const parts = token.split('.');
  if (parts.length !== 3) {
    errorDiv.textContent = '⚠️ Invalid JWT: Expected 3 parts separated by dots (header.payload.signature)';
    errorDiv.style.display = 'block';
    return;
  }

  let header, payload;
  try { header = JSON.parse(b64UrlDecode(parts[0])); } catch(e) {
    errorDiv.textContent = '⚠️ Failed to decode header: ' + e.message;
    errorDiv.style.display = 'block'; return;
  }
  try { payload = JSON.parse(b64UrlDecode(parts[1])); } catch(e) {
    errorDiv.textContent = '⚠️ Failed to decode payload: ' + e.message;
    errorDiv.style.display = 'block'; return;
  }

  visual.innerHTML = `<div class="jwt-visual">
    <span class="jwt-header-seg">${escHtml(parts[0])}</span>
    <span class="jwt-dot">.</span>
    <span class="jwt-payload-seg">${escHtml(parts[1])}</span>
    <span class="jwt-dot">.</span>
    <span class="jwt-sig-seg">${escHtml(parts[2])}</span>
  </div>`;
  visual.style.display = 'block';

  document.getElementById('headerDisplay').textContent = JSON.stringify(header, null, 2);
  document.getElementById('payloadDisplay').textContent = JSON.stringify(payload, null, 2);
  document.getElementById('algoDisplay').innerHTML = `<span class="algo-info">alg: ${header.alg || '?'} | typ: ${header.typ || '?'}</span>`;

  const now = Math.floor(Date.now() / 1000);
  const badges = [];

  if (payload.exp) {
    const expDate = new Date(payload.exp * 1000);
    if (payload.exp < now) {
      badges.push(`<span class="badge-ok badge-err">✗ Expired ${timeSince(payload.exp)}</span>`);
    } else {
      badges.push(`<span class="badge-ok">✓ Valid — expires in ${timeUntil(payload.exp)}</span>`);
    }
  } else {
    badges.push('<span class="badge-ok badge-warn">⚠ No expiry (exp) claim</span>');
  }

  if (payload.nbf && payload.nbf > now) {
    badges.push(`<span class="badge-ok badge-warn">⚠ Not valid yet (nbf: ${new Date(payload.nbf*1000).toISOString()})</span>`);
  }

  badges.push(`<span class="badge-ok badge-info">⚠ Signature not verified (client-side)</span>`);
  document.getElementById('statusBadges').innerHTML = badges.join('');

  const CLAIM_NAMES = {
    sub:'Subject — unique user identifier',iss:'Issuer — token issuer URL',
    aud:'Audience — intended recipients',exp:'Expiration time (Unix timestamp)',
    iat:'Issued at (Unix timestamp)',nbf:'Not before (Unix timestamp)',jti:'JWT ID — unique token identifier'
  };

  let claimsHtml = '<thead><tr><th>Claim</th><th>Full Name</th><th>Value</th><th>Status</th></tr></thead><tbody>';
  for (const [k, v] of Object.entries(payload)) {
    const name = CLAIM_NAMES[k] || 'Custom claim';
    let status = '';
    if (k === 'exp') {
      const expired = v < now;
      status = expired ? '<span class="badge-ok badge-err">Expired</span>' : '<span class="badge-ok">Active</span>';
    } else if (k === 'iat' || k === 'nbf' || k === 'exp') {
      status = `<span class="badge-ok badge-info">${new Date(v*1000).toISOString()}</span>`;
    }
    let displayVal = typeof v === 'object' ? JSON.stringify(v) : escHtml(String(v));
    if ((k==='iat'||k==='nbf'||k==='exp') && typeof v === 'number') {
      displayVal += ` <small style="color:var(--muted);">(${new Date(v*1000).toLocaleString()})</small>`;
    }
    claimsHtml += `<tr><td><span class="claim-name">${escHtml(k)}</span></td><td style="font-size:0.82rem;color:var(--muted);">${escHtml(name)}</td><td>${displayVal}</td><td>${status}</td></tr>`;
  }
  claimsHtml += '</tbody>';
  document.getElementById('claimsTable').innerHTML = claimsHtml;
  resultCard.style.display = 'block';
}

function timeSince(ts) {
  const diff = Math.floor(Date.now()/1000) - ts;
  if (diff < 60) return `${diff}s ago`;
  if (diff < 3600) return `${Math.floor(diff/60)}m ago`;
  if (diff < 86400) return `${Math.floor(diff/3600)}h ago`;
  return `${Math.floor(diff/86400)}d ago`;
}

function timeUntil(ts) {
  const diff = ts - Math.floor(Date.now()/1000);
  if (diff < 60) return `${diff}s`;
  if (diff < 3600) return `${Math.floor(diff/60)}m`;
  if (diff < 86400) return `${Math.floor(diff/3600)}h`;
  return `${Math.floor(diff/86400)}d`;
}

function clearAll() {
  document.getElementById('jwtInput').value = '';
  document.getElementById('resultCard').style.display = 'none';
  document.getElementById('jwtVisual').style.display = 'none';
  document.getElementById('errorMsg').style.display = 'none';
}

function escHtml(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
</script>
