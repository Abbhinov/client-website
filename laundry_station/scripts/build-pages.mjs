import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";

const logo = "/assets/laundry-station-logo.jpg";

const services = [
  {
    title: "Wash & Fold",
    slug: "/services/wash-and-fold/",
    summary: "Drop it off and pick it up washed, dried, and folded.",
    best: "Weekly laundry, busy families, towels, everyday clothing.",
    caution: "Customers who need special handling should point it out at drop-off.",
    features: ["By the pound", "Folded neatly", "Rush token pending"],
    heroImage: "/assets/service-wash-fold-hero.png"
  },
  {
    title: "Pickup & Delivery",
    slug: "/services/pickup-delivery/",
    summary: "Schedule from your phone and let the store handle the trip.",
    best: "Northwest Side customers who want laundry returned clean without a store visit.",
    caution: "Delivery ring, fees, and turnaround still need owner confirmation.",
    features: ["Cents booking", "Door pickup", "Delivery area pending"],
    heroImage: "/assets/service-pickup-delivery-hero.png"
  },
  {
    title: "Self-Service",
    slug: "/services/self-service/",
    summary: "Use serviced machines yourself at 6043 W Addison St.",
    best: "Large weekly loads, comforters, and anyone who wants posted machine pricing.",
    caution: "Machine counts and cycle times stay as visible tokens until confirmed.",
    features: ["Serviced machines", "Large capacity", "Attendant token pending"],
    heroImage: "/assets/service-self-service-hero.png"
  },
  {
    title: "Commercial",
    slug: "/services/commercial/",
    summary: "Recurring laundry support for Chicago businesses.",
    best: "Salons, rentals, clinics, fitness, restaurants, and other repeat laundry needs.",
    caution: "Quoted per account; no savings percentage or generic rate claim.",
    features: ["Recurring pickup", "Volume workflow", "Quote required"],
    heroImage: "/assets/service-commercial-hero.png"
  },
  {
    title: "Oversized & Household",
    slug: "/services/oversized/",
    summary: "Wash comforters, area rugs, sleeping bags, and bulky household items.",
    best: "Loads that do not fit or dry properly in a home machine.",
    caution: "Material limits and pet-bedding handling need owner confirmation.",
    features: ["Large washers", "Per item", "DIY or drop-off"],
    heroImage: "/assets/service-oversized-hero.png"
  },
  {
    title: "Ironing & Pressing",
    slug: "/services/ironing-pressing/",
    summary: "Per-item pressing for washable garments and household linens.",
    best: "Shirts, uniforms, table linens, trousers, skirts, and linens that need a crisp finish.",
    caution: "This is not a dry-cleaning page; dry cleaning remains unresolved.",
    features: ["Per item", "Add to wash & fold", "Scope controlled"],
    heroImage: "/assets/service-ironing-pressing-hero.png"
  }
];

const esServices = [
  ["Lavado y doblado", "/es/services/wash-and-fold/", "Deja tu ropa y recógela lavada, seca y doblada."],
  ["Recolección y entrega", "/es/services/pickup-delivery/", "Programa una recolección y Laundry Station se encarga del viaje."],
  ["Autoservicio", "/es/services/self-service/", "Lava aquí en máquinas revisadas y mantenidas."],
  ["Lavandería comercial", "/es/services/commercial/", "Servicio recurrente para negocios de Chicago."],
  ["Grandes y del hogar", "/es/services/oversized/", "Lava edredones, tapetes, sleeping bags y cargas grandes."],
  ["Planchado", "/es/services/ironing-pressing/", "Planchado por pieza para prendas lavables y ropa del hogar."]
];

const pageMap = new Map();

function pageDepth(pagePath = "/") {
  if (pagePath === "/") return 0;
  return pagePath.replace(/^\/|\/$/g, "").split("/").filter(Boolean).length;
}

function relativePrefix(pagePath = "/") {
  const depth = pageDepth(pagePath);
  return depth === 0 ? "./" : "../".repeat(depth);
}

function relativizeRootPath(value = "", pagePath = "/") {
  if (!value.startsWith("/") || value.startsWith("//")) return value;
  const match = value.match(/^([^?#]*)([?#].*)?$/);
  const pathname = match?.[1] || value;
  const suffix = match?.[2] || "";
  let target = pathname === "/" ? "index.html" : pathname.replace(/^\//, "");
  if (target.endsWith("/")) target += "index.html";
  return `${relativePrefix(pagePath)}${target}${suffix}`;
}

function relativizeHtml(html = "", pagePath = "/") {
  return html
    .replace(/\b(href|src|content)=(")(\/(?!\/)[^"]*)"/g, (_match, attr, quote, value) => `${attr}=${quote}${relativizeRootPath(value, pagePath)}${quote}`)
    .replace(/\b(href|src|content)=(')(\/(?!\/)[^']*)'/g, (_match, attr, quote, value) => `${attr}=${quote}${relativizeRootPath(value, pagePath)}${quote}`);
}

function page(path, data, body = "") {
  pageMap.set(path, { ...data, body });
}

function esc(value = "") {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function attrs(items = {}) {
  return Object.entries(items)
    .filter(([, value]) => value !== false && value !== null && value !== undefined)
    .map(([key, value]) => (value === true ? key : `${key}="${esc(value)}"`))
    .join(" ");
}

function swap(label) {
  return `<span class="swap">${esc(label)}</span>`;
}

const iconFiles = {
  about: "icon-about-store.png",
  accessibility: "icon-accessibility.png",
  areaRug: "icon-area-rug.png",
  attendant: "icon-attendant-on-site.png",
  bag: "icon-wash-fold-worth-it.png",
  belmontCragin: "icon-belmont-cragin.png",
  board: "icon-pricing-board.png",
  building: "icon-short-term-rental-linens.png",
  call: "icon-call-phone.png",
  check: "icon-turnaround-time.png",
  comforter: "icon-comforter-duvet.png",
  contact: "icon-contact-message.png",
  detergent: "icon-detergent-supplies.png",
  directions: "icon-directions-map.png",
  done: "icon-turnaround-time.png",
  dunning: "icon-dunning.png",
  englishSpanish: "icon-english-spanish.png",
  faq: "icon-faq-question.png",
  firstTime: "icon-first-time-laundromat.png",
  ironing: "icon-laundry-care-symbols.png",
  jeffersonPark: "icon-jefferson-park.png",
  largeCapacity: "icon-large-capacity.png",
  laundrySymbols: "icon-laundry-care-symbols.png",
  machines: "icon-large-capacity.png",
  map: "icon-service-area-map.png",
  montclare: "icon-montclare.png",
  northwestSide: "icon-northwest-side.png",
  oversized: "icon-large-capacity.png",
  payment: "icon-payment-methods.png",
  petBedding: "icon-pet-bedding.png",
  pickup: "icon-recurring-pickup.png",
  press: "icon-laundry-care-symbols.png",
  portagePark: "icon-portage-park.png",
  pricing: "icon-pricing-board.png",
  privacy: "icon-privacy-lock.png",
  recurring: "icon-recurring-pickup.png",
  rush: "icon-same-day-rush.png",
  salon: "icon-salon-barbershop-towels.png",
  schedule: "icon-schedule-pickup.png",
  sheetsTowels: "icon-sheets-towels.png",
  shortTermRental: "icon-short-term-rental-linens.png",
  sleepingBag: "icon-sleeping-bag.png",
  store: "icon-store-location.png",
  storeHours: "icon-store-hours.png",
  terms: "icon-terms-document.png",
  towelSmell: "icon-towel-smell.png",
  truck: "icon-recurring-pickup.png",
  turnaround: "icon-turnaround-time.png",
  washer: "icon-attendant-on-site.png",
  washerSize: "icon-washer-size-guide.png",
  washFold: "icon-wash-fold-worth-it.png",
  washFoldWorth: "icon-wash-fold-worth-it.png"
};

function serviceIconName(title = "") {
  if (title.includes("Pickup")) return "recurring";
  if (title.includes("Commercial")) return "shortTermRental";
  if (title.includes("Ironing")) return "laundrySymbols";
  if (title.includes("Oversized")) return "largeCapacity";
  if (title.includes("Self")) return "attendant";
  return "washFoldWorth";
}

function icon(name = "washer") {
  const file = iconFiles[name] || iconFiles.washer;
  return `<img class="site-picture-icon" src="/assets/home-icons/${file}" alt="" width="256" height="256" loading="lazy" decoding="async">`;
}

function nav(current = "") {
  const active = (href) => (current === href || (href !== "/" && current.startsWith(href)) ? ' aria-current="page"' : "");
  const englishCandidate = current.startsWith("/es/") ? current.replace(/^\/es/, "") || "/" : current;
  const spanishCandidate = current.startsWith("/es/") ? current : `/es${current === "/" ? "/" : current}`;
  const englishHref = pageMap.has(englishCandidate) ? englishCandidate : "/";
  const spanishHref = pageMap.has(spanishCandidate) ? spanishCandidate : "/es/";
  return `
    <header class="site-header" data-header>
      <a class="brand" href="/" aria-label="Laundry Station home">
        <img src="${logo}" alt="Laundry Station logo" width="1254" height="1254">
      </a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">
        <span></span><span></span><span></span><span class="sr-only">Menu</span>
      </button>
      <nav class="primary-nav" id="primary-nav" aria-label="Primary">
        <div class="nav-group">
          <a href="/services/"${active("/services/")}>Services</a>
          <div class="service-menu" aria-label="Service links">
            ${services.map((item) => `<a href="${item.slug}">${item.title}</a>`).join("")}
          </div>
        </div>
        <a href="/pricing/"${active("/pricing/")}>Pricing</a>
        <a href="/about/"${active("/about/")}>About</a>
        <a href="/faq/"${active("/faq/")}>FAQ</a>
        <a href="/contact/"${active("/contact/")}>Contact</a>
      </nav>
      <div class="header-actions">
        <a class="phone-link pending-inline" href="/contact/#phone">Phone needed</a>
        <div class="language-switch" aria-label="Language">
          <a href="${englishHref}"${!current.startsWith("/es/") ? ' aria-current="page"' : ""}>EN</a>
          <a href="${spanishHref}"${current.startsWith("/es/") ? ' aria-current="page"' : ""}>ES</a>
        </div>
        <a class="btn btn-primary" href="/services/pickup-delivery/" target="_blank" rel="noopener" data-event="schedule_click" data-block="header">Schedule Pickup</a>
      </div>
    </header>`;
}

function footer() {
  return `
    <footer class="site-footer">
      <div class="container footer-grid">
        <div>
          <img src="${logo}" alt="Laundry Station logo" width="1254" height="1254">
          <p>6043 W Addison St<br>Chicago, IL 60634</p>
          <p><span class="footer-token">Phone needed</span><br><span class="footer-token">Hours needed</span></p>
        </div>
        <nav aria-label="Services">
          <h2>Services</h2>
          ${services.map((item) => `<a href="${item.slug}">${item.title}</a>`).join("")}
        </nav>
        <nav aria-label="Company">
          <h2>Company</h2>
          <a href="/pricing/">Pricing</a>
          <a href="/about/">About</a>
          <a href="/faq/">FAQ</a>
          <a href="/contact/">Contact</a>
        </nav>
        <div>
          <h2>Languages</h2>
          <p class="footer-language-links"><a href="/">English</a><a href="/es/">Espa&ntilde;ol</a></p>
          <h2>Payment</h2>
          <p><span class="footer-token">Payment methods needed</span></p>
        </div>
      </div>
      <div class="container footer-bottom">
        <p>&copy; 2026 Laundry Station</p>
        <nav aria-label="Legal">
          <a href="/privacy/">Privacy</a>
          <a href="/terms/">Terms</a>
          <a href="/accessibility/">Accessibility</a>
        </nav>
      </div>
    </footer>
    <div class="mobile-action-bar" aria-label="Quick actions">
      <a class="btn btn-secondary" href="/contact/#phone">Call</a>
      <a class="btn btn-primary" href="/services/pickup-delivery/" target="_blank" rel="noopener" data-event="schedule_click" data-block="mobile_bar">Schedule Pickup</a>
    </div>`;
}

function head({ title, description, lang = "en", path }) {
  return `<!doctype html>
<html lang="${lang}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>${esc(title)}</title>
    <meta name="description" content="${esc(description)}">
    <meta name="theme-color" content="#0C479C">
    <meta property="og:type" content="website">
    <meta property="og:title" content="${esc(title)}">
    <meta property="og:description" content="${esc(description)}">
    <meta property="og:image" content="${logo}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/styles.css?v=20260731-allicons2">
  </head>
  <body class="sub-page">
    ${nav(path)}
    <main id="main">`;
}

function end({ lang = "en", schema = [] } = {}) {
  const schemaBlocks = schema.map((block) => `<script type="application/ld+json">${JSON.stringify(block, null, 2)}</script>`).join("\n");
  return `</main>
    ${footer()}
    ${schemaBlocks}
    <script src="/script.js?v=20260731-allicons2"></script>
  </body>
</html>`;
}

function pageHero({ title, lede, cta = true, chips = [], variant = "page", image = "" }) {
  const imageKey = image ? image.split("/").pop().replace(/^service-/, "").replace(/-hero\.png$/, "") : "";
  return `
    <section class="page-hero page-hero-${variant}${imageKey ? ` page-hero-with-image page-hero-bg-${imageKey}` : ""}">
      <div class="container page-hero-grid">
        <div>
          <h1>${title}</h1>
          <p>${lede}</p>
          ${cta ? `<div class="hero-actions">
            <a class="btn btn-primary" href="/services/pickup-delivery/" target="_blank" rel="noopener" data-event="schedule_click" data-block="hero">Schedule Pickup</a>
            <a class="btn btn-secondary" href="/contact/#phone">Call when phone is confirmed</a>
          </div>` : ""}
          ${chips.length ? `<div class="chip-row hero-chip-row">${chips.map((chip) => `<span class="chip">${chip}</span>`).join("")}</div>` : ""}
        </div>
        ${imageKey ? "" : `<div class="page-hero-panel" aria-hidden="true">
          <div class="panel-lines"><span></span><span></span><span></span><span></span></div>
        </div>`}
      </div>
    </section>`;
}

function band({ title, body = "", surface = "white", content = "", className = "" }) {
  return `
    <section class="section section-${surface} ${className}">
      <div class="container">
        ${title ? `<div class="section-head"><h2>${title}</h2>${body ? `<p>${body}</p>` : ""}</div>` : ""}
        ${content}
      </div>
    </section>`;
}

function cardGrid(items, columns = "auto") {
  return `<div class="content-grid content-grid-${columns}">
    ${items.map((item) => `<article class="info-card">
      ${item.icon ? icon(item.icon) : ""}
      <h3>${item.title}</h3>
      <p>${item.body}</p>
      ${item.link ? `<a class="text-link" href="${item.link.href}">${item.link.label}</a>` : ""}
    </article>`).join("")}
  </div>`;
}

function serviceCards(list = services) {
  return `<div class="services-grid">${list.map((item) => `
    <a class="service-card" href="${item.slug}" data-event="service_card_click" data-service="${item.title.toLowerCase().replaceAll(" ", "_").replaceAll("&", "and")}">
      ${icon(serviceIconName(item.title))}
      <h3>${item.title}</h3>
      <p>${item.summary}</p>
      <span>${item.features.join(" <b></b> ")}</span>
    </a>`).join("")}</div>`;
}

function table({ caption, headers, rows, className = "" }) {
  return `<div class="board-wrap ${className}">
    <table class="board-table">
      <caption>${caption}</caption>
      <thead><tr>${headers.map((h) => `<th>${h}</th>`).join("")}</tr></thead>
      <tbody>
        ${rows.map((row) => `<tr>${row.map((cell, i) => `<td data-label="${headers[i]}">${cell}</td>`).join("")}</tr>`).join("")}
      </tbody>
    </table>
  </div>`;
}

function steps(items) {
  return `<div class="steps">${items.map((item, i) => `<article><span>${i + 1}</span><h3>${item.title}</h3><p>${item.body}</p></article>`).join("")}</div>`;
}

function faq(items) {
  return `<div class="faq-list">${items.map((item) => `<details><summary>${item.q}</summary><p>${item.a}</p></details>`).join("")}</div>`;
}

function conversion(title = "Ready to get laundry off your list?") {
  return `
    <section class="conversion-band">
      <div class="container conversion-inner">
        <h2>${title}</h2>
        <div class="conversion-actions">
          <a class="btn btn-primary" href="/services/pickup-delivery/" target="_blank" rel="noopener" data-event="schedule_click" data-block="footer">Schedule Pickup</a>
          <a class="btn btn-secondary" href="/contact/#phone" data-event="call_click" data-block="footer">Call when phone is confirmed</a>
          <a class="btn btn-secondary" href="/contact/">Contact</a>
        </div>
      </div>
    </section>`;
}

function render(path, data, body) {
  const html = relativizeHtml(`${head({ ...data, path })}${body}${end({ lang: data.lang, schema: data.schema })}`, path);
  const out = path === "/" ? "index.html" : join(path.slice(1), "index.html");
  mkdirSync(dirname(out), { recursive: true });
  writeFileSync(out, html, "utf8");
}

page("/services/", {
  title: "Laundry Services in Chicago 60634 | Laundry Station",
  description: "Compare self-service, wash and fold, pickup and delivery, commercial laundry, oversized household laundry, and ironing at Laundry Station."
}, `
  ${pageHero({
    title: "Six ways to get your laundry done",
    lede: "Use the machines yourself, drop laundry off, schedule pickup, or bring the loads that do not fit at home. This page is a decision aid, not a menu.",
    cta: false,
    chips: ["Services hub", "English", "Prices posted when confirmed"]
  })}
  ${band({
    title: "Choose by the job, not by the label",
    body: "Each service has a clear job. Start with what you need done, then move to the page that owns the details.",
    content: serviceCards()
  })}
  ${band({
    title: "Quick comparison",
    surface: "tint",
    content: table({
      caption: "Which service fits the load?",
      headers: ["Service", "Best fit", "Maybe not if", "Next step"],
      rows: services.map((item) => [item.title, item.best, item.caution, `<a href="${item.slug}">Open</a>`])
    })
  })}
  ${conversion("Know which path fits?")}
`);

const servicePages = [
  {
    path: "/services/wash-and-fold/",
    title: "Wash and Fold in Chicago 60634 | Laundry Station",
    h1: "Wash and fold in Chicago's 60634",
    lede: "Drop off everyday laundry and pick it up washed, dried, and folded. The page stays honest about rate, minimum, and turnaround until the owner confirms them.",
    chips: ["Drop-off", "By the pound", "Turnaround pending"],
    intro: [
      { icon: "bag", title: "What you bring", body: "Everyday washable clothing, towels, sheets, and similar household laundry." },
      { icon: "check", title: "What we do", body: "Wash, dry, fold, and keep the service on the same serviced-machine reliability story as the rest of the site." },
      { icon: "board", title: "What still needs confirmation", body: `${swap("WF rate")} ${swap("Minimum")} ${swap("Turnaround")}` }
    ],
    sections: [
      ["How drop-off works", steps([
        { title: "Bring it in", body: "Drop laundry at the counter and mention anything that needs special handling." },
        { title: "We wash and dry", body: "Laundry is cleaned on serviced machines in the store." },
        { title: "We fold", body: "Items are folded neatly for pickup." },
        { title: "You pick up", body: `Turnaround stays as ${swap("WF turnaround needed")} until confirmed.` }
      ])],
      ["What is included", cardGrid([
        { title: "Sorted sensibly", body: "Service copy should stay plain and operational, with no luxury-language drift." },
        { title: "Folded for the shelf", body: "The page sells relief from the chore, not a fabricated premium process." },
        { title: "Optional rush", body: `${swap("Same-day rush policy needed")}` }
      ], "three")]
    ]
  },
  {
    path: "/services/pickup-delivery/",
    title: "Laundry Pickup and Delivery Chicago | Laundry Station",
    h1: "Laundry pickup and delivery across Chicago's Northwest Side",
    lede: "Schedule a pickup, send the laundry out, and get it back clean. The exact Cents booking link, delivery ring, and fees remain visible owner-confirmed inputs.",
    chips: ["Cents booking", "Northwest Side", "Delivery ring pending"],
    intro: [
      { icon: "truck", title: "Schedule", body: "The platform is Cents; the exact booking URL is the only remaining link token." },
      { icon: "bag", title: "Pickup and return", body: "Laundry moves between your door and the store without needing a laundromat visit." },
      { icon: "map", title: "Delivery area", body: `${swap("Delivery ring needed")}` }
    ],
    sections: [
      ["How pickup works", steps([
        { title: "Schedule", body: "Book a pickup in a minute once the Cents link is connected." },
        { title: "We pick up", body: "Laundry is collected from your door in the confirmed service area." },
        { title: "We clean", body: "Washed, dried, and folded on serviced machines." },
        { title: "We deliver", body: `Back to you clean and ready. ${swap("Turnaround needed")}` }
      ])],
      ["Rates and delivery facts", table({
        caption: "Pickup and delivery tokens",
        headers: ["Item", "Status", "Launch note"],
        rows: [
          ["Per-pound rate", swap("PND rate needed"), "Owner confirmation required"],
          ["Pickup/delivery fee", swap("PND fee needed"), "Do not guess"],
          ["Minimum order", swap("PND minimum needed"), "Do not borrow from sister site"],
          ["Rush option", swap("PND rush needed"), "Optional until confirmed"]
        ]
      })]
    ]
  },
  {
    path: "/services/self-service/",
    title: "Self-Service Laundry in Chicago 60634 | Laundry Station",
    h1: "Self-service laundry on machines that work",
    lede: "Do it yourself on serviced washers and dryers at 6043 W Addison St. The page supports the reliability claim with a Board-style machine floor.",
    chips: ["Walk-in", "Machine floor", "Payment pending"],
    intro: [
      { icon: "washer", title: "Serviced machines", body: "The store story is repaired and working, not a vague promise of brand new." },
      { icon: "board", title: "Posted machine prices", body: "The full machine table stays tokenized until real washer and dryer rows are confirmed." },
      { icon: "check", title: "Useful for big loads", body: `${swap("Largest machine sentence needed")}` }
    ],
    sections: [
      ["The machine floor", table({
        caption: "Self-service Board rows awaiting confirmation",
        headers: ["Machine", "Capacity", "Count", "Price", "What it fits"],
        rows: [
          [swap("Washer tier"), swap("Capacity"), swap("Count"), swap("Price"), swap("Fits")],
          [swap("Washer tier"), swap("Capacity"), swap("Count"), swap("Price"), swap("Fits")],
          [swap("Dryer tier"), swap("Capacity"), swap("Count"), swap("Price"), swap("Fits")]
        ]
      })],
      ["Before you come in", cardGrid([
        { title: "Payment", body: `${swap("Payment sentence needed")}` },
        { title: "Supplies", body: `${swap("Detergent policy needed")}` },
        { title: "Time", body: `${swap("Self-service time needed")}` }
      ], "three")]
    ]
  },
  {
    path: "/services/commercial/",
    title: "Commercial Laundry for Chicago Businesses | Laundry Station",
    h1: "Commercial laundry for Chicago businesses",
    lede: "Recurring laundry is quoted per account. The page sells a clear process and a dependable handoff, not an invented discount.",
    chips: ["Quote required", "Recurring pickup", "No savings claim"],
    intro: [
      { icon: "building", title: "For repeat laundry", body: "Useful for businesses with towels, linens, uniforms, or recurring washable items." },
      { icon: "truck", title: "Pickup available", body: `${swap("Commercial pickup policy needed")}` },
      { icon: "board", title: "Quoted per account", body: "No public commercial rate until the owner confirms the quote process." }
    ],
    sections: [
      ["Business types", cardGrid([
        { title: "Salons and barbershops", body: "Towels and washable linens with predictable weekly volume." },
        { title: "Short-term rentals", body: "Sheets, towels, and guest turnover laundry." },
        { title: "Fitness and wellness", body: "Towels and washable service textiles." },
        { title: "Restaurants and cafes", body: "Aprons, towels, and other washable business laundry." }
      ], "four")],
      ["Quote request", `<form class="quote-form" aria-label="Commercial quote request">
        <label>Business name<input type="text" name="business" autocomplete="organization"></label>
        <label>Contact name<input type="text" name="name" autocomplete="name"></label>
        <label>Phone or email<input type="text" name="contact" autocomplete="email"></label>
        <label>Weekly laundry notes<textarea name="notes" rows="5"></textarea></label>
        <button class="btn btn-primary" type="button">Request quote</button>
      </form>`]
    ]
  },
  {
    path: "/services/oversized/",
    title: "Oversized Laundry in Chicago | Laundry Station",
    h1: "Wash the things that do not fit at home",
    lede: "Comforters, area rugs, sleeping bags, and pet bedding need room to move and dry. This page keeps the promise local and practical.",
    chips: ["Comforters", "Area rugs", "Large washers"],
    intro: [
      { icon: "bag", title: "King comforters", body: "The strongest local pull: bulky home items that smaller home machines fight." },
      { icon: "washer", title: "Large capacity", body: `${swap("Largest washer details needed")}` },
      { icon: "check", title: "DIY or drop-off", body: `${swap("Oversized service policy needed")}` }
    ],
    sections: [
      ["Common oversized items", table({
        caption: "Oversized item guidance",
        headers: ["Item", "Best route", "Price"],
        rows: [
          ["King comforter", "Large washer or drop-off", swap("Price needed")],
          ["Area rug", "Ask at counter first", swap("Price needed")],
          ["Sleeping bag", "Large washer", swap("Price needed")],
          ["Pet bedding", swap("Handling policy needed"), swap("Price needed")]
        ]
      })],
      ["What this page does not claim", cardGrid([
        { title: "No health claims", body: "Pet bedding and towels can be described mechanically, without pest or hygiene promises." },
        { title: "No dry-cleaning promise", body: "Items that need dry cleaning remain out of scope until the service is confirmed." },
        { title: "No guessed capacity", body: "Machine sizes stay tokenized until the owner confirms the floor." }
      ], "three")]
    ]
  },
  {
    path: "/services/ironing-pressing/",
    title: "Ironing and Pressing in Chicago 60634 | Laundry Station",
    h1: "Ironing and pressing, per item",
    lede: "Pressed, finished, and ready to wear. This page keeps the scope tight: washable garments and household linens, not dry cleaning.",
    chips: ["Per item", "Scope controlled", "No dry cleaning claim"],
    intro: [
      { icon: "press", title: "Crisp finish", body: "Shirts, uniforms, linens, and other washable items that need pressing." },
      { icon: "bag", title: "Add to wash & fold", body: `${swap("Add-on policy needed")}` },
      { icon: "board", title: "Rates by item", body: "Each item remains a published row once rates are confirmed." }
    ],
    sections: [
      ["Per-item rates", table({
        caption: "Ironing and pressing rows awaiting confirmation",
        headers: ["Item", "Scope", "Price"],
        rows: [
          ["Shirt", swap("Press shirt scope"), swap("Price")],
          ["Trousers", swap("Press trousers scope"), swap("Price")],
          ["Skirt", swap("Press skirt scope"), swap("Price")],
          ["Uniform", swap("Press uniform scope"), swap("Price")],
          ["Tablecloth or linens", swap("Press linens scope"), swap("Price")]
        ]
      })],
      ["Scope line", cardGrid([
        { title: "Washable garments", body: "The page should avoid dry-cleaning vocabulary until the business confirms it." },
        { title: "Household linens", body: "Useful for table linens and flat household pieces that need a finished look." },
        { title: "Turnaround", body: `${swap("Turnaround needed")}` }
      ], "three")]
    ]
  }
];

for (const item of servicePages) {
  page(item.path, {
    title: item.title,
    description: item.lede
  }, `
    ${pageHero({ title: item.h1, lede: item.lede, chips: item.chips, image: services.find((service) => service.slug === item.path)?.heroImage })}
    ${band({ title: "What this page covers", content: cardGrid(item.intro, "three") })}
    ${item.sections.map(([title, content], i) => band({ title, surface: i % 2 ? "white" : "tint", content })).join("")}
    ${band({ title: "Questions before launch", surface: "tint", content: faq([
      { q: "Can this page ship with the visible tokens?", a: "As a preview, yes. For production, hard owner facts need confirmation or the page should stay held." },
      { q: "Does this page include ratings or savings claims?", a: "No. The site avoids fabricated proof and discount language." },
      { q: "Can customers schedule pickup from here?", a: "The CTA routes through the Cents fallback path until the exact booking URL is supplied." }
    ]) })}
    ${conversion()}
  `);
}

page("/pricing/", {
  title: "Laundry Prices in Chicago 60634 | Laundry Station",
  description: "The Board will list Laundry Station washer, dryer, wash and fold, pickup and delivery, oversized, and ironing prices once owner-confirmed."
}, `
  ${pageHero({
    title: "All our prices, posted",
    lede: "The Board is the signature page: machine sizes, what they fit, and every published rate in one place. Unknown prices stay visible as tokens until confirmed.",
    cta: false,
    chips: ["The Board", "No savings claims", "Machine rows pending"]
  })}
  ${band({ title: "What pricing will show", content: cardGrid([
    { icon: "pricing", title: "Posted board", body: "Public rows stay visible so customers know what still needs confirmation." },
    { icon: "payment", title: "Payment methods", body: `${swap("Payment methods needed")}` },
    { icon: "largeCapacity", title: "Machine size", body: "Capacity and fit guidance belong next to the price, not hidden on a separate page." }
  ], "three") })}
  ${band({ title: "Self-service machines", content: table({
    caption: "Washer and dryer rows",
    headers: ["Machine", "Capacity", "Count", "Price", "What it fits"],
    rows: [
      [swap("Washer"), swap("Capacity"), swap("Count"), swap("Price"), swap("Fits")],
      [swap("Washer"), swap("Capacity"), swap("Count"), swap("Price"), swap("Fits")],
      [swap("Dryer"), swap("Capacity"), swap("Count"), swap("Price"), swap("Fits")]
    ]
  }) })}
  ${band({ title: "Done-for-you rates", surface: "tint", content: table({
    caption: "Service rates awaiting confirmation",
    headers: ["Service", "How priced", "Rate", "Minimum"],
    rows: [
      ["Wash & Fold", "Per pound", swap("WF rate"), swap("WF minimum")],
      ["Pickup & Delivery", "Per pound + fees", swap("PND rate"), swap("PND minimum")],
      ["Commercial", "Quoted per account", "Quote", swap("Commercial minimum")],
      ["Ironing & Pressing", "Per item", swap("Item rates"), "n/a"]
    ]
  }) })}
  ${band({ title: "Oversized and household", content: table({
    caption: "Oversized rows",
    headers: ["Item", "Route", "Price"],
    rows: [
      ["Comforter", "DIY or drop-off", swap("Price")],
      ["Area rug", "Ask first", swap("Price")],
      ["Sleeping bag", "Large washer", swap("Price")],
      ["Pet bedding", swap("Policy"), swap("Price")]
    ]
  }) })}
  ${conversion("Need a price before you come in?")}
`);

page("/about/", {
  title: "About Laundry Station | 6043 W Addison",
  description: "Laundry Station is a laundromat at 6043 W Addison St in Chicago, built around serviced machines, posted prices, and practical help."
}, `
  ${pageHero({
    title: "A laundromat on Addison, run properly",
    lede: "Laundry Station's website answers the reputation question with operating facts: serviced machines, posted prices, and clear options when you want laundry done for you.",
    cta: false,
    chips: ["6043 W Addison", "Chicago 60634", "Ownership date pending"]
  })}
  ${band({ title: "The reset is factual", content: `<div class="story-block"><p>${swap("Ownership date needed")} Machines serviced, prices posted. The site avoids the phrase that drags old reviews back into view and simply states what changed once the date is confirmed.</p></div>` })}
  ${band({ title: "What the store is built to prove", surface: "tint", content: cardGrid([
    { icon: "about", title: "The store is local", body: "6043 W Addison is the center of the page story." },
    { icon: "machines", title: "The machines work", body: "Reliability is the thread through every page." },
    { icon: "pricing", title: "Prices are posted", body: "The Board makes cost visible before someone arrives." },
    { icon: "done", title: "Laundry can be done for you", body: "Wash & fold and pickup & delivery lead the revenue path without hiding self-service." }
  ], "four") })}
  ${band({ title: "Neighbourhood context", content: `<div class="split-layout"><div><p>The site speaks to Dunning, Portage Park, Belmont Cragin, and Montclare without pretending those neighbourhoods are the same. English and Spanish pages are both part of the launch plan.</p></div><div class="map-card"><div class="map-grid"><span class="map-pin">6043 W Addison</span></div></div></div>` })}
  ${conversion("Need laundry done this week?")}
`);

page("/faq/", {
  title: "Laundry Station FAQ | Chicago 60634",
  description: "Answers about hours, payments, machines, pickup and delivery, wash and fold, oversized laundry, ironing, and store details."
}, `
  ${pageHero({
    title: "Answers before you make the trip",
    lede: "The FAQ is operational. It answers what people actually need to know before they come in, call, or schedule pickup.",
    cta: false,
    chips: ["FAQ", "Schema-ready", "Owner facts pending"]
  })}
  ${band({ title: "Fast paths", content: cardGrid([
    { icon: "storeHours", title: "Hours", body: swap("Hours sentence needed") },
    { icon: "payment", title: "Payment", body: swap("Payment sentence needed") },
    { icon: "englishSpanish", title: "Language", body: "Se habla espa&ntilde;ol." },
    { icon: "faq", title: "Questions", body: "Use this page before calling or visiting." }
  ], "four") })}
  ${band({ title: "Store basics", content: faq([
    { q: "What are your hours?", a: swap("Hours sentence needed") },
    { q: "Where are you located?", a: "Laundry Station is at 6043 W Addison St, Chicago, IL 60634." },
    { q: "What payment methods do you accept?", a: `${swap("Payment sentence needed")} The final wording must handle Illinois LINK cash assistance accurately.` },
    { q: "Do you speak Spanish?", a: "Se habla espa&ntilde;ol. The Spanish pages are planned as native pages, not machine translations." }
  ]) })}
  ${band({ title: "Machines and self-service", surface: "tint", content: faq([
    { q: "Are the machines working?", a: "The page uses serviced and working as the reliability claim. Specific machine rows still need owner confirmation." },
    { q: "What is the largest machine?", a: swap("Largest machine sentence needed") },
    { q: "How long does a wash and dry take?", a: swap("Self-service time needed") }
  ]) })}
  ${band({ title: "Done-for-you services", content: faq([
    { q: "Do you offer wash and fold?", a: "Yes. Drop-off wash and fold has its own service page, with rate and turnaround tokens pending." },
    { q: "Do you offer pickup and delivery?", a: `${swap("Delivery area sentence needed")}` },
    { q: "Do you offer ironing or pressing?", a: "Yes, as a controlled per-item service for washable garments and linens once the item list is confirmed." }
  ]) })}
  ${conversion("Still have a question?")}
`);

page("/contact/", {
  title: "Contact Laundry Station | 6043 W Addison",
  description: "Call, visit, get directions, or schedule pickup and delivery with Laundry Station at 6043 W Addison St in Chicago."
}, `
  ${pageHero({
    title: "Visit us or call",
    lede: "Use this page when you need the address, phone, directions, pickup scheduling, or the basic store facts before you leave home.",
    cta: true,
    chips: ["6043 W Addison", "Phone pending", "Hours pending"]
  })}
  ${band({ title: "Contact methods", content: cardGrid([
    { icon: "store", title: "Visit", body: "6043 W Addison St, Chicago, IL 60634", link: { href: "https://www.google.com/maps/search/?api=1&query=6043+W+Addison+St+Chicago+IL+60634", label: "Get directions" } },
    { icon: "call", title: "Call", body: swap("Phone number needed") },
    { icon: "schedule", title: "Schedule pickup", body: "Cents is confirmed; the exact store booking URL is still pending.", link: { href: "/services/pickup-delivery/", label: "Pickup details" } },
    { icon: "contact", title: "Text", body: swap("Text-capable number needed") }
  ], "four") })}
  ${band({ title: "Find us on Addison", surface: "tint", content: `<div class="split-layout"><div><p>The map centers on 41.94541, -87.77826. The production version can replace this placeholder with a lazy-loaded Google map once the deployment domain is known.</p><a class="text-link on-tint" href="https://www.google.com/maps/search/?api=1&query=6043+W+Addison+St+Chicago+IL+60634" target="_blank" rel="noopener">Open directions</a></div><div class="map-card"><div class="map-grid"><span class="map-pin">6043 W Addison</span></div></div></div>` })}
  ${band({ title: "Send a message", content: `<form class="quote-form" aria-label="Contact message">
    <label>Your name<input type="text" name="name" autocomplete="name"></label>
    <label>Phone or email<input type="text" name="contact"></label>
    <label>What do you need?<textarea name="message" rows="5"></textarea></label>
    <button class="btn btn-primary" type="button">Send message</button>
  </form>` })}
`);

const legalPages = [
  ["/privacy/", "Privacy Policy", "Privacy Policy | Laundry Station", "This placeholder page names the privacy topics counsel or the owner should confirm before launch.", [
    ["Information we may collect", "Contact messages, quote requests, approximate analytics, device/browser data, and pickup request details once Cents is connected."],
    ["How information may be used", "To respond to customers, operate pickup and delivery, understand site performance, and maintain the website."],
    ["What still needs review", `${swap("Host needed")} ${swap("Analytics setup needed")} ${swap("Form routing needed")}`]
  ]],
  ["/terms/", "Terms of Use", "Terms of Use | Laundry Station", "This is a site-specific placeholder for counsel review, not final legal advice.", [
    ["Website use", "The site provides store information, service descriptions, and links to booking or contact routes."],
    ["Service scope", "Laundry, pickup, delivery, commercial, oversized, and pressing terms should be confirmed by the owner before launch."],
    ["What still needs review", `${swap("Commercial account terms")} ${swap("Damage/loss policy")} ${swap("Pickup policy")}`]
  ]],
  ["/accessibility/", "Accessibility", "Accessibility | Laundry Station", "Laundry Station's web pages are built to be readable, keyboard accessible, and responsive.", [
    ["Our approach", "Semantic HTML, visible focus, AA contrast, 44px tap targets, and no horizontal overflow at mobile widths."],
    ["Known limitations", "Owner facts, final maps, and third-party booking surfaces may need additional checks once connected."],
    ["Contact for help", `${swap("Phone needed")} ${swap("Email or contact route needed")}`]
  ]]
];

const legalIcons = {
  "/privacy/": "privacy",
  "/terms/": "terms",
  "/accessibility/": "accessibility"
};

for (const [path, h1, title, lede, sections] of legalPages) {
  page(path, { title, description: lede }, `
    ${pageHero({ title: h1, lede, cta: false, chips: ["Draft placeholder", "Counsel review"] })}
    ${band({ title: "Page sections", content: cardGrid(sections.map(([head, body], index) => ({
      icon: index === 0 ? legalIcons[path] : index === 1 ? "check" : "contact",
      title: head,
      body
    })), "three") })}
  `);
}

const esLegalPages = [
  ["/es/privacy/", "Privacidad", "Privacidad | Laundry Station", "Página provisional para revisar antes del lanzamiento.", "Privacidad"],
  ["/es/terms/", "Términos de uso", "Términos de uso | Laundry Station", "Página provisional para revisión legal antes del lanzamiento.", "Términos"],
  ["/es/accessibility/", "Accesibilidad", "Accesibilidad | Laundry Station", "Pautas de accesibilidad para las páginas de Laundry Station.", "Accesibilidad"]
];

for (const [path, h1, title, lede, chip] of esLegalPages) {
  page(path, { title, description: lede, lang: "es" }, `
    ${pageHero({ title: h1, lede, cta: false, chips: [chip, "Borrador", "Revisión pendiente"] })}
    ${band({ title: "Contenido provisional", content: `<div class="legal-prose"><h2>Antes del lanzamiento</h2><p>Esta página debe revisarse con los datos finales del negocio, el formulario, el proveedor de hosting y el flujo de Cents.</p><h2>Dato pendiente</h2><p>${swap("Texto legal final pendiente")}</p></div>` })}
  `);
}

const esPathMap = [
  ["/es/", "Lavandería en Chicago 60634 | Laundry Station", "Laundry Station en 6043 W Addison St, Chicago. Autoservicio, lavado y doblado, y recolección y entrega.", "Una lavandería en Chicago 60634 con máquinas revisadas", "Laundry Station está en 6043 W Addison St: autoservicio en máquinas revisadas, más lavado y doblado y recolección y entrega."],
  ["/es/services/", "Servicios de lavandería | Laundry Station", "Compara autoservicio, lavado y doblado, recolección y entrega, comercial, grandes del hogar y planchado.", "Seis maneras de lavar tu ropa", "Elige el camino que encaja con tu día: hacerlo tú mismo, dejarlo, pedir recolección o traer cargas grandes."],
  ["/es/pricing/", "Precios de lavandería | Laundry Station", "Precios publicados para autoservicio, lavado y doblado, recolección, grandes del hogar y planchado.", "Todos nuestros precios, publicados", "The Board mostrará cada precio cuando los datos del dueño estén confirmados."],
  ["/es/about/", "Sobre Laundry Station", "Laundry Station en 6043 W Addison St, Chicago.", "Una lavandería en Addison, bien atendida", "La página responde con hechos: máquinas revisadas, precios publicados y opciones para que te laven la ropa."],
  ["/es/faq/", "Preguntas frecuentes | Laundry Station", "Respuestas sobre horarios, pagos, máquinas, recolección, entrega y servicios.", "Respuestas antes de venir", "Preguntas prácticas para llamar, venir o programar una recolección."],
  ["/es/contact/", "Contacto | Laundry Station", "Llama, visita o programa recolección con Laundry Station.", "Ven a vernos o llámanos", "Laundry Station está en 6043 W Addison St, Chicago, IL 60634."]
];

for (const [path, title, description, h1, lede] of esPathMap) {
  page(path, { title, description, lang: "es" }, `
    ${pageHero({ title: h1, lede, cta: !path.includes("pricing") && !path.includes("faq"), chips: ["Espa&ntilde;ol", "Datos por confirmar"] })}
    ${band({ title: "Servicios", content: `<div class="services-grid">${esServices.map(([name, href, summary], index) => `<a class="service-card" href="${href}">${icon(serviceIconName(services[index]?.title || ""))}<h3>${name}</h3><p>${summary}</p><span>Detalle en progreso <b></b> Datos por confirmar</span></a>`).join("")}</div>` })}
    ${band({ title: "Datos que faltan", surface: "tint", content: cardGrid([
      { title: "Teléfono", body: swap("Teléfono pendiente") },
      { title: "Horario", body: swap("Horario pendiente") },
      { title: "Pagos", body: swap("Métodos de pago pendientes") }
    ], "three") })}
    ${conversion("¿Listo para lavar?")}
  `);
}

for (const [index, [name, href, summary]] of esServices.entries()) {
  page(href, {
    title: `${name} | Laundry Station`,
    description: summary,
    lang: "es"
  }, `
    ${pageHero({ title: name, lede: summary, chips: ["Espa&ntilde;ol", "Página espejo"], image: services[index]?.heroImage })}
    ${band({ title: "Qué cubre esta página", content: cardGrid([
      { title: "Servicio", body: summary },
      { title: "Datos por confirmar", body: `${swap("Precio pendiente")} ${swap("Tiempo pendiente")}` },
      { title: "Siguiente paso", body: "Conectar esta página con la guía española completa cuando se llenen los datos del dueño." }
    ], "three") })}
    ${band({ title: "Preguntas", surface: "tint", content: faq([
      { q: "¿La página está lista para producción?", a: "Todavía no. Los datos visibles deben confirmarse antes del lanzamiento." },
      { q: "¿La versión en español es nativa?", a: "Sí. Esta estructura evita traducción automática literal y deja espacio para el texto final." }
    ]) })}
    ${conversion("¿Quieres programar recolección?")}
  `);
}

const areas = [
  ["Dunning", "/areas/dunning/", "Your laundromat in Dunning", "For nearby walk-in laundry and done-for-you routes from the Addison store."],
  ["Portage Park", "/areas/portage-park/", "Wash and fold for Portage Park", "A local handoff page for customers who want laundry done without losing an evening."],
  ["Belmont Cragin", "/areas/belmont-cragin/", "Self-service laundry for Belmont Cragin", "A practical page for self-service and Spanish-language discovery around the store."],
  ["Montclare", "/areas/montclare/", "Pickup and delivery in Montclare", "A route page for customers who want Laundry Station to handle the trip."],
  ["Jefferson Park", "/areas/jefferson-park/", "Pickup and delivery for Jefferson Park", "A careful delivery-area page that stays tokenized until the ring is confirmed."],
  ["Northwest Side", "/areas/northwest-side/", "Where we deliver", "The delivery-area hub for neighbourhoods served by pickup and delivery."]
];

const areaIcons = {
  "/areas/belmont-cragin/": "belmontCragin",
  "/areas/dunning/": "dunning",
  "/areas/jefferson-park/": "jeffersonPark",
  "/areas/montclare/": "montclare",
  "/areas/northwest-side/": "northwestSide",
  "/areas/portage-park/": "portagePark"
};

page("/areas/", {
  title: "Laundry Service Areas | Laundry Station",
  description: "Neighbourhood pages for Dunning, Portage Park, Belmont Cragin, Montclare, Jefferson Park, and the Northwest Side delivery area."
}, `
  ${pageHero({ title: "Where Laundry Station fits locally", lede: "Area pages route visitors to the right service without repeating every service page. Delivery boundaries stay visible until confirmed.", cta: false, chips: ["Area hub", "Delivery ring pending"] })}
  ${band({ title: "Neighbourhood pages", content: `<div class="services-grid">${areas.map(([name, href, h1, summary]) => `<a class="service-card" href="${href}">${icon(areaIcons[href] || "map")}<h3>${name}</h3><p>${summary}</p><span>${h1}</span></a>`).join("")}</div>` })}
  ${band({ title: "Local facts still needed", surface: "tint", content: cardGrid([
    { title: "Delivery ring", body: swap("Delivery ring needed") },
    { title: "Parking", body: swap("Parking details needed") },
    { title: "Language", body: "Spanish pages stay native where the audience needs it most." }
  ], "three") })}
`);

for (const [name, href, h1, summary] of areas) {
  page(href, {
    title: `${name} Laundry Service | Laundry Station`,
    description: summary
  }, `
    ${pageHero({ title: h1, lede: summary, cta: href.includes("delivery") || name !== "Belmont Cragin", chips: [name, "Area page", "Local proof pending"] })}
    ${band({ title: "Best route from this area", content: cardGrid([
      { icon: areaIcons[href] || "map", title: name, body: "Start with the neighbourhood route, then choose the service that fits the load." },
      { icon: "washer", title: "Walk in", body: "Use self-service machines at 6043 W Addison St." },
      { icon: "bag", title: "Drop off", body: "Wash & fold is the straightforward done-for-you option." },
      { icon: "truck", title: "Pickup", body: `${swap("Delivery sentence needed")}` }
    ], "four") })}
    ${band({ title: "Services for this area", surface: "tint", content: serviceCards(services.slice(0, 4)) })}
    ${conversion("Need the right laundry route?")}
  `);
}

const resources = [
  ["/resources/how-to-wash-comforter-duvet/", "How to wash a comforter or duvet", "A practical guide for deciding between home washing and a large laundromat machine.", "Oversized & Household"],
  ["/resources/can-you-wash-area-rug/", "Can you wash an area rug?", "What to check before putting a rug in a washer, and when to ask first.", "Oversized & Household"],
  ["/resources/wash-sleeping-bag/", "How to wash a sleeping bag without ruining it", "A careful oversized-load guide for sleeping bags.", "Oversized & Household"],
  ["/resources/washing-pet-bedding/", "Washing pet bedding: what actually works", "Mechanical guidance without pest or health claims.", "Oversized & Household"],
  ["/resources/why-towels-smell/", "Why your towels smell, and how to fix it", "Residue, moisture, and washing habits explained plainly.", "Self-Service"],
  ["/resources/is-wash-and-fold-worth-it/", "Is wash and fold worth it?", "A decision page that argues both sides honestly.", "Wash & Fold"],
  ["/resources/laundry-care-symbols/", "Laundry care symbols, explained in plain English", "A reference page for washing, drying, bleaching, and ironing symbols.", "Ironing & Pressing"],
  ["/resources/how-often-wash-sheets-towels/", "How often should you wash sheets, towels and everything else?", "Frequency guidance for household laundry without overclaiming.", "Wash & Fold"],
  ["/resources/first-time-at-laundromat/", "First time at a laundromat: how it works", "A walk-through for people who have not used a laundromat before.", "Self-Service"],
  ["/resources/what-size-washer/", "What size washer do you need?", "How to think about washer capacity for bulky or everyday loads.", "Self-Service"],
  ["/resources/linen-management-short-term-rentals/", "Linen management for short-term rental hosts", "Operational laundry guidance for hosts with repeat turnover.", "Commercial"],
  ["/resources/towel-laundering-salons-barbershops/", "Towel laundering for salons and barbershops", "Commercial towel guidance without regulatory overreach.", "Commercial"]
];

const resourceIcons = {
  "/resources/can-you-wash-area-rug/": "areaRug",
  "/resources/first-time-at-laundromat/": "firstTime",
  "/resources/how-often-wash-sheets-towels/": "sheetsTowels",
  "/resources/how-to-wash-comforter-duvet/": "comforter",
  "/resources/is-wash-and-fold-worth-it/": "washFoldWorth",
  "/resources/laundry-care-symbols/": "laundrySymbols",
  "/resources/linen-management-short-term-rentals/": "shortTermRental",
  "/resources/towel-laundering-salons-barbershops/": "salon",
  "/resources/wash-sleeping-bag/": "sleepingBag",
  "/resources/washing-pet-bedding/": "petBedding",
  "/resources/what-size-washer/": "washerSize",
  "/resources/why-towels-smell/": "towelSmell"
};

page("/resources/", {
  title: "Laundry Resource Guides | Laundry Station",
  description: "Helpful laundry guides for comforters, area rugs, towels, symbols, washer size, wash and fold, and commercial laundry."
}, `
  ${pageHero({ title: "Laundry questions, answered plainly", lede: "Resource pages should be genuinely useful first, then route readers to the right Laundry Station service when the store can help.", cta: false, chips: ["Resource hub", "Helpful guides"] })}
  ${band({ title: "Guides", content: `<div class="content-grid content-grid-three">${resources.map(([href, title, summary, service]) => `<article class="info-card">${icon(resourceIcons[href] || "board")}<h3>${title}</h3><p>${summary}</p><span class="chip">${service}</span><a class="text-link" href="${href}">Read guide</a></article>`).join("")}</div>` })}
`);

for (const [href, title, summary, service] of resources) {
  page(href, {
    title: `${title} | Laundry Station`,
    description: summary
  }, `
    ${pageHero({ title, lede: summary, cta: false, chips: ["Resource", service] })}
    ${band({ title: "The short answer", content: `<div class="story-block"><p>This guide is scaffolded from the content plan and ready for full article copy. It should stay concrete, avoid invented claims, and hand off to ${service} only where Laundry Station genuinely helps.</p></div>` })}
    ${band({ title: "What the full article should cover", surface: "tint", content: cardGrid([
      { icon: resourceIcons[href] || "board", title: "The load type", body: "Give the reader a useful threshold, not a sales pitch." },
      { icon: "largeCapacity", title: "When a large machine helps", body: "Explain the mechanical reason: volume, movement, drying, or repeat load size." },
      { icon: "attendant", title: "When to ask first", body: "Flag materials, labels, and unresolved service policies honestly." }
    ], "three") })}
    ${band({ title: "Related service", content: serviceCards(services.filter((item) => item.title === service || item.title.includes(service.split(" ")[0])).slice(0, 1)) })}
    ${conversion("Need help with this load?")}
  `);
}

for (const [path, data] of pageMap) {
  render(path, data, data.body || "");
}
