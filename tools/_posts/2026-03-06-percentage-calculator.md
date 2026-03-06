---
layout: default
title: "PERCIVIA – Percentage Calculator | Profit, Discount, Markup & More"
excerpt: "Calculate percentages instantly — X% of Y, percentage increase/decrease, profit margin, discount, markup. Includes visual percentage bars and example use cases."
date: 2026-03-06
categories: tools
permalink: /tools/percentage-calculator/
logo_svg: /assets/images/tools/logos/percentage-calculator.svg
description: "Free online percentage calculator with multiple modes: X% of Y, percentage increase/decrease, profit margin, discount calculator, markup calculator. Visual bars and instant results."
keywords: ["percentage calculator", "percent of a number", "percentage increase calculator", "discount calculator", "profit margin calculator", "markup calculator", "percentage decrease", "online percentage tool"]
tags: [calculator, percentage, finance, math, discount]
---

<style>
:root{--primary:#f59e0b;--primary-dark:#d97706;--accent:#10b981;--success:#10b981;--danger:#ef4444;--bg:#fffbeb;--card:#fff;--text:#1c1409;--muted:#6b7280;--border:#fde68a;--shadow:0 8px 32px rgba(245,158,11,0.12);}
[data-theme="dark"]{--bg:#1a1200;--card:#231900;--text:#fef9c3;--muted:#9ca3af;--border:#78350f;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;transition:background 0.3s,color 0.3s;}
.percivia{max-width:860px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:40px 20px 32px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),#fbbf24);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:800;background:linear-gradient(135deg,var(--primary),#fbbf24,#10b981);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}
.hero p{color:var(--muted);font-size:1.05rem;max-width:560px;margin:0 auto;}
.toolbar{display:flex;justify-content:flex-end;gap:10px;margin-bottom:16px;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-ghost{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);color:var(--primary);}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.card{background:var(--card);border-radius:16px;padding:28px;box-shadow:var(--shadow);border:1px solid var(--border);margin-bottom:24px;}
.card-title{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:20px;display:flex;align-items:center;gap:8px;}
.mode-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:24px;}
.mode-tab{padding:9px 18px;border-radius:20px;border:1.5px solid var(--border);background:var(--bg);color:var(--muted);font-size:0.85rem;font-weight:600;cursor:pointer;transition:all 0.2s;}
.mode-tab.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.mode-panel{display:none;}
.mode-panel.active{display:block;}
.calc-row{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:16px;}
.calc-row input{padding:12px 16px;border:2px solid var(--border);border-radius:10px;background:var(--bg);color:var(--text);font-size:1.1rem;font-weight:700;width:140px;transition:border-color 0.2s;}
.calc-row input:focus{outline:none;border-color:var(--primary);}
.calc-row span{font-size:1.1rem;font-weight:600;color:var(--muted);white-space:nowrap;}
.result-card{background:linear-gradient(135deg,var(--primary),#fbbf24);border-radius:14px;padding:24px;text-align:center;color:#fff;margin-top:16px;animation:fadeIn 0.4s;}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:none;}}
.result-val{font-size:3rem;font-weight:800;line-height:1;}
.result-label{font-size:0.9rem;opacity:0.85;margin-top:6px;}
.result-secondary{font-size:1rem;margin-top:10px;opacity:0.9;}
.pct-bar-wrap{margin-top:18px;}
.pct-bar-label{display:flex;justify-content:space-between;font-size:0.82rem;margin-bottom:5px;color:rgba(255,255,255,0.8);}
.pct-bar{height:14px;background:rgba(255,255,255,0.3);border-radius:20px;overflow:hidden;}
.pct-fill{height:100%;background:#fff;border-radius:20px;transition:width 0.9s cubic-bezier(.4,0,.2,1);}
.examples-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:16px;}
.example-item{padding:14px;background:var(--bg);border:1px solid var(--border);border-radius:10px;cursor:pointer;transition:all 0.2s;}
.example-item:hover{border-color:var(--primary);background:rgba(245,158,11,0.05);}
.example-item .ei-q{font-size:0.85rem;font-weight:600;color:var(--text);}
.example-item .ei-a{font-size:1rem;font-weight:800;color:var(--primary);margin-top:4px;}
.hidden{display:none;}
.seo-block{margin-top:48px;padding:32px;background:var(--card);border-radius:16px;border:1px solid var(--border);}
.seo-block h2{font-size:1.5rem;font-weight:700;color:var(--primary);margin-bottom:16px;}
.seo-block h3{font-size:1.1rem;font-weight:600;margin:20px 0 8px;}
.seo-block p,.seo-block li{color:var(--muted);line-height:1.7;font-size:0.95rem;}
.seo-block ul{padding-left:20px;}
.faq-item{border-bottom:1px solid var(--border);padding:16px 0;}
.faq-q{font-weight:600;cursor:pointer;display:flex;justify-content:space-between;color:var(--text);}
.faq-a{color:var(--muted);font-size:0.9rem;line-height:1.6;padding-top:10px;}
.related-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-top:16px;}
.related-card{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center;text-decoration:none;transition:all 0.2s;}
.related-card:hover{border-color:var(--primary);transform:translateY(-2px);}
.related-card .rc-emoji{font-size:1.6rem;}
.related-card .rc-name{font-size:0.85rem;font-weight:600;color:var(--text);margin-top:6px;}
</style>

<div class="percivia">
  <div class="hero">
    <div class="hero-badge">📊 PERCIVIA</div>
    <h1>Percentage Calculator</h1>
    <p>Calculate percentages, discounts, profit margins, markup, and more — with visual bars.</p>
  </div>

  <div class="toolbar">
    <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Toggle Theme</button>
    <button class="btn btn-ghost" onclick="resetAll()">↺ Reset</button>
  </div>

  <div class="card">
    <div class="card-title">🔢 Calculation Mode</div>
    <div class="mode-tabs">
      <button class="mode-tab active" onclick="setMode('basic',this)">X% of Y</button>
      <button class="mode-tab" onclick="setMode('increase',this)">% Increase</button>
      <button class="mode-tab" onclick="setMode('decrease',this)">% Decrease</button>
      <button class="mode-tab" onclick="setMode('margin',this)">Profit Margin</button>
      <button class="mode-tab" onclick="setMode('discount',this)">Discount</button>
      <button class="mode-tab" onclick="setMode('markup',this)">Markup</button>
    </div>

    <!-- Basic -->
    <div id="panel-basic" class="mode-panel active">
      <div class="calc-row">
        <input type="number" id="b-pct" placeholder="%" oninput="calcBasic()">
        <span>% of</span>
        <input type="number" id="b-val" placeholder="value" oninput="calcBasic()">
        <span>=</span>
        <strong id="b-result" style="font-size:1.3rem;color:var(--primary);">?</strong>
      </div>
    </div>

    <!-- Increase -->
    <div id="panel-increase" class="mode-panel">
      <div class="calc-row">
        <span>From</span>
        <input type="number" id="inc-from" placeholder="old value" oninput="calcIncrease()">
        <span>to</span>
        <input type="number" id="inc-to" placeholder="new value" oninput="calcIncrease()">
      </div>
    </div>

    <!-- Decrease -->
    <div id="panel-decrease" class="mode-panel">
      <div class="calc-row">
        <span>From</span>
        <input type="number" id="dec-from" placeholder="old value" oninput="calcDecrease()">
        <span>to</span>
        <input type="number" id="dec-to" placeholder="new value" oninput="calcDecrease()">
      </div>
    </div>

    <!-- Margin -->
    <div id="panel-margin" class="mode-panel">
      <div class="calc-row">
        <span>Cost</span>
        <input type="number" id="mg-cost" placeholder="cost" oninput="calcMargin()">
        <span>Revenue</span>
        <input type="number" id="mg-rev" placeholder="revenue" oninput="calcMargin()">
      </div>
    </div>

    <!-- Discount -->
    <div id="panel-discount" class="mode-panel">
      <div class="calc-row">
        <span>Original Price</span>
        <input type="number" id="dc-price" placeholder="price" oninput="calcDiscount()">
        <span>Discount</span>
        <input type="number" id="dc-pct" placeholder="%" oninput="calcDiscount()">
        <span>%</span>
      </div>
    </div>

    <!-- Markup -->
    <div id="panel-markup" class="mode-panel">
      <div class="calc-row">
        <span>Cost</span>
        <input type="number" id="mu-cost" placeholder="cost" oninput="calcMarkup()">
        <span>Markup</span>
        <input type="number" id="mu-pct" placeholder="%" oninput="calcMarkup()">
        <span>%</span>
      </div>
    </div>

    <div id="result-card" class="result-card hidden">
      <div class="result-val" id="main-result">0</div>
      <div class="result-label" id="result-label">Result</div>
      <div class="result-secondary" id="result-secondary"></div>
      <div class="pct-bar-wrap">
        <div class="pct-bar-label"><span id="bar-left">0%</span><span id="bar-right">100%</span></div>
        <div class="pct-bar"><div class="pct-fill" id="pct-fill" style="width:0%"></div></div>
      </div>
    </div>

    <div style="margin-top:14px;display:flex;gap:10px;flex-wrap:wrap;">
      <button class="btn btn-primary" onclick="shareResult()">📤 Share Result</button>
      <button class="btn btn-ghost" onclick="copyResult()">📋 Copy</button>
    </div>
  </div>

  <div class="card">
    <div class="card-title">💡 Example Calculations</div>
    <div class="examples-grid" id="examples-grid"></div>
  </div>

  <div class="seo-block">
    <h2>How to Calculate Percentages</h2>
    <p>Percentage calculations are fundamental to everyday mathematics — from understanding sale discounts to calculating profit margins and tax. PERCIVIA covers all six common percentage scenarios with instant visual feedback.</p>
    <h3>Formula Reference</h3>
    <ul>
      <li><strong>X% of Y:</strong> Result = (X / 100) × Y</li>
      <li><strong>Percentage increase:</strong> ((New − Old) / Old) × 100</li>
      <li><strong>Percentage decrease:</strong> ((Old − New) / Old) × 100</li>
      <li><strong>Profit margin:</strong> ((Revenue − Cost) / Revenue) × 100</li>
      <li><strong>Discount price:</strong> Original × (1 − Discount% / 100)</li>
      <li><strong>Markup price:</strong> Cost × (1 + Markup% / 100)</li>
    </ul>
    <h3>Difference Between Margin and Markup</h3>
    <p>Margin is calculated as a percentage of the selling price, while markup is calculated as a percentage of the cost. For example, a product costing ₹100 sold for ₹150 has a 33.3% margin but a 50% markup. Understanding this distinction is critical in pricing strategy.</p>
    <h3>Common Use Cases</h3>
    <ul>
      <li>Calculate how much you save in a sale (discount calculator)</li>
      <li>Track portfolio growth percentage over time</li>
      <li>Calculate GST or sales tax amounts</li>
      <li>Determine profitability of products</li>
      <li>Compute grade percentages from raw scores</li>
    </ul>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">What is the difference between percentage increase and markup? <span>+</span></div>
      <div class="faq-a hidden">Percentage increase measures any change relative to the original value. Markup specifically refers to the percentage added to a cost to arrive at a selling price. They use the same formula but are applied in different business contexts.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">How do I calculate the original price after a discount? <span>+</span></div>
      <div class="faq-a hidden">To find the original price, divide the discounted price by (1 - discount%). For example, if you paid ₹800 after a 20% discount: Original = 800 / (1 - 0.20) = 800 / 0.80 = ₹1,000.</div>
    </div>
    <div class="related-grid">
      <a href="/tools/unit-converter/" class="related-card"><div class="rc-emoji">⚖️</div><div class="rc-name">Unit Converter</div></a>
      <a href="/tools/age-calculator/" class="related-card"><div class="rc-emoji">🎂</div><div class="rc-name">Age Calculator</div></a>
      <a href="/tools/word-counter/" class="related-card"><div class="rc-emoji">📝</div><div class="rc-name">Word Counter</div></a>
      <a href="/tools/timezone-converter/" class="related-card"><div class="rc-emoji">🌍</div><div class="rc-name">Timezone Converter</div></a>
    </div>
  </div>
</div>

<script>
let currentMode = 'basic';
const EXAMPLES = {
  basic:[['15% of 200','30'],['8.5% of 1500','127.5'],['25% of 80','20'],['VAT: 18% of 599','107.82']],
  increase:[['50 → 75','+50%'],['1000 → 1250','+25%'],['200 → 300','+50%'],['80 → 96','+20%']],
  decrease:[['100 → 75','−25%'],['500 → 400','−20%'],['1200 → 900','−25%'],['60 → 45','−25%']],
  margin:[['Cost 100, Rev 150','33.3%'],['Cost 80, Rev 120','33.3%'],['Cost 500, Rev 750','33.3%'],['Cost 200, Rev 280','28.6%']],
  discount:[['₹1000 @ 20% off','₹800'],['₹2499 @ 15% off','₹2124'],['₹599 @ 10% off','₹539'],['₹5000 @ 30% off','₹3500']],
  markup:[['Cost 100, 50% up','₹150'],['Cost 80, 25% up','₹100'],['Cost 500, 40% up','₹700'],['Cost 200, 15% up','₹230']]
};

function setMode(mode, btn) {
  currentMode = mode;
  document.querySelectorAll('.mode-tab').forEach(t => t.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('.mode-panel').forEach(p => p.classList.remove('active'));
  document.getElementById('panel-'+mode).classList.add('active');
  document.getElementById('result-card').classList.add('hidden');
  renderExamples();
}

function showResult(main, label, secondary, barPct) {
  const card = document.getElementById('result-card');
  document.getElementById('main-result').textContent = main;
  document.getElementById('result-label').textContent = label;
  document.getElementById('result-secondary').textContent = secondary;
  const pct = Math.min(100, Math.max(0, Math.abs(barPct)));
  document.getElementById('bar-right').textContent = Math.round(pct) + '%';
  document.getElementById('bar-left').textContent = '0%';
  card.classList.remove('hidden');
  setTimeout(() => document.getElementById('pct-fill').style.width = pct + '%', 50);
}

function calcBasic() {
  const p = parseFloat(document.getElementById('b-pct').value);
  const v = parseFloat(document.getElementById('b-val').value);
  if (isNaN(p) || isNaN(v)) return;
  const r = (p/100)*v;
  document.getElementById('b-result').textContent = r.toFixed(2);
  showResult(r.toFixed(2), `${p}% of ${v}`, `Remainder: ${(v - r).toFixed(2)}`, p);
}

function calcIncrease() {
  const from = parseFloat(document.getElementById('inc-from').value);
  const to = parseFloat(document.getElementById('inc-to').value);
  if (isNaN(from) || isNaN(to) || from === 0) return;
  const pct = ((to - from) / from) * 100;
  const sign = pct >= 0 ? '+' : '';
  showResult(sign + pct.toFixed(2) + '%', `Change from ${from} to ${to}`, `Absolute change: ${(to - from).toFixed(2)}`, Math.abs(pct));
}

function calcDecrease() {
  const from = parseFloat(document.getElementById('dec-from').value);
  const to = parseFloat(document.getElementById('dec-to').value);
  if (isNaN(from) || isNaN(to) || from === 0) return;
  const pct = ((from - to) / from) * 100;
  showResult(pct.toFixed(2) + '%', `Decrease from ${from} to ${to}`, `Amount reduced: ${(from - to).toFixed(2)}`, Math.abs(pct));
}

function calcMargin() {
  const cost = parseFloat(document.getElementById('mg-cost').value);
  const rev = parseFloat(document.getElementById('mg-rev').value);
  if (isNaN(cost) || isNaN(rev) || rev === 0) return;
  const margin = ((rev - cost) / rev) * 100;
  const profit = rev - cost;
  showResult(margin.toFixed(2) + '%', 'Profit Margin', `Profit: ${profit.toFixed(2)} | Markup: ${((profit/cost)*100).toFixed(2)}%`, margin);
}

function calcDiscount() {
  const price = parseFloat(document.getElementById('dc-price').value);
  const pct = parseFloat(document.getElementById('dc-pct').value);
  if (isNaN(price) || isNaN(pct)) return;
  const discounted = price * (1 - pct/100);
  const saved = price - discounted;
  showResult(discounted.toFixed(2), `Price after ${pct}% discount`, `You save: ${saved.toFixed(2)}`, pct);
}

function calcMarkup() {
  const cost = parseFloat(document.getElementById('mu-cost').value);
  const pct = parseFloat(document.getElementById('mu-pct').value);
  if (isNaN(cost) || isNaN(pct)) return;
  const price = cost * (1 + pct/100);
  const margin = ((price - cost) / price) * 100;
  showResult(price.toFixed(2), `Selling price at ${pct}% markup`, `Profit margin: ${margin.toFixed(2)}%`, pct);
}

function renderExamples() {
  const items = EXAMPLES[currentMode] || [];
  document.getElementById('examples-grid').innerHTML = items.map(([q,a]) => `
    <div class="example-item">
      <div class="ei-q">${q}</div>
      <div class="ei-a">${a}</div>
    </div>`).join('');
}

function resetAll() {
  document.querySelectorAll('input[type="number"]').forEach(i => i.value = '');
  document.getElementById('result-card').classList.add('hidden');
}

function shareResult() {
  const main = document.getElementById('main-result').textContent;
  const lbl = document.getElementById('result-label').textContent;
  const text = `${lbl} = ${main}\nCalculated with PERCIVIA – ${window.location.href}`;
  if (navigator.share) navigator.share({title:'PERCIVIA Result',text}); else navigator.clipboard.writeText(text).then(()=>alert('Copied!'));
}

function copyResult() {
  const main = document.getElementById('main-result').textContent;
  const lbl = document.getElementById('result-label').textContent;
  navigator.clipboard.writeText(`${lbl} = ${main}`).then(()=>alert('Copied!'));
}

function toggleTheme() { const d=document.documentElement; d.setAttribute('data-theme',d.getAttribute('data-theme')==='dark'?'light':'dark'); }
function toggleFaq(el) { const a=el.nextElementSibling; const s=el.querySelector('span'); a.classList.toggle('hidden'); s.textContent=a.classList.contains('hidden')?'+':'−'; }
renderExamples();
</script>
