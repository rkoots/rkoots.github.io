---
layout: default
title: "TYPIQ – Typing Speed Test | WPM, Accuracy & Error Highlighting"
excerpt: "Test your typing speed in WPM with accuracy tracking, error highlighting, timed modes (30/60/120s), animated progress, and shareable result cards."
date: 2026-03-06
categories: tools
permalink: /tools/typing-speed/
logo_svg: /assets/images/tools/logos/typing-speed.svg
description: "Free online typing speed test. Measure WPM (words per minute), accuracy percentage, error highlighting. Choose 30, 60, or 120 second timed modes. Share your result card."
keywords: ["typing speed test", "WPM test", "words per minute", "typing test online", "typing accuracy", "keyboard speed test", "typing practice", "typing speed checker"]
tags: [typing, speed-test, WPM, productivity, practice]
---

<style>
:root{--primary:#f97316;--primary-dark:#ea580c;--accent:#8b5cf6;--success:#10b981;--danger:#ef4444;--bg:#fff7ed;--card:#fff;--text:#1c0a00;--muted:#6b7280;--border:#fed7aa;--shadow:0 8px 32px rgba(249,115,22,0.10);}
[data-theme="dark"]{--bg:#1a0d00;--card:#231200;--text:#ffedd5;--muted:#9ca3af;--border:#7c2d12;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;transition:background 0.3s,color 0.3s;}
.typiq{max-width:900px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:40px 20px 32px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),#fb923c);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:800;background:linear-gradient(135deg,var(--primary),#fb923c,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}
.hero p{color:var(--muted);font-size:1.05rem;max-width:560px;margin:0 auto;}
.toolbar{display:flex;justify-content:flex-end;gap:10px;margin-bottom:16px;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);color:var(--primary);}
.card{background:var(--card);border-radius:16px;padding:28px;box-shadow:var(--shadow);border:1px solid var(--border);margin-bottom:24px;}
.card-title{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:20px;display:flex;align-items:center;gap:8px;}
.mode-row{display:flex;gap:10px;margin-bottom:20px;flex-wrap:wrap;}
.mode-btn{padding:8px 20px;border-radius:20px;border:2px solid var(--border);background:var(--bg);color:var(--muted);font-size:0.9rem;font-weight:700;cursor:pointer;transition:all 0.2s;}
.mode-btn.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.stats-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px;}
@media(max-width:600px){.stats-row{grid-template-columns:repeat(2,1fr);}}
.stat-box{background:var(--bg);border:1.5px solid var(--border);border-radius:12px;padding:14px;text-align:center;}
.stat-val{font-size:2rem;font-weight:800;color:var(--primary);}
.stat-lbl{font-size:0.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.5px;margin-top:3px;}
.timer-ring-wrap{display:flex;justify-content:center;margin-bottom:20px;}
.timer-display{font-size:3rem;font-weight:800;color:var(--primary);text-align:center;animation:pulse 1s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:0.7;}}
.timer-display.done{animation:none;color:var(--success);}
.passage-wrap{background:#0f172a;border-radius:14px;padding:20px;font-family:'Courier New',monospace;font-size:1.05rem;line-height:1.8;margin-bottom:16px;min-height:120px;user-select:none;word-wrap:break-word;overflow-wrap:break-word;white-space:pre-wrap;}
.char-correct{color:#4ade80;}
.char-wrong{color:#f87171;text-decoration:underline;background:rgba(239,68,68,0.15);}
.char-current{background:rgba(249,115,22,0.5);border-radius:2px;}
.char-pending{color:#94a3b8;}
.type-input{width:100%;padding:14px 18px;border:2px solid var(--border);border-radius:12px;background:var(--bg);color:var(--text);font-size:1.05rem;font-family:'Courier New',monospace;transition:border-color 0.2s;}
.type-input:focus{outline:none;border-color:var(--primary);}
.type-input:disabled{opacity:0.5;}
.progress-wrap{margin-bottom:16px;}
.progress-label{display:flex;justify-content:space-between;font-size:0.82rem;color:var(--muted);margin-bottom:5px;}
.progress-bar{height:8px;background:var(--border);border-radius:20px;overflow:hidden;}
.progress-fill{height:100%;border-radius:20px;background:linear-gradient(90deg,var(--primary),var(--accent));transition:width 0.3s;}
.result-card{background:linear-gradient(135deg,var(--primary),var(--accent));border-radius:18px;padding:32px;text-align:center;color:#fff;animation:fadeIn 0.5s;}
@keyframes fadeIn{from{opacity:0;transform:scale(0.95);}to{opacity:1;transform:scale(1);}}
.result-big{font-size:4rem;font-weight:900;line-height:1;}
.result-sub{font-size:1rem;opacity:0.85;margin-top:8px;}
.result-details{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:20px;}
.result-detail{background:rgba(255,255,255,0.2);border-radius:12px;padding:14px;}
.rd-val{font-size:1.5rem;font-weight:800;}
.rd-lbl{font-size:0.78rem;opacity:0.85;margin-top:2px;}
.leaderboard{display:flex;flex-direction:column;gap:8px;margin-top:8px;}
.lb-item{display:flex;align-items:center;gap:12px;padding:10px 16px;background:var(--bg);border:1px solid var(--border);border-radius:10px;}
.lb-rank{font-size:1.1rem;font-weight:800;color:var(--primary);min-width:30px;}
.lb-name{flex:1;font-size:0.9rem;font-weight:600;}
.lb-wpm{font-size:0.9rem;font-weight:800;color:var(--primary);}
.lb-acc{font-size:0.8rem;color:var(--muted);}
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

<div class="typiq">
  <div class="hero">
    <div class="hero-badge">⌨️ TYPIQ</div>
    <h1>Typing Speed Test</h1>
    <p>Measure your WPM, accuracy, and error rate with animated real-time feedback. Share your score!</p>
  </div>

  <div class="toolbar">
    <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Toggle Theme</button>
  </div>

  <div class="card">
    <div class="card-title">⏱️ Choose Duration</div>
    <div class="mode-row">
      <button class="mode-btn active" onclick="setDuration(30,this)">30s</button>
      <button class="mode-btn" onclick="setDuration(60,this)">60s</button>
      <button class="mode-btn" onclick="setDuration(120,this)">120s</button>
    </div>

    <div class="stats-row">
      <div class="stat-box"><div class="stat-val" id="st-wpm">0</div><div class="stat-lbl">WPM</div></div>
      <div class="stat-box"><div class="stat-val" id="st-acc">100%</div><div class="stat-lbl">Accuracy</div></div>
      <div class="stat-box"><div class="stat-val" id="st-errors">0</div><div class="stat-lbl">Errors</div></div>
      <div class="stat-box"><div class="stat-val" id="st-chars">0</div><div class="stat-lbl">Chars</div></div>
    </div>

    <div style="text-align:center;margin-bottom:16px;">
      <div class="timer-display" id="timer-display">30</div>
    </div>

    <div class="progress-wrap">
      <div class="progress-label"><span>Progress</span><span id="prog-pct">0%</span></div>
      <div class="progress-bar"><div class="progress-fill" id="prog-fill" style="width:0%"></div></div>
    </div>

    <div class="passage-wrap" id="passage-display"></div>

    <textarea class="type-input" id="type-input" placeholder="Start typing here to begin the test..." oninput="onType()" spellcheck="false" autocomplete="off" autocorrect="off" autocapitalize="off"></textarea>

    <div style="margin-top:14px;display:flex;gap:10px;flex-wrap:wrap;">
      <button class="btn btn-primary" onclick="resetTest()">↺ Reset / New Text</button>
      <button class="btn btn-ghost" onclick="shareResult()">📤 Share Result</button>
    </div>
  </div>

  <div id="result-section" class="card hidden">
    <div class="card-title">🏆 Results</div>
    <div class="result-card">
      <div class="result-big" id="final-wpm">0</div>
      <div class="result-sub">Words Per Minute</div>
      <div class="result-details">
        <div class="result-detail"><div class="rd-val" id="final-acc">0%</div><div class="rd-lbl">Accuracy</div></div>
        <div class="result-detail"><div class="rd-val" id="final-errors">0</div><div class="rd-lbl">Errors</div></div>
        <div class="result-detail"><div class="rd-val" id="final-chars">0</div><div class="rd-lbl">Characters</div></div>
      </div>
    </div>
    <div style="margin-top:16px;display:flex;gap:10px;flex-wrap:wrap;">
      <button class="btn btn-primary" onclick="resetTest()">⚡ Try Again</button>
      <button class="btn btn-ghost" onclick="shareResult()">📤 Share</button>
    </div>
  </div>

  <div class="card">
    <div class="card-title">🏆 Simulated Leaderboard</div>
    <div class="leaderboard" id="leaderboard"></div>
  </div>

  <div class="seo-block">
    <h2>How to Improve Your Typing Speed</h2>
    <p>The average typing speed is around 40 WPM (words per minute). Professional typists average 65–75 WPM, while the world record is over 200 WPM. With consistent practice, most people can reach 60+ WPM within a few weeks. TYPIQ provides real-time feedback to help you identify and fix your weakest areas.</p>
    <h3>Key Techniques for Faster Typing</h3>
    <ul>
      <li><strong>Touch typing</strong> – Learn to type without looking at the keyboard. Use all 10 fingers with proper home-row positioning (ASDF + JKL;)</li>
      <li><strong>Accuracy first</strong> – Focus on accuracy before speed. Errors slow you down more than careful typing</li>
      <li><strong>Practice consistently</strong> – 15–20 minutes daily is more effective than occasional marathon sessions</li>
      <li><strong>Use proper posture</strong> – Sit up straight, wrists level, fingers curved over the home row</li>
      <li><strong>Target weak keys</strong> – Identify which characters cause the most errors and drill them specifically</li>
    </ul>
    <h3>Understanding WPM Calculation</h3>
    <p>WPM is calculated as (characters typed correctly / 5) divided by minutes elapsed. The "5" represents the average word length in English. This standardizes the measure so that typing short words doesn't inflate your score compared to long words.</p>
    <h3>WPM Benchmarks</h3>
    <ul>
      <li>Below 30 WPM — Beginner, hunt-and-peck typist</li>
      <li>30–50 WPM — Average speed, suitable for most tasks</li>
      <li>50–70 WPM — Good typist, comfortable for most office work</li>
      <li>70–90 WPM — Excellent, professional-level typing</li>
      <li>90+ WPM — Advanced typist</li>
      <li>120+ WPM — Elite typist</li>
    </ul>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">Does typing speed matter in programming? <span>+</span></div>
      <div class="faq-a hidden">To a degree — faster typing reduces friction when writing code. However, programming time is mostly spent thinking, reading, and debugging rather than typing. That said, professional developers who type 70+ WPM can maintain better "flow" states and express ideas more fluidly.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">How is accuracy calculated? <span>+</span></div>
      <div class="faq-a hidden">Accuracy = (correct characters / total characters typed) × 100%. Both correct and incorrect characters count toward total typed, so errors directly reduce your accuracy percentage. High accuracy with slightly lower WPM is generally better than high WPM with many errors.</div>
    </div>
    <div class="related-grid">
      <a href="/tools/word-counter/" class="related-card"><div class="rc-emoji">📝</div><div class="rc-name">Word Counter</div></a>
      <a href="/tools/markdown-converter/" class="related-card"><div class="rc-emoji">📄</div><div class="rc-name">Markdown Converter</div></a>
      <a href="/tools/password-generator/" class="related-card"><div class="rc-emoji">🔐</div><div class="rc-name">Password Generator</div></a>
      <a href="/tools/slug-generator/" class="related-card"><div class="rc-emoji">🔗</div><div class="rc-name">Slug Generator</div></a>
    </div>
  </div>
</div>

<script>
const PASSAGES = [
  "The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs. How vexingly quick daft zebras jump! The five boxing wizards jump quickly.",
  "Technology is best when it brings people together. The advance of technology is based on making it fit in so that you do not really even notice it. It becomes part of everyday life.",
  "In the beginning was the code, and the code was with the developer, and the code was good. Every bug fixed is a step toward perfection, though perfection itself remains always one step ahead.",
  "Success is not final, failure is not fatal: it is the courage to continue that counts. The only way to do great work is to love what you do. Innovation distinguishes between a leader and a follower.",
  "The internet is becoming the town square for the global village of tomorrow. Software is eating the world. Every company is now a technology company, whether they know it or not.",
  "To be or not to be, that is the question. Whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles.",
  "Data is the new oil. Artificial intelligence will have a more profound impact on humanity than electricity or fire. We are living through the most extraordinary technological revolution in human history."
];

const LEADERBOARD_SIM = [
  {name:'⚡ SpeedDemon',wpm:127,acc:'98.2%'},
  {name:'🎯 PrecisionTypist',wpm:112,acc:'99.5%'},
  {name:'🔥 FastFingers',wpm:98,acc:'96.8%'},
  {name:'💻 CodeMonkey',wpm:87,acc:'97.1%'},
  {name:'🚀 KeyboardWarrior',wpm:75,acc:'98.9%'}
];

let duration = 30;
let timeLeft = 30;
let timer = null;
let started = false;
let passage = '';
let typedChars = 0;
let errorCount = 0;
let correctCount = 0;
let startTime = null;

function setDuration(d, btn) {
  duration = d;
  document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  resetTest();
}

function resetTest() {
  clearInterval(timer);
  started = false;
  timeLeft = duration;
  typedChars = 0;
  errorCount = 0;
  correctCount = 0;
  startTime = null;
  passage = PASSAGES[Math.floor(Math.random()*PASSAGES.length)];
  while (passage.length < 200) passage += ' ' + PASSAGES[Math.floor(Math.random()*PASSAGES.length)];
  document.getElementById('type-input').value = '';
  document.getElementById('type-input').disabled = false;
  document.getElementById('type-input').placeholder = 'Start typing here to begin the test...';
  document.getElementById('timer-display').textContent = duration;
  document.getElementById('timer-display').classList.remove('done');
  document.getElementById('st-wpm').textContent = '0';
  document.getElementById('st-acc').textContent = '100%';
  document.getElementById('st-errors').textContent = '0';
  document.getElementById('st-chars').textContent = '0';
  document.getElementById('prog-fill').style.width = '0%';
  document.getElementById('prog-pct').textContent = '0%';
  document.getElementById('result-section').classList.add('hidden');
  renderPassage('');
  renderLeaderboard();
}

function renderPassage(typed) {
  const el = document.getElementById('passage-display');
  let html = '';
  const len = Math.min(passage.length, typed.length + 80);
  for (let i = 0; i < len; i++) {
    const ch = passage[i] === ' ' ? '&nbsp;' : passage[i];
    if (i < typed.length) {
      if (typed[i] === passage[i]) html += `<span class="char-correct">${ch}</span>`;
      else html += `<span class="char-wrong">${ch}</span>`;
    } else if (i === typed.length) {
      html += `<span class="char-current">${ch}</span>`;
    } else {
      html += `<span class="char-pending">${ch}</span>`;
    }
  }
  el.innerHTML = html;
}

function onType() {
  const input = document.getElementById('type-input');
  const typed = input.value;
  if (!started && typed.length > 0) {
    started = true;
    startTime = Date.now();
    timer = setInterval(tick, 1000);
  }
  if (!started) return;
  renderPassage(typed);
  let correct = 0, errors = 0;
  for (let i = 0; i < typed.length; i++) {
    if (i < passage.length && typed[i] === passage[i]) correct++;
    else errors++;
  }
  correctCount = correct;
  errorCount = errors;
  typedChars = typed.length;
  const elapsed = (Date.now() - startTime) / 60000;
  const wpm = elapsed > 0 ? Math.round((correct / 5) / elapsed) : 0;
  const acc = typedChars > 0 ? Math.round((correct / typedChars) * 100) : 100;
  document.getElementById('st-wpm').textContent = wpm;
  document.getElementById('st-acc').textContent = acc + '%';
  document.getElementById('st-errors').textContent = errors;
  document.getElementById('st-chars').textContent = typedChars;
  const pct = Math.min(100, Math.floor((typed.length / passage.length) * 100));
  document.getElementById('prog-fill').style.width = pct + '%';
  document.getElementById('prog-pct').textContent = pct + '%';
  if (typed.length >= passage.length) endTest();
}

function tick() {
  timeLeft--;
  document.getElementById('timer-display').textContent = timeLeft;
  if (timeLeft <= 0) endTest();
}

function endTest() {
  clearInterval(timer);
  document.getElementById('type-input').disabled = true;
  document.getElementById('timer-display').textContent = '✓';
  document.getElementById('timer-display').classList.add('done');
  const elapsed = (Date.now() - startTime) / 60000;
  const wpm = elapsed > 0 ? Math.round((correctCount / 5) / elapsed) : 0;
  const acc = typedChars > 0 ? Math.round((correctCount / typedChars) * 100) : 100;
  document.getElementById('final-wpm').textContent = wpm;
  document.getElementById('final-acc').textContent = acc + '%';
  document.getElementById('final-errors').textContent = errorCount;
  document.getElementById('final-chars').textContent = typedChars;
  document.getElementById('result-section').classList.remove('hidden');
  document.getElementById('result-section').scrollIntoView({behavior:'smooth'});
  renderLeaderboard(wpm, acc);
}

function renderLeaderboard(myWpm, myAcc) {
  const lb = [...LEADERBOARD_SIM];
  if (myWpm) {
    lb.push({name:'🎯 You (just now)', wpm:myWpm, acc:(myAcc||100)+'%'});
    lb.sort((a,b) => b.wpm - a.wpm);
  }
  const el = document.getElementById('leaderboard');
  const medals = ['🥇','🥈','🥉','4️⃣','5️⃣','6️⃣'];
  el.innerHTML = lb.slice(0,6).map((item,i) => `
    <div class="lb-item" style="${item.name.includes('You') ? 'border-color:var(--primary);background:rgba(249,115,22,0.05)' : ''}">
      <span class="lb-rank">${medals[i]||i+1}</span>
      <span class="lb-name">${item.name}</span>
      <span class="lb-wpm">${item.wpm} WPM</span>
      <span class="lb-acc">${item.acc}</span>
    </div>`).join('');
}

function shareResult() {
  const wpm = document.getElementById('final-wpm').textContent;
  const acc = document.getElementById('final-acc').textContent;
  const text = `⌨️ My TYPIQ score: ${wpm} WPM with ${acc} accuracy!\nTest your typing at: ${window.location.href}`;
  if (navigator.share) navigator.share({title:'My Typing Speed', text}); else navigator.clipboard.writeText(text).then(()=>alert('Result copied!'));
}

function toggleTheme() { const d=document.documentElement; d.setAttribute('data-theme',d.getAttribute('data-theme')==='dark'?'light':'dark'); }
function toggleFaq(el) { const a=el.nextElementSibling; const s=el.querySelector('span'); a.classList.toggle('hidden'); s.textContent=a.classList.contains('hidden')?'+':'−'; }
resetTest();
</script>
