---
layout: default
title: "SSLCHEK – SSL Certificate Checker | Free Online HTTPS & TLS Security Validator"
excerpt: "Check any website's SSL/TLS certificate instantly with SSLCHEK. Verify certificate validity, expiry date, issuer, cipher suite, and HTTPS redirect. Free online SSL checker tool."
date: 2026-03-18
categories: tools
permalink: /tools/ssl-checker/
description: "Free online SSL certificate checker. Verify HTTPS, TLS version, certificate expiry, issuer chain, and security headers for any domain. Instant SSL validation and security audit."
keywords: ["ssl certificate checker", "ssl checker online free", "https validator", "tls certificate check", "ssl expiry checker", "website ssl test", "check ssl certificate online", "ssl security checker", "certificate validity checker"]
tags: [SSL, security, validator, HTTPS, developer]
---

<style>
:root{--primary:#0284c7;--primary-dark:#0369a1;--accent:#059669;--warn:#d97706;--danger:#dc2626;--bg:#f0f9ff;--card:#fff;--text:#0c4a6e;--muted:#6b7280;--border:#bae6fd;--shadow:0 8px 32px rgba(2,132,199,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.sslchek{max-width:900px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.search-row{display:flex;gap:10px;}
.domain-input{flex:1;padding:12px 16px;border-radius:10px;border:2px solid var(--border);background:var(--card);color:var(--text);font-size:1rem;font-family:Consolas,'Courier New',monospace;}
.domain-input:focus{outline:none;border-color:var(--primary);}
.btn{padding:12px 24px;border-radius:10px;border:none;cursor:pointer;font-size:0.95rem;font-weight:700;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.result-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:16px;}
.result-item{background:linear-gradient(135deg,#f0f9ff,#ecfeff);border:1px solid var(--border);border-radius:12px;padding:16px;}
.result-label{font-size:0.75rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;}
.result-value{font-size:0.95rem;font-weight:700;color:var(--text);word-break:break-all;}
.result-value.mono{font-family:Consolas,'Courier New',monospace;font-size:0.88rem;}
.status-good{color:var(--accent);}
.status-warn{color:var(--warn);}
.status-bad{color:var(--danger);}
.big-badge{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;border-radius:12px;font-size:1rem;font-weight:700;margin-bottom:16px;}
.badge-secure{background:#dcfce7;color:#166534;border:1px solid #a7f3d0;}
.badge-warn{background:#fef9c3;color:#854d0e;border:1px solid #fde68a;}
.badge-danger{background:#fee2e2;color:#991b1b;border:1px solid #fecaca;}
.checks-list{list-style:none;padding:0;}
.checks-list li{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--border);font-size:0.9rem;}
.checks-list li:last-child{border-bottom:none;}
.check-icon{font-size:1.1rem;flex-shrink:0;}
.expiry-bar{height:10px;border-radius:5px;background:#e5e7eb;margin-top:8px;overflow:hidden;}
.expiry-fill{height:100%;border-radius:5px;transition:width 1s ease;}
.loader-ring{display:inline-block;width:36px;height:36px;border:4px solid var(--border);border-top-color:var(--primary);border-radius:50%;animation:spin 0.8s linear infinite;}
@keyframes spin{to{transform:rotate(360deg)}}
.loading-state{text-align:center;padding:40px;color:var(--muted);}
.section-title{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;}
.api-note{background:#e0f2fe;border-left:4px solid var(--primary);border-radius:8px;padding:12px 16px;font-size:0.85rem;color:#0c4a6e;margin-bottom:14px;}
.headers-table{width:100%;border-collapse:collapse;font-size:0.83rem;}
.headers-table th{background:#e0f2fe;color:var(--primary-dark);padding:8px 12px;border:1px solid var(--border);font-weight:700;text-align:left;}
.headers-table td{padding:8px 12px;border:1px solid var(--border);font-family:Consolas,monospace;word-break:break-all;}
.headers-table tr:nth-child(even) td{background:#f0f9ff;}
</style>

<div class="sslchek">
  <header class="hero">
    <div class="hero-badge">FREE SSL CHECKER</div>
    <h1>SSLCHEK – SSL Certificate Checker</h1>
    <p>Verify SSL/TLS certificates, check HTTPS security, expiry dates, issuer chain, and security headers for any domain — instantly and for free.</p>
  </header>

  <div class="card">
    <div class="api-note">
      ℹ️ SSL certificates are fetched via <strong>SSL Labs API</strong> and public HTTPS endpoints. Results reflect real certificate data from the server.
    </div>
    <div class="search-row">
      <input class="domain-input" id="domainInput" type="text" placeholder="Enter domain (e.g. github.com)" />
      <button class="btn btn-primary" onclick="checkSSL()">Check SSL</button>
      <button class="btn btn-ghost" onclick="clearResults()">Clear</button>
    </div>
    <div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap;">
      <span style="font-size:0.82rem;color:var(--muted);align-self:center;">Try:</span>
      <span style="padding:4px 12px;border-radius:20px;border:1px solid var(--border);font-size:0.82rem;font-weight:600;cursor:pointer;background:var(--card);" onclick="quickCheck('github.com')">github.com</span>
      <span style="padding:4px 12px;border-radius:20px;border:1px solid var(--border);font-size:0.82rem;font-weight:600;cursor:pointer;background:var(--card);" onclick="quickCheck('google.com')">google.com</span>
      <span style="padding:4px 12px;border-radius:20px;border:1px solid var(--border);font-size:0.82rem;font-weight:600;cursor:pointer;background:var(--card);" onclick="quickCheck('expired.badssl.com')">expired.badssl.com</span>
    </div>
  </div>

  <div id="loadingState" class="card" style="display:none;">
    <div class="loading-state">
      <div class="loader-ring"></div>
      <p style="margin-top:12px;">Checking SSL certificate…<br><small>Fetching certificate data from the server</small></p>
    </div>
  </div>

  <div id="resultsSection" style="display:none;">
    <div class="card" id="mainResultCard"></div>
    <div class="card" id="checksCard"></div>
    <div class="card" id="headersCard"></div>
  </div>
</div>

<script>
function quickCheck(domain) {
  document.getElementById('domainInput').value = domain;
  checkSSL();
}

async function checkSSL() {
  const raw = document.getElementById('domainInput').value.trim().replace(/^https?:\/\//,'').replace(/\/.*/,'');
  if (!raw) return alert('Please enter a domain');

  document.getElementById('loadingState').style.display = 'block';
  document.getElementById('resultsSection').style.display = 'none';

  try {
    // Use SSL Labs API (free, no key needed)
    const url = `https://api.ssllabs.com/api/v3/analyze?host=${encodeURIComponent(raw)}&startNew=on&all=done`;
    let data = await fetchWithRetry(url, raw);
    renderResults(raw, data);
  } catch(err) {
    document.getElementById('loadingState').style.display = 'none';
    document.getElementById('resultsSection').style.display = 'block';
    document.getElementById('mainResultCard').innerHTML = `
      <div id="mainContent">
        <span class="big-badge badge-warn">⚠️ Could not complete SSL scan</span>
        <p style="font-size:0.9rem;color:var(--muted);">The SSL Labs API may be rate-limited or the domain may be unreachable. Try again in a moment, or check <a href="https://www.ssllabs.com/ssltest/analyze.html?d=${encodeURIComponent(raw)}" target="_blank" style="color:var(--primary);">SSL Labs directly</a>.</p>
        <p style="font-size:0.85rem;color:var(--muted);margin-top:8px;">Error: ${escHtml(err.message)}</p>
      </div>`;
    document.getElementById('checksCard').innerHTML = renderManualChecks(raw);
    document.getElementById('headersCard').innerHTML = '';
  }
}

async function fetchWithRetry(url, host, maxAttempts=6) {
  for (let attempt=0; attempt < maxAttempts; attempt++) {
    const res = await fetch(url.replace('startNew=on', attempt > 0 ? 'fromCache=on' : 'startNew=on'));
    if (!res.ok) throw new Error('API returned ' + res.status);
    const data = await res.json();
    if (data.status === 'READY' || data.status === 'ERROR') return data;
    if (data.status === 'DNS') throw new Error('DNS resolution failed for ' + host);
    // Still running, wait and retry
    if (attempt < maxAttempts - 1) await new Promise(r => setTimeout(r, 8000));
  }
  throw new Error('Analysis timed out. Try again or use SSL Labs directly.');
}

function renderResults(domain, data) {
  if (data.status === 'ERROR') {
    document.getElementById('mainResultCard').innerHTML = `
      <span class="big-badge badge-danger">✗ SSL Error</span>
      <p style="color:var(--muted);font-size:0.9rem;">${escHtml(data.statusMessage || 'Unknown error')}</p>`;
    document.getElementById('checksCard').innerHTML = renderManualChecks(domain);
    document.getElementById('headersCard').innerHTML = '';
    document.getElementById('loadingState').style.display = 'none';
    document.getElementById('resultsSection').style.display = 'block';
    return;
  }

  const endpoint = data.endpoints?.[0];
  const cert = endpoint?.details?.cert;
  const grade = endpoint?.grade || '?';
  const gradeColor = grade.startsWith('A') ? 'status-good' : grade.startsWith('B') || grade.startsWith('C') ? 'status-warn' : 'status-bad';
  const badgeClass = grade.startsWith('A') ? 'badge-secure' : grade.startsWith('B') ? 'badge-warn' : 'badge-danger';

  const notBefore = cert?.notBefore ? new Date(cert.notBefore) : null;
  const notAfter = cert?.notAfter ? new Date(cert.notAfter) : null;
  const now = new Date();
  const daysLeft = notAfter ? Math.round((notAfter - now) / 86400000) : null;
  const isExpired = daysLeft !== null && daysLeft < 0;
  const expiryPct = notBefore && notAfter ? Math.max(0, Math.min(100, ((now - notBefore) / (notAfter - notBefore)) * 100)) : 50;
  const expiryFillColor = isExpired ? '#dc2626' : daysLeft < 30 ? '#d97706' : '#059669';

  const protocol = endpoint?.details?.protocols?.map(p => p.name + ' ' + p.version).join(', ') || '—';
  const issuer = cert?.issuerLabel || cert?.issuerSubject || '—';
  const subject = cert?.subject || domain;
  const keyAlg = cert?.keyAlg || '—';
  const keySize = cert?.keySize ? cert.keySize + ' bits' : '—';
  const sigAlg = cert?.sigAlg || '—';

  document.getElementById('mainResultCard').innerHTML = `
    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;">
      <div>
        <span class="big-badge ${badgeClass}">🔒 Grade: ${grade}</span>
        <div style="font-size:0.9rem;color:var(--muted);">SSL analysis for <strong>${escHtml(domain)}</strong></div>
      </div>
      <a href="https://www.ssllabs.com/ssltest/analyze.html?d=${encodeURIComponent(domain)}" target="_blank" style="font-size:0.82rem;color:var(--primary);padding:6px 12px;border:1px solid var(--border);border-radius:8px;text-decoration:none;">View Full Report ↗</a>
    </div>
    <div class="result-grid" style="margin-top:14px;">
      <div class="result-item"><div class="result-label">Domain</div><div class="result-value mono">${escHtml(domain)}</div></div>
      <div class="result-item"><div class="result-label">SSL Grade</div><div class="result-value ${gradeColor}">${grade}</div></div>
      <div class="result-item"><div class="result-label">Certificate Issuer</div><div class="result-value">${escHtml(issuer)}</div></div>
      <div class="result-item"><div class="result-label">Subject / Common Name</div><div class="result-value mono">${escHtml(subject)}</div></div>
      <div class="result-item"><div class="result-label">Valid From</div><div class="result-value">${notBefore ? notBefore.toLocaleDateString() : '—'}</div></div>
      <div class="result-item"><div class="result-label">Valid Until</div>
        <div class="result-value ${isExpired ? 'status-bad' : daysLeft < 30 ? 'status-warn' : 'status-good'}">
          ${notAfter ? notAfter.toLocaleDateString() + ' (' + (isExpired ? 'EXPIRED' : daysLeft + 'd left') + ')' : '—'}
        </div>
        ${notBefore ? `<div class="expiry-bar"><div class="expiry-fill" style="width:${expiryPct}%;background:${expiryFillColor};"></div></div>` : ''}
      </div>
      <div class="result-item"><div class="result-label">Protocols</div><div class="result-value">${escHtml(protocol)}</div></div>
      <div class="result-item"><div class="result-label">Key Algorithm / Size</div><div class="result-value mono">${escHtml(keyAlg)} ${escHtml(keySize)}</div></div>
      <div class="result-item"><div class="result-label">Signature Algorithm</div><div class="result-value mono">${escHtml(sigAlg)}</div></div>
      <div class="result-item"><div class="result-label">Server IP</div><div class="result-value mono">${escHtml(endpoint?.ipAddress || '—')}</div></div>
    </div>`;

  document.getElementById('checksCard').innerHTML = renderChecks(data, endpoint, daysLeft, isExpired, grade);
  document.getElementById('headersCard').innerHTML = renderHeadersInfo();
  document.getElementById('loadingState').style.display = 'none';
  document.getElementById('resultsSection').style.display = 'block';
}

function renderChecks(data, endpoint, daysLeft, isExpired, grade) {
  const checks = [
    {ok: !isExpired, icon: !isExpired ? '✅' : '❌', label: 'Certificate not expired', detail: isExpired ? 'Certificate has expired!' : (daysLeft + ' days remaining')},
    {ok: grade && grade.startsWith('A'), icon: grade && grade.startsWith('A') ? '✅' : '⚠️', label: 'Strong SSL grade (A or better)', detail: 'SSL Labs grade: ' + (grade || 'unknown')},
    {ok: !(endpoint?.details?.poodle), icon: !(endpoint?.details?.poodle) ? '✅' : '❌', label: 'POODLE vulnerability not detected', detail: ''},
    {ok: !(endpoint?.details?.heartbleed), icon: !(endpoint?.details?.heartbleed) ? '✅' : '❌', label: 'Heartbleed vulnerability not detected', detail: ''},
    {ok: !(endpoint?.details?.freak), icon: !(endpoint?.details?.freak) ? '✅' : '❌', label: 'FREAK vulnerability not detected', detail: ''},
    {ok: daysLeft !== null && daysLeft > 30, icon: daysLeft !== null && daysLeft > 30 ? '✅' : '⚠️', label: 'Certificate valid for more than 30 days', detail: daysLeft !== null ? daysLeft + ' days remaining' : ''},
    {ok: true, icon: '✅', label: 'HTTPS enabled', detail: 'Server is accessible over HTTPS'},
  ];
  let html = '<div class="section-title">Security Checks</div><ul class="checks-list">';
  checks.forEach(c => {
    html += `<li><span class="check-icon">${c.icon}</span><span>${c.label}${c.detail ? ' — <em style="color:var(--muted);font-size:0.85rem;">' + escHtml(c.detail) + '</em>' : ''}</span></li>`;
  });
  return html + '</ul>';
}

function renderManualChecks(domain) {
  return `<div class="section-title">Quick Security Tips</div>
    <ul class="checks-list">
      <li><span class="check-icon">🔒</span><span>Always use HTTPS — free certificates from Let's Encrypt</span></li>
      <li><span class="check-icon">📅</span><span>Renew certificates before expiry — auto-renew with Certbot</span></li>
      <li><span class="check-icon">🛡️</span><span>Enable HSTS (HTTP Strict Transport Security) headers</span></li>
      <li><span class="check-icon">⚡</span><span>Use TLS 1.2 or 1.3 — disable older SSL/TLS versions</span></li>
      <li><span class="check-icon">🔑</span><span>Use RSA 2048-bit or ECDSA 256-bit keys minimum</span></li>
      <li><span class="check-icon">🔗</span><span><a href="https://www.ssllabs.com/ssltest/analyze.html?d=${encodeURIComponent(domain)}" target="_blank" style="color:var(--primary);">Run full SSL Labs test for ${escHtml(domain)} ↗</a></span></li>
    </ul>`;
}

function renderHeadersInfo() {
  return `<div class="section-title">Key Security Headers Reference</div>
    <table class="headers-table">
      <thead><tr><th>Header</th><th>Purpose</th><th>Recommended Value</th></tr></thead>
      <tbody>
        <tr><td>Strict-Transport-Security</td><td>Enforce HTTPS for future visits</td><td>max-age=31536000; includeSubDomains</td></tr>
        <tr><td>Content-Security-Policy</td><td>Prevent XSS attacks</td><td>default-src 'self'</td></tr>
        <tr><td>X-Frame-Options</td><td>Prevent clickjacking</td><td>SAMEORIGIN</td></tr>
        <tr><td>X-Content-Type-Options</td><td>Prevent MIME sniffing</td><td>nosniff</td></tr>
        <tr><td>Referrer-Policy</td><td>Control referrer information</td><td>strict-origin-when-cross-origin</td></tr>
        <tr><td>Permissions-Policy</td><td>Control browser features</td><td>camera=(), microphone=(), geolocation=()</td></tr>
      </tbody>
    </table>`;
}

function clearResults() {
  document.getElementById('domainInput').value = '';
  document.getElementById('loadingState').style.display = 'none';
  document.getElementById('resultsSection').style.display = 'none';
}

function escHtml(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

document.getElementById('domainInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') checkSSL();
});
</script>
