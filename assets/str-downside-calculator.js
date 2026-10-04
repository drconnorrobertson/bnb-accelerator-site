(() => {
  'use strict';
  const form = document.getElementById('downside-form');
  if (!form) return;
  const keys = ['revenue', 'variable', 'fixed', 'debt', 'reserve', 'cash', 'drop'];
  const dollars = value => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(value);
  const percent = value => value === null ? 'Not defined: no cash invested' : `${value.toFixed(2)}%`;
  function calculate(event) {
    if (event) event.preventDefault();
    const error = document.getElementById('calc-error');
    const output = document.getElementById('downside-results');
    const inputs = keys.map(key => document.getElementById(key));
    const values = inputs.map(input => Number(input.value));
    if (inputs.some(input => input.value.trim() === '') || values.some(value => !Number.isFinite(value) || value < 0) || values[1] > 100 || values[6] > 100) {
      error.textContent = 'Enter nonnegative numbers in every field. Percentages must be between 0 and 100.';
      output.replaceChildren();
      return;
    }
    error.textContent = '';
    const [revenue, variable, fixed, debt, reserve, cash, drop] = values;
    const margin = 1 - variable / 100;
    const annualCost = fixed + debt + reserve;
    const downsideRevenue = revenue * (1 - drop / 100);
    const baseFlow = revenue * margin - annualCost;
    const downsideFlow = downsideRevenue * margin - annualCost;
    const breakEven = margin > 0 ? dollars(annualCost / margin) : 'No positive contribution margin';
    output.innerHTML = `<h2>Modeled results</h2><div class="table-scroll"><table><thead><tr><th>Annual measure</th><th>Base case</th><th>Downside case</th></tr></thead><tbody><tr><td>Accommodation revenue</td><td>${dollars(revenue)}</td><td>${dollars(downsideRevenue)}</td></tr><tr><td>Cash flow after reserves and debt</td><td>${dollars(baseFlow)}</td><td>${dollars(downsideFlow)}</td></tr><tr><td>Cash-on-cash return</td><td>${percent(cash > 0 ? baseFlow / cash * 100 : null)}</td><td>${percent(cash > 0 ? downsideFlow / cash * 100 : null)}</td></tr></tbody></table></div><p><strong>Annual break-even accommodation revenue:</strong> ${breakEven}.</p><p><strong>Cash-flow change:</strong> ${dollars(downsideFlow - baseFlow)} per year. These modeled results depend on the inputs and simplified cost behavior described below.</p>`;
  }
  form.addEventListener('submit', calculate);
  form.addEventListener('input', calculate);
  calculate();
})();
