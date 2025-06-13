---
layout: default
title: "Daily Market Outlook"
categories: finance
---

<h5>✅ Market Dashboard</h5>

<ul class="w3-ul w3-gray-light">
  <li>Nifty: {{ site.data.market.nifty.value }} ({{ site.data.market.nifty.change }})</li>
  <li>Bank Nifty: {{ site.data.market.bank_nifty.value }} ({{ site.data.market.bank_nifty.change }})</li>
  <li>Sentiment: {{ site.data.market.market_sentiment.value }}</li>
  <li>Volatility: {{ site.data.market.volatility.value }}</li>
</ul>

<h5>✅ Market News</h5>
<ul class="w3-ul w3-gray-light">
{% for item in site.data.market.market_news %}
  <li>{{ item }}</li>
{% endfor %}
</ul>

<h5>✅ Top Gainers</h5>
<table class="w3-table w3-gray-light">
  <thead>
    <tr>
      <th>Ticker</th>
      <th>Company</th>
      <th>Change</th>
      <th>Sector</th>
    </tr>
  </thead>
  <tbody>
  {% for gainer in site.data.market.top_gainers %}
    <tr>
      <td>{{ gainer.ticker }}</td>
      <td>{{ gainer.company }}</td>
      <td>{{ gainer.change }}</td>
      <td>{{ gainer.sector }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

<h5>✅ Top Losers</h5>
<table class="w3-table w3-gray-light">
  <thead>
    <tr>
      <th>Ticker</th>
      <th>Company</th>
      <th>Change</th>
      <th>Sector</th>
    </tr>
  </thead>
  <tbody>
  {% for loser in site.data.market.top_losers %}
    <tr>
      <td>{{ loser.ticker }}</td>
      <td>{{ loser.company }}</td>
      <td>{{ loser.change }}</td>
      <td>{{ loser.sector }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

<h5>✅ Momentum/Sector-wise movers</h5>
<ul class="w3-ul w3-gray-light">
{% for momentum in site.data.market.momentum_stocks %}
  <li>{{ momentum.momentum | capitalize }}: {{ momentum.stocks | join: ", " }}</li>
{% endfor %}
</ul>

<h5>✅ Technical Indicators</h5>
<ul class="w3-ul w3-gray-light">
{% for indicator in site.data.market.technical_indicators %}
  <li>{{ indicator }}</li>
{% endfor %}
</ul>

<h5>✅ Derivative Market Insights (Option Chain)</h5>
<ul class="w3-ul w3-gray-light">
{% for item in site.data.market.derivative_data %}
  <li>{{ item }}</li>
{% endfor %}
</ul>

<h5>✅ Institutional Activity</h5>
<ul class="w3-ul w3-gray-light">
{% for activity in site.data.market.institutional_activity %}
  <li>{{ activity }}</li>
{% endfor %}
</ul>

<h5>✅ Additional Notes or Comments</h5>
<ul class="w3-ul w3-gray-light">
{% for note in site.data.market.additional_notes %}
  <li>{{ note }}</li>
{% endfor %}
</ul>
