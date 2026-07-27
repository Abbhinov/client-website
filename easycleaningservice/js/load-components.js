const { initHome } = await import(new URL("home.js", import.meta.url));

async function loadInto(id, url) {
  const el = document.getElementById(id);
  if (!el) return;

  try {
    const res = await fetch(url, { cache: "no-store" });
    if (!res.ok) throw new Error(`Failed to load ${url} (${res.status})`);
    el.innerHTML = await res.text();
  } catch (err) {
    el.innerHTML = `<!-- Component load failed: ${err.message} -->`;
  }
}

(async () => {
  if (!document.querySelector("#site-header #navigation")) {
    await loadInto("site-header", new URL("../header-fragment.html", import.meta.url).href);
  }

  const headerEl = document.querySelector("#site-header #navigation");
  if (headerEl) {
    const update = () => {
      headerEl.classList.toggle("is-scrolled", window.scrollY > 40);
    };
    window.addEventListener("scroll", update, { passive: true });
    update();
  }

  const dropdownParents = document.querySelectorAll(".nav-item-dropdown");
  dropdownParents.forEach((li) => {
    const topLink = li.querySelector(":scope > .nav-link");
    if (!topLink) return;
    topLink.addEventListener("click", (e) => {
      // On desktop, dropdowns open on hover via CSS; let the link navigate normally.
      if (window.matchMedia("(min-width: 781px)").matches) return;
      e.preventDefault();
      li.classList.toggle("is-open");
    });
  });

  // Mobile hamburger toggle
  const navToggle = document.querySelector(".nav-toggle");
  const navHeader = document.querySelector("#navigation");
  if (navToggle && navHeader) {
    const setOpen = (open) => {
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      navHeader.classList.toggle("is-open", open);
      document.body.classList.toggle("nav-open", open);
    };
    navToggle.addEventListener("click", () => {
      const isOpen = navToggle.getAttribute("aria-expanded") === "true";
      setOpen(!isOpen);
    });
    // Close menu when a leaf nav link is tapped (so the next page loads cleanly)
    navHeader.querySelectorAll(".nav-dropdown a, .nav-main > li:not(.nav-item-dropdown) > .nav-link, .nav-cta").forEach((a) => {
      a.addEventListener("click", () => setOpen(false));
    });
    // Close menu on Esc
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && navToggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        navToggle.focus();
      }
    });
    // Reset menu state when crossing the desktop breakpoint
    const mq = window.matchMedia("(min-width: 781px)");
    const handleMq = () => {
      if (mq.matches) setOpen(false);
    };
    if (mq.addEventListener) mq.addEventListener("change", handleMq);
    else mq.addListener(handleMq);
  }

  if (!document.querySelector("#site-footer .site-footer")) {
    await loadInto("site-footer", new URL("../footer.html", import.meta.url).href);
  }

  initHome();
})();
