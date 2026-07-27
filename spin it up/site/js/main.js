/* =================================================================
   SPIN IT UP LAUNDRY — Shared interactions
   Header scroll state, mobile menu, FAQ accordion, sticky mobile CTA.
   Vanilla JS, no dependencies. Loaded with `defer`.
   ================================================================= */
(function () {
  "use strict";

  /* ---- 1. Header background on scroll ----
     For overlay headers (homepage), watches the hero; for solid headers,
     toggles shadow after a small scroll. */
  var header = document.querySelector(".site-header");
  if (header) {
    var hero = document.querySelector(".hero");
    if (hero && header.classList.contains("site-header--overlay")) {
      var io = new IntersectionObserver(function (entries) {
        header.classList.toggle("is-scrolled", !entries[0].isIntersecting);
      }, { rootMargin: "-" + (header.offsetHeight + 10) + "px 0px 0px 0px", threshold: 0 });
      io.observe(hero);
    } else {
      var onScroll = function () {
        header.classList.toggle("is-scrolled", window.scrollY > 8);
      };
      onScroll();
      window.addEventListener("scroll", onScroll, { passive: true });
    }
  }

  /* ---- 2. Mobile menu ---- */
  var menu = document.querySelector(".mobile-menu");
  var openBtn = document.querySelector(".nav-toggle");
  var closeBtn = document.querySelector(".mobile-menu__close");

  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("is-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (openBtn) openBtn.setAttribute("aria-expanded", String(open));
    if (open) {
      var firstLink = menu.querySelector("a, button");
      if (firstLink) firstLink.focus();
    } else if (openBtn) {
      openBtn.focus();
    }
  }
  if (openBtn) openBtn.addEventListener("click", function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setMenu(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && menu && menu.classList.contains("is-open")) setMenu(false);
  });

  /* Mobile sub-menu accordions */
  document.querySelectorAll(".mobile-menu__sub-toggle").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var sub = btn.nextElementSibling;
      var open = sub.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", String(open));
    });
  });

  /* ---- 3. FAQ accordion ---- */
  document.querySelectorAll(".faq__q").forEach(function (btn) {
    var panel = btn.nextElementSibling;
    btn.addEventListener("click", function () {
      var expanded = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!expanded));
      panel.style.maxHeight = expanded ? null : panel.scrollHeight + "px";
      if (window.dataLayer && !expanded) {
        window.dataLayer.push({ event: "faq_expand", question_text: btn.textContent.trim() });
      }
    });
  });
  // Expand any default-open item to its content height on load (desktop only)
  if (window.matchMedia("(min-width: 768px)").matches) {
    document.querySelectorAll('.faq__q[aria-expanded="true"]').forEach(function (btn) {
      var panel = btn.nextElementSibling;
      if (panel) panel.style.maxHeight = panel.scrollHeight + "px";
    });
  }

  /* ---- 4. Sticky mobile CTA bar ----
     Shows after the user scrolls past the hero; hides when footer enters view. */
  var sticky = document.querySelector(".sticky-cta");
  if (sticky) {
    var anchorTop = document.querySelector(".hero, .page-hero");
    var footer = document.querySelector(".site-footer");
    var pastHero = false, footerVisible = false;
    var update = function () { sticky.classList.toggle("is-visible", pastHero && !footerVisible); };

    if (anchorTop) {
      new IntersectionObserver(function (e) {
        pastHero = !e[0].isIntersecting; update();
      }, { threshold: 0 }).observe(anchorTop);
    } else { pastHero = true; }

    if (footer) {
      new IntersectionObserver(function (e) {
        footerVisible = e[0].isIntersecting; update();
      }, { threshold: 0 }).observe(footer);
    }
    update();
  }

  /* ---- 4b. Forms: client-side validation + on-page success ----
     Static demo handler. Replace the no-backend path with a real endpoint
     (Formspree, Netlify Forms, Cloud Function, etc.) before launch. */
  document.querySelectorAll("form.js-form").forEach(function (form) {
    var started = false;
    form.addEventListener("input", function () {
      if (!started) { started = true; track("form_start", { form_type: form.dataset.formType || "contact" }); }
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (field) {
        var wrap = field.closest(".field");
        var valid = field.checkValidity() && field.value.trim() !== "";
        if (wrap) wrap.classList.toggle("field--error", !valid);
        if (!valid && ok) { field.focus(); ok = false; }
      });
      // Honeypot: if filled, silently drop.
      var hp = form.querySelector(".honeypot input");
      if (hp && hp.value) return;
      if (!ok) return;
      track("form_submit", {
        request_type: form.dataset.formType || "contact",
        business_type: (form.elements["business_type"] && form.elements["business_type"].value) || undefined
      });
      var name = (form.elements["name"] && form.elements["name"].value)
        || (form.elements["contact_name"] && form.elements["contact_name"].value) || "";
      var success = form.parentNode.querySelector(".form-success");
      if (success) {
        success.textContent = success.dataset.template
          ? success.dataset.template.replace("{name}", name.trim())
          : success.textContent;
        form.hidden = true;
        success.hidden = false;
        success.setAttribute("tabindex", "-1");
        success.focus();
      }
    });
  });

  /* ---- 5. GA4 event hooks (no-op until dataLayer/GTM present) ---- */
  function track(event, params) {
    if (window.dataLayer) window.dataLayer.push(Object.assign({ event: event }, params || {}));
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a");
    if (!a) return;
    var section = a.closest("[data-section]");
    var pageSection = section ? section.getAttribute("data-section") : "";
    if (a.href.indexOf("tel:") === 0) {
      track("phone_click", { phone_number: a.href.replace("tel:", ""), page_section: pageSection });
    } else if (a.dataset.cents !== undefined || /schedule pickup/i.test(a.textContent)) {
      track("schedule_pickup", { page_section: pageSection, button_text: a.textContent.trim() });
    } else if (/get directions/i.test(a.textContent)) {
      track("directions_click", { page_section: pageSection });
    }
  });
})();
