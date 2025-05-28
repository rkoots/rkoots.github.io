---
layout: default
title: Income Tax Calculator FY 2025-26
permalink: /income-tax-calculator/
description: See how the latest 2025 budget impacts your income tax. Calculate taxes under both old and new regimes with age-wise slabs, deductions, and digital asset income support.
---

<h1>💰 Income Tax Calculator – FY 2025-2026</h1>
<p>See how the <strong>latest budget (23 July 2025)</strong> affects your taxes. Compare old vs new regime. Plan smart. File on time.</p>

<form id="tax-form">
    <fieldset>
        <legend><strong>Choose Financial Year:</strong></legend>
        <label><input type="radio" name="fy" value="2025" checked> FY 2025-2026</label><br>
        <label><input type="radio" name="fy" value="2024"> FY 2024-2025</label>
    </fieldset>

    <fieldset>
        <legend><strong>Your Age:</strong></legend>
        <label><input type="radio" name="age" value="normal" checked> 0 to 60</label><br>
        <label><input type="radio" name="age" value="senior"> 60 to 80</label><br>
        <label><input type="radio" name="age" value="super"> 80+</label>
    </fieldset>

    <fieldset>
        <legend><strong>Income Sources:</strong></legend>
        <label>Salary: ₹<input type="number" name="salary" value="0"></label><br>
        <label>Exempt Allowances: ₹<input type="number" name="exempt" value="0"></label><br>
        <label>Interest Income: ₹<input type="number" name="interest" value="0"></label><br>
        <label>Home Loan Interest (Self-occupied): ₹<input type="number" name="home_self" value="0"></label><br>
        <label>Rental Income: ₹<input type="number" name="rental" value="0"></label><br>
        <label>Home Loan Interest (Let Out): ₹<input type="number" name="home_let" value="0"></label><br>
        <label>Crypto/Digital Assets Income: ₹<input type="number" name="digital" value="0"></label><br>
        <label>Other Income: ₹<input type="number" name="other" value="0"></label>
    </fieldset>

    <fieldset>
        <legend><strong>Deductions:</strong></legend>
        <label>Section 80C: ₹<input type="number" name="ded_80c" value="0"></label><br>
        <label>Section 80TTB: ₹<input type="number" name="ded_80ttb" value="0"></label><br>
        <label>Section 80D (Insurance): ₹<input type="number" name="ded_80d" value="0"></label><br>
        <label>Section 80G (Charity): ₹<input type="number" name="ded_80g" value="0"></label><br>
        <label>Section 80E (Edu Loan): ₹<input type="number" name="ded_80e" value="0"></label><br>
        <label>Section 80EEA (Housing): ₹<input type="number" name="ded_80eea" value="0"></label><br>
        <label>Section 80CCD (NPS Employee): ₹<input type="number" name="ded_80ccd" value="0"></label><br>
        <label>Section 80CCD(2) (NPS Employer): ₹<input type="number" name="ded_80ccd2" value="0"></label>
    </fieldset>

    <br>
    <button type="button" onclick="calculateTax()">Calculate Tax</button>
</form>

<h2>🧾 Tax Summary</h2>
<div id="result"></div>

<h2>📊 Tax Planning Tips</h2>
<ul>
    <li>Invest in ELSS, PPF, LIC, or Tax-Saving FDs to maximize <strong>Section 80C</strong> limit.</li>
    <li>Use <strong>80D</strong> for health insurance premium deductions (₹25k–₹75k based on age).</li>
    <li>Senior citizens should leverage <strong>80TTB</strong> for interest income (up to ₹50,000).</li>
    <li>High-income professionals may benefit more under <strong>New Regime</strong> if they claim fewer deductions.</li>
    <li>Renting? Consider <strong>HRA Exemption</strong> under the Old Regime if eligible.</li>
</ul>

<script>
    function calculateTax() {
      const form = document.getElementById("tax-form");
      const values = Object.fromEntries(new FormData(form).entries());
      const age = values.age;
      const fy = values.fy;

      const salary = +values.salary;
      const exempt = +values.exempt;
      const interest = +values.interest;
      const home_self = +values.home_self;
      const rental = +values.rental;
      const home_let = +values.home_let;
      const digital = +values.digital;
      const other = +values.other;

      const income = salary - exempt + interest + rental + digital + other - home_self - home_let;
      const deductions = Math.min(+values.ded_80c, 150000)
                       + +values.ded_80ttb
                       + +values.ded_80d
                       + +values.ded_80g
                       + +values.ded_80e
                       + +values.ded_80eea
                       + +values.ded_80ccd
                       + +values.ded_80ccd2;

      const old_taxable = Math.max(0, income - deductions);
      const new_taxable = Math.max(0, income);

      const old_tax = calculateOldTax(old_taxable, age);
      const new_tax = calculateNewTax(new_taxable);

      document.getElementById("result").innerHTML = `
        <p><strong>Old Regime Taxable Income:</strong> ₹${old_taxable.toLocaleString()}</p>
        <p><strong>New Regime Taxable Income:</strong> ₹${new_taxable.toLocaleString()}</p>
        <p style="color:green;"><strong>Tax under Old Regime:</strong> ₹${old_tax.toLocaleString()}</p>
        <p style="color:blue;"><strong>Tax under New Regime:</strong> ₹${new_tax.toLocaleString()}</p>
        <p><strong>Recommendation:</strong> You save more by using the <b>${old_tax < new_tax ? "Old" : "New"}</b> Regime.</p>
      `;
    }

    function calculateOldTax(income, age) {
      const slabs = {
        normal: [250000, 500000, 1000000],
        senior: [300000, 500000, 1000000],
        super: [500000, 1000000]
      };

      const rates = [0.05, 0.2, 0.3];
      let tax = 0, remaining = income;

      const thresholds = slabs[age];
      if (!thresholds) return 0;

      if (income <= thresholds[0]) return 0;

      if (thresholds.length === 2) {
        if (income <= thresholds[0]) return 0;
        if (income <= thresholds[1]) return (income - thresholds[0]) * 0.2;
        return (thresholds[1] - thresholds[0]) * 0.2 + (income - thresholds[1]) * 0.3;
      }

      if (income <= thresholds[1]) return (income - thresholds[0]) * 0.05;
      if (income <= thresholds[2])
        return (thresholds[1] - thresholds[0]) * 0.05 + (income - thresholds[1]) * 0.2;
      return (thresholds[1] - thresholds[0]) * 0.05 + (thresholds[2] - thresholds[1]) * 0.2 + (income - thresholds[2]) * 0.3;
    }

    function calculateNewTax(income) {
      const slabs = [300000, 600000, 900000, 1200000, 1500000];
      const rates = [0.05, 0.10, 0.15, 0.20, 0.30];
      let tax = 0;

      for (let i = 0; i < slabs.length; i++) {
        if (income > slabs[i]) {
          const prev = i === 0 ? 0 : slabs[i - 1];
          tax += (Math.min(income, slabs[i]) - prev) * rates[i];
        }
      }

      if (income > 1500000) tax += (income - 1500000) * 0.3;
      return tax;
    }
</script>
