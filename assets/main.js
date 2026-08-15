/* My BnB Accelerator -- site behavior */
(function () {
  'use strict';

  var doc = document;

  /* ---------------------------------------------- Sticky header state -- */
  var header = doc.querySelector('.site-header');
  if (header) {
    var startsTransparent = header.getAttribute('data-start') === 'transparent';
    var setMode = function () {
      if (!startsTransparent) {
        header.setAttribute('data-mode', 'solid');
        return;
      }
      header.setAttribute('data-mode', window.scrollY > 40 ? 'solid' : 'transparent');
    };
    setMode();
    window.addEventListener('scroll', setMode, { passive: true });
  }

  /* ------------------------------------------------------ Mobile menu -- */
  var toggle = doc.querySelector('.menu-toggle');
  var nav = doc.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.setAttribute('data-open', String(!open));
      if (header && !open) header.setAttribute('data-mode', 'solid');
      else if (header) header.dispatchEvent(new Event('recheck'));
      if (!open) doc.body.style.overflow = 'hidden';
      else doc.body.style.overflow = '';
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        toggle.setAttribute('aria-expanded', 'false');
        nav.setAttribute('data-open', 'false');
        doc.body.style.overflow = '';
      }
    });
    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.getAttribute('data-open') === 'true') {
        toggle.setAttribute('aria-expanded', 'false');
        nav.setAttribute('data-open', 'false');
        doc.body.style.overflow = '';
        toggle.focus();
      }
    });
  }

  /* ------------------------------------------------- Reveal on scroll -- */
  var revealItems = doc.querySelectorAll('[data-reveal]');
  if (revealItems.length) {
    if (!('IntersectionObserver' in window)) {
      revealItems.forEach(function (el) { el.classList.add('is-visible'); });
    } else {
      var revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            revealObserver.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      revealItems.forEach(function (el) { revealObserver.observe(el); });
    }
  }

  /* -------------------------------------------------- Counting stats -- */
  var counters = doc.querySelectorAll('[data-count]');
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function runCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    if (isNaN(target)) return;
    if (reduceMotion) { el.textContent = String(target); return; }
    var duration = 1500;
    var start = null;
    function frame(ts) {
      if (start === null) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      // easeOutExpo
      var eased = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
      el.textContent = String(Math.round(eased * target));
      if (progress < 1) requestAnimationFrame(frame);
      else el.textContent = String(target);
    }
    requestAnimationFrame(frame);
  }

  if (counters.length) {
    if (!('IntersectionObserver' in window)) {
      counters.forEach(runCount);
    } else {
      var countObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            runCount(entry.target);
            countObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });
      counters.forEach(function (el) { countObserver.observe(el); });
    }
  }

  /* ------------------------------------------------- Current year(s) -- */
  doc.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ----------------------------------------------- FAQ deep-link open -- */
  function openFromHash() {
    if (!window.location.hash) return;
    var id = window.location.hash.slice(1);
    var el = doc.getElementById(id);
    if (!el) return;
    var details = el.closest('details');
    if (details) details.open = true;
    else if (el.tagName === 'DETAILS') el.open = true;
  }
  openFromHash();
  window.addEventListener('hashchange', openFromHash);


  /* --------------------------------------------- Sticky conversion bar -- */
  /* Show once the hero CTA is gone, hide whenever a real CTA band or the
     footer is on screen so the page never presents two competing asks. */
  var sticky = doc.querySelector('[data-sticky-cta]');
  if (sticky) {
    var rivals = doc.querySelectorAll('.cta-band, .site-footer, .form-card');
    var rivalVisible = false;

    /* Declared before the observer: its first callback can fire before a
       var assignment further down would have run. */
    function updateSticky() {
      var past = window.scrollY > (window.innerHeight * 0.6);
      sticky.setAttribute('data-show', String(past && !rivalVisible));
    }

    if ('IntersectionObserver' in window && rivals.length) {
      var seen = [];
      var rivalObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          var i = seen.indexOf(entry.target);
          if (entry.isIntersecting && i === -1) seen.push(entry.target);
          else if (!entry.isIntersecting && i !== -1) seen.splice(i, 1);
        });
        rivalVisible = seen.length > 0;
        updateSticky();
      }, { threshold: 0 });
      rivals.forEach(function (el) { rivalObserver.observe(el); });
    }

    updateSticky();
    window.addEventListener('scroll', updateSticky, { passive: true });
    window.addEventListener('resize', updateSticky, { passive: true });
  }


  /* ------------------------------------------------------- Lead magnets -- */
  /* Same pattern as the application form: no backend is wired up on the
     static build, so capture locally and confirm. Swap the stub for a real
     endpoint and the markup does not change. */
  doc.querySelectorAll('form.lead-form').forEach(function (lf) {
    lf.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = doc.getElementById(lf.id + '-status');
      var btn = lf.querySelector('button[type="submit"]');
      var email = lf.querySelector('input[type="email"]');

      if (email && !email.checkValidity()) {
        if (status) {
          status.setAttribute('data-state', 'err');
          status.textContent = 'Please enter a valid email address so we can send it to you.';
        }
        email.focus();
        return;
      }

      var original = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Sending...'; }
      try {
        var data = {};
        new FormData(lf).forEach(function (v, k) { data[k] = v; });
        window.sessionStorage.setItem('bnb_lead_' + lf.id, JSON.stringify(data));
      } catch (err) { /* storage unavailable -- non-fatal */ }

      if (status) {
        status.setAttribute('data-state', 'ok');
        status.textContent = 'Thanks. We will email it to you within two to three business days.';
      }
      lf.reset();
      if (btn) { btn.disabled = false; btn.textContent = original; }
    });
  });

  /* ------------------------------------------------- Application form -- */
  var form = doc.getElementById('apply-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = doc.getElementById('form-status');
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = 'Submitting...'; }
      // No backend is wired up on the static build. Store locally and confirm,
      // so the form is usable the moment an endpoint is added.
      try {
        var data = {};
        new FormData(form).forEach(function (v, k) { data[k] = v; });
        window.sessionStorage.setItem('bnb_application', JSON.stringify(data));
      } catch (err) { /* storage unavailable -- non-fatal */ }
      if (status) {
        status.setAttribute('data-state', 'ok');
        status.textContent = 'Thanks. Your application is in. A member of our acquisitions team will reach out within one business day to schedule your strategy call.';
        status.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
      }
      form.reset();
      if (btn) { btn.disabled = false; btn.textContent = 'Submit Application'; }
    });
  }
})();
