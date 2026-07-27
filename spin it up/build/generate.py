#!/usr/bin/env python3
"""
Spin It Up Laundry — static site generator (bilingual EN/ES).

A dev-time tool only. It wraps each page's unique <main> content (stored in
build/content/<key>.html) with the shared chrome (head, header, mobile menu,
footer, sticky CTA) and writes pure static HTML into site/. Nothing in the
shipped output depends on this script — deploy the contents of site/ as-is.

Each page in build/pages.json sets:
  out, active, title, description, canonical, ...
  lang     : "en" (default) or "es"
  alt      : URL of the other-language counterpart (drives language toggle + hreflang)
             (English pages may use legacy key "es"; Spanish pages use "en")
  hreflang : False to omit alternate-language <link>s

Usage:  python build/generate.py
"""
import os, json, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "build", "content")
SITE = os.path.join(ROOT, "site")

PHONE_TEL = "+17736541275"
PHONE_DISP = "(773) 654-1275"
CENTS = "https://app.trycents.com/new-order/YTYw/home"
MAPS_DIR = "https://www.google.com/maps/dir/?api=1&destination=3710+N+Kimball+Ave,+Chicago,+IL+60618"
REVIEW = "https://g.page/r/CVQzki5-O0I_EBM/review"

PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
CAL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'
HAMBURGER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>'
CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
FB = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>'
IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>'
YELP = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.27 2c.7 0 1.27.57 1.27 1.27v8.1c0 .9-1.13 1.3-1.7.6L7.6 6.9a1.27 1.27 0 0 1 .3-1.9A11 11 0 0 1 12.27 2z"/></svg>'

# Localized chrome strings + nav structures ----------------------------------
# nav entry: (label, href, key, [children]) ; child: (label, href)
CHROME = {
"en": {
  "skip": "Skip to content", "primary": "Primary", "menu": "Menu", "open_menu": "Open menu",
  "close_menu": "Close menu", "legal": "Legal", "schedule": "Schedule Pickup",
  "call": "Call %s" % PHONE_DISP, "call_now": "Call Now", "leave_review": "Leave a Review",
  "tagline": "Avondale's Largest Modern Laundromat.", "hours": "Open 6 AM–11 PM, 7 Days",
  "f_services": "Services", "f_company": "Company", "f_connect": "Connect",
  "about_us": "About Us", "contact": "Contact", "faq": "FAQ", "areas": "Service Areas",
  "view_pricing": "View Pricing", "rights": "© 2026 Spin It Up Laundry. All rights reserved. | Powered by TradeWorks AI.",
  "privacy": "Privacy Policy", "terms": "Terms of Service", "accessibility": "Accessibility",
  "lang_full": ("English", "Español"),
  "svc": [("Self-Service Laundry","/services/self-service/"),("Wash &amp; Fold","/services/wash-and-fold/"),
          ("Pickup &amp; Delivery","/services/pickup-delivery/"),("Commercial","/services/commercial/"),
          ("Ironing &amp; Pressing","/services/ironing-pressing/")],
  "areas_list": [("Avondale","/areas/avondale/"),("Irving Park","/areas/irving-park/"),
                 ("Logan Square","/areas/logan-square/"),("Hermosa","/areas/hermosa/"),("Albany Park","/areas/albany-park/")],
  "nav": [("Services","/services/","services",True),("Pricing","/pricing/","pricing",False),
          ("Areas We Serve","/areas/","areas",True),("About","/about/","about",False),
          ("FAQ","/faq/","faq",False),("Contact","/contact/","contact",False)],
  "footer_services": [("Self-Service Laundry","/services/self-service/"),("Wash &amp; Fold","/services/wash-and-fold/"),
          ("Pickup &amp; Delivery","/services/pickup-delivery/"),("Commercial Services","/services/commercial/"),
          ("Ironing &amp; Pressing","/services/ironing-pressing/"),("View Pricing","/pricing/")],
  "footer_company": [("About Us","/about/"),("Contact","/contact/"),("FAQ","/faq/"),("Service Areas","/areas/"),("Resources","/resources/")],
  "all_services": "All Services", "all_areas": "All Areas",
  "announce": ["🆓 FREE DRY WED & THU", "📶 FREE WI-FI", "☕ FREE COFFEE",
               "🅿️ FREE PARKING", "💳 EBT ACCEPTED", "📍 3710 N KIMBALL AVE, CHICAGO"],
},
"es": {
  "skip": "Saltar al contenido", "primary": "Navegación principal", "menu": "Menú", "open_menu": "Abrir menú",
  "close_menu": "Cerrar menú", "legal": "Legal", "schedule": "Programar Recogida",
  "call": "Llamar %s" % PHONE_DISP, "call_now": "Llamar Ahora", "leave_review": "Dejar una Reseña",
  "tagline": "La Lavandería Moderna Más Grande de Avondale.", "hours": "Abierto 6 AM–11 PM, Todos los Días",
  "f_services": "Servicios", "f_company": "Empresa", "f_connect": "Conéctese",
  "about_us": "Nosotros", "contact": "Contacto", "faq": "Preguntas Frecuentes", "areas": "Áreas de Servicio",
  "view_pricing": "Ver Precios", "rights": "© 2026 Spin It Up Laundry. Todos los derechos reservados. | Desarrollado por TradeWorks AI.",
  "privacy": "Política de Privacidad", "terms": "Términos de Servicio", "accessibility": "Accesibilidad",
  "lang_full": ("English", "Español"),
  "svc": [("Autoservicio","/es/servicios/autoservicio/"),("Lavado y Doblado","/es/servicios/lavado-y-doblado/"),
          ("Recogida y Entrega","/es/servicios/recogida-y-entrega/"),("Comercial","/services/commercial/"),
          ("Planchado","/services/ironing-pressing/")],
  "areas_list": [("Avondale","/areas/avondale/"),("Irving Park","/areas/irving-park/"),
                 ("Logan Square","/areas/logan-square/"),("Hermosa","/areas/hermosa/"),("Albany Park","/areas/albany-park/")],
  "nav": [("Servicios","/es/servicios/","services",True),("Precios","/es/precios/","pricing",False),
          ("Áreas de Servicio","/areas/","areas",True),("Nosotros","/about/","about",False),
          ("Preguntas Frecuentes","/es/preguntas-frecuentes/","faq",False),("Contacto","/es/contacto/","contact",False)],
  "footer_services": [("Autoservicio","/es/servicios/autoservicio/"),("Lavado y Doblado","/es/servicios/lavado-y-doblado/"),
          ("Recogida y Entrega","/es/servicios/recogida-y-entrega/"),("Servicios Comerciales","/services/commercial/"),
          ("Planchado","/services/ironing-pressing/"),("Ver Precios","/es/precios/")],
  "footer_company": [("Nosotros","/about/"),("Contacto","/es/contacto/"),("Preguntas Frecuentes","/es/preguntas-frecuentes/"),("Áreas de Servicio","/areas/"),("Recursos","/resources/")],
  "all_services": "Todos los Servicios", "all_areas": "Todas las Áreas",
  "announce": ["🆓 SECADO GRATIS MIÉ Y JUE", "📶 WI-FI GRATIS", "☕ CAFÉ GRATIS",
               "🅿️ ESTACIONAMIENTO GRATIS", "💳 ACEPTAMOS EBT", "📍 3710 N KIMBALL AVE, CHICAGO"],
},
}

def lang_toggle(lang, self_url, alt_url, full=False):
    en_label, es_label = ("English", "Español") if full else ("EN", "ES")
    if lang == "en":
        en = f'<a href="{self_url}" aria-current="true">{en_label}</a>'
        es = f'<a href="{alt_url}">{es_label}</a>'
    else:
        en = f'<a href="{alt_url}">{en_label}</a>'
        es = f'<a href="{self_url}" aria-current="true">{es_label}</a>'
    return f'<span class="lang-toggle">{en} | {es}</span>'

def nav(active, lang):
    c = CHROME[lang]
    items = []
    for label, href, key, has_menu in c["nav"]:
        cur = ' aria-current="page"' if key == active else ''
        if has_menu and key == "services":
            kids = "\n".join(f'              <li><a href="{h}">{l}</a></li>' for l, h in c["svc"])
            items.append(f'''          <li class="nav__item nav__item--has-menu">
            <a class="nav__link" href="{href}"{cur}>{label}</a>
            <ul class="dropdown">
{kids}
            </ul>
          </li>''')
        elif has_menu and key == "areas":
            kids = "\n".join(f'              <li><a href="{h}">{l}</a></li>' for l, h in c["areas_list"])
            items.append(f'''          <li class="nav__item nav__item--has-menu">
            <a class="nav__link" href="{href}"{cur}>{label}</a>
            <ul class="dropdown">
{kids}
            </ul>
          </li>''')
        else:
            items.append(f'          <li class="nav__item"><a class="nav__link" href="{href}"{cur}>{label}</a></li>')
    return '<nav class="nav" aria-label="%s">\n        <ul class="nav__list">\n%s\n        </ul>\n      </nav>' % (c["primary"], "\n".join(items))

def announce(lang):
    items = CHROME[lang]["announce"]
    # each item followed by a separator so the set duplicates seamlessly for the marquee
    one = "".join(f'<span>{x}</span><span class="sep">·</span>' for x in items)
    return ('    <div class="announce-bar" aria-label="Key amenities">\n'
            '      <div class="announce-track">' + one + one + '</div>\n'
            '    </div>')

def topnav_menu(active, lang):
    """The centered menu (our menu list) with hover dropdowns, dark 'v2' style."""
    c = CHROME[lang]
    out = []
    for label, href, key, has_menu in c["nav"]:
        active_cls = " active" if key == active else ""
        if has_menu and key in ("services", "areas"):
            kids_data = c["svc"] if key == "services" else c["areas_list"]
            kids = "\n".join(f'          <a href="{h}">{l}</a>' for l, h in kids_data)
            out.append(f'''        <div class="tn-dd{active_cls}">
          <a href="{href}">{label} <span class="tn-caret">▼</span></a>
          <div class="tn-menu">
{kids}
          </div>
        </div>''')
        else:
            cls = ' class="active"' if key == active else ''
            out.append(f'        <a href="{href}"{cls}>{label}</a>')
    return "\n".join(out)

def header(active, overlay, lang, self_url, alt_url):
    c = CHROME[lang]
    home = '/es/' if lang == 'es' else '/'
    return f'''  <header class="site-topbar" role="banner">
{announce(lang)}
    <nav class="topnav" aria-label="{c['primary']}">
      <a class="tn-logo" href="{home}" aria-label="Spin It Up Laundry"><img src="/images/spin-it-up-logo.png" alt="Spin It Up Laundry"><span class="brand-name">Spin It Up</span></a>
      <div class="tn-center">
{topnav_menu(active, lang)}
      </div>
      <div class="tn-actions">
        <a class="tn-phone" href="tel:{PHONE_TEL}">📞 {PHONE_DISP}</a>
        {lang_toggle(lang, self_url, alt_url)}
        <a class="tn-cta" href="{CENTS}" target="_blank" rel="noopener" data-cents>{c['schedule'].upper()} →</a>
        <button class="nav-toggle" aria-label="{c['open_menu']}" aria-expanded="false" aria-controls="mobile-menu">{HAMBURGER}</button>
      </div>
    </nav>
  </header>'''

def mobile_menu(active, lang, self_url, alt_url):
    c = CHROME[lang]
    svc_open = ' is-open' if active == 'services' else ''
    svc_exp = 'true' if active == 'services' else 'false'
    areas_open = ' is-open' if active == 'areas' else ''
    areas_exp = 'true' if active == 'areas' else 'false'
    svc_kids = "\n".join(f'          <li><a href="{h}">{l}</a></li>' for l, h in c["svc"])
    areas_kids = "\n".join(f'          <li><a href="{h}">{l}</a></li>' for l, h in c["areas_list"])
    svc_label, pricing_label = c["nav"][0][0], c["nav"][1][0]
    areas_label, about_label = c["nav"][2][0], c["nav"][3][0]
    faq_label, contact_label = c["nav"][4][0], c["nav"][5][0]
    home = '/es/' if lang == 'es' else '/'
    return f'''  <div class="mobile-menu" id="mobile-menu" role="dialog" aria-modal="true" aria-label="{c['menu']}">
    <div class="mobile-menu__head">
      <a class="logo" href="{home}" aria-label="Spin It Up Laundry"><img src="/images/spin-it-up-logo.png" alt="Spin It Up Laundry" style="height:48px;width:auto"><span class="brand-name">Spin It Up</span></a>
      <button class="mobile-menu__close" aria-label="{c['close_menu']}">{CLOSE}</button>
    </div>
    <ul class="mobile-menu__list">
      <li>
        <button class="mobile-menu__sub-toggle" aria-expanded="{svc_exp}">{svc_label} <span aria-hidden="true">+</span></button>
        <ul class="mobile-menu__sub{svc_open}">
          <li><a href="{c['nav'][0][1]}">{c['all_services']}</a></li>
{svc_kids}
        </ul>
      </li>
      <li><a href="{c['nav'][1][1]}">{pricing_label}</a></li>
      <li>
        <button class="mobile-menu__sub-toggle" aria-expanded="{areas_exp}">{areas_label} <span aria-hidden="true">+</span></button>
        <ul class="mobile-menu__sub{areas_open}">
          <li><a href="/areas/">{c['all_areas']}</a></li>
{areas_kids}
        </ul>
      </li>
      <li><a href="{c['nav'][3][1]}">{about_label}</a></li>
      <li><a href="{c['nav'][4][1]}">{faq_label}</a></li>
      <li><a href="{c['nav'][5][1]}">{contact_label}</a></li>
    </ul>
    <div class="mobile-menu__footer">
      <a class="btn btn--primary btn--block" href="{CENTS}" target="_blank" rel="noopener" data-cents>{c['schedule']}</a>
      <a class="btn btn--outline btn--block" href="tel:{PHONE_TEL}">{c['call']}</a>
      {lang_toggle(lang, self_url, alt_url, full=True)}
    </div>
  </div>'''

def footer(lang, self_url, alt_url):
    c = CHROME[lang]
    home = '/es/' if lang == 'es' else '/'
    services = "\n".join(f'            <li><a href="{h}">{l}</a></li>' for l, h in c["footer_services"])
    company = "\n".join(f'            <li><a href="{h}">{l}</a></li>' for l, h in c["footer_company"])
    return f'''  <footer class="site-footer" data-section="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <a class="logo" href="{home}" aria-label="Spin It Up Laundry"><img src="/images/spin-it-up-logo.png" alt="Spin It Up Laundry" style="height:48px;width:auto"><span class="brand-name">Spin It Up</span></a>
          <p class="footer__tagline">{c['tagline']}</p>
          <p class="footer__meta">
            <a href="{MAPS_DIR}">3710 N Kimball Ave, Chicago, IL 60618</a><br>
            <a href="tel:{PHONE_TEL}">{PHONE_DISP}</a><br>
            {c['hours']}
          </p>
          <a class="btn btn--primary btn--sm" href="{CENTS}" target="_blank" rel="noopener" data-cents>{c['schedule']}</a>
        </div>
        <div>
          <h4>{c['f_services']}</h4>
          <ul>
{services}
          </ul>
        </div>
        <div>
          <h4>{c['f_company']}</h4>
          <ul>
{company}
          </ul>
        </div>
        <div>
          <h4>{c['f_connect']}</h4>
          <div class="footer__social">
            <a href="https://www.facebook.com/SpinItUpLaundry/" aria-label="Facebook">{FB}</a>
            <a href="https://www.instagram.com/spinituplaundry/" aria-label="Instagram">{IG}</a>
            <a href="https://www.yelp.com/biz/spin-it-up-laundry-chicago" aria-label="Yelp">{YELP}</a>
          </div>
          <ul>
            <li><a href="{REVIEW}" target="_blank" rel="noopener">{c['leave_review']}</a></li>
            <li>{lang_toggle(lang, self_url, alt_url, full=True)}</li>
          </ul>
        </div>
      </div>
      <div class="footer__bottom">
        <span>{c['rights']}</span>
        <nav aria-label="{c['legal']}">
          <a href="/privacy-policy/">{c['privacy']}</a>
          <a href="/terms-of-service/">{c['terms']}</a>
          <a href="/accessibility/">{c['accessibility']}</a>
        </nav>
      </div>
    </div>
  </footer>'''

def sticky(lang):
    c = CHROME[lang]
    return f'''  <div class="sticky-cta" data-section="sticky-bar">
    <a class="btn btn--primary" href="tel:{PHONE_TEL}">{PHONE_SVG} {c['call_now']}</a>
    <a class="btn btn--secondary" href="{CENTS}" target="_blank" rel="noopener" data-cents>{CAL_SVG} {c['schedule']}</a>
  </div>'''

def page_html(meta, body):
    lang = meta.get("lang", "en")
    overlay = meta.get("overlay", False)
    classes = []
    if overlay: classes.append("has-overlay-header")
    if meta.get("body_class"): classes.append(meta["body_class"])
    body_cls = f' class="{" ".join(classes)}"' if classes else ''
    self_url = meta["canonical"].replace("https://spinituplaundry.net", "")
    # alt_url: the other-language counterpart (English pages may use legacy "es")
    alt_url = meta.get("alt") or (meta.get("es") if lang == "en" else meta.get("en")) or ("/es/" if lang == "en" else "/")

    if meta.get("hreflang", True):
        en_href = ("https://spinituplaundry.net" + alt_url) if lang == "es" else meta["canonical"]
        es_href = meta["canonical"] if lang == "es" else ("https://spinituplaundry.net" + alt_url)
        hreflang = (f'  <link rel="alternate" hreflang="en" href="{en_href}">\n'
                    f'  <link rel="alternate" hreflang="es" href="{es_href}">\n'
                    f'  <link rel="alternate" hreflang="x-default" href="{en_href}">\n')
    else:
        hreflang = ""

    extra_head = meta.get("head", "")
    preload = meta.get("preload", "")
    og_img = meta.get("og_image", "https://spinituplaundry.net/images/og-homepage.jpg")
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{meta["title"]}</title>
  <meta name="description" content="{meta["description"]}">
  <meta name="robots" content="{meta.get("robots", "index, follow")}">
  <link rel="canonical" href="{meta["canonical"]}">
{hreflang}
  <meta property="og:title" content="{meta.get("og_title", meta["title"])}">
  <meta property="og:description" content="{meta.get("og_description", meta["description"])}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{meta["canonical"]}">
  <meta property="og:image" content="{og_img}">
  <meta property="og:locale" content="{'es_US' if lang=='es' else 'en_US'}">
  <meta property="og:site_name" content="Spin It Up Laundry">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{meta.get("og_title", meta["title"])}">
  <meta name="twitter:description" content="{meta.get("og_description", meta["description"])}">
  <meta name="twitter:image" content="{og_img}">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{preload}  <link rel="stylesheet" href="/css/main.css?v=24">
  <link rel="icon" type="image/png" sizes="512x512" href="/images/spin-it-up-logo.png">
{extra_head}</head>
<body{body_cls}>
  <a class="skip-link" href="#main">{CHROME[lang]["skip"]}</a>

{header(meta["active"], overlay, lang, self_url, alt_url)}

{mobile_menu(meta["active"], lang, self_url, alt_url)}

  <main id="main">
{body}
  </main>

{footer(lang, self_url, alt_url)}

{sticky(lang)}

  <script src="/js/main.js" defer></script>
</body>
</html>
'''

# Per-page hero background image (sits behind .page-hero__overlay). The SVGs
# live in site/images/. Pages not listed keep the plain gradient hero.
HERO_IMG = {
    "self-service": "hero-self-service.svg", "wash-and-fold": "hero-wash-and-fold.svg",
    "pickup-delivery": "hero-pickup-delivery.svg", "commercial": "hero-commercial.svg",
    "ironing-pressing": "hero-ironing-pressing.svg", "services": "hero-services.svg",
    "about": "hero-about.svg", "areas": "hero-areas.svg", "pricing": "hero-pricing.svg",
    "contact": "hero-contact.svg", "faq": "hero-faq.svg",
    "avondale": "hero-avondale.svg", "irving-park": "hero-irving-park.svg",
    "logan-square": "hero-logan-square.svg", "hermosa": "hero-hermosa.svg",
    "albany-park": "hero-albany-park.svg",
    # Spanish pages reuse the matching English hero artwork
    "es-autoservicio": "hero-self-service.svg", "es-lavado-y-doblado": "hero-wash-and-fold.svg",
    "es-recogida-y-entrega": "hero-pickup-delivery.svg", "es-servicios": "hero-services.svg",
    "es-precios": "hero-pricing.svg", "es-contacto": "hero-contact.svg",
    "es-preguntas-frecuentes": "hero-faq.svg",
}

def inject_hero_bg(key, body):
    """Insert a background image + dark overlay into the page hero, if mapped."""
    img = HERO_IMG.get(key)
    if not img or "page-hero__bg" in body:
        return body
    bg = (f'\n      <img class="page-hero__bg" src="/images/{img}" alt="" aria-hidden="true">'
          f'\n      <div class="page-hero__overlay"></div>')
    return re.sub(r'(<section class="page-hero"[^>]*>)', lambda m: m.group(1) + bg, body, count=1)

PAGES = json.load(open(os.path.join(ROOT, "build", "pages.json"), encoding="utf-8"))

# index.html and es/index.html are maintained by hand as the standalone rich
# homepage design (EN + ES), so the generator no longer overwrites them.
SKIP = {"home", "es-home"}

# Convert internal absolute paths (/css, /images, /services ...) to relative,
# per page depth, so the site works under any prefix (e.g. a GCS bucket folder)
# AND at a domain root. Leaves external URLs (https:, tel:, mailto:, #, //) and
# absolute canonical/OG/JSON-LD URLs untouched. Idempotent.
_ATTR_RE = re.compile(r'(\b(?:href|src|srcset|poster|action)=")/(?!/)')
_URL_RE = re.compile(r"""url\((['"]?)/(?!/)""")

def relativize_site():
    n = 0
    for dirpath, _dirs, files in os.walk(SITE):
        for f in files:
            if not f.endswith(".html"):
                continue
            path = os.path.join(dirpath, f)
            rel = os.path.relpath(path, SITE).replace(os.sep, "/")
            depth = rel.count("/")
            prefix = "./" if depth == 0 else "../" * depth
            s = open(path, encoding="utf-8").read()
            new = _ATTR_RE.sub(lambda m: m.group(1) + prefix, s)
            new = _URL_RE.sub(lambda m: "url(" + m.group(1) + prefix, new)
            if new != s:
                open(path, "w", encoding="utf-8").write(new)
                n += 1
    print(f"Relativized paths in {n} files.")

# Append index.html to every internal directory link (ending in "/") so the
# site works on a raw object server (GCS bucket) with no directory routing.
# Skips external schemes, anchors, queries, and SEO links (canonical/hreflang
# use https:// and are left absolute). Idempotent (links ending in a file are
# left as-is).
_HREF_RE = re.compile(r'href="([^"]*)"')
_SKIP_HREF = re.compile(r'^(https?:|tel:|mailto:|#|//|data:|javascript:|\?)', re.I)

def _indexify_href(m):
    v = m.group(1)
    if _SKIP_HREF.match(v):
        return m.group(0)
    part = re.match(r'^([^#?]*)([#?].*)?$', v)
    path, suffix = part.group(1), part.group(2) or ""
    if path.endswith("/"):
        return 'href="%sindex.html%s"' % (path, suffix)
    return m.group(0)

def indexify_site():
    n = 0
    for dirpath, _dirs, files in os.walk(SITE):
        for f in files:
            if not f.endswith(".html"):
                continue
            path = os.path.join(dirpath, f)
            s = open(path, encoding="utf-8").read()
            new = _HREF_RE.sub(_indexify_href, s)
            if new != s:
                open(path, "w", encoding="utf-8").write(new)
                n += 1
    print(f"Appended index.html to directory links in {n} files.")

def main():
    built = 0
    for key, meta in PAGES.items():
        if key in SKIP:
            print("  skip", meta["out"], "(maintained manually)")
            continue
        with open(os.path.join(CONTENT, key + ".html"), encoding="utf-8") as f:
            body = f.read().rstrip("\n")
        body = inject_hero_bg(key, body)
        head_path = os.path.join(CONTENT, "_" + key + "_head.html")
        if os.path.exists(head_path):
            with open(head_path, encoding="utf-8") as f:
                meta = dict(meta, head=f.read().rstrip("\n") + "\n")
        out_path = os.path.join(SITE, meta["out"])
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html(meta, body))
        built += 1
        print("  wrote", meta["out"])
    print(f"Done. {built} pages generated.")
    relativize_site()
    indexify_site()

if __name__ == "__main__":
    main()
