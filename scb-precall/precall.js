// No CRM writes, query-string personalization, contact storage or parameter forwarding.
document.querySelectorAll('[data-youtube]').forEach(player => {
  player.querySelector('button').addEventListener('click', () => {
    const frame = document.createElement('iframe');
    frame.src = `https://www.youtube-nocookie.com/embed/${player.dataset.youtube}?autoplay=1`;
    frame.title = player.querySelector('button').getAttribute('aria-label').replace(/^Play /, '');
    frame.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
    frame.allowFullscreen = true;
    // YouTube requires an origin referer. Never send query strings or page paths.
    frame.referrerPolicy = 'strict-origin';
    player.querySelector('button').replaceWith(frame);
  });
});
const search = document.querySelector('#deal-search');
const deals = [...document.querySelectorAll('#deals .bnb-ul > li')];
function filterDeals() {
  const term = search.value.trim().toLocaleLowerCase();
  let shown = 0;
  deals.forEach(deal => {
    deal.hidden = !deal.textContent.toLocaleLowerCase().includes(term);
    if (!deal.hidden) shown++;
  });
  document.querySelector('#deal-count').textContent = `${shown} of ${deals.length} source-provided examples${shown === 0 ? ' — try another city or address' : ''}`;
}
if (search) { search.addEventListener('input', filterDeals); filterDeals(); }
