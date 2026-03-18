---
layout: default
title: "DIFFIQO – Text Diff Checker | Free Online Code & Text Comparison Tool"
excerpt: "Compare two text or code blocks side-by-side with DIFFIQO. Highlights added, removed, and changed lines instantly. Free online diff checker for developers, writers, and QA teams."
date: 2026-03-18
categories: tools
permalink: /tools/diff-checker/
description: "Free online text diff checker and code comparison tool. Highlight differences between two text blocks with line-by-line diff, added/removed highlighting, and copy support."
keywords: ["diff checker online", "text comparison tool", "code diff tool", "compare two texts online", "online diff tool free", "find differences in text", "line diff checker", "code compare online", "text diff highlighter"]
tags: [developer, text, comparator, diff, utility]
---

<style>
:root{--primary:#0f172a;--accent:#6366f1;--success:#10b981;--danger:#ef4444;--warn:#f59e0b;--bg:#f8fafc;--card:#fff;--text:#0f172a;--muted:#64748b;--border:#e2e8f0;--shadow:0 8px 32px rgba(15,23,42,0.08);--add:#dcfce7;--add-text:#166534;--del:#fee2e2;--del-text:#991b1b;--chg:#fef9c3;--chg-text:#854d0e;}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.diffiqo{max-width:1200px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--accent),#8b5cf6);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--accent),#8b5cf6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.toolbar{display:flex;gap:10px;margin-bottom:14px;flex-wrap:wrap;align-items:center;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-accent{background:var(--accent);color:#fff;}
.btn-accent:hover{background:#4f46e5;transform:translateY(-1px);}
.btn-ghost{background:var(--bg);color:var(--accent);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--accent);}
.editors{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.editor-label{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;display:flex;justify-content:space-between;}
textarea{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.85rem;background:var(--card);color:var(--text);resize:vertical;line-height:1.6;}
textarea:focus{outline:none;border-color:var(--accent);}
.diff-output{margin-top:6px;}
.diff-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;flex-wrap:wrap;gap:8px;}
.stat-chips{display:flex;gap:8px;}
.stat-chip{padding:4px 12px;border-radius:20px;font-size:0.8rem;font-weight:700;}
.add-chip{background:var(--add);color:var(--add-text);}
.del-chip{background:var(--del);color:var(--del-text);}
.chg-chip{background:var(--chg);color:var(--chg-text);}
.diff-table{width:100%;border-collapse:collapse;font-family:Consolas,'Courier New',monospace;font-size:0.83rem;}
.diff-table td{padding:4px 10px;white-space:pre-wrap;word-break:break-all;vertical-align:top;border-bottom:1px solid var(--border);}
.diff-table td:first-child{width:44px;color:var(--muted);text-align:right;user-select:none;border-right:2px solid var(--border);padding-right:8px;}
.diff-table td:nth-child(2){width:20px;text-align:center;font-weight:700;}
.line-add{background:var(--add);color:var(--add-text);}
.line-del{background:var(--del);color:var(--del-text);}
.line-eq{background:var(--card);}
.mode-chips{display:flex;gap:8px;}
.mode-chip{padding:5px 14px;border-radius:20px;border:1px solid var(--border);font-size:0.82rem;font-weight:600;cursor:pointer;transition:all 0.2s;}
.mode-chip.active{background:var(--accent);color:#fff;border-color:var(--accent);}
.legend{display:flex;gap:12px;flex-wrap:wrap;}
.leg{display:flex;align-items:center;gap:6px;font-size:0.82rem;}
.leg-box{width:14px;height:14px;border-radius:3px;}
@media(max-width:700px){.editors{grid-template-columns:1fr;}}
</style>

<div class="diffiqo">
  <header class="hero">
    <div class="hero-badge">FREE DIFF CHECKER</div>
    <h1>DIFFIQO – Text Diff Checker</h1>
    <p>Compare any two texts, code blocks, or files side-by-side with instant line-by-line highlighting of all additions, deletions, and changes.</p>
  </header>

  <div class="card">
    <div class="toolbar">
      <button class="btn btn-accent" onclick="computeDiff()">Compare</button>
      <button class="btn btn-ghost" onclick="swapTexts()">⇄ Swap</button>
      <button class="btn btn-ghost" onclick="clearAll()">Clear</button>
      <div class="mode-chips">
        <span class="mode-chip active" onclick="setMode('line',this)">Line</span>
        <span class="mode-chip" onclick="setMode('word',this)">Word</span>
        <span class="mode-chip" onclick="setMode('char',this)">Char</span>
      </div>
      <label style="font-size:0.85rem;color:var(--muted);display:flex;align-items:center;gap:6px;">
        <input type="checkbox" id="ignoreCase"> Ignore case
      </label>
      <label style="font-size:0.85rem;color:var(--muted);display:flex;align-items:center;gap:6px;">
        <input type="checkbox" id="ignoreWhitespace"> Ignore whitespace
      </label>
    </div>

    <div class="editors">
      <div>
        <div class="editor-label"><span>Original Text (A)</span></div>
        <textarea id="textA" rows="12" placeholder="Paste original text here…"></textarea>
      </div>
      <div>
        <div class="editor-label"><span>Modified Text (B)</span></div>
        <textarea id="textB" rows="12" placeholder="Paste modified text here…"></textarea>
      </div>
    </div>
  </div>

  <div id="diffCard" class="card" style="display:none;">
    <div class="diff-header">
      <div class="stat-chips" id="diffStats"></div>
      <div class="legend">
        <div class="leg"><div class="leg-box" style="background:var(--add);"></div>Added</div>
        <div class="leg"><div class="leg-box" style="background:var(--del);"></div>Removed</div>
        <div class="leg"><div class="leg-box" style="background:var(--card);border:1px solid var(--border);"></div>Unchanged</div>
      </div>
      <button class="btn btn-ghost" onclick="copyDiff()" style="font-size:0.82rem;padding:6px 12px;">Copy Diff</button>
    </div>
    <div class="diff-output" id="diffOutput"></div>
  </div>
</div>

<script>
let diffMode = 'line';

function setMode(m, el) {
  diffMode = m;
  document.querySelectorAll('.mode-chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}

function normalize(s) {
  if (document.getElementById('ignoreCase').checked) s = s.toLowerCase();
  if (document.getElementById('ignoreWhitespace').checked) s = s.replace(/\s+/g, ' ').trim();
  return s;
}

function tokenize(text) {
  if (diffMode === 'line') return text.split('\n');
  if (diffMode === 'word') return text.match(/\S+|\s+/g) || [];
  return text.split('');
}

function lcs(a, b) {
  const m = a.length, n = b.length;
  const dp = Array.from({length:m+1}, () => new Array(n+1).fill(0));
  for (let i=1;i<=m;i++) for (let j=1;j<=n;j++) {
    if (normalize(a[i-1]) === normalize(b[j-1])) dp[i][j] = dp[i-1][j-1]+1;
    else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
  }
  const seq = [];
  let i=m,j=n;
  while(i>0&&j>0){
    if(normalize(a[i-1])===normalize(b[j-1])){seq.unshift({type:'eq',val:a[i-1]});i--;j--;}
    else if(dp[i-1][j]>dp[i][j-1]){seq.unshift({type:'del',val:a[i-1]});i--;}
    else{seq.unshift({type:'ins',val:b[j-1]});j--;}
  }
  while(i>0){seq.unshift({type:'del',val:a[i-1]});i--;}
  while(j>0){seq.unshift({type:'ins',val:b[j-1]});j--;}
  return seq;
}

function computeDiff() {
  const a = document.getElementById('textA').value;
  const b = document.getElementById('textB').value;
  if (!a && !b) return;

  const tokA = tokenize(a), tokB = tokenize(b);
  const diff = lcs(tokA, tokB);

  let added = 0, deleted = 0, lineNum = 1;
  let html = '<table class="diff-table"><tbody>';

  diff.forEach(d => {
    const escaped = escHtml(d.val);
    if (d.type === 'eq') {
      html += `<tr class="line-eq"><td>${diffMode==='line'?lineNum++:''}</td><td></td><td>${escaped}</td></tr>`;
    } else if (d.type === 'ins') {
      added++;
      html += `<tr class="line-add"><td>${diffMode==='line'?lineNum++:''}</td><td style="color:var(--add-text);">+</td><td>${escaped}</td></tr>`;
    } else {
      deleted++;
      html += `<tr class="line-del"><td></td><td style="color:var(--del-text);">−</td><td>${escaped}</td></tr>`;
    }
  });

  html += '</tbody></table>';
  document.getElementById('diffOutput').innerHTML = html;
  document.getElementById('diffStats').innerHTML =
    `<span class="stat-chip add-chip">+${added} added</span>
     <span class="stat-chip del-chip">−${deleted} removed</span>
     <span class="stat-chip chg-chip">${Math.abs(added-deleted)} net change</span>`;
  document.getElementById('diffCard').style.display = 'block';
}

function swapTexts() {
  const a = document.getElementById('textA').value;
  const b = document.getElementById('textB').value;
  document.getElementById('textA').value = b;
  document.getElementById('textB').value = a;
}

function clearAll() {
  document.getElementById('textA').value = '';
  document.getElementById('textB').value = '';
  document.getElementById('diffCard').style.display = 'none';
}

function copyDiff() {
  const rows = document.querySelectorAll('.diff-table tr');
  let text = '';
  rows.forEach(r => {
    const sign = r.querySelector('td:nth-child(2)').textContent.trim();
    const content = r.querySelector('td:nth-child(3)').textContent;
    text += (sign || ' ') + ' ' + content + '\n';
  });
  navigator.clipboard.writeText(text).then(() => alert('Diff copied to clipboard!'));
}

function escHtml(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
</script>
