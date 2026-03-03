---
layout: default
title: "Daily Market Outlook - Nifty, Bank Nifty, Top Gainers, Losers, Market Sentiment and News"
categories: finance
permalink: /tools/market/
author: "Rajkumar V"
summary: "Daily Market Outlook with financial news, trends, Nifty, Bank Nifty, momentum stocks, and more."
keywords: [Daily Market Outlook, Nifty, Bank Nifty, Top Gainers, Top Losers, Market Sentiment, Finance News, Sector-wise Market Performance]
tags: [Daily Market Outlook, Nifty, Bank Nifty, Finance News, Market Sentiment, Sector-wise Performance, Top Gainers, Top Losers]
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">

<section class="market-shell">
  <div class="market-bg-glow market-bg-glow-a"></div>
  <div class="market-bg-glow market-bg-glow-b"></div>

  <header class="market-hero">
    <p class="eyebrow">TOOLS • MARKET INTELLIGENCE</p>
    <h1>Daily Market Outlook</h1>
    <p class="hero-subtitle">
      Multi-factor market read for India equities with sentiment, flows, breadth, momentum, and live macro/crypto pulse.
    </p>
    <div class="hero-meta">
      <span>Updated: {{ site.data.market.date | default: "Today" }}</span>
      <span>Data mode: Local + Public APIs</span>
    </div>
  </header>

  <section class="pulse-grid" id="pulse">
    <article class="metric-card {% if site.data.market.nifty.change > 0 %}is-up{% else %}is-down{% endif %}">
      <p>Nifty 50</p>
      <h2>{{ site.data.market.nifty.value }}</h2>
      <strong>{% if site.data.market.nifty.change > 0 %}▲{% else %}▼{% endif %} {{ site.data.market.nifty.change }}</strong>
    </article>

    <article class="metric-card {% if site.data.market.banknifty.change > 0 %}is-up{% else %}is-down{% endif %}">
      <p>Bank Nifty</p>
      <h2>{{ site.data.market.banknifty.value }}</h2>
      <strong>{% if site.data.market.banknifty.change > 0 %}▲{% else %}▼{% endif %} {{ site.data.market.banknifty.change }}</strong>
    </article>

    <article class="metric-card {% if site.data.market.vix < 16 %}is-up{% else %}is-neutral{% endif %}">
      <p>India VIX</p>
      <h2>{{ site.data.market.vix }}</h2>
      <strong>{% if site.data.market.vix < 16 %}Risk-on volatility{% else %}Heightened volatility{% endif %}</strong>
    </article>

    <article class="metric-card {% if site.data.market.pcr > 1 %}is-up{% else %}is-down{% endif %}">
      <p>Put/Call Ratio</p>
      <h2>{{ site.data.market.pcr }}</h2>
      <strong>{% if site.data.market.pcr > 1 %}Bullish options skew{% else %}Cautious options skew{% endif %}</strong>
    </article>
  </section>

  <section class="insight-grid">
    <article class="panel panel-wide fade-in">
      <h3>AI Market Narrative</h3>
      <p>{{ site.data.market.ai_outlook }}</p>
      <div class="tag-row">
        <span class="tag">Momentum</span>
        <span class="tag">Breadth</span>
        <span class="tag">Flows</span>
        <span class="tag">Volatility</span>
      </div>
    </article>

    <article class="panel fade-in delay-1">
      <h3>Institutional Flows</h3>
      <ul class="clean-list">
        <li><span>FII Net</span> <strong>{{ site.data.market.fii_flow }}</strong></li>
        <li><span>DII Net</span> <strong>{{ site.data.market.dii_flow }}</strong></li>
        <li><span>OBV Trend</span> <strong>{{ site.data.market.obv }}</strong></li>
        <li><span>Fib Zone</span> <strong>{{ site.data.market.Fibonacci_Retracement }}</strong></li>
      </ul>
    </article>

    <article class="panel fade-in delay-2">
      <h3>Action Radar</h3>
      <ul class="clean-list compact">
        <li>
          <span>Trend Bias</span>
          <strong>{% if site.data.market.nifty.change > 0 and site.data.market.banknifty.change > 0 %}Risk-On{% else %}Mixed{% endif %}</strong>
        </li>
        <li>
          <span>Volatility Regime</span>
          <strong>{% if site.data.market.vix < 16 %}Low{% elsif site.data.market.vix < 20 %}Moderate{% else %}High{% endif %}</strong>
        </li>
        <li>
          <span>Options Sentiment</span>
          <strong>{% if site.data.market.pcr > 1 %}Positive{% else %}Defensive{% endif %}</strong>
        </li>
      </ul>
    </article>
  </section>

  <section class="tables-grid">
    <article class="panel">
      <h3>Top Gainers</h3>
      <table>
        <thead>
          <tr><th>Ticker</th><th>Company</th><th>Change</th><th>%</th></tr>
        </thead>
        <tbody>
          {% for gainer in site.data.market.gainers %}
          <tr>
            <td>{{ gainer.symbol }}</td>
            <td>{{ gainer.name }}</td>
            <td>{{ gainer.change }}</td>
            <td>{{ gainer.percent }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </article>

    <article class="panel">
      <h3>Top Losers</h3>
      <table>
        <thead>
          <tr><th>Ticker</th><th>Company</th><th>Change</th><th>%</th></tr>
        </thead>
        <tbody>
          {% for loser in site.data.market.losers %}
          <tr>
            <td>{{ loser.symbol }}</td>
            <td>{{ loser.name }}</td>
            <td>{{ loser.change }}</td>
            <td>{{ loser.percent }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </article>
  </section>

  <section class="panel live-panel">
    <div class="live-header">
      <h3>Live Macro & Risk Dashboard</h3>
      <p>Public API widgets with fallback values. Auto-refresh every 5 minutes.</p>
    </div>

    <div class="live-grid" id="liveGrid">
      <article class="live-card">
        <p>BTC (USD)</p>
        <h4 id="btcUsd">Loading...</h4>
        <span id="btcChange">-</span>
      </article>

      <article class="live-card">
        <p>ETH (USD)</p>
        <h4 id="ethUsd">Loading...</h4>
        <span id="ethChange">-</span>
      </article>

      <article class="live-card">
        <p>USD/INR</p>
        <h4 id="usdInr">Loading...</h4>
        <span>Frankfurter FX feed</span>
      </article>

      <article class="live-card">
        <p>EUR/INR</p>
        <h4 id="eurInr">Loading...</h4>
        <span>Frankfurter FX feed</span>
      </article>
    </div>
  </section>

  <section class="panel news-panel">
    <h3>Key Market News</h3>
    <ul class="news-list">
      {% for news in site.data.market.news %}
      <li>{{ news }}</li>
      {% endfor %}
    </ul>
  </section>

  <section class="api-notes">
    <p>
      APIs used: <strong>CoinGecko</strong> (crypto risk proxy) and <strong>Frankfurter</strong> (FX macro pulse).
      You can extend this with Alpha Vantage, Finnhub, Twelve Data, Polygon, or FMP by adding your API key in a secure backend proxy.
    </p>
  </section>
</section>

<style>
  :root {
    --mk-bg: #0c1418;
    --mk-panel: #121f25;
    --mk-panel-soft: #17272f;
    --mk-text: #edf5f7;
    --mk-muted: #9ab0b7;
    --mk-line: rgba(255, 255, 255, 0.08);
    --mk-green: #2fd79c;
    --mk-red: #ff6e5b;
    --mk-amber: #f7bd4c;
  }

  .market-shell {
    position: relative;
    overflow: hidden;
    color: var(--mk-text);
    background: radial-gradient(circle at 0% 0%, #1a2f3a 0%, transparent 36%),
      radial-gradient(circle at 100% 8%, #222429 0%, transparent 38%),
      linear-gradient(160deg, #081116 0%, #0b161b 55%, #0f1f26 100%);
    border-radius: 24px;
    padding: clamp(1.2rem, 2.4vw, 2.2rem);
    margin: 1rem auto 2rem;
    max-width: 1120px;
    font-family: "IBM Plex Sans", sans-serif;
  }

  .market-bg-glow {
    position: absolute;
    border-radius: 999px;
    filter: blur(34px);
    opacity: 0.18;
    pointer-events: none;
  }

  .market-bg-glow-a {
    width: 260px;
    height: 260px;
    top: -60px;
    right: 8%;
    background: #2fd79c;
  }

  .market-bg-glow-b {
    width: 220px;
    height: 220px;
    bottom: -80px;
    left: 5%;
    background: #2ea6ff;
  }

  .market-hero h1,
  .panel h3,
  .metric-card h2 {
    font-family: "Space Grotesk", sans-serif;
    letter-spacing: 0.02em;
  }

  .market-hero {
    margin-bottom: 1.1rem;
    animation: rise 500ms ease;
  }

  .eyebrow {
    color: var(--mk-amber);
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    margin-bottom: 0.45rem;
  }

  .hero-subtitle {
    max-width: 78ch;
    color: var(--mk-muted);
  }

  .hero-meta {
    margin-top: 0.7rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
  }

  .hero-meta span {
    font-size: 0.85rem;
    border: 1px solid var(--mk-line);
    background: rgba(255, 255, 255, 0.03);
    border-radius: 999px;
    padding: 0.3rem 0.7rem;
    color: #d7e7ec;
  }

  .pulse-grid,
  .insight-grid,
  .tables-grid,
  .live-grid {
    display: grid;
    gap: 0.9rem;
  }

  .pulse-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }

  .metric-card {
    background: linear-gradient(150deg, rgba(255, 255, 255, 0.06), rgba(255, 255, 255, 0.01));
    border: 1px solid var(--mk-line);
    border-radius: 16px;
    padding: 0.95rem;
    backdrop-filter: blur(4px);
  }

  .metric-card p {
    margin: 0;
    color: var(--mk-muted);
    font-size: 0.86rem;
  }

  .metric-card h2 {
    margin: 0.3rem 0;
    font-size: 1.5rem;
  }

  .metric-card strong {
    font-size: 0.83rem;
  }

  .is-up strong {
    color: var(--mk-green);
  }

  .is-down strong {
    color: var(--mk-red);
  }

  .is-neutral strong {
    color: var(--mk-amber);
  }

  .insight-grid {
    grid-template-columns: 1.5fr 1fr 1fr;
    margin-top: 1rem;
  }

  .panel {
    background: var(--mk-panel);
    border: 1px solid var(--mk-line);
    border-radius: 16px;
    padding: 1rem;
  }

  .panel-wide {
    background: linear-gradient(145deg, #15252d, #101a1f 70%);
  }

  .panel h3 {
    margin-top: 0;
    margin-bottom: 0.8rem;
    font-size: 1.1rem;
  }

  .tag-row {
    margin-top: 0.8rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
  }

  .tag {
    background: rgba(47, 215, 156, 0.12);
    color: #88efca;
    border: 1px solid rgba(47, 215, 156, 0.35);
    border-radius: 999px;
    font-size: 0.75rem;
    padding: 0.24rem 0.62rem;
  }

  .clean-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    gap: 0.55rem;
  }

  .clean-list li {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.7rem;
    border-bottom: 1px dashed var(--mk-line);
    padding-bottom: 0.48rem;
    color: #d8e8ec;
  }

  .clean-list.compact li {
    font-size: 0.92rem;
  }

  .tables-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    margin-top: 1rem;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    overflow: hidden;
    border-radius: 12px;
  }

  th,
  td {
    text-align: left;
    padding: 0.62rem 0.5rem;
    border-bottom: 1px solid var(--mk-line);
    font-size: 0.9rem;
  }

  th {
    font-size: 0.76rem;
    text-transform: uppercase;
    color: #94adb5;
    letter-spacing: 0.06em;
  }

  .live-panel {
    margin-top: 1rem;
    background: linear-gradient(140deg, #14212a, #101b22 60%);
  }

  .live-header p {
    margin-top: -0.2rem;
    color: var(--mk-muted);
    font-size: 0.92rem;
  }

  .live-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    margin-top: 0.85rem;
  }

  .live-card {
    background: var(--mk-panel-soft);
    border: 1px solid var(--mk-line);
    border-radius: 12px;
    padding: 0.8rem;
  }

  .live-card p {
    margin: 0;
    color: var(--mk-muted);
    font-size: 0.8rem;
  }

  .live-card h4 {
    margin: 0.38rem 0;
    font-size: 1.1rem;
    font-family: "Space Grotesk", sans-serif;
  }

  .live-card span {
    color: #b9ccd1;
    font-size: 0.78rem;
  }

  .news-panel {
    margin-top: 1rem;
  }

  .news-list {
    margin: 0;
    padding-left: 1rem;
    color: #dcebee;
    display: grid;
    gap: 0.5rem;
  }

  .api-notes {
    margin-top: 0.9rem;
    color: #99afb6;
    font-size: 0.86rem;
  }

  .fade-in {
    animation: rise 500ms ease;
  }

  .delay-1 {
    animation-delay: 80ms;
  }

  .delay-2 {
    animation-delay: 150ms;
  }

  @keyframes rise {
    from {
      transform: translateY(10px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }

  @media (max-width: 980px) {
    .pulse-grid,
    .live-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .insight-grid,
    .tables-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 560px) {
    .market-shell {
      border-radius: 16px;
      padding: 1rem;
    }

    .pulse-grid,
    .live-grid {
      grid-template-columns: 1fr;
    }

    .market-hero h1 {
      font-size: 1.55rem;
    }
  }
</style>

<script>
  (function () {
    const ids = {
      btcUsd: document.getElementById("btcUsd"),
      ethUsd: document.getElementById("ethUsd"),
      btcChange: document.getElementById("btcChange"),
      ethChange: document.getElementById("ethChange"),
      usdInr: document.getElementById("usdInr"),
      eurInr: document.getElementById("eurInr")
    };

    function fmtCurrency(value) {
      if (value === null || value === undefined || Number.isNaN(value)) {
        return "N/A";
      }
      return Number(value).toLocaleString("en-IN", { maximumFractionDigits: 2 });
    }

    function fmtPct(value) {
      if (value === null || value === undefined || Number.isNaN(value)) {
        return "N/A";
      }
      const num = Number(value);
      const sign = num >= 0 ? "+" : "";
      return sign + num.toFixed(2) + "% (24h)";
    }

    async function loadCoinGecko() {
      const endpoint =
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true";

      const response = await fetch(endpoint, { cache: "no-store" });
      if (!response.ok) {
        throw new Error("CoinGecko unavailable");
      }

      const data = await response.json();
      const btc = data.bitcoin || {};
      const eth = data.ethereum || {};

      ids.btcUsd.textContent = "$" + fmtCurrency(btc.usd);
      ids.ethUsd.textContent = "$" + fmtCurrency(eth.usd);
      ids.btcChange.textContent = fmtPct(btc.usd_24h_change);
      ids.ethChange.textContent = fmtPct(eth.usd_24h_change);
      ids.btcChange.style.color = Number(btc.usd_24h_change) >= 0 ? "#2fd79c" : "#ff6e5b";
      ids.ethChange.style.color = Number(eth.usd_24h_change) >= 0 ? "#2fd79c" : "#ff6e5b";
    }

    async function loadFrankfurter() {
      const response = await fetch("https://api.frankfurter.app/latest?from=USD&to=INR,EUR", { cache: "no-store" });
      if (!response.ok) {
        throw new Error("Frankfurter unavailable");
      }

      const data = await response.json();
      const usdInr = data.rates && data.rates.INR ? data.rates.INR : null;
      const usdEur = data.rates && data.rates.EUR ? data.rates.EUR : null;
      const eurInr = usdInr && usdEur ? usdInr / usdEur : null;

      ids.usdInr.textContent = usdInr ? fmtCurrency(usdInr) : "N/A";
      ids.eurInr.textContent = eurInr ? fmtCurrency(eurInr) : "N/A";
    }

    function setFallback() {
      if (ids.btcUsd.textContent === "Loading...") {
        ids.btcUsd.textContent = "API delayed";
      }
      if (ids.ethUsd.textContent === "Loading...") {
        ids.ethUsd.textContent = "API delayed";
      }
      if (ids.usdInr.textContent === "Loading...") {
        ids.usdInr.textContent = "API delayed";
      }
      if (ids.eurInr.textContent === "Loading...") {
        ids.eurInr.textContent = "API delayed";
      }
    }

    async function refreshLiveWidgets() {
      await Promise.allSettled([loadCoinGecko(), loadFrankfurter()]);
      setFallback();
    }

    refreshLiveWidgets();
    setInterval(refreshLiveWidgets, 300000);
  })();
</script>
