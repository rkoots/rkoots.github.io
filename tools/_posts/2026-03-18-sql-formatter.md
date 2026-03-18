---
layout: default
title: "SQLIQO – SQL Query Formatter & Beautifier | Free Online SQL Formatter Tool"
excerpt: "Format, beautify, and minify SQL queries online with SQLIQO. Supports SELECT, INSERT, UPDATE, DELETE, JOIN, and subqueries. Instant syntax highlighting and copy."
date: 2026-03-18
categories: tools
permalink: /tools/sql-formatter/
description: "Free online SQL formatter and beautifier. Instantly format SQL queries with proper indentation, keyword casing, and syntax highlighting for PostgreSQL, MySQL, and more."
keywords: ["sql formatter online", "sql beautifier", "format sql query", "sql query formatter free", "sql pretty printer", "sql indentation tool", "online sql formatter", "mysql formatter", "postgresql formatter"]
tags: [SQL, database, formatter, developer, utility]
---

<style>
:root{--primary:#0284c7;--primary-dark:#0369a1;--accent:#f59e0b;--success:#10b981;--danger:#ef4444;--bg:#f0f9ff;--card:#fff;--text:#0c4a6e;--muted:#6b7280;--border:#bae6fd;--shadow:0 8px 32px rgba(2,132,199,0.10);}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;}
.sqliqo{max-width:1100px;margin:0 auto;padding:24px 16px 60px;}
.hero{text-align:center;padding:36px 20px 28px;}
.hero-badge{display:inline-block;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-size:0.72rem;font-weight:700;letter-spacing:2px;padding:4px 14px;border-radius:20px;margin-bottom:14px;}
.hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;}
.hero p{color:var(--muted);font-size:1rem;max-width:600px;margin:0 auto;}
.card{background:var(--card);border-radius:14px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;border:1px solid var(--border);}
.toolbar{display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap;align-items:center;}
.btn{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;border-radius:8px;border:none;cursor:pointer;font-size:0.9rem;font-weight:600;transition:all 0.2s;}
.btn-primary{background:var(--primary);color:#fff;}
.btn-primary:hover{background:var(--primary-dark);transform:translateY(-1px);}
.btn-success{background:var(--success);color:#fff;}
.btn-success:hover{filter:brightness(1.1);}
.btn-ghost{background:var(--bg);color:var(--primary);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--primary);}
.btn-danger{background:#fff0f0;color:var(--danger);border:1px solid #fecaca;}
select.opt{padding:8px 12px;border-radius:8px;border:1px solid var(--border);background:var(--card);color:var(--text);font-size:0.88rem;}
.editors{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.editor-label{font-size:0.78rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;}
textarea{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.88rem;background:var(--card);color:var(--text);resize:vertical;line-height:1.6;}
textarea:focus{outline:none;border-color:var(--primary);}
.output-box{width:100%;border:2px solid #bae6fd;border-radius:10px;padding:12px;font-family:Consolas,'Courier New',monospace;font-size:0.88rem;background:#f0f9ff;color:#0c4a6e;white-space:pre-wrap;word-break:break-word;line-height:1.6;min-height:200px;max-height:400px;overflow:auto;}
.stats{display:flex;gap:12px;flex-wrap:wrap;margin-top:10px;}
.stat-chip{padding:4px 12px;border-radius:20px;font-size:0.8rem;font-weight:600;background:#e0f2fe;color:#0369a1;}
.examples{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin-top:16px;}
.example-btn{padding:10px 14px;border:1px solid var(--border);border-radius:8px;background:var(--card);color:var(--text);cursor:pointer;font-size:0.85rem;text-align:left;transition:all 0.2s;}
.example-btn:hover{border-color:var(--primary);color:var(--primary);}
.example-btn strong{display:block;margin-bottom:4px;}
@media(max-width:700px){.editors{grid-template-columns:1fr;}}
</style>

<div class="sqliqo">
  <header class="hero">
    <div class="hero-badge">FREE SQL FORMATTER</div>
    <h1>SQLIQO – SQL Query Formatter</h1>
    <p>Beautify messy SQL instantly. Format queries with proper indentation, uppercase keywords, and clean structure for MySQL, PostgreSQL, SQLite, and more.</p>
  </header>

  <div class="card">
    <div class="toolbar">
      <button class="btn btn-primary" onclick="formatSQL()">Format SQL</button>
      <button class="btn btn-ghost" onclick="minifySQL()">Minify</button>
      <button class="btn btn-success" onclick="copyOutput()">Copy Result</button>
      <button class="btn btn-danger" onclick="clearAll()">Clear</button>
      <select class="opt" id="caseOpt">
        <option value="upper">Keywords UPPERCASE</option>
        <option value="lower">Keywords lowercase</option>
        <option value="preserve">Preserve case</option>
      </select>
      <select class="opt" id="indentOpt">
        <option value="2">2 spaces</option>
        <option value="4">4 spaces</option>
        <option value="tab">Tab</option>
      </select>
    </div>

    <div class="editors">
      <div>
        <div class="editor-label">Input SQL</div>
        <textarea id="sqlInput" rows="14" placeholder="Paste your SQL query here…"></textarea>
      </div>
      <div>
        <div class="editor-label">Formatted Output</div>
        <div class="output-box" id="sqlOutput">Formatted SQL will appear here…</div>
      </div>
    </div>

    <div class="stats" id="statsBar" style="display:none;">
      <span class="stat-chip" id="statLines"></span>
      <span class="stat-chip" id="statChars"></span>
      <span class="stat-chip" id="statKeywords"></span>
    </div>
  </div>

  <div class="card">
    <div class="editor-label" style="margin-bottom:12px;">Quick Examples</div>
    <div class="examples">
      <button class="example-btn" onclick="loadExample('select')"><strong>SELECT Query</strong>Multi-table JOIN with WHERE</button>
      <button class="example-btn" onclick="loadExample('insert')"><strong>INSERT Statement</strong>Multi-row insert</button>
      <button class="example-btn" onclick="loadExample('update')"><strong>UPDATE Statement</strong>Conditional update</button>
      <button class="example-btn" onclick="loadExample('create')"><strong>CREATE TABLE</strong>Table definition</button>
      <button class="example-btn" onclick="loadExample('subquery')"><strong>Subquery</strong>Nested SELECT</button>
    </div>
  </div>
</div>

<script>
const EXAMPLES = {
  select: `select u.id,u.name,u.email,o.total,o.created_at from users u inner join orders o on u.id=o.user_id where u.active=1 and o.total>100 order by o.created_at desc limit 50;`,
  insert: `insert into products(name,category,price,stock,created_at) values('Widget A','Electronics',29.99,150,now()),('Widget B','Electronics',49.99,80,now()),('Gadget C','Accessories',9.99,500,now());`,
  update: `update users set last_login=now(),login_count=login_count+1,updated_at=now() where id=? and active=1;`,
  create: `create table orders(id int auto_increment primary key,user_id int not null,total decimal(10,2) not null default 0.00,status varchar(20) not null default 'pending',created_at timestamp default current_timestamp,updated_at timestamp default current_timestamp on update current_timestamp,foreign key(user_id) references users(id) on delete cascade);`,
  subquery: `select name,email from users where id in(select user_id from orders where total>(select avg(total) from orders) and created_at>date_sub(now(),interval 30 day)) order by name;`
};

const KEYWORDS = ['SELECT','FROM','WHERE','JOIN','INNER JOIN','LEFT JOIN','RIGHT JOIN','FULL JOIN','CROSS JOIN','ON','AND','OR','NOT','IN','NOT IN','EXISTS','BETWEEN','LIKE','IS NULL','IS NOT NULL','GROUP BY','ORDER BY','HAVING','LIMIT','OFFSET','INSERT INTO','VALUES','UPDATE','SET','DELETE FROM','CREATE TABLE','ALTER TABLE','DROP TABLE','CREATE INDEX','PRIMARY KEY','FOREIGN KEY','REFERENCES','DEFAULT','NOT NULL','UNIQUE','AUTO_INCREMENT','DISTINCT','AS','UNION','UNION ALL','INTERSECT','EXCEPT','CASE','WHEN','THEN','ELSE','END','WITH','COALESCE','NULLIF','CAST','CONVERT','COUNT','SUM','AVG','MIN','MAX','NOW','DATE','TIMESTAMP','VARCHAR','INT','DECIMAL','BOOLEAN','TEXT'];

function formatSQL() {
  const raw = document.getElementById('sqlInput').value.trim();
  if (!raw) return;
  const caseOpt = document.getElementById('caseOpt').value;
  const indentVal = document.getElementById('indentOpt').value;
  const indent = indentVal === 'tab' ? '\t' : ' '.repeat(Number(indentVal));

  const CLAUSE_KEYWORDS = ['SELECT','FROM','WHERE','INNER JOIN','LEFT JOIN','RIGHT JOIN','FULL JOIN','CROSS JOIN','JOIN','ON','AND','OR','GROUP BY','ORDER BY','HAVING','LIMIT','OFFSET','UNION ALL','UNION','INTERSECT','EXCEPT','INSERT INTO','VALUES','UPDATE','SET','DELETE FROM','CREATE TABLE','ALTER TABLE'];

  let sql = raw.replace(/\s+/g, ' ');

  CLAUSE_KEYWORDS.forEach(kw => {
    const re = new RegExp(`\\b${kw}\\b`, 'gi');
    sql = sql.replace(re, `\n${kw}`);
  });

  sql = sql.replace(/,\s*/g, ',\n' + indent + indent);

  const lines = sql.split('\n').map(l => l.trim()).filter(l => l.length > 0);
  let formatted = '';
  lines.forEach(line => {
    const upper = line.toUpperCase();
    const isClause = CLAUSE_KEYWORDS.some(k => upper.startsWith(k));
    formatted += (isClause ? '' : indent) + applyCase(line, caseOpt) + '\n';
  });

  document.getElementById('sqlOutput').textContent = formatted.trim();
  showStats(formatted.trim());
}

function applyCase(sql, opt) {
  if (opt === 'preserve') return sql;
  return sql.replace(/\b([A-Z_]+)\b/g, (m) => {
    const up = m.toUpperCase();
    if (KEYWORDS.includes(up)) return opt === 'upper' ? up : up.toLowerCase();
    return m;
  });
}

function minifySQL() {
  const raw = document.getElementById('sqlInput').value.trim();
  if (!raw) return;
  const minified = raw.replace(/\s+/g, ' ').replace(/\s*([,;()])\s*/g, '$1').trim();
  document.getElementById('sqlOutput').textContent = minified;
  showStats(minified);
}

function showStats(sql) {
  const lines = sql.split('\n').length;
  const chars = sql.length;
  const kwCount = KEYWORDS.filter(k => new RegExp('\\b' + k + '\\b', 'i').test(sql)).length;
  document.getElementById('statLines').textContent = `${lines} lines`;
  document.getElementById('statChars').textContent = `${chars} chars`;
  document.getElementById('statKeywords').textContent = `${kwCount} keywords`;
  document.getElementById('statsBar').style.display = 'flex';
}

function copyOutput() {
  const text = document.getElementById('sqlOutput').textContent;
  navigator.clipboard.writeText(text).then(() => alert('Copied to clipboard!'));
}

function clearAll() {
  document.getElementById('sqlInput').value = '';
  document.getElementById('sqlOutput').textContent = 'Formatted SQL will appear here…';
  document.getElementById('statsBar').style.display = 'none';
}

function loadExample(key) {
  document.getElementById('sqlInput').value = EXAMPLES[key];
  formatSQL();
}

document.getElementById('sqlInput').addEventListener('keydown', function(e) {
  if (e.ctrlKey && e.key === 'Enter') formatSQL();
});
</script>
