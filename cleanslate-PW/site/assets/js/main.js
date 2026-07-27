/* =========================================================================
   Clean Slate PW — Main JavaScript
   Wires up: mobile nav, dropdowns, FAQ accordion, before/after sliders,
   testimonials carousel, scroll-state, announcement-bar dismissal,
   form validation/submission, and GA4 dataLayer events per Homepage Guide §20.

   NOTE: Header/footer partials are baked into every HTML file at build time
   (see .refactor-static.py). The data-include loader below is kept as a
   no-op safety net so any future page that still uses the include pattern
   keeps working.
   ========================================================================= */
(function () {
  "use strict";

  /* ----------------------------------------------------------------------
     Tiny helpers
     ---------------------------------------------------------------------- */
  const $  = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));
  const on = (el, evt, fn, opts) => el && el.addEventListener(evt, fn, opts);

  window.dataLayer = window.dataLayer || [];
  function track(event, params = {}) {
    window.dataLayer.push({ event, ...params });
  }
  window.csTrack = track;

  /* ----------------------------------------------------------------------
     Asset base resolver
        Computes the absolute URL of /assets/images/placeholder.svg
        based on THIS script's own location, so it works under any folder
        depth on a static bucket. Captured at script-load time (sync).
     ---------------------------------------------------------------------- */
  const PLACEHOLDER_URL = (function () {
    const s = document.currentScript;
    // Fall back to a relative guess if currentScript isn't available
    // (e.g. when the script is dynamically injected).
    if (!s || !s.src) return "assets/images/placeholder.svg";
    try {
      // s.src ends in ".../assets/js/main.js" — replace the trailing
      // "js/main.js" with "images/placeholder.svg" to land at the SVG.
      return new URL("../images/placeholder.svg", s.src).href;
    } catch (e) {
      return "assets/images/placeholder.svg";
    }
  })();

  /* ----------------------------------------------------------------------
     0. IMAGE FALLBACK
        Production HTML references real .jpg/.webp assets. While those
        photos are not yet on disk, swap any broken <img> for a neutral
        SVG placeholder so the page still renders cleanly.
     ---------------------------------------------------------------------- */
  function attachImageFallback(scope = document) {
    scope.querySelectorAll("img").forEach((img) => {
      if (img.dataset.fallbackBound) return;
      img.dataset.fallbackBound = "1";
      img.addEventListener("error", function handle() {
        if (img.src === PLACEHOLDER_URL || img.src.endsWith("/placeholder.svg")) return;
        img.src = PLACEHOLDER_URL;
      });
    });
  }
  if (document.readyState !== "loading") attachImageFallback();
  else on(document, "DOMContentLoaded", () => attachImageFallback());

  /* ----------------------------------------------------------------------
     1. PARTIALS LOADER
        Replaces <div data-include="/partials/x.html"></div> with the
        partial's HTML, then runs the init queue (so header/footer wiring
        happens AFTER injection).
     ---------------------------------------------------------------------- */
  const initQueue = [];
  window.csReady = (fn) => initQueue.push(fn);

  async function loadIncludes() {
    const nodes = $$("[data-include]");
    await Promise.all(nodes.map(async (node) => {
      const url = node.getAttribute("data-include");
      try {
        const res = await fetch(url, { credentials: "same-origin" });
        if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
        const html = await res.text();
        const wrapper = document.createElement("div");
        wrapper.innerHTML = html.trim();
        // Replace the placeholder node with the partial's top-level children
        const frag = document.createDocumentFragment();
        while (wrapper.firstChild) frag.appendChild(wrapper.firstChild);
        node.replaceWith(frag);
      } catch (err) {
        console.error("Failed to load partial:", url, err);
        node.innerHTML = `<!-- include failed: ${url} -->`;
      }
    }));
    // Bind image fallback to any images that came in via partials
    attachImageFallback();
    // Now that partials are in the DOM, run all initializers
    initQueue.forEach((fn) => { try { fn(); } catch (e) { console.error(e); } });
  }

  /* ----------------------------------------------------------------------
     2. ANNOUNCEMENT BAR — dismiss + persist 30 days
     ---------------------------------------------------------------------- */
  window.csReady(function initAnnouncement() {
    const bar = $(".announcement");
    if (!bar) return;
    const variant = bar.dataset.variant || "default";
    const key = "csAnnouncementDismissed";
    try {
      const raw = localStorage.getItem(key);
      if (raw) {
        const obj = JSON.parse(raw);
        if (obj.variant === variant && obj.until > Date.now()) {
          bar.hidden = true;
          return;
        }
      }
    } catch (e) {/* ignore */}

    const closeBtn = $(".announcement__close", bar);
    on(closeBtn, "click", () => {
      const until = Date.now() + 30 * 24 * 60 * 60 * 1000;
      try { localStorage.setItem(key, JSON.stringify({ variant, until })); } catch (e) {}
      bar.hidden = true;
    });

    on($(".announcement__cta", bar), "click", () => {
      track("announcement_bar_click", { promo_id: variant, message_variant: variant });
    });
  });

  /* ----------------------------------------------------------------------
     3. HEADER — scroll shadow + sticky offset
     ---------------------------------------------------------------------- */
  window.csReady(function initHeader() {
    const header = $(".site-header");
    if (!header) return;
    const onScroll = () => {
      header.classList.toggle("is-scrolled", window.scrollY > 20);
    };
    onScroll();
    on(window, "scroll", onScroll, { passive: true });
  });

  /* ----------------------------------------------------------------------
     4. MOBILE NAV
     ---------------------------------------------------------------------- */
  window.csReady(function initMobileNav() {
    const openBtn  = $(".hamburger");
    const closeBtn = $(".mobile-nav__close");
    if (!openBtn) return;
    const root = document.documentElement;
    const toggle = (open) => {
      root.classList.toggle("is-mobile-open", open);
      document.body.style.overflow = open ? "hidden" : "";
      openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    };
    on(openBtn, "click", () => toggle(!root.classList.contains("is-mobile-open")));
    on(closeBtn, "click", () => toggle(false));
    // Close when clicking a link inside the mobile nav
    $$(".mobile-nav a").forEach((a) => on(a, "click", () => toggle(false)));
    // Esc closes
    on(document, "keydown", (e) => {
      if (e.key === "Escape" && root.classList.contains("is-mobile-open")) toggle(false);
    });
  });

  /* ----------------------------------------------------------------------
     5. DESKTOP DROPDOWNS — keyboard support (click toggles for touch+kb)
     ---------------------------------------------------------------------- */
  window.csReady(function initDropdowns() {
    $$(".primary-nav__item.has-menu > .primary-nav__link").forEach((trigger) => {
      const parent = trigger.parentElement;
      on(trigger, "click", (e) => {
        // Only intercept on devices where hover doesn't apply (touch / kb-only)
        if (window.matchMedia("(hover: none)").matches || e.detail === 0) {
          e.preventDefault();
          const open = parent.classList.toggle("is-open");
          trigger.setAttribute("aria-expanded", open ? "true" : "false");
        }
      });
    });
    // Close on outside click
    on(document, "click", (e) => {
      $$(".primary-nav__item.is-open").forEach((item) => {
        if (!item.contains(e.target)) item.classList.remove("is-open");
      });
    });
  });

  /* ----------------------------------------------------------------------
     6. SERVICE / RESOURCE CARD CLICK TRACKING
     ---------------------------------------------------------------------- */
  window.csReady(function initCardTracking() {
    $$(".service-card").forEach((card) => {
      on(card, "click", () => {
        track("service_card_click", {
          service_name: card.dataset.service || card.querySelector("h3")?.textContent?.trim(),
          service_url: card.getAttribute("href")
        });
      });
    });
    $$("[data-cta]").forEach((el) => {
      on(el, "click", () => {
        track("cta_click", {
          cta_label: el.textContent.trim(),
          cta_location: el.dataset.cta,
          cta_target_url: el.getAttribute("href") || el.dataset.target || ""
        });
      });
    });
    $$('a[href^="tel:"]').forEach((a) => {
      on(a, "click", () => {
        track("phone_click", {
          phone_number: a.getAttribute("href").replace("tel:", ""),
          click_location: a.dataset.loc || "unknown"
        });
      });
    });
  });

  /* ----------------------------------------------------------------------
     7. FAQ ACCORDION
     ---------------------------------------------------------------------- */
  window.csReady(function initFAQ() {
    $$(".faq__q").forEach((btn) => {
      on(btn, "click", () => {
        const item = btn.closest(".faq__item");
        const panel = $(".faq__a", item);
        const expanded = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", expanded ? "false" : "true");
        panel.style.maxHeight = expanded ? "0px" : panel.scrollHeight + "px";
        if (!expanded) {
          track("faq_expand", {
            question_text: btn.textContent.trim(),
            question_index: Number(item.dataset.index || 0)
          });
        }
      });
    });
  });

  /* ----------------------------------------------------------------------
     8. BEFORE / AFTER COMPARISON SLIDERS
     ---------------------------------------------------------------------- */
  window.csReady(function initCompareSliders() {
    $$(".compare").forEach((root, idx) => {
      const after  = root.querySelectorAll("img")[1];
      const handle = $(".compare__handle", root);
      if (!after || !handle) return;

      let dragging = false;
      const setPct = (pct) => {
        pct = Math.max(0, Math.min(100, pct));
        after.style.clipPath = `inset(0 ${100 - pct}% 0 0)`;
        handle.style.left = pct + "%";
      };
      const pctFromEvent = (e) => {
        const rect = root.getBoundingClientRect();
        const x = ("touches" in e ? e.touches[0].clientX : e.clientX) - rect.left;
        return (x / rect.width) * 100;
      };
      const onDown = (e) => { dragging = true; setPct(pctFromEvent(e)); e.preventDefault(); };
      const onMove = (e) => { if (dragging) setPct(pctFromEvent(e)); };
      const onUp   = () => {
        if (dragging) {
          track("before_after_interact", {
            project_name: root.dataset.project || `project_${idx + 1}`,
            project_index: idx + 1
          });
        }
        dragging = false;
      };

      on(root, "mousedown", onDown);
      on(window, "mousemove", onMove);
      on(window, "mouseup", onUp);
      on(root, "touchstart", onDown, { passive: false });
      on(window, "touchmove", onMove, { passive: true });
      on(window, "touchend", onUp);
      // Click to position
      on(root, "click", (e) => {
        if (e.target === handle) return;
        setPct(pctFromEvent(e));
      });
      setPct(50);
    });
  });

  /* ----------------------------------------------------------------------
     9. TESTIMONIALS CAROUSEL — 8s auto-rotate, pause on hover, dots nav
     ---------------------------------------------------------------------- */
  window.csReady(function initTestimonials() {
    const root = $(".testimonials");
    if (!root) return;
    const track = $(".testimonials__track", root);
    const items = $$(".testimonial", track);
    const dotsBox = $(".testimonials__nav", root);
    if (!track || items.length === 0) return;

    const perView = () => {
      if (window.innerWidth < 768) return 1;
      if (window.innerWidth < 1200) return 2;
      return 3;
    };
    let index = 0;
    let timer = null;

    const pages = () => Math.max(1, items.length - perView() + 1);
    const render = () => {
      const visible = perView();
      const itemW = items[0].getBoundingClientRect().width;
      const gap = parseFloat(getComputedStyle(track).gap) || 24;
      track.style.transform = `translateX(${-(itemW + gap) * index}px)`;
      $$(".testimonials__dot", dotsBox).forEach((d, i) => {
        d.classList.toggle("is-active", i === index);
      });
    };

    const buildDots = () => {
      if (!dotsBox) return;
      dotsBox.innerHTML = "";
      for (let i = 0; i < pages(); i++) {
        const b = document.createElement("button");
        b.className = "testimonials__dot";
        b.setAttribute("aria-label", `Go to testimonial ${i + 1}`);
        on(b, "click", () => { index = i; render(); restart(); });
        dotsBox.appendChild(b);
      }
    };

    const next = () => { index = (index + 1) % pages(); render(); };
    const restart = () => { clearInterval(timer); timer = setInterval(next, 8000); };

    on(root, "mouseenter", () => clearInterval(timer));
    on(root, "mouseleave", restart);
    on(window, "resize", () => { index = 0; buildDots(); render(); });

    buildDots();
    render();
    restart();
  });

  /* ----------------------------------------------------------------------
     10. SCROLL DEPTH (GA4) + Mobile sticky CTA reveal
     ---------------------------------------------------------------------- */
  window.csReady(function initScrollDepth() {
    const milestones = [25, 50, 75, 90];
    const fired = new Set();
    const hero = $(".hero");
    const onScroll = () => {
      const docH = document.documentElement.scrollHeight - window.innerHeight;
      const pct = (window.scrollY / docH) * 100;
      milestones.forEach((m) => {
        if (pct >= m && !fired.has(m)) {
          fired.add(m);
          track("scroll", { percent_scrolled: m });
        }
      });
      if (hero) {
        const past = window.scrollY > hero.offsetHeight * 0.6;
        document.body.classList.toggle("scrolled-past-hero", past);
      }
    };
    on(window, "scroll", onScroll, { passive: true });
  });

  /* ----------------------------------------------------------------------
     11. FORMS — validation, conditional fields, URL params, GA4 events
     ---------------------------------------------------------------------- */
  window.csReady(function initForms() {
    $$("form[data-form-name]").forEach((form) => initOneForm(form));
  });

  function initOneForm(form) {
    const formName = form.dataset.formName;

    // ------- form_start: first focus anywhere in the form -------
    let started = false;
    on(form, "focusin", (e) => {
      if (started) return;
      if (!e.target.matches("input, textarea, select")) return;
      started = true;
      track("form_start", { form_name: formName, field_name: e.target.name || e.target.id });
    });

    // ------- inline validation on blur -------
    $$("input, select, textarea", form).forEach((field) => {
      on(field, "blur", () => validateField(field));
      on(field, "input", () => {
        // clear error once user starts typing again
        const wrap = field.closest(".field");
        if (wrap) wrap.classList.remove("field--error");
      });
    });

    // ------- conditional fields (data-show-when="other_field=value") -------
    function refreshConditional() {
      $$("[data-show-when]", form).forEach((node) => {
        const [name, val] = node.dataset.showWhen.split("=");
        const trigger = form.querySelector(`[name="${name}"]`);
        if (!trigger) return;
        let active = false;
        if (trigger.type === "checkbox" || trigger.type === "radio") {
          active = form.querySelector(`[name="${name}"][value="${val}"]:checked`) != null;
        } else {
          active = trigger.value === val;
        }
        node.hidden = !active;
        // Inputs inside hidden conditionals shouldn't block submit
        $$("input, select, textarea", node).forEach((f) => f.disabled = !active);
      });
    }
    on(form, "change", refreshConditional);
    refreshConditional();

    // ------- URL parameter pre-fill -------
    const params = new URLSearchParams(location.search);
    params.forEach((value, key) => {
      // service=foo can match either a select option, a checkbox, or a text field
      const select = form.querySelector(`select[name="${key}"]`);
      if (select) {
        const opt = Array.from(select.options).find(o => o.value === value);
        if (opt) select.value = value;
      }
      const checkbox = form.querySelector(`[name="${key}[]"][value="${value}"], [name="services[]"][value="${value}"]`);
      if (checkbox) checkbox.checked = true;
      const text = form.querySelector(`input[name="${key}"]`);
      if (text && !select) text.value = value;
    });

    // ------- submit handler -------
    on(form, "submit", (e) => {
      e.preventDefault();

      // Honeypot: any bot that fills the trap is rejected silently
      const hp = form.querySelector('input[name="company_website"]');
      if (hp && hp.value.trim() !== "") return;

      // Validate every visible required field
      let valid = true;
      $$("input, select, textarea", form).forEach((f) => {
        if (f.disabled) return;
        if (f.closest("[data-show-when][hidden]")) return;
        if (!validateField(f)) valid = false;
      });
      // Multi-select: at least one checkbox in any group flagged required
      $$("[data-checkbox-group][data-required='true']", form).forEach((group) => {
        const checked = group.querySelectorAll("input[type='checkbox']:checked").length;
        if (checked === 0) {
          group.classList.add("field--error");
          valid = false;
        } else {
          group.classList.remove("field--error");
        }
      });

      if (!valid) {
        const firstErr = form.querySelector(".field--error");
        if (firstErr) firstErr.scrollIntoView({ behavior: "smooth", block: "center" });
        return;
      }

      // Build payload + simulate submission (real endpoint will be wired in production)
      const data = serializeForm(form);
      track("form_submit", {
        form_name: formName,
        form_destination: form.getAttribute("action") || location.pathname,
        services: data.services
      });
      // In production, swap this for a fetch() to the Cloud Functions endpoint.
      console.info(`[${formName}] submission payload`, data);

      showFormSuccess(form, data);
    });
  }

  function validateField(field) {
    const wrap = field.closest(".field");
    if (!wrap) return true;
    const err = wrap.querySelector(".field__error");
    const val = (field.value || "").trim();
    let message = "";
    if (field.required && !val) {
      message = "This field is required.";
    } else if (field.type === "email" && val && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) {
      message = "Enter a valid email address.";
    } else if (field.type === "tel" && val) {
      const digits = val.replace(/\D/g, "");
      if (digits.length < 10) message = "Enter a 10-digit US phone number.";
    } else if (field.dataset.minLength && val.length < +field.dataset.minLength) {
      message = `Must be at least ${field.dataset.minLength} characters.`;
    }
    if (message) {
      wrap.classList.add("field--error");
      if (err) err.textContent = message;
      return false;
    }
    wrap.classList.remove("field--error");
    return true;
  }

  function serializeForm(form) {
    const fd = new FormData(form);
    const out = {};
    for (const [k, v] of fd.entries()) {
      if (k.endsWith("[]") || k === "services") {
        const key = k.replace(/\[\]$/, "");
        out[key] = out[key] || [];
        out[key].push(v);
      } else {
        out[k] = v;
      }
    }
    return out;
  }

  function showFormSuccess(form, data) {
    const success = form.parentElement.querySelector(".form__success");
    if (success) {
      const tpl = success.dataset.template || "Thank you! We received your message.";
      const filled = tpl
        .replace("{name}", (data.name || "").split(" ")[0] || "there")
        .replace("{services}", Array.isArray(data.services) ? data.services.join(", ") : (data.services || "your request"))
        .replace("{address}", data.address || "your property");
      success.textContent = filled;
      success.classList.add("is-visible");
      success.scrollIntoView({ behavior: "smooth", block: "center" });
    }
    form.classList.add("is-submitted");
  }

  /* ----------------------------------------------------------------------
     Boot
     ---------------------------------------------------------------------- */
  if (document.readyState === "loading") {
    on(document, "DOMContentLoaded", loadIncludes);
  } else {
    loadIncludes();
  }
})();
