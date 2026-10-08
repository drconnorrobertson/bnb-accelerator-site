(function () {
  'use strict';
  function calculateRevpar(revenue, booked, available) {
    if (![revenue, booked, available].every(Number.isFinite) || revenue < 0 || !Number.isInteger(booked) || !Number.isInteger(available) || available < 1 || booked < 0 || booked > available || (booked === 0 && revenue !== 0)) {
      throw new RangeError('Use non-negative lodging revenue, whole nights, and at least one available night. Booked nights cannot exceed availability; revenue requires a booked night.');
    }
    return {revpar: revenue / available, adr: booked ? revenue / booked : null, occupancy: booked / available * 100};
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {calculateRevpar};
  if (typeof document === 'undefined') return;
  const form = document.getElementById('revpar-form');
  if (!form) return;
  const money = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'});
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const result = document.getElementById('revpar-result');
    if (!form.reportValidity()) return;
    try {
      const numbers = ['revenue', 'booked', 'available'].map(name => Number(form.elements.namedItem(name).value));
      const value = calculateRevpar(...numbers);
      result.textContent = 'RevPAR: ' + money.format(value.revpar) + ' · ADR: ' + (value.adr === null ? 'not defined without bookings' : money.format(value.adr)) + ' · Occupancy: ' + value.occupancy.toFixed(2) + '%. Revenue productivity only; expenses and financing are not included.';
    } catch (error) { result.textContent = error.message; }
  });
})();
