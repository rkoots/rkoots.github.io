---
layout: default
title: Finance Planning App
permalink: /finance-pannner/
description: Plan your investments, control spending, and visualize your financial future.
---
<section>
  <h1>Finance Planning App</h1>
  <p><em>Plan your investments, control spending, and visualize your financial future.</em></p>

  <form id="financeForm">
    <h3>Income Details</h3>
    <label>Monthly Salary:</label>
    <input type="number" id="incomeSalary" required><br>
    <label>Other Income:</label>
    <input type="number" id="otherIncome"><br>
    <h3>Expenses</h3>
    <label>Rent/Mortgage:</label>
    <input type="number" id="rent"><br>
    <label>Utilities & Bills:</label>
    <input type="number" id="bills"><br>
    <label>Groceries & Essentials:</label>
    <input type="number" id="groceries"><br>
    <label>Other Expenses:</label>
    <input type="number" id="otherExpenses"><br>
    <button type="submit">💡 Generate Plan</button>
  </form>

  <div id="results" style="margin-top:30px;">
    <h2>Suggested Financial Package</h2>
    <p id="summaryText"></p>
    <canvas id="wealthChart" width="400" height="200"></canvas>
  </div>
</section>

<!-- Include Chart.js -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
document.getElementById("financeForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const income = parseFloat(document.getElementById("incomeSalary").value) + 
                 parseFloat(document.getElementById("otherIncome").value || 0);

  const expenses = ['rent', 'bills', 'groceries', 'otherExpenses']
    .map(id => parseFloat(document.getElementById(id).value || 0))
    .reduce((a, b) => a + b, 0);

  const savings = income - expenses;
  const emergencyFund = Math.min(savings * 0.2, 50000);
  const investments = savings - emergencyFund;

  const equity = investments * 0.6;
  const debt = investments * 0.3;
  const gold = investments * 0.1;

  document.getElementById("summaryText").innerHTML = `
    Your monthly savings: ₹${savings.toFixed(2)} <br>
    Recommended Emergency Fund: ₹${emergencyFund.toFixed(2)} <br>
    Suggested Investment: ₹${investments.toFixed(2)}<br>
    <strong>Allocation:</strong> Equity: ₹${equity.toFixed(2)}, Debt: ₹${debt.toFixed(2)}, Gold: ₹${gold.toFixed(2)}
  `;

  const ctx = document.getElementById("wealthChart").getContext("2d");
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Equity', 'Debt', 'Gold'],
      datasets: [{
        label: 'Investment Split',
        data: [equity, debt, gold],
        backgroundColor: ['#36a2eb', '#ffcd56', '#ff6384']
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'bottom' },
        title: { display: true, text: 'Wealth Diversification' }
      }
    }
  });
});
</script>
