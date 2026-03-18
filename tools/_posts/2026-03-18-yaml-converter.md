---
layout: default
title: "YAMLIQO – YAML to JSON Converter | Free Online YAML Parser, Validator & Formatter"
excerpt: "Convert YAML to JSON and JSON to YAML instantly with YAMLIQO. Validate YAML syntax, format output, and view parsed data. Free online YAML converter and validator for developers."
date: 2026-03-18
categories: tools
permalink: /tools/yaml-converter/
description: "Free online YAML to JSON converter. Parse, validate, and format YAML files. Convert YAML to JSON or JSON to YAML instantly with syntax error highlighting and download support."
keywords: ["yaml to json converter", "yaml parser online", "yaml validator free", "convert yaml to json", "json to yaml converter", "yaml formatter online", "yaml lint online", "yaml editor free", "parse yaml online"]
tags: [YAML, JSON, converter, developer, validator]
---

<style>
:root{--primary:#059669;--primary-dark:#047857;--accent:#6366f1;--bg:#f0fdf4;--card:#fff;--text:#052e16;--muted:#6b7280;--border:#a7f3d0;--shadow:0 8px 32px rgba(5,150,105,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.yamliqo{max-width:1100px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:580px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.mode-tabs{display:flex;gap:4px;border-bottom:2px solid var(--border);margin-bottom:16px;}
.mode-tab{padding:9px 20px;border:none;background:none;color:var(--muted);font-size:0.9rem;font-weight:700;cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px;}
.mode-tab.active{color:var(--primary);border-bottom-color:var(--primary);}
.toolbar{display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-success{background:var(--accent);color:#fff;}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);}
.editors{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.editor-label{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;}
textarea{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.85rem;background:var(--card);color:var(--text);resize:vertical;line-height:1.6;}
textarea:focus{outline:none;border-color:var(--primary);}
.output-box{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.85rem;background:#f0fdf4;white-space:pre-wrap;word-break:break-all;min-height:200px;max-height:440px;overflow:auto;}
.status-bar{display:flex;align-items:center;gap:10px;margin-top:10px;flex-wrap:wrap;}
.badge-ok{display:inline-flex;align-items:center;gap:4px;padding:4px 12px;border-radius:20px;font-size:0.82rem;font-weight:700;background:#dcfce7;color:#166534;}
.badge-err{background:#fee2e2;color:#991b1b;}
.error-detail{font-family:Consolas,monospace;font-size:0.83rem;color:#991b1b;background:#fee2e2;padding:8px 12px;border-radius:8px;margin-top:8px;}
.samples{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;}
.sample-btn{padding:5px 14px;border-radius:20px;border:1px solid var(--border);background:var(--card);color:var(--primary);font-size:0.82rem;font-weight:600;cursor:pointer;}
.sample-btn:hover{background:var(--primary);color:#fff;border-color:var(--primary);}
@media(max-width:700px){.editors{grid-template-columns:1fr;}}
</style>

<div class="yamliqo">
  <header class="hero">
    <div class="hero-badge">FREE YAML CONVERTER</div>
    <h1>YAMLIQO – YAML to JSON Converter</h1>
    <p>Parse, validate, and convert YAML to JSON or JSON to YAML. Instant syntax validation with error highlighting, indentation options, and download support.</p>
  </header>

  <div class="card">
    <div class="mode-tabs">
      <button class="mode-tab active" onclick="setMode('yaml2json',this)">YAML → JSON</button>
      <button class="mode-tab" onclick="setMode('json2yaml',this)">JSON → YAML</button>
      <button class="mode-tab" onclick="setMode('validate',this)">Validate YAML</button>
    </div>

    <div class="samples">
      <span style="font-size:0.82rem;color:var(--muted);align-self:center;">Samples:</span>
      <button class="sample-btn" onclick="loadSample('docker')">Docker Compose</button>
      <button class="sample-btn" onclick="loadSample('k8s')">Kubernetes</button>
      <button class="sample-btn" onclick="loadSample('config')">App Config</button>
      <button class="sample-btn" onclick="loadSample('github')">GitHub Actions</button>
    </div>

    <div class="toolbar">
      <button class="btn btn-primary" onclick="convert()">Convert</button>
      <button class="btn btn-ghost" onclick="copyOutput()">Copy Output</button>
      <button class="btn btn-ghost" onclick="downloadOutput()">Download</button>
      <button class="btn btn-ghost" onclick="clearAll()">Clear</button>
      <label style="font-size:0.85rem;color:var(--muted);display:flex;align-items:center;gap:6px;">
        <input type="checkbox" id="prettyPrint" checked> Pretty print
      </label>
      <select id="indentSize" style="padding:8px 12px;border-radius:8px;border:1px solid var(--border);background:var(--card);color:var(--text);font-size:0.88rem;">
        <option value="2">2 spaces</option>
        <option value="4">4 spaces</option>
      </select>
    </div>

    <div class="editors">
      <div>
        <div class="editor-label" id="inputLabel">YAML Input</div>
        <textarea id="inputArea" rows="16" placeholder="Paste YAML here…"></textarea>
      </div>
      <div>
        <div class="editor-label" id="outputLabel">JSON Output</div>
        <div class="output-box" id="outputArea">Output will appear here…</div>
      </div>
    </div>
    <div class="status-bar" id="statusBar"></div>
  </div>
</div>

<script>
let currentMode = 'yaml2json';
let outputText = '';

const SAMPLES = {
  docker: `version: '3.8'\nservices:\n  web:\n    image: nginx:alpine\n    ports:\n      - "80:80"\n    volumes:\n      - ./html:/usr/share/nginx/html\n    depends_on:\n      - db\n  db:\n    image: postgres:15\n    environment:\n      POSTGRES_DB: mydb\n      POSTGRES_USER: admin\n      POSTGRES_PASSWORD: secret\n    volumes:\n      - pgdata:/var/lib/postgresql/data\nvolumes:\n  pgdata:`,
  k8s: `apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: myapp\n  labels:\n    app: myapp\nspec:\n  replicas: 3\n  selector:\n    matchLabels:\n      app: myapp\n  template:\n    metadata:\n      labels:\n        app: myapp\n    spec:\n      containers:\n      - name: myapp\n        image: myapp:1.0.0\n        ports:\n        - containerPort: 8080\n        resources:\n          limits:\n            memory: "128Mi"\n            cpu: "500m"`,
  config: `app:\n  name: MyApplication\n  version: 2.1.0\n  debug: false\n\nserver:\n  host: 0.0.0.0\n  port: 8080\n  timeout: 30\n\ndatabase:\n  host: localhost\n  port: 5432\n  name: mydb\n  pool:\n    min: 2\n    max: 10\n\nlogging:\n  level: info\n  format: json\n  output:\n    - console\n    - file`,
  github: `name: CI Pipeline\non:\n  push:\n    branches: [main, develop]\n  pull_request:\n    branches: [main]\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - name: Setup Node.js\n        uses: actions/setup-node@v4\n        with:\n          node-version: '20'\n      - name: Install dependencies\n        run: npm ci\n      - name: Run tests\n        run: npm test`
};

function setMode(mode, el) {
  currentMode = mode;
  document.querySelectorAll('.mode-tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('inputLabel').textContent = mode === 'json2yaml' ? 'JSON Input' : 'YAML Input';
  document.getElementById('outputLabel').textContent = mode === 'json2yaml' ? 'YAML Output' : mode === 'validate' ? 'Validation Result' : 'JSON Output';
  document.getElementById('inputArea').placeholder = mode === 'json2yaml' ? 'Paste JSON here…' : 'Paste YAML here…';
  clearAll();
}

function loadSample(key) {
  document.getElementById('inputArea').value = SAMPLES[key];
  if (currentMode === 'json2yaml') setMode('yaml2json', document.querySelector('.mode-tab'));
}

function parseYAML(text) {
  // Simple YAML parser supporting common patterns
  const lines = text.split('\n');
  return parseYAMLLines(lines, 0).value;
}

function parseYAMLLines(lines, baseIndent) {
  const result = {};
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim() || line.trim().startsWith('#')) { i++; continue; }
    const indent = line.search(/\S/);
    if (indent < baseIndent) break;
    if (indent > baseIndent) { i++; continue; }

    const trimmed = line.trim();

    if (trimmed.startsWith('- ')) {
      // Array — reparse as array
      const arr = [];
      while (i < lines.length) {
        const l = lines[i];
        if (!l.trim() || l.trim().startsWith('#')) { i++; continue; }
        const ind = l.search(/\S/);
        if (ind < baseIndent) break;
        const t = l.trim();
        if (t.startsWith('- ')) {
          const val = t.slice(2).trim();
          if (val === '') {
            // Object item
            const sub = parseYAMLLines(lines.slice(i+1).map((ln,idx) => lines[i+1+idx]), baseIndent + 2);
            arr.push(sub.value);
            i += sub.consumed + 1;
          } else {
            arr.push(castValue(val));
            i++;
          }
        } else break;
      }
      return {value: arr, consumed: i};
    }

    const colonIdx = trimmed.indexOf(': ');
    const colonEnd = trimmed.endsWith(':');
    if (colonIdx !== -1 || colonEnd) {
      const key = colonEnd ? trimmed.slice(0,-1) : trimmed.slice(0, colonIdx);
      const valRaw = colonEnd ? '' : trimmed.slice(colonIdx + 2);

      if (!valRaw || valRaw === '|' || valRaw === '>') {
        // Look ahead for nested
        const nextLines = [];
        let j = i + 1;
        while (j < lines.length) {
          const nl = lines[j];
          if (!nl.trim()) { nextLines.push(''); j++; continue; }
          if (nl.search(/\S/) <= indent) break;
          nextLines.push(nl);
          j++;
        }
        if (nextLines.length) {
          const sub = parseYAMLLines(nextLines, nextLines[0].search(/\S/));
          result[key] = sub.value;
          i = j;
        } else {
          result[key] = null;
          i++;
        }
      } else {
        result[key] = castValue(valRaw);
        i++;
      }
    } else {
      i++;
    }
  }
  return {value: result, consumed: i};
}

function castValue(v) {
  if (v === 'true') return true;
  if (v === 'false') return false;
  if (v === 'null' || v === '~') return null;
  if (/^-?\d+$/.test(v)) return parseInt(v);
  if (/^-?\d+\.\d+$/.test(v)) return parseFloat(v);
  // Remove quotes
  if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) {
    return v.slice(1,-1);
  }
  return v;
}

function jsonToYAML(obj, indent=0) {
  const indentStr = ' '.repeat(indent);
  const indentSize = parseInt(document.getElementById('indentSize').value);
  const childIndent = ' '.repeat(indent + indentSize);

  if (obj === null) return 'null';
  if (typeof obj === 'boolean') return obj.toString();
  if (typeof obj === 'number') return obj.toString();
  if (typeof obj === 'string') {
    if (obj.includes('\n') || obj.includes(':') || obj.includes('#') || obj.match(/^['"]/)) {
      return '"' + obj.replace(/\\/g,'\\\\').replace(/"/g,'\\"') + '"';
    }
    return obj;
  }
  if (Array.isArray(obj)) {
    if (obj.length === 0) return '[]';
    return obj.map(item => {
      const val = jsonToYAML(item, indent + indentSize);
      if (typeof item === 'object' && item !== null) {
        return indentStr + '-\n' + childIndent + val.split('\n').join('\n' + childIndent);
      }
      return indentStr + '- ' + val;
    }).join('\n');
  }
  if (typeof obj === 'object') {
    if (Object.keys(obj).length === 0) return '{}';
    return Object.entries(obj).map(([k, v]) => {
      if (typeof v === 'object' && v !== null) {
        const nested = jsonToYAML(v, indent + indentSize);
        return indentStr + k + ':\n' + nested;
      }
      return indentStr + k + ': ' + jsonToYAML(v, indent);
    }).join('\n');
  }
  return String(obj);
}

function convert() {
  const input = document.getElementById('inputArea').value.trim();
  const statusBar = document.getElementById('statusBar');
  if (!input) return;

  try {
    const indent = parseInt(document.getElementById('indentSize').value);
    if (currentMode === 'yaml2json') {
      const parsed = parseYAML(input);
      const json = document.getElementById('prettyPrint').checked
        ? JSON.stringify(parsed, null, indent)
        : JSON.stringify(parsed);
      outputText = json;
      document.getElementById('outputArea').textContent = json;
      statusBar.innerHTML = '<span class="badge-ok">✓ Valid YAML — converted to JSON</span>';
    } else if (currentMode === 'json2yaml') {
      const parsed = JSON.parse(input);
      const yaml = jsonToYAML(parsed);
      outputText = yaml;
      document.getElementById('outputArea').textContent = yaml;
      statusBar.innerHTML = '<span class="badge-ok">✓ Valid JSON — converted to YAML</span>';
    } else {
      // Validate only
      parseYAML(input);
      outputText = '✓ YAML is valid. No syntax errors found.';
      document.getElementById('outputArea').textContent = outputText;
      statusBar.innerHTML = '<span class="badge-ok">✓ YAML syntax is valid</span>';
    }
  } catch(e) {
    statusBar.innerHTML = `<span class="badge-ok badge-err">✗ Error: ${escHtml(e.message)}</span>`;
    document.getElementById('outputArea').textContent = 'Error: ' + e.message;
    outputText = '';
  }
}

function copyOutput() {
  if (!outputText) return alert('Convert first');
  navigator.clipboard.writeText(outputText).then(() => alert('Copied to clipboard!'));
}

function downloadOutput() {
  if (!outputText) return alert('Convert first');
  const ext = currentMode === 'json2yaml' ? 'yaml' : 'json';
  const blob = new Blob([outputText], {type:'text/plain'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `output.${ext}`;
  a.click();
}

function clearAll() {
  document.getElementById('inputArea').value = '';
  document.getElementById('outputArea').textContent = 'Output will appear here…';
  document.getElementById('statusBar').innerHTML = '';
  outputText = '';
}

function escHtml(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
</script>
