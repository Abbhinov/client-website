/* ==========================================================================
   Cutz by Raul — contact.js
   Client-side inquiry-form validation, honeypot, success state, GA4 event.
   Submission endpoint (Formspree/Basin/Cloud Function) is wired via the
   form's `action` attribute; replace the placeholder before launch.
   Per Contact Dev Guide §7.
   ========================================================================== */
(function () {
  "use strict";

  function track(event, params) {
    if (typeof window.gtag === "function") window.gtag("event", event, params || {});
  }

  var form = document.getElementById("inquiryForm");
  if (!form) return;
  var success = document.getElementById("formSuccess");

  function setError(field, msg) {
    var wrap = field.closest(".field");
    wrap.classList.add("has-error");
    var el = wrap.querySelector(".error-msg");
    if (el) el.textContent = msg;
    field.setAttribute("aria-invalid", "true");
  }
  function clearError(field) {
    var wrap = field.closest(".field");
    wrap.classList.remove("has-error");
    field.removeAttribute("aria-invalid");
  }

  function validateField(field) {
    var v = field.value.trim();
    if (field.name === "name") {
      if (v.length < 2) return setError(field, "Please enter your name."), false;
    } else if (field.name === "phone") {
      var digits = v.replace(/\D/g, "");
      if (digits.length < 10) return setError(field, "Please enter a valid phone number."), false;
    } else if (field.name === "email") {
      if (v && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) return setError(field, "Please enter a valid email address."), false;
    } else if (field.name === "message") {
      if (v.length < 10) return setError(field, "Please enter at least 10 characters."), false;
    }
    clearError(field);
    return true;
  }

  // Inline validation on blur
  Array.prototype.forEach.call(form.querySelectorAll("input, textarea"), function (f) {
    if (f.classList.contains("hp-input")) return;
    f.addEventListener("blur", function () { validateField(f); });
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    // Honeypot: silently drop bot submissions
    var hp = form.querySelector(".hp-input");
    if (hp && hp.value) return;

    var fields = ["name", "phone", "email", "message"].map(function (n) { return form.elements[n]; });
    var ok = true;
    fields.forEach(function (f) { if (f && !validateField(f)) ok = false; });
    if (!ok) {
      var firstBad = form.querySelector(".has-error input, .has-error textarea");
      if (firstBad) firstBad.focus();
      return;
    }

    // NOTE: wire form.action to Formspree/Basin/Cloud Function for real delivery.
    // Demo behaviour: show the on-page success state without a network round-trip.
    track("form_submit", { request_type: "inquiry" });
    form.style.display = "none";
    if (success) {
      success.classList.add("is-visible");
      success.setAttribute("tabindex", "-1");
      success.focus();
    }
  });
})();
