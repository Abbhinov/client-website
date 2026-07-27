/* =========================================================
   Cool & Cozy AC Repair — main.js
   - Loads HTML partials marked with [data-include]
   - Initializes interactive components after partials are in
   ========================================================= */

(function () {
  'use strict';

  /* ------------------------------------------------------------------
     Partial loader.
     Usage: <div data-include="partials/header.html"></div>
     The placeholder element is replaced by the partial's content.
     Supports nested partials (one extra pass after first load).
     ------------------------------------------------------------------ */
  async function loadPartials(root = document) {
    const placeholders = [...root.querySelectorAll('[data-include]')];
    if (placeholders.length === 0) return false;

    await Promise.all(
      placeholders.map(async (el) => {
        const url = el.getAttribute('data-include');
        try {
          const res = await fetch(url, { cache: 'no-cache' });
          if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
          const html = await res.text();
          // Replace the placeholder element with the partial's HTML
          const tpl = document.createElement('template');
          tpl.innerHTML = html.trim();
          el.replaceWith(tpl.content);
        } catch (err) {
          console.error('[partial] failed:', url, err);
          el.innerHTML =
            '<!-- partial failed to load: ' + url + ' (run via local server) -->';
        }
      })
    );
    return true;
  }

  /* ------------------------------------------------------------------
     Emergency banner — dismiss persists for the session
     ------------------------------------------------------------------ */
  function initBanner() {
    const banner = document.getElementById('emergency-banner');
    if (!banner) return;
    if (sessionStorage.getItem('bannerDismissed') === '1') {
      banner.style.display = 'none';
      return;
    }
    const btn = banner.querySelector('[data-banner-dismiss]');
    if (!btn) return;
    btn.addEventListener('click', () => {
      banner.classList.add('is-dismissing');
      sessionStorage.setItem('bannerDismissed', '1');
      setTimeout(() => { banner.style.display = 'none'; }, 320);
    });
  }

  /* ------------------------------------------------------------------
     Header — sticky shadow on scroll
     ------------------------------------------------------------------ */
  function initHeader() {
    const nav = document.querySelector('.main-nav');
    if (!nav) return;
    let scrolled = false;
    const onScroll = () => {
      const isScrolled = window.scrollY > 80;
      if (isScrolled !== scrolled) {
        scrolled = isScrolled;
        nav.classList.toggle('is-scrolled', scrolled);
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ------------------------------------------------------------------
     Mobile nav overlay + sub-menu accordions
     ------------------------------------------------------------------ */
  function initMobileNav() {
    const trigger = document.querySelector('[data-mobile-nav-open]');
    const overlay = document.getElementById('mobile-nav');
    if (!trigger || !overlay) return;
    const closeBtn = overlay.querySelector('[data-mobile-nav-close]');

    const open = () => {
      overlay.classList.add('is-open');
      trigger.setAttribute('aria-expanded', 'true');
      document.body.classList.add('no-scroll');
      // Move focus into the overlay
      setTimeout(() => closeBtn?.focus(), 50);
    };
    const close = () => {
      overlay.classList.remove('is-open');
      trigger.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('no-scroll');
      trigger.focus();
    };

    trigger.addEventListener('click', open);
    closeBtn?.addEventListener('click', close);

    // Close on Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && overlay.classList.contains('is-open')) close();
    });

    // Close when an inner link is clicked
    overlay.querySelectorAll('a[href]').forEach((a) => {
      a.addEventListener('click', () => {
        // Tiny delay so the navigation is felt; not strictly required
        setTimeout(close, 50);
      });
    });

    // Sub-menu accordions inside the overlay
    overlay.querySelectorAll('[data-submenu-toggle]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const target = btn.nextElementSibling;
        const expanded = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!expanded));
        target?.classList.toggle('is-open', !expanded);
      });
    });
  }

  /* ------------------------------------------------------------------
     FAQ accordion — one open at a time, first open by default
     ------------------------------------------------------------------ */
  function initFaq() {
    const items = [...document.querySelectorAll('.faq-item')];
    if (items.length === 0) return;

    items.forEach((item, i) => {
      const btn = item.querySelector('.faq-item__q');
      const panel = item.querySelector('.faq-item__a');
      if (!btn || !panel) return;

      // Wire ARIA
      const id = 'faq-panel-' + i;
      panel.id = id;
      btn.setAttribute('aria-controls', id);
      btn.setAttribute('aria-expanded', i === 0 ? 'true' : 'false');
      if (i === 0) item.classList.add('is-open');

      btn.addEventListener('click', () => {
        const isOpen = item.classList.contains('is-open');
        items.forEach((other) => {
          other.classList.remove('is-open');
          other.querySelector('.faq-item__q')?.setAttribute('aria-expanded', 'false');
        });
        if (!isOpen) {
          item.classList.add('is-open');
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });
  }

  /* ------------------------------------------------------------------
     Testimonials carousel — manual + auto-advance, responsive
     ------------------------------------------------------------------ */
  function initTestimonials() {
    const root = document.querySelector('[data-testimonials]');
    if (!root) return;
    const track = root.querySelector('.testimonials__track');
    const cards = [...root.querySelectorAll('.testimonial-card')];
    const prev = root.querySelector('[data-testimonials-prev]');
    const next = root.querySelector('[data-testimonials-next]');
    const dotsContainer = root.querySelector('[data-testimonials-dots]');
    if (!track || cards.length === 0) return;

    let perView = 3;
    let idx = 0;
    let timer = null;

    const computePerView = () => {
      const w = window.innerWidth;
      if (w < 640) return 1;
      if (w < 1024) return 2;
      return 3;
    };

    const totalPages = () => Math.max(1, cards.length - perView + 1);

    const renderDots = () => {
      if (!dotsContainer) return;
      dotsContainer.innerHTML = '';
      for (let i = 0; i < totalPages(); i++) {
        const d = document.createElement('button');
        d.className = 'testimonials__dot' + (i === idx ? ' is-active' : '');
        d.type = 'button';
        d.setAttribute('aria-label', 'Go to slide ' + (i + 1));
        d.addEventListener('click', () => { idx = i; render(); restartTimer(); });
        dotsContainer.appendChild(d);
      }
    };

    const render = () => {
      const cardWidth = cards[0].getBoundingClientRect().width;
      const gap = parseFloat(getComputedStyle(track).gap) || 24;
      track.style.transform = 'translateX(-' + (idx * (cardWidth + gap)) + 'px)';
      const dots = dotsContainer ? [...dotsContainer.children] : [];
      dots.forEach((d, i) => d.classList.toggle('is-active', i === idx));
      if (prev) prev.disabled = idx === 0;
      if (next) next.disabled = idx >= totalPages() - 1;
    };

    const goPrev = () => { idx = Math.max(0, idx - 1); render(); restartTimer(); };
    const goNext = () => { idx = Math.min(totalPages() - 1, idx + 1); render(); restartTimer(); };

    prev?.addEventListener('click', goPrev);
    next?.addEventListener('click', goNext);

    const startTimer = () => {
      stopTimer();
      timer = setInterval(() => {
        idx = (idx + 1) % totalPages();
        render();
      }, 6000);
    };
    const stopTimer = () => { if (timer) { clearInterval(timer); timer = null; } };
    const restartTimer = () => { startTimer(); };

    root.addEventListener('mouseenter', stopTimer);
    root.addEventListener('mouseleave', startTimer);
    root.addEventListener('focusin', stopTimer);
    root.addEventListener('focusout', startTimer);

    // Touch swipe
    let touchStartX = 0;
    track.addEventListener('touchstart', (e) => {
      touchStartX = e.touches[0].clientX;
      stopTimer();
    }, { passive: true });
    track.addEventListener('touchend', (e) => {
      const dx = e.changedTouches[0].clientX - touchStartX;
      if (Math.abs(dx) > 40) (dx < 0 ? goNext : goPrev)();
      else startTimer();
    });

    // Resize handling
    let resizeT;
    window.addEventListener('resize', () => {
      clearTimeout(resizeT);
      resizeT = setTimeout(() => {
        const newPv = computePerView();
        if (newPv !== perView) {
          perView = newPv;
          idx = Math.min(idx, totalPages() - 1);
          renderDots();
        }
        render();
      }, 100);
    });

    perView = computePerView();
    renderDots();
    render();
    startTimer();
  }

  /* ------------------------------------------------------------------
     Sticky mobile CTA — visible after scrolling, hidden over footer
     ------------------------------------------------------------------ */
  function initStickyCTA() {
    const cta = document.querySelector('.mobile-cta');
    if (!cta) return;
    document.body.classList.add('has-mobile-cta');

    const footer = document.querySelector('.site-footer');
    const onScroll = () => {
      if (window.innerWidth >= 768) {
        cta.classList.remove('is-visible');
        return;
      }
      const past = window.scrollY > 200;
      let footerVisible = false;
      if (footer) {
        const rect = footer.getBoundingClientRect();
        footerVisible = rect.top < window.innerHeight - 32;
      }
      cta.classList.toggle('is-visible', past && !footerVisible);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    onScroll();
  }

  /* ------------------------------------------------------------------
     Contact form — only initialises if the form exists on the page
     ------------------------------------------------------------------ */
  function initContactForm() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    const serviceSelect = form.querySelector('[name="service"]');
    const propertySelect = form.querySelector('[name="property_type"]');
    const unitsField = form.querySelector('[data-conditional="multi-unit"]');
    const emergencyAlert = form.querySelector('.form-emergency-alert');
    const success = document.querySelector('.form-success');
    const submitBtn = form.querySelector('button[type="submit"]');

    // 1. Pre-select service from ?service= URL param
    const params = new URLSearchParams(window.location.search);
    const svc = params.get('service');
    if (svc && serviceSelect) {
      const opt = serviceSelect.querySelector('option[value="' + svc + '"]');
      if (opt) {
        serviceSelect.value = svc;
        // trigger change so emergency/conditional handlers run
        serviceSelect.dispatchEvent(new Event('change'));
      }
    }

    // 2. Emergency alert toggle on service change
    serviceSelect?.addEventListener('change', () => {
      const isEmergency = serviceSelect.value === 'emergency-ac-repair';
      emergencyAlert?.classList.toggle('is-visible', isEmergency);
    });

    // 3. Conditional "Number of Units" field
    propertySelect?.addEventListener('change', () => {
      const isMulti = propertySelect.value === 'multi-unit';
      unitsField?.classList.toggle('is-visible', isMulti);
      const inp = unitsField?.querySelector('input');
      if (inp) inp.required = isMulti;
    });

    // 4. Inline validation on blur
    const requireds = form.querySelectorAll('[required]');
    requireds.forEach((el) => {
      el.addEventListener('blur', () => validateField(el));
    });

    function validateField(el) {
      const wrap = el.closest('.field');
      if (!wrap) return true;
      const errEl = wrap.querySelector('.field__error');
      let msg = '';
      if (!el.value || (el.type === 'select-one' && !el.value)) {
        msg = errEl?.dataset.errorRequired || 'This field is required.';
      } else if (el.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value)) {
        msg = errEl?.dataset.errorEmail || 'Please enter a valid email address.';
      } else if (el.type === 'tel') {
        const digits = el.value.replace(/\D/g, '');
        if (digits.length < 10) msg = errEl?.dataset.errorTel || 'Please enter a valid 10-digit phone number.';
      }
      if (msg) {
        wrap.classList.add('field--error');
        if (errEl) errEl.textContent = msg;
        return false;
      }
      wrap.classList.remove('field--error');
      return true;
    }

    // 5. Submit handler — front-end only, no real backend
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      // Honeypot — silent reject if filled
      const honeypot = form.querySelector('[name="website"]');
      if (honeypot && honeypot.value) return;

      // Validate all required fields
      let ok = true;
      requireds.forEach((el) => {
        if (!validateField(el)) ok = false;
      });
      if (!ok) {
        const firstError = form.querySelector('.field--error [required]');
        firstError?.focus();
        return;
      }

      // Disable button and pretend to submit
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending…';
      }

      // Simulate latency, then swap form for success state
      setTimeout(() => {
        const isEmergency = serviceSelect?.value === 'emergency-ac-repair';
        if (success) {
          const heading = success.querySelector('[data-success-heading]');
          const message = success.querySelector('[data-success-message]');
          if (isEmergency && heading && message) {
            heading.textContent = 'Request Flagged as Urgent';
            message.innerHTML = 'For the fastest response, call <a href="tel:+19045550199">(904) 555-0199</a> right now &mdash; emergency calls are always prioritized.';
          }
          form.style.display = 'none';
          success.classList.add('is-visible');
          success.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 600);
    });
  }

  /* ------------------------------------------------------------------
     Language switcher — persists manual choice so auto-detect respects it.
     Writes both localStorage (read by the in-page fallback script) and a
     cookie scoped to .coolcozyac.com (read by the Cloudflare Worker from
     either the apex or es subdomain).
     ------------------------------------------------------------------ */
  function initLangSwitcher() {
    const anchors = document.querySelectorAll('a[data-lang]');
    if (anchors.length === 0) return;

    anchors.forEach((a) => {
      a.addEventListener('click', () => {
        const lang = a.getAttribute('data-lang');
        if (lang !== 'en' && lang !== 'es') return;
        try { localStorage.setItem('lang-preference', lang); } catch (e) {}
        const oneYear = 60 * 60 * 24 * 365;
        const domainAttr = location.hostname.endsWith('coolcozyac.com')
          ? '; domain=.coolcozyac.com' : '';
        document.cookie = 'lang-preference=' + lang + '; path=/' + domainAttr +
          '; max-age=' + oneYear + '; SameSite=Lax';
      });
    });
  }

  /* ------------------------------------------------------------------
     Mark active nav link by current path
     ------------------------------------------------------------------ */
  function highlightActiveNav() {
    const path = location.pathname.replace(/\/$/, '') || '/';
    document.querySelectorAll('[data-nav-link]').forEach((a) => {
      const href = a.getAttribute('href').replace(/\/$/, '') || '/';
      if (href === path) a.classList.add('is-active');
    });
  }

  /* ------------------------------------------------------------------
     Boot
     ------------------------------------------------------------------ */
  async function boot() {
    // First pass: load partials referenced by the page
    await loadPartials();
    // Second pass: in case any partial itself contains another data-include
    await loadPartials();

    initBanner();
    initHeader();
    initMobileNav();
    initFaq();
    initTestimonials();
    initStickyCTA();
    initContactForm();
    initLangSwitcher();
    highlightActiveNav();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
