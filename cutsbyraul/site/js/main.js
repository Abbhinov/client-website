/* ==========================================================================
   Cutz by Raul — main.js
   Nav scroll state, mobile menu, sticky CTA, Booksy wiring, GA4 events.
   No dependencies. Per Homepage Dev Guide §13.
   ========================================================================== */
(function () {
  "use strict";

  var body = document.body;
  var BOOKSY = body.getAttribute("data-booksy");

  /* ---- GA4 helper (safe no-op until gtag is installed) ---- */
  function track(event, params) {
    if (typeof window.gtag === "function") window.gtag("event", event, params || {});
  }

  /* ---- Wire all Booksy "book" links ---- */
  document.querySelectorAll("[data-book]").forEach(function (el) {
    el.setAttribute("href", BOOKSY);
    el.setAttribute("target", "_blank");
    el.setAttribute("rel", "noopener");
    el.addEventListener("click", function () {
      track("book_click", {
        service_type: el.getAttribute("data-service") || "general",
        page_section: el.getAttribute("data-section") || "unknown",
        button_text: el.textContent.trim()
      });
    });
  });

  /* ---- Generic GA4 events (phone, directions, gallery) ---- */
  document.querySelectorAll("[data-ga]").forEach(function (el) {
    el.addEventListener("click", function () {
      var name = el.getAttribute("data-ga");
      var params = { page_section: el.getAttribute("data-section") || "unknown" };
      if (name === "phone_click") params.phone_number = "+13234043231";
      if (name === "gallery_view") params.service_category = el.getAttribute("data-category") || "";
      track(name, params);
    });
  });

  /* ---- Nav: solid background after scrolling past hero ---- */
  var nav = document.getElementById("nav");
  function onScroll() {
    if (window.scrollY > 80) nav.classList.add("is-scrolled");
    else nav.classList.remove("is-scrolled");
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---- Mobile menu overlay ---- */
  var toggle = document.getElementById("navToggle");
  var overlay = document.getElementById("navOverlay");
  var closeBtn = document.getElementById("navClose");

  function openMenu() {
    overlay.classList.add("is-open");
    toggle.setAttribute("aria-expanded", "true");
    body.style.overflow = "hidden";
    closeBtn.focus();
  }
  function closeMenu() {
    overlay.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    body.style.overflow = "";
    toggle.focus();
  }
  if (toggle) toggle.addEventListener("click", openMenu);
  if (closeBtn) closeBtn.addEventListener("click", closeMenu);
  overlay.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeMenu); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && overlay.classList.contains("is-open")) closeMenu();
  });

  /* ---- Mobile sticky CTA: show after scrolling past the fold, hide over footer ----
     Works on every page: pages with a full hero hide it until the hero scrolls out;
     subpages (short dark hero) reveal it after a small scroll threshold. */
  var sticky = document.getElementById("stickyCta");
  var hero = document.querySelector(".hero");
  var footer = document.querySelector(".footer");

  if (sticky) {
    var footerVisible = false;
    var THRESHOLD = hero ? (window.innerHeight * 0.6) : 300;

    function updateSticky() {
      var pastFold = window.scrollY > THRESHOLD;
      if (pastFold && !footerVisible) {
        sticky.classList.add("is-visible");
        sticky.setAttribute("aria-hidden", "false");
      } else {
        sticky.classList.remove("is-visible");
        sticky.setAttribute("aria-hidden", "true");
      }
    }

    if ("IntersectionObserver" in window && footer) {
      new IntersectionObserver(function (e) { footerVisible = e[0].isIntersecting; updateSticky(); })
        .observe(footer);
    }
    window.addEventListener("scroll", updateSticky, { passive: true });
    updateSticky();
  }

  /* ---- Highlight today's row in the hours table ---- */
  var rows = document.querySelectorAll(".hours__row");
  if (rows.length) {
    var day = new Date().getDay(); // 0=Sun ... 6=Sat
    var idx = (day >= 1 && day <= 5) ? 0 : (day === 6 ? 1 : 2);
    if (rows[idx]) rows[idx].classList.add("hours__row--today");
  }

  /* ---- Scroll depth tracking (25/50/75/100) ---- */
  var marks = [25, 50, 75, 100], fired = {};
  window.addEventListener("scroll", function () {
    var h = document.documentElement;
    var pct = Math.round(((h.scrollTop + h.clientHeight) / h.scrollHeight) * 100);
    marks.forEach(function (m) {
      if (pct >= m && !fired[m]) { fired[m] = true; track("scroll_depth", { percent_scrolled: m }); }
    });
  }, { passive: true });
})();
