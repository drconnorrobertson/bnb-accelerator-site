/* Local catalog filtering; all calculator links remain available without JS. */
(function () {
  'use strict';
  var input = document.getElementById('tool-search');
  var controls = document.getElementById('tool-search-controls');
  var clear = document.getElementById('tool-search-clear');
  var status = document.getElementById('tool-search-status');
  var empty = document.getElementById('tool-search-empty');
  var cards = Array.prototype.slice.call(document.querySelectorAll('[data-tool-card]'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.tool-group'));
  if (!input || !controls || !clear || !status || !empty || !cards.length) return;

  function filter() {
    var terms = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    var count = 0;
    cards.forEach(function (card) {
      var text = card.textContent.toLowerCase();
      card.hidden = !terms.every(function (term) { return text.indexOf(term) !== -1; });
      if (!card.hidden) count++;
    });
    groups.forEach(function (group) {
      group.hidden = !Array.prototype.some.call(group.querySelectorAll('[data-tool-card]'), function (card) { return !card.hidden; });
    });
    status.textContent = count + ' of ' + cards.length + ' calculators shown.';
    empty.hidden = count !== 0;
  }
  input.addEventListener('input', filter);
  clear.addEventListener('click', function () { input.value = ''; filter(); input.focus(); });
  document.querySelectorAll('.tool-jumps a').forEach(function (link) {
    link.addEventListener('click', function () { input.value = ''; filter(); });
  });
  controls.hidden = false;
  filter();
}());
