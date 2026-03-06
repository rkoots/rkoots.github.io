---
layout: default
title: "PULSAR - Market Outlook"
categories: finance
permalink: /finance/daily-market-outlook/
excerpt: Live Indian market dashboard with real-time Nifty, Bank Nifty indices, top gainers/losers, and technical sentiment signals.
author: "Rajkumar V"
summary: "Daily Market Outlook with financial news, trends, Nifty, Bank Nifty, momentum stocks, and more. Daily Market Outlook - Nifty & Bank Nifty Live"
keywords: [Daily Market Outlook, Nifty, Bank Nifty, Top Gainers, Top Losers, Market Sentiment, Finance News, Sector-wise Market Performance]
tags: [Daily Market Outlook, Nifty, Bank Nifty, Finance News, Market Sentiment, Sector-wise Performance, Top Gainers, Top Losers]
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700&family=Outfit:wght@500;700&display=swap" rel="stylesheet">

<section class="outlook-shell">
  <div class="hero-grid">
    <header class="outlook-hero reveal">
      <p class="chip">LIVE • TRADING</p>
      <h1><span style="background: linear-gradient(135deg, #66c0ff, #4a90e2); color: white; padding: 8px 16px; border-radius: 12px; font-weight: 700; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(102, 192, 255, 0.3); display: inline-block;">⚡ PULSAR</span> - Market Outlook</h1>
      <p>
        Browser-side realtime pulse for your core stock universe + ETFs. Includes breadth,
        momentum, risk-bucket heat, and top movers from TradingView India scanner.
        Daily Market Outlook - Nifty & Bank Nifty Live
      </p>
      <div class="hero-meta">
        <span id="lastRefresh">Last refresh: --</span>
        <span id="fetchStatus">Status: Waiting for first fetch</span>
        <button id="retryBtn" type="button" class="retry-btn">Refresh now</button>
      </div>
    </header>

    <section class="indices-grid reveal delay-1">
      <article class="index-card">
        <p>NIFTY 50</p>
        <h3 id="niftyCard">--</h3>
        <small id="niftyChange">--</small>
      </article>
      <article class="index-card">
        <p>BANK NIFTY</p>
        <h3 id="bankniftyCard">--</h3>
        <small id="bankniftyChange">--</small>
      </article>
      <article class="index-card">
        <p>SENSEX</p>
        <h3 id="sensexCard">--</h3>
        <small id="sensexChange">--</small>
      </article>
      <article class="index-card">
        <p>Advancers / Decliners</p>
        <h3 id="breadthCard">-- / --</h3>
        <small>Based on intraday % change</small>
      </article>
    </section>
  </div>

  <section class="summary-grid reveal delay-2">
    <article class="stat-card">
      <p>Universe Coverage</p>
      <h3 id="coverageCard">-- / --</h3>
      <small>Fetched symbols vs configured watchlist</small>
    </article>
    <article class="stat-card">
      <p>Average Return</p>
      <h3 id="avgChangeCard">--</h3>
      <small>Equal-weight watchlist move</small>
    </article>
    <article class="stat-card">
      <p>Risk-Adjusted Pulse</p>
      <h3 id="riskPulseCard">--</h3>
      <small>Higher-risk names weighted down</small>
    </article>
  </section>

  <section class="cards-3col reveal delay-3">
    <article class="panel">
      <h2>Top 8 Gainers</h2>
      <div id="gainersList" class="list-stack"></div>
    </article>
    <article class="panel">
      <h2>Top 8 Losers</h2>
      <div id="losersList" class="list-stack"></div>
    </article>
    <article class="panel">
      <h2>Signal Snapshot</h2>
      <ul class="clean-list">
        <li><span>ADX Trend Leaders</span><strong id="adxLeaders">--</strong></li>
        <li><span>Above SMA50</span><strong id="sma50Breadth">--</strong></li>
        <li><span>Above SMA100</span><strong id="sma100Breadth">--</strong></li>
        <li><span>Median RSI(1D)</span><strong id="medianRsi">--</strong></li>
      </ul>
    </article>
  </section>

  <section class="panel reveal delay-3">
    <h2>Risk Bucket Performance</h2>
    <div id="riskBuckets" class="risk-grid"></div>
  </section>

  <section class="table-grid reveal delay-3">
    <article class="panel">
      <h2>Stocks Monitor</h2>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Symbol</th>
              <th>Close</th>
              <th>Chg%</th>
              <th>ADR%</th>
              <th>RSI</th>
              <th>ADX</th>
              <th>SMA50 Gap%</th>
              <th>Risk</th>
            </tr>
          </thead>
          <tbody id="stocksTableBody"></tbody>
        </table>
      </div>
    </article>

    <article class="panel">
      <h2>ETF Monitor</h2>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>ETF</th>
              <th>Close</th>
              <th>Chg%</th>
              <th>1W ROC%</th>
              <th>1M ROC%</th>
              <th>RSI</th>
            </tr>
          </thead>
          <tbody id="etfTableBody"></tbody>
        </table>
      </div>
    </article>
  </section>

  <section class="panel api-note reveal delay-3">
    <p>
      Source: <strong>https://rkoots.github.io/</strong>.
      Refresh interval: 60 seconds. If your browser/network blocks this endpoint due to CORS,
      use a backend proxy for guaranteed reliability.
    </p>
  </section>
</section>

<style>
  :root {
    --bg-1: #091218;
    --bg-2: #12202a;
    --panel: rgba(9, 20, 28, 0.78);
    --line: rgba(158, 196, 214, 0.22);
    --text: #e8f4f6;
    --muted: #93adb7;
    --up: #56f0a0;
    --down: #ff7d76;
    --accent: #66c0ff;
    --warn: #ffca6b;
  }

  .outlook-shell {
    font-family: "Sora", sans-serif;
    color: var(--text);
    max-width: 1180px;
    margin: 1rem auto 2rem;
    border-radius: 26px;
    padding: clamp(1rem, 2.3vw, 2rem);
    border: 1px solid var(--line);
    background:
      radial-gradient(130% 95% at 0% -8%, rgba(48, 93, 131, 0.45) 0%, transparent 52%),
      radial-gradient(80% 80% at 100% 0%, rgba(18, 92, 99, 0.35) 0%, transparent 40%),
      linear-gradient(145deg, var(--bg-1) 0%, var(--bg-2) 58%, #0a1419 100%);
    box-shadow: 0 18px 60px rgba(0, 0, 0, 0.35);
  }

  .hero-grid,
  .indices-grid,
  .summary-grid,
  .cards-3col,
  .table-grid,
  .risk-grid {
    display: grid;
    gap: 0.9rem;
  }

  .chip {
    display: inline-block;
    font-size: 0.76rem;
    letter-spacing: 0.12em;
    color: #c4e7ff;
    border: 1px solid rgba(102, 192, 255, 0.4);
    background: rgba(102, 192, 255, 0.12);
    border-radius: 999px;
    padding: 0.26rem 0.64rem;
    margin-bottom: 0.6rem;
  }

  .outlook-hero h1,
  .panel h2,
  .stat-card h3 {
    font-family: "Outfit", sans-serif;
    margin: 0;
    letter-spacing: 0.015em;
  }

  .outlook-hero p {
    color: var(--muted);
    max-width: 80ch;
  }

  .hero-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin-top: 0.75rem;
  }

  .hero-meta span {
    border: 1px solid var(--line);
    border-radius: 999px;
    padding: 0.32rem 0.7rem;
    font-size: 0.78rem;
    color: #c6dde4;
    background: rgba(255, 255, 255, 0.03);
  }

  .retry-btn {
    border: 1px solid rgba(102, 192, 255, 0.5);
    background: rgba(102, 192, 255, 0.14);
    color: #d7ecff;
    border-radius: 999px;
    padding: 0.35rem 0.8rem;
    font-size: 0.76rem;
    cursor: pointer;
  }

  .retry-btn:hover {
    background: rgba(102, 192, 255, 0.24);
  }

  .indices-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }

  .summary-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .stat-card,
  .index-card,
  .panel {
    border: 1px solid var(--line);
    border-radius: 16px;
    background: var(--panel);
    backdrop-filter: blur(4px);
  }

  .stat-card,
  .index-card {
    padding: 0.85rem;
  }

  .stat-card p,
  .index-card p {
    margin: 0;
    color: var(--muted);
    font-size: 0.78rem;
  }

  .stat-card h3,
  .index-card h3 {
    margin-top: 0.34rem;
    font-size: 1.34rem;
  }

  .stat-card small,
  .index-card small {
    color: #9eb9c2;
    font-size: 0.72rem;
  }

  .cards-3col,
  .table-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    margin-top: 0.9rem;
  }

  .table-grid {
    grid-template-columns: 2fr 1fr;
  }

  .panel {
    padding: 0.95rem;
  }

  .panel h2 {
    margin-bottom: 0.75rem;
    font-size: 1.08rem;
  }

  .list-stack {
    display: grid;
    gap: 0.48rem;
  }

  .list-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 0.4rem;
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 11px;
    background: rgba(255, 255, 255, 0.02);
    padding: 0.45rem 0.55rem;
    font-size: 0.84rem;
  }

  .list-row strong {
    font-family: "Outfit", sans-serif;
  }

  .up {
    color: var(--up);
  }

  .down {
    color: var(--down);
  }

  .clean-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: grid;
    gap: 0.58rem;
  }

  .clean-list li {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px dashed var(--line);
    padding-bottom: 0.42rem;
    font-size: 0.86rem;
  }

  .clean-list span {
    color: #a7c2cb;
  }

  .risk-grid {
    grid-template-columns: repeat(5, minmax(0, 1fr));
  }

  .risk-card {
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 0.65rem;
    background: rgba(255, 255, 255, 0.02);
  }

  .risk-card p {
    margin: 0;
    color: #bdd3da;
    font-size: 0.77rem;
  }

  .risk-card h4 {
    margin: 0.36rem 0 0.2rem;
    font-size: 1.1rem;
    font-family: "Outfit", sans-serif;
  }

  .table-wrap {
    overflow-x: auto;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    min-width: 520px;
  }

  th,
  td {
    text-align: left;
    padding: 0.56rem 0.42rem;
    border-bottom: 1px solid var(--line);
    font-size: 0.83rem;
    white-space: nowrap;
  }

  th {
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #98b5bf;
  }

  .api-note {
    margin-top: 0.9rem;
    background: linear-gradient(135deg, rgba(13, 34, 49, 0.75), rgba(8, 22, 30, 0.75));
  }

  .api-note p {
    margin: 0;
    color: #b8d0d8;
    font-size: 0.84rem;
  }

  .reveal {
    animation: rise 520ms ease both;
  }

  .delay-1 {
    animation-delay: 70ms;
  }

  .delay-2 {
    animation-delay: 120ms;
  }

  .delay-3 {
    animation-delay: 170ms;
  }

  @keyframes rise {
    from {
      transform: translateY(9px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }

  @media (max-width: 1040px) {
    .indices-grid,
    .summary-grid,
    .risk-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .cards-3col,
    .table-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 620px) {
    .outlook-shell {
      border-radius: 16px;
      padding: 0.85rem;
    }

    .indices-grid,
    .summary-grid,
    .risk-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<script>
{% raw %}
  (function () {
    const TRADINGVIEW_URL = "https://scanner.tradingview.com/india/scan";
    const REFRESH_MS = 60000;
    const FETCH_TIMEOUT_MS = 12000;
    const CHUNK_SIZE = 24;
    const TV_ENDPOINTS = [
      TRADINGVIEW_URL,
      `https://corsproxy.io/?${encodeURIComponent(TRADINGVIEW_URL)}`,
      `https://cors.isomorphic-git.org/${TRADINGVIEW_URL}`
    ];

    const INVEST_STOCKS = {
      HDFCBANK: 1333, TCS: 11536, RELIANCE: 2885, INFY: 1594, ICICIBANK: 4963, NESTLEIND: 17963,
      BHARTIARTL: 10604, ASIANPAINT: 236, ITC: 1660, SUNPHARMA: 3351, HCLTECH: 7229,
      "BAJAJ-AUTO": 16669, APOLLOHOSP: 157, DMART: 19913, SBIN: 3045, AXISBANK: 5900,
      NTPC: 11630, POWERGRID: 14977, COALINDIA: 20374, CIPLA: 694, ADANIPORTS: 15083,
      TRENT: 1964, VBL: 18921, BEL: 383, IRCTC: 13611, CAMS: 342, CDSL: 21174,
      CHOLAFIN: 685, LTF: 24948, ICICIPRULI: 18652, IDFCFIRSTB: 11184, ABCAPITAL: 21614,
      TATAMOTORS: 3456, TATASTEEL: 3499, TATAPOWER: 3426, DLF: 14732, GODREJPROP: 17875,
      ACC: 22, AMBUJACEM: 1270, APLAPOLLO: 25780, JIOFIN: 18143, BDL: 2144, IOC: 1624,
      NHPC: 17400, GMRINFRA: 13528, ASHOKLEY: 212, IDEA: 14366
    };

    const INVEST_STOCKS_RISK = {
      HDFCBANK: 1, TCS: 1, RELIANCE: 1, INFY: 1, ICICIBANK: 1, NESTLEIND: 1,
      BHARTIARTL: 2, ASIANPAINT: 2, ITC: 2, SUNPHARMA: 2, HCLTECH: 2, "BAJAJ-AUTO": 2,
      APOLLOHOSP: 2, DMART: 2, SBIN: 3, AXISBANK: 3, NTPC: 3, POWERGRID: 2, COALINDIA: 3,
      MARUTI: 3, CIPLA: 2, ADANIPORTS: 4, TRENT: 4, VBL: 3, BEL: 3, IRCTC: 3, CAMS: 2,
      CDSL: 3, COLPAL: 2, DIXON: 4, CHOLAFIN: 3, LTF: 4, ICICIPRULI: 3, FEDERALBNK: 3,
      IDFCFIRSTB: 4, ABCAPITAL: 4, TATAMOTORS: 4, TATASTEEL: 5, TATAPOWER: 4, DLF: 4,
      GODREJPROP: 4, ACC: 3, AMBUJACEM: 3, APLAPOLLO: 4, JIOFIN: 4, BDL: 3, IOC: 4,
      NHPC: 3, GMRINFRA: 5, INDUSTOWER: 4, ASHOKLEY: 4, NYKAA: 5, AUROPHARMA: 4,
      IDEA: 5, SUZLON: 5
    };

    const INDICES_DICT = {
      NIFTY: 260, BANKNIFTY: 260105, SENSEX: 265
    };

    const ETF_DICT = {
      ALPHA: 7412, EVINDIA: 24461, ITBEES: 19084, SML100CASE: 758955, MID150CASE: 24077,
      MODEFENCE: 24944, MOM30IETF: 10585, GOLDBEES: 14428, OILIETF: 24533, TOP20: 760415
    };

    const COLUMNS = [
      "name", "close", "change", "change_abs", "high", "low", "ADR", "ADRP", "ADX-DI",
      "ROC|1W", "ROC|1M", "SMA50", "SMA100", "High.3M", "High.6M", "Low.3M",
      "price_target_1y", "price_target_median", "RSI|1", "RSI|5", "BB.lower",
      "recommendation_buy", "recommendation_sell", "recommendation_total"
    ];

    const dom = {
      niftyCard: document.getElementById("niftyCard"),
      niftyChange: document.getElementById("niftyChange"),
      bankniftyCard: document.getElementById("bankniftyCard"),
      bankniftyChange: document.getElementById("bankniftyChange"),
      sensexCard: document.getElementById("sensexCard"),
      sensexChange: document.getElementById("sensexChange"),
      coverageCard: document.getElementById("coverageCard"),
      breadthCard: document.getElementById("breadthCard"),
      avgChangeCard: document.getElementById("avgChangeCard"),
      riskPulseCard: document.getElementById("riskPulseCard"),
      gainersList: document.getElementById("gainersList"),
      losersList: document.getElementById("losersList"),
      adxLeaders: document.getElementById("adxLeaders"),
      sma50Breadth: document.getElementById("sma50Breadth"),
      sma100Breadth: document.getElementById("sma100Breadth"),
      medianRsi: document.getElementById("medianRsi"),
      riskBuckets: document.getElementById("riskBuckets"),
      stocksTableBody: document.getElementById("stocksTableBody"),
      etfTableBody: document.getElementById("etfTableBody"),
      lastRefresh: document.getElementById("lastRefresh"),
      fetchStatus: document.getElementById("fetchStatus"),
      retryBtn: document.getElementById("retryBtn")
    };

    let activeEndpoint = TV_ENDPOINTS[0];
    let refreshTimer = null;

    function num(value, fallback) {
      const parsed = Number(value);
      return Number.isFinite(parsed) ? parsed : (fallback || 0);
    }

    function fmt(value, digits) {
      if (value === null || value === undefined || Number.isNaN(Number(value))) {
        return "--";
      }
      return Number(value).toLocaleString("en-IN", {
        minimumFractionDigits: digits || 0,
        maximumFractionDigits: digits || 0
      });
    }

    function pct(value) {
      if (value === null || value === undefined || Number.isNaN(Number(value))) {
        return "--";
      }
      const n = Number(value);
      return `${n >= 0 ? "+" : ""}${n.toFixed(2)}%`;
    }

    function parseRows(rawData) {
      const parsed = [];
      for (const row of rawData || []) {
        const values = row.d || [];
        const obj = { symbol: String(row.s || "").replace("NSE:", "") };
        COLUMNS.forEach((key, index) => {
          obj[key] = values[index];
        });
        parsed.push(obj);
      }
      return parsed;
    }

    function splitIntoChunks(list, size) {
      const chunks = [];
      for (let i = 0; i < list.length; i += size) {
        chunks.push(list.slice(i, i + size));
      }
      return chunks;
    }

    async function postScanner(endpoint, payload) {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);
      try {
        const response = await fetch(endpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
          cache: "no-store",
          signal: controller.signal
        });
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        return await response.json();
      } finally {
        clearTimeout(timeout);
      }
    }

    async function fetchMarketRows(symbols) {
      const payload = {
        symbols: {
          tickers: [],
          query: { types: [] }
        },
        columns: COLUMNS
      };

      const allRows = [];
      const chunks = splitIntoChunks(symbols, CHUNK_SIZE);
      let lastError = "Unknown error";

      for (const chunk of chunks) {
        payload.symbols.tickers = chunk.map((s) => `NSE:${s}`);
        let chunkLoaded = false;

        for (const endpoint of TV_ENDPOINTS) {
          try {
            const json = await postScanner(endpoint, payload);
            const parsed = parseRows(json.data);
            if (parsed.length) {
              activeEndpoint = endpoint;
              allRows.push(...parsed);
              chunkLoaded = true;
              break;
            }
            lastError = "Empty payload from scanner";
          } catch (error) {
            lastError = error && error.message ? error.message : String(error);
          }
        }

        if (!chunkLoaded) {
          throw new Error(`Scanner unavailable (${lastError})`);
        }
      }

      const dedupMap = new Map();
      allRows.forEach((row) => dedupMap.set(row.symbol, row));
      return [...dedupMap.values()];
    }

    function renderTopList(container, rows) {
      container.innerHTML = rows.map((item) => {
        const cls = num(item.change) >= 0 ? "up" : "down";
        return `
          <div class="list-row">
            <span>${item.symbol}</span>
            <strong class="${cls}">${pct(item.change)}</strong>
          </div>
        `;
      }).join("");
    }

    function renderRiskBuckets(rows) {
      const groups = { 1: [], 2: [], 3: [], 4: [], 5: [] };
      rows.forEach((row) => {
        const level = INVEST_STOCKS_RISK[row.symbol] || 3;
        if (!groups[level]) groups[level] = [];
        groups[level].push(row);
      });

      dom.riskBuckets.innerHTML = Object.keys(groups).map((key) => {
        const list = groups[key];
        const avg = list.length
          ? list.reduce((acc, r) => acc + num(r.change), 0) / list.length
          : 0;
        const cls = avg >= 0 ? "up" : "down";
        return `
          <article class="risk-card">
            <p>Risk ${key}</p>
            <h4 class="${cls}">${pct(avg)}</h4>
            <p>${list.length} symbols tracked</p>
          </article>
        `;
      }).join("");
    }

    function renderStockTable(rows) {
      const sorted = [...rows].sort((a, b) => num(b.change) - num(a.change));
      dom.stocksTableBody.innerHTML = sorted.map((r) => {
        const chgClass = num(r.change) >= 0 ? "up" : "down";
        const sma50Gap = r.SMA50 ? ((num(r.close) - num(r.SMA50)) / num(r.SMA50)) * 100 : null;
        return `
          <tr>
            <td>${r.symbol}</td>
            <td>${fmt(r.close, 2)}</td>
            <td class="${chgClass}">${pct(r.change)}</td>
            <td>${pct(r.ADRP)}</td>
            <td>${fmt(r["RSI|1"], 1)}</td>
            <td>${fmt(r["ADX-DI"], 1)}</td>
            <td class="${sma50Gap >= 0 ? "up" : "down"}">${pct(sma50Gap)}</td>
            <td>${INVEST_STOCKS_RISK[r.symbol] || 3}</td>
          </tr>
        `;
      }).join("");
    }

    function renderEtfTable(rows) {
      const sorted = [...rows].sort((a, b) => num(b["ROC|1W"]) - num(a["ROC|1W"]));
      dom.etfTableBody.innerHTML = sorted.map((r) => {
        return `
          <tr>
            <td>${r.symbol}</td>
            <td>${fmt(r.close, 2)}</td>
            <td class="${num(r.change) >= 0 ? "up" : "down"}">${pct(r.change)}</td>
            <td class="${num(r["ROC|1W"]) >= 0 ? "up" : "down"}">${pct(r["ROC|1W"])}</td>
            <td class="${num(r["ROC|1M"]) >= 0 ? "up" : "down"}">${pct(r["ROC|1M"])}</td>
            <td>${fmt(r["RSI|1"], 1)}</td>
          </tr>
        `;
      }).join("");
    }

    function renderIndices(indexRows) {
      indexRows.forEach(index => {
        const change = num(index.change);
        const changeClass = change >= 0 ? "up" : "down";
        const changeText = pct(index.change);
        
        switch(index.symbol) {
          case 'NIFTY':
            dom.niftyCard.textContent = fmt(index.close, 2);
            dom.niftyCard.className = changeClass;
            dom.niftyChange.textContent = changeText;
            dom.niftyChange.className = changeClass;
            break;
          case 'BANKNIFTY':
            dom.bankniftyCard.textContent = fmt(index.close, 2);
            dom.bankniftyCard.className = changeClass;
            dom.bankniftyChange.textContent = changeText;
            dom.bankniftyChange.className = changeClass;
            break;
          case 'SENSEX':
            dom.sensexCard.textContent = fmt(index.close, 2);
            dom.sensexCard.className = changeClass;
            dom.sensexChange.textContent = changeText;
            dom.sensexChange.className = changeClass;
            break;
        }
      });
    }

    function renderSummary(stockRows) {
      const total = Object.keys(INVEST_STOCKS).length;
      const got = stockRows.length;
      const adv = stockRows.filter((r) => num(r.change) > 0).length;
      const dec = stockRows.filter((r) => num(r.change) < 0).length;
      const avg = got ? stockRows.reduce((acc, r) => acc + num(r.change), 0) / got : 0;

      const riskAdjusted = got
        ? stockRows.reduce((acc, r) => {
            const risk = INVEST_STOCKS_RISK[r.symbol] || 3;
            return acc + (num(r.change) / risk);
          }, 0) / got
        : 0;

      dom.coverageCard.textContent = `${got} / ${total}`;
      dom.breadthCard.textContent = `${adv} / ${dec}`;
      dom.avgChangeCard.textContent = pct(avg);
      dom.avgChangeCard.className = avg >= 0 ? "up" : "down";
      dom.riskPulseCard.textContent = pct(riskAdjusted);
      dom.riskPulseCard.className = riskAdjusted >= 0 ? "up" : "down";

      const adxLeaders = [...stockRows]
        .sort((a, b) => num(b["ADX-DI"]) - num(a["ADX-DI"]))
        .slice(0, 3)
        .map((r) => r.symbol)
        .join(", ");

      const above50 = stockRows.filter((r) => num(r.close) > num(r.SMA50)).length;
      const above100 = stockRows.filter((r) => num(r.close) > num(r.SMA100)).length;

      const rsiSorted = stockRows
        .map((r) => num(r["RSI|1"], NaN))
        .filter((x) => Number.isFinite(x))
        .sort((a, b) => a - b);
      const median = rsiSorted.length
        ? (rsiSorted[Math.floor((rsiSorted.length - 1) / 2)] + rsiSorted[Math.ceil((rsiSorted.length - 1) / 2)]) / 2
        : null;

      dom.adxLeaders.textContent = adxLeaders || "--";
      dom.sma50Breadth.textContent = `${above50}/${got}`;
      dom.sma100Breadth.textContent = `${above100}/${got}`;
      dom.medianRsi.textContent = median !== null ? fmt(median, 1) : "--";
    }

    async function refreshAll() {
      dom.fetchStatus.textContent = "Status: Fetching live market scan...";
      try {
        const [indexRows, stockRows, etfRows] = await Promise.all([
          fetchMarketRows(Object.keys(INDICES_DICT)),
          fetchMarketRows(Object.keys(INVEST_STOCKS)),
          fetchMarketRows(Object.keys(ETF_DICT))
        ]);

        if (!stockRows.length && !etfRows.length && !indexRows.length) {
          throw new Error("No rows received from TradingView");
        }

        // Render indices first
        renderIndices(indexRows);

        const gainers = [...stockRows].sort((a, b) => num(b.change) - num(a.change)).slice(0, 8);
        const losers = [...stockRows].sort((a, b) => num(a.change) - num(b.change)).slice(0, 8);

        renderSummary(stockRows);
        renderTopList(dom.gainersList, gainers);
        renderTopList(dom.losersList, losers);
        renderRiskBuckets(stockRows);
        renderStockTable(stockRows);
        renderEtfTable(etfRows);

        const now = new Date();
        dom.lastRefresh.textContent = `Last refresh: ${now.toLocaleString("en-IN")}`;
        const endpointLabel = activeEndpoint === TRADINGVIEW_URL ? "direct" : "proxy";
        dom.fetchStatus.textContent = `Status: Live data streaming (${endpointLabel})`;
      } catch (error) {
        dom.fetchStatus.textContent = `Status: ${error.message}`;
      }
    }

    dom.retryBtn.addEventListener("click", refreshAll);
    
    // Auto-invoke refresh on page load
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", refreshAll);
    } else {
      // DOM is already ready, invoke immediately
      setTimeout(refreshAll, 100);
    }
    // Removed continuous refresh to prevent constant fetching
    // refreshTimer = setInterval(refreshAll, REFRESH_MS);
  })();
{% endraw %}
</script>
