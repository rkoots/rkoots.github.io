---
layout: default
title: "QRYPTA – QR Code Generator | Free Custom QR Codes Online"
excerpt: "Generate QR codes for URLs, text, email, phone, WiFi, and events. Customize colors, size, and download as PNG or SVG instantly."
date: 2026-03-06
categories: tools
permalink: /tools/qr-generator/
logo_svg: /assets/images/tools/logos/qr-generator.svg
description: "Free online QR code generator. Create custom QR codes for URL, text, email, phone, WiFi login and event details. Color customization, PNG and SVG download."
keywords: ["QR code generator", "free QR code", "custom QR code", "WiFi QR code", "URL QR code", "QR code maker", "online QR generator", "QR code download"]
tags: [QR, generator, utility, download, mobile]
---

<style>
:root{--primary:#059669;--primary-dark:#047857;--accent:#f59e0b;--bg:#f0fdf4;--card:#fff;--text:#064e3b;--muted:#6b7280;--border:#a7f3d0;--shadow:0 8px 32px rgba(5,150,105,0.10);}
[data-theme="dark"]{--bg:#071a12;--card:#0d2a1d;--text:#d1fae5;--muted:#9ca3af;--border:#134e2a;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;transition:background 0.3s,color 0.3s;}
.qrypta{max-width:960px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:40px 20px 32px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),#34d399);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:800;background:linear-gradient(135deg,var(--primary),#34d399,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}
.hero p{color:var(--muted);font-size:1.05rem;max-width:560px;margin:0 auto;}
.toolbar{display:flex;justify-content:flex-end;gap:10px;margin-bottom:16px;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);color:var(--primary);}
.card{background:var(--card);border-radius:16px;padding:28px;box-shadow:var(--shadow);border:1px solid var(--border);margin-bottom:24px;}
.card-title{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:20px;display:flex;align-items:center;gap:8px;}
.type-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px;}
.type-tab{padding:8px 16px;border-radius:20px;border:1.5px solid var(--border);background:var(--bg);color:var(--muted);font-size:0.85rem;font-weight:600;cursor:pointer;transition:all 0.2s;}
.type-tab.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.form-panel{display:none;}
.form-panel.active{display:block;}
.field{margin-bottom:14px;}
.field label{display:block;font-size:0.85rem;font-weight:600;color:var(--muted);margin-bottom:6px;}
.field input,.field select,.field textarea{width:100%;padding:10px 14px;border:1.5px solid var(--border);border-radius:10px;background:var(--bg);color:var(--text);font-size:0.95rem;transition:border-color 0.2s;font-family:inherit;}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--primary);}
.field textarea{min-height:90px;resize:vertical;}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
@media(max-width:600px){.form-grid{grid-template-columns:1fr;}}
.main-layout{display:grid;grid-template-columns:1fr 280px;gap:24px;}
@media(max-width:760px){.main-layout{grid-template-columns:1fr;}}
.qr-preview-card{background:var(--card);border-radius:16px;padding:24px;box-shadow:var(--shadow);border:1px solid var(--border);display:flex;flex-direction:column;align-items:center;gap:16px;position:sticky;top:20px;}
.qr-canvas-wrap{width:220px;height:220px;display:flex;align-items:center;justify-content:center;background:#fff;border-radius:12px;padding:10px;border:2px solid var(--border);box-shadow:inset 0 2px 8px rgba(0,0,0,0.05);transition:all 0.3s;}
.qr-canvas-wrap canvas{border-radius:4px;}
.qr-placeholder{text-align:center;color:var(--muted);}
.qr-placeholder .qr-icon{font-size:3rem;margin-bottom:8px;opacity:0.3;}
.color-row{display:flex;align-items:center;gap:10px;width:100%;}
.color-row label{font-size:0.82rem;font-weight:600;color:var(--muted);min-width:70px;}
.color-row input[type="color"]{width:40px;height:36px;border:1.5px solid var(--border);border-radius:8px;padding:2px;cursor:pointer;background:none;}
.size-row{width:100%;}
.size-row label{font-size:0.82rem;font-weight:600;color:var(--muted);display:flex;justify-content:space-between;margin-bottom:6px;}
.size-row input[type="range"]{width:100%;accent-color:var(--primary);}
.dl-btns{display:flex;gap:8px;width:100%;}
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

<script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.3/build/qrcode.min.js"></script>

<div class="qrypta">
  <div class="hero">
    <div class="hero-badge">📱 QRYPTA</div>
    <h1>QR Code Generator</h1>
    <p>Generate custom QR codes for URLs, WiFi, email, phone and more. Download as PNG or SVG instantly.</p>
  </div>

  <div class="toolbar">
    <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Toggle Theme</button>
    <button class="btn btn-ghost" onclick="resetTool()">↺ Reset</button>
  </div>

  <div class="main-layout">
    <div>
      <div class="card">
        <div class="card-title">📋 QR Type</div>
        <div class="type-tabs">
          <button class="type-tab active" onclick="setType('url',this)">🔗 URL</button>
          <button class="type-tab" onclick="setType('text',this)">📝 Text</button>
          <button class="type-tab" onclick="setType('email',this)">📧 Email</button>
          <button class="type-tab" onclick="setType('phone',this)">📞 Phone</button>
          <button class="type-tab" onclick="setType('wifi',this)">📶 WiFi</button>
          <button class="type-tab" onclick="setType('event',this)">📅 Event</button>
        </div>

        <div id="panel-url" class="form-panel active">
          <div class="field"><label>Website URL</label><input type="url" id="in-url" placeholder="https://example.com" oninput="generateQR()"></div>
        </div>
        <div id="panel-text" class="form-panel">
          <div class="field"><label>Plain Text</label><textarea id="in-text" placeholder="Enter any text..." oninput="generateQR()"></textarea></div>
        </div>
        <div id="panel-email" class="form-panel">
          <div class="field"><label>Email Address</label><input type="email" id="in-email" placeholder="user@example.com" oninput="generateQR()"></div>
          <div class="field"><label>Subject (optional)</label><input type="text" id="in-email-sub" placeholder="Hello!" oninput="generateQR()"></div>
          <div class="field"><label>Body (optional)</label><textarea id="in-email-body" placeholder="Message..." oninput="generateQR()"></textarea></div>
        </div>
        <div id="panel-phone" class="form-panel">
          <div class="field"><label>Phone Number</label><input type="tel" id="in-phone" placeholder="+1-555-000-0000" oninput="generateQR()"></div>
        </div>
        <div id="panel-wifi" class="form-panel">
          <div class="form-grid">
            <div class="field"><label>Network Name (SSID)</label><input type="text" id="in-wifi-ssid" placeholder="MyHomeWiFi" oninput="generateQR()"></div>
            <div class="field"><label>Password</label><input type="password" id="in-wifi-pass" placeholder="••••••••" oninput="generateQR()"></div>
            <div class="field"><label>Security</label>
              <select id="in-wifi-sec" onchange="generateQR()">
                <option value="WPA">WPA/WPA2</option>
                <option value="WEP">WEP</option>
                <option value="nopass">None</option>
              </select>
            </div>
            <div class="field"><label>Hidden Network</label>
              <select id="in-wifi-hidden" onchange="generateQR()">
                <option value="false">No</option>
                <option value="true">Yes</option>
              </select>
            </div>
          </div>
        </div>
        <div id="panel-event" class="form-panel">
          <div class="field"><label>Event Title</label><input type="text" id="in-evt-title" placeholder="Team Meeting" oninput="generateQR()"></div>
          <div class="form-grid">
            <div class="field"><label>Start Date & Time</label><input type="datetime-local" id="in-evt-start" oninput="generateQR()"></div>
            <div class="field"><label>End Date & Time</label><input type="datetime-local" id="in-evt-end" oninput="generateQR()"></div>
          </div>
          <div class="field"><label>Location (optional)</label><input type="text" id="in-evt-loc" placeholder="123 Main St, City" oninput="generateQR()"></div>
          <div class="field"><label>Description (optional)</label><textarea id="in-evt-desc" placeholder="Details..." oninput="generateQR()"></textarea></div>
        </div>
      </div>

      <div class="card">
        <div class="card-title">🎨 Customization</div>
        <div class="color-row" style="margin-bottom:12px;">
          <label>Foreground</label>
          <input type="color" id="qr-fg" value="#000000" oninput="generateQR()">
          <span style="font-size:0.85rem;color:var(--muted);">QR color</span>
        </div>
        <div class="color-row" style="margin-bottom:18px;">
          <label>Background</label>
          <input type="color" id="qr-bg" value="#ffffff" oninput="generateQR()">
          <span style="font-size:0.85rem;color:var(--muted);">BG color</span>
        </div>
        <div class="size-row">
          <label>Size <span id="size-val">256 px</span></label>
          <input type="range" min="128" max="512" step="32" value="256" id="qr-size" oninput="document.getElementById('size-val').textContent=this.value+' px';generateQR()">
        </div>
      </div>
    </div>

    <div class="qr-preview-card">
      <div style="font-size:0.85rem;font-weight:700;color:var(--primary);">QR Preview</div>
      <div class="qr-canvas-wrap" id="qr-wrap">
        <div class="qr-placeholder">
          <div class="qr-icon">▦</div>
          <div style="font-size:0.8rem;">Fill in a field to generate</div>
        </div>
      </div>
      <div class="dl-btns">
        <button class="btn btn-primary" style="flex:1;justify-content:center;" onclick="downloadPNG()">⬇️ PNG</button>
        <button class="btn btn-ghost" style="flex:1;justify-content:center;" onclick="downloadSVG()">⬇️ SVG</button>
      </div>
      <button class="btn btn-ghost" style="width:100%;justify-content:center;" onclick="shareQR()">📤 Share</button>
    </div>
  </div>

  <div class="seo-block">
    <h2>What is a QR Code and How Does it Work?</h2>
    <p>A QR (Quick Response) code is a two-dimensional barcode that can be scanned by any smartphone camera to instantly open a URL, connect to WiFi, dial a phone number, or perform other actions. Originally developed in Japan for automotive manufacturing, QR codes have become ubiquitous in marketing, payments, and information sharing worldwide.</p>
    <h3>QR Code Types Explained</h3>
    <ul>
      <li><strong>URL QR codes</strong> – Direct scanners to a website instantly. Best for marketing, business cards, and posters.</li>
      <li><strong>WiFi QR codes</strong> – Allow guests to join your network without typing a password. Perfect for coffee shops and offices.</li>
      <li><strong>Email QR codes</strong> – Pre-fill recipient, subject, and body in the user's email app.</li>
      <li><strong>vCard QR codes</strong> – Share contact information that users can save directly to their phone.</li>
      <li><strong>Event QR codes</strong> – Share calendar event details in iCalendar format.</li>
    </ul>
    <h3>Error Correction in QR Codes</h3>
    <p>QR codes include built-in error correction using Reed-Solomon codes. This allows a QR code to remain scannable even if up to 30% of the code is damaged, dirty, or obscured. This is why you can add logos inside QR codes — as long as the logo covers less than ~30% of the code area.</p>
    <h3>Best Practices for QR Codes</h3>
    <ul>
      <li>Use high contrast colors — dark foreground on light background scans best</li>
      <li>Always test your QR code before printing or publishing</li>
      <li>Use a minimum size of 2cm × 2cm for print materials</li>
      <li>Add a clear call-to-action near the code ("Scan to visit our website")</li>
      <li>For dynamic QR codes, use a URL shortener so you can update the destination</li>
    </ul>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">Are custom colored QR codes scannable? <span>+</span></div>
      <div class="faq-a hidden">Yes, as long as there is sufficient contrast between the foreground and background colors. Avoid light-on-light or dark-on-dark combinations. Always test with multiple QR scanner apps before deploying.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">What is the maximum data capacity of a QR code? <span>+</span></div>
      <div class="faq-a hidden">A single QR code can store up to 7,089 numeric characters, 4,296 alphanumeric characters, or 2,953 bytes of binary data. For web URLs, this is more than sufficient. Long text content may result in denser, harder-to-scan codes.</div>
    </div>
    <div class="related-grid">
      <a href="/tools/password-generator/" class="related-card"><div class="rc-emoji">🔐</div><div class="rc-name">Password Generator</div></a>
      <a href="/tools/base64/" class="related-card"><div class="rc-emoji">🔢</div><div class="rc-name">Base64 Encoder</div></a>
      <a href="/tools/slug-generator/" class="related-card"><div class="rc-emoji">🔗</div><div class="rc-name">Slug Generator</div></a>
      <a href="/tools/color-palette/" class="related-card"><div class="rc-emoji">🎨</div><div class="rc-name">Color Palette</div></a>
    </div>
  </div>
</div>

<script>
let currentType = 'url';
let qrCanvas = null;

// Check if QRCode library is loaded
if (typeof QRCode === 'undefined') {
  console.error('QRCode library not loaded!');
  alert('QRCode library failed to load. Please refresh the page.');
} else {
  console.log('QRCode library loaded successfully');
}

function setType(type, btn) {
  currentType = type;
  document.querySelectorAll('.type-tab').forEach(t => t.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('.form-panel').forEach(p => p.classList.remove('active'));
  document.getElementById('panel-' + type).classList.add('active');
  generateQR();
}

function getQRData() {
  switch(currentType) {
    case 'url': return document.getElementById('in-url').value.trim();
    case 'text': return document.getElementById('in-text').value.trim();
    case 'email': {
      const e = document.getElementById('in-email').value.trim();
      if (!e) return '';
      const s = encodeURIComponent(document.getElementById('in-email-sub').value.trim());
      const b = encodeURIComponent(document.getElementById('in-email-body').value.trim());
      return `mailto:${e}?subject=${s}&body=${b}`;
    }
    case 'phone': {
      const p = document.getElementById('in-phone').value.trim();
      return p ? `tel:${p}` : '';
    }
    case 'wifi': {
      const ssid = document.getElementById('in-wifi-ssid').value.trim();
      if (!ssid) return '';
      const pass = document.getElementById('in-wifi-pass').value;
      const sec = document.getElementById('in-wifi-sec').value;
      const hidden = document.getElementById('in-wifi-hidden').value;
      return `WIFI:T:${sec};S:${ssid};P:${pass};H:${hidden};;`;
    }
    case 'event': {
      const title = document.getElementById('in-evt-title').value.trim();
      if (!title) return '';
      const start = (document.getElementById('in-evt-start').value || '').replace(/[-:T]/g,'').slice(0,15);
      const end = (document.getElementById('in-evt-end').value || '').replace(/[-:T]/g,'').slice(0,15);
      const loc = document.getElementById('in-evt-loc').value.trim();
      const desc = document.getElementById('in-evt-desc').value.trim();
      return `BEGIN:VCALENDAR\nBEGIN:VEVENT\nSUMMARY:${title}\nDTSTART:${start}\nDTEND:${end}\nLOCATION:${loc}\nDESCRIPTION:${desc}\nEND:VEVENT\nEND:VCALENDAR`;
    }
    default: return '';
  }
}

function generateQR() {
  const data = getQRData();
  const wrap = document.getElementById('qr-wrap');
  if (!data) {
    wrap.innerHTML = '<div class="qr-placeholder"><div class="qr-icon">▦</div><div style="font-size:0.8rem;">Fill in a field to generate</div></div>';
    qrCanvas = null;
    return;
  }
  const size = parseInt(document.getElementById('qr-size').value);
  const fg = document.getElementById('qr-fg').value;
  const bg = document.getElementById('qr-bg').value;
  console.log('Generating QR with data:', data, 'size:', size, 'fg:', fg, 'bg:', bg);
  const canvas = document.createElement('canvas');
  wrap.innerHTML = '';
  wrap.appendChild(canvas);
  QRCode.toCanvas(canvas, data, { width: Math.min(size, 240), margin: 2, color: { dark: fg, light: bg } }, err => {
    if (err) { 
      console.error('QR generation error:', err);
      wrap.innerHTML = '<div style="color:red;font-size:0.85rem;text-align:center;padding:20px;">Error: ' + err.message + '</div>'; 
      return; 
    }
    console.log('QR generated successfully');
    qrCanvas = canvas;
  });
}

function downloadPNG() {
  if (!qrCanvas) { alert('Generate a QR code first!'); return; }
  const size = parseInt(document.getElementById('qr-size').value);
  const offscreen = document.createElement('canvas');
  offscreen.width = size; offscreen.height = size;
  const ctx = offscreen.getContext('2d');
  ctx.drawImage(qrCanvas, 0, 0, size, size);
  const a = document.createElement('a'); a.href = offscreen.toDataURL('image/png'); a.download = 'qrypta-qrcode.png'; a.click();
}

async function downloadSVG() {
  const data = getQRData();
  if (!data) { alert('Generate a QR code first!'); return; }
  const fg = document.getElementById('qr-fg').value;
  const bg = document.getElementById('qr-bg').value;
  const size = document.getElementById('qr-size').value;
  console.log('Generating SVG with data:', data, 'size:', size, 'fg:', fg, 'bg:', bg);
  try {
    const svgStr = await QRCode.toString(data, { type: 'svg', width: size, margin: 2, color: { dark: fg, light: bg } });
    console.log('SVG generated successfully, length:', svgStr.length);
    const blob = new Blob([svgStr], {type:'image/svg+xml'});
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'qrypta-qrcode.svg'; a.click();
  } catch(e) { 
    console.error('SVG generation error:', e);
    alert('SVG generation failed: ' + e.message); 
  }
}

function shareQR() {
  if (!qrCanvas) { alert('Generate a QR code first!'); return; }
  qrCanvas.toBlob(blob => {
    if (navigator.share && navigator.canShare && navigator.canShare({files:[new File([blob],'qrcode.png',{type:'image/png'})]})) {
      navigator.share({title:'QR Code', files:[new File([blob],'qrcode.png',{type:'image/png'})]});
    } else {
      navigator.clipboard.writeText(window.location.href).then(() => alert('Link copied to clipboard!'));
    }
  });
}

function resetTool() {
  document.querySelectorAll('input[type="text"],input[type="url"],input[type="email"],input[type="tel"],input[type="password"],textarea').forEach(el => el.value = '');
  document.getElementById('qr-fg').value = '#000000';
  document.getElementById('qr-bg').value = '#ffffff';
  document.getElementById('qr-size').value = 256;
  document.getElementById('size-val').textContent = '256 px';
  setType('url', document.querySelector('.type-tab'));
}

function toggleTheme() { const d=document.documentElement; d.setAttribute('data-theme',d.getAttribute('data-theme')==='dark'?'light':'dark'); }
function toggleFaq(el) { const a=el.nextElementSibling; const s=el.querySelector('span'); a.classList.toggle('hidden'); s.textContent=a.classList.contains('hidden')?'+':'−'; }
</script>
