/* ==========================================================================
   Cutz by Raul — gallery.js
   Client-side category filtering + accessible lightbox. Vanilla JS, no deps.
   Per Gallery Dev Guide §5–7.
   ========================================================================== */
(function () {
  "use strict";

  function track(event, params) {
    if (typeof window.gtag === "function") window.gtag("event", event, params || {});
  }

  var BOOKSY = document.body.getAttribute("data-booksy");
  var items = Array.prototype.slice.call(document.querySelectorAll(".portfolio__item"));
  var pills = Array.prototype.slice.call(document.querySelectorAll(".filter-pill"));

  /* ---------- Filtering ---------- */
  function applyFilter(cat) {
    items.forEach(function (it) {
      var match = cat === "all" || it.getAttribute("data-category") === cat;
      it.classList.toggle("is-hidden", !match);
    });
    pills.forEach(function (p) {
      var on = p.getAttribute("data-filter") === cat;
      p.classList.toggle("is-active", on);
      p.setAttribute("aria-pressed", on ? "true" : "false");
    });
    if (history.replaceState) history.replaceState(null, "", cat === "all" ? "#" : "#" + cat);
  }

  pills.forEach(function (p) {
    p.addEventListener("click", function () {
      var cat = p.getAttribute("data-filter");
      applyFilter(cat);
      track("gallery_filter", { filter_category: cat });
    });
  });

  // Honor incoming hash (shareable filtered view)
  var initial = (location.hash || "").replace("#", "");
  if (initial && pills.some(function (p) { return p.getAttribute("data-filter") === initial; })) {
    applyFilter(initial);
  }

  /* ---------- Lightbox ---------- */
  var lb = document.getElementById("lightbox");
  if (!lb) return;
  var lbStage = lb.querySelector(".lightbox__stage");
  var lbCat = lb.querySelector(".lightbox__cat");
  var lbBook = lb.querySelector("[data-book-style]");
  var btnClose = lb.querySelector(".lightbox__close");
  var btnPrev = lb.querySelector(".lightbox__nav--prev");
  var btnNext = lb.querySelector(".lightbox__nav--next");
  var lastFocused = null;
  var current = -1;

  function visibleItems() { return items.filter(function (it) { return !it.classList.contains("is-hidden"); }); }

  function render(idx) {
    var vis = visibleItems();
    if (!vis.length) return;
    current = (idx + vis.length) % vis.length;
    var it = vis[current];
    var label = it.getAttribute("data-label");
    var cat = it.getAttribute("data-category");
    // Clone the item's placeholder into the stage
    var ph = it.querySelector(".ph").cloneNode(true);
    lbStage.innerHTML = "";
    lbStage.appendChild(ph);
    lbCat.textContent = label;
    var only = vis.length <= 1;
    btnPrev.style.display = only ? "none" : "";
    btnNext.style.display = only ? "none" : "";
    track("gallery_view", { image_category: cat, image_index: current });
  }

  function open(it) {
    var vis = visibleItems();
    var idx = vis.indexOf(it);
    if (idx < 0) return;
    lastFocused = it;
    render(idx);
    lb.classList.add("is-open");
    document.body.style.overflow = "hidden";
    btnClose.focus();
  }
  function close() {
    lb.classList.remove("is-open");
    document.body.style.overflow = "";
    if (lastFocused) lastFocused.focus();
  }

  items.forEach(function (it) { it.addEventListener("click", function () { open(it); }); });
  btnClose.addEventListener("click", close);
  btnPrev.addEventListener("click", function () { render(current - 1); });
  btnNext.addEventListener("click", function () { render(current + 1); });
  lb.addEventListener("click", function (e) { if (e.target === lb) close(); });

  if (lbBook) {
    lbBook.setAttribute("href", BOOKSY);
    lbBook.setAttribute("target", "_blank");
    lbBook.setAttribute("rel", "noopener");
    lbBook.addEventListener("click", function () {
      var vis = visibleItems();
      track("book_click", { service_type: vis[current] ? vis[current].getAttribute("data-label") : "gallery", page_section: "gallery_lightbox" });
    });
  }

  document.addEventListener("keydown", function (e) {
    if (!lb.classList.contains("is-open")) return;
    if (e.key === "Escape") close();
    else if (e.key === "ArrowLeft") render(current - 1);
    else if (e.key === "ArrowRight") render(current + 1);
    else if (e.key === "Tab") {
      // Simple focus trap across the lightbox controls
      var focusables = [btnClose, btnPrev, btnNext, lbBook].filter(function (el) { return el && el.offsetParent !== null; });
      var first = focusables[0], last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  // Touch swipe
  var sx = 0;
  lb.addEventListener("touchstart", function (e) { sx = e.changedTouches[0].clientX; }, { passive: true });
  lb.addEventListener("touchend", function (e) {
    var dx = e.changedTouches[0].clientX - sx;
    if (Math.abs(dx) > 50) render(current + (dx < 0 ? 1 : -1));
  }, { passive: true });
})();
