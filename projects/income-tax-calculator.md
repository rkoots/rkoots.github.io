---
layout: default
title: Income Tax Calculator
permalink: /income-tax-calculator/
description: Calculate your income tax for FY 2025-26 and FY 2024-25 with an interactive calculator and get tax planning insights.
---

<style>
  /* Container and card styles */
  .card {
    max-width: 600px;
    margin: 2rem auto;
    padding: 1.8rem 2rem;
    border-radius: 12px;
    background: #f9faff;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    display: none;
    flex-direction: column;
    gap: 1rem;
  }
  .card.active {
    display: flex;
  }

  label {
    font-weight: 600;
    margin-bottom: 0.3rem;
    display: block;
  }
  input[type=number], select {
    width: 100%;
    padding: 0.6rem 1rem;
    font-size: 1rem;
    border-radius: 6px;
    border: 1.5px solid #ccc;
    transition: border-color 0.3s ease;
  }
  input[type=number]:focus, select:focus {
    border-color: #4a90e2;
    outline: none;
  }

  /* Modern button styling */
  button {
    background: linear-gradient(135deg, #4a90e2, #357ABD);
    border: none;
    border-radius: 30px;
    color: white;
    padding: 12px 28px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 6px 15px rgba(53, 122, 189, 0.4);
    transition: background 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
    user-select: none;
    align-self: flex-start;
    margin-top: 1rem;
  }
  button:hover {
    background: linear-gradient(135deg, #357ABD, #4a90e2);
    box-shadow: 0 8px 20px rgba(53, 122, 189, 0.6);
    transform: translateY(-3px);
  }
  button:active {
    background: linear-gradient(135deg, #2a5e9e, #2461a1);
    box-shadow: 0 4px 8px rgba(36, 97, 161, 0.7);
    transform: translateY(1px);
  }
  button:focus {
    outline: none;
    box-shadow: 0 0 0 4px rgba(53, 122, 189, 0.5);
  }

  /* Result styling */
  .result {
    background: #e6f0ff;
    border: 1px solid #4a90e2;
    padding: 1.2rem 1.6rem;
    border-radius: 8px;
    margin-top: 2rem;
    font-size: 1.2rem;
    color: #2c3e50;
  }

  .insights {
    margin-top: 1.5rem;
    font-size: 1rem;
    color: #34495e;
    background: #dff0d8;
    padding: 1rem 1.2rem;
    border-radius: 8px;
    border: 1px solid #3c763d;
  }
</style>

<section>
  <h1>Income Tax Calculator</h1>
  <p><em>See how the latest budget impacts your tax calculation. Updated as per latest budget on 23 July, 2025.</em></p>

  <!-- Card 1: Select Financial Year -->
  <div id="card-fy" class="card active">
    <label for="financialYear">Which Financial Year do you want to calculate taxes for?</label>
    <select id="financialYear">
      <option value="2025">FY 2025-2026 (Return: 1st Apr 2026 - 31st Mar 2027)</option>
      <option value="2024">FY 2024-2025 (Return: 1st Apr 2025 - 31st Mar 2026)</option>
    </select>
    <button onclick="nextCard('card-age')">Next →</button>
  </div>

  <!-- Card 2: Select Age -->
  <div id="card-age" class="card">
    <label for="ageGroup">Your age</label>
    <select id="ageGroup">
      <option value="below60">0 to 60</option>
      <option value="below80">60 to 80</option>
      <option value="above80">80 & above</option>
    </select>
    <div>
      <button onclick="prevCard('card-fy')">← Back</button>
      <button onclick="nextCard('card-income')">Next →</button>
    </div>
  </div>

  <!-- Card 3: Income Inputs -->
  <div id="card-income" class="card">
    <h3>Income Details</h3>
    <label>Income from Salary</label>
    <input type="number" id="incomeSalary" min="0" value="0" />

    <label>Exempt Allowances</label>
    <input type="number" id="exemptAllowances" min="0" value="0" />

    <label>Income from Interest</label>
    <input type="number" id="incomeInterest" min="0" value="0" />

    <label>Interest on Home Loan - Self Occupied</label>
    <input type="number" id="intHomeLoanSelf" min="0" value="0" />

    <label>Rental Income Received</label>
    <input type="number" id="rentalIncome" min="0" value="0" />

    <label>Interest on Home Loan - Let Out</label>
    <input type="number" id="intHomeLoanLetOut" min="0" value="0" />

    <label>Income from Digital Assets</label>
    <input type="number" id="incomeDigitalAssets" min="0" value="0" />

    <label>Other Income</label>
    <input type="number" id="otherIncome" min="0" value="0" />

    <div>
      <button onclick="prevCard('card-age')">← Back</button>
      <button onclick="nextCard('card-deductions')">Next →</button>
    </div>
  </div>

  <!-- Card 4: Deductions -->
  <div id="card-deductions" class="card">
    <h3>Deductions & Limits</h3>

    <label>Basic Deductions - 80C (Max ₹1,50,000)</label>
    <input type="number" id="deduct80C" min="0" max="150000" value="0" />

    <label>Interest from Deposits - 80TTB (Max ₹50,000 for senior citizens)</label>
    <input type="number" id="deduct80TTB" min="0" value="0" />

    <label>Medical Insurance - 80D (Max ₹50,000 for senior citizens, ₹25,000 others)</label>
    <input type="number" id="deduct80D" min="0" value="0" />

    <label>Donations to Charity - 80G</label>
    <input type="number" id="deduct80G" min="0" value="0" />

    <label>Interest on Educational Loan - 80E</label>
    <input type="number" id="deduct80E" min="0" value="0" />

    <label>Interest on Housing Loan - 80EEA</label>
    <input type="number" id="deduct80EEA" min="0" value="0" />

    <label>Employee's contribution to NPS - 80CCD (Max ₹50,000)</label>
    <input type="number" id="deduct80CCD" min="0" max="50000" value="0" />

    <label>Employer's contribution to NPS - 80CCD(2) (Max ₹50,000)</label>
    <input type="number" id="deduct80CCD2" min="0" max="50000" value="0" />

    <div>
      <button onclick="prevCard('card-income')">← Back</button>
      <button onclick="calculateTax()">💡 Calculate Tax</button>
    </div>
  </div>

  <!-- Result card -->
  <div id="card-result" class="card">
    <h2>Tax Calculation Result</h2>
    <div class="result" id="resultText"></div>
    <div class="insights" id="taxInsights"></div>
    <button onclick="resetCalculator()">↻ Start Over</button>
  </div>
</section>

<script>
  // Card navigation
  function showCard(id) {
    document.querySelectorAll('.card').forEach(c => c.classList.remove('active'));
    document.getElementById(id).classList.add('active');
  }
  function nextCard(id) { showCard(id); }
  function prevCard(id) { showCard(id); }

  function resetCalculator() {
    // Reset all inputs
    document.querySelectorAll('input[type=number]').forEach(i => i.value = 0);
    document.getElementById('financialYear').value = '2025';
    document.getElementById('ageGroup').value = 'below60';
    showCard('card-fy');
    document.getElementById('resultText').innerHTML = '';
    document.getElementById('taxInsights').innerHTML = '';
  }

  // Simple tax calculation logic (example)
  function calculateTax() {
    const fy = document.getElementById('financialYear').value;
    const age = document.getElementById('ageGroup').value;

    // Income inputs
    const salary = +document.getElementById('incomeSalary').value || 0;
    const exempt = +document.getElementById('exemptAllowances').value || 0;
    const interestIncome = +document.getElementById('incomeInterest').value || 0;
    const homeLoanSelf = +document.getElementById('intHomeLoanSelf').value || 0;
    const rental = +document.getElementById('rentalIncome').value || 0;
    const homeLoanLetOut = +document.getElementById('intHomeLoanLetOut').value || 0;
    const digitalAssets = +document.getElementById('incomeDigitalAssets').value || 0;
    const otherIncome = +document.getElementById('otherIncome').value || 0;

    // Deductions (apply max limits)
    const deduct80C = Math.min(+document.getElementById('deduct80C').value || 0, 150000);
    const deduct80TTB = +document.getElementById('deduct80TTB').value || 0;
    const deduct80D = +document.getElementById('deduct80D').value || 0;
    const deduct80G = +document.getElementById('deduct80G').value || 0;
    const deduct80E = +document.getElementById('deduct80E').value || 0;
    const deduct80EEA = +document.getElementById('deduct80EEA').value || 0;
    const deduct80CCD = Math.min(+document.getElementById('deduct80CCD').value || 0, 50000);
    const deduct80CCD2 = Math.min(+document.getElementById('deduct80CCD2').value || 0, 50000);

    // Total income calculation (simplified)
    let grossIncome = salary + interestIncome + rental + digitalAssets + otherIncome;
    grossIncome -= exempt;

    // Apply home loan interest deductions
    if (homeLoanSelf) grossIncome -= homeLoanSelf; // self occupied interest is deduction if applicable
    if (homeLoanLetOut) grossIncome -= homeLoanLetOut; // let out interest can be deducted

    // Total deductions sum
    const totalDeductions = deduct80C + deduct80TTB + deduct80D + deduct80G + deduct80E + deduct80EEA + deduct80CCD + deduct80CCD2;

    let taxableIncome = grossIncome - totalDeductions;
    taxableIncome = taxableIncome < 0 ? 0 : taxableIncome;

    // Tax slabs (simplified and illustrative, FY 2025-26 new regime slabs)
    // Real slabs will vary by FY and age, here is an example for new regime FY 2025-26
    const slabsNew = [
      {limit: 300000, rate: 0},
      {limit: 300000, rate: 0.05},
      {limit: 400000, rate: 0.1},
      {limit: 300000, rate: 0.15},
      {limit: 500000, rate: 0.2},
      {limit: Infinity, rate: 0.3},
    ];

    // Old regime slabs for <60 years (simplified)
    const slabsOld = [
      {limit: 250000, rate: 0},
      {limit: 250000, rate: 0.05},
      {limit: 500000, rate: 0.2},
      {limit: Infinity, rate: 0.3},
    ];

    // Calculate tax using slabs
    function computeTax(income, slabs) {
      let tax = 0;
      let remaining = income;
      for (let slab of slabs) {
        let slabAmount = Math.min(remaining, slab.limit);
        tax += slabAmount * slab.rate;
        remaining -= slabAmount;
        if (remaining <= 0) break;
      }
      return tax;
    }

    // Pick slabs based on FY and age (for demo, only FY 2025-26 uses new regime slabs)
    let taxOld = computeTax(taxableIncome, slabsOld);
    let taxNew = computeTax(taxableIncome, slabsNew);

    // Rebate for taxable income <= 5L (simplified)
    if (taxOld < 12500) taxOld = 0;
    if (taxNew < 12500) taxNew = 0;

    // Add cess (4%)
    taxOld = taxOld * 1.04;
    taxNew = taxNew * 1.04;

    // Round off
    taxOld = Math.round(taxOld);
    taxNew = Math.round(taxNew);

    let resultHtml = `<strong>Taxable Income:</strong> ₹${taxableIncome.toLocaleString()}<br>`;
    resultHtml += `<strong>Estimated Tax under Old Regime:</strong> ₹${taxOld.toLocaleString()}<br>`;
    resultHtml += `<strong>Estimated Tax under New Regime:</strong> ₹${taxNew.toLocaleString()}<br>`;

    // Provide a simple insight
    let insights = '';
    if (taxOld < taxNew) {
      insights = 'You save more tax under the <strong>Old Regime</strong>. Consider maximizing deductions.';
    } else if (taxNew < taxOld) {
      insights = 'You save more tax under the <strong>New Regime</strong>. This is better if you prefer fewer deductions.';
    } else {
      insights = 'Both regimes result in similar tax liability.';
    }
    if (taxableIncome < 250000) {
      insights += '<br><em>Note: Your income is below the basic exemption limit, no tax is payable.</em>';
    }

    document.getElementById('resultText').innerHTML = resultHtml;
    document.getElementById('taxInsights').innerHTML = insights;

    showCard('card-result');
  }
</script>
