(function () {
  'use strict';
  function calculate(values) {
    var names = ['price', 'down', 'closing', 'furnishing', 'repairs', 'fees', 'reserve', 'available'];
    names.forEach(function (name) {
      if (!Number.isFinite(values[name]) || values[name] < 0) throw new Error('Enter a nonnegative amount for every field.');
    });
    if (values.down <= 0 || values.down > 100) throw new Error('Enter a down payment greater than 0 and no more than 100 percent.');
    function cents(n) { return Math.round((n + Number.EPSILON) * 100) / 100; }
    var deposit = cents(values.price * values.down / 100);
    var other = cents(values.closing + values.furnishing + values.repairs + values.fees);
    var upfront = cents(deposit + other);
    var total = cents(upfront + values.reserve);
    return { deposit: deposit, upfront: upfront, reserve: values.reserve, total: total,
      remaining: cents(values.available - total),
      cashPriceCeiling: cents(Math.max(0, values.available - other - values.reserve) / (values.down / 100)) };
  }
  window.BNBFirstStrBudget = { calculate: calculate };
  var form = document.getElementById('first-str-budget-form');
  if (!form) return;
  var results = document.getElementById('first-str-budget-results');
  function money(value) { return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 2 }).format(value); }
  function render() {
    try {
      var values = {};
      ['price', 'down', 'closing', 'furnishing', 'repairs', 'fees', 'reserve', 'available'].forEach(function (name) {
        var input = document.getElementById('budget-' + name);
        if (input.value.trim() === '') throw new Error('Complete every amount; use zero only when you have deliberately excluded that cost.');
        values[name] = Number(input.value);
      });
      var r = calculate(values);
      results.replaceChildren();
      var title = document.createElement('h2'); title.textContent = 'Your first-STR purchase cash plan'; results.appendChild(title);
      var lines = [
        'Down payment: ' + money(r.deposit),
        'Cash used through launch: ' + money(r.upfront),
        'Cash retained as reserves: ' + money(r.reserve),
        'Total allocated cash needed: ' + money(r.total),
        r.remaining >= 0 ? 'Cash remaining after this plan: ' + money(r.remaining) : 'Cash gap to resolve: ' + money(-r.remaining),
        'Cash-only property price ceiling at these fixed inputs: ' + money(r.cashPriceCeiling),
        'Planning estimate only. Confirm lender eligibility, property-specific costs, required liquidity and deal economics before buying.'
      ];
      if (values.fees === 0) lines.push('No service fee is included. Obtain and enter your written quote; zero does not represent BNB Accelerator pricing.');
      lines.forEach(function (line) { var p = document.createElement('p'); p.textContent = line; results.appendChild(p); });
    } catch (error) { results.textContent = error.message; }
  }
  form.addEventListener('submit', function (event) { event.preventDefault(); render(); });
  render();
})();
