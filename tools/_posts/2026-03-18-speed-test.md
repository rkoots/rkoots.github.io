---
layout: default
title: "VELOXIQ – Website Speed Test | Free Online Page Performance Analyzer & Core Web Vitals Checker"
excerpt: "Analyze any website's performance metrics with VELOXIQ. Check load times, Core Web Vitals, resource sizes, and optimization tips. Free online website speed test and performance checker."
date: 2026-03-18
categories: tools
permalink: /tools/speed-test/
description: "Free online website speed test and performance analyzer. Check page load time, resource sizes, Core Web Vitals score, HTTP headers, and get actionable optimization recommendations."
keywords: ["website speed test", "page speed checker online", "web performance analyzer", "core web vitals checker", "site load time test", "page load speed tool", "website performance test free", "check website speed", "google pagespeed alternative"]
tags: [performance, speed, developer, web, analytics]
---

<style>
:root{--primary:#059669;--primary-dark:#047857;--accent:#f59e0b;--warn:#ef4444;--bg:#f0fdf4;--card:#fff;--text:#052e16;--muted:#6b7280;--border:#a7f3d0;--shadow:0 8px 32px rgba(5,150,105,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.veloxiq{max-width:960px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.search-row{display:flex;gap:10px;}
.url-input{flex:1;padding:12px 16px;border-radius:10px;border:2px solid var(--border);background:var(--card);color:var(--text);font-size:1rem;font-family:Consolas,'Courier New',monospace;}
.url-input:focus{outline:none;border-color:var(--primary);}
.btn{padding:12px 24px;border-radius:10px;border:none;cursor:pointer;font-size:0.95rem;font-weight:700;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);}
.device-chips{display:flex;gap:8px;margin-top:10px;}
.device-chip{padding:5px 14px;border-radius:20px;border:1px solid var(--border);font-size:0.82rem;font-weight:600;cursor:pointer;}
.device-chip.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.metrics-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px;margin-top:16px;}
.metric-card{background:var(--card);border-radius:12px;padding:16px;border:1px solid var(--border);text-align:center;}
.metric-score{font-size:2rem;font-weight:800;margin-bottom:4px;}
.score-good{color:#059669;}
.score-avg{color:#d97706;}
.score-poor{color:#dc2626;}
.metric-label{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;}
.metric-bar{height:6px;border-radius:3px;background:#e5e7eb;margin-top:8px;overflow:hidden;}
.metric-fill{height:100%;border-radius:3px;transition:width 1s ease;}
.fill-good{background:#059669;}
.fill-avg{background:#d97706;}
.fill-poor{background:#dc2626;}
.results-section{margin-top:16px;}
.loader-ring{display:inline-block;width:40px;height:40px;border:4px solid var(--border);border-top-color:var(--primary);border-radius:50%;animation:spin 0.8s linear infinite;}
@keyframes spin{to{transform:rotate(360deg)}}
.loading-state{text-align:center;padding:40px;color:var(--muted);}
.resource-table{width:100%;border-collapse:collapse;font-size:0.83rem;}
.resource-table th{background:#f0fdf4;color:#065f46;font-weight:700;padding:8px 12px;border-bottom:2px solid var(--border);text-align:left;}
.resource-table td{padding:8px 12px;border-bottom:1px solid #d1fae5;word-break:break-all;}
.resource-table tr:hover td{background:#f0fdf4;}
.type-badge{display:inline-block;padding:2px 8px;border-radius:4px;font-size:0.72rem;font-weight:700;}
.type-html{background:#dbeafe;color:#1d4ed8;}
.type-css{background:#fce7f3;color:#9d174d;}
.type-js{background:#fef9c3;color:#854d0e;}
.type-img{background:#dcfce7;color:#166534;}
.type-font{background:#ede9fe;color:#5b21b6;}
.type-other{background:#f1f5f9;color:#475569;}
.tip-list{list-style:none;padding:0;}
.tip-list li{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid var(--border);}
.tip-list li:last-child{border-bottom:none;}
.tip-icon{font-size:1.1rem;flex-shrink:0;margin-top:1px;}
.tip-text{font-size:0.88rem;}
.tip-text strong{color:var(--text);}
.section-title{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;}
.score-ring{position:relative;width:80px;height:80px;margin:0 auto 8px;}
.score-ring svg{transform:rotate(-90deg);}
.score-ring .score-center{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:1.4rem;font-weight:800;}
.api-note{background:#e0f2fe;border-left:4px solid #0284c7;border-radius:8px;padding:12px 16px;font-size:0.88rem;color:#0c4a6e;margin-bottom:14px;}
</style>

<div class="veloxiq">
  <header class="hero">
    <div class="hero-badge">FREE SPEED TEST</div>
    <h1>VELOXIQ – Website Speed Test</h1>
    <p>Analyze page performance, load times, Core Web Vitals, and resource breakdown. Get actionable recommendations to speed up any website.</p>
  </header>

  <div class="card">
    <div class="api-note">
      ℹ️ This tool fetches performance data via the <strong>Google PageSpeed Insights API</strong> (free, no key needed for basic use). Results reflect real-world performance data.
    </div>
    <div class="search-row">
      <input class="url-input" id="urlInput" type="text" placeholder="https://example.com" value="" />
      <button class="btn btn-primary" onclick="runTest()">Analyze</button>
      <button class="btn btn-ghost" onclick="clearResults()">Clear</button>
    </div>
    <div class="device-chips">
      <span style="font-size:0.82rem;color:var(--muted);align-self:center;">Device:</span>
      <span class="device-chip active" onclick="setDevice('mobile',this)">📱 Mobile</span>
      <span class="device-chip" onclick="setDevice('desktop',this)">🖥 Desktop</span>
    </div>
  </div>

  <div id="loadingState" class="card" style="display:none;">
    <div class="loading-state">
      <div class="loader-ring"></div>
      <p style="margin-top:12px;">Analyzing website performance…<br><small>This may take 10–20 seconds</small></p>
    </div>
  </div>

  <div id="resultsSection" style="display:none;">
    <div class="card">
      <div class="section-title">Core Web Vitals & Performance Score</div>
      <div class="metrics-grid" id="metricsGrid"></div>
    </div>

    <div class="card">
      <div class="section-title">Optimization Opportunities</div>
      <ul class="tip-list" id="tipsList"></ul>
    </div>

    <div class="card" id="resourceCard">
      <div class="section-title">Resource Breakdown</div>
      <div style="overflow:auto;">
        <table class="resource-table" id="resourceTable"></table>
      </div>
    </div>
  </div>
</div>

<script>
let device = 'mobile';

function setDevice(d, el) {
  device = d;
  document.querySelectorAll('.device-chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}

async function runTest() {
  const url = document.getElementById('urlInput').value.trim();
  if (!url) return alert('Please enter a URL to test');

  const fullUrl = url.startsWith('http') ? url : 'https://' + url;
  document.getElementById('loadingState').style.display = 'block';
  document.getElementById('resultsSection').style.display = 'none';

  try {
    const apiUrl = `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${encodeURIComponent(fullUrl)}&strategy=${device}&fields=lighthouseResult,loadingExperience`;
    const res = await fetch(apiUrl);
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.error?.message || 'API error ' + res.status);
    }
    const data = await res.json();
    renderResults(data);
  } catch(err) {
    document.getElementById('loadingState').style.display = 'none';
    document.getElementById('resultsSection').style.display = 'block';
    document.getElementById('metricsGrid').innerHTML = `<div style="grid-column:1/-1;background:#fee2e2;border-left:4px solid #ef4444;border-radius:8px;padding:14px;color:#991b1b;">⚠️ ${err.message}<br><small>Make sure the URL is publicly accessible and try again.</small></div>`;
    document.getElementById('tipsList').innerHTML = '';
    document.getElementById('resourceTable').innerHTML = '';
  }
}

function renderResults(data) {
  const lhr = data.lighthouseResult;
  if (!lhr) { document.getElementById('loadingState').style.display='none'; return; }

  const cats = lhr.categories;
  const audits = lhr.audits;

  const perfScore = Math.round((cats.performance?.score || 0) * 100);
  const metrics = [
    {label:'Performance Score', value: perfScore + '/100', raw: perfScore, unit:'', type:'score'},
    {label:'First Contentful Paint', key:'first-contentful-paint'},
    {label:'Largest Contentful Paint', key:'largest-contentful-paint'},
    {label:'Total Blocking Time', key:'total-blocking-time'},
    {label:'Cumulative Layout Shift', key:'cumulative-layout-shift'},
    {label:'Speed Index', key:'speed-index'},
    {label:'Time to Interactive', key:'interactive'},
  ];

  let gridHtml = '';
  metrics.forEach(m => {
    if (m.type === 'score') {
      const cls = perfScore >= 90 ? 'score-good' : perfScore >= 50 ? 'score-avg' : 'score-poor';
      const fillCls = perfScore >= 90 ? 'fill-good' : perfScore >= 50 ? 'fill-avg' : 'fill-poor';
      gridHtml += `<div class="metric-card"><div class="metric-score ${cls}">${perfScore}</div><div class="metric-label">Performance</div><div class="metric-bar"><div class="metric-fill ${fillCls}" style="width:${perfScore}%"></div></div></div>`;
    } else if (m.key && audits[m.key]) {
      const a = audits[m.key];
      const score = a.score !== null ? Math.round(a.score * 100) : null;
      const cls = score === null ? '' : score >= 90 ? 'score-good' : score >= 50 ? 'score-avg' : 'score-poor';
      const fillCls = score === null ? 'fill-avg' : score >= 90 ? 'fill-good' : score >= 50 ? 'fill-avg' : 'fill-poor';
      gridHtml += `<div class="metric-card"><div class="metric-score ${cls}">${a.displayValue || '—'}</div><div class="metric-label">${m.label}</div><div class="metric-bar"><div class="metric-fill ${fillCls}" style="width:${score||50}%"></div></div></div>`;
    }
  });
  document.getElementById('metricsGrid').innerHTML = gridHtml;

  // Tips
  const opportunities = ['render-blocking-resources','uses-optimized-images','uses-responsive-images',
    'uses-text-compression','uses-long-cache-ttl','efficient-animated-content',
    'unused-css-rules','unused-javascript','uses-webp-images','offscreen-images'];
  let tipsHtml = '';
  opportunities.forEach(key => {
    const a = audits[key];
    if (a && a.score !== null && a.score < 1) {
      const impact = a.score < 0.5 ? '🔴' : a.score < 0.8 ? '🟡' : '🟢';
      tipsHtml += `<li><span class="tip-icon">${impact}</span><span class="tip-text"><strong>${a.title}</strong><br>${a.description?.split('.')[0] || ''}.</span></li>`;
    }
  });
  document.getElementById('tipsList').innerHTML = tipsHtml || '<li><span class="tip-icon">✅</span><span class="tip-text"><strong>Great job!</strong> No major optimization issues found.</span></li>';

  // Resources
  const networkAudit = audits['network-requests'];
  if (networkAudit?.details?.items) {
    const items = networkAudit.details.items.slice(0, 15);
    let tableHtml = '<thead><tr><th>Resource</th><th>Type</th><th>Size</th><th>Duration</th></tr></thead><tbody>';
    items.forEach(item => {
      const url = item.url || '';
      const ext = url.split('?')[0].split('.').pop().toLowerCase();
      const type = ['html','htm'].includes(ext) ? 'html' : ['css'].includes(ext) ? 'css' : ['js'].includes(ext) ? 'js' : ['jpg','jpeg','png','gif','webp','svg','ico'].includes(ext) ? 'img' : ['woff','woff2','ttf','eot'].includes(ext) ? 'font' : 'other';
      const size = item.transferSize ? (item.transferSize / 1024).toFixed(1) + ' KB' : '—';
      const dur = item.endTime && item.startTime ? Math.round(item.endTime - item.startTime) + ' ms' : '—';
      const shortUrl = url.length > 60 ? url.slice(0,58)+'…' : url;
      tableHtml += `<tr><td title="${url}">${escHtml(shortUrl)}</td><td><span class="type-badge type-${type}">${type.toUpperCase()}</span></td><td>${size}</td><td>${dur}</td></tr>`;
    });
    tableHtml += '</tbody>';
    document.getElementById('resourceTable').innerHTML = tableHtml;
  }

  document.getElementById('loadingState').style.display = 'none';
  document.getElementById('resultsSection').style.display = 'block';
}

function clearResults() {
  document.getElementById('urlInput').value = '';
  document.getElementById('loadingState').style.display = 'none';
  document.getElementById('resultsSection').style.display = 'none';
}

function escHtml(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

document.getElementById('urlInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') runTest();
});
</script>
