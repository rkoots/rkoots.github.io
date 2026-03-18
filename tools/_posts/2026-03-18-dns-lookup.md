---
layout: default
title: "DNSVEX – DNS Lookup Tool | Free Online DNS Record Checker & Propagation Tester"
excerpt: "Check DNS records instantly with DNSVEX. Query A, AAAA, MX, TXT, CNAME, NS, SOA records for any domain. Free online DNS lookup tool with real-time propagation checking."
date: 2026-03-18
categories: tools
permalink: /tools/dns-lookup/
description: "Free online DNS lookup tool. Check A, AAAA, MX, TXT, CNAME, NS, SOA, and PTR records for any domain. Real-time DNS propagation checker for developers and sysadmins."
keywords: ["dns lookup tool", "dns record checker", "check dns records online", "mx record lookup", "txt record lookup", "cname lookup", "dns propagation checker", "nslookup online", "dns query tool free"]
tags: [DNS, networking, lookup, sysadmin, developer]
---

<style>
:root{--primary:#059669;--primary-dark:#047857;--accent:#6366f1;--bg:#f0fdf4;--card:#fff;--text:#052e16;--muted:#6b7280;--border:#a7f3d0;--shadow:0 8px 32px rgba(5,150,105,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.dnsvex{max-width:960px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.search-row{display:flex;gap:10px;flex-wrap:wrap;}
.domain-input{flex:1;padding:12px 16px;border-radius:10px;border:2px solid var(--border);background:var(--card);color:var(--text);font-size:1rem;font-family:Consolas,'Courier New',monospace;min-width:200px;}
.domain-input:focus{outline:none;border-color:var(--primary);}
select.type-select{padding:12px 14px;border-radius:10px;border:2px solid var(--border);background:var(--card);color:var(--text);font-size:0.95rem;cursor:pointer;}
.btn{padding:12px 24px;border-radius:10px;border:none;cursor:pointer;font-size:0.95rem;font-weight:700;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.type-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px;}
.chip{padding:5px 14px;border-radius:20px;border:1px solid var(--border);background:var(--card);color:var(--text);font-size:0.82rem;font-weight:600;cursor:pointer;transition:all 0.2s;}
.chip:hover,.chip.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.result-table{width:100%;border-collapse:collapse;font-size:0.88rem;}
.result-table th{background:#f0fdf4;color:#065f46;font-weight:700;padding:10px 14px;text-align:left;border-bottom:2px solid var(--border);}
.result-table td{padding:10px 14px;border-bottom:1px solid #d1fae5;word-break:break-all;font-family:Consolas,'Courier New',monospace;}
.result-table tr:last-child td{border-bottom:none;}
.result-table tr:hover td{background:#f0fdf4;}
.record-type{display:inline-block;padding:2px 8px;border-radius:4px;font-size:0.75rem;font-weight:700;background:#dcfce7;color:#15803d;}
.ttl-badge{color:#6b7280;font-size:0.82rem;}
.no-records{text-align:center;padding:30px;color:var(--muted);}
.loader{text-align:center;padding:30px;color:var(--muted);}
.error-msg{background:#fee2e2;border-left:4px solid #ef4444;border-radius:8px;padding:12px 16px;color:#991b1b;font-size:0.9rem;}
.section-title{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;}
.copy-btn{float:right;padding:4px 10px;border:none;background:#d1fae5;color:#065f46;border-radius:6px;cursor:pointer;font-size:0.8rem;}
</style>

<div class="dnsvex">
  <header class="hero">
    <div class="hero-badge">FREE DNS LOOKUP</div>
    <h1>DNSVEX – DNS Lookup Tool</h1>
    <p>Query any DNS record type for any domain in real-time. Check A, MX, TXT, CNAME, NS, SOA records instantly using Google's DNS-over-HTTPS API.</p>
  </header>

  <div class="card">
    <div class="search-row">
      <input class="domain-input" id="domainInput" type="text" placeholder="Enter domain (e.g. google.com)" />
      <select class="type-select" id="recordType">
        <option value="A">A</option>
        <option value="AAAA">AAAA</option>
        <option value="MX">MX</option>
        <option value="TXT">TXT</option>
        <option value="CNAME">CNAME</option>
        <option value="NS">NS</option>
        <option value="SOA">SOA</option>
        <option value="PTR">PTR</option>
        <option value="SRV">SRV</option>
        <option value="CAA">CAA</option>
      </select>
      <button class="btn btn-primary" onclick="lookupDNS()">Lookup</button>
    </div>
    <div class="type-chips" id="typeChips">
      <span class="chip active" onclick="quickLookup('A',this)">A</span>
      <span class="chip" onclick="quickLookup('AAAA',this)">AAAA</span>
      <span class="chip" onclick="quickLookup('MX',this)">MX</span>
      <span class="chip" onclick="quickLookup('TXT',this)">TXT</span>
      <span class="chip" onclick="quickLookup('CNAME',this)">CNAME</span>
      <span class="chip" onclick="quickLookup('NS',this)">NS</span>
      <span class="chip" onclick="quickLookup('SOA',this)">SOA</span>
      <span class="chip" onclick="quickLookup('PTR',this)">PTR</span>
    </div>
  </div>

  <div id="resultSection" style="display:none;">
    <div class="card">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
        <span class="section-title" id="resultTitle"></span>
        <button class="copy-btn" onclick="copyResults()">Copy All</button>
      </div>
      <div id="resultContent"></div>
    </div>
  </div>

  <div class="card" style="margin-top:8px;">
    <div class="section-title">Common DNS Record Types</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;">
      <div style="padding:12px;background:#f0fdf4;border-radius:8px;"><strong style="color:var(--primary);">A Record</strong><br><span style="font-size:0.85rem;color:var(--muted);">Maps domain to IPv4 address</span></div>
      <div style="padding:12px;background:#f0fdf4;border-radius:8px;"><strong style="color:var(--primary);">AAAA Record</strong><br><span style="font-size:0.85rem;color:var(--muted);">Maps domain to IPv6 address</span></div>
      <div style="padding:12px;background:#f0fdf4;border-radius:8px;"><strong style="color:var(--primary);">MX Record</strong><br><span style="font-size:0.85rem;color:var(--muted);">Mail server routing records</span></div>
      <div style="padding:12px;background:#f0fdf4;border-radius:8px;"><strong style="color:var(--primary);">TXT Record</strong><br><span style="font-size:0.85rem;color:var(--muted);">SPF, DKIM, DMARC, and verification</span></div>
      <div style="padding:12px;background:#f0fdf4;border-radius:8px;"><strong style="color:var(--primary);">CNAME Record</strong><br><span style="font-size:0.85rem;color:var(--muted);">Alias pointing to another domain</span></div>
      <div style="padding:12px;background:#f0fdf4;border-radius:8px;"><strong style="color:var(--primary);">NS Record</strong><br><span style="font-size:0.85rem;color:var(--muted);">Authoritative nameservers</span></div>
    </div>
  </div>
</div>

<script>
const TYPE_MAP = {A:1,AAAA:28,MX:15,TXT:16,CNAME:5,NS:2,SOA:6,PTR:12,SRV:33,CAA:257};

function quickLookup(type, el) {
  document.getElementById('recordType').value = type;
  document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  if (document.getElementById('domainInput').value.trim()) lookupDNS();
}

async function lookupDNS() {
  const domain = document.getElementById('domainInput').value.trim().replace(/^https?:\/\//,'').replace(/\/.*/,'');
  const type = document.getElementById('recordType').value;
  if (!domain) return alert('Please enter a domain name');

  const section = document.getElementById('resultSection');
  const content = document.getElementById('resultContent');
  const title = document.getElementById('resultTitle');
  section.style.display = 'block';
  content.innerHTML = '<div class="loader">🔍 Querying DNS records…</div>';
  title.textContent = `${type} Records for ${domain}`;

  try {
    const typeNum = TYPE_MAP[type] || 1;
    const res = await fetch(`https://dns.google/resolve?name=${encodeURIComponent(domain)}&type=${typeNum}`);
    if (!res.ok) throw new Error('DNS API error');
    const data = await res.json();

    if (!data.Answer || data.Answer.length === 0) {
      content.innerHTML = `<div class="no-records">No ${type} records found for <strong>${domain}</strong></div>`;
      return;
    }

    let rows = '';
    data.Answer.forEach(r => {
      const typeLabel = getTypeName(r.type);
      rows += `<tr>
        <td><span class="record-type">${typeLabel}</span></td>
        <td>${escHtml(r.name)}</td>
        <td>${escHtml(String(r.data))}</td>
        <td class="ttl-badge">${r.TTL}s</td>
      </tr>`;
    });

    content.innerHTML = `
      <table class="result-table">
        <thead><tr><th>Type</th><th>Name</th><th>Value</th><th>TTL</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>`;
  } catch(err) {
    content.innerHTML = `<div class="error-msg">⚠️ ${err.message}. Check the domain name and try again.</div>`;
  }
}

function getTypeName(n) {
  const m = {1:'A',2:'NS',5:'CNAME',6:'SOA',12:'PTR',15:'MX',16:'TXT',28:'AAAA',33:'SRV',257:'CAA'};
  return m[n] || String(n);
}

function escHtml(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function copyResults() {
  const rows = document.querySelectorAll('.result-table tbody tr');
  let text = '';
  rows.forEach(r => {
    const cells = r.querySelectorAll('td');
    text += [...cells].map(c => c.textContent.trim()).join('\t') + '\n';
  });
  navigator.clipboard.writeText(text).then(() => alert('Records copied to clipboard!'));
}

document.getElementById('domainInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') lookupDNS();
});
</script>
