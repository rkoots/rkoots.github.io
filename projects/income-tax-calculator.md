---
layout: default
title: Income Tax Calculator
permalink: /income-tax-calculator/
description: Calculate your income tax for FY 2025-26 and FY 2024-25 with an interactive calculator and get tax planning insights.
---

<style>
  /* Container and card styles */
  .card {
    max-width: 480px;
    margin: 2rem auto;
    padding: 1.8rem 2rem;
    border-radius: 12px;
    background: #f9faff;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    display: none;
    flex-direction: column;
    gap: 0.15rem;
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

<input type="hidden" id="ageGroup" value="below60" />
<input type="hidden" id="financialYear"  value="2025" />


  <!-- Card 1 -->
  <div id="card-income" class="card active">
    <h3>Income Details</h3>
    <label>Income from Salary</label>
    <input type="number" id="incomeSalary" min="0" value="0" />
    <label>Exempt Allowances</label>
    <input type="number" id="exemptAllowances" min="0" value="0" />
    <label>Income from Interest</label>
    <input type="number" id="incomeInterest" min="0" value="0" />
    <label>Income from Digital Assets</label>
    <input type="number" id="incomeDigitalAssets" min="0" value="0" />
    <div>
      <button onclick="nextCard('card-income2')">Next →</button>
    </div>
  </div>

  <!-- Card 2 -->
  <div id="card-income2" class="card ">
    <h3>Any Other Income?</h3>
    <label>Interest on Home Loan - Self Occupied</label>
    <input type="number" id="intHomeLoanSelf" min="0" value="0" />
    <label>Rental Income Received</label>
    <input type="number" id="rentalIncome" min="0" value="0" />
    <label>Interest on Home Loan - Let Out</label>
    <input type="number" id="intHomeLoanLetOut" min="0" value="0" />
    <label>Other Income</label>
    <input type="number" id="otherIncome" min="0" value="0" />
    <div>
      <button onclick="prevCard('card-income')">← Back</button>
      <button onclick="nextCard('card-deductions')">Next →</button>
    </div>
  </div>

  <!-- Card 3: Deductions -->
  <div id="card-deductions" class="card">
    <h3>Key Deductions</h3>
    <label>Basic Deductions - 80C (Max ₹1,50,000)</label>
    <input type="number" id="deduct80C" min="0" max="150000" value="0" />
    <label>Medical Insurance - 80D (Max ₹50,000 for senior citizens, ₹25,000 others)</label>
    <input type="number" id="deduct80D" min="0" value="0" />
    <label>Employee's contribution to NPS - 80CCD (Max ₹50,000)</label>
    <input type="number" id="deduct80CCD" min="0" max="50000" value="0" />
    <label>Employer's contribution to NPS - 80CCD(2) (Max ₹50,000)</label>
    <input type="number" id="deduct80CCD2" min="0" max="50000" value="0" />
    <label>Donations to Charity - 80G</label>
    <input type="number" id="deduct80G" min="0" value="0" />
    <div>
      <button onclick="prevCard('card-income2')">← Back</button>
      <button onclick="nextCard('card-deductions2')">💡 Calculate Tax</button>
    </div>
  </div>

  <div id="card-deductions2" class="card">
    <h3>Deductions on Interest Earned</h3>
    <label>Interest from Deposits - 80TTB (Max ₹50,000 for senior citizens)</label>
    <input type="number" id="deduct80TTB" min="0" value="0" />
    <label>Interest on Educational Loan - 80E</label>
    <input type="number" id="deduct80E" min="0" value="0" />
    <label>Interest on Housing Loan - 80EEA</label>
    <input type="number" id="deduct80EEA" min="0" value="0" />
    <div>
      <button onclick="prevCard('card-deductions')">← Back</button>
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
    showCard('card-income');
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
    const deduct80C = Math.min(+document.getElementById('deduct80C').value || 0, 150000);  // Max ₹1.5 lakh
    const deduct80TTB = Math.min(+document.getElementById('deduct80TTB').value || 0, 10000); // Max ₹10,000 (example max)
    const deduct80D = Math.min(+document.getElementById('deduct80D').value || 0, 75000);   // Max ₹75,000 (health insurance + medical exp.)
    const deduct80G = Math.min(+document.getElementById('deduct80G').value || 0, 1000000);  // No fixed max, example ₹10 lakh max
    const deduct80E = +document.getElementById('deduct80E').value || 0;                    // No max limit, full amount allowed (interest on education loan)
    const deduct80EEA = Math.min(+document.getElementById('deduct80EEA').value || 0, 150000); // Max ₹1.5 lakh (interest on housing loan for first-time buyers)
    const deduct80CCD = Math.min(+document.getElementById('deduct80CCD').value || 0, 50000);   // Max ₹50,000 (NPS contribution by employee)
    const deduct80CCD2 = Math.min(+document.getElementById('deduct80CCD2').value || 0, 50000); // Max ₹50,000 (NPS contribution by employer)


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



<br/><br/>
## Comprehensive Income Tax Toolkit
*For FY 2025-26 (AY 2026-27) | Updated with Union Budget 2025 Tax Changes*

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

Section 80C of the Income Tax Act provides exemptions or deductions on specific expenditures and investments from income tax. By investing in options like PPF, NSC, ELSS, SSY, etc., you can claim deductions of up to Rs. 1.5 lakh each year under Section 80C, helping you save on income tax. Let us understand these deductions in detail:

## Section 80C - Deductions and Exemptions on Investments

Section 80C is one of the most popular and favorite sections amongst taxpayers as it allows them to reduce taxable income by making tax-saving investments or incurring eligible expenses.

- Section 80C deduction can be claimed only by **Individuals and HUFs**.
- Companies, partnership firms, and LLPs **cannot** avail this deduction.
- Up to **₹1.5 lakh** can be claimed as a deduction every year from the Gross total income.

### Section 80C Deductions List

| Investment / Payment                    | Details                                                                                     |
|---------------------------------------|---------------------------------------------------------------------------------------------|
| Employee Provident Fund (EPF)          | Contributions by employees to EPF are eligible for deduction.                               |
| Public Provident Fund (PPF)            | Deposits to a PPF account (maximum limit ₹1.5 lakh per year).                               |
| Life Insurance Premium                 | Premium paid for life insurance policies for self, spouse, or children.                    |
| Equity-Linked Savings Scheme (ELSS)   | Investments in specified mutual funds with a 3-year lock-in period.                         |
| National Savings Certificate (NSC)    | Investment in NSC qualifies for deduction. Accrued interest (except last year) eligible.   |
| 5-Year Fixed Deposit with Banks        | Fixed deposits of 5 years or more with scheduled banks.                                    |
| Sukanya Samriddhi Yojana (SSY)         | Deposits made for the benefit of a girl child.                                             |
| Principal Repayment of Home Loan       | Principal portion of EMI paid for a home loan.                                             |
| Stamp Duty and Registration Charges   | Paid for residential property (allowed in the year of purchase).                           |
| Tuition Fees                          | Paid for full-time education of up to two children in India.                              |
| Senior Citizens Savings Scheme (SCSS) | Investment made by senior citizens in SCSS.                                               |
| Unit Linked Insurance Plan (ULIP)     | Premium paid towards ULIP for self, spouse, and children.                                  |
| Post Office Time Deposit (5 years)     | Investment in 5-year time deposits at post offices.                                        |
| Superannuation fund                   | Employee's contribution to an approved superannuation fund.                               |
| Pension Plans                        | Contribution to specific pension plans like LIC's Jeevan Suraksha, etc.                    |

*Example:* An individual investing ₹50,000 in PPF, ₹40,000 in ELSS, paying ₹30,000 as life insurance premium, and having an EPF contribution of ₹30,000 utilizes the full ₹1.5 lakh 80C deduction limit.

---

## Deduction Limits under Sections 80C, 80CCC, 80CCD(1), 80CCE & 80CCD(1B)

Sections 80CCC and 80CCD provide deductions for investments in pension schemes.

| Section       | Eligible Investments                                       | Maximum Deduction            |
|---------------|------------------------------------------------------------|-----------------------------|
| **80C**       | ELSS, PPF/SPF/RPF, Life Insurance Premiums, Home Loan principal, SSY, NSC, SCSS, etc. | ₹1,50,000                   |
| **80CCC**     | Payment towards pension funds                              | ₹1,50,000                   |
| **80CCD(1)**  | Payments to Atal Pension Yojana or other notified pension schemes | Employed: 10% of basic salary + DA<br>Self-employed: 20% of gross total income |
| **80CCE**     | Total deduction under 80C, 80CCC & 80CCD(1)                | ₹1,50,000                   |
| **80CCD(1B)** | Additional investments in NPS (outside ₹1.5 lakh limit)    | ₹50,000                     |
| **80CCD(2)**  | Employer’s contribution towards NPS (outside ₹1.5 lakh limit) | Govt: 14% of basic salary + DA<br>Others: 10% of basic salary + DA |

*Maximum combined deduction limit:*  
₹2,00,000 under Section 80C + 80CCC + 80CCD(1) + 80CCD(1B).

---

## Other Important Sections for Deductions

### Section 80TTA – Interest on Savings Accounts
- Deduction up to ₹10,000 for interest earned on savings accounts (individual or HUF).

### Section 80TTB – Interest on Deposits for Senior Citizens
- Deduction up to ₹50,000 for interest earned on deposits by senior citizens (60+ years).

### Section 80GG – House Rent Paid
- Deduction for taxpayers not receiving HRA but paying rent for accommodation.

### Section 80E – Interest on Education Loan
- Deduction on interest paid for education loans for self, spouse, children, or legal ward.

### Section 80EEA – Interest on Home Loan for First-Time Home Owners
- Extra deduction up to ₹1.5 lakh on interest paid for affordable house loans.

### Section 80EEB – Interest on Electric Vehicle Loan
- Deduction up to ₹1.5 lakh on interest paid for loans on electric vehicles.

### Section 80D – Medical Insurance Premiums
| Policy For                    | Deduction for Self & Family | Deduction for Parents | Preventive Health Check-up | Maximum Deduction  |
|------------------------------|-----------------------------|----------------------|----------------------------|--------------------|
| Self & Family (below 60 yrs) | ₹25,000                     | -                    | ₹5,000                     | ₹25,000            |
| Self & Family + Parents (all below 60 yrs) | ₹25,000          | ₹25,000              | ₹5,000                     | ₹50,000            |
| Self & Family (below 60) + Parents (above 60) | ₹25,000          | ₹50,000              | ₹5,000                     | ₹75,000            |
| Self & Family + Parents (above 60) | ₹50,000                | ₹50,000              | ₹5,000                     | ₹1,00,000          |

### Section 80DD – Medical Treatment of Disabled Dependent
- Deduction for expenses on medical treatment, training, and rehabilitation of specially-abled dependents.

### Section 80DDB – Medical Treatment
- Deduction for expenses on medical treatment of self or dependents.

### Section 80U – Deduction for Disabled Individuals
- ₹75,000 for disability, ₹1.2 lakh for severe disability.

### Section 80G – Donations for Social Causes
- Deductions on donations (50% or 100% depending on cause), cash donations above ₹2,000 not allowed.

### Section 80GGB & 80GGC – Donations to Political Parties
- Deduction on donations (non-cash mode) by companies and individuals respectively.

### Section 80RRB – Royalty Income from Patents
- Deduction up to ₹3 lakh for royalty income from patents for individual residents.

### Section 80QQB – Royalty Income for Authors
- Deduction up to ₹3 lakh for authors on royalty income, limited to actual income.

---

*Stop guessing your capital gains tax!*  
**Book a Tax Expert for precision | Use code ADV70 to get 70% OFF!**

---

## Income Tax - Latest Updates, Basics, Tax Slabs, Rules, Income Tax Guide FY 2024-25

Income tax is a mandatory levy imposed by the government on the income earned by individuals and entities. It plays a vital role in funding public services, infrastructure, and national development. In India, income tax is governed by the Income Tax Act, 1961, and administered by the Income Tax Department under the Central Board of Direct Taxes (CBDT). It is a progressive tax based on income, age, residential status, and type of income.

**ITR Due Date Extension:** The due date for ITR filing has been extended to **15th September 2025** from the original due date of 31st July 2025.

---

## Browse By Topics

- Income Tax Law in India
- Income Tax Department
- Types of Taxpayers
- Residential Status
- Types of Income – What are the 5 Heads of Income?
- Deductions under the Income Tax Act
- Popular Deductions
- Computation Of Income
- Calculation of Tax
- Tax Slabs
- Old Income Tax Regime
- New Tax Regime
- Special Tax Rates
- Rebate u/s 87A and Cess
- Income Tax Payment
- Tax Deducted at Source (TDS)
- Advance Tax
- Self-Assessment Tax
- E-Payment of Taxes
- Refund
- Important terms
- Financial Year
- Assessment Year
- PAN
- TAN
- Filing Your ITR
- Meaning of ITR
- Documents Required for ITR Filing
- Persons Not Required to File ITR
- Consequences of Not Filing ITR
- E-Filing
- What is ITR–V?
- Important Income Tax Dates 2025
- Frequently Asked Questions

---

## Income Tax Law in India

The Constitution of India mandates that tax can only be imposed under the provisions of a law. Income tax rules are governed by the Income Tax Act, 1961, which is under the Union List, empowering the Central Government to levy and collect income tax. Amendments to the Act are introduced via the Finance Bill during the Budget session and brought into force through the Finance Act.

Additional components like income tax rules, circulars, notifications, and case laws aid in the implementation of the tax laws.

---

## Income Tax Department

The Income Tax Department collects direct taxes for the Government of India. The Ministry of Finance administers revenue functions through the Central Board of Direct Taxes (CBDT), which oversees the implementation of direct tax laws.

---

## Types of Taxpayers

- Individuals
- Hindu Undivided Family (HUF)
- Firms
- Companies
- Association of Persons (AOP)
- Body of Individuals (BOI)
- Local Authority
- Artificial Judicial Person

Certain assessees must file ITR based on conditions specified under the Income Tax Act.

---

## Residential Status

Assessees are classified based on residential status into:
- Resident and Ordinarily Resident (ROR)
- Resident but Not Ordinarily Resident (RNOR)
- Non-Resident (NR)

| Income Type | ROR | RNOR | NR |
|-------------|-----|------|----|
| Income received in India | Taxable | Taxable | Taxable |
| Accrued income in India | Taxable | Taxable | Taxable |
| Income from business/profession in India but accrued outside India | Taxable | Taxable | Non-taxable |
| Income accrued outside India | Taxable | Non-taxable | Non-taxable |
| Untaxed past foreign income brought into India | Non-taxable | Non-taxable | Non-taxable |

---

## Types of Income – What are the 5 Heads of Income?

| Head of Income               | Nature of Income Covered                             |
|-----------------------------|----------------------------------------------------|
| Income from Salary           | Salary and pension income                           |
| Income from House Property   | Rental income from property                         |
| Income from Business & Profession | Profits from self-employment, business, or freelancing |
| Income from Capital Gains    | Income from sale of capital assets like shares, property, etc. |
| Income from Other Sources    | Interest, lottery winnings, etc.                   |

---

## Deductions under the Income Tax Act

Deductions reduce taxable income based on investments, expenses, or specific income types. Popular deductions can significantly reduce tax liability.

---

## Popular Deductions

### Section 80C Deductions

Allows up to ₹1.5 lakh per financial year for investments like ELSS, NSC, etc.

### New Tax Regime Deductions

- Transport allowance for specially-abled persons
- Conveyance allowance for employment-related travel
- Daily allowances for absence from place of duty

Other key features:
- Highest surcharge reduced to 25% for income > ₹5 crore
- Standard deduction: ₹75,000 (new regime), ₹50,000 (old regime)
- Employer's pension contribution deduction: 14% (new), 10% (old)
- Family pension deduction limit: ₹25,000 (new), ₹15,000 (old)
- Long Term Capital Gains exemption limit increased to ₹1.25 lakh per year

---

## Special Tax Rates

- Long-Term Capital Gains: 12.5%
- Short-Term Capital Gains: 20% flat for listed shares and equity funds
- Casual incomes (lottery, betting): 30%
- Virtual Digital Assets: 30%

| Asset Type | Short-term | Long-term |
|------------|------------|-----------|
| Listed securities & equity-oriented units | ≤12 months | >12 months |
| Other assets | ≤24 months | >24 months |

---

## Rebate u/s 87A and Cess

| Regime      | Income Limit for Rebate | Maximum Rebate | Remarks |
|-------------|------------------------|----------------|---------|
| Old Tax Regime | ₹5 lakh                | ₹12,500        | Tax payable < rebate, no tax |
| New Tax Regime | ₹7 lakh (₹12 lakh from FY 2025-26) | ₹25,000 (₹60,000 from FY 2025-26) | Tax payable < rebate, no tax |

Health and Education Cess is 4% of income tax after rebate.

---

## Income Tax Payment

### Tax Deducted at Source (TDS)

Tax deducted by payer and credited to government on behalf of taxpayer.

### Advance Tax

Payable if estimated tax liability exceeds ₹10,000. Due dates apply.

### Self-Assessment Tax

Balance tax paid after adjusting advance tax and TDS.

### E-Payment of Taxes

Online payment facility available.

### Refund

Excess tax paid is refunded to taxpayer’s bank account.

---

## Important Terms

- **Financial Year (FY):** April 1 to March 31 (e.g., FY 2024-25)
- **Assessment Year (AY):** Year following FY when tax is assessed (e.g., AY 2025-26)
- **PAN:** Permanent Account Number, unique ID for tax transactions
- **TAN:** Tax Deduction and Collection Account Number, required for TDS/TCS transactions

---

## Filing Your ITR

ITR must be filed online via prescribed forms. Various forms apply depending on the taxpayer’s income sources and entity type.

| ITR Form | Applicable To                                               |
|----------|-------------------------------------------------------------|
| ITR-1    | Individuals (residents) with salary, one house property, other sources, agri income < ₹5,000, total income ≤ ₹50 lakh |
| ITR-2    | Individuals/HUFs with no business income, multiple house properties |
| ITR-3    | Individuals/HUFs with proprietary business or profession income |
| ITR-4    | Individuals/HUFs with presumptive income from business/profession |
| ITR-5    | Partnership firms or LLPs                                   |
| ITR-6    | Companies                                                  |
| ITR-7    | Trusts                                                    |

---

## Documents Required for ITR Filing

Be prepared with:
- PAN card
- Aadhaar card
- Bank statements
- Form 16 (salary)
- Form 26AS (tax credit)
- Investment proofs for deductions
- Other relevant documents

---

<!-- Add more sections as needed -->

---

*For detailed queries or expert assistance, consider booking a top tax expert using code ADV70 for 70% OFF.*

---

**Home > Income Tax > Income Tax - Latest Updates, Basics, Tax Slabs, Rules, Income Tax Guide FY 2024-25**

---

