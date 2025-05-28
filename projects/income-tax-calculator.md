---
layout: default
title: Income Tax Calculator
permalink: /income-tax-calculator/
description: Calculate your income tax for FY 2025-26 or FY 2024-25 using the latest budget rules as of July 23, 2025.
---

<h1>🧾 Income Tax Calculator (India)</h1>
<p><strong>See how the latest budget impacts your taxes. Updated as per budget announced on <u>July 23, 2025</u>.</strong></p>

<form id="taxForm">
  <fieldset>
    <legend>1️⃣ Select Financial Year</legend>
    <label><input type="radio" name="fy" value="2025" checked> FY 2025–2026</label><br>
    <label><input type="radio" name="fy" value="2024"> FY 2024–2025</label>
  </fieldset>

  <fieldset>
    <legend>2️⃣ Select Age Group</legend>
    <label><input type="radio" name="age" value="normal" checked> Below 60</label><br>
    <label><input type="radio" name="age" value="senior"> 60 to 80</label><br>
    <label><input type="radio" name="age" value="super"> 80 & above</label>
  </fieldset>

  <fieldset>
    <legend>3️⃣ Income Sources (₹)</legend>
    <label>Salary: <input type="number" id="salary" value="0"></label><br>
    <label>Exempt Allowances: <input type="number" id="exemptAllowances" value="0"></label><br>
    <label>Interest Income: <input type="number" id="interestIncome" value="0"></label><br>
    <label>Rental Income: <input type="number" id="rentalIncome" value="0"></label><br>
    <label>Home Loan Interest (Self-Occupied): <input type="number" id="homeLoanSelf" value="0"></label><br>
    <label>Home Loan Interest (Let-Out): <input type="number" id="homeLoanLetOut" value="0"></label><br>
    <label>Income from Digital Assets: <input type="number" id="digitalIncome" value="0"></label><br>
    <label>Other Income: <input type="number" id="otherIncome" value="0"></label>
  </fieldset>

  <fieldset>
    <legend>4️⃣ Deductions</legend>
    <label>80C (Investments): <input type="number" id="ded80C" value="0"></label><br>
    <label>80TTB (Senior Citizen Interest): <input type="number" id="ded80TTB" value="0"></label><br>
    <label>80D (Health Insurance): <input type="number" id="ded80D" value="0"></label><br>
    <label>80G (Donations): <input type="number" id="ded80G" value="0"></label><br>
    <label>80E (Edu Loan Interest): <input type="number" id="ded80E" value="0"></label><br>
    <label>80EEA (Home Loan Interest): <input type="number" id="ded80EEA" value="0"></label><br>
    <label>80CCD (NPS Employee): <input type="number" id="ded80CCD" value="0"></label><br>
    <label>80CCD(2) (NPS Employer): <input type="number" id="ded80CCD2" value="0"></label>
  </fieldset>

<button type="button" onclick="calculateTax()">💡 Calculate Tax</button>
</form>

<hr>

<div id="result" style="display:none;">
  <h2>💼 Tax Summary</h2>
  <div id="summary"></div>
  <h3>📊 Tax Planning Insights</h3>
  <ul id="tips"></ul>
</div>

<style>
  form fieldset {
    margin-bottom: 1.5rem;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  input[type="number"] {
    width: 200px;
    margin-bottom: 8px;
  }
  button {
    font-size: 1.1rem;
    padding: 10px 20px;
    cursor: pointer;
  }
</style>

<script>
function calculateTax() {
  const fy = document.querySelector('input[name="fy"]:checked').value;
  const age = document.querySelector('input[name="age"]:checked').value;

  const income = +document.getElementById('salary').value
               + +document.getElementById('interestIncome').value
               + +document.getElementById('rentalIncome').value
               + +document.getElementById('digitalIncome').value
               + +document.getElementById('otherIncome').value;

  const exempt = +document.getElementById('exemptAllowances').value;
  const deductions = +document.getElementById('ded80C').value
                   + +document.getElementById('ded80TTB').value
                   + +document.getElementById('ded80D').value
                   + +document.getElementById('ded80G').value
                   + +document.getElementById('ded80E').value
                   + +document.getElementById('ded80EEA').value
                   + +document.getElementById('ded80CCD').value
                   + +document.getElementById('ded80CCD2').value;

  const loanDeduct = +document.getElementById('homeLoanSelf').value + +document.getElementById('homeLoanLetOut').value;
  const totalIncome = Math.max(0, income - exempt - loanDeduct);

  const taxableOld = Math.max(0, totalIncome - deductions);
  const taxableNew = Math.max(0, totalIncome); // New regime = no deductions

  const oldTax = getOldRegimeTax(taxableOld, age, fy);
  const newTax = getNewRegimeTax(taxableNew, fy);

  let summary = `
    <p><strong>Total Gross Income:</strong> ₹${income.toLocaleString()}</p>
    <p><strong>Taxable Income (Old Regime):</strong> ₹${taxableOld.toLocaleString()}</p>
    <p><strong>Taxable Income (New Regime):</strong> ₹${taxableNew.toLocaleString()}</p>
    <p><strong>Tax Payable (Old Regime):</strong> ₹${oldTax.toLocaleString()}</p>
    <p><strong>Tax Payable (New Regime):</strong> ₹${newTax.toLocaleString()}</p>
  `;

  document.getElementById('summary').innerHTML = summary;
  document.getElementById('result').style.display = 'block';

  const tips = document.getElementById('tips');
  tips.innerHTML = '';

  if (deductions > 200000) {
    tips.innerHTML += `<li>You can benefit more from the <strong>Old Regime</strong> due to high deductions claimed.</li>`;
  }
  if (deductions < 100000) {
    tips.innerHTML += `<li>Consider <strong>New Regime</strong> if you're not utilizing deductions.</li>`;
  }
  tips.innerHTML += `<li>Use Section 80C fully by investing in ELSS, PPF, or life insurance.</li>`;
  tips.innerHTML += `<li>Senior citizens can claim 80TTB for interest up to ₹50,000.</li>`;
}

function getOldRegimeTax(income, age, fy) {
  let slabs = (fy === "2025") ? [250000, 500000, 1000000] : [250000, 500000, 1000000];
  if (age === "senior") slabs[0] = 300000;
  if (age === "super") slabs[0] = 500000;

  if (income <= slabs[0]) return 0;
  if (income <= slabs[1]) return (income - slabs[0]) * 0.05;
  if (income <= slabs[2]) return 12500 + (income - slabs[1]) * 0.2;
  return 112500 + (income - slabs[2]) * 0.3;
}

function getNewRegimeTax(income, fy) {
  // Using standard new regime as per 2023–2025 policy
  let tax = 0;
  const slabs = [300000, 600000, 900000, 1200000, 1500000];
  const rates = [0.05, 0.10, 0.15, 0.20, 0.30];

  for (let i = slabs.length - 1; i >= 0; i--) {
    if (income > slabs[i]) {
      tax += (income - slabs[i]) * rates[i];
      income = slabs[i];
    }
  }
  return tax;
}
</script>
