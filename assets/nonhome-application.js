
(function () {
  'use strict';
  var dialog = document.getElementById('bnb-application');
  var frame = document.getElementById('bnb-application-frame');
  var title = document.getElementById('bnb-application-title');
  var status = document.getElementById('bnb-application-status');
  var formOrigin = 'https://api.leadconnectorhq.com';
  var formId = frame.dataset.formId;
  var step = 'lead';
  var opener;
  var contact = null;
  var bodyOverflow;
  function open(event) {
    if (!dialog.showModal) return;
    event.preventDefault();
    event.stopPropagation();
    var nav = document.getElementById('site-nav');
    var toggle = document.querySelector('.menu-toggle');
    if (nav && nav.dataset.open === 'true') {
      nav.dataset.open = 'false';
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
    opener = event.currentTarget;
    bodyOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    if (!frame.getAttribute('src')) frame.src = formOrigin + '/widget/form/' + formId;
    dialog.showModal();
  }
  // Every booking CTA follows the same two-step flow.
  document.querySelectorAll('a[href="/apply/"]').forEach(function (link) {
    if (dialog.contains(link)) return;
    link.setAttribute('aria-haspopup', 'dialog');
    link.setAttribute('aria-controls', dialog.id);
    link.addEventListener('click', open);
  });
  dialog.querySelector('.bnb-close').addEventListener('click', function () { dialog.close(); });
  dialog.addEventListener('click', function (event) {
    if (event.target !== dialog) return;
    var bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
  dialog.addEventListener('close', function () {
    document.body.style.overflow = bodyOverflow || '';
    if (opener) opener.focus();
  });
  function schedule(data) {
    step = 'schedule';
    contact = data;
    dialog.dataset.step = step;
    title.textContent = 'Choose A Time For Your BNB Accelerator Call';
    status.textContent = 'Step 2 of 2: Your details have been received. Select an available date and time below.';
    frame.title = 'Schedule a BNB Accelerator call';
    frame.style.height = '';
    // Personal details stay in memory and are passed only to the same booking provider.
    frame.src = formOrigin + '/widget/booking/ZsaZ20WoBCzlaqpmBxQF';
    dialog.scrollTop = 0;
  }
  window.addEventListener('message', function (event) {
    if (event.origin !== formOrigin || event.source !== frame.contentWindow || !Array.isArray(event.data)) return;
    var message = event.data;
    if (message[0] === 'fetch-query-params') {
      var params = Object.fromEntries(new URLSearchParams(window.location.search));
      frame.contentWindow.postMessage(['query-params', params, window.location.href, document.referrer, frame.id, {consent:null,isConsentExpected:false}], formOrigin);
    } else if (message[0] === 'fetch-sticky-contacts') {
      frame.contentWindow.postMessage(['sticky-contacts', contact, null], formOrigin);
    } else if (message[0] === 'highlevel.setHeight' && message[1]) {
      var height = Number(message[1].height);
      if (Number.isFinite(height) && height > 200 && height < 3000) frame.style.height = height + 'px';
    } else if (step === 'lead' && message[0] === 'set-sticky-contacts' && message[1] === '_ud' && typeof message[2] === 'string' && message[4]) {
      // This provider event is emitted after the form API confirms a saved contact.
      try {
        var data = JSON.parse(message[2]);
        if (data && typeof data === 'object' && !Array.isArray(data)) schedule(data);
      } catch (_) { /* A malformed message must never advance the flow. */ }
    }
  });
})();
