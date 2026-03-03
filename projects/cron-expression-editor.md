---
layout: default
title: Cron Expression Editor - Visual Cron Schedule Builder & Validator
permalink: /cron-editor/
description: Visual cron expression generator and editor online. Build, test, and validate cron schedules with real-time human-readable output.
keywords: cron expression generator, cron schedule builder, cron editor online, cron syntax tester, cron expression validator, how to write cron job, cron parser, cron translator, cron expression builder, schedule cron jobs, linux cron helper
tags: cron, scheduler, devtools, automation, validator, generator, editor, productivity
og:title: Cron Expression Editor - Visual Cron Schedule Builder
og:description: Build and validate cron expressions with a beginner-friendly visual editor, presets, and real-time natural language translation.
og:type: website
og:url: https://rkoots.github.io/cron-editor/
og:image: https://rkoots.github.io/assets/images/cron-editor.png
twitter:card: summary_large_image
twitter:title: Cron Expression Editor - Visual Cron Schedule Builder
twitter:description: Generate and validate cron expressions with presets and instant human-readable output.
twitter:image: https://rkoots.github.io/assets/images/cron-editor.png
---

<style>
:root {
  --primary: #2563eb;
  --primary-dark: #1d4ed8;
  --accent: #14b8a6;
  --warn: #f59e0b;
  --danger: #ef4444;
  --bg: #f8fafc;
  --text: #0f172a;
  --muted: #64748b;
  --card: #ffffff;
  --shadow: 0 12px 24px rgba(2, 6, 23, 0.08);
}

* { box-sizing: border-box; }

.cron-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background: linear-gradient(180deg, #eef2ff 0%, #f8fafc 100%);
  min-height: 100vh;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: var(--text);
}

.hero {
  text-align: center;
  margin-bottom: 24px;
  animation: fadeUp 420ms ease;
}

.hero h1 {
  margin: 0 0 8px;
  font-size: clamp(1.8rem, 4vw, 2.4rem);
  color: #0b3aa5;
}

.hero p {
  margin: 0 auto;
  max-width: 900px;
  color: #1e3a8a;
  font-size: 1.02rem;
}

.grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 16px;
}

.card {
  background: var(--card);
  border-radius: 14px;
  padding: 18px;
  box-shadow: var(--shadow);
  transition: transform 180ms ease, box-shadow 180ms ease;
  animation: fadeUp 500ms ease;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 28px rgba(2, 6, 23, 0.12);
}

.card h2 {
  margin: 0 0 14px;
  font-size: 1.25rem;
  color: var(--primary-dark);
  border-bottom: 2px solid #dbeafe;
  padding-bottom: 8px;
}

.field-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.field label {
  font-weight: 600;
  color: #334155;
}

.field small {
  color: var(--muted);
}

select,
input[type="text"],
textarea {
  width: 100%;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  padding: 10px 12px;
  background: #fff;
  font-size: 0.96rem;
  transition: border-color 160ms ease, box-shadow 160ms ease;
}

select:focus,
input[type="text"]:focus,
textarea:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
  outline: none;
}

.output-box {
  background: #0f172a;
  color: #e2e8f0;
  border-radius: 10px;
  padding: 10px 12px;
  font-family: Consolas, 'Courier New', monospace;
  font-size: 1rem;
  word-break: break-word;
}

.description-box {
  background: #ecfeff;
  border-left: 4px solid var(--accent);
  border-radius: 8px;
  padding: 10px 12px;
  color: #134e4a;
  margin-top: 10px;
}

.controls,
.preset-grid {
  display: grid;
  gap: 8px;
}

.controls {
  grid-template-columns: repeat(3, minmax(0, 1fr));
  margin-top: 12px;
}

.preset-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

button {
  border: none;
  border-radius: 10px;
  padding: 10px 12px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 120ms ease, opacity 120ms ease;
}

button:hover { transform: translateY(-1px); }
button:active { transform: translateY(0); }

.btn-primary { background: var(--primary); color: #fff; }
.btn-secondary { background: #e2e8f0; color: #0f172a; }
.btn-success { background: #059669; color: #fff; }
.btn-outline { background: #fff; border: 1px solid #cbd5e1; color: #0f172a; }

.status {
  margin-top: 10px;
  padding: 10px 12px;
  border-radius: 8px;
  font-size: 0.95rem;
  display: none;
}

.status.ok { display: block; background: #dcfce7; color: #166534; border-left: 4px solid #22c55e; }
.status.err { display: block; background: #fee2e2; color: #991b1b; border-left: 4px solid #ef4444; }

.field-help {
  margin-top: 14px;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  overflow: hidden;
}

.field-help table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.93rem;
}

.field-help th,
.field-help td {
  border-bottom: 1px solid #f1f5f9;
  padding: 8px 10px;
  text-align: left;
}

.field-help th { background: #f8fafc; color: #1e293b; }

.advanced {
  margin-top: 12px;
  padding: 12px;
  border-radius: 10px;
  border: 1px dashed #cbd5e1;
  background: #fafafa;
}

.faq, .cta, .content {
  margin-top: 18px;
}

.faq-item {
  background: #fff;
  border-radius: 12px;
  box-shadow: var(--shadow);
  padding: 14px;
  margin-bottom: 10px;
}

.faq-item h3 {
  margin: 0 0 6px;
  color: #1e3a8a;
  font-size: 1.02rem;
}

.cta .card {
  text-align: center;
}

.links a {
  display: inline-block;
  margin: 6px;
  padding: 10px 14px;
  border-radius: 8px;
  text-decoration: none;
  color: #fff;
  background: var(--primary);
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 980px) {
  .grid { grid-template-columns: 1fr; }
  .field-grid { grid-template-columns: 1fr; }
  .controls { grid-template-columns: 1fr; }
}
</style>

<div class="cron-page">
  <header class="hero">
    <h1>Cron Expression Editor - Visual Cron Schedule Builder</h1>
    <p>
      Use this cron expression generator to build, test, and validate cron schedules in seconds.
      This beginner-friendly cron editor online gives instant syntax feedback and plain-English translations.
    </p>
  </header>

  <!-- Ad Slot -->

  <main class="grid">
    <section class="card" aria-labelledby="builder-heading">
      <h2 id="builder-heading">Visual Cron Schedule Builder</h2>

      <div class="field-grid">
        <div class="field">
          <label for="minute">Minutes</label>
          <select id="minute"></select>
          <small>0-59, * for every minute, */n for intervals.</small>
        </div>

        <div class="field">
          <label for="hour">Hours</label>
          <select id="hour"></select>
          <small>0-23 in 24-hour format.</small>
        </div>

        <div class="field">
          <label for="dayOfMonth">Day of Month</label>
          <select id="dayOfMonth"></select>
          <small>1-31 or * for every day of month.</small>
        </div>

        <div class="field">
          <label for="month">Month</label>
          <select id="month"></select>
          <small>1-12 or * for every month.</small>
        </div>

        <div class="field">
          <label for="dayOfWeek">Day of Week</label>
          <select id="dayOfWeek"></select>
          <small>0-6 where 0 is Sunday, or * for every day.</small>
        </div>
      </div>

      <div class="controls">
        <button class="btn-primary" id="generateBtn" type="button">Generate / Validate</button>
        <button class="btn-success" id="copyBtn" type="button">Copy Expression</button>
        <button class="btn-secondary" id="resetBtn" type="button">Clear / Reset</button>
      </div>

      <div class="advanced">
        <label>
          <input type="checkbox" id="advancedToggle" />
          Advanced mode (manual cron editing)
        </label>
        <div style="margin-top:10px;">
          <input type="text" id="manualExpression" placeholder="e.g. 30 2 * * 1" disabled />
        </div>
      </div>

      <div class="status" id="statusMessage" role="status" aria-live="polite"></div>
    </section>

    <aside class="card" aria-labelledby="output-heading">
      <h2 id="output-heading">Generated Output</h2>

      <h3 style="margin:8px 0 6px;color:#334155;font-size:1rem;">Cron Expression</h3>
      <div class="output-box" id="cronOutput">* * * * *</div>

      <h3 style="margin:12px 0 6px;color:#334155;font-size:1rem;">Human-Readable Schedule</h3>
      <div class="description-box" id="humanOutput">Runs every minute.</div>

      <div class="field-help" aria-label="Field explanation table">
        <table>
          <thead>
            <tr>
              <th>Field</th>
              <th>Value</th>
              <th>Meaning</th>
            </tr>
          </thead>
          <tbody id="fieldExplainBody"></tbody>
        </table>
      </div>
    </aside>
  </main>

  <section class="content">
    <div class="card">
      <h2>Common Cron Presets</h2>
      <div class="preset-grid">
        <button class="btn-outline preset" data-exp="* * * * *">Every minute</button>
        <button class="btn-outline preset" data-exp="*/5 * * * *">Every 5 minutes</button>
        <button class="btn-outline preset" data-exp="0 * * * *">Every hour</button>
        <button class="btn-outline preset" data-exp="0 0 * * *">Daily at midnight</button>
        <button class="btn-outline preset" data-exp="0 0 * * 1">Weekly on Monday</button>
        <button class="btn-outline preset" data-exp="0 0 1 * *">Monthly on 1st</button>
      </div>
      <p style="margin-top:10px;color:#475569;">
        Need to learn how to write cron job schedules? Start with presets, then fine-tune each field in the visual builder.
      </p>
    </div>
  </section>

  <section class="faq" aria-labelledby="faq-heading">
    <h2 id="faq-heading" style="color:#1e3a8a;">FAQ: Cron Syntax Tester & Validator</h2>

    <article class="faq-item">
      <h3>What is a cron expression?</h3>
      <p>A cron expression is a 5-field schedule string (minute hour day month weekday) used to run recurring jobs automatically.</p>
    </article>

    <article class="faq-item">
      <h3>How do I write a cron job for every 5 minutes?</h3>
      <p>Use <code>*/5 * * * *</code>. This means the job runs every five minutes across all hours and days.</p>
    </article>

    <article class="faq-item">
      <h3>How do I schedule a job every Monday at 2:30 AM?</h3>
      <p>Use <code>30 2 * * 1</code>. That translates to minute 30, hour 2, every day-of-month, every month, Monday.</p>
    </article>

    <article class="faq-item">
      <h3>What do * and */n mean in cron syntax?</h3>
      <p><code>*</code> means every possible value in that field. <code>*/n</code> means every n interval in that field.</p>
    </article>

    <article class="faq-item">
      <h3>Can this cron expression validator detect invalid syntax?</h3>
      <p>Yes. Advanced mode validates structure and common value ranges so you can fix errors before deploying your cron job.</p>
    </article>
  </section>

  <section class="cta">
    <div class="card">
      <h2>More Interactive Tools</h2>
      <p>Explore more utilities for planning and automation.</p>
      <div class="links">
        <a href="/finance-pannner/">Finance Planner</a>
        <a href="/regex-generator-tester/">Regex Generator & Tester</a>
        <a href="/projects/">All Project Tools</a>
      </div>
    </div>
  </section>
</div>

<script>
(function () {
  const minuteEl = document.getElementById('minute');
  const hourEl = document.getElementById('hour');
  const domEl = document.getElementById('dayOfMonth');
  const monthEl = document.getElementById('month');
  const dowEl = document.getElementById('dayOfWeek');

  const cronOutput = document.getElementById('cronOutput');
  const humanOutput = document.getElementById('humanOutput');
  const fieldExplainBody = document.getElementById('fieldExplainBody');
  const statusMessage = document.getElementById('statusMessage');
  const advancedToggle = document.getElementById('advancedToggle');
  const manualExpression = document.getElementById('manualExpression');

  const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const monthNames = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

  const fieldMeta = [
    { key: 'minute', label: 'Minute', min: 0, max: 59, node: minuteEl },
    { key: 'hour', label: 'Hour', min: 0, max: 23, node: hourEl },
    { key: 'dom', label: 'Day of Month', min: 1, max: 31, node: domEl },
    { key: 'month', label: 'Month', min: 1, max: 12, node: monthEl },
    { key: 'dow', label: 'Day of Week', min: 0, max: 6, node: dowEl }
  ];

  function addOption(select, value, text) {
    const opt = document.createElement('option');
    opt.value = value;
    opt.textContent = text;
    select.appendChild(opt);
  }

  function buildSelects() {
    // Minutes
    addOption(minuteEl, '*', 'Every minute (*)');
    [2, 5, 10, 15, 30].forEach(n => addOption(minuteEl, `*/${n}`, `Every ${n} minutes (*/${n})`));
    for (let i = 0; i <= 59; i++) addOption(minuteEl, String(i), `At minute ${i}`);

    // Hours
    addOption(hourEl, '*', 'Every hour (*)');
    [2, 3, 6, 12].forEach(n => addOption(hourEl, `*/${n}`, `Every ${n} hours (*/${n})`));
    for (let i = 0; i <= 23; i++) addOption(hourEl, String(i), `At ${String(i).padStart(2, '0')}:00`);

    // Day of month
    addOption(domEl, '*', 'Every day (*)');
    for (let i = 1; i <= 31; i++) addOption(domEl, String(i), `Day ${i}`);

    // Month
    addOption(monthEl, '*', 'Every month (*)');
    for (let i = 1; i <= 12; i++) addOption(monthEl, String(i), monthNames[i]);

    // Day of week
    addOption(dowEl, '*', 'Every day (*)');
    dayNames.forEach((d, i) => addOption(dowEl, String(i), d));
  }

  function rangeCheck(v, min, max) {
    return /^\d+$/.test(v) && Number(v) >= min && Number(v) <= max;
  }

  function validatePart(part, min, max, allowNames) {
    if (part === '*') return true;

    const namePattern = allowNames ? /^(SUN|MON|TUE|WED|THU|FRI|SAT|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)$/i : null;

    const tokens = part.split(',');
    for (const tokenRaw of tokens) {
      const token = tokenRaw.trim();
      if (!token) return false;

      if (namePattern && namePattern.test(token)) continue;

      if (/^\*\/\d+$/.test(token)) {
        const step = Number(token.split('/')[1]);
        if (step < 1 || step > max) return false;
        continue;
      }

      if (/^\d+-\d+$/.test(token)) {
        const [a, b] = token.split('-').map(Number);
        if (a > b || a < min || b > max) return false;
        continue;
      }

      if (!rangeCheck(token, min, max)) return false;
    }

    return true;
  }

  function validateCron(expr) {
    const parts = expr.trim().split(/\s+/);
    if (parts.length !== 5) return { ok: false, error: 'Cron expression must have exactly 5 fields.' };

    const checks = [
      validatePart(parts[0], 0, 59, false),
      validatePart(parts[1], 0, 23, false),
      validatePart(parts[2], 1, 31, false),
      validatePart(parts[3], 1, 12, true),
      validatePart(parts[4], 0, 6, true)
    ];

    if (checks.every(Boolean)) return { ok: true, parts };

    return { ok: false, error: 'Invalid cron syntax. Check ranges, steps, lists, or field count.' };
  }

  function humanizeField(part, type) {
    if (part === '*') {
      if (type === 'minute') return 'every minute';
      if (type === 'hour') return 'every hour';
      if (type === 'dom') return 'every day';
      if (type === 'month') return 'every month';
      if (type === 'dow') return 'every day of week';
    }

    if (/^\*\/\d+$/.test(part)) {
      const n = part.split('/')[1];
      if (type === 'minute') return `every ${n} minutes`;
      if (type === 'hour') return `every ${n} hours`;
      return `every ${n} intervals`;
    }

    if (type === 'dow' && /^\d$/.test(part)) return dayNames[Number(part)] || part;
    if (type === 'month' && /^\d+$/.test(part)) return monthNames[Number(part)] || part;

    return part;
  }

  function getExpressionFromUI() {
    return [minuteEl.value, hourEl.value, domEl.value, monthEl.value, dowEl.value].join(' ');
  }

  function setUIFromExpression(expr) {
    const parts = expr.trim().split(/\s+/);
    if (parts.length !== 5) return false;

    const [m, h, dom, mo, dow] = parts;
    const assignIfOptionExists = (selectNode, value) => {
      const hasValue = Array.from(selectNode.options).some(opt => opt.value === value);
      if (hasValue) {
        selectNode.value = value;
      }
      return hasValue;
    };

    const applied = [
      assignIfOptionExists(minuteEl, m),
      assignIfOptionExists(hourEl, h),
      assignIfOptionExists(domEl, dom),
      assignIfOptionExists(monthEl, mo),
      assignIfOptionExists(dowEl, dow)
    ];

    // Return true only when every field could be represented in visual mode.
    // Manual mode still supports richer syntax like lists/ranges not in dropdowns.
    if (!applied.every(Boolean)) return false;

    return true;
  }

  function describe(parts) {
    const [m, h, dom, mo, dow] = parts;

    const exactTime = /^\d+$/.test(m) && /^\d+$/.test(h);
    let sentence = 'Runs ';

    if (m === '*' && h === '*' && dom === '*' && mo === '*' && dow === '*') {
      sentence += 'every minute.';
    } else if (/^\*\/\d+$/.test(m) && h === '*' && dom === '*' && mo === '*' && dow === '*') {
      sentence += `every ${m.split('/')[1]} minutes.`;
    } else if (m === '0' && h === '*' && dom === '*' && mo === '*' && dow === '*') {
      sentence += 'at minute 0 of every hour.';
    } else if (exactTime && dom === '*' && mo === '*' && /^\d+$/.test(dow)) {
      sentence += `every ${dayNames[Number(dow)]} at ${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}.`;
    } else if (exactTime && dom === '*' && mo === '*' && dow === '*') {
      sentence += `daily at ${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}.`;
    } else if (exactTime && /^\d+$/.test(dom) && mo === '*' && dow === '*') {
      sentence += `monthly on day ${dom} at ${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}.`;
    } else {
      sentence += `${humanizeField(m, 'minute')}, ${humanizeField(h, 'hour')}, ${humanizeField(dom, 'dom')}, ${humanizeField(mo, 'month')}, ${humanizeField(dow, 'dow')}.`;
    }

    return sentence;
  }

  function getMeaning(fieldKey, value) {
    if (value === '*') return 'Every value';
    if (/^\*\/\d+$/.test(value)) return `Every ${value.split('/')[1]} intervals`;

    if (fieldKey === 'dow' && /^\d$/.test(value)) return dayNames[Number(value)] || value;
    if (fieldKey === 'month' && /^\d+$/.test(value)) return monthNames[Number(value)] || value;

    if (/^\d+$/.test(value)) return `At ${value}`;
    if (value.includes(',')) return 'Multiple specific values';
    if (value.includes('-')) return 'Range of values';
    return 'Custom value';
  }

  function renderFieldExplain(parts) {
    const [m, h, dom, mo, dow] = parts;
    const vals = { minute: m, hour: h, dom, month: mo, dow };

    fieldExplainBody.innerHTML = fieldMeta.map(meta => {
      const val = vals[meta.key];
      return `<tr><td>${meta.label}</td><td><code>${val}</code></td><td>${getMeaning(meta.key, val)}</td></tr>`;
    }).join('');
  }

  function showStatus(type, text) {
    statusMessage.className = `status ${type}`;
    statusMessage.textContent = text;
  }

  function updateFromUI() {
    const expression = getExpressionFromUI();
    const result = validateCron(expression);

    if (!result.ok) {
      cronOutput.textContent = expression;
      humanOutput.textContent = 'Invalid cron expression.';
      showStatus('err', result.error);
      return;
    }

    cronOutput.textContent = expression;
    humanOutput.textContent = describe(result.parts);
    renderFieldExplain(result.parts);
    showStatus('ok', 'Valid cron expression generated.');

    if (!advancedToggle.checked) {
      manualExpression.value = expression;
    }
  }

  function updateFromManual() {
    const expression = manualExpression.value.trim();
    const result = validateCron(expression);

    if (!result.ok) {
      cronOutput.textContent = expression || '* * * * *';
      humanOutput.textContent = 'Invalid cron expression.';
      showStatus('err', result.error);
      return;
    }

    cronOutput.textContent = expression;
    humanOutput.textContent = describe(result.parts);
    renderFieldExplain(result.parts);
    showStatus('ok', 'Valid cron expression.');

    setUIFromExpression(expression);
  }

  function resetAll() {
    setUIFromExpression('* * * * *');
    advancedToggle.checked = false;
    manualExpression.disabled = true;
    manualExpression.value = '* * * * *';
    updateFromUI();
  }

  function copyExpression() {
    const txt = cronOutput.textContent;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(txt)
        .then(() => showStatus('ok', 'Cron expression copied to clipboard.'))
        .catch(() => showStatus('err', 'Clipboard access failed. Copy manually.'));
      return;
    }

    // Fallback
    const temp = document.createElement('textarea');
    temp.value = txt;
    document.body.appendChild(temp);
    temp.select();
    try {
      document.execCommand('copy');
      showStatus('ok', 'Cron expression copied to clipboard.');
    } catch (e) {
      showStatus('err', 'Clipboard copy failed. Copy manually.');
    }
    document.body.removeChild(temp);
  }

  buildSelects();
  resetAll();

  [minuteEl, hourEl, domEl, monthEl, dowEl].forEach(el => {
    el.addEventListener('change', updateFromUI);
  });

  document.getElementById('generateBtn').addEventListener('click', function () {
    if (advancedToggle.checked) {
      updateFromManual();
    } else {
      updateFromUI();
    }
  });

  document.getElementById('copyBtn').addEventListener('click', copyExpression);
  document.getElementById('resetBtn').addEventListener('click', resetAll);

  advancedToggle.addEventListener('change', function () {
    manualExpression.disabled = !this.checked;
    if (this.checked) {
      manualExpression.value = getExpressionFromUI();
      manualExpression.focus();
      showStatus('ok', 'Advanced mode enabled. You can now edit cron manually.');
    } else {
      updateFromUI();
    }
  });

  manualExpression.addEventListener('input', function () {
    if (advancedToggle.checked) updateFromManual();
  });

  document.querySelectorAll('.preset').forEach(btn => {
    btn.addEventListener('click', function () {
      const exp = this.getAttribute('data-exp');
      if (!setUIFromExpression(exp)) return;
      manualExpression.value = exp;
      updateFromUI();
    });
  });
})();
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a cron expression?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A cron expression is a 5-field schedule string used to define recurring tasks by minute, hour, day of month, month, and day of week."
      }
    },
    {
      "@type": "Question",
      "name": "How do I write a cron job for every 5 minutes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use */5 * * * * to run a job every 5 minutes."
      }
    },
    {
      "@type": "Question",
      "name": "How do I schedule a job every Monday at 2:30 AM?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use 30 2 * * 1, where 30 is minute, 2 is hour, and 1 is Monday."
      }
    },
    {
      "@type": "Question",
      "name": "Can this cron expression validator detect invalid syntax?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, it checks field count and common cron ranges, steps, lists, and ranges for quick validation feedback."
      }
    }
  ]
}
</script>
