---
layout: default
title: "CONVERTIQ – Unit Converter | Length, Weight, Temperature, Data & More"
excerpt: "Convert units instantly across length, weight, temperature, data size, speed, area, and volume. Swap units, view conversion history, and get animated results."
date: 2026-03-06
categories: tools
permalink: /tools/unit-converter/
description: "Free online unit converter for length, weight, temperature, data size, speed, area and volume. Instant conversion with swap button, history, and animated results."
keywords: ["unit converter", "length converter", "weight converter", "temperature converter", "data size converter", "speed converter", "area converter", "online unit conversion"]
tags: [converter, utility, math, measurement, calculator]
---

<style>
:root{--primary:#7c3aed;--primary-dark:#6d28d9;--accent:#f59e0b;--success:#10b981;--bg:#faf5ff;--card:#fff;--text:#1e1b4b;--muted:#6b7280;--border:#e9d5ff;--shadow:0 8px 32px rgba(124,58,237,0.10);}
[data-theme="dark"]{--bg:#0f0a1e;--card:#1a1035;--text:#ede9fe;--muted:#a78bfa;--border:#3730a3;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;transition:background 0.3s,color 0.3s;}
.convertiq{max-width:900px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:40px 20px 32px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),#a855f7);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:800;background:linear-gradient(135deg,var(--primary),#a855f7,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}
.hero p{color:var(--muted);font-size:1.05rem;max-width:560px;margin:0 auto;}
.toolbar{display:flex;justify-content:flex-end;gap:10px;margin-bottom:16px;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-ghost{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);color:var(--primary);}
.card{background:var(--card);border-radius:16px;padding:28px;box-shadow:var(--shadow);border:1px solid var(--border);margin-bottom:24px;}
.card-title{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:20px;display:flex;align-items:center;gap:8px;}
.cat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(100px,1fr));gap:10px;margin-bottom:24px;}
.cat-btn{padding:10px 6px;border-radius:12px;border:2px solid var(--border);background:var(--bg);color:var(--muted);font-size:0.82rem;font-weight:600;cursor:pointer;text-align:center;transition:all 0.2s;}
.cat-btn.active{border-color:var(--primary);background:var(--primary);color:#fff;}
.cat-btn .cat-emoji{display:block;font-size:1.4rem;margin-bottom:4px;}
.converter-row{display:grid;grid-template-columns:1fr 60px 1fr;gap:12px;align-items:end;}
@media(max-width:600px){.converter-row{grid-template-columns:1fr;}.swap-btn{margin:0 auto;width:48px;}}
.field label{display:block;font-size:0.85rem;font-weight:600;color:var(--muted);margin-bottom:6px;}
.field input{width:100%;padding:14px 16px;border:2px solid var(--border);border-radius:12px;background:var(--bg);color:var(--text);font-size:1.1rem;font-weight:600;transition:border-color 0.2s,box-shadow 0.2s;}
.field input:focus{outline:none;border-color:var(--primary);box-shadow:0 0 0 3px rgba(124,58,237,0.1);}
.field select{width:100%;padding:10px 14px;border:1.5px solid var(--border);border-radius:10px;background:var(--bg);color:var(--text);font-size:0.95rem;margin-top:8px;transition:border-color 0.2s;}
.field select:focus{outline:none;border-color:var(--primary);}
.swap-btn{width:48px;height:48px;border-radius:50%;border:2px solid var(--border);background:var(--card);cursor:pointer;font-size:1.2rem;display:flex;align-items:center;justify-content:center;transition:all 0.3s;margin-bottom:6px;}
.swap-btn:hover{border-color:var(--primary);transform:rotate(180deg);background:var(--primary);color:#fff;}
.result-display{margin-top:20px;padding:20px;background:linear-gradient(135deg,var(--primary),#a855f7);border-radius:14px;text-align:center;color:#fff;animation:fadeIn 0.4s;}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:none;}}
.result-big{font-size:2rem;font-weight:800;margin-bottom:4px;}
.result-formula{font-size:0.85rem;opacity:0.8;}
.popular-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin-top:16px;}
.popular-item{padding:10px 14px;background:var(--bg);border:1px solid var(--border);border-radius:10px;cursor:pointer;transition:all 0.2s;display:flex;justify-content:space-between;align-items:center;font-size:0.85rem;}
.popular-item:hover{border-color:var(--primary);background:rgba(124,58,237,0.05);}
.popular-item .pi-label{font-weight:600;color:var(--text);}
.popular-item .pi-value{color:var(--muted);}
.history-list{display:flex;flex-direction:column;gap:8px;max-height:250px;overflow-y:auto;}
.history-item{display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:var(--bg);border:1px solid var(--border);border-radius:8px;font-size:0.85rem;}
.history-item .hi-from{color:var(--muted);}
.history-item .hi-to{font-weight:700;color:var(--primary);}
.history-item .hi-arrow{color:var(--muted);margin:0 6px;}
.seo-block{margin-top:48px;padding:32px;background:var(--card);border-radius:16px;border:1px solid var(--border);}
.seo-block h2{font-size:1.5rem;font-weight:700;color:var(--primary);margin-bottom:16px;}
.seo-block h3{font-size:1.1rem;font-weight:600;margin:20px 0 8px;}
.seo-block p,.seo-block li{color:var(--muted);line-height:1.7;font-size:0.95rem;}
.seo-block ul{padding-left:20px;}
.faq-item{border-bottom:1px solid var(--border);padding:16px 0;}
.faq-q{font-weight:600;cursor:pointer;display:flex;justify-content:space-between;color:var(--text);}
.faq-a{color:var(--muted);font-size:0.9rem;line-height:1.6;padding-top:10px;}
.hidden{display:none;}
.related-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-top:16px;}
.related-card{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center;text-decoration:none;transition:all 0.2s;}
.related-card:hover{border-color:var(--primary);transform:translateY(-2px);}
.related-card .rc-emoji{font-size:1.6rem;}
.related-card .rc-name{font-size:0.85rem;font-weight:600;color:var(--text);margin-top:6px;}
</style>

<div class="convertiq">
  <div class="hero">
    <div class="hero-badge">⚖️ CONVERTIQ</div>
    <h1>Unit Converter</h1>
    <p>Instantly convert any unit — length, weight, temperature, data, speed, area, and volume.</p>
  </div>

  <div class="toolbar">
    <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Toggle Theme</button>
    <button class="btn btn-ghost" onclick="clearHistory()">🗑️ Clear History</button>
  </div>

  <div class="card">
    <div class="card-title">📐 Select Category</div>
    <div class="cat-grid" id="cat-grid"></div>

    <div class="converter-row">
      <div class="field">
        <label id="from-label">From</label>
        <input type="number" id="from-val" placeholder="Enter value" oninput="convert()">
        <select id="from-unit" onchange="convert()"></select>
      </div>
      <div style="display:flex;justify-content:center;padding-bottom:6px;">
        <button class="swap-btn" onclick="swapUnits()" title="Swap units">⇄</button>
      </div>
      <div class="field">
        <label id="to-label">To</label>
        <input type="number" id="to-val" placeholder="Result" oninput="convertReverse()">
        <select id="to-unit" onchange="convert()"></select>
      </div>
    </div>

    <div id="result-display" class="result-display hidden">
      <div class="result-big" id="result-big">–</div>
      <div class="result-formula" id="result-formula">–</div>
    </div>
  </div>

  <div class="card">
    <div class="card-title">⚡ Popular Conversions</div>
    <div class="popular-grid" id="popular-grid"></div>
  </div>

  <div class="card">
    <div class="card-title">📜 Conversion History</div>
    <div class="history-list" id="history-list">
      <div style="color:var(--muted);font-size:0.9rem;text-align:center;padding:16px;">No conversions yet</div>
    </div>
  </div>

  <div class="seo-block">
    <h2>About CONVERTIQ Unit Converter</h2>
    <p>CONVERTIQ is a comprehensive unit conversion tool covering all common measurement categories. Whether you need to convert kilometers to miles, Celsius to Fahrenheit, megabytes to gigabytes, or knots to km/h, CONVERTIQ handles all conversions instantly in your browser — no server required, no data transmitted.</p>
    <h3>Temperature Conversion Formulas</h3>
    <ul>
      <li>Celsius to Fahrenheit: °F = (°C × 9/5) + 32</li>
      <li>Fahrenheit to Celsius: °C = (°F − 32) × 5/9</li>
      <li>Celsius to Kelvin: K = °C + 273.15</li>
      <li>Kelvin to Celsius: °C = K − 273.15</li>
    </ul>
    <h3>Common Length Conversions</h3>
    <ul>
      <li>1 mile = 1.60934 km</li>
      <li>1 inch = 2.54 cm</li>
      <li>1 foot = 30.48 cm</li>
      <li>1 yard = 0.9144 m</li>
      <li>1 nautical mile = 1.852 km</li>
    </ul>
    <h3>Data Size Reference</h3>
    <ul>
      <li>1 KB = 1,024 bytes</li>
      <li>1 MB = 1,048,576 bytes</li>
      <li>1 GB = 1,073,741,824 bytes</li>
      <li>1 TB = 1,099,511,627,776 bytes</li>
    </ul>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">How accurate are the conversions? <span>+</span></div>
      <div class="faq-a hidden">All conversions use standard internationally-recognized conversion factors. Results are displayed with up to 8 significant figures for maximum precision. For scientific applications, always verify with authoritative sources.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">Why is temperature conversion different from others? <span>+</span></div>
      <div class="faq-a hidden">Most unit conversions are multiplicative (multiply by a factor). Temperature conversions involve an offset (additive) component as well, because the zero points of Celsius, Fahrenheit, and Kelvin scales are different.</div>
    </div>
    <div class="related-grid">
      <a href="/tools/percentage-calculator/" class="related-card"><div class="rc-emoji">📊</div><div class="rc-name">Percentage Calc</div></a>
      <a href="/tools/age-calculator/" class="related-card"><div class="rc-emoji">🎂</div><div class="rc-name">Age Calculator</div></a>
      <a href="/tools/timezone-converter/" class="related-card"><div class="rc-emoji">🌍</div><div class="rc-name">Timezone Converter</div></a>
      <a href="/tools/word-counter/" class="related-card"><div class="rc-emoji">📝</div><div class="rc-name">Word Counter</div></a>
    </div>
  </div>
</div>

<script>
const CATEGORIES = {
  length: { emoji:'📏', units: { meter:1, kilometer:0.001, centimeter:100, millimeter:1000, inch:39.3701, foot:3.28084, yard:1.09361, mile:0.000621371, 'nautical mile':0.000539957, light_year:1.057e-16 } },
  weight: { emoji:'⚖️', units: { kilogram:1, gram:1000, milligram:1e6, pound:2.20462, ounce:35.274, ton:0.001, 'metric ton':0.001, stone:0.157473, 'short ton':0.00110231 } },
  temperature: { emoji:'🌡️', units: { celsius:'C', fahrenheit:'F', kelvin:'K' } },
  data: { emoji:'💾', units: { byte:1, kilobyte:1/1024, megabyte:1/1048576, gigabyte:1/1073741824, terabyte:1/1099511627776, petabyte:1/1.126e15, bit:8, kilobit:8/1024, megabit:8/1048576, gigabit:8/1073741824 } },
  speed: { emoji:'🚀', units: { 'meter/second':1, 'kilometer/hour':3.6, 'mile/hour':2.23694, knot:1.94384, 'foot/second':3.28084, mach:0.00292 } },
  area: { emoji:'🔲', units: { 'sq meter':1, 'sq kilometer':1e-6, 'sq centimeter':1e4, 'sq foot':10.7639, 'sq inch':1550, 'sq yard':1.19599, acre:0.000247105, hectare:1e-4 } },
  volume: { emoji:'🧪', units: { liter:1, milliliter:1000, 'cubic meter':0.001, 'cubic centimeter':1000, gallon:0.264172, quart:1.05669, pint:2.11338, cup:4.22675, 'fluid ounce':33.814, tablespoon:67.628, teaspoon:202.884 } }
};
const POPULAR = {
  length: [['1 km','miles',1,'kilometer','mile'],['1 mile','km',1,'mile','kilometer'],['1 ft','cm',1,'foot','centimeter'],['1 in','cm',1,'inch','centimeter']],
  weight: [['1 kg','lbs',1,'kilogram','pound'],['1 lb','kg',1,'pound','kilogram'],['1 oz','grams',1,'ounce','gram'],['1 stone','kg',1,'stone','kilogram']],
  temperature: [['0°C','°F',0,'celsius','fahrenheit'],['100°C','°F',100,'celsius','fahrenheit'],['32°F','°C',32,'fahrenheit','celsius'],['0 K','°C',0,'kelvin','celsius']],
  data: [['1 GB','MB',1,'gigabyte','megabyte'],['1 TB','GB',1,'terabyte','gigabyte'],['1 MB','KB',1,'megabyte','kilobyte'],['1 GB','KB',1,'gigabyte','kilobyte']],
  speed: [['100 km/h','mph',100,'kilometer/hour','mile/hour'],['60 mph','km/h',60,'mile/hour','kilometer/hour'],['1 mach','km/h',1,'mach','kilometer/hour'],['30 knots','km/h',30,'knot','kilometer/hour']],
  area: [['1 acre','m²',1,'acre','sq meter'],['1 hectare','acres',1,'hectare','acre'],['100 sq ft','sq m',100,'sq foot','sq meter'],['1 sq km','sq mi',1,'sq kilometer','sq yard']],
  volume: [['1 gallon','liters',1,'gallon','liter'],['1 liter','cups',1,'liter','cup'],['1 cup','ml',1,'cup','milliliter'],['1 fl oz','ml',1,'fluid ounce','milliliter']]
};

let currentCat = 'length';
let history = [];

function init() {
  const catGrid = document.getElementById('cat-grid');
  catGrid.innerHTML = Object.entries(CATEGORIES).map(([key,val]) => `
    <button class="cat-btn ${key===currentCat?'active':''}" onclick="setCategory('${key}',this)">
      <span class="cat-emoji">${val.emoji}</span>${key.charAt(0).toUpperCase()+key.slice(1)}
    </button>`).join('');
  populateUnits();
  renderPopular();
}

function setCategory(cat, btn) {
  currentCat = cat;
  document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  populateUnits();
  renderPopular();
  document.getElementById('from-val').value = '';
  document.getElementById('to-val').value = '';
  document.getElementById('result-display').classList.add('hidden');
}

function populateUnits() {
  const units = Object.keys(CATEGORIES[currentCat].units);
  const fromSel = document.getElementById('from-unit');
  const toSel = document.getElementById('to-unit');
  fromSel.innerHTML = units.map(u => `<option value="${u}">${u}</option>`).join('');
  toSel.innerHTML = units.map(u => `<option value="${u}">${u}</option>`).join('');
  toSel.selectedIndex = Math.min(1, units.length - 1);
}

function convertTemp(val, from, to) {
  let celsius;
  if (from === 'celsius') celsius = val;
  else if (from === 'fahrenheit') celsius = (val - 32) * 5/9;
  else celsius = val - 273.15;
  if (to === 'celsius') return celsius;
  if (to === 'fahrenheit') return celsius * 9/5 + 32;
  return celsius + 273.15;
}

function doConvert(val, from, to) {
  if (currentCat === 'temperature') return convertTemp(val, from, to);
  const units = CATEGORIES[currentCat].units;
  const base = val / units[from];
  return base * units[to];
}

function convert() {
  const val = parseFloat(document.getElementById('from-val').value);
  const from = document.getElementById('from-unit').value;
  const to = document.getElementById('to-unit').value;
  if (isNaN(val)) { document.getElementById('result-display').classList.add('hidden'); return; }
  const result = doConvert(val, from, to);
  const formatted = Math.abs(result) < 0.0001 || Math.abs(result) > 1e8 ? result.toExponential(4) : parseFloat(result.toPrecision(8)).toString();
  document.getElementById('to-val').value = formatted;
  showResult(val, from, result, to);
  addHistory(val, from, result, to);
}

function convertReverse() {
  const val = parseFloat(document.getElementById('to-val').value);
  const from = document.getElementById('to-unit').value;
  const to = document.getElementById('from-unit').value;
  if (isNaN(val)) return;
  const result = doConvert(val, from, to);
  const formatted = Math.abs(result) < 0.0001 || Math.abs(result) > 1e8 ? result.toExponential(4) : parseFloat(result.toPrecision(8)).toString();
  document.getElementById('from-val').value = formatted;
}

function showResult(val, from, result, to) {
  const formatted = Math.abs(result) < 0.0001 || Math.abs(result) > 1e8 ? result.toExponential(4) : parseFloat(result.toPrecision(8)).toString();
  document.getElementById('result-big').textContent = `${val} ${from} = ${formatted} ${to}`;
  document.getElementById('result-formula').textContent = `Category: ${currentCat.charAt(0).toUpperCase()+currentCat.slice(1)}`;
  const rd = document.getElementById('result-display');
  rd.classList.remove('hidden');
  rd.style.animation = 'none'; void rd.offsetWidth; rd.style.animation = 'fadeIn 0.4s';
}

function swapUnits() {
  const fromSel = document.getElementById('from-unit');
  const toSel = document.getElementById('to-unit');
  const fromVal = document.getElementById('from-val').value;
  const toVal = document.getElementById('to-val').value;
  [fromSel.value, toSel.value] = [toSel.value, fromSel.value];
  document.getElementById('from-val').value = toVal;
  document.getElementById('to-val').value = fromVal;
  convert();
}

function addHistory(val, from, result, to) {
  const formatted = Math.abs(result) < 0.0001 || Math.abs(result) > 1e8 ? result.toExponential(4) : parseFloat(result.toPrecision(8)).toString();
  history.unshift({from:`${val} ${from}`, to:`${formatted} ${to}`});
  if (history.length > 15) history.pop();
  const el = document.getElementById('history-list');
  el.innerHTML = history.map(h => `<div class="history-item"><span class="hi-from">${h.from}</span><span class="hi-arrow">→</span><span class="hi-to">${h.to}</span></div>`).join('');
}

function clearHistory() { history = []; document.getElementById('history-list').innerHTML = '<div style="color:var(--muted);font-size:0.9rem;text-align:center;padding:16px;">No conversions yet</div>'; }

function renderPopular() {
  const items = POPULAR[currentCat] || [];
  document.getElementById('popular-grid').innerHTML = items.map(([label,,val,from,to]) => {
    const result = doConvert(val, from, to);
    const fmt = Math.abs(result) < 0.0001 || Math.abs(result) > 1e8 ? result.toExponential(3) : parseFloat(result.toPrecision(6)).toString();
    return `<div class="popular-item" onclick="loadPopular(${val},'${from}','${to}')">
      <span class="pi-label">${label}</span>
      <span class="pi-value">= ${fmt} ${to}</span>
    </div>`;
  }).join('');
}

function loadPopular(val, from, to) {
  document.getElementById('from-val').value = val;
  document.getElementById('from-unit').value = from;
  document.getElementById('to-unit').value = to;
  convert();
}

function toggleTheme() { const d=document.documentElement; d.setAttribute('data-theme',d.getAttribute('data-theme')==='dark'?'light':'dark'); }
function toggleFaq(el) { const a=el.nextElementSibling; const s=el.querySelector('span'); a.classList.toggle('hidden'); s.textContent=a.classList.contains('hidden')?'+':'−'; }
init();
</script>
