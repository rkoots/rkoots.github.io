---
layout: default
title: "TIMEVIA – Time Zone Converter | World Clock & Meeting Planner"
excerpt: "Convert time across multiple cities and time zones. World clock dashboard, meeting planner, DST detection, and time difference visual timeline."
date: 2026-03-06
categories: tools
permalink: /tools/timezone-converter/
description: "Free online time zone converter with world clock dashboard, meeting planner, daylight saving detection, and visual time difference timeline. Search any city instantly."
keywords: ["time zone converter", "world clock", "meeting planner", "time zone calculator", "DST detector", "city time converter", "online time zone tool", "compare time zones"]
tags: [timezone, world-clock, converter, productivity, meeting]
---

<style>
:root{--primary:#0369a1;--primary-dark:#075985;--accent:#f59e0b;--success:#10b981;--danger:#ef4444;--bg:#f0f9ff;--card:#fff;--text:#0c4a6e;--muted:#6b7280;--border:#bae6fd;--shadow:0 8px 32px rgba(3,105,161,0.10);}
[data-theme="dark"]{--bg:#020c18;--card:#051525;--text:#e0f2fe;--muted:#93c5fd;--border:#1e3a5f;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;transition:background 0.3s,color 0.3s;}
.timevia{max-width:1000px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:40px 20px 32px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),#38bdf8);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:800;background:linear-gradient(135deg,var(--primary),#38bdf8,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}
.hero p{color:var(--muted);font-size:1.05rem;max-width:560px;margin:0 auto;}
.toolbar{display:flex;justify-content:flex-end;gap:10px;margin-bottom:16px;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);color:var(--primary);}
.card{background:var(--card);border-radius:16px;padding:28px;box-shadow:var(--shadow);border:1px solid var(--border);margin-bottom:24px;}
.card-title{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:20px;display:flex;align-items:center;gap:8px;}
.search-row{display:flex;gap:10px;margin-bottom:16px;}
.search-row input{flex:1;padding:11px 16px;border:1.5px solid var(--border);border-radius:10px;background:var(--bg);color:var(--text);font-size:1rem;}
.search-row input:focus{outline:none;border-color:var(--primary);}
.city-suggestions{background:var(--card);border:1px solid var(--border);border-radius:10px;max-height:200px;overflow-y:auto;margin-top:-8px;margin-bottom:8px;box-shadow:var(--shadow);display:none;}
.city-suggestion{padding:10px 16px;cursor:pointer;font-size:0.9rem;border-bottom:1px solid var(--border);}
.city-suggestion:last-child{border-bottom:none;}
.city-suggestion:hover{background:var(--bg);color:var(--primary);}
.world-clocks{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;}
.clock-card{background:var(--bg);border:1.5px solid var(--border);border-radius:14px;padding:18px;position:relative;transition:all 0.2s;}
.clock-card:hover{border-color:var(--primary);transform:translateY(-3px);}
.clock-remove{position:absolute;top:10px;right:10px;background:none;border:none;color:var(--muted);cursor:pointer;font-size:1.1rem;line-height:1;transition:color 0.2s;}
.clock-remove:hover{color:var(--danger);}
.clock-emoji{font-size:1.5rem;margin-bottom:6px;}
.clock-city{font-size:0.8rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:2px;}
.clock-time{font-size:1.8rem;font-weight:800;color:var(--text);line-height:1;}
.clock-date{font-size:0.78rem;color:var(--muted);margin-top:3px;}
.clock-offset{font-size:0.75rem;color:var(--primary);margin-top:4px;font-weight:600;}
.dst-badge{display:inline-block;background:var(--accent);color:#fff;font-size:0.65rem;font-weight:700;padding:2px 7px;border-radius:10px;margin-left:4px;}
.meeting-section{margin-top:10px;}
.time-input-row{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:16px;}
.time-input-row label{font-size:0.85rem;font-weight:600;color:var(--muted);}
.time-input-row input{padding:10px 14px;border:1.5px solid var(--border);border-radius:10px;background:var(--bg);color:var(--text);font-size:1rem;}
.time-input-row input:focus{outline:none;border-color:var(--primary);}
.timeline{margin-top:16px;overflow-x:auto;}
.timeline-grid{display:grid;gap:10px;min-width:600px;}
.timeline-row{display:flex;align-items:center;gap:12px;}
.timeline-label{min-width:140px;font-size:0.82rem;font-weight:700;color:var(--text);}
.timeline-bar-wrap{flex:1;display:flex;gap:2px;}
.hour-block{flex:1;height:32px;border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:0.65rem;font-weight:700;cursor:default;transition:transform 0.15s;}
.hour-block:hover{transform:scaleY(1.2);}
.hour-working{background:var(--success);color:#fff;}
.hour-overlap{background:var(--primary);color:#fff;}
.hour-sleep{background:#e5e7eb;color:var(--muted);}
[data-theme="dark"] .hour-sleep{background:#1f2937;}
.hour-label-row{display:flex;gap:2px;padding-left:152px;min-width:600px;}
.hour-lbl{flex:1;text-align:center;font-size:0.6rem;color:var(--muted);}
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

<div class="timevia">
  <div class="hero">
    <div class="hero-badge">🌍 TIMEVIA</div>
    <h1>Time Zone Converter</h1>
    <p>World clock dashboard, meeting planner, DST detection, and visual time difference timeline.</p>
  </div>

  <div class="toolbar">
    <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Toggle Theme</button>
  </div>

  <div class="card">
    <div class="card-title">🌐 World Clock Dashboard</div>
    <div class="search-row">
      <input type="text" id="city-search" placeholder="Search city or time zone (e.g. Mumbai, Tokyo, EST)..." oninput="searchCities()" onkeydown="onSearchKey(event)">
      <button class="btn btn-primary" onclick="addSelectedCity()">+ Add</button>
    </div>
    <div class="city-suggestions" id="city-suggestions"></div>
    <div class="world-clocks" id="world-clocks"></div>
  </div>

  <div class="card">
    <div class="card-title">📅 Meeting Planner</div>
    <div class="time-input-row">
      <label>Meeting Time (local):</label>
      <input type="datetime-local" id="meeting-time" oninput="renderTimeline()">
    </div>
    <div class="timeline" id="timeline-wrap">
      <div style="color:var(--muted);font-size:0.9rem;text-align:center;padding:20px;">Add at least 2 cities and select a meeting time to see the overlap timeline</div>
    </div>
  </div>

  <div class="seo-block">
    <h2>About TIMEVIA Time Zone Converter</h2>
    <p>TIMEVIA is a comprehensive time zone tool that helps you coordinate across global teams. The world clock dashboard shows real-time clocks for multiple cities simultaneously, with automatic DST (Daylight Saving Time) detection. The meeting planner visualizes working hours across time zones to find the ideal meeting slot.</p>
    <h3>Understanding Time Zones</h3>
    <p>The world is divided into 24 primary time zones, each offset from UTC (Coordinated Universal Time) by a whole number of hours (though some zones use 30 or 45-minute offsets). UTC is the primary time standard by which the world regulates clocks and time — it does not observe Daylight Saving Time.</p>
    <h3>Daylight Saving Time (DST)</h3>
    <p>Over 70 countries observe Daylight Saving Time, moving clocks forward 1 hour in spring and back in autumn. This creates temporary changes in UTC offsets, making time zone conversion particularly tricky. DST dates vary by country and even by region within countries. TIMEVIA uses your browser's built-in timezone database to detect DST automatically.</p>
    <h3>Tips for Global Meetings</h3>
    <ul>
      <li>Aim for 9 AM–5 PM overlap between all participant time zones</li>
      <li>When no overlap exists, rotate meeting times to share the burden fairly</li>
      <li>Always specify time zones explicitly in meeting invites (e.g., "3 PM IST / 9:30 AM UTC")</li>
      <li>Consider async communication for teams spanning more than 8 hours of difference</li>
    </ul>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">What is UTC and why is it important? <span>+</span></div>
      <div class="faq-a hidden">UTC (Coordinated Universal Time) is the global time standard. All other time zones are expressed as offsets from UTC (e.g., IST is UTC+5:30). Using UTC eliminates ambiguity when coordinating across regions, especially since UTC never observes Daylight Saving Time.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">How does Daylight Saving Time affect international meetings? <span>+</span></div>
      <div class="faq-a hidden">When one region shifts clocks for DST but another doesn't (or shifts at a different time), the time difference between them temporarily changes by 1 hour. This is why a meeting that worked at a consistent offset in winter may be 1 hour off in summer. TIMEVIA accounts for DST automatically.</div>
    </div>
    <div class="related-grid">
      <a href="/tools/age-calculator/" class="related-card"><div class="rc-emoji">🎂</div><div class="rc-name">Age Calculator</div></a>
      <a href="/tools/unit-converter/" class="related-card"><div class="rc-emoji">⚖️</div><div class="rc-name">Unit Converter</div></a>
      <a href="/tools/percentage-calculator/" class="related-card"><div class="rc-emoji">📊</div><div class="rc-name">Percentage Calc</div></a>
      <a href="/tools/word-counter/" class="related-card"><div class="rc-emoji">📝</div><div class="rc-name">Word Counter</div></a>
    </div>
  </div>
</div>

<script>
const CITIES = [
  {name:'Mumbai',tz:'Asia/Kolkata',emoji:'🇮🇳'},
  {name:'Delhi',tz:'Asia/Kolkata',emoji:'🇮🇳'},
  {name:'Bangalore',tz:'Asia/Kolkata',emoji:'🇮🇳'},
  {name:'London',tz:'Europe/London',emoji:'🇬🇧'},
  {name:'New York',tz:'America/New_York',emoji:'🇺🇸'},
  {name:'Los Angeles',tz:'America/Los_Angeles',emoji:'🇺🇸'},
  {name:'Chicago',tz:'America/Chicago',emoji:'🇺🇸'},
  {name:'Tokyo',tz:'Asia/Tokyo',emoji:'🇯🇵'},
  {name:'Singapore',tz:'Asia/Singapore',emoji:'🇸🇬'},
  {name:'Dubai',tz:'Asia/Dubai',emoji:'🇦🇪'},
  {name:'Paris',tz:'Europe/Paris',emoji:'🇫🇷'},
  {name:'Berlin',tz:'Europe/Berlin',emoji:'🇩🇪'},
  {name:'Sydney',tz:'Australia/Sydney',emoji:'🇦🇺'},
  {name:'Beijing',tz:'Asia/Shanghai',emoji:'🇨🇳'},
  {name:'Seoul',tz:'Asia/Seoul',emoji:'🇰🇷'},
  {name:'Toronto',tz:'America/Toronto',emoji:'🇨🇦'},
  {name:'São Paulo',tz:'America/Sao_Paulo',emoji:'🇧🇷'},
  {name:'Cairo',tz:'Africa/Cairo',emoji:'🇪🇬'},
  {name:'Moscow',tz:'Europe/Moscow',emoji:'🇷🇺'},
  {name:'Jakarta',tz:'Asia/Jakarta',emoji:'🇮🇩'},
  {name:'Bangkok',tz:'Asia/Bangkok',emoji:'🇹🇭'},
  {name:'Karachi',tz:'Asia/Karachi',emoji:'🇵🇰'},
  {name:'Istanbul',tz:'Europe/Istanbul',emoji:'🇹🇷'},
  {name:'Nairobi',tz:'Africa/Nairobi',emoji:'🇰🇪'},
  {name:'Auckland',tz:'Pacific/Auckland',emoji:'🇳🇿'},
  {name:'UTC',tz:'UTC',emoji:'🌐'}
];

let activeCities = ['Mumbai','London','New York','Tokyo'];
let clockInterval;

function getTimeInTz(tz) {
  try { return new Date().toLocaleString('en-US', {timeZone:tz,hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false}); }
  catch(e) { return '--:--:--'; }
}
function getDateInTz(tz) {
  try { return new Date().toLocaleString('en-US', {timeZone:tz,weekday:'short',month:'short',day:'numeric'}); }
  catch(e) { return ''; }
}
function getOffsetLabel(tz) {
  try {
    const now = new Date();
    const utcMs = now.getTime() + now.getTimezoneOffset()*60000;
    const tzDate = new Date(now.toLocaleString('en-US',{timeZone:tz}));
    const localDate = new Date(now.toLocaleString('en-US',{timeZone:Intl.DateTimeFormat().resolvedOptions().timeZone}));
    const diffMin = Math.round((tzDate - localDate) / 60000);
    const sign = diffMin >= 0 ? '+' : '';
    const h = Math.floor(Math.abs(diffMin)/60);
    const m = Math.abs(diffMin)%60;
    return `${sign}${h}h${m?m+'m':''} from local`;
  } catch(e) { return ''; }
}

function renderClocks() {
  const grid = document.getElementById('world-clocks');
  grid.innerHTML = activeCities.map(name => {
    const city = CITIES.find(c => c.name === name) || {name, tz:'UTC', emoji:'🌐'};
    return `<div class="clock-card" id="clock-${name.replace(/\s/g,'-')}">
      <button class="clock-remove" onclick="removeCity('${name}')" title="Remove">✕</button>
      <div class="clock-emoji">${city.emoji}</div>
      <div class="clock-city">${city.name}</div>
      <div class="clock-time" id="ct-${name.replace(/\s/g,'-')}">${getTimeInTz(city.tz)}</div>
      <div class="clock-date">${getDateInTz(city.tz)}</div>
      <div class="clock-offset">${getOffsetLabel(city.tz)}</div>
    </div>`;
  }).join('');
}

function tickClocks() {
  activeCities.forEach(name => {
    const city = CITIES.find(c => c.name === name) || {tz:'UTC'};
    const el = document.getElementById('ct-' + name.replace(/\s/g,'-'));
    if (el) el.textContent = getTimeInTz(city.tz);
  });
}

function removeCity(name) {
  activeCities = activeCities.filter(c => c !== name);
  renderClocks();
  renderTimeline();
}

function searchCities() {
  const q = document.getElementById('city-search').value.toLowerCase();
  const box = document.getElementById('city-suggestions');
  if (!q) { box.style.display='none'; return; }
  const matches = CITIES.filter(c => c.name.toLowerCase().includes(q) || c.tz.toLowerCase().includes(q)).slice(0,8);
  if (!matches.length) { box.style.display='none'; return; }
  box.innerHTML = matches.map(c => `<div class="city-suggestion" onclick="addCity('${c.name}')">${c.emoji} ${c.name} <span style="color:var(--muted);font-size:0.78rem;">(${c.tz})</span></div>`).join('');
  box.style.display='block';
}

function onSearchKey(e) { if (e.key==='Enter') { const first = document.querySelector('.city-suggestion'); if (first) first.click(); } }

function addSelectedCity() {
  const q = document.getElementById('city-search').value;
  const match = CITIES.find(c => c.name.toLowerCase() === q.toLowerCase());
  if (match) addCity(match.name);
  else alert('City not found. Try searching from the suggestions.');
}

function addCity(name) {
  if (!activeCities.includes(name)) { activeCities.push(name); renderClocks(); renderTimeline(); }
  document.getElementById('city-search').value = '';
  document.getElementById('city-suggestions').style.display = 'none';
}

function renderTimeline() {
  const wrap = document.getElementById('timeline-wrap');
  const mtVal = document.getElementById('meeting-time').value;
  if (activeCities.length < 2 || !mtVal) {
    wrap.innerHTML = '<div style="color:var(--muted);font-size:0.9rem;text-align:center;padding:20px;">Add at least 2 cities and select a meeting time to see the overlap timeline</div>';
    return;
  }
  const mt = new Date(mtVal);
  const hours = Array.from({length:24},(_,i)=>i);
  const hourLabels = `<div class="hour-label-row">${hours.map(h=>`<div class="hour-lbl">${h}</div>`).join('')}</div>`;
  const rows = activeCities.map(name => {
    const city = CITIES.find(c=>c.name===name)||{tz:'UTC',emoji:'🌐'};
    const blocks = hours.map(h => {
      const localHour = new Date(mt.getFullYear(),mt.getMonth(),mt.getDate(),h);
      let cityHour;
      try { cityHour = parseInt(new Date(localHour).toLocaleString('en-US',{timeZone:city.tz,hour:'2-digit',hour12:false})); }
      catch(e) { cityHour = h; }
      const isWorking = cityHour >= 9 && cityHour < 18;
      const isMeeting = h === mt.getHours();
      const cls = isMeeting ? 'hour-overlap' : isWorking ? 'hour-working' : 'hour-sleep';
      return `<div class="hour-block ${cls}" title="${city.name}: ${cityHour}:00">${isMeeting?'📍':''}</div>`;
    }).join('');
    return `<div class="timeline-row"><div class="timeline-label">${city.emoji} ${city.name}</div><div class="timeline-bar-wrap">${blocks}</div></div>`;
  }).join('');
  wrap.innerHTML = `<div class="timeline-grid">${hourLabels}${rows}</div><div style="margin-top:10px;font-size:0.78rem;color:var(--muted);">🟩 Working hours (9–18) &nbsp; 🔵 Meeting time &nbsp; ⬜ Off hours</div>`;
}

document.addEventListener('click', e => { if (!e.target.closest('.search-row') && !e.target.closest('.city-suggestions')) document.getElementById('city-suggestions').style.display='none'; });

renderClocks();
clockInterval = setInterval(tickClocks, 1000);
document.getElementById('meeting-time').value = new Date(new Date().setMinutes(0,0,0)).toISOString().slice(0,16);
renderTimeline();
function toggleTheme() { const d=document.documentElement; d.setAttribute('data-theme',d.getAttribute('data-theme')==='dark'?'light':'dark'); }
function toggleFaq(el) { const a=el.nextElementSibling; const s=el.querySelector('span'); a.classList.toggle('hidden'); s.textContent=a.classList.contains('hidden')?'+':'−'; }
</script>
