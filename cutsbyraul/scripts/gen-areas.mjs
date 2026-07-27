/* ==========================================================================
   gen-areas.mjs — generates the Service Areas hub + 5 city landing pages
   as plain static HTML, per the TradeWorks AI city dev guides.
   Run:  node scripts/gen-areas.mjs
   Output: site/areas/index.html and site/areas/<slug>/index.html
   ========================================================================== */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE = path.join(__dirname, "..", "site");

const BOOKSY = "https://booksy.com/en-us/1195934_raulito-the-barber_barber-shop_15755_riverview";
const PHONE_TEL = "+13234043231";
const PHONE_DISP = "(323) 404-3231";
const IG = "https://instagram.com/cutzbyraul";
const MAP_EMBED = "https://maps.google.com/maps?q=7822%20US-301%20S%20Riverview%20FL%2033578&t=&z=15&ie=UTF8&iwloc=&output=embed";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

/* ---------- Shared chrome ---------- */
const NAV = `  <header class="nav is-scrolled" id="nav">
    <div class="nav__inner">
      <a class="brand" href="/" aria-label="Cutz by Raul home">CUTZ BY <b>RAUL</b></a>
      <nav class="nav__links" aria-label="Primary">
        <a class="nav__link" href="/">Home</a>
        <a class="nav__link" href="/services/">Services</a>
        <a class="nav__link" href="/gallery/">Gallery</a>
        <a class="nav__link" href="/about/">About</a>
        <a class="nav__link" href="/contact/">Contact</a>
      </nav>
      <div class="nav__actions">
        <a class="nav__phone" href="tel:${PHONE_TEL}" data-ga="phone_click" data-section="nav">
          <svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.24 1l-2.24 2.2z"/></svg>
          ${PHONE_DISP}
        </a>
        <a class="btn btn--primary nav__cta" href="#" data-book data-section="nav">Book Now</a>
        <a class="nav__phone-mobile" href="tel:${PHONE_TEL}" data-ga="phone_click" data-section="nav" aria-label="Call ${PHONE_DISP}">
          <svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.24 1l-2.24 2.2z"/></svg>
        </a>
        <button class="nav__toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="navOverlay">
          <svg class="icon" viewBox="0 0 24 24" stroke-width="2" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>
  </header>

  <div class="nav__overlay" id="navOverlay" role="dialog" aria-modal="true" aria-label="Menu">
    <button class="nav__close" id="navClose" aria-label="Close menu">
      <svg class="icon" viewBox="0 0 24 24" stroke-width="2" aria-hidden="true"><line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/></svg>
    </button>
    <a href="/">Home</a><a href="/services/">Services</a><a href="/gallery/">Gallery</a><a href="/about/">About</a><a href="/contact/">Contact</a>
    <a class="btn btn--primary" href="#" data-book data-section="mobile_menu">Book Now</a>
  </div>`;

const FOOTER = `  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__col footer__brand">
          <a class="brand" href="/">CUTZ BY <b>RAUL</b></a>
          <p class="footer__tag">Riverview's Trusted Barber.</p>
          <a class="social" href="${IG}" target="_blank" rel="noopener" aria-label="Follow Cutz by Raul on Instagram">
            <svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s0 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58 0-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.8 3.8 0 0 1-1.38-.9 3.8 3.8 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.21 15.58 2.2 15.2 2.2 12s0-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.21 8.8 2.2 12 2.2zm0 1.8c-3.15 0-3.5 0-4.74.07-.9.04-1.38.19-1.7.32-.43.16-.74.36-1.06.68-.32.32-.52.63-.68 1.06-.13.32-.28.8-.32 1.7C3.43 8.95 3.42 9.3 3.42 12s0 3.05.07 4.74c.04.9.19 1.38.32 1.7.16.43.36.74.68 1.06.32.32.63.52 1.06.68.32.13.8.28 1.7.32 1.24.07 1.59.07 4.74.07s3.5 0 4.74-.07c.9-.04 1.38-.19 1.7-.32.43-.16.74-.36 1.06-.68.32-.32.52-.63.68-1.06.13-.32.28-.8.32-1.7.07-1.24.07-1.59.07-4.74s0-3.05-.07-4.74c-.04-.9-.19-1.38-.32-1.7a2.85 2.85 0 0 0-.68-1.06 2.85 2.85 0 0 0-1.06-.68c-.32-.13-.8-.28-1.7-.32C15.5 4 15.15 4 12 4zm0 3.06A4.94 4.94 0 1 1 7.06 12 4.94 4.94 0 0 1 12 7.06zm0 8.15A3.21 3.21 0 1 0 8.79 12 3.21 3.21 0 0 0 12 15.21zm6.29-8.35a1.15 1.15 0 1 1-1.15-1.15 1.15 1.15 0 0 1 1.15 1.15z"/></svg>
          </a>
        </div>
        <div class="footer__col"><h4>Quick Links</h4><ul><li><a href="/">Home</a></li><li><a href="/services/">Services</a></li><li><a href="/gallery/">Gallery</a></li><li><a href="/areas/">Service Areas</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li></ul></div>
        <div class="footer__col"><h4>Visit</h4><address><a href="tel:${PHONE_TEL}" data-ga="phone_click" data-section="footer">${PHONE_DISP}</a><br>7822 US-301 S<br>Riverview, FL 33578<br><br>Mon–Fri 9–7 · Sat 9–6 · Sun 9–2</address></div>
        <div class="footer__col"><h4>Book Today</h4><a class="btn btn--primary" href="#" data-book data-section="footer">Book Now</a></div>
      </div>
      <div class="footer__bottom">
        <span>© 2026 Cutz by Raul. All rights reserved.</span>
        <nav aria-label="Legal"><a href="/privacy-policy/">Privacy Policy</a><a href="/terms-of-service/">Terms of Service</a><a href="https://tradeworksai.com" target="_blank" rel="noopener">Website by TradeWorks AI</a></nav>
      </div>
    </div>
  </footer>

  <div class="sticky-cta" id="stickyCta" aria-hidden="true">
    <a class="btn btn--primary btn--book" href="#" data-book data-section="sticky_bar">Book Now</a>
    <a class="btn btn--outline-light btn--call" href="tel:${PHONE_TEL}" data-ga="phone_click" data-section="sticky_bar">Call</a>
  </div>

  <script src="/js/main.js" defer></script>`;

const FONTS = `  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Montserrat:wght@500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/css/styles.css" />`;

const SERVICES = [
  ["Male Haircut", "$30"], ["Kids Haircut", "$25"], ["Haircut + Eyebrows", "$35"],
  ["Haircut + Beard", "$40"], ["Haircut + Beard + Eyebrows", "$45"],
  ["Haircut + Beard + Hot Towel", "$50"], ["Head Shave", "$30"], ["Beard Shaping", "$20"],
];

function compactServices(cityName) {
  return SERVICES.map(([n, p]) => `          <div class="svc-compact">
            <span class="svc-compact__name">${esc(n)}</span>
            <span class="svc-compact__price">${p}</span>
            <a href="#" data-book data-section="city_services" data-service="${esc(n)}">Book →</a>
          </div>`).join("\n");
}

/* ---------- City pages ---------- */
const CITIES = [
  {
    slug: "brandon", name: "Brandon", drive: "~8 minutes", pop: "119,000+", zips: "33510, 33511",
    title: "Barber in Brandon, FL | Cutz by Raul | Book Online",
    meta: "Brandon residents: professional haircuts, beard grooming & kids' cuts just 8 minutes away at Blessed by Blends in Riverview. 5.0★ rated. Book online with Raul.",
    h1: "Professional Barber Serving Brandon, FL",
    aeo: "Cutz by Raul provides professional barber services to Brandon, Florida residents from Blessed by Blends Barber Studio, located just 8 minutes south on US-301 in Riverview. Brandon's 119,000 residents have access to precision haircuts starting at $30, expert beard grooming, and patient kids' cuts — all bookable online through Booksy. Whether you live near the Westfield Brandon mall, along Providence Road, or in the neighborhoods off Bloomingdale Avenue, Raul's studio is a quick, straight drive down 301.",
    context: [
      ["Brandon's Largest Suburb, One Trusted Barber", ["Brandon is the largest community in eastern Hillsborough County, with over 119,000 residents making it the 19th largest in Florida. It's a diverse, fast-growing area where roughly 30% of residents are Hispanic or Latino and the median age is 37 — exactly the demographic that values a skilled, reliable barber. Despite its size, Brandon has no barber with a dedicated personal website, which means residents searching for “barber in Brandon FL” are getting generic Google Business Profile listings instead of a real look at the barber's work and reputation."]],
      ["A Quick Drive Down 301", ["The studio at 7822 US-301 S sits directly on the corridor that connects Brandon to Riverview. For clients coming from the Westfield Brandon mall area, the Providence Lakes neighborhood, or the Bloomingdale corridor, it's a straight shot down 301 with no interstate traffic. At 8 minutes in normal conditions, it's closer than many Brandon restaurants. And unlike the shops along 301 in Brandon proper, Blessed by Blends is appointment-first through Booksy — meaning no walk-in wait and no wasted time."]],
      ["Built for Brandon's Working Professionals", ["Brandon has one of the highest rates of remote and hybrid workers in the state, with over 16% of residents working from home in knowledge-based professions. That means flexible schedules and midday availability — perfect for squeezing in a 30-minute cut during a lunch break. Raul's seven-day schedule (including Sundays until 2 PM) accommodates the Monday-through-Friday professionals who can't make weekday appointments as well as the remote workers who prefer off-peak hours."]],
      ["Families in Brandon", ["With a median age of 37 and strong school enrollment across Burns Middle, Brandon High, and Limona Elementary, Brandon is full of families with kids who need regular haircuts. Parents searching for a patient, kid-friendly barber consistently name Raul in their Booksy reviews. His $25 kids' cuts are popular with Brandon families who've grown tired of the rushed, impersonal chain-salon experience and want someone who genuinely cares about their child's comfort."]],
    ],
    drv: "Approximately 8 minutes via US-301 South or Bloomingdale Avenue",
    drvText: "From central Brandon, head south on US-301 (Falkenburg Road merges into 301). The studio is at 7822 US-301 S in the plaza on the right, about 4 miles south of the Brandon Town Center area. Alternatively, take Bloomingdale Avenue west to US-301 and turn left. Either route avoids I-75.",
    dirUrl: "https://www.google.com/maps/dir/Brandon,+FL/7822+US-301+S+Riverview+FL+33578",
    faq: [
      ["How far is Cutz by Raul from Brandon, FL?", "The studio is approximately 8 minutes from central Brandon via US-301 South. It's a straight drive with no interstate required. The address is 7822 US-301 S in Riverview, FL 33578, inside Blessed by Blends Barber Studio."],
      ["Is there a good barber near Westfield Brandon mall?", "Cutz by Raul at Blessed by Blends is about 4 miles south of the Westfield Brandon area on US-301. Raul is a 5.0-rated barber on Booksy specializing in fades, beard grooming, and kids' cuts. Appointments can be booked online through Booksy."],
      ["Does Raul accept Brandon clients on Sundays?", "Yes. Cutz by Raul is open seven days a week, including Sundays from 9 AM to 2 PM. This is especially convenient for Brandon professionals with busy weekday schedules."],
      ["What's the best route from Brandon to Blessed by Blends?", "The most direct route is south on US-301. From the Brandon Town Center area, take US-301 (Falkenburg) southbound for about 4 miles. The studio is on the right in a plaza at 7822 US-301 S. You can also take Bloomingdale Avenue west to US-301 and turn left."],
    ],
    cta: "Brandon Residents — Book Your Appointment Today.",
  },
  {
    slug: "valrico", name: "Valrico", drive: "~12 minutes", pop: "40,000+", zips: "33594, 33596",
    title: "Barber Near Valrico, FL | Cutz by Raul | Book Online",
    meta: "Valrico families: precision haircuts, beard grooming & patient kids' cuts 12 minutes away in Riverview. 5.0★ rated barber. Book online with Raul.",
    h1: "Your Barber Near Valrico, FL",
    aeo: "Cutz by Raul offers professional barber services to Valrico, Florida residents from Blessed by Blends Barber Studio in nearby Riverview, approximately 12 minutes west via Bloomingdale Avenue. Valrico's 40,000 residents can book precision haircuts from $30, beard shaping from $20, and patient kids' cuts for $25 through Booksy. Raul is known for his family-friendly approach, making him a natural fit for Valrico's community of families and established homeowners along Durant Road, Buckhorn, and the Bloomingdale corridor.",
    context: [
      ["Valrico: Where Families Put Down Roots", ["Valrico is one of the most family-oriented communities in Hillsborough County. With a median age of 44.5, a median household income over $104,000, and a homeownership rate that far exceeds the county average, Valrico is a place where families settle in for the long term. Over 22% of households have children under 18, and the highly rated public schools — Valrico Elementary, Buckhorn Elementary, Mulrennan Middle, and Bloomingdale High — are a major draw. For a barber, this means a community of repeat clients: dads who come in biweekly, sons who need a fresh cut before picture day, and families looking for a barber they can trust across generations."]],
      ["Close Enough to Be Convenient", ["At 12 minutes from central Valrico, Blessed by Blends is well within the radius most Valrico residents already travel for everyday errands. The Bloomingdale Avenue corridor connects Valrico directly to US-301, where the studio is located. For residents along Durant Road or near Buckhorn, it's a familiar westbound route with no highway required. Many Valrico residents already drive to Riverview or Brandon for dining and shopping — adding a barber appointment to that routine is seamless."]],
      ["Higher Income, Higher Expectations", ["Valrico's household income ranks well above the Hillsborough County median, and that financial comfort translates into expectations for quality. Valrico clients aren't looking for the cheapest haircut — they're looking for the best one. Raul's premium services, like the $50 Haircut + Beard + Hot Towel experience, are designed for exactly this audience: people who value craftsmanship, cleanliness, and a barber who takes time rather than rushing to the next client."]],
      ["A Quieter Alternative to Chain Salons", ["Valrico residents have access to the chain salons and walk-in shops along SR-60 and the Brandon corridor, but the experience at those locations rarely matches the expectations of Valrico's homeowner demographic. A dedicated barber with a personal reputation, a perfect 5.0 rating, and an appointment-based model offers a fundamentally different experience. Raul's studio at Blessed by Blends is clean, welcoming, and personal — the kind of place Valrico families recommend to their neighbors."]],
    ],
    drv: "Approximately 12 minutes via Bloomingdale Avenue or SR-60 to US-301",
    drvText: "From central Valrico near Durant Road, take Bloomingdale Avenue west or SR-60 (Brandon Boulevard) west to US-301, then head south on 301. The studio is at 7822 US-301 S on the right. From the Buckhorn Road area, take Lithia Pinecrest Road south to Bloomingdale, then west to 301.",
    dirUrl: "https://www.google.com/maps/dir/Valrico,+FL/7822+US-301+S+Riverview+FL+33578",
    faq: [
      ["How far is Cutz by Raul from Valrico, FL?", "The studio is approximately 12 minutes from central Valrico via Bloomingdale Avenue to US-301 South. The address is 7822 US-301 S in Riverview, FL 33578, inside Blessed by Blends Barber Studio."],
      ["Is there a barber near Valrico good with kids?", "Yes. Raul Galeano at Cutz by Raul is consistently praised for his patience with children, from toddlers to pre-teens. His studio is 12 minutes from Valrico, and kids' haircuts are $25 for a 30-minute appointment. Book through Booksy."],
      ["What are the best barber services for Valrico professionals?", "Raul's most popular service for professionals is the Haircut + Beard package at $40, or the premium Haircut + Beard + Hot Towel at $50 for the full experience. Appointments are available seven days a week, including Sundays, to fit around demanding work schedules."],
      ["What's the best route from Valrico to Blessed by Blends?", "From central Valrico, take Bloomingdale Avenue west until it reaches US-301 in Riverview. Turn left (south) on 301 and the studio is on the right at 7822 US-301 S. From the Buckhorn Road area, take Lithia Pinecrest Road south to Bloomingdale Avenue, then head west to 301."],
    ],
    cta: "Valrico Residents — Book Your Appointment Today.",
  },
  {
    slug: "fishhawk", name: "FishHawk", drive: "~10 minutes", pop: "24,000+", zips: "33547",
    title: "Barber Near FishHawk, FL | Cutz by Raul | Book Online",
    meta: "FishHawk families: precision haircuts, beard grooming & patient kids' cuts 10 minutes away in Riverview. 5.0★ rated. Book with Raul at Blessed by Blends.",
    h1: "Barber Serving FishHawk Ranch & Lithia, FL",
    aeo: "Cutz by Raul provides professional barber services to FishHawk Ranch residents from Blessed by Blends Barber Studio, located just 10 minutes west on US-301 in Riverview, Florida. FishHawk's 24,000 residents have access to precision haircuts from $30, expert beard grooming from $20, and patient kids' cuts at $25 — all bookable online through Booksy. From the Lake House to Osprey Club and across every village in FishHawk Ranch, a trusted barber is a quick drive down FishHawk Boulevard.",
    context: [
      ["FishHawk Ranch: A Community That Expects Quality", ["FishHawk Ranch is a master-planned community spanning over 3,000 acres in Lithia, Florida, with approximately 24,000 residents across multiple distinct villages. With a median household income of $141,000 — the highest among all communities Raul serves — FishHawk residents have clear expectations for quality and professionalism. The community's resort-style amenities, including the Lake House fitness center, the Aquatic Center, Osprey Club, and 25-mile nature trail, reflect a standard of living that extends to every service residents choose, including their barber."]],
      ["Families, Schools, and Saturday Morning Haircuts", ["FishHawk is one of the most family-dense communities in eastern Hillsborough County. Newsome High School, FishHawk Creek Elementary, Bevis Elementary, and Barrington Middle School are all A-rated institutions that draw families to the area specifically for education quality. This concentration of families means a steady demand for two of Raul's strongest services: kids' haircuts and father-son appointment blocks. Parents in FishHawk regularly book Raul for Saturday morning back-to-back appointments — dad gets the Haircut + Beard while the son gets a clean cut at the same visit."]],
      ["Ten Minutes, No Highway Required", ["Despite feeling tucked away from the commercial corridors, FishHawk Ranch is surprisingly close to Blessed by Blends. FishHawk Boulevard runs directly west from the community to US-301, where the studio sits. The entire drive is surface streets with consistent traffic flow — no I-75 merge, no Brandon congestion, no construction zones. Residents coming from the Encore 55+ village, the Starling neighborhood, or anywhere along FishHawk Boulevard are looking at a comfortable 10-minute drive with free parking on arrival."]],
      ["Beyond the Chain Salon Experience", ["FishHawk's Village Center on FishHawk Boulevard offers convenience retail and dining, but barbershop options within the community itself are limited. Most FishHawk residents currently drive to Brandon or Riverview for barber services anyway. Raul offers something the generic walk-in shops along that corridor don't: a personal relationship with your barber, a perfect 5.0 rating built on genuine client satisfaction, and an appointment model that respects your time. For a community accustomed to premium HOA amenities and curated experiences, that distinction matters."]],
    ],
    drv: "Approximately 10 minutes via FishHawk Boulevard to US-301",
    drvText: "From FishHawk Ranch, take FishHawk Boulevard west to US-301 (about 3 miles). Turn left (south) on US-301 and the studio is on the right at 7822 US-301 S. From Fish Hawk Trails or the Boyette Road area, take Boyette Road west to US-301 and turn right. Both routes avoid I-75 entirely.",
    dirUrl: "https://www.google.com/maps/dir/FishHawk,+FL/7822+US-301+S+Riverview+FL+33578",
    faq: [
      ["How far is Cutz by Raul from FishHawk Ranch?", "The studio is approximately 10 minutes from FishHawk Ranch via FishHawk Boulevard to US-301. It's a straight surface-street drive with no highway required. The address is 7822 US-301 S in Riverview, FL 33578."],
      ["Is there a barber near FishHawk good with kids?", "Yes. Raul Galeano is consistently praised by parents for his patience with children of all ages, from first haircuts to pre-teen fades. Kids' haircuts are $25. Many FishHawk families book back-to-back father-son appointments on Saturday mornings."],
      ["Can FishHawk residents book a barber online?", "Yes. Cutz by Raul uses Booksy for all appointments. FishHawk residents can browse available times, select their service, and book in under a minute from their phone. No walk-in wait required."],
      ["What route should I take from FishHawk to Blessed by Blends?", "Take FishHawk Boulevard west approximately 3 miles to US-301. Turn left (south) on 301 and the studio is on the right at 7822 US-301 S. From Fish Hawk Trails or the Boyette Road area, take Boyette west to 301 and turn right."],
    ],
    cta: "FishHawk Residents — Book Your Appointment Today.",
    crossLink: { href: "/areas/lithia/", text: "Looking for the broader area? See our Lithia barber page →" },
  },
  {
    slug: "bloomingdale", name: "Bloomingdale", drive: "~7 minutes", pop: "25,000+", zips: "33511, 33596",
    title: "Barber Near Bloomingdale, FL | Cutz by Raul | Book Online",
    meta: "Bloomingdale residents: professional haircuts & beard grooming just 7 minutes south on US-301. 5.0★ rated barber at Blessed by Blends. Book online with Raul.",
    h1: "Your Barber Near Bloomingdale, FL",
    aeo: "Cutz by Raul serves Bloomingdale, Florida residents from Blessed by Blends Barber Studio on US-301 in Riverview, just 7 minutes south via Bloomingdale Avenue. Bloomingdale's 25,000 residents can book precision haircuts starting at $30, beard shaping from $20, and kids' cuts for $25 online through Booksy. Located at the intersection of the Brandon, Riverview, and Valrico communities, Bloomingdale residents are closer to Raul's studio than most of their daily errands.",
    context: [
      ["Bloomingdale: The Crossroads of Eastern Hillsborough", ["Bloomingdale is an unincorporated community of approximately 25,000 residents nestled between Brandon to the north, Riverview to the west, Valrico to the east, and FishHawk to the south. Its position at the crossroads of Bloomingdale Avenue and Bell Shoals Road makes it one of the most centrally located communities in eastern Hillsborough County. Despite being surrounded by larger neighbors, Bloomingdale has maintained a distinct residential character since its establishment around 1850, with steady growth over the past two decades transforming it into one of the area's most desirable suburban enclaves."]],
      ["Established Families, Consistent Grooming Needs", ["With a median age of 41 and a median household income of $107,000, Bloomingdale skews toward established homeowners and dual-income families. Over 60% of households are married-couple families, and roughly 36% have children under 18. This demographic profile produces exactly the kind of client base that builds a barber's livelihood: dads on a biweekly schedule, kids needing cuts before school events, and professionals who want a barber they can trust without a long drive. Bloomingdale's 19% Hispanic population also aligns well with Raul's bilingual capability."]],
      ["Seven Minutes — Closer Than the Grocery Store", ["Bloomingdale's proximity to Blessed by Blends is its strongest advantage. At just 7 minutes via Bloomingdale Avenue to US-301, the studio is closer to central Bloomingdale than most residents' regular shopping destinations in Brandon. The route is a single arterial road with no highway merging, and parking is free in the plaza lot. For residents along Bell Shoals Road, Nature's Way, or the neighborhoods between Bloomingdale Avenue and Lithia Pinecrest Road, the drive is practically a neighborhood errand."]],
      ["A Growing, Diversifying Community", ["Bloomingdale has seen increasing diversity over the past decade, with its demographics shifting to reflect the broader Tampa Bay trend toward a more multicultural population. The 2024 census data shows 64% White, 19% Hispanic, and 10% Black residents. This growing diversity creates demand for a barber who understands different hair textures, cultural style preferences, and the importance of a welcoming environment for everyone. Raul's experience across a wide range of hair types and his bilingual Spanish-English communication make him a natural fit for Bloomingdale's evolving community."]],
    ],
    drv: "Approximately 7 minutes via Bloomingdale Avenue to US-301 South",
    drvText: "From central Bloomingdale near the Bloomingdale Avenue and Bell Shoals Road intersection, head south on Bell Shoals which becomes Lithia Pinecrest Road, then west on Bloomingdale Avenue to US-301. Turn left on 301 and the studio is on the right. Alternatively, take Bloomingdale Avenue directly west to US-301 — a single-turn route that takes about 7 minutes.",
    dirUrl: "https://www.google.com/maps/dir/Bloomingdale,+FL/7822+US-301+S+Riverview+FL+33578",
    faq: [
      ["How far is Cutz by Raul from Bloomingdale, FL?", "Just 7 minutes via Bloomingdale Avenue to US-301 South. Blessed by Blends Barber Studio is at 7822 US-301 S in Riverview — one of the closest barber options for Bloomingdale residents."],
      ["Is there a barber near Bell Shoals Road in Bloomingdale?", "Cutz by Raul at Blessed by Blends is about 7 minutes from the Bell Shoals and Bloomingdale Avenue area. Raul offers precision haircuts, beard grooming, and kids' cuts with a 5.0 Booksy rating. Book online through Booksy."],
      ["Does the barber near Bloomingdale speak Spanish?", "Yes. Raul is bilingual in English and Spanish and has served many Spanish-speaking clients. His Booksy reviews include feedback from both English and Spanish-speaking customers praising his professionalism and skill."],
      ["What is the quickest route from Bloomingdale to the barbershop?", "Take Bloomingdale Avenue west to US-301. Turn left (south) on 301 and the studio is on the right at 7822 US-301 S. It's a single-turn route that takes approximately 7 minutes with free parking on arrival."],
    ],
    cta: "Bloomingdale Residents — Book Your Appointment Today.",
  },
  {
    slug: "lithia", name: "Lithia", drive: "~15 minutes", pop: "32,000+", zips: "33547",
    title: "Barber Near Lithia, FL | Cutz by Raul | Book Online",
    meta: "Lithia residents: professional haircuts, beard grooming & kids' cuts at Blessed by Blends in Riverview. 15 minutes away. 5.0★ rated. Book online with Raul.",
    h1: "Professional Barber Serving Lithia, FL",
    aeo: "Cutz by Raul provides professional barber services to Lithia, Florida residents from Blessed by Blends Barber Studio on US-301 in Riverview, approximately 15 minutes northwest via Lithia Pinecrest Road. Lithia's 32,000 residents across the Hawkstone, Fish Hawk Trails, and rural homestead communities can book precision haircuts from $30, expert beard grooming, and patient kids' cuts through Booksy. Whether you're coming from Lithia Springs Park, the Alafia River corridor, or anywhere in ZIP 33547, Raul's studio is the closest dedicated barber experience.",
    context: [
      ["Lithia: Rural Roots, Growing Community", ["Lithia is an unincorporated community in southeastern Hillsborough County with approximately 32,000 residents spread across a mix of master-planned developments, established homesteads, and rural acreage. Historically known for agriculture, phosphate mining, and sawmills, Lithia has transformed over the past two decades into one of Tampa Bay's most desirable suburban-rural communities. The area maintains a distinctly different character from the denser Brandon and Riverview corridors — more space between homes, more tree canopy, more land. Residents here chose Lithia intentionally for its quieter pace."]],
      ["Three Distinct Neighborhoods, One Barber", ["Lithia encompasses three major residential areas, each with its own identity. FishHawk Ranch (covered separately on our FishHawk page) is the master-planned community with resort amenities. Fish Hawk Trails, developed independently in the mid-1990s, offers established single-family homes in a more traditional subdivision layout. And Hawkstone is a gated community with larger executive homes averaging over 4,000 square feet. Beyond these developments, Lithia includes rural properties along the Alafia River corridor where five-acre lots are common. Raul's studio serves clients across all three communities and the surrounding homesteads."]],
      ["Outdoor Lifestyle, Regular Grooming", ["Lithia residents are outdoor people. Lithia Springs Park, Alderman Ford Conservation Park, and Alafia River State Park provide hiking, kayaking, horseback riding, and mountain biking within minutes. The R&R Ranch offers guided horseback tours. FishHawk Sporting Clays draws shooting enthusiasts. River Hills Country Club serves golfers, tennis players, and swimmers. This active outdoor lifestyle means Lithia clients often arrive after a morning on the trails or a round of golf — they want a barber who can clean up quickly and efficiently. Raul's 30-minute haircut appointment fits perfectly into an active day."]],
      ["Limited Local Options, Worth the Drive", ["Lithia's rural-suburban character means barbershop options within the community itself are virtually nonexistent. Residents routinely drive to Brandon or Riverview for services of all kinds. At 15 minutes, Blessed by Blends is well within the driving radius Lithia residents already accept for grocery shopping, dining, and errands. And unlike the walk-in shops along the Brandon corridor, Raul offers an appointment-based model that eliminates wait time — especially valuable for clients who've just driven 15 minutes and don't want to spend another 20 waiting."]],
    ],
    drv: "Approximately 15 minutes via Lithia Pinecrest Road or FishHawk Boulevard to US-301",
    drvText: "From central Lithia near Lithia Springs Park, take Lithia Pinecrest Road north to Bloomingdale Avenue, then west to US-301. Turn left on 301 and the studio is on the right at 7822 US-301 S. From the Boyette Road area (south Lithia), take Boyette west to US-301. From areas near Alafia River State Park, take CR-39 north to Bloomingdale Avenue.",
    dirUrl: "https://www.google.com/maps/dir/Lithia,+FL/7822+US-301+S+Riverview+FL+33578",
    faq: [
      ["How far is Cutz by Raul from Lithia, FL?", "Approximately 15 minutes from central Lithia via Lithia Pinecrest Road to Bloomingdale Avenue to US-301. The address is 7822 US-301 S in Riverview, FL 33578 inside Blessed by Blends Barber Studio."],
      ["Is there a barber near Lithia Springs Park?", "Cutz by Raul at Blessed by Blends is the closest dedicated barber to the Lithia Springs area, about 15 minutes northwest on US-301 in Riverview. Raul offers precision haircuts, beard grooming, and kids' cuts with a perfect 5.0 rating on Booksy."],
      ["Do Lithia residents need to book in advance?", "Yes, appointments are recommended through Booksy to guarantee your time slot. This is especially important for Lithia residents making the 15-minute drive — booking ahead ensures no wait time on arrival."],
      ["What's the best route from Lithia to Blessed by Blends?", "From central Lithia near Lithia Springs Park, take Lithia Pinecrest Road north to Bloomingdale Avenue, then head west to US-301 and turn left. From southern Lithia or the Boyette Road area, take Boyette west directly to US-301 and turn right. Both routes are surface streets with free parking at the studio."],
    ],
    cta: "Lithia Residents — Book Your Appointment Today.",
    crossLink: { href: "/areas/fishhawk/", text: "Live in FishHawk Ranch? See our dedicated FishHawk barber page →" },
  },
];

function faqJsonLd(faq) {
  return JSON.stringify(faq.map(([q, a]) => ({
    "@type": "Question", name: q, acceptedAnswer: { "@type": "Answer", text: a },
  })));
}

function cityPage(c) {
  const contextHtml = c.context.map(([h, ps]) =>
    `          <h2>${esc(h)}</h2>\n` + ps.map((p) => `          <p>${esc(p)}</p>`).join("\n")
  ).join("\n");

  const faqHtml = c.faq.map(([q, a], i) =>
    `          <details${i === 0 ? " open" : ""}><summary>${esc(q)}</summary><p>${esc(a)}</p></details>`
  ).join("\n");

  const crossLinkHtml = c.crossLink
    ? `\n          <p style="margin-top:var(--sp-6)"><a href="${c.crossLink.href}">${esc(c.crossLink.text)}</a></p>`
    : "";

  const schema = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Service",
        serviceType: "Barber Services",
        provider: { "@id": "https://cutzbyraul.com/#barbershop" },
        areaServed: { "@type": "Place", name: c.name, containedInPlace: { "@type": "State", name: "Florida" } },
        description: `Professional haircuts, beard grooming, and kids' cuts for ${c.name}, FL residents at Blessed by Blends Barber Studio in Riverview.`,
        url: `https://cutzbyraul.com/areas/${c.slug}/`,
      },
      {
        "@type": "BreadcrumbList",
        itemListElement: [
          { "@type": "ListItem", position: 1, name: "Home", item: "https://cutzbyraul.com/" },
          { "@type": "ListItem", position: 2, name: "Service Areas", item: "https://cutzbyraul.com/areas/" },
          { "@type": "ListItem", position: 3, name: c.name, item: `https://cutzbyraul.com/areas/${c.slug}/` },
        ],
      },
      { "@type": "FAQPage", mainEntity: JSON.parse(faqJsonLd(c.faq)) },
    ],
  };

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>${esc(c.title)}</title>
  <meta name="description" content="${esc(c.meta)}" />
  <link rel="canonical" href="https://cutzbyraul.com/areas/${c.slug}/" />
  <meta name="robots" content="index, follow" />
  <meta name="theme-color" content="#1A1A2E" />

  <meta property="og:title" content="${esc(c.title)}" />
  <meta property="og:description" content="${esc(c.meta)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://cutzbyraul.com/areas/${c.slug}/" />
  <meta property="og:image" content="https://cutzbyraul.com/images/og-homepage.jpg" />
  <meta property="og:site_name" content="Cutz by Raul" />

${FONTS}

  <script type="application/ld+json">
  ${JSON.stringify(schema, null, 2).split("\n").join("\n  ")}
  </script>
</head>

<body data-booksy="${BOOKSY}" data-instagram="${IG}">

  <a class="skip-link" href="#main">Skip to content</a>

${NAV}

  <main id="main">

    <!-- CITY HERO -->
    <section class="subhero">
      <div class="container">
        <p class="breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/areas/">Service Areas</a><span class="sep">/</span><span aria-current="page">${esc(c.name)}</span></p>
        <h1 class="h1">${esc(c.h1)}</h1>
        <p class="subhero__lead">${esc(c.aeo)}</p>
      </div>
    </section>

    <!-- LOCAL CONTEXT -->
    <section class="section section--offwhite">
      <div class="container">
        <div class="prose">
${contextHtml}${crossLinkHtml}
        </div>
      </div>
    </section>

    <!-- SERVICES AVAILABLE -->
    <section class="section section--linen">
      <div class="container">
        <h2 class="h2 text-center">Barber Services Available to ${esc(c.name)} Clients</h2>
        <div class="svc-compact-grid">
${compactServices(c.name)}
        </div>
        <div class="section__cta"><a class="link-cta" href="/services/">View Full Service Details
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>
      </div>
    </section>

    <!-- GETTING HERE -->
    <section class="section section--offwhite">
      <div class="container">
        <div class="contact-grid directions">
          <div>
            <h2 class="h2 h2--display">Getting to Cutz by Raul from ${esc(c.name)}</h2>
            <p class="directions__drive">Drive time: ${esc(c.drv)}</p>
            <p>${esc(c.drvText)}</p>
            <a class="btn btn--outline-dark btn--sm" href="${c.dirUrl}" target="_blank" rel="noopener" data-ga="directions_click" data-section="city_${c.slug}">Get Directions from ${esc(c.name)} →</a>
            <p class="location__park">Free parking available in the plaza lot at 7822 US-301 S.</p>
          </div>
          <div class="location__map-wrap">
            <iframe class="location__map" title="Map to Blessed by Blends Barber Studio, 7822 US-301 S, Riverview, FL"
              src="${MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section section--linen">
      <div class="container">
        <h2 class="h2 text-center">${esc(c.name)} Barber FAQ</h2>
        <div class="faq">
${faqHtml}
        </div>
      </div>
    </section>

    <!-- CTA BAR -->
    <section class="cta-bar">
      <div class="container cta-bar__inner">
        <h3>${esc(c.cta)}</h3>
        <div class="cta-bar__btns">
          <a class="btn btn--on-dark" href="#" data-book data-section="final_cta">Book Your Appointment</a>
          <a class="btn btn--outline-dark" href="tel:${PHONE_TEL}" data-ga="phone_click" data-section="final_cta">Call ${PHONE_DISP}</a>
        </div>
      </div>
    </section>
  </main>

${FOOTER}
</body>
</html>
`;
}

/* ---------- Areas hub ---------- */
function hubPage() {
  const hubCities = [
    { name: "Riverview", pop: "95,000+", drive: "Home Base", zips: "33578, 33569", href: "/" },
    { name: "Brandon", pop: "119,000+", drive: "~8 minutes", zips: "33510, 33511", href: "/areas/brandon/" },
    { name: "Valrico", pop: "40,000+", drive: "~12 minutes", zips: "33594, 33596", href: "/areas/valrico/" },
    { name: "FishHawk", pop: "24,000+", drive: "~10 minutes", zips: "33547", href: "/areas/fishhawk/" },
    { name: "Bloomingdale", pop: "25,000+", drive: "~7 minutes", zips: "33511, 33596", href: "/areas/bloomingdale/" },
    { name: "Lithia", pop: "32,000+", drive: "~15 minutes", zips: "33547", href: "/areas/lithia/" },
  ];

  const cards = hubCities.map((c) => `          <a class="city-card" href="${c.href}"${c.href === "/" ? "" : ' data-ga="area_card"'}>
            <span>
              <span class="city-card__name">${esc(c.name)}</span><br>
              <span class="city-card__drive">${esc(c.drive)}</span><br>
              <span class="city-card__meta">${esc(c.pop)} residents · ${esc(c.zips)}</span>
            </span>
            <svg class="city-card__chev" viewBox="0 0 24 24" aria-hidden="true"><polyline points="9 6 15 12 9 18"/></svg>
          </a>`).join("\n");

  const schema = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BarberShop",
        "@id": "https://cutzbyraul.com/#barbershop",
        name: "Cutz by Raul — Raulito the Barber",
        url: "https://cutzbyraul.com/",
        areaServed: [
          { "@type": "City", name: "Riverview", containedInPlace: { "@type": "State", name: "Florida" } },
          { "@type": "City", name: "Brandon" },
          { "@type": "City", name: "Valrico" },
          { "@type": "City", name: "Lithia" },
          { "@type": "Place", name: "FishHawk" },
          { "@type": "Place", name: "Bloomingdale" },
        ],
      },
      {
        "@type": "BreadcrumbList",
        itemListElement: [
          { "@type": "ListItem", position: 1, name: "Home", item: "https://cutzbyraul.com/" },
          { "@type": "ListItem", position: 2, name: "Service Areas", item: "https://cutzbyraul.com/areas/" },
        ],
      },
    ],
  };

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>Service Areas | Barber Serving Riverview, Brandon, Valrico &amp; More | Cutz by Raul</title>
  <meta name="description" content="Cutz by Raul serves Riverview, Brandon, Valrico, FishHawk, Bloomingdale &amp; Lithia, FL. Professional barber services just minutes from your neighborhood. Book today." />
  <link rel="canonical" href="https://cutzbyraul.com/areas/" />
  <meta name="robots" content="index, follow" />
  <meta name="theme-color" content="#1A1A2E" />

  <meta property="og:title" content="Service Areas | Cutz by Raul | Eastern Hillsborough County" />
  <meta property="og:description" content="Serving Riverview, Brandon, Valrico, FishHawk, Bloomingdale & Lithia, FL. Book online with Raul." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://cutzbyraul.com/areas/" />
  <meta property="og:image" content="https://cutzbyraul.com/images/og-homepage.jpg" />
  <meta property="og:site_name" content="Cutz by Raul" />

${FONTS}

  <script type="application/ld+json">
  ${JSON.stringify(schema, null, 2).split("\n").join("\n  ")}
  </script>
</head>

<body data-booksy="${BOOKSY}" data-instagram="${IG}">

  <a class="skip-link" href="#main">Skip to content</a>

${NAV}

  <main id="main">

    <!-- HERO -->
    <section class="subhero">
      <div class="container">
        <p class="breadcrumb"><a href="/">Home</a><span class="sep">/</span><span aria-current="page">Service Areas</span></p>
        <h1 class="h1">Serving Riverview &amp; Surrounding Communities</h1>
        <p class="subhero__lead">Cutz by Raul is located at Blessed by Blends Barber Studio on US-301 in Riverview, Florida, serving clients across eastern Hillsborough County. Whether you're in Brandon, Valrico, FishHawk, Bloomingdale, or Lithia, professional haircuts, beard grooming, and kids' cuts are just minutes away. Select your area below to see how close you are.</p>
      </div>
    </section>

    <!-- MAP + CITY GRID -->
    <section class="section section--offwhite">
      <div class="container">
        <div class="areas-layout">
          <div class="areas-map-wrap">
            <iframe class="areas-map" title="Map of Blessed by Blends Barber Studio serving eastern Hillsborough County"
              src="${MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          </div>
          <div class="areas-cards">
${cards}
          </div>
        </div>
      </div>
    </section>

    <!-- WHY LOCAL -->
    <section class="section section--linen">
      <div class="container">
        <div class="prose" style="max-width:800px;text-align:center">
          <h2 style="font-family:var(--font-ui);font-size:var(--sp-8)">Why a Local Barber Matters</h2>
          <p>A great barber isn't someone you visit once — it's someone who knows your hair, your preferences, and your schedule. Located right on US-301 in Riverview, Cutz by Raul is centrally positioned in eastern Hillsborough County, making it easy for clients from Brandon, Valrico, FishHawk, Bloomingdale, and Lithia to maintain a regular grooming routine without a long commute. Free parking, flexible hours seven days a week, and online booking through Booksy make every visit effortless.</p>
        </div>
      </div>
    </section>

    <!-- CTA BAR -->
    <section class="cta-bar">
      <div class="container cta-bar__inner">
        <h3>Your Neighborhood, Your Barber. Book with Raul.</h3>
        <div class="cta-bar__btns">
          <a class="btn btn--on-dark" href="#" data-book data-section="final_cta">Book Your Appointment</a>
          <a class="btn btn--outline-dark" href="tel:${PHONE_TEL}" data-ga="phone_click" data-section="final_cta">Call ${PHONE_DISP}</a>
        </div>
      </div>
    </section>
  </main>

${FOOTER}
</body>
</html>
`;
}

/* ---------- Write files ---------- */
function writePage(relDir, html) {
  const dir = path.join(SITE, relDir);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, "index.html"), html);
  console.log("wrote", path.join(relDir, "index.html"));
}

writePage("areas", hubPage());
for (const c of CITIES) writePage(path.join("areas", c.slug), cityPage(c));
console.log("done — 1 hub + " + CITIES.length + " city pages");
