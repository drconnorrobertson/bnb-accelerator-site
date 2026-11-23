(function () {
  'use strict';
  const form = document.getElementById('cl-filters');
  if (!form) return;
  const search = document.getElementById('cl-search');
  const platform = document.getElementById('cl-platform');
  const kind = document.getElementById('cl-kind');
  const topic = document.getElementById('cl-topic');
  const grid = document.getElementById('cl-grid');
  const status = document.getElementById('cl-status');
  const more = document.getElementById('cl-more');
  const empty = document.getElementById('cl-empty');
  const pages = document.getElementById('cl-pagination');
  const topics = {participation:'Material participation',depreciation:'Depreciation and tax planning','seller-finance':'Seller and creative financing',loan:'Loans and cash to close',refinance:'Equity and refinancing',design:'Design and furnishing',management:'Co-hosting and operations',regulations:'Rules and property permissions',markets:'Market selection','case-studies':'Client stories and examples','cash-flow':'Cash flow and underwriting',process:'Acquisition process'};
  let records = [], matches = [], limit = 24;
  const escape = text => String(text).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
  const normalize = text => String(text).normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  function card(item) {
    const path = escape(item.path), title = escape(item.title);
    const visual = item.platform === 'YouTube' ? '<img src="https://i.ytimg.com/vi/'+escape(item.id)+'/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">' : '<span class="cl-instagram-art" aria-hidden="true">BNB<br>Instagram</span>';
    return '<article class="cl-card"><a class="cl-card-image" href="'+path+'" tabindex="-1" aria-hidden="true">'+visual+'</a><div class="cl-card-copy"><p class="cl-label">'+escape(item.platform)+' · '+escape(item.kind)+'</p><h2><a href="'+path+'">'+title+'</a></h2><p>'+escape(topics[item.topic] || item.topic)+'</p><a class="cl-read" href="'+path+'">Watch and read<span class="cl-sr">: '+title+'</span></a></div></article>';
  }
  function render() {
    grid.innerHTML = matches.slice(0,limit).map(card).join('');
    status.textContent = 'Showing '+Math.min(limit,matches.length)+' of '+matches.length+' matching posts.';
    empty.hidden = matches.length !== 0;
    more.hidden = matches.length <= limit;
    pages.hidden = true;
  }
  function filter(updateURL = true) {
    const words = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    matches = records.filter(item => (!platform.value || item.platform === platform.value) && (!kind.value || item.kind === kind.value) && (!topic.value || item.topic === topic.value) && words.every(word => normalize(item.title+' '+item.platform+' '+item.kind+' '+(topics[item.topic]||'')).includes(word)));
    limit = 24;
    render();
    if (updateURL) {
      const url = new URL(location.href);
      for (const [key,value] of [['q',search.value.trim()],['platform',platform.value],['format',kind.value],['topic',topic.value]]) {
        if (value) url.searchParams.set(key,value); else url.searchParams.delete(key);
      }
      history.replaceState(null,'',url);
    }
  }
  function ready() {
    records = window.BNB_CONTENT_LIBRARY || [];
    if (!records.length) return;
    const params = new URLSearchParams(location.search);
    search.value = params.get('q') || '';
    for (const [element,key] of [[platform,'platform'],[kind,'format'],[topic,'topic']]) {
      const value=params.get(key)||'';
      if ([...element.options].some(option=>option.value===value)) element.value=value;
    }
    if (search.value || platform.value || kind.value || topic.value) filter(false);
  }
  form.addEventListener('submit',event=>{event.preventDefault();filter();});
  search.addEventListener('input',()=>filter());
  [platform,kind,topic].forEach(element=>element.addEventListener('change',()=>filter()));
  form.addEventListener('reset',()=>{search.value='';platform.value='';kind.value='';topic.value='';filter();});
  more.addEventListener('click',()=>{limit+=24;render();});
  window.addEventListener('bnb-content-ready',ready);
  if (window.BNB_CONTENT_LIBRARY) ready();
})();
