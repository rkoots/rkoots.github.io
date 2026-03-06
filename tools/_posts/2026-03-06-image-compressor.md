---
layout: default
title: "PIXORA – Image Compressor | Free Client-Side JPG PNG WebP Compressor"
excerpt: "Compress images online for free — drag and drop JPG, PNG, WebP. Client-side compression, quality slider, before/after preview, file size comparison, and batch support."
date: 2026-03-06
categories: tools
permalink: /tools/image-compressor/
description: "Free online image compressor. Compress JPG, PNG, WebP images entirely in your browser — no uploads. Quality slider, before/after preview, file size comparison, batch compression."
keywords: ["image compressor", "compress images online", "JPG compressor", "PNG compressor", "WebP compressor", "reduce image size", "image optimization", "free image compressor"]
tags: [image, compression, optimization, utility, web]
---

<style>
:root{--primary:#ec4899;--primary-dark:#db2777;--accent:#f59e0b;--success:#10b981;--bg:#fdf2f8;--card:#fff;--text:#1f0a14;--muted:#6b7280;--border:#fbcfe8;--shadow:0 8px 32px rgba(236,72,153,0.10);}
[data-theme="dark"]{--bg:#1a0511;--card:#220a16;--text:#fce7f3;--muted:#9ca3af;--border:#831843;--shadow:0 8px 32px rgba(0,0,0,0.5);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;transition:background 0.3s,color 0.3s;}
.pixora{max-width:960px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:40px 20px 32px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),#f472b6);color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);font-weight:800;background:linear-gradient(135deg,var(--primary),#f472b6,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}
.hero p{color:var(--muted);font-size:1.05rem;max-width:560px;margin:0 auto;}
.toolbar{display:flex;justify-content:flex-end;gap:10px;margin-bottom:16px;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-ghost{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);color:var(--primary);}
.card{background:var(--card);border-radius:16px;padding:28px;box-shadow:var(--shadow);border:1px solid var(--border);margin-bottom:24px;}
.card-title{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:20px;display:flex;align-items:center;gap:8px;}
.drop-zone{border:2.5px dashed var(--border);border-radius:16px;padding:50px 20px;text-align:center;cursor:pointer;transition:all 0.3s;background:var(--bg);}
.drop-zone:hover,.drop-zone.drag-over{border-color:var(--primary);background:rgba(236,72,153,0.05);}
.drop-zone .dz-icon{font-size:3rem;margin-bottom:12px;opacity:0.6;}
.drop-zone h3{font-size:1.1rem;font-weight:700;margin-bottom:6px;}
.drop-zone p{color:var(--muted);font-size:0.9rem;}
.format-badges{display:flex;gap:8px;justify-content:center;margin-top:12px;}
.fmt-badge{padding:4px 12px;background:var(--border);border-radius:20px;font-size:0.78rem;font-weight:700;color:var(--primary);}
.quality-wrap{margin-top:20px;}
.quality-top{display:flex;justify-content:space-between;margin-bottom:8px;}
.quality-top label{font-size:0.9rem;font-weight:600;}
.quality-top span{font-size:1.1rem;font-weight:800;color:var(--primary);}
input[type="range"]{width:100%;accent-color:var(--primary);cursor:pointer;}
.images-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;margin-top:20px;}
.img-item{background:var(--bg);border:1px solid var(--border);border-radius:14px;overflow:hidden;transition:transform 0.2s;}
.img-item:hover{transform:translateY(-3px);}
.img-preview-row{display:grid;grid-template-columns:1fr 1fr;gap:2px;background:var(--border);}
.img-preview-half{position:relative;}
.img-preview-half img{width:100%;height:140px;object-fit:cover;display:block;}
.img-preview-half .half-label{position:absolute;top:6px;left:6px;background:rgba(0,0,0,0.6);color:#fff;font-size:0.7rem;font-weight:700;padding:2px 8px;border-radius:10px;}
.img-info{padding:14px;}
.img-name{font-size:0.85rem;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-bottom:8px;}
.size-comparison{display:flex;align-items:center;gap:8px;font-size:0.82rem;margin-bottom:10px;}
.size-before{color:var(--muted);}
.size-arrow{color:var(--muted);}
.size-after{font-weight:700;color:var(--success);}
.savings-badge{background:rgba(16,185,129,0.12);color:var(--success);padding:3px 10px;border-radius:20px;font-size:0.78rem;font-weight:700;}
.compress-bar{height:6px;background:var(--border);border-radius:10px;overflow:hidden;margin-bottom:10px;}
.compress-fill{height:100%;border-radius:10px;background:linear-gradient(90deg,var(--primary),var(--accent));transition:width 0.6s;}
.progress-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:1000;align-items:center;justify-content:center;}
.progress-overlay.visible{display:flex;}
.progress-box{background:var(--card);border-radius:16px;padding:32px 40px;text-align:center;}
.progress-spinner{width:48px;height:48px;border:4px solid var(--border);border-top-color:var(--primary);border-radius:50%;animation:spin 0.8s linear infinite;margin:0 auto 16px;}
@keyframes spin{to{transform:rotate(360deg);}}
.batch-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px;}
.dim-info{font-size:0.78rem;color:var(--muted);}
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

<div class="pixora">
  <div class="hero">
    <div class="hero-badge">🖼️ PIXORA</div>
    <h1>Image Compressor</h1>
    <p>Compress JPG, PNG & WebP images entirely in your browser — private, fast, and free.</p>
  </div>

  <div class="toolbar">
    <button class="btn btn-ghost" onclick="toggleTheme()">🌙 Toggle Theme</button>
    <button class="btn btn-ghost" onclick="clearAll()">↺ Clear All</button>
  </div>

  <div class="card">
    <div class="card-title">📂 Upload Images</div>
    <div class="drop-zone" id="drop-zone" onclick="document.getElementById('file-input').click()" ondragover="onDragOver(event)" ondragleave="onDragLeave(event)" ondrop="onDrop(event)">
      <div class="dz-icon">🖼️</div>
      <h3>Drop images here or click to upload</h3>
      <p>Supports JPG, PNG, WebP — batch compression supported</p>
      <div class="format-badges">
        <span class="fmt-badge">JPG</span>
        <span class="fmt-badge">PNG</span>
        <span class="fmt-badge">WebP</span>
      </div>
    </div>
    <input type="file" id="file-input" accept="image/jpeg,image/png,image/webp" multiple style="display:none" onchange="handleFiles(this.files)">

    <div class="quality-wrap">
      <div class="quality-top">
        <label>Compression Quality</label>
        <span id="quality-val">75%</span>
      </div>
      <input type="range" min="10" max="100" value="75" id="quality-slider" oninput="document.getElementById('quality-val').textContent=this.value+'%'; recompressAll()">
    </div>
  </div>

  <div id="results-section" class="card hidden">
    <div class="card-title">📊 Compression Results</div>
    <div class="images-grid" id="images-grid"></div>
    <div class="batch-actions">
      <button class="btn btn-primary" onclick="downloadAll()">⬇️ Download All</button>
      <button class="btn btn-ghost" onclick="clearAll()">🗑️ Clear</button>
    </div>
  </div>

  <div class="progress-overlay" id="progress-overlay">
    <div class="progress-box">
      <div class="progress-spinner"></div>
      <div style="font-weight:700;font-size:1rem;" id="progress-text">Compressing...</div>
    </div>
  </div>

  <div class="seo-block">
    <h2>About PIXORA Image Compressor</h2>
    <p>PIXORA compresses images entirely within your browser using the HTML5 Canvas API. Your images are never uploaded to any server, ensuring complete privacy. This tool supports JPEG, PNG, and WebP formats and allows batch compression of multiple images simultaneously.</p>
    <h3>How Image Compression Works</h3>
    <p>PIXORA uses lossy compression via the browser's Canvas toDataURL method. The quality parameter (0–100%) controls how much information is discarded during compression. At 75% quality, most images see a significant file size reduction with minimal visible quality loss — the sweet spot for web use.</p>
    <h3>When to Compress Images</h3>
    <ul>
      <li><strong>Website performance</strong> – Large images slow page load time; compressed images improve Core Web Vitals scores</li>
      <li><strong>Email attachments</strong> – Reduce attachment size for faster delivery and compatibility</li>
      <li><strong>Social media</strong> – Faster uploads and within platform size limits</li>
      <li><strong>Storage optimization</strong> – Save disk space on phones and computers</li>
    </ul>
    <h3>Image Format Guide</h3>
    <ul>
      <li><strong>JPEG</strong> – Best for photographs; supports lossy compression; smallest file size</li>
      <li><strong>PNG</strong> – Best for screenshots, graphics with text; supports transparency; lossless but larger</li>
      <li><strong>WebP</strong> – Modern format by Google; 25–35% smaller than JPEG at same quality; excellent for web</li>
    </ul>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">Are my images private? <span>+</span></div>
      <div class="faq-a hidden">Absolutely. PIXORA processes all images using browser-side JavaScript. Your images never leave your device and are never uploaded to any server. When you close the tab, the images are gone.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">What quality setting should I use? <span>+</span></div>
      <div class="faq-a hidden">For web use, 70–80% is typically ideal — significant size reduction with barely noticeable quality loss. For archiving important images, 85–95% preserves better quality. For social media thumbnails, 60–70% is often sufficient.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">Why does PNG not compress as much as JPG? <span>+</span></div>
      <div class="faq-a hidden">PNG uses lossless compression, meaning no image data is discarded. When canvas converts PNG to JPEG, you can achieve large savings. However, if output format stays PNG, the canvas re-encoding may not compress much. Consider converting PNG to JPEG for maximum savings when transparency is not needed.</div>
    </div>
    <div class="related-grid">
      <a href="/tools/qr-generator/" class="related-card"><div class="rc-emoji">📱</div><div class="rc-name">QR Generator</div></a>
      <a href="/tools/color-palette/" class="related-card"><div class="rc-emoji">🎨</div><div class="rc-name">Color Palette</div></a>
      <a href="/tools/base64/" class="related-card"><div class="rc-emoji">🔢</div><div class="rc-name">Base64 Encoder</div></a>
      <a href="/tools/json-formatter/" class="related-card"><div class="rc-emoji">📋</div><div class="rc-name">JSON Formatter</div></a>
    </div>
  </div>
</div>

<script>
let uploadedFiles = [];
let compressedResults = [];

function onDragOver(e) { e.preventDefault(); document.getElementById('drop-zone').classList.add('drag-over'); }
function onDragLeave() { document.getElementById('drop-zone').classList.remove('drag-over'); }
function onDrop(e) { e.preventDefault(); onDragLeave(); handleFiles(e.dataTransfer.files); }

function handleFiles(files) {
  const arr = Array.from(files).filter(f => f.type.startsWith('image/'));
  if (!arr.length) return;
  uploadedFiles = arr;
  compressAll();
}

async function compressAll() {
  showProgress('Compressing images...');
  compressedResults = [];
  const quality = parseInt(document.getElementById('quality-slider').value) / 100;
  for (const file of uploadedFiles) {
    const result = await compressImage(file, quality);
    compressedResults.push(result);
  }
  hideProgress();
  renderResults();
}

function recompressAll() {
  if (uploadedFiles.length > 0) compressAll();
}

function compressImage(file, quality) {
  return new Promise(resolve => {
    const reader = new FileReader();
    reader.onload = e => {
      const img = new Image();
      img.onload = () => {
        const canvas = document.createElement('canvas');
        canvas.width = img.width; canvas.height = img.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);
        const mimeType = file.type === 'image/png' ? 'image/jpeg' : file.type;
        const dataUrl = canvas.toDataURL(mimeType, quality);
        const byteStr = atob(dataUrl.split(',')[1]);
        const arr = new Uint8Array(byteStr.length);
        for (let i = 0; i < byteStr.length; i++) arr[i] = byteStr.charCodeAt(i);
        const blob = new Blob([arr], {type: mimeType});
        resolve({ name: file.name, originalSize: file.size, compressedSize: blob.size, originalUrl: e.target.result, compressedUrl: dataUrl, blob, mimeType, width: img.width, height: img.height });
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  });
}

function renderResults() {
  document.getElementById('results-section').classList.remove('hidden');
  document.getElementById('images-grid').innerHTML = compressedResults.map((r, i) => {
    const savings = Math.max(0, Math.round((1 - r.compressedSize / r.originalSize) * 100));
    const pct = Math.min(100, savings);
    return `<div class="img-item">
      <div class="img-preview-row">
        <div class="img-preview-half"><img src="${r.originalUrl}" alt="Original"><span class="half-label">Original</span></div>
        <div class="img-preview-half"><img src="${r.compressedUrl}" alt="Compressed"><span class="half-label">Compressed</span></div>
      </div>
      <div class="img-info">
        <div class="img-name">${r.name}</div>
        <div class="dim-info">${r.width} × ${r.height}px</div>
        <div class="size-comparison" style="margin-top:6px;">
          <span class="size-before">${formatBytes(r.originalSize)}</span>
          <span class="size-arrow">→</span>
          <span class="size-after">${formatBytes(r.compressedSize)}</span>
          <span class="savings-badge">-${savings}%</span>
        </div>
        <div class="compress-bar"><div class="compress-fill" style="width:${pct}%"></div></div>
        <button class="btn btn-primary" style="width:100%;justify-content:center;font-size:0.85rem;padding:8px;" onclick="downloadSingle(${i})">⬇️ Download</button>
      </div>
    </div>`;
  }).join('');
}

function formatBytes(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB';
  return (bytes / 1048576).toFixed(2) + ' MB';
}

function downloadSingle(i) {
  const r = compressedResults[i];
  const ext = r.mimeType === 'image/jpeg' ? '.jpg' : r.mimeType === 'image/webp' ? '.webp' : '.png';
  const a = document.createElement('a');
  a.href = URL.createObjectURL(r.blob);
  a.download = r.name.replace(/\.[^.]+$/, '') + '_compressed' + ext;
  a.click();
}

async function downloadAll() {
  for (let i = 0; i < compressedResults.length; i++) {
    await new Promise(r => setTimeout(r, 300));
    downloadSingle(i);
  }
}

function clearAll() {
  uploadedFiles = []; compressedResults = [];
  document.getElementById('images-grid').innerHTML = '';
  document.getElementById('results-section').classList.add('hidden');
  document.getElementById('file-input').value = '';
}

function showProgress(text) {
  document.getElementById('progress-text').textContent = text;
  document.getElementById('progress-overlay').classList.add('visible');
}
function hideProgress() { document.getElementById('progress-overlay').classList.remove('visible'); }
function toggleTheme() { const d=document.documentElement; d.setAttribute('data-theme',d.getAttribute('data-theme')==='dark'?'light':'dark'); }
function toggleFaq(el) { const a=el.nextElementSibling; const s=el.querySelector('span'); a.classList.toggle('hidden'); s.textContent=a.classList.contains('hidden')?'+':'−'; }
</script>
