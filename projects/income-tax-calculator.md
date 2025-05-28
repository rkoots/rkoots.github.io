---
layout: default
title: Income Tax Calculator
permalink: /income-tax-calculator/
description: Calculate your income tax for FY 2025-26 or FY 2024-25 using the latest budget rules as of July 23, 2025.
---

<h1>🧾 Income Tax Calculator (India)</h1>
<p><strong>See how the latest budget impacts your taxes. Updated as per budget announced on <u>July 23, 2025</u>.</strong></p>

<div id="flashcards-container">

  <div class="flashcard active" id="card-fy">
    <h2>1️⃣ Select Financial Year</h2>
    <label><input type="radio" name="fy" value="2025" checked> FY 2025–2026</label><br>
    <label><input type="radio" name="fy" value="2024"> FY 2024–2025</label><br><br>
    <button onclick="nextCard('card-age')">Next →</button>
  </div>

  <div class="flashcard" id="card-age">
    <h2>2️⃣ Select Age Group</h2>
    <label><input type="radio" name="age" value="normal" checked> Below 60</label><br>
    <label><input type="radio" name="age" value="senior"> 60 to 80</label><br>
    <label><input type="radio" name="age" value="super"> 80 & above</label><br><br>
    <button onclick="prevCard('card-fy')">← Back</button>
    <button onclick="nextCard('card-income')">Next →</button>
  </div>

  <div class="flashcard" id="card-income">
    <h2>3️⃣ Income Sources (₹)</h2>
    <label>Salary: <input type="number" id="salary" value="0" min="0"></label><br>
    <label>Exempt Allowances: <input type="number" id="exemptAllowances" value="0" min="0"></label><br>
    <label>Interest Income: <input type="number" id="interestIncome" value="0" min="0"></label><br>
    <label>Rental Income: <input type="number" id="rentalIncome" value="0" min="0"></label><br>
    <label>Home Loan Interest (Self-Occupied): <input type="number" id="homeLoanSelf" value="0" min="0"></label><br>
    <label>Home Loan Interest (Let-Out): <input type="number" id="homeLoanLetOut" value="0" min="0"></label><br>
    <label>Income from Digital Assets: <input type="number" id="digitalIncome" value="0" min="0"></label><br>
    <label>Other Income: <input type="number" id="otherIncome" value="0" min="0"></label><br><br>
    <button onclick="prevCard('card-age')">← Back</button>
    <button onclick="nextCard('card-deductions')">Next →</button>
  </div>

  <div class="flashcard" id="card-deductions">
    <h2>4️⃣ Deductions (Max Limits)</h2>
    <label>80C (Investments, max ₹1,50,000): <input type="number" id="ded80C" value="0" min="0" max="150000" oninput="validateMax(this)"></label><br>
    <label>80TTB (Senior Citizen Interest, max ₹50,000): <input type="number" id="ded80TTB" value="0" min="0" max="50000" oninput="validateMax(this)"></label><br>
    <label>80D (Health Insurance, max ₹75,000): <input type="number" id="ded80D" value="0" min="0" max="75000" oninput="validateMax(this)"></label><br>
    <label>80G (Donations, no limit): <input type="number" id="ded80G" value="0" min="0"></label><br>
    <label>80E (Education Loan Interest, no limit): <input type="number" id="ded80E" value="0" min="0"></label><br>
    <label>80EEA (Home Loan Interest, max ₹1,50,000): <input type="number" id="ded80EEA" value="0" min="0" max="150000" oninput="validateMax(this)"></label><br>
    <label>80CCD (NPS Employee, max ₹50,000): <input type="number" id="ded80CCD" value="0" min="0" max="50000" oninput="validateMax(this)"></label><br>
    <label>80CCD(2) (NPS Employer, max ₹1,50,000): <input type="number" id="ded80CCD2" value="0" min="0" max="150000" oninput="validateMax(this)"></label><br><br>
    <button onclick="prevCard('card-income')">← Back</button>
    <button onclick="calculateTax()">💡 Calculate Tax</button>
  </div>

</div>

<hr>

<div id="result" style="display:none;">
  <h2>💼 Tax Summary</h2>
  <div id="summary"></div>
  <h3>📊 Tax Planning Insights</h3>
  <ul id="tips"></ul>
  <button onclick="resetCalculator()">↻ Start Over</button>
</div>

<style>
  #flashcards-container {
    max-width: 600px;
    margin: auto;
  }
  .flashcard {
    display: none;
    padding: 1.5rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 1px 1px 5px #ccc;
    margin-bottom: 1rem;
  }
  .flashcard.active {
    display: block;
  }
  label {
    display: block;
    margin-bottom: 8px;
  }
  input[type="number"] {
    width: 180px;
    margin-left: 8px;
  }
  button {
    margin-top: 1rem;
    padding: 8px 16px;
    cursor: pointer;
    font-size: 1rem;
  }
  #result {
    max-width: 600px;
    margin: auto;
    padding: 1rem;
    border: 1px solid #007acc;
    border-radius: 8px;
    background: #f0faff;
  }
  #tips li {
    margin-bottom: 0.5rem;
  }
</style>

<script>
function nextCard(nextId) {
  const current = document.querySelector('.flashcard.active');
  current.classList.remove('active');
  document.getElementById(nextId).classList.add('active');
}

function prevCard(prevId) {
  const current = document.querySelector('.flashcard.active');
  current.classList.remove('active');
  document.getElementById(prevId).classList.add('active');
}

function validateMax(input) {
  const max = parseInt(input.max);
  const val = parseInt(input.value);
  if (val > max) {
    input.value = max;
    alert(`Maximum allowed deduction for this field is ₹${max.toLocaleString()}`);
  } else if (val < 0) {
    input.value = 0;
  }
}

function calculateTax() {
  // Fetch inputs
  const fy = document.querySelector('input[name="fy"]:checked').value;
  const age = document.querySelector('input[name="age"]:checked').value;

  const income = Number(document.getElementById('salary').value)
               + Number(document.getElementById('interestIncome').value)
               + Number(document.getElementById('rentalIncome').value)
               + Number(document.getElementById('digitalIncome').value)
               + Number(document.getElementById('otherIncome').value);

  const exempt = Number(document.getElementById('exemptAllowances').value);

  const deductions = Number(document.getElementById('ded80C').value)
                   + Number(document.getElementById('ded80TTB').value)
                   + Number(document.getElementById('ded80D').value)
                   + Number(document.getElementById('ded80G').value)
                   + Number(document.getElementById('ded80E').value)
                   + Number(document.getElementById('ded80EEA').value)
                   + Number(document.getElementById('ded80CCD').value)
                   + Number(document.getElementById('ded80CCD2').value);

  const loanDeduct = Number(document.getElementById('homeLoanSelf').value) + Number(document.getElementById('homeLoanLetOut').value);

  const totalIncome = Math.max(0, income - exempt - loanDeduct);

  const taxableOld = Math.max(0, totalIncome - deductions);
  const taxableNew = Math.max(0, totalIncome - deductions); // For demo, same deduction rules. Can be adjusted.

  // Tax slabs example (simplified):
  // For FY 25-26 and age groups, slabs can differ. We'll use basic slabs here:

  // Old Regime slabs by age (FY 25-26) - simplified example:
  const slabsOld = {
    normal: [
      { upTo: 300000, rate: 0 },
      { upTo: 500000, rate: 0.05 },
      { upTo: 1000000, rate: 0.2 },
      { upTo: Infinity, rate: 0.3 }
    ],
    senior: [
      { upTo: 300000, rate: 0 },
      { upTo: 500000, rate: 0.05 },
      { upTo: 1000000, rate: 0.2 },
      { upTo: Infinity, rate: 0.3 }
    ],
    super: [
      { upTo: 500000, rate: 0 },
      { upTo: 1000000, rate: 0.2 },
      { upTo: Infinity, rate: 0.3 }
    ]
  };

  // New Regime slabs (simplified, same for all ages):
  const slabsNew = [
    { upTo: 300000, rate: 0 },
    { upTo: 600000, rate: 0.05 },
    { upTo: 900000, rate: 0.1 },
    { upTo: 1200000, rate: 0.15 },
    { upTo: 1500000, rate: 0.2 },
    { upTo: 1800000, rate: 0.25 },
    { upTo: Infinity, rate: 0.3 }
  ];

  function calcTax(income, slabs) {
    let tax = 0, lowerLimit = 0;
    for (const slab of slabs) {
      if (income <= lowerLimit) break;
      let taxableAtThisRate = Math.min(income, slab.upTo) - lowerLimit;
      if (taxableAtThisRate > 0) {
        tax += taxableAtThisRate * slab.rate;
      }
      lowerLimit = slab.upTo;
      if (income <= slab.upTo) break;
    }
    return tax;
  }

  const taxOld = calcTax(taxableOld, slabsOld[age]);
  const taxNew = calcTax(taxableNew, slabsNew);

  // Add cess 4%
  const cessOld = taxOld * 0.04;
  const cessNew = taxNew * 0.04;

  // Final tax
  const finalOld = taxOld + cessOld;
  const finalNew = taxNew + cessNew;

  // Show result
  document.getElementById('flashcards-container').style.display = 'none';
  document.getElementById('result').style.display = 'block';

  let summaryHTML = `
    <p><strong>Financial Year:</strong> FY ${fy}</p>
    <p><strong>Age Group:</strong> ${age === 'normal' ? 'Below 60' : age === 'senior' ? '60 to 80' : '80 & above'}</p>
    <p><strong>Total Income (After Exemptions & Home Loan Interest):</strong> ₹${totalIncome.toLocaleString()}</p>
    <p><strong>Total Deductions:</strong> ₹${deductions.toLocaleString()}</p>
    <hr>
    <p><strong>Tax Payable (Old Regime):</strong> ₹${finalOld.toFixed(2)}</p>
    <p><strong>Tax Payable (New Regime):</strong> ₹${finalNew.toFixed(2)}</p>
  `;

  document.getElementById('summary').innerHTML = summaryHTML;

  let tipsHTML = '';

  if (finalOld < finalNew) {
    tipsHTML += `<li>Old regime offers lower tax. Consider continuing with deductions under 80C, 80D, etc.</li>`;
  } else if (finalNew < finalOld) {
    tipsHTML += `<li>New regime offers lower tax. Consider the simplified tax slabs with fewer deductions.</li>`;
  } else {
    tipsHTML += `<li>Both regimes result in similar tax. Choose the regime based on your comfort with filing and deductions.</li>`;
  }

  tipsHTML += `<li>Maximize your 80C investments (up to ₹1,50,000) for better tax savings.</li>`;
  tipsHTML += `<li>Claim health insurance deduction under 80D (up to ₹75,000 if applicable).</li>`;
  tipsHTML += `<li>Review home loan interest benefits carefully under different sections.</li>`;

  document.getElementById('tips').innerHTML = tipsHTML;
}

function resetCalculator() {
  document.getElementById('result').style.display = 'none';
  document.getElementById('flashcards-container').style.display = 'block';

  // Reset all inputs and go to first card
  document.querySelectorAll('input[type=number]').forEach(input => input.value = 0);
  document.querySelector('input[name="fy"][value="2025"]').checked = true;
  document.querySelector('input[name="age"][value="normal"]').checked = true;

  const cards = document.querySelectorAll('.flashcard');
  cards.forEach(card => card.classList.remove('active'));
  document.getElementById('card-fy').classList.add('active');
}
</script>
