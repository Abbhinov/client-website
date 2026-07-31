const header = document.querySelector("[data-header]");
const menuToggle = document.querySelector(".menu-toggle");
const boardPreview = document.querySelector("[data-event-view]");
const homeRevealTargets = document.body.classList.contains("home-page")
  ? document.querySelectorAll(".home-page main > section, .home-page .home-icon-tile, .home-page .service-card, .home-page .fact-panel, .home-page .pillar-grid article, .home-page .steps article, .home-page .stepper-node, .home-page .site-footer")
  : [];
const pickupStepper = document.querySelector("[data-stepper]");
const answerStation = document.querySelector("[data-answer-station]");

window.dataLayer = window.dataLayer || [];
window.dataLayer.push({ page_locale: document.documentElement.lang || "en" });

if (header) {
  const setHeaderState = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  };
  setHeaderState();
  window.addEventListener("scroll", setHeaderState, { passive: true });
}

if (menuToggle) {
  menuToggle.addEventListener("click", () => {
    const isOpen = document.body.classList.toggle("menu-open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
  });
}

document.querySelectorAll("[data-event]").forEach((element) => {
  element.addEventListener("click", () => {
    const payload = { event: element.dataset.event };
    if (element.dataset.block) payload.block = element.dataset.block;
    if (element.dataset.service) payload.service = element.dataset.service;
    window.dataLayer.push(payload);
  });
});

if (boardPreview && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      window.dataLayer.push({ event: boardPreview.dataset.eventView });
      observer.disconnect();
    });
  }, { threshold: 0.45 });
  observer.observe(boardPreview);
}

if (homeRevealTargets.length) {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  homeRevealTargets.forEach((element, index) => {
    element.classList.add("scroll-reveal");
    element.style.setProperty("--reveal-delay", `${Math.min(index * 35, 280)}ms`);
  });

  if ("IntersectionObserver" in window && !prefersReducedMotion) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        revealObserver.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });

    homeRevealTargets.forEach((element) => revealObserver.observe(element));
  } else {
    homeRevealTargets.forEach((element) => element.classList.add("is-visible"));
  }
}

if (pickupStepper) {
  const triggers = pickupStepper.querySelectorAll("[data-stepper-trigger]");
  const images = pickupStepper.querySelectorAll("[data-stepper-image]");
  const captions = pickupStepper.querySelectorAll("[data-stepper-caption]");
  const nodes = pickupStepper.querySelectorAll(".stepper-node");

  const setStepperStep = (step) => {
    triggers.forEach((trigger) => {
      trigger.setAttribute("aria-pressed", String(trigger.dataset.stepperTrigger === step));
    });
    images.forEach((image) => {
      image.classList.toggle("is-active", image.dataset.stepperImage === step);
    });
    captions.forEach((caption) => {
      caption.classList.toggle("is-active", caption.dataset.stepperCaption === step);
    });
    nodes.forEach((node) => {
      const trigger = node.querySelector("[data-stepper-trigger]");
      node.classList.toggle("is-active", trigger?.dataset.stepperTrigger === step);
    });
  };

  triggers.forEach((trigger) => {
    const activate = () => setStepperStep(trigger.dataset.stepperTrigger);
    trigger.addEventListener("mouseenter", activate);
    trigger.addEventListener("focus", activate);
    trigger.addEventListener("click", activate);
  });
}

if (answerStation) {
  const triggers = answerStation.querySelectorAll("[data-answer-trigger]");
  const panels = answerStation.querySelectorAll("[data-answer-panel]");

  const setAnswer = (answerId) => {
    triggers.forEach((trigger) => {
      const isActive = trigger.dataset.answerTrigger === answerId;
      trigger.classList.toggle("is-active", isActive);
      trigger.setAttribute("aria-pressed", String(isActive));
    });
    panels.forEach((panel) => {
      panel.classList.toggle("is-active", panel.dataset.answerPanel === answerId);
    });
  };

  triggers.forEach((trigger) => {
    trigger.addEventListener("click", () => setAnswer(trigger.dataset.answerTrigger));
    trigger.addEventListener("focus", () => setAnswer(trigger.dataset.answerTrigger));
  });
}
