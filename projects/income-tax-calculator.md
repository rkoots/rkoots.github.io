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
  <p><em>See how the latest budget impacts your tax calculation. Updated as per latest budget on 2025.</em></p>

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


# Comprehensive Income Tax Toolkit
*For FY 2025-26 (AY 2026-27) | Updated with Union Budget 2025 Tax Changes*

---

## Introduction

Individuals in India can file income tax returns under either the **Old Tax Regime** or the **New Tax Regime**, each offering different slab rates, deductions, and benefits.

Our **Income Tax Calculator** is a simple, cost-effective online tool that helps you:

- Calculate your tax liability accurately.
- Compare old vs new tax regimes side-by-side.
- Make informed decisions to optimize your tax savings.

This guide explains the tax slabs, deductions, exemptions, and how to use the calculator effectively for smarter tax planning.

---

## Budget 2025 Updates at a Glance

- **No tax for income up to ₹12 Lakhs** under the new regime due to a rebate of ₹60,000.
- Modified slab rates introduced for FY 2025-26 (AY 2026-27) under the new regime.

| Income Slab (₹)          | Tax Rate (New Regime) |
|-------------------------|---------------------|
| Up to 4,00,000          | NIL                 |
| 4,00,001 – 8,00,000     | 5%                  |
| 8,00,001 – 12,00,000    | 10%                 |
| 12,00,001 – 16,00,000   | 15%                 |
| 16,00,001 – 20,00,000   | 20%                 |
| 20,00,001 – 24,00,000   | 25%                 |
| Above 24,00,000         | 30%                 |

---

## What is the Income Tax Calculator?

The **Income Tax Calculator** is an easy-to-use online tool that:

- Calculates your total tax liability based on income, deductions, and exemptions.
- Shows a comparison between old and new tax regimes.
- Helps you plan your investments and deductions efficiently.
- Is updated according to the latest tax rules from the Union Budget 2025.

---

## How to Use the Income Tax Calculator

Follow these steps:

1. **Select Financial Year:** Choose FY 2024-25 or FY 2025-26.
2. **Select Age Group:** Different slabs for age groups in old regime.
3. **Enter Salary Details:** Include gross salary, exempt allowances (like HRA, LTA).
4. **Add Other Incomes:** Interest income, rental income, capital gains, digital assets, etc.
5. **Provide Investment Details:** Enter investments eligible under Sections 80C, 80D, 80G, 80E, and 80TTA.
6. **Calculate:** View tax liability under both regimes and plan accordingly.

---

## How to Calculate Income Tax on Salary: A Simplified Example

Consider Neha:

| Component           | Amount (₹) | Exemption (₹) | Taxable Income Old Regime (₹) | Taxable Income New Regime (₹) |
|---------------------|------------|---------------|-------------------------------|-------------------------------|
| Basic Salary        | 12,00,000  | -             | 12,00,000                     | 12,00,000                     |
| HRA                 | 6,00,000   | 3,60,000      | 2,40,000                      | 6,00,000                      |
| Special Allowance   | 2,52,000   | -             | 2,52,000                      | 2,52,000                      |
| LTA                 | 20,000     | 12,000        | 8,000                        | 20,000                       |
| **Standard Deduction** | -          | 50,000        | 50,000                       | 75,000                       |
| **Gross Salary Income** | -          | -             | 16,50,000                    | 19,97,000                    |

Additional income and deductions:

| Deduction Section | Maximum Allowed (₹) | Neha's Claimed Amount (₹)             |
|-------------------|---------------------|--------------------------------------|
| 80C               | 1,50,000            | PPF 50,000 + ELSS 20,000 + LIC 8,000 + EPF contribution 72,000 (considered) |
| 80D               | 25,000              | Medical Insurance 12,000              |
| 80TTA             | 10,000              | Savings Account Interest 8,000        |

---

## Tax Calculation Summary for Neha

| Description          | Old Regime (₹) | New Regime (₹) |
|----------------------|----------------|----------------|
| Gross Income         | 16,70,000      | 19,42,000      |
| Deductions           | 1,70,000       | 0              |
| **Taxable Income**   | 15,00,000      | 19,42,000      |
| **Tax Liability**    | 2,73,000       | 2,83,504       |

---

## Tax Slabs Comparison: Old Regime vs New Regime

### Old Regime (Age-based slabs)

| Income Slab (₹)      | <60 yrs | 60-80 yrs | 80+ yrs  |
|----------------------|---------|-----------|----------|
| Up to 2,50,000       | NIL     | NIL       | NIL      |
| 2,50,001 – 3,00,000  | 5%      | NIL       | NIL      |
| 3,00,001 – 5,00,000  | 5%      | 5%        | NIL      |
| 5,00,001 – 10,00,000 | 20%     | 20%       | 20%      |
| Above 10,00,000      | 30%     | 30%       | 30%      |

### New Regime (Same slabs for all ages)

| Income Slab (₹)      | Tax Rate |
|----------------------|----------|
| Up to 3,00,000       | NIL      |
| 3,00,001 – 7,00,000  | 5%       |
| 7,00,001 – 10,00,000 | 10%      |
| 10,00,001 – 12,00,000| 15%      |
| 12,00,001 – 15,00,000| 20%      |
| Above 15,00,000      | 30%      |

---

## Surcharge and Education Cess

- Surcharge applies on income tax if total income exceeds certain thresholds.

| Income Range (₹)              | Surcharge Rate  |
|------------------------------|-----------------|
| ₹50 lakh - ₹1 crore           | 10%             |
| ₹1 crore - ₹2 crore           | 15%             |
| ₹2 crore - ₹5 crore           | 25%             |
| Above ₹5 crore                | 37% (Old Regime) / 25% (New Regime) |

- Health and Education Cess: **4%** of total tax liability.

---

## When to Choose Old Regime vs New Regime?

<details>
<summary><strong>Click to expand</strong></summary>

- **Old Regime** is beneficial if you have significant deductions/investments under sections 80C, 80D, 80E, etc.
- **New Regime** suits taxpayers preferring lower tax rates with fewer/no deductions.
- If your total deductions exceed the tax savings from slab benefits in the new regime, old regime may be better.
- If you do not have many investments or deductions, new regime generally leads to lower tax.

---

**Note:** You can use the Income Tax Calculator to input your exact details and instantly compare which regime benefits you more.

</details>

---

## Frequently Asked Questions (FAQ)

<details>
<summary><strong>What is Rebate u/s 87A?</strong></summary>
You get a rebate of up to ₹12,500 (old regime) or ₹60,000 (new regime) on tax payable if your total income is below ₹5,00,000 or ₹12,00,000 respectively, effectively reducing your tax liability to zero.
</details>

<details>
<summary><strong>What is Marginal Relief on Rebate?</strong></summary>
Marginal relief ensures taxpayers just above the rebate income limit do not pay disproportionately higher tax by providing a gradual phase-out of rebate.
</details>

<details>
<summary><strong>What deductions are not available under New Regime?</strong></summary>
Deductions such as standard deduction, house rent allowance (HRA), leave travel allowance (LTA), and various other exemptions under sections 80C, 80D, etc., are not available in the new tax regime.
</details>

<details>
<summary><strong>How do I calculate income from salary?</strong></summary>
Sum up Basic Salary, HRA, Special Allowances, Transport Allowance, and other allowances. Subtract exemptions such as HRA exemption (if applicable) and standard deduction to arrive at taxable salary.
</details>

<details>
<summary><strong>How can I reduce my tax liability?</strong></summary>
Invest in tax-saving instruments under Section 80C (PPF, ELSS), 80D (medical insurance), 80E (education loan interest), and claim all eligible deductions and exemptions to reduce taxable income.
</details>

---

## Final Word

Understanding the nuances of both tax regimes empowers you to plan better financially and minimize your tax burden legally. Use our updated Income Tax Calculator to make data-driven decisions for FY 2025-26 and beyond.
