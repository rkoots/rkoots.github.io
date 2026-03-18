---
layout: default
title: "DATAVIA – JSON to CSV Converter | Free Online Data Transformation Tool"
excerpt: "Convert JSON to CSV instantly with DATAVIA. Supports nested objects, arrays, custom delimiters, live preview, file upload, and download. Free online JSON to CSV converter."
date: 2026-03-18
categories: tools
permalink: /tools/json-to-csv/
description: "Free online JSON to CSV converter. Transform JSON arrays to CSV with custom delimiter, header options, nested field flattening, and instant download. No sign-up required."
keywords: ["json to csv converter", "convert json to csv online", "json to csv free tool", "json csv transformer", "export json as csv", "json array to csv", "online data converter", "json to spreadsheet", "json to excel csv"]
tags: [JSON, CSV, converter, data, developer]
---

<style>
:root{--primary:#0284c7;--primary-dark:#0369a1;--accent:#10b981;--bg:#f0f9ff;--card:#fff;--text:#0c4a6e;--muted:#6b7280;--border:#bae6fd;--shadow:0 8px 32px rgba(2,132,199,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.datavia{max-width:1100px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.toolbar{display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap;align-items:center;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-success{background:var(--accent);color:#fff;}
.btn-success:hover{filter:brightness(1.1);}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);}
select.opt,input.opt{padding:8px 12px;border-radius:8px;border:1px solid var(--border);background:var(--card);color:var(--text);font-size:0.88rem;}
.editors{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.editor-label{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;}
textarea{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.85rem;background:var(--card);color:var(--text);resize:vertical;line-height:1.5;}
textarea:focus{outline:none;border-color:var(--primary);}
.output-box{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.83rem;background:#f0f9ff;white-space:pre-wrap;word-break:break-all;min-height:200px;max-height:400px;overflow:auto;color:var(--text);}
.preview-table{width:100%;border-collapse:collapse;font-size:0.83rem;margin-top:10px;}
.preview-table th{background:#e0f2fe;color:var(--primary-dark);padding:8px 12px;border:1px solid var(--border);font-weight:700;text-align:left;}
.preview-table td{padding:7px 12px;border:1px solid var(--border);}
.preview-table tr:nth-child(even) td{background:#f0f9ff;}
.stats{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px;}
.stat-chip{padding:4px 12px;border-radius:20px;font-size:0.8rem;font-weight:600;background:#e0f2fe;color:var(--primary-dark);}
.error-msg{background:#fee2e2;border-left:4px solid #ef4444;border-radius:8px;padding:12px;color:#991b1b;font-size:0.9rem;margin-top:10px;}
.file-btn{padding:8px 14px;border-radius:8px;border:1px dashed var(--border);background:var(--card);color:var(--primary);cursor:pointer;font-size:0.85rem;font-weight:600;}
.file-btn:hover{border-color:var(--primary);}
@media(max-width:700px){.editors{grid-template-columns:1fr;}}
</style>

<div class="datavia">
  <header class="hero">
    <div class="hero-badge">FREE DATA CONVERTER</div>
    <h1>DATAVIA – JSON to CSV Converter</h1>
    <p>Transform JSON arrays into CSV instantly. Upload a file or paste JSON, choose delimiter options, preview the table, and download your data.</p>
  </header>

  <div class="card">
    <div class="toolbar">
      <button class="btn btn-primary" onclick="convertJSON()">Convert to CSV</button>
      <button class="btn btn-success" onclick="downloadCSV()">Download CSV</button>
      <button class="btn btn-ghost" onclick="copyCSV()">Copy CSV</button>
      <button class="btn btn-ghost" onclick="loadSample()">Load Sample</button>
      <button class="btn btn-ghost" onclick="clearAll()">Clear</button>
      <label class="file-btn">📂 Upload JSON <input type="file" accept=".json,application/json" style="display:none;" onchange="loadFile(this)"></label>
      <select class="opt" id="delimiter">
        <option value=",">Comma (,)</option>
        <option value=";">Semicolon (;)</option>
        <option value="\t">Tab (\t)</option>
        <option value="|">Pipe (|)</option>
      </select>
      <label style="font-size:0.85rem;color:var(--muted);display:flex;align-items:center;gap:6px;">
        <input type="checkbox" id="includeHeader" checked> Include header row
      </label>
      <label style="font-size:0.85rem;color:var(--muted);display:flex;align-items:center;gap:6px;">
        <input type="checkbox" id="flattenNested"> Flatten nested
      </label>
    </div>

    <div class="editors">
      <div>
        <div class="editor-label">JSON Input</div>
        <textarea id="jsonInput" rows="14" placeholder='Paste JSON array here, e.g.
[
  {"name":"Alice","age":30,"city":"New York"},
  {"name":"Bob","age":25,"city":"London"}
]'></textarea>
      </div>
      <div>
        <div class="editor-label">CSV Output</div>
        <div class="output-box" id="csvOutput">CSV output will appear here…</div>
        <div class="stats" id="statsBar" style="display:none;"></div>
      </div>
    </div>

    <div id="errorMsg" class="error-msg" style="display:none;"></div>
  </div>

  <div id="previewCard" class="card" style="display:none;">
    <div class="editor-label" style="margin-bottom:10px;">Table Preview (first 10 rows)</div>
    <div style="overflow:auto;">
      <table class="preview-table" id="previewTable"></table>
    </div>
  </div>
</div>

<script>
let csvData = '';

const SAMPLE = JSON.stringify([
  {"id":1,"name":"Alice Johnson","email":"alice@example.com","age":30,"city":"New York","active":true},
  {"id":2,"name":"Bob Smith","email":"bob@example.com","age":25,"city":"London","active":false},
  {"id":3,"name":"Carol White","email":"carol@example.com","age":35,"city":"Paris","active":true},
  {"id":4,"name":"David Brown","email":"david@example.com","age":28,"city":"Tokyo","active":true}
], null, 2);

function loadSample() {
  document.getElementById('jsonInput').value = SAMPLE;
  convertJSON();
}

function loadFile(input) {
  const file = input.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => {
    document.getElementById('jsonInput').value = e.target.result;
    convertJSON();
  };
  reader.readAsText(file);
}

function flattenObject(obj, prefix='') {
  const result = {};
  for (const [k, v] of Object.entries(obj)) {
    const key = prefix ? `${prefix}.${k}` : k;
    if (v && typeof v === 'object' && !Array.isArray(v) && document.getElementById('flattenNested').checked) {
      Object.assign(result, flattenObject(v, key));
    } else {
      result[key] = Array.isArray(v) ? JSON.stringify(v) : v;
    }
  }
  return result;
}

function escapeCSVField(val, delim) {
  const str = val === null || val === undefined ? '' : String(val);
  if (str.includes(delim) || str.includes('"') || str.includes('\n') || str.includes('\r')) {
    return '"' + str.replace(/"/g, '""') + '"';
  }
  return str;
}

function convertJSON() {
  const raw = document.getElementById('jsonInput').value.trim();
  const delimRaw = document.getElementById('delimiter').value;
  const delim = delimRaw === '\\t' ? '\t' : delimRaw;
  const includeHeader = document.getElementById('includeHeader').checked;
  const errorDiv = document.getElementById('errorMsg');
  errorDiv.style.display = 'none';

  if (!raw) return;

  let data;
  try { data = JSON.parse(raw); } catch(e) {
    errorDiv.textContent = '⚠️ Invalid JSON: ' + e.message;
    errorDiv.style.display = 'block';
    return;
  }

  if (!Array.isArray(data)) {
    if (typeof data === 'object' && data !== null) data = [data];
    else { errorDiv.textContent = '⚠️ JSON must be an array of objects or a single object.'; errorDiv.style.display = 'block'; return; }
  }

  const rows = data.map(item => flattenObject(item));
  const allKeys = [...new Set(rows.flatMap(r => Object.keys(r)))];

  let csv = '';
  if (includeHeader) csv += allKeys.map(k => escapeCSVField(k, delim)).join(delim) + '\n';
  rows.forEach(row => {
    csv += allKeys.map(k => escapeCSVField(row[k], delim)).join(delim) + '\n';
  });

  csvData = csv;
  document.getElementById('csvOutput').textContent = csv;
  document.getElementById('statsBar').innerHTML =
    `<span class="stat-chip">${rows.length} rows</span><span class="stat-chip">${allKeys.length} columns</span><span class="stat-chip">${csv.length} chars</span>`;
  document.getElementById('statsBar').style.display = 'flex';

  renderPreview(allKeys, rows);
}

function renderPreview(headers, rows) {
  const maxRows = Math.min(10, rows.length);
  let html = '<thead><tr>' + headers.map(h => `<th>${escHtml(h)}</th>`).join('') + '</tr></thead><tbody>';
  for (let i=0;i<maxRows;i++) {
    html += '<tr>' + headers.map(h => `<td>${escHtml(String(rows[i][h] ?? ''))}</td>`).join('') + '</tr>';
  }
  html += '</tbody>';
  document.getElementById('previewTable').innerHTML = html;
  document.getElementById('previewCard').style.display = 'block';
}

function downloadCSV() {
  if (!csvData) return alert('Convert JSON first');
  const blob = new Blob([csvData], {type:'text/csv'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'data.csv';
  a.click();
}

function copyCSV() {
  if (!csvData) return alert('Convert JSON first');
  navigator.clipboard.writeText(csvData).then(() => alert('CSV copied to clipboard!'));
}

function clearAll() {
  document.getElementById('jsonInput').value = '';
  document.getElementById('csvOutput').textContent = 'CSV output will appear here…';
  document.getElementById('statsBar').style.display = 'none';
  document.getElementById('previewCard').style.display = 'none';
  csvData = '';
}

function escHtml(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
</script>
