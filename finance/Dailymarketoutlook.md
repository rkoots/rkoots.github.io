---
layout: default
title: "Daily Market Outlook - Nifty, Bank Nifty, Top Gainers, Losers, Market Sentiment and News"
categories: finance
permalink: /finance/market/
author: "Rajkumar V"
summary: "Daily Market Outlook with financial news, trends, Nifty, Bank Nifty, momentum stocks, and more."
keywords: [Daily Market Outlook, Nifty, Bank Nifty, Top Gainers, Top Losers, Market Sentiment, Finance News, Sector-wise Market Performance]
tags: [Daily Market Outlook, Nifty, Bank Nifty, Finance News, Market Sentiment, Sector-wise Performance, Top Gainers, Top Losers]
---

<link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

 <!-- Sidebar -->
<nav class="w3-sidebar w3-collapse w3-gray-light w3-animate-left" style="z-index:3;width:300px;" id="mySidebar"><br>
  <div class="w3-container w3-row">
      <span>Welcome, <strong>Trader</strong></span><br>
      <a href="#" class="w3-bar-item w3-button"><i class="fa fa-envelope fa-fw"></i></a>
      <a href="#" class="w3-bar-item w3-button"><i class="fa fa-user fa-fw"></i></a>
      <a href="#" class="w3-bar-item w3-button"><i class="fa fa-cog fa-fw"></i></a>
  </div>
  <hr>
  <div class="w3-container">
    <h5>AI Market Outlook</h5>
  </div>
  <div class="w3-bar-block">
    <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-arrow-up fa-fw w3-text-green"></i> Nifty</a>
    <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-arrow-up fa-fw w3-text-blue"></i> Bank Nifty</a>
    <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-arrow-up fa-fw w3-text-orange"></i> Top Gainers</a>
    <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-arrow-down fa-fw w3-text-red"></i> Top Losers</a>
    <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-newspaper-o fa-fw w3-text-blue-gray"></i> Market News</a>
    <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-cog fa-fw w3-text-gray-blue"></i> Market Indicators</a>
  </div>
</nav>

 <!-- Overlay -->
<div class="w3-overlay w3-hide-large w3-animate-opacity" onclick="w3_close()" style="cursor:pointer" id="myOverlay" title="Close side menu"></div>

 <!-- Main Content -->
<div class="w3-main" style="margin-left:300px;margin-top:43px">
  <header class="w3-container" style="padding-top:22px">
    <h5><b><i class="fa fa-dashboard fa-fw w3-text-blue-gray"></i>AI Market Outlook - {{site.data.market.date}}</b></h5>
  </header>
  <div class="w3-row-padding w3-margin-bottom">
    <div class="w3-quarter">
      <div class="w3-container {% if site.data.market.nifty.change > 0 %}w3-green{% else %}w3-red{% endif %} w3-padding-16">
        <div class="w3-left"><i class="fa {% if site.data.market.nifty.change > 0 %}fa-arrow-up{% else %}fa-arrow-down{% endif %} w3-xxxlarge w3-text-black-50"></i></div>
        <div class="w3-right">
          <h3>{{ site.data.market.nifty.value }}</h3><!-- Nifty 50 Index -->
        </div>
        <div class="w3-clear"></div>
        <h4>Nifty 50</h4>
      </div>
    </div>

    <div class="w3-quarter">
      <div class="w3-container {% if site.data.market.banknifty.change > 0 %}w3-green{% else %}w3-red{% endif %} w3-padding-16">
        <div class="w3-left"><i class="fa {% if site.data.market.banknifty.change > 0 %}fa-arrow-up{% else %}fa-arrow-down{% endif %} w3-xxxlarge w3-text-black-50"></i></div>
        <div class="w3-right">
          <h3>{{ site.data.market.banknifty.value }}</h3><!-- Bank Nifty Index -->
        </div>
        <div class="w3-clear"></div>
        <h4>Bank Nifty</h4>
      </div>
    </div>

    <div class="w3-quarter">
      <div class="w3-container w3-orange w3-padding-16">
        <div class="w3-left"><i class="fa fa-arrow-up w3-xxxlarge w3-text-black-50"></i></div>
        <div class="w3-right">
          <h3>{{ site.data.market.vix }}</h3><!-- Market Volatility Indicator -->
        </div>
        <div class="w3-clear"></div>
        <h4>VIX</h4>
      </div>
    </div>

    <div class="w3-quarter">
      <div class="w3-container {% if site.data.market.pcr > 1 %}w3-green{% else %}w3-red{% endif %} w3-padding-16">
        <div class="w3-left"><i class="fa {% if site.data.market.pcr > 0 %}fa-arrow-up{% else %}fa-arrow-down{% endif %} w3-xxxlarge w3-text-black-50"></i></div>
        <div class="w3-right">
          <h3>{{ site.data.market.pcr }}</h3><!-- Put Call Ratio -->
        </div>
        <div class="w3-clear"></div>
        <h4>PCR</h4>
      </div>
    </div>
  </div>

  <!-- Market News Section -->
  <div class="w3-panel">
    <h5>Key Market News</h5>
    <ul class="w3-ul w3-card-4 w3-gray-light">
      {% for news in site.data.market.news %}
      <li>{{ news }}</li>
      {% endfor %}
    </ul>
  </div>

  <div class="w3-panel">
    <h5>AI Outlook</h5>
    <p>{{ site.data.market.ai_outlook }}</p>
  </div>


  <!-- Top Gainers and Losers Section -->
  <div class="w3-row-padding">
    <div class="w3-half">
      <h5>Top Gainers</h5>
      <table class="w3-table w3-bordered w3-hoverable w3-gray-light">
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Company</th>
            <th>Change</th>
            <th>%</th>
          </tr>
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
    </div>

    <div class="w3-half">
      <h5>Top Losers</h5>
      <table class="w3-table w3-bordered w3-hoverable w3-gray-light">
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Company</th>
            <th>Change</th>
            <th>%</th>
          </tr>
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
    </div>
  </div>

  <!-- Market Indicators Section -->
  <div class="w3-panel">
    <h5>Key Market Indicators</h5>
    <div class="w3-row-padding">
      <div class="w3-quarter">
        <div class="w3-gray-light w3-padding-16">
          <h4>VIX</h4>
          <p>{{ site.data.market.obv }}</p>
        </div>
      </div>
      <div class="w3-quarter">
        <div class="w3-gray-light w3-padding-16">
          <h4>PCR</h4>
          <p>{{ site.data.market.Fibonacci_Retracement }}</p><!-- Put Call Ratio -->
        </div>
      </div>
      <div class="w3-quarter">
        <div class="w3-gray-light w3-padding-16">
          <h4>FII Net Flow</h4>
          <p>{{ site.data.market.fii_flow }}</p><!-- FII flow today -->
        </div>
      </div>
      <div class="w3-quarter">
        <div class="w3-gray-light w3-padding-16">
          <h4>DII Net Flow</h4>
          <p>{{ site.data.market.dii_flow }}</p><!-- DII flow today -->
        </div>
      </div>
    </div>
  </div>


</div><!-- End main -->

<script>
  // Get the Sidebar
  var mySidebar = document.getElementById("mySidebar");

  // Get the DIV with overlay effect
  var overlayBg = document.getElementById("myOverlay");

  // Toggle between showing and hiding the sidebar, and add overlay effect
  function w3_open() {
    if (mySidebar.style.display === 'block') {
      mySidebar.style.display = 'none';
      overlayBg.style.display = "none";
    } else {
      mySidebar.style.display = 'block';
      overlayBg.style.display = "block";
    }
  }

  // Close the sidebar with the close button
  function w3_close() {
    mySidebar.style.display = "none";
    overlayBg.style.display = "none";
  }
</script>
