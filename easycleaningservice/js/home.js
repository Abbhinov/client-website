export function initHome() {
  initFaqAccordion();
  initBeforeAfterSliders();
  initEstimateForm();
  initEstimateDateMin();
  initExitIntent();
  initRevealOnScroll();
}

function initFaqAccordion() {
  document.querySelectorAll(".faq-acc-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const expanded = btn.getAttribute("aria-expanded") === "true";
      const panel = document.getElementById(btn.getAttribute("aria-controls"));
      btn.setAttribute("aria-expanded", expanded ? "false" : "true");
      if (panel) {
        if (expanded) {
          panel.hidden = true;
        } else {
          panel.hidden = false;
        }
      }
    });
  });
}

function initBeforeAfterSliders() {
  document.querySelectorAll("[data-ba-slider]").forEach((root) => {
    const range = root.querySelector(".ba-range");
    const afterImg = root.querySelector(".ba-after");
    if (!range || !afterImg) return;

    const apply = () => {
      const v = Number(range.value);
      afterImg.style.clipPath = `inset(0 ${100 - v}% 0 0)`;
    };

    range.addEventListener("input", apply);
    range.addEventListener("change", apply);
    apply();
  });
}

function initEstimateForm() {
  const form = document.getElementById("estimate-request-form");
  const success = document.getElementById("estimate-form-success");
  if (!form || !success) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }
    success.hidden = false;
    form.reset();
    initEstimateDateMin();
    success.focus();
  });
}

function initEstimateDateMin() {
  const input = document.getElementById("est-date");
  if (!input) return;
  const t = new Date();
  t.setDate(t.getDate() + 1);
  const iso = t.toISOString().slice(0, 10);
  input.min = iso;
}

function initRevealOnScroll() {
  const els = document.querySelectorAll(".reveal-on-scroll");
  if (!els.length) return;

  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    els.forEach((el) => el.classList.add("is-visible"));
    return;
  }

  const io = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          obs.unobserve(entry.target);
        }
      });
    },
    { rootMargin: "0px 0px -6% 0px", threshold: 0.06 }
  );

  els.forEach((el) => io.observe(el));
}

function initExitIntent() {
  if (window.matchMedia("(max-width: 900px)").matches) return;
  if (sessionStorage.getItem("ecs_exit_shown") === "1") return;

  const modal = document.getElementById("exit-intent-modal");
  const form = document.getElementById("exit-intent-form");
  if (!modal || !form) return;

  // Show shortly after page load (1s feels immediate without being jarring)
  setTimeout(() => {
    if (sessionStorage.getItem("ecs_exit_shown") === "1") return;
    sessionStorage.setItem("ecs_exit_shown", "1");
    modal.hidden = false;
    document.body.style.overflow = "hidden";
  }, 1000);

  modal.querySelectorAll("[data-exit-close]").forEach((el) => {
    el.addEventListener("click", () => {
      modal.hidden = true;
      document.body.style.overflow = "";
    });
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const fd = new FormData(form);
    if (!fd.get("email")) return;
    const thanks = document.getElementById("exit-modal-thanks");
    if (thanks) thanks.hidden = false;
    form.hidden = true;
  });
}
