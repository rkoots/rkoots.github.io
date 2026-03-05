---
layout: default
excerpt: Advanced finance planner with investment calculator, budget analyzer, and wealth projection tools for personalized financial planning.
date: 2026-01-04
title: Finance Planner - Investment & Budget Calculator
categories: finance
permalink: /finance/finance-planner/

description: Plan your investments, control spending, and visualize your financial future with our advanced finance planning calculator. Get personalized investment strategies, budget analysis, and wealth projection tools.
keywords: finance planner, investment calculator, budget planner, financial planning, investment strategy, wealth management, retirement planning, tax saving, mutual funds, SIP calculator, emergency fund, financial goals, expense tracker, savings calculator, investment portfolio, financial advisor, personal finance, money management, investment analysis, risk assessment, financial freedom, wealth building, investment returns, compound interest calculator, retirement corpus, tax planning, financial literacy, investment tips, budget management, expense optimization, financial security, investment planning, wealth projection, financial dashboard
---

<style>
:root {
  --primary: #6366f1;
  --primary-dark: #4f46e5;
  --success: #10b981;
  --warning: #f59e0b;
  --danger: #ef4444;
  --bg-dark: #1e293b;
  --bg-card: #334155;
  --text-light: #f1f5f9;
  --shadow: 0 10px 30px rgba(0,0,0,0.3);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

.finance-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

.header {
  text-align: center;
  color: white;
  margin-bottom: 30px;
  animation: fadeInDown 0.6s ease-out;
}

.header h1 {
  font-size: 2.8em;
  margin-bottom: 10px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.header p {
  font-size: 1.2em;
  opacity: 0.95;
}

.main-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 25px;
  margin-bottom: 25px;
}

.card {
  background: white;
  border-radius: 16px;
  padding: 25px;
  box-shadow: var(--shadow);
  animation: fadeInUp 0.6s ease-out;
}

.card h2 {
  color: var(--primary);
  margin-bottom: 20px;
  font-size: 1.6em;
  border-bottom: 3px solid var(--primary);
  padding-bottom: 10px;
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  font-weight: 600;
  margin-bottom: 8px;
  color: #334155;
  font-size: 0.95em;
}

.input-wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
}

.input-wrapper input[type="number"] {
  flex: 1;
  padding: 12px 15px;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1em;
  transition: all 0.3s;
}

.input-wrapper input[type="number"]:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.currency-symbol {
  font-weight: bold;
  color: var(--primary);
  font-size: 1.1em;
}

.slider-group {
  margin-top: 25px;
  padding: 20px;
  background: #f8fafc;
  border-radius: 12px;
  border: 2px dashed #cbd5e1;
}

.slider-group h3 {
  color: var(--primary-dark);
  margin-bottom: 15px;
  font-size: 1.2em;
}

.slider-item {
  margin-bottom: 20px;
}

.slider-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
}

.slider-header label {
  font-weight: 600;
  color: #475569;
}

.slider-value {
  font-weight: bold;
  color: var(--primary);
  font-size: 1.1em;
}

input[type="range"] {
  width: 100%;
  height: 8px;
  border-radius: 5px;
  background: #e2e8f0;
  outline: none;
  -webkit-appearance: none;
}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--primary);
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 2px 6px rgba(99, 102, 241, 0.4);
}

input[type="range"]::-webkit-slider-thumb:hover {
  transform: scale(1.2);
  background: var(--primary-dark);
}

input[type="range"]::-moz-range-thumb {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--primary);
  cursor: pointer;
  border: none;
  transition: all 0.3s;
}

.btn-primary {
  width: 100%;
  padding: 15px;
  background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.1em;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6);
}

.btn-primary:active {
  transform: translateY(0);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
  margin-bottom: 25px;
}

.stat-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  animation: scaleIn 0.4s ease-out;
}

.stat-card h3 {
  font-size: 0.9em;
  opacity: 0.9;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.stat-card .value {
  font-size: 2em;
  font-weight: bold;
  margin-bottom: 5px;
}

.stat-card .subtext {
  font-size: 0.85em;
  opacity: 0.8;
}

.recommendations {
  background: white;
  border-radius: 16px;
  padding: 25px;
  box-shadow: var(--shadow);
  margin-bottom: 25px;
}

.recommendations h2 {
  color: var(--primary);
  margin-bottom: 20px;
  font-size: 1.6em;
}

.recommendation-item {
  padding: 15px;
  margin-bottom: 15px;
  border-left: 4px solid var(--primary);
  background: #f8fafc;
  border-radius: 8px;
  animation: slideInLeft 0.5s ease-out;
}

.recommendation-item h4 {
  color: var(--primary-dark);
  margin-bottom: 8px;
  font-size: 1.1em;
}

.recommendation-item p {
  color: #475569;
  line-height: 1.6;
}

.chart-container {
  background: white;
  border-radius: 16px;
  padding: 25px;
  box-shadow: var(--shadow);
  margin-bottom: 25px;
  min-height: 500px;
}

.chart-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 25px;
}

.alert {
  padding: 15px 20px;
  border-radius: 10px;
  margin-bottom: 20px;
  font-weight: 500;
  animation: slideInRight 0.5s ease-out;
}

.alert-warning {
  background: #fef3c7;
  color: #92400e;
  border-left: 4px solid var(--warning);
}

.alert-success {
  background: #d1fae5;
  color: #065f46;
  border-left: 4px solid var(--success);
}

.alert-danger {
  background: #fee2e2;
  color: #991b1b;
  border-left: 4px solid var(--danger);
}

.hidden {
  display: none;
}

@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInLeft {
  from { opacity: 0; transform: translateX(-20px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes slideInRight {
  from { opacity: 0; transform: translateX(20px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}

@media (max-width: 1024px) {
  .main-grid, .chart-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .header h1 { font-size: 2em; }
  .header p { font-size: 1em; }
  .stats-grid { grid-template-columns: 1fr; }
}
</style>

<div class="finance-container">
  <div class="header">
    <h1>💰 Advanced Finance Planner</h1>
    <p>Plan your investments, control spending, and visualize your financial future with interactive 3D analytics</p>
    <p style="font-size: 0.9em; opacity: 0.8; margin-top: 10px;">✅ Free Financial Planning Tool | 📊 Real-time Investment Analysis | 🎯 Personalized Wealth Strategies | 📈 3D Visualization Charts</p>
  </div>

  <div class="main-grid">
    <div class="card">
      <h2>📊 Income Details</h2>
      <div class="input-group">
        <label for="monthlySalary">Monthly Salary</label>
        <div class="input-wrapper">
          <span class="currency-symbol">₹</span>
          <input type="number" id="monthlySalary" placeholder="50000" min="0" step="1000">
        </div>
      </div>
      <div class="input-group">
        <label for="otherIncome">Other Income (Freelance, Rent, etc.)</label>
        <div class="input-wrapper">
          <span class="currency-symbol">₹</span>
          <input type="number" id="otherIncome" placeholder="10000" min="0" step="1000">
        </div>
      </div>
      <div class="input-group">
        <label for="age">Your Age</label>
        <div class="input-wrapper">
          <input type="number" id="age" placeholder="30" min="18" max="100">
        </div>
      </div>
      <div class="input-group">
        <label for="riskProfile">Risk Profile</label>
        <select id="riskProfile" style="width: 100%; padding: 12px; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 1em;">
          <option value="conservative">Conservative (Low Risk)</option>
          <option value="moderate" selected>Moderate (Balanced)</option>
          <option value="aggressive">Aggressive (High Risk)</option>
        </select>
      </div>
      <button class="btn-primary" onclick="generatePlan()">🚀 Generate Financial Plan</button>
    </div>

    <div class="card">
      <h2>💳 Monthly Expenses</h2>
      <div class="input-group">
        <label for="rent">Rent/Mortgage</label>
        <div class="input-wrapper">
          <span class="currency-symbol">₹</span>
          <input type="number" id="rent" placeholder="15000" min="0" step="500">
        </div>
      </div>
      <div class="input-group">
        <label for="utilities">Utilities & Bills</label>
        <div class="input-wrapper">
          <span class="currency-symbol">₹</span>
          <input type="number" id="utilities" placeholder="3000" min="0" step="500">
        </div>
      </div>
      <div class="input-group">
        <label for="groceries">Groceries & Food</label>
        <div class="input-wrapper">
          <span class="currency-symbol">₹</span>
          <input type="number" id="groceries" placeholder="8000" min="0" step="500">
        </div>
      </div>
      <div class="input-group">
        <label for="transport">Transportation</label>
        <div class="input-wrapper">
          <span class="currency-symbol">₹</span>
          <input type="number" id="transport" placeholder="3000" min="0" step="500">
        </div>
      </div>
      <div class="input-group">
        <label for="entertainment">Entertainment & Lifestyle</label>
        <div class="input-wrapper">
          <span class="currency-symbol">₹</span>
          <input type="number" id="entertainment" placeholder="5000" min="0" step="500">
        </div>
      </div>
      <div class="input-group">
        <label for="otherExpenses">Other Expenses</label>
        <div class="input-wrapper">
          <span class="currency-symbol">₹</span>
          <input type="number" id="otherExpenses" placeholder="2000" min="0" step="500">
        </div>
      </div>
    </div>
  </div>

  <div id="resultsSection" class="hidden">
    <div id="alertContainer"></div>

    <div class="stats-grid">
      <div class="stat-card">
        <h3>Total Income</h3>
        <div class="value" id="totalIncome">₹0</div>
        <div class="subtext">Per Month</div>
      </div>
      <div class="stat-card">
        <h3>Total Expenses</h3>
        <div class="value" id="totalExpenses">₹0</div>
        <div class="subtext">Per Month</div>
      </div>
      <div class="stat-card">
        <h3>Monthly Savings</h3>
        <div class="value" id="monthlySavings">₹0</div>
        <div class="subtext" id="savingsRate">0% of Income</div>
      </div>
      <div class="stat-card">
        <h3>Yearly Savings</h3>
        <div class="value" id="yearlySavings">₹0</div>
        <div class="subtext">Potential Growth</div>
      </div>
    </div>

    <div class="card slider-group">
      <h3>🎚️ Adjust Your Expenses in Real-Time</h3>
      <div class="slider-item">
        <div class="slider-header">
          <label>Rent/Mortgage</label>
          <span class="slider-value" id="rentSliderValue">₹0</span>
        </div>
        <input type="range" id="rentSlider" min="0" max="50000" step="500" oninput="updateExpenseSlider('rent')">
      </div>
      <div class="slider-item">
        <div class="slider-header">
          <label>Utilities & Bills</label>
          <span class="slider-value" id="utilitiesSliderValue">₹0</span>
        </div>
        <input type="range" id="utilitiesSlider" min="0" max="10000" step="200" oninput="updateExpenseSlider('utilities')">
      </div>
      <div class="slider-item">
        <div class="slider-header">
          <label>Groceries & Food</label>
          <span class="slider-value" id="groceriesSliderValue">₹0</span>
        </div>
        <input type="range" id="groceriesSlider" min="0" max="20000" step="500" oninput="updateExpenseSlider('groceries')">
      </div>
      <div class="slider-item">
        <div class="slider-header">
          <label>Transportation</label>
          <span class="slider-value" id="transportSliderValue">₹0</span>
        </div>
        <input type="range" id="transportSlider" min="0" max="15000" step="500" oninput="updateExpenseSlider('transport')">
      </div>
      <div class="slider-item">
        <div class="slider-header">
          <label>Entertainment & Lifestyle</label>
          <span class="slider-value" id="entertainmentSliderValue">₹0</span>
        </div>
        <input type="range" id="entertainmentSlider" min="0" max="20000" step="500" oninput="updateExpenseSlider('entertainment')">
      </div>
      <div class="slider-item">
        <div class="slider-header">
          <label>Other Expenses</label>
          <span class="slider-value" id="otherExpensesSliderValue">₹0</span>
        </div>
        <input type="range" id="otherExpensesSlider" min="0" max="10000" step="500" oninput="updateExpenseSlider('otherExpenses')">
      </div>
    </div>

    <div class="recommendations">
      <h2>💡 Personalized Recommendations</h2>
      <div id="recommendationsContent"></div>
    </div>

    <div class="chart-grid">
      <div class="chart-container">
        <h2 style="color: var(--primary); margin-bottom: 20px;">📈 Investment Allocation (3D)</h2>
        <div id="investmentChart"></div>
      </div>
      <div class="chart-container">
        <h2 style="color: var(--primary); margin-bottom: 20px;">💰 Expense Breakdown (3D)</h2>
        <div id="expenseChart"></div>
      </div>
    </div>

    <div class="chart-container">
      <h2 style="color: var(--primary); margin-bottom: 20px;">🚀 Wealth Projection (10 Years)</h2>
      <div id="wealthProjectionChart"></div>
    </div>

    <div class="chart-container">
      <h2 style="color: var(--primary); margin-bottom: 20px;">🎯 Financial Goals Timeline</h2>
      <div id="goalsChart"></div>
    </div>
  </div>

  <!-- FAQ Section -->
  <div class="recommendations" style="margin-top: 40px;">
    <h2>❓ Frequently Asked Questions (FAQ)</h2>
    
    <div class="recommendation-item">
      <h4>🎯 How much should I save monthly for financial security?</h4>
      <p>Financial experts recommend saving at least 20% of your monthly income. This includes emergency fund contributions, retirement savings, and other investments. Our finance planner helps you track your savings rate and provides personalized recommendations based on your income and expenses.</p>
    </div>

    <div class="recommendation-item">
      <h4>💎 What is the ideal investment allocation for my age?</h4>
      <p>The ideal investment allocation depends on your age, risk tolerance, and financial goals. A common rule is (100 - your age) in equity investments. Our advanced finance planner automatically calculates optimal allocation across equity, debt, gold, and liquid assets based on your risk profile and age.</p>
    </div>

    <div class="recommendation-item">
      <h4>🛡️ How big should my emergency fund be?</h4>
      <p>Your emergency fund should cover 6-12 months of essential expenses. This fund should be kept in liquid instruments like savings accounts, fixed deposits, or liquid mutual funds. Our calculator automatically determines your ideal emergency fund amount based on your monthly expenses.</p>
    </div>

    <div class="recommendation-item">
      <h4>📊 How can I optimize my monthly budget?</h4>
      <p>Start by tracking all expenses, categorize them, and identify areas where you can cut costs. The 50/30/20 rule suggests 50% for needs, 30% for wants, and 20% for savings. Our budget planner provides real-time expense tracking with interactive sliders to help you optimize your spending.</p>
    </div>

    <div class="recommendation-item">
      <h4>🚀 What are the best tax-saving investment options in India?</h4>
      <p>Popular tax-saving options under Section 80C include ELSS mutual funds, PPF, NSC, and tax-saving fixed deposits (up to ₹1.5 lakh). Additional deductions are available under Section 80D for health insurance and Section 80CCD(1B) for NPS investments. Our planner helps maximize your tax savings while building wealth.</p>
    </div>

    <div class="recommendation-item">
      <h4>📈 How much wealth can I build through SIP investments?</h4>
      <p>Systematic Investment Plans (SIPs) can build substantial wealth through compounding. For example, investing ₹10,000 monthly at 12% annual return for 20 years can create over ₹1 crore. Our wealth projection calculator shows your potential growth across different return scenarios.</p>
    </div>

    <div class="recommendation-item">
      <h4>🎓 When should I start retirement planning?</h4>
      <p>The best time to start retirement planning is in your 20s or early 30s. Starting early allows compound interest to work in your favor. Even small monthly investments can grow into substantial retirement corpus. Our calculator helps you plan for retirement based on your current age and desired retirement age.</p>
    </div>

    <div class="recommendation-item">
      <h4>⚖️ How do I choose between conservative, moderate, and aggressive investment strategies?</h4>
      <p>Conservative strategies focus on capital preservation with lower returns (6-8%), suitable for retirees or risk-averse investors. Moderate strategies balance risk and returns (10-12%), ideal for most investors. Aggressive strategies aim for higher returns (14%+) with higher risk, suitable for young investors with long time horizons.</p>
    </div>
  </div>

  <!-- Additional Content Section -->
  <div class="recommendations" style="margin-top: 30px;">
    <h2>📚 Financial Planning Resources & Tips</h2>
    
    <div class="recommendation-item">
      <h4>💡 Key Financial Planning Principles</h4>
      <p><strong>1. Pay Yourself First:</strong> Automate your savings and investments before spending on anything else.<br>
      <strong>2. Diversify Your Portfolio:</strong> Spread investments across different asset classes to minimize risk.<br>
      <strong>3. Review Regularly:</strong> Review your financial plan quarterly and adjust as needed.<br>
      <strong>4. Stay Informed:</strong> Keep learning about personal finance and investment options.</p>
    </div>

    <div class="recommendation-item">
      <h4>🎯 Common Financial Goals and Timelines</h4>
      <p><strong>Emergency Fund:</strong> 1-2 years | <strong>Vacation:</strong> 1-3 years | <strong>Car Purchase:</strong> 3-5 years<br>
      <strong>Home Down Payment:</strong> 5-7 years | <strong>Children's Education:</strong> 10-15 years | <strong>Retirement:</strong> 20-30 years</p>
    </div>

    <div class="recommendation-item">
      <h4>📊 Investment Options for Different Risk Profiles</h4>
      <p><strong>Conservative:</strong> Fixed deposits, PPF, debt mutual funds, government bonds<br>
      <strong>Moderate:</strong> Balanced mutual funds, index funds, corporate FDs, gold ETFs<br>
      <strong>Aggressive:</strong> Equity mutual funds, direct stocks, sectoral funds, international funds</p>
    </div>

    <div class="recommendation-item">
      <h4>🔍 Why Use Our Finance Planner?</h4>
      <p>✅ <strong>Comprehensive Analysis:</strong> Complete financial health assessment in minutes<br>
      ✅ <strong>Personalized Recommendations:</strong> Tailored advice based on your unique situation<br>
      ✅ <strong>Real-time Calculations:</strong> Instant updates as you adjust your numbers<br>
      ✅ <strong>3D Visualizations:</strong> Interactive charts for better understanding<br>
      ✅ <strong>Goal Tracking:</strong> Plan and track multiple financial goals<br>
      ✅ <strong>Tax Optimization:</strong> Maximize your tax-saving opportunities<br>
      ✅ <strong>Retirement Planning:</strong> Secure your financial future with proper planning</p>
    </div>
  </div>
</div>

<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>

<script>
{% raw %}
let financialData = {
  income: 0,
  expenses: {},
  totalExpenses: 0,
  savings: 0,
  age: 30,
  riskProfile: 'moderate'
};

function generatePlan() {
  const monthlySalary = parseFloat(document.getElementById('monthlySalary').value) || 0;
  const otherIncome = parseFloat(document.getElementById('otherIncome').value) || 0;
  const age = parseInt(document.getElementById('age').value) || 30;
  const riskProfile = document.getElementById('riskProfile').value;

  financialData.income = monthlySalary + otherIncome;
  financialData.age = age;
  financialData.riskProfile = riskProfile;

  const expenseFields = ['rent', 'utilities', 'groceries', 'transport', 'entertainment', 'otherExpenses'];
  financialData.expenses = {};
  financialData.totalExpenses = 0;

  expenseFields.forEach(field => {
    const value = parseFloat(document.getElementById(field).value) || 0;
    financialData.expenses[field] = value;
    financialData.totalExpenses += value;
    
    document.getElementById(field + 'Slider').value = value;
    document.getElementById(field + 'SliderValue').textContent = '₹' + value.toLocaleString('en-IN');
  });

  financialData.savings = financialData.income - financialData.totalExpenses;

  updateDashboard();
  document.getElementById('resultsSection').classList.remove('hidden');
  document.getElementById('resultsSection').scrollIntoView({ behavior: 'smooth' });
}

function updateExpenseSlider(field) {
  const slider = document.getElementById(field + 'Slider');
  const value = parseFloat(slider.value);
  
  financialData.expenses[field] = value;
  document.getElementById(field + 'SliderValue').textContent = '₹' + value.toLocaleString('en-IN');
  
  financialData.totalExpenses = Object.values(financialData.expenses).reduce((a, b) => a + b, 0);
  financialData.savings = financialData.income - financialData.totalExpenses;
  
  updateDashboard();
}

function updateDashboard() {
  document.getElementById('totalIncome').textContent = '₹' + financialData.income.toLocaleString('en-IN');
  document.getElementById('totalExpenses').textContent = '₹' + financialData.totalExpenses.toLocaleString('en-IN');
  document.getElementById('monthlySavings').textContent = '₹' + financialData.savings.toLocaleString('en-IN');
  
  const savingsRate = financialData.income > 0 ? ((financialData.savings / financialData.income) * 100).toFixed(1) : 0;
  document.getElementById('savingsRate').textContent = savingsRate + '% of Income';
  document.getElementById('yearlySavings').textContent = '₹' + (financialData.savings * 12).toLocaleString('en-IN');

  showAlerts();
  generateRecommendations();
  renderCharts();
}

function showAlerts() {
  const alertContainer = document.getElementById('alertContainer');
  alertContainer.innerHTML = '';

  const savingsRate = (financialData.savings / financialData.income) * 100;

  if (financialData.savings < 0) {
    alertContainer.innerHTML += `<div class="alert alert-danger">⚠️ <strong>Critical:</strong> Your expenses exceed your income by ₹${Math.abs(financialData.savings).toLocaleString('en-IN')}. Immediate action required!</div>`;
  } else if (savingsRate < 10) {
    alertContainer.innerHTML += `<div class="alert alert-warning">⚠️ <strong>Warning:</strong> Your savings rate is only ${savingsRate.toFixed(1)}%. Aim for at least 20% for financial security.</div>`;
  } else if (savingsRate >= 30) {
    alertContainer.innerHTML += `<div class="alert alert-success">✅ <strong>Excellent:</strong> You're saving ${savingsRate.toFixed(1)}% of your income! Keep up the great work!</div>`;
  }
}

function generateRecommendations() {
  const container = document.getElementById('recommendationsContent');
  const savingsRate = (financialData.savings / financialData.income) * 100;
  const age = financialData.age;
  const yearsToRetirement = 60 - age;
  
  let recommendations = [];

  const allocation = calculateAllocation();

  recommendations.push({
    title: '🎯 Investment Allocation Strategy',
    text: `Based on your ${financialData.riskProfile} risk profile and age ${age}, we recommend: <strong>${allocation.equity}% Equity</strong>, <strong>${allocation.debt}% Debt</strong>, <strong>${allocation.gold}% Gold</strong>, and <strong>${allocation.liquid}% Liquid/Emergency Fund</strong>.`
  });

  if (financialData.savings > 0) {
    const emergencyFund = Math.min(financialData.totalExpenses * 6, financialData.savings * 0.25);
    recommendations.push({
      title: '🛡️ Emergency Fund',
      text: `Build an emergency fund of ₹${emergencyFund.toLocaleString('en-IN')} (6 months of expenses). Keep this in liquid instruments like savings accounts or liquid funds.`
    });

    const monthlyInvestment = financialData.savings - (emergencyFund / 6);
    const projectedWealth = calculateFutureValue(monthlyInvestment, 12, yearsToRetirement);
    
    recommendations.push({
      title: '💎 Retirement Planning',
      text: `Investing ₹${monthlyInvestment.toLocaleString('en-IN')}/month at 12% annual return could grow to approximately <strong>₹${(projectedWealth / 10000000).toFixed(2)} Crores</strong> by retirement (age 60).`
    });
  }

  const highestExpense = Object.entries(financialData.expenses).reduce((a, b) => a[1] > b[1] ? a : b);
  const expenseLabels = {
    rent: 'Rent/Mortgage',
    utilities: 'Utilities',
    groceries: 'Groceries',
    transport: 'Transportation',
    entertainment: 'Entertainment',
    otherExpenses: 'Other Expenses'
  };
  
  if (highestExpense[1] > financialData.income * 0.35) {
    recommendations.push({
      title: '💡 Expense Optimization',
      text: `Your ${expenseLabels[highestExpense[0]]} (₹${highestExpense[1].toLocaleString('en-IN')}) is ${((highestExpense[1] / financialData.income) * 100).toFixed(1)}% of your income. Consider optimizing this category to increase savings.`
    });
  }

  if (savingsRate >= 20) {
    recommendations.push({
      title: '🚀 Tax Saving Opportunities',
      text: `Maximize tax benefits under Section 80C (₹1.5L), 80D (₹25K-₹50K for health insurance), and NPS (additional ₹50K under 80CCD(1B)). This could save you ₹${(46000).toLocaleString('en-IN')}+ in taxes annually.`
    });
  }

  recommendations.push({
    title: '📊 Diversification Strategy',
    text: `Diversify across asset classes: Large-cap equity funds (40%), Mid/Small-cap funds (${allocation.equity - 40}%), Debt funds (${allocation.debt}%), Gold ETFs (${allocation.gold}%), and maintain ${allocation.liquid}% in liquid assets.`
  });

  container.innerHTML = recommendations.map(rec => `
    <div class="recommendation-item">
      <h4>${rec.title}</h4>
      <p>${rec.text}</p>
    </div>
  `).join('');
}

function calculateAllocation() {
  const age = financialData.age;
  const risk = financialData.riskProfile;
  
  let equity, debt, gold, liquid;
  
  if (risk === 'aggressive') {
    equity = Math.max(100 - age, 60);
    debt = Math.min(age - 10, 25);
    gold = 5;
    liquid = 10;
  } else if (risk === 'conservative') {
    equity = Math.max(100 - age - 20, 30);
    debt = Math.min(age + 10, 50);
    gold = 10;
    liquid = 10;
  } else {
    equity = Math.max(100 - age, 50);
    debt = Math.min(age, 35);
    gold = 10;
    liquid = 5;
  }
  
  const total = equity + debt + gold + liquid;
  return {
    equity: Math.round((equity / total) * 100),
    debt: Math.round((debt / total) * 100),
    gold: Math.round((gold / total) * 100),
    liquid: Math.round((liquid / total) * 100)
  };
}

function calculateFutureValue(monthlyInvestment, annualReturn, years) {
  const monthlyRate = annualReturn / 100 / 12;
  const months = years * 12;
  return monthlyInvestment * ((Math.pow(1 + monthlyRate, months) - 1) / monthlyRate) * (1 + monthlyRate);
}

function renderCharts() {
  renderInvestmentChart();
  renderExpenseChart();
  renderWealthProjection();
  renderGoalsChart();
}

function renderInvestmentChart() {
  if (financialData.savings <= 0) return;

  const allocation = calculateAllocation();
  const investmentAmount = financialData.savings * 0.75;

  const data = [{
    type: 'pie',
    values: [
      (allocation.equity / 100) * investmentAmount,
      (allocation.debt / 100) * investmentAmount,
      (allocation.gold / 100) * investmentAmount,
      (allocation.liquid / 100) * investmentAmount
    ],
    labels: ['Equity', 'Debt', 'Gold', 'Liquid/Emergency'],
    marker: {
      colors: ['#6366f1', '#10b981', '#f59e0b', '#3b82f6'],
      line: { color: 'white', width: 2 }
    },
    textinfo: 'label+percent',
    textposition: 'outside',
    hole: 0.4,
    pull: [0.05, 0, 0, 0],
    rotation: 45
  }];

  const layout = {
    height: 350,
    showlegend: true,
    legend: { orientation: 'h', y: -0.1 },
    margin: { t: 20, b: 60, l: 20, r: 20 },
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    font: { family: 'Segoe UI', size: 12 }
  };

  Plotly.newPlot('investmentChart', data, layout, { responsive: true, displayModeBar: false });
}

function renderExpenseChart() {
  const expenseLabels = {
    rent: 'Rent/Mortgage',
    utilities: 'Utilities',
    groceries: 'Groceries',
    transport: 'Transportation',
    entertainment: 'Entertainment',
    otherExpenses: 'Other'
  };

  const labels = Object.keys(financialData.expenses).map(k => expenseLabels[k]);
  const values = Object.values(financialData.expenses);
  const colors = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6', '#ec4899'];

  const data = [{
    type: 'pie',
    values: values,
    labels: labels,
    marker: {
      colors: colors,
      line: { color: 'white', width: 2 }
    },
    textinfo: 'label+percent',
    textposition: 'auto',
    hole: 0.4
  }];

  const layout = {
    height: 350,
    showlegend: true,
    legend: { orientation: 'h', y: -0.1 },
    margin: { t: 20, b: 60, l: 20, r: 20 },
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    font: { family: 'Segoe UI', size: 12 }
  };

  Plotly.newPlot('expenseChart', data, layout, { responsive: true, displayModeBar: false });
}

function renderWealthProjection() {
  const years = [];
  const conservativeWealth = [];
  const moderateWealth = [];
  const aggressiveWealth = [];
  
  const monthlyInvestment = Math.max(financialData.savings * 0.75, 0);
  
  for (let year = 0; year <= 10; year++) {
    years.push(year);
    conservativeWealth.push(calculateFutureValue(monthlyInvestment, 8, year) / 100000);
    moderateWealth.push(calculateFutureValue(monthlyInvestment, 12, year) / 100000);
    aggressiveWealth.push(calculateFutureValue(monthlyInvestment, 15, year) / 100000);
  }

  const trace1 = {
    x: years,
    y: conservativeWealth,
    z: conservativeWealth.map((v, i) => i * 2),
    mode: 'lines+markers',
    type: 'scatter3d',
    name: 'Conservative (8%)',
    line: { color: '#10b981', width: 4 },
    marker: { size: 5, color: '#10b981' }
  };

  const trace2 = {
    x: years,
    y: moderateWealth,
    z: moderateWealth.map((v, i) => i * 2 + 5),
    mode: 'lines+markers',
    type: 'scatter3d',
    name: 'Moderate (12%)',
    line: { color: '#6366f1', width: 4 },
    marker: { size: 5, color: '#6366f1' }
  };

  const trace3 = {
    x: years,
    y: aggressiveWealth,
    z: aggressiveWealth.map((v, i) => i * 2 + 10),
    mode: 'lines+markers',
    type: 'scatter3d',
    name: 'Aggressive (15%)',
    line: { color: '#ef4444', width: 4 },
    marker: { size: 5, color: '#ef4444' }
  };

  const layout = {
    height: 500,
    scene: {
      xaxis: { title: 'Years' },
      yaxis: { title: 'Wealth (Lakhs ₹)' },
      zaxis: { title: 'Growth Trajectory' },
      camera: {
        eye: { x: 1.5, y: 1.5, z: 1.3 }
      }
    },
    margin: { t: 20, b: 20, l: 20, r: 20 },
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    font: { family: 'Segoe UI', size: 11 }
  };

  Plotly.newPlot('wealthProjectionChart', [trace1, trace2, trace3], layout, { responsive: true, displayModeBar: false });
}

function renderGoalsChart() {
  const goals = [
    { name: 'Emergency Fund', target: financialData.totalExpenses * 6, years: 1, color: '#10b981' },
    { name: 'Vacation Fund', target: 200000, years: 2, color: '#3b82f6' },
    { name: 'Car Purchase', target: 800000, years: 4, color: '#f59e0b' },
    { name: 'Home Down Payment', target: 2000000, years: 7, color: '#8b5cf6' },
    { name: 'Retirement Corpus', target: 10000000, years: 60 - financialData.age, color: '#ef4444' }
  ];

  const monthlyInvestment = Math.max(financialData.savings * 0.75, 0);

  const x = goals.map(g => g.name);
  const y = goals.map(g => g.years);
  const z = goals.map(g => {
    const achieved = calculateFutureValue(monthlyInvestment, 12, g.years);
    return (achieved / g.target) * 100;
  });
  const colors = goals.map(g => g.color);

  const data = [{
    x: x,
    y: y,
    z: z,
    type: 'bar',
    marker: {
      color: colors,
      line: { color: 'white', width: 2 }
    },
    text: z.map(v => v.toFixed(1) + '%'),
    textposition: 'outside',
    hovertemplate: '<b>%{x}</b><br>Years: %{y}<br>Achievement: %{z:.1f}%<extra></extra>'
  }];

  const layout = {
    height: 400,
    xaxis: { title: 'Financial Goals' },
    yaxis: { title: 'Time Horizon (Years)' },
    margin: { t: 40, b: 100, l: 60, r: 40 },
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    font: { family: 'Segoe UI', size: 11 }
  };

  Plotly.newPlot('goalsChart', data, layout, { responsive: true, displayModeBar: false });
}
{% endraw %}
</script>












