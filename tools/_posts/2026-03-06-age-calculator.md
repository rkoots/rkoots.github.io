---
layout: default
title: "CHRONEXA – Age Calculator | Exact Age in Years, Months, Days & Hours"
excerpt: "Calculate your exact age in years, months, days, hours and minutes. Get zodiac sign, birthday countdown, planet ages, life stats and milestone tracker."
date: 2026-03-06
categories: tools
permalink: /tools/age-calculator/
logo_svg: /assets/images/tools/logos/age-calculator.svg
description: "Free age calculator online. Calculate exact age in years, months, days, hours and minutes from date of birth instantly."
keywords: ["age calculator", "exact age calculator", "birthday calculator", "how old am I", "age in days", "zodiac sign calculator", "age on other planets", "birthday countdown", "days lived calculator"]
tags: [age, calculator, birthday, zodiac, productivity, fun]
og:title: "CHRONEXA – Advanced Age Calculator"
og:description: "Find your exact age, zodiac sign, birthday countdown and life statistics instantly."
og:type: website
---

<style>
:root {
  --primary: #7c3aed;
  --primary-dark: #5b21b6;
  --accent: #f59e0b;
  --success: #10b981;
  --danger: #ef4444;
  --bg: #f5f3ff;
  --card: #ffffff;
  --text: #1e1b4b;
  --muted: #6b7280;
  --border: #e5e7eb;
  --shadow: 0 8px 32px rgba(124,58,237,0.10);
}
[data-theme="dark"] {
  --bg: #0f0a1e;
  --card: #1e1534;
  --text: #e5e7eb;
  --muted: #9ca3af;
  --border: #374151;
  --shadow: 0 8px 32px rgba(0,0,0,0.4);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: var(--bg); color: var(--text); font-family: 'Segoe UI', system-ui, sans-serif; transition: background 0.3s, color 0.3s; }
.chronexa { max-width: 960px; margin: 0 auto; padding: 24px 16px 60px; }
.hero { text-align: center; padding: 40px 20px 32px; }
.hero-badge { display: inline-block; background: linear-gradient(135deg, var(--primary), #a855f7); color: #fff; font-size: 0.72rem; font-weight: 700; letter-spacing: 2px; padding: 4px 14px; border-radius: 20px; margin-bottom: 16px; }
.hero h1 { font-size: clamp(2rem, 5vw, 2.8rem); font-weight: 800; background: linear-gradient(135deg, var(--primary), #a855f7, var(--accent)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 12px; }
.hero p { color: var(--muted); font-size: 1.05rem; max-width: 560px; margin: 0 auto; }
.toolbar { display: flex; justify-content: flex-end; gap: 10px; margin-bottom: 20px; }
.btn { display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; border-radius: 8px; border: none; cursor: pointer; font-size: 0.9rem; font-weight: 600; transition: all 0.2s; }
.btn-primary { background: var(--primary); color: #fff; }
.btn-primary:hover { background: var(--primary-dark); transform: translateY(-1px); }
.btn-ghost { background: var(--card); color: var(--text); border: 1px solid var(--border); }
.btn-ghost:hover { border-color: var(--primary); color: var(--primary); }
.card { background: var(--card); border-radius: 16px; padding: 28px; box-shadow: var(--shadow); border: 1px solid var(--border); margin-bottom: 24px; }
.card-title { font-size: 1rem; font-weight: 700; color: var(--primary); margin-bottom: 20px; display: flex; align-items: center; gap: 8px; }
.input-group { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
@media(max-width:600px) { .input-group { grid-template-columns: 1fr; } }
.field label { display: block; font-size: 0.85rem; font-weight: 600; color: var(--muted); margin-bottom: 6px; }
.field input { width: 100%; padding: 12px 14px; border: 1.5px solid var(--border); border-radius: 10px; background: var(--bg); color: var(--text); font-size: 1rem; transition: border-color 0.2s; }
.field input:focus { outline: none; border-color: var(--primary); }
.results-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 16px; margin-top: 8px; }
.result-item { background: linear-gradient(135deg, var(--primary) 0%, #a855f7 100%); border-radius: 12px; padding: 20px 16px; text-align: center; color: #fff; }
.result-item .val { font-size: 2rem; font-weight: 800; line-height: 1; }
.result-item .lbl { font-size: 0.78rem; opacity: 0.85; margin-top: 4px; letter-spacing: 0.5px; text-transform: uppercase; }
.result-item.accent { background: linear-gradient(135deg, var(--accent) 0%, #f97316 100%); }
.result-item.success { background: linear-gradient(135deg, var(--success) 0%, #059669 100%); }
.result-item.danger { background: linear-gradient(135deg, var(--danger) 0%, #dc2626 100%); }
.zodiac-card { display: flex; align-items: center; gap: 20px; padding: 20px; background: linear-gradient(135deg, #fdf4ff, #ede9fe); border-radius: 12px; border: 1px solid #ddd6fe; margin-top: 16px; }
[data-theme="dark"] .zodiac-card { background: linear-gradient(135deg, #1e1534, #2d1b69); border-color: #4c1d95; }
.zodiac-emoji { font-size: 3rem; }
.zodiac-info h3 { font-size: 1.2rem; font-weight: 700; color: var(--primary); }
.zodiac-info p { color: var(--muted); font-size: 0.9rem; margin-top: 4px; }
.progress-wrap { margin-top: 16px; }
.progress-label { display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--muted); margin-bottom: 6px; }
.progress-bar { height: 12px; background: var(--border); border-radius: 20px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 20px; background: linear-gradient(90deg, var(--primary), #a855f7); transition: width 1.2s cubic-bezier(.4,0,.2,1); }
.planet-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; margin-top: 8px; }
.planet-card { background: var(--bg); border: 1px solid var(--border); border-radius: 10px; padding: 14px; text-align: center; transition: transform 0.2s; }
.planet-card:hover { transform: translateY(-3px); }
.planet-card .planet-emoji { font-size: 1.8rem; }
.planet-card .planet-name { font-size: 0.78rem; font-weight: 600; color: var(--muted); margin: 4px 0 2px; text-transform: uppercase; letter-spacing: 0.5px; }
.planet-card .planet-age { font-size: 1.1rem; font-weight: 800; color: var(--primary); }
.milestones { display: flex; flex-direction: column; gap: 12px; margin-top: 8px; }
.milestone-item { display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-radius: 10px; border: 1px solid var(--border); background: var(--bg); }
.milestone-item.achieved { border-color: var(--success); background: #f0fdf4; }
[data-theme="dark"] .milestone-item.achieved { background: #052e16; }
.milestone-item .mi-icon { font-size: 1.4rem; }
.milestone-item .mi-text { flex: 1; }
.milestone-item .mi-title { font-weight: 600; font-size: 0.9rem; }
.milestone-item .mi-sub { color: var(--muted); font-size: 0.8rem; margin-top: 2px; }
.milestone-item .mi-badge { font-size: 0.75rem; font-weight: 700; padding: 3px 10px; border-radius: 20px; }
.badge-done { background: var(--success); color: #fff; }
.badge-future { background: var(--border); color: var(--muted); }
.countdown-display { text-align: center; padding: 20px; }
.countdown-display .cd-big { font-size: 2.5rem; font-weight: 800; color: var(--accent); }
.countdown-display .cd-sub { color: var(--muted); font-size: 0.9rem; margin-top: 4px; }
.life-stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-top: 8px; }
.life-stat { background: var(--bg); border: 1px solid var(--border); border-radius: 10px; padding: 16px; }
.life-stat .ls-val { font-size: 1.4rem; font-weight: 800; color: var(--primary); }
.life-stat .ls-lbl { font-size: 0.8rem; color: var(--muted); margin-top: 4px; }
.share-bar { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px; }
.hidden { display: none; }
.example-btn { font-size: 0.8rem; padding: 5px 12px; background: #ede9fe; color: var(--primary); border: none; border-radius: 6px; cursor: pointer; font-weight: 600; }
.example-btn:hover { background: #ddd6fe; }
.seo-block { margin-top: 48px; padding: 32px; background: var(--card); border-radius: 16px; border: 1px solid var(--border); }
.seo-block h2 { font-size: 1.5rem; font-weight: 700; color: var(--primary); margin-bottom: 16px; }
.seo-block h3 { font-size: 1.1rem; font-weight: 600; margin: 20px 0 8px; color: var(--text); }
.seo-block p, .seo-block li { color: var(--muted); line-height: 1.7; font-size: 0.95rem; }
.seo-block ul { padding-left: 20px; }
.faq-item { border-bottom: 1px solid var(--border); padding: 16px 0; }
.faq-q { font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--text); }
.faq-a { color: var(--muted); font-size: 0.9rem; line-height: 1.6; padding-top: 10px; }
.related-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 16px; }
.related-card { background: var(--bg); border: 1px solid var(--border); border-radius: 10px; padding: 16px; text-align: center; text-decoration: none; transition: all 0.2s; }
.related-card:hover { border-color: var(--primary); transform: translateY(-2px); }
.related-card .rc-emoji { font-size: 1.6rem; }
.related-card .rc-name { font-size: 0.85rem; font-weight: 600; color: var(--text); margin-top: 6px; }
</style>

<div class="chronexa">
  <div class="hero">
    <div class="hero-badge">✨ CHRONEXA</div>
    <h1>Age Calculator</h1>
    <p>Discover your exact age, zodiac sign, life stats, and how old you are on other planets.</p>
    <div style="margin-top:14px; display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
      <button class="example-btn" onclick="loadExample('1990-05-15')">Try: May 15, 1990</button>
      <button class="example-btn" onclick="loadExample('2000-01-01')">Try: Jan 1, 2000</button>
      <button class="example-btn" onclick="loadExample('1985-12-25')">Try: Dec 25, 1985</button>
    </div>
  </div>

  <div class="toolbar">
    <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Toggle Theme</button>
    <button class="btn btn-ghost" onclick="resetTool()">↺ Reset</button>
  </div>

  <div class="card">
    <div class="card-title">📅 Enter Your Birth Details</div>
    <div class="input-group">
      <div class="field">
        <label for="birthdate">Date of Birth</label>
        <input type="date" id="birthdate" onchange="calculate()" max="">
      </div>
      <div class="field">
        <label for="birthtime">Time of Birth (optional)</label>
        <input type="time" id="birthtime" onchange="calculate()" value="00:00">
      </div>
    </div>
  </div>

  <div id="results" class="hidden">
    <div class="card">
      <div class="card-title">🎂 Your Exact Age</div>
      <div class="results-grid">
        <div class="result-item"><div class="val" id="r-years">0</div><div class="lbl">Years</div></div>
        <div class="result-item accent"><div class="val" id="r-months">0</div><div class="lbl">Months</div></div>
        <div class="result-item success"><div class="val" id="r-days">0</div><div class="lbl">Days</div></div>
        <div class="result-item danger"><div class="val" id="r-hours">0</div><div class="lbl">Hours</div></div>
      </div>
      <div class="progress-wrap" style="margin-top:20px;">
        <div class="progress-label"><span>Year Progress</span><span id="year-pct">0%</span></div>
        <div class="progress-bar"><div class="progress-fill" id="year-bar" style="width:0%"></div></div>
      </div>
      <div class="zodiac-card" id="zodiac-card">
        <div class="zodiac-emoji" id="zodiac-emoji">♈</div>
        <div class="zodiac-info">
          <h3 id="zodiac-name">Aries</h3>
          <p id="zodiac-dates">March 21 – April 19</p>
          <p id="zodiac-trait" style="margin-top:4px; font-size:0.85rem;"></p>
        </div>
      </div>
      <div style="margin-top:16px; padding:14px; background:var(--bg); border-radius:10px; border:1px solid var(--border);">
        <span style="font-size:0.85rem; color:var(--muted);">📆 You were born on a </span>
        <strong id="birth-weekday" style="color:var(--primary);">Monday</strong>
      </div>
    </div>

    <div class="card">
      <div class="card-title">⏳ Next Birthday Countdown</div>
      <div class="countdown-display">
        <div class="cd-big" id="next-bday-days">0</div>
        <div class="cd-sub">days until your next birthday</div>
        <div style="margin-top:12px; color:var(--muted); font-size:0.9rem;" id="next-bday-date"></div>
      </div>
      <div class="progress-wrap">
        <div class="progress-label"><span>Days until birthday</span><span id="bday-pct">0%</span></div>
        <div class="progress-bar"><div class="progress-fill" id="bday-bar" style="width:0%;background:linear-gradient(90deg,var(--accent),#f97316)"></div></div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📊 Life Statistics</div>
      <div class="life-stats-grid">
        <div class="life-stat"><div class="ls-val" id="ls-total-days">0</div><div class="ls-lbl">Total Days Lived</div></div>
        <div class="life-stat"><div class="ls-val" id="ls-total-hours">0</div><div class="ls-lbl">Total Hours Lived</div></div>
        <div class="life-stat"><div class="ls-val" id="ls-total-mins">0</div><div class="ls-lbl">Total Minutes Lived</div></div>
        <div class="life-stat"><div class="ls-val" id="ls-heartbeats">0</div><div class="ls-lbl">Estimated Heartbeats</div></div>
        <div class="life-stat"><div class="ls-val" id="ls-breaths">0</div><div class="ls-lbl">Estimated Breaths</div></div>
        <div class="life-stat"><div class="ls-val" id="ls-sleep-hrs">0</div><div class="ls-lbl">Hours Slept (est.)</div></div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🪐 Age on Other Planets</div>
      <div class="planet-grid" id="planet-grid"></div>
    </div>

    <div class="card">
      <div class="card-title">🏆 Milestone Tracker</div>
      <div class="milestones" id="milestones"></div>
    </div>

    <div class="share-bar">
      <button class="btn btn-primary" onclick="shareResult()">📤 Share Age Card</button>
      <button class="btn btn-ghost" onclick="copyResult()">📋 Copy Result</button>
    </div>
  </div>

  <div class="seo-block">
    <h2>How Does an Age Calculator Work?</h2>
    <p>An age calculator computes the difference between a given birth date and the current date. It accounts for leap years, varying month lengths, and timezone offsets to give you a precise result in years, months, days, and hours. CHRONEXA goes beyond basic calculation to provide zodiac signs, life statistics, and planetary ages for a richer experience.</p>
    <h3>Understanding Leap Years</h3>
    <p>A leap year occurs every 4 years when an extra day (February 29) is added to the calendar to keep it synchronized with Earth's orbit around the sun. If you were born on February 29, your "exact" birthday only occurs every 4 years; in other years, most people celebrate on February 28 or March 1. This calculator handles leap year edge cases correctly.</p>
    <h3>Age on Other Planets</h3>
    <p>Each planet in our solar system takes a different amount of time to complete one orbit around the sun. Earth takes ~365.25 days (1 year), while Mercury takes only ~87.97 days and Neptune takes ~60,190 days (~164.8 years). Your "age" on another planet is simply your total days lived divided by that planet's orbital period.</p>
    <h3>Zodiac Sign Calculation</h3>
    <p>Western astrology divides the year into 12 signs based on the sun's position. Each sign covers approximately 30 days. Your zodiac sign is determined purely by your birth date — no time or location is needed for the sun sign.</p>
    <h3>Common Uses</h3>
    <ul>
      <li>Calculating exact age for official documents or forms</li>
      <li>Finding out how many days until your next birthday</li>
      <li>Discovering fun life statistics like total heartbeats</li>
      <li>Checking which zodiac sign you belong to</li>
      <li>Educational use in astronomy to understand planetary orbits</li>
    </ul>
    <h3>Frequently Asked Questions</h3>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">How do I calculate my exact age in days? <span>+</span></div>
      <div class="faq-a hidden">Multiply your years by 365.25 (to account for leap years), add the days for extra months, then add remaining days. Or simply use this tool — it handles all the math automatically.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">What is the most accurate way to calculate age? <span>+</span></div>
      <div class="faq-a hidden">The most accurate method uses the exact timestamp of birth (date + time + timezone). CHRONEXA uses your birth date and optional time to give you the most precise calculation possible.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">How are heartbeat estimates calculated? <span>+</span></div>
      <div class="faq-a hidden">The average adult heart beats ~72 times per minute. We multiply your total minutes lived by 72 to get an estimated total heartbeat count.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">Can I use this calculator for official purposes? <span>+</span></div>
      <div class="faq-a hidden">While this tool is highly accurate, always verify age calculations with certified documents (birth certificate, passport) for official or legal purposes.</div>
    </div>
    <h3>Related Tools</h3>
    <div class="related-grid">
      <a href="/tools/percentage-calculator/" class="related-card"><div class="rc-emoji">📊</div><div class="rc-name">Percentage Calculator</div></a>
      <a href="/tools/unit-converter/" class="related-card"><div class="rc-emoji">⚖️</div><div class="rc-name">Unit Converter</div></a>
      <a href="/tools/timezone-converter/" class="related-card"><div class="rc-emoji">🌍</div><div class="rc-name">Time Zone Converter</div></a>
      <a href="/tools/word-counter/" class="related-card"><div class="rc-emoji">📝</div><div class="rc-name">Word Counter</div></a>
    </div>
  </div>
</div>

<script>
const ZODIAC = [
  {name:'Capricorn',emoji:'♑',dates:'Dec 22 – Jan 19',trait:'Ambitious, disciplined, practical'},
  {name:'Aquarius',emoji:'♒',dates:'Jan 20 – Feb 18',trait:'Innovative, independent, humanitarian'},
  {name:'Pisces',emoji:'♓',dates:'Feb 19 – Mar 20',trait:'Compassionate, artistic, intuitive'},
  {name:'Aries',emoji:'♈',dates:'Mar 21 – Apr 19',trait:'Bold, energetic, pioneering'},
  {name:'Taurus',emoji:'♉',dates:'Apr 20 – May 20',trait:'Reliable, patient, determined'},
  {name:'Gemini',emoji:'♊',dates:'May 21 – Jun 20',trait:'Curious, adaptable, witty'},
  {name:'Cancer',emoji:'♋',dates:'Jun 21 – Jul 22',trait:'Nurturing, intuitive, loyal'},
  {name:'Leo',emoji:'♌',dates:'Jul 23 – Aug 22',trait:'Confident, creative, generous'},
  {name:'Virgo',emoji:'♍',dates:'Aug 23 – Sep 22',trait:'Analytical, meticulous, helpful'},
  {name:'Libra',emoji:'♎',dates:'Sep 23 – Oct 22',trait:'Diplomatic, fair, social'},
  {name:'Scorpio',emoji:'♏',dates:'Oct 23 – Nov 21',trait:'Intense, perceptive, passionate'},
  {name:'Sagittarius',emoji:'♐',dates:'Nov 22 – Dec 21',trait:'Adventurous, optimistic, philosophical'}
];
const PLANETS = [
  {name:'Mercury',emoji:'☿',period:87.97},
  {name:'Venus',emoji:'♀',period:224.7},
  {name:'Mars',emoji:'♂',period:686.97},
  {name:'Jupiter',emoji:'♃',period:4332.59},
  {name:'Saturn',emoji:'♄',period:10759.22},
  {name:'Uranus',emoji:'⛢',period:30688.5},
  {name:'Neptune',emoji:'♆',period:60190},
  {name:'Pluto',emoji:'♇',period:90560}
];
const MILESTONES_DEF = [
  {days:1000,label:'1,000 Days Old',emoji:'🎖️'},
  {days:5000,label:'5,000 Days Old',emoji:'🌟'},
  {days:10000,label:'10,000 Days Old',emoji:'🏅'},
  {days:20000,label:'20,000 Days Old',emoji:'🏆'},
  {days:25000,label:'25,000 Days Old',emoji:'💎'},
  {days:30000,label:'30,000 Days Old',emoji:'👑'}
];
const WEEKDAYS = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

function getZodiac(month, day) {
  const dates = [[1,20],[2,19],[3,21],[4,20],[5,21],[6,21],[7,23],[8,23],[9,23],[10,23],[11,22],[12,22]];
  for (let i = 0; i < 12; i++) {
    if (month === (i+1) && day < dates[i][1]) return ZODIAC[i];
    if (month === (i+1) && day >= dates[i][1]) return ZODIAC[(i+1)%12];
  }
  return ZODIAC[0];
}

function formatNum(n) {
  if (n >= 1e9) return (n/1e9).toFixed(2)+'B';
  if (n >= 1e6) return (n/1e6).toFixed(2)+'M';
  if (n >= 1e3) return (n/1e3).toFixed(1)+'K';
  return n.toLocaleString();
}

function calculate() {
  const bdVal = document.getElementById('birthdate').value;
  if (!bdVal) return;
  const btVal = document.getElementById('birthtime').value || '00:00';
  const [bh, bm] = btVal.split(':').map(Number);
  const birth = new Date(bdVal);
  birth.setHours(bh, bm, 0, 0);
  const now = new Date();
  if (birth > now) { alert('Birth date cannot be in the future!'); return; }

  const diffMs = now - birth;
  const totalDays = Math.floor(diffMs / 86400000);
  const totalHours = Math.floor(diffMs / 3600000);
  const totalMins = Math.floor(diffMs / 60000);

  // Exact age breakdown
  let years = now.getFullYear() - birth.getFullYear();
  let months = now.getMonth() - birth.getMonth();
  let days = now.getDate() - birth.getDate();
  if (days < 0) { months--; const prev = new Date(now.getFullYear(), now.getMonth(), 0); days += prev.getDate(); }
  if (months < 0) { years--; months += 12; }
  const hours = now.getHours() - birth.getHours();

  document.getElementById('r-years').textContent = years;
  document.getElementById('r-months').textContent = months;
  document.getElementById('r-days').textContent = days;
  document.getElementById('r-hours').textContent = Math.abs(hours);

  // Year progress
  const startOfYear = new Date(now.getFullYear(), now.getMonth(), birth.getDate());
  const endOfYear = new Date(now.getFullYear() + 1, now.getMonth(), birth.getDate());
  const pct = Math.min(100, Math.floor(((now - startOfYear) / (endOfYear - startOfYear)) * 100));
  document.getElementById('year-pct').textContent = pct + '%';
  document.getElementById('year-bar').style.width = pct + '%';

  // Zodiac
  const z = getZodiac(birth.getMonth()+1, birth.getDate());
  document.getElementById('zodiac-emoji').textContent = z.emoji;
  document.getElementById('zodiac-name').textContent = z.name;
  document.getElementById('zodiac-dates').textContent = z.dates;
  document.getElementById('zodiac-trait').textContent = z.trait;

  // Birth weekday
  document.getElementById('birth-weekday').textContent = WEEKDAYS[birth.getDay()];

  // Next birthday
  let nextBday = new Date(now.getFullYear(), birth.getMonth(), birth.getDate());
  if (nextBday <= now) nextBday.setFullYear(now.getFullYear() + 1);
  const daysUntil = Math.ceil((nextBday - now) / 86400000);
  document.getElementById('next-bday-days').textContent = daysUntil;
  document.getElementById('next-bday-date').textContent = 'Your next birthday is on ' + nextBday.toLocaleDateString('en-US', {weekday:'long', year:'numeric', month:'long', day:'numeric'});
  const bdayPct = Math.floor(((365 - daysUntil) / 365) * 100);
  document.getElementById('bday-pct').textContent = bdayPct + '%';
  document.getElementById('bday-bar').style.width = bdayPct + '%';

  // Life stats
  document.getElementById('ls-total-days').textContent = formatNum(totalDays);
  document.getElementById('ls-total-hours').textContent = formatNum(totalHours);
  document.getElementById('ls-total-mins').textContent = formatNum(totalMins);
  document.getElementById('ls-heartbeats').textContent = formatNum(totalMins * 72);
  document.getElementById('ls-breaths').textContent = formatNum(totalMins * 16);
  document.getElementById('ls-sleep-hrs').textContent = formatNum(Math.floor(totalHours * 0.33));

  // Planets
  const planetGrid = document.getElementById('planet-grid');
  planetGrid.innerHTML = PLANETS.map(p => `
    <div class="planet-card">
      <div class="planet-emoji">${p.emoji}</div>
      <div class="planet-name">${p.name}</div>
      <div class="planet-age">${(totalDays / p.period).toFixed(2)}</div>
    </div>`).join('');

  // Milestones
  const msEl = document.getElementById('milestones');
  msEl.innerHTML = MILESTONES_DEF.map(m => {
    const done = totalDays >= m.days;
    const remaining = m.days - totalDays;
    return `<div class="milestone-item ${done ? 'achieved' : ''}">
      <div class="mi-icon">${m.emoji}</div>
      <div class="mi-text">
        <div class="mi-title">${m.label}</div>
        <div class="mi-sub">${done ? '✅ Already achieved!' : `${remaining.toLocaleString()} more days to go`}</div>
      </div>
      <span class="mi-badge ${done ? 'badge-done' : 'badge-future'}">${done ? 'Done' : 'Pending'}</span>
    </div>`;
  }).join('');

  document.getElementById('results').classList.remove('hidden');
}

function loadExample(date) {
  document.getElementById('birthdate').value = date;
  calculate();
}

function resetTool() {
  document.getElementById('birthdate').value = '';
  document.getElementById('birthtime').value = '00:00';
  document.getElementById('results').classList.add('hidden');
}

function toggleTheme() {
  const d = document.documentElement;
  d.setAttribute('data-theme', d.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
}

function toggleFaq(el) {
  const a = el.nextElementSibling;
  const s = el.querySelector('span');
  a.classList.toggle('hidden');
  s.textContent = a.classList.contains('hidden') ? '+' : '−';
}

function shareResult() {
  const years = document.getElementById('r-years').textContent;
  const months = document.getElementById('r-months').textContent;
  const days = document.getElementById('r-days').textContent;
  const zodiac = document.getElementById('zodiac-name').textContent;
  const text = `🎂 My age: ${years} years, ${months} months, ${days} days\n♎ Zodiac: ${zodiac}\nCalculated with CHRONEXA – ${window.location.href}`;
  if (navigator.share) { navigator.share({title: 'My Age', text}); }
  else { navigator.clipboard.writeText(text).then(() => alert('Copied to clipboard!')); }
}

function copyResult() {
  const years = document.getElementById('r-years').textContent;
  const months = document.getElementById('r-months').textContent;
  const days = document.getElementById('r-days').textContent;
  navigator.clipboard.writeText(`Age: ${years} years, ${months} months, ${days} days`).then(() => alert('Copied!'));
}

// Set max date to today
document.getElementById('birthdate').max = new Date().toISOString().split('T')[0];
</script>
