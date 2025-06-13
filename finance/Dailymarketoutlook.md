---
layout: default
title: "Daily Market Outlook with financial news and trends"
categories: finance
permalink: /finance/market/
author: "Rajkumar V"
summary: "Daily Market Outlook with financial news, trends, and video analyses."
keywords: [Daily Market Outlook, Stock Market News, Nifty, Sensex, Market Forecast]
tags: [Daily Market Outlook, Nifty, Finance]
---

<link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<h2>Daily Market Outlook</h2>
<p>Date: {{ site.data.market.date }}</p>

<h4>Index Levels</h4>
<ul>
  <li>Nifty 50: {{ site.data.market.nifty.current }} ({{ site.data.market.nifty.change }}) — Support: {{ site.data.market.nifty.support }}, Resistance: {{ site.data.market.nifty.resistance }}</li>
  <li>Bank Nifty: {{ site.data.market.banknifty.current }} ({{ site.data.market.banknifty.change }}) — Support: {{ site.data.market.banknifty.support }}, Resistance: {{ site.data.market.banknifty.resistance }}</li>
</ul>

<h4>General Market Sentiment</h4>
<ul>
  <li>VIX: {{ site.data.market.vix }}</li>
  <li>FII Flow: {{ site.data.market.fii_flow }}</li>
  <li>DII Flow: {{ site.data.market.dii_flow }}</li>
</ul>

<h4>Top Gainers</h4>
<ul>
{% for gainer in site.data.market.gainers %}
  <li>{{ gainer.name }} ({{ gainer.change }}) — Sector: {{ gainer.sector }}</li>
{% endfor %}
</ul>

<h4>Top Losers</h4>
<ul>
{% for loser in site.data.market.losers %}
  <li>{{ loser.name }} ({{ loser.change }}) — Sector: {{ loser.sector }}</li>
{% endfor %}
</ul>

<h4>Momentum Stocks</h4>
<ul>
{% for momentum in site.data.market.momentum_stocks %}
  <li>{{ momentum.name }} — momentum: {{ momentum.momentum }}</li>
{% endfor %}
</ul>
