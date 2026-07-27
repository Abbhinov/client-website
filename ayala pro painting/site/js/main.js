/* =========================================================================
   AYALA PRO PAINTING — main.js
   - Loads reusable header/footer partials (single source of truth)
   - Wires global behavior: nav, dropdowns, sticky header, sticky CTA,
     announcement dismiss, FAQ accordion, GA4 event hooks.
   ========================================================================= */
(function () {
  'use strict';

  /* -----------------------------------------------------------------------
     GA4 helper — safe no-op if gtag/dataLayer absent
     ----------------------------------------------------------------------- */
  function track(event, params) {
    params = params || {};
    if (typeof window.gtag === 'function') {
      window.gtag('event', event, params);
    } else {
      (window.dataLayer = window.dataLayer || []).push(Object.assign({ event: event }, params));
    }
  }
  function deviceType() {
    return window.matchMedia('(max-width: 768px)').matches ? 'mobile' : 'desktop';
  }

  /* Relative prefix from the current file to the site root.
     Static GCS bucket has no server routing, so internal links generated in JS
     must be relative to the page's folder depth (e.g. ../ or ../../). */
  function rootPrefix() {
    var parts = location.pathname.split('/').filter(Boolean);
    var endsSlash = location.pathname.charAt(location.pathname.length - 1) === '/';
    var depth = endsSlash ? parts.length : Math.max(0, parts.length - 1);
    return depth ? new Array(depth + 1).join('../') : './';
  }

  /* -----------------------------------------------------------------------
     1. Announcement bar — dismiss with 7-day localStorage memory
     ----------------------------------------------------------------------- */
  function initAnnouncement() {
    var bar = document.getElementById('announcement-bar');
    if (!bar) return;
    var KEY = 'announcement_dismissed';
    var SEVEN_DAYS = 7 * 24 * 60 * 60 * 1000;

    try {
      var ts = parseInt(localStorage.getItem(KEY), 10);
      if (ts && (Date.now() - ts) < SEVEN_DAYS) { bar.hidden = true; }
    } catch (e) { /* localStorage unavailable */ }

    var close = bar.querySelector('.announcement-bar__close');
    if (close) {
      close.addEventListener('click', function () {
        bar.hidden = true;
        try { localStorage.setItem(KEY, String(Date.now())); } catch (e) {}
        track('announcement_dismiss', { announcement_text: 'south_hillsborough_estimate' });
      });
    }
  }

  /* -----------------------------------------------------------------------
     3. Sticky header shadow on scroll (throttled)
     ----------------------------------------------------------------------- */
  function initStickyHeader() {
    var header = document.getElementById('site-header');
    if (!header) return;
    var ticking = false;
    function onScroll() {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        header.classList.toggle('header--scrolled', window.scrollY > 200);
        ticking = false;
      });
    }
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* -----------------------------------------------------------------------
     4. Mobile navigation + dropdown accordions + active link highlight
     ----------------------------------------------------------------------- */
  function initNav() {
    var hamburger = document.querySelector('.header__hamburger');
    var nav = document.getElementById('main-nav');
    var backdrop = document.getElementById('nav-backdrop');
    if (!hamburger || !nav) return;

    function openNav() {
      nav.classList.add('is-open');
      hamburger.setAttribute('aria-expanded', 'true');
      if (backdrop) { backdrop.hidden = false; backdrop.classList.add('is-open'); }
    }
    function closeNav() {
      nav.classList.remove('is-open');
      hamburger.setAttribute('aria-expanded', 'false');
      if (backdrop) { backdrop.classList.remove('is-open'); backdrop.hidden = true; }
    }
    hamburger.addEventListener('click', function () {
      nav.classList.contains('is-open') ? closeNav() : openNav();
    });
    if (backdrop) backdrop.addEventListener('click', closeNav);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeNav();
    });

    // Dropdown toggles (click on mobile / keyboard everywhere)
    var dropdowns = document.querySelectorAll('.header__nav-item--dropdown');
    Array.prototype.forEach.call(dropdowns, function (item) {
      var link = item.querySelector('.header__nav-link');
      var menu = item.querySelector('.header__dropdown');
      if (!link || !menu) return;
      link.addEventListener('click', function (e) {
        // On mobile, first tap expands the submenu instead of navigating.
        if (window.matchMedia('(max-width: 768px)').matches) {
          e.preventDefault();
          var open = menu.classList.toggle('is-open');
          link.setAttribute('aria-expanded', String(open));
        }
      });
    });

    // Active link highlight based on current path
    var path = window.location.pathname;
    Array.prototype.forEach.call(document.querySelectorAll('.header__nav-item[data-path]'), function (item) {
      var p = item.getAttribute('data-path');
      if (p !== '/' && path.indexOf(p) !== -1) item.classList.add('header__nav-item--active');
    });
  }

  /* -----------------------------------------------------------------------
     5. Mobile sticky CTA — show after hero, hide over footer
     ----------------------------------------------------------------------- */
  function initStickyCta() {
    var bar = document.getElementById('sticky-cta');
    if (!bar) return;
    if (!window.matchMedia('(max-width: 768px)').matches) return;

    document.body.classList.add('has-sticky-cta');
    var hero = document.querySelector('.hero, [data-hero]');
    var footer = document.querySelector('.footer');
    var pastHero = false, atFooter = false;

    function update() {
      bar.classList.toggle('sticky-cta--visible', pastHero && !atFooter);
    }
    if ('IntersectionObserver' in window) {
      if (hero) {
        new IntersectionObserver(function (entries) {
          pastHero = !entries[0].isIntersecting;
          update();
        }, { rootMargin: '0px' }).observe(hero);
      } else { pastHero = true; }
      if (footer) {
        new IntersectionObserver(function (entries) {
          atFooter = entries[0].isIntersecting;
          update();
        }).observe(footer);
      }
    } else {
      bar.classList.add('sticky-cta--visible');
    }
  }

  /* -----------------------------------------------------------------------
     6. FAQ accordion — one open at a time, keyboard accessible
     ----------------------------------------------------------------------- */
  function initFaq() {
    var items = document.querySelectorAll('.faq__item');
    Array.prototype.forEach.call(items, function (item) {
      var btn = item.querySelector('.faq__question');
      var answer = item.querySelector('.faq__answer');
      if (!btn || !answer) return;
      btn.addEventListener('click', function () {
        var isOpen = item.classList.contains('is-open');
        // Close all
        Array.prototype.forEach.call(items, function (other) {
          other.classList.remove('is-open');
          var b = other.querySelector('.faq__question');
          var a = other.querySelector('.faq__answer');
          if (b) b.setAttribute('aria-expanded', 'false');
          if (a) a.style.maxHeight = null;
        });
        if (!isOpen) {
          item.classList.add('is-open');
          btn.setAttribute('aria-expanded', 'true');
          answer.style.maxHeight = answer.scrollHeight + 'px';
          track('faq_expand', { question_text: btn.textContent.trim(), page_section: 'faq' });
        }
      });
    });
  }

  /* -----------------------------------------------------------------------
     7. Testimonial carousel dots
     ----------------------------------------------------------------------- */
  function initCarousel() {
    var track = document.querySelector('.testimonials__track');
    var dotsWrap = document.querySelector('.testimonials__dots');
    if (!track || !dotsWrap) return;
    var cards = track.querySelectorAll('.testimonial-card');
    Array.prototype.forEach.call(cards, function (card, i) {
      var dot = document.createElement('button');
      dot.className = 'carousel-dot';
      dot.type = 'button';
      dot.setAttribute('aria-label', 'Go to testimonial ' + (i + 1));
      dot.addEventListener('click', function () {
        card.scrollIntoView({ behavior: 'smooth', inline: 'start', block: 'nearest' });
      });
      dotsWrap.appendChild(dot);
    });
  }

  /* -----------------------------------------------------------------------
     7b. Estimate form — inline validation, honeypot, on-page success, GA4
     ----------------------------------------------------------------------- */
  function initEstimateForm() {
    var form = document.getElementById('estimate-form');
    if (!form) return;

    var banner = form.querySelector('.form-banner');
    var submitBtn = form.querySelector('button[type="submit"]');
    var started = false;

    function fieldError(field) {
      if (!field.value && field.hasAttribute('required')) return 'This field is required.';
      if (field.type === 'email' && field.value && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(field.value)) return 'Enter a valid email address.';
      if (field.type === 'tel' && field.value && !/^\d{10}$/.test(field.value.replace(/\D/g, ''))) return 'Enter a 10-digit phone number.';
      if (field.minLength > 0 && field.value && field.value.length < field.minLength) return 'Please enter at least ' + field.minLength + ' characters.';
      return '';
    }
    function showError(field, msg) {
      var group = field.closest('.form-group');
      if (!group) return;
      var slot = group.querySelector('.form-error');
      group.classList.toggle('has-error', !!msg);
      field.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (slot) slot.textContent = msg;
    }

    // Inline validation on blur
    Array.prototype.forEach.call(form.querySelectorAll('input, select, textarea'), function (field) {
      if (field.name === 'website') return; // honeypot
      field.addEventListener('blur', function () { showError(field, fieldError(field)); });
      field.addEventListener('focus', function () {
        if (!started) {
          started = true;
          track('form_start', { form_id: 'estimate-form', page_url: window.location.pathname });
        }
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Honeypot: silently drop bot submissions
      var hp = form.querySelector('[name="website"]');
      if (hp && hp.value) return;

      // Validate all required/typed fields
      var firstInvalid = null;
      Array.prototype.forEach.call(form.querySelectorAll('input, select, textarea'), function (field) {
        if (field.name === 'website') return;
        var msg = fieldError(field);
        showError(field, msg);
        if (msg && !firstInvalid) firstInvalid = field;
      });
      // Required radio group (preferred contact)
      var radios = form.querySelectorAll('input[name="contact_method"]');
      if (radios.length) {
        var chosen = Array.prototype.some.call(radios, function (r) { return r.checked; });
        var radioGroup = radios[0].closest('.form-group');
        if (radioGroup) {
          radioGroup.classList.toggle('has-error', !chosen);
          var slot = radioGroup.querySelector('.form-error');
          if (slot) slot.textContent = chosen ? '' : 'Please choose a contact method.';
        }
        if (!chosen && !firstInvalid) firstInvalid = radios[0];
      }
      if (firstInvalid) { firstInvalid.focus(); return; }

      // Disable to prevent duplicate submission
      submitBtn.disabled = true;
      var originalText = submitBtn.textContent;
      submitBtn.textContent = 'Sending…';
      if (banner) banner.hidden = true;

      var data = Object.fromEntries(new FormData(form).entries());

      // [PLACEHOLDER] Wire to Formspree/Basin/Cloud Function endpoint.
      // No endpoint configured yet → simulate success so UX is testable.
      var endpoint = form.getAttribute('data-endpoint');
      var request = endpoint
        ? fetch(endpoint, { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form) })
            .then(function (r) { if (!r.ok) throw new Error('bad status'); })
        : Promise.resolve();

      request.then(function () {
        track('form_submit', {
          service_type: data.service || '',
          contact_method: data.contact_method || '',
          source_page: '/contact/'
        });
        showSuccess(data.name || 'there');
      }).catch(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
        if (banner) { banner.hidden = false; banner.focus && banner.focus(); }
      });
    });

    function showSuccess(name) {
      var success = document.createElement('div');
      success.className = 'form-success';
      success.setAttribute('role', 'status');
      success.innerHTML =
        '<svg class="form-success__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>' +
        '<h2>Thank You, ' + escapeHtml(name) + '!</h2>' +
        '<p>We&rsquo;ve received your estimate request and will contact you within 24&ndash;48 hours via your preferred method.</p>' +
        '<p style="margin-top:24px"><a class="btn btn--secondary" href="' + rootPrefix() + 'gallery/index.html">In the meantime, explore our recent work</a></p>';
      form.replaceWith(success);
      success.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    function escapeHtml(s) {
      return String(s).replace(/[&<>"']/g, function (c) {
        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
      });
    }
  }

  /* -----------------------------------------------------------------------
     7c. Resource category filter (Resources hub)
     ----------------------------------------------------------------------- */
  function initResourceFilter() {
    var bar = document.querySelector('.filter-bar');
    var grid = document.querySelector('.resource-grid');
    if (!bar || !grid) return;
    var pills = bar.querySelectorAll('.filter-pill');
    var cards = grid.querySelectorAll('.resource-card');
    bar.addEventListener('click', function (e) {
      var pill = e.target.closest('.filter-pill');
      if (!pill) return;
      var filter = pill.getAttribute('data-filter');
      pills.forEach(function (p) { p.classList.toggle('is-active', p === pill); });
      cards.forEach(function (card) {
        var cat = card.getAttribute('data-category');
        card.hidden = !(filter === 'all' || cat === filter);
      });
    });
  }

  /* -----------------------------------------------------------------------
     7d. Gallery — category filter + accessible lightbox
     ----------------------------------------------------------------------- */
  function initGallery() {
    var grid = document.querySelector('.gallery-grid');
    if (!grid) return;
    var items = Array.prototype.slice.call(grid.querySelectorAll('.gallery-item'));

    // Filter
    var bar = document.querySelector('.gallery-filter');
    if (bar) {
      bar.addEventListener('click', function (e) {
        var pill = e.target.closest('.filter-pill');
        if (!pill) return;
        var f = pill.getAttribute('data-filter');
        bar.querySelectorAll('.filter-pill').forEach(function (p) { p.classList.toggle('is-active', p === pill); });
        items.forEach(function (it) {
          it.hidden = !(f === 'all' || it.getAttribute('data-category') === f);
        });
        track('gallery_filter', { filter_category: f });
      });
    }

    // Lightbox
    var box = document.createElement('div');
    box.className = 'lightbox';
    box.hidden = true;
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.setAttribute('aria-label', 'Project image viewer');
    box.innerHTML =
      '<button class="lightbox__btn lightbox__close" aria-label="Close">✕</button>' +
      '<button class="lightbox__btn lightbox__prev" aria-label="Previous">‹</button>' +
      '<img class="lightbox__img" alt="">' +
      '<button class="lightbox__btn lightbox__next" aria-label="Next">›</button>' +
      '<div class="lightbox__caption"><strong></strong><span></span></div>';
    document.body.appendChild(box);
    var lbImg = box.querySelector('.lightbox__img');
    var lbTitle = box.querySelector('.lightbox__caption strong');
    var lbDetail = box.querySelector('.lightbox__caption span');
    var current = 0, trigger = null;

    function visibleItems() { return items.filter(function (it) { return !it.hidden; }); }
    function show(i) {
      var vis = visibleItems();
      if (!vis.length) return;
      current = (i + vis.length) % vis.length;
      var it = vis[current];
      lbImg.src = it.getAttribute('data-full');
      lbImg.alt = it.querySelector('img') ? it.querySelector('img').alt : '';
      lbTitle.textContent = it.getAttribute('data-caption') || '';
      lbDetail.textContent = it.getAttribute('data-detail') || '';
      track('gallery_view', { project_type: it.getAttribute('data-category'), image_index: current });
    }
    function open(it) {
      trigger = it;
      var vis = visibleItems();
      show(vis.indexOf(it));
      box.hidden = false;
      document.body.style.overflow = 'hidden';
      box.querySelector('.lightbox__close').focus();
    }
    function close() {
      box.hidden = true;
      document.body.style.overflow = '';
      if (trigger) trigger.focus();
    }
    items.forEach(function (it) {
      it.addEventListener('click', function () { open(it); });
    });
    box.querySelector('.lightbox__close').addEventListener('click', close);
    box.querySelector('.lightbox__prev').addEventListener('click', function () { show(current - 1); });
    box.querySelector('.lightbox__next').addEventListener('click', function () { show(current + 1); });
    box.addEventListener('click', function (e) { if (e.target === box) close(); });
    document.addEventListener('keydown', function (e) {
      if (box.hidden) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') show(current - 1);
      else if (e.key === 'ArrowRight') show(current + 1);
    });
  }

  /* -----------------------------------------------------------------------
     8. Global click delegation for GA4 events (phone / cta / outbound / email)
     ----------------------------------------------------------------------- */
  function initTracking() {
    document.addEventListener('click', function (e) {
      var phone = e.target.closest('[data-phone]');
      if (phone) {
        track('phone_click', {
          phone_number: '(813) 555-0199',
          page_url: window.location.pathname,
          page_section: phone.getAttribute('data-section') || sectionOf(phone),
          device_type: deviceType()
        });
      }
      var cta = e.target.closest('[data-cta]');
      if (cta) {
        track('cta_click', {
          button_text: (cta.textContent || '').trim(),
          destination_url: cta.getAttribute('href') || '',
          page_section: cta.getAttribute('data-cta')
        });
      }
      var out = e.target.closest('[data-outbound]');
      if (out) {
        track('outbound_click', {
          destination_url: out.getAttribute('href') || '',
          link_text: out.getAttribute('aria-label') || ''
        });
      }
      var mail = e.target.closest('a[href^="mailto:"]');
      if (mail) {
        track('email_click', { page_section: sectionOf(mail) });
      }
    });

    // Scroll depth 75%
    var fired = false;
    window.addEventListener('scroll', function () {
      if (fired) return;
      var scrolled = (window.scrollY + window.innerHeight) / document.body.scrollHeight;
      if (scrolled >= 0.75) {
        fired = true;
        track('scroll_75', { page_url: window.location.pathname, page_title: document.title });
      }
    }, { passive: true });
  }

  function sectionOf(el) {
    var sec = el.closest('[data-section], section, header, footer');
    if (!sec) return 'unknown';
    if (sec.getAttribute && sec.getAttribute('data-section')) return sec.getAttribute('data-section');
    return sec.id || sec.tagName.toLowerCase();
  }

  /* -----------------------------------------------------------------------
     Boot
     ----------------------------------------------------------------------- */
  function init() {
    initAnnouncement();
    initStickyHeader();
    initNav();
    initStickyCta();
    initFaq();
    initCarousel();
    initEstimateForm();
    initResourceFilter();
    initGallery();
    initTracking();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
