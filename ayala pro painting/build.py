#!/usr/bin/env python3
"""
Ayala Pro Painting — static page generator.

Reads the canonical reusable partials (site/partials/header.html and
footer.html) and stitches them, INLINED, into each generated page. The
output files physically contain the header/footer markup — no JS loading.
Header/footer remain a single source of truth in site/partials/.

Section helpers below mirror the dev-guide service-page template so each
page is defined declaratively and the FAQ accordion + FAQPage schema are
generated from one shared list (they can never drift apart).
"""
import json, os, io, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
HEADER = open(os.path.join(SITE, "partials", "header.html"), encoding="utf-8").read().strip()
FOOTER = open(os.path.join(SITE, "partials", "footer.html"), encoding="utf-8").read().strip()
PHONE = "(813) 555-0199"
BASE = "https://ayalapropainting.com"

# ---------------------------------------------------------------- schema
def breadcrumb(items):
    el = [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
          for i, (n, u) in enumerate(items)]
    return json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList",
                       "itemListElement": el}, ensure_ascii=False, indent=2)

def faqpage(qas):
    main = [{"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                       "mainEntity": main}, ensure_ascii=False, indent=2)

def service_schema(name, desc, url, stype):
    return json.dumps({
        "@context": "https://schema.org", "@type": "Service", "name": name,
        "description": desc, "url": url,
        "provider": {"@type": "HousePainter", "name": "Ayala Pro Painting",
                     "telephone": "+1-813-555-0199"},
        "areaServed": {"@type": "City", "name": "Riverview"},
        "serviceType": stype}, ensure_ascii=False, indent=2)

def collection_schema(name, desc, url):
    return json.dumps({"@context": "https://schema.org", "@type": "CollectionPage",
                       "name": name, "description": desc, "url": url},
                      ensure_ascii=False, indent=2)

# ---------------------------------------------------------------- sections
CHECK = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M20 6 9 17l-5-5"/></svg>')

def page_hero(eyebrow, h1, lead, crumbs, phone_first=False, estimate_label="Get Your Free Estimate"):
    items = "".join(
        f'<li><a href="{u}">{n}</a></li>' if u else f'<li aria-current="page">{n}</li>'
        for n, u in crumbs)
    estimate = f'<a href="/contact/" class="btn btn--primary btn--lg" data-cta="page_hero">{estimate_label}</a>'
    call = f'<a href="tel:8135550199" class="btn btn--outline-white btn--lg" data-phone>Call {PHONE}</a>'
    if phone_first:
        estimate, call = (f'<a href="tel:8135550199" class="btn btn--primary btn--lg" data-phone>Call {PHONE}</a>',
                          '<a href="/contact/" class="btn btn--outline-white btn--lg" data-cta="page_hero">Request an Estimate</a>')
    return f'''    <section class="page-hero" data-section="page_hero">
      <div class="page-hero__overlay"></div>
      <div class="container">
        <div class="page-hero__inner">
          <nav class="breadcrumb" aria-label="Breadcrumb"><ol>{items}</ol></nav>
          <p class="page-hero__eyebrow">{eyebrow}</p>
          <h1 class="page-hero__title">{h1}</h1>
          <p class="page-hero__lead">{lead}</p>
          <div class="page-hero__ctas">{estimate}{call}</div>
        </div>
      </div>
    </section>'''

def signs_section(eyebrow, h2, intro, items, img_alt, bg="white"):
    lis = "".join(f'<li>{CHECK} {it}</li>' for it in items)
    return f'''    <section class="section section--{bg}" aria-labelledby="signs-heading">
      <div class="container">
        <div class="split">
          <div class="split__content">
            <p class="section-eyebrow">{eyebrow}</p>
            <h2 id="signs-heading" class="section-title">{h2}</h2>
            <p>{intro}</p>
            <ul class="signs-list">{lis}</ul>
          </div>
          <div class="split__media">
            <img src="/images/placeholder.svg" alt="{img_alt}" width="800" height="600" loading="lazy">
          </div>
        </div>
      </div>
    </section>'''

def process_section(h2, steps, bg="cream"):
    rows = "".join(
        f'<div class="process__step"><div class="process__num">{i+1}</div>'
        f'<div><h3 class="process__title">{t}</h3><p class="process__desc">{d}</p></div></div>'
        for i, (t, d) in enumerate(steps))
    return f'''    <section class="section section--{bg}" aria-labelledby="process-heading">
      <div class="container">
        <p class="section-eyebrow">How We Work</p>
        <h2 id="process-heading" class="section-title">{h2}</h2>
        <div class="process">{rows}</div>
      </div>
    </section>'''

def table_section(eyebrow, h2, subtitle, headers, rows, bg="white", anchor="table", center_table=False):
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    sub = f'<p class="section-subtitle">{subtitle}</p>' if subtitle else ""
    style = ' style="max-width:820px;margin:24px auto;"' if center_table else ""
    return f'''    <section class="section section--{bg}" aria-labelledby="{anchor}-heading">
      <div class="container">
        <p class="section-eyebrow">{eyebrow}</p>
        <h2 id="{anchor}-heading" class="section-title">{h2}</h2>
        {sub}
        <table class="data-table"{style}><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>
      </div>
    </section>'''

def pricing_section(h2, subtitle, rows, disclaimer, cta_text="Get Your Personalized Quote", bg="cream"):
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'''    <section class="section section--{bg}" aria-labelledby="pricing-heading">
      <div class="container">
        <div class="pricing">
          <h2 id="pricing-heading" class="section-title">{h2}</h2>
          <p class="section-subtitle">{subtitle}</p>
        </div>
        <table class="data-table" style="max-width:820px;margin:24px auto;">
          <thead><tr><th scope="col">Service Variant</th><th scope="col">Typical Range</th><th scope="col">Factors</th></tr></thead>
          <tbody>{body}</tbody>
        </table>
        <p class="pricing__disclaimer" style="text-align:center;">{disclaimer}</p>
        <div class="pricing__ctas"><a href="/contact/" class="btn btn--primary" data-cta="pricing">{cta_text}</a></div>
      </div>
    </section>'''

def feature_section(eyebrow, h2, cards, bg="white"):
    c = "".join(f'<div class="feature-card"><h3>{t}</h3><p>{d}</p></div>' for t, d in cards)
    return f'''    <section class="section section--{bg}" aria-labelledby="why-heading">
      <div class="container">
        <p class="section-eyebrow">{eyebrow}</p>
        <h2 id="why-heading" class="section-title">{h2}</h2>
        <div class="feature-grid">{c}</div>
      </div>
    </section>'''

def gallery_section(h2, items, bg="cream"):
    figs = "".join(
        f'<figure class="project-card"><div class="project-card__img">'
        f'<img src="/images/placeholder.svg" alt="{alt}" width="800" height="600" loading="lazy"></div>'
        f'<figcaption class="project-card__caption"><p class="project-card__title">{t}</p>'
        f'<p class="project-card__detail">{loc}</p></figcaption></figure>'
        for t, loc, alt in items)
    return f'''    <section class="section section--{bg}" aria-labelledby="gallery-heading" data-section="gallery">
      <div class="container">
        <p class="section-eyebrow">Our Recent Work</p>
        <h2 id="gallery-heading" class="section-title">{h2}</h2>
        <div class="gallery__grid">{figs}</div>
        <div class="gallery__cta"><a href="/gallery/" class="btn btn--secondary" data-cta="gallery_all">View Full Gallery</a></div>
      </div>
    </section>'''

def faq_section(h2, qas, bg="white"):
    items = ""
    for q, a in qas:
        items += (f'<div class="faq__item"><button class="faq__question" aria-expanded="false">{q}'
                  f'<span class="faq__icon" aria-hidden="true">+</span></button>'
                  f'<div class="faq__answer"><div class="faq__answer-inner">{a}</div></div></div>')
    return f'''    <section class="section section--{bg}" aria-labelledby="faq-heading" data-section="faq">
      <div class="container">
        <p class="section-eyebrow">Frequently Asked Questions</p>
        <h2 id="faq-heading" class="section-title">{h2}</h2>
        <div class="faq">{items}</div>
      </div>
    </section>'''

def related_section(h2, cards, bg="cream"):
    c = "".join(
        f'<a href="{href}" class="service-card" data-cta="related"><h3 class="service-card__title">{t}</h3>'
        f'<p class="service-card__desc">{d}</p><span class="service-card__link">Learn More &rarr;</span></a>'
        for href, t, d in cards)
    return f'''    <section class="section section--{bg}" aria-labelledby="related-heading">
      <div class="container">
        <p class="section-eyebrow">Related Services</p>
        <h2 id="related-heading" class="section-title">{h2}</h2>
        <div class="services__grid">{c}</div>
      </div>
    </section>'''

AREAS = [("Riverview", "/areas/riverview/"), ("Brandon", "/areas/brandon/"),
         ("Valrico", "/areas/valrico/"), ("Lithia", "/areas/lithia/"),
         ("Fish Hawk", "/areas/fish-hawk/"), ("Apollo Beach", "/areas/apollo-beach/")]

def area_callout(h2, bg="white"):
    links = "".join(f'<a href="{u}">{n}</a>' for n, u in AREAS) + '<a href="/areas/">All Areas &rarr;</a>'
    return f'''    <section class="section section--{bg} area-callout" aria-labelledby="area-heading">
      <div class="container">
        <h2 id="area-heading" class="section-title">{h2}</h2>
        <div class="area-callout__list">{links}</div>
      </div>
    </section>'''

def cta_banner(title, text, phone_first=False):
    estimate = '<a href="/contact/" class="btn btn--primary btn--lg" data-cta="bottom_cta_banner">Get Your Free Estimate</a>'
    call = f'<a href="tel:8135550199" class="btn btn--outline-white btn--lg" data-phone>Call {PHONE}</a>'
    if phone_first:
        estimate, call = (f'<a href="tel:8135550199" class="btn btn--primary btn--lg" data-phone>Call {PHONE}</a>',
                          '<a href="/contact/" class="btn btn--outline-white btn--lg" data-cta="bottom_cta_banner">Request an Estimate</a>')
    return f'''    <section class="cta-banner" data-section="bottom_cta_banner">
      <div class="container">
        <div class="cta-banner__inner">
          <h2 class="cta-banner__title">{title}</h2>
          <p class="cta-banner__text">{text}</p>
          <div class="cta-banner__ctas">{estimate}{call}</div>
        </div>
      </div>
    </section>'''

# ---------------------------------------------------------------- area helpers
def area_localbusiness(city):
    return json.dumps({
        "@context": "https://schema.org", "@type": "HousePainter", "name": "Ayala Pro Painting",
        "url": BASE, "telephone": "+1-813-555-0199",
        "areaServed": {"@type": "City", "name": city,
                       "containedInPlace": {"@type": "AdministrativeArea", "name": "Hillsborough County, FL"}},
        "address": {"@type": "PostalAddress", "addressLocality": "Riverview", "addressRegion": "FL",
                    "postalCode": "33578", "addressCountry": "US"}}, ensure_ascii=False, indent=2)

def prose_section(eyebrow, h2, paragraphs, bg="white", anchor="prose"):
    eb = f'<p class="section-eyebrow">{eyebrow}</p>' if eyebrow else ""
    ps = "".join(f"<p>{p}</p>" for p in paragraphs)
    return f'''    <section class="section section--{bg}" aria-labelledby="{anchor}-heading">
      <div class="container">
        {eb}
        <h2 id="{anchor}-heading" class="section-title">{h2}</h2>
        <div class="prose">{ps}</div>
      </div>
    </section>'''

def local_context_section(h2, profile_rows, prose_paragraphs, bg="cream"):
    prof = "".join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in profile_rows)
    ps = "".join(f"<p>{p}</p>" for p in prose_paragraphs)
    return f'''    <section class="section section--{bg}" aria-labelledby="about-heading">
      <div class="container">
        <p class="section-eyebrow">Local Knowledge</p>
        <h2 id="about-heading" class="section-title">{h2}</h2>
        <div class="local-context">
          <table class="data-table"><thead><tr><th scope="col">Community Profile</th><th scope="col"></th></tr></thead><tbody>{prof}</tbody></table>
          <div class="prose">{ps}</div>
        </div>
      </div>
    </section>'''

AREA_SERVICES = [
    ("/services/interior-painting/", "Interior Painting", "Walls, ceilings, trim, and accent walls with low-VOC, humidity-resistant finishes."),
    ("/services/exterior-painting/", "Exterior Painting", "UV- and weather-rated coatings with our 7-step Florida prep process."),
    ("/services/cabinet-painting/", "Cabinet Painting", "Factory-smooth kitchen and bath cabinet refinishing in any color."),
    ("/services/commercial-painting/", "Commercial Painting", "Offices, retail, HOAs, and multi-family with minimal disruption."),
    ("/services/pressure-washing/", "Pressure Washing", "Driveways, decks, fences, and exteriors cleaned the right way."),
    ("/services/deck-patio-staining/", "Deck &amp; Patio Staining", "Premium stains and sealers built for Florida UV and moisture."),
]

def area_services_section(city, bg="white"):
    cards = "".join(
        f'<a href="{href}" class="service-card" data-cta="area_service"><h3 class="service-card__title">{t}</h3>'
        f'<p class="service-card__desc">{d}</p><span class="service-card__link">Learn More &rarr;</span></a>'
        for href, t, d in AREA_SERVICES)
    return f'''    <section class="section section--{bg}" aria-labelledby="services-heading">
      <div class="container">
        <p class="section-eyebrow">Services</p>
        <h2 id="services-heading" class="section-title">Painting Services We Provide in {city}</h2>
        <div class="services__grid">{cards}</div>
      </div>
    </section>'''

def map_section(h2, subtitle, bg="white"):
    return f'''    <section class="section section--{bg}" aria-labelledby="map-heading">
      <div class="container">
        <p class="section-eyebrow">Where We Work</p>
        <h2 id="map-heading" class="section-title">{h2}</h2>
        <p class="section-subtitle">{subtitle}</p>
        <iframe title="Map of Ayala Pro Painting service areas in south Hillsborough County"
          src="https://www.google.com/maps?q=Riverview,FL&z=11&output=embed"
          width="100%" height="460" style="border:0;border-radius:8px;" loading="lazy" allowfullscreen></iframe>
      </div>
    </section>'''

def area_cards_section(h2, subtitle, cards, bg="cream"):
    c = "".join(
        f'<a href="{url}" class="service-card" data-cta="area_card"><h3 class="service-card__title">{name}</h3>'
        f'<p class="service-card__desc">{desc}</p><span class="service-card__link">Learn More &rarr;</span></a>'
        for name, url, desc in cards)
    return f'''    <section class="section section--{bg}" aria-labelledby="areas-heading">
      <div class="container">
        <p class="section-eyebrow">Select Your Community</p>
        <h2 id="areas-heading" class="section-title">{h2}</h2>
        <p class="section-subtitle">{subtitle}</p>
        <div class="services__grid services__grid--4">{c}</div>
      </div>
    </section>'''

# ---------------------------------------------------------------- resources / articles
def light_header(eyebrow, h1, subtitle, crumbs):
    items = "".join(
        f'<li><a href="{u}">{n}</a></li>' if u else f'<li aria-current="page">{n}</li>'
        for n, u in crumbs)
    return f'''    <section class="light-header">
      <div class="container">
        <nav class="breadcrumb breadcrumb--dark" aria-label="Breadcrumb"><ol>{items}</ol></nav>
        <p class="section-eyebrow" style="text-align:left;margin-left:0;">{eyebrow}</p>
        <h1 class="light-header__title">{h1}</h1>
        <p class="light-header__subtitle">{subtitle}</p>
      </div>
    </section>'''

RESOURCE_FILTERS = [("all", "All"), ("costs", "Costs &amp; Pricing"), ("how-to", "How-To Guides"),
                    ("florida", "Florida Tips"), ("color", "Color &amp; Design"), ("product", "Product Guides")]

def resource_hub_body(cards):
    pills = "".join(
        f'<button class="filter-pill{" is-active" if key=="all" else ""}" data-filter="{key}" type="button">{label}</button>'
        for key, label in RESOURCE_FILTERS)
    items = ""
    for c in cards:
        items += f'''<article class="resource-card" data-category="{c['cat']}">
          <a href="/resources/{c['slug']}/" class="resource-card__link">
            <img src="/images/placeholder.svg" alt="{c['alt']}" width="400" height="225" loading="lazy" class="resource-card__img">
            <div class="resource-card__content">
              <span class="resource-card__category">{c['cat_label']}</span>
              <h2 class="resource-card__title">{c['title']}</h2>
              <p class="resource-card__excerpt">{c['excerpt']}</p>
              <div class="resource-card__meta"><span>By Eliseo Ayala</span> &bull; <time datetime="{c['date_iso']}">{c['date']}</time> &bull; <span>{c['read']} min read</span></div>
              <span class="resource-card__read-more">Read More &rarr;</span>
            </div>
          </a>
        </article>'''
    return f'''    <section class="section section--white" aria-label="Resource articles">
      <div class="container">
        <div class="filter-bar" role="tablist" aria-label="Filter articles by category">{pills}</div>
        <div class="resource-grid">{items}</div>
      </div>
    </section>'''

def article_schema(headline, desc, url, date_iso, image):
    return json.dumps({
        "@context": "https://schema.org", "@type": "Article", "headline": headline,
        "description": desc, "url": url,
        "author": {"@type": "Person", "name": "Eliseo Ayala"},
        "publisher": {"@type": "Organization", "name": "Ayala Pro Painting", "url": BASE},
        "datePublished": date_iso, "dateModified": date_iso,
        "image": image}, ensure_ascii=False, indent=2)

# Article body building blocks ------------------------------------
def a_h2(t): return f'<h2 class="article__h2">{t}</h2>'
def a_h3(t): return f'<h3 class="article__h3">{t}</h3>'
def a_p(t): return f'<p>{t}</p>'
def a_ul(items): return '<ul class="article__list">' + "".join(f'<li>{i}</li>' for i in items) + '</ul>'
def a_callout(t): return f'<aside class="article__callout">{t}</aside>'
def a_table(headers, rows):
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="data-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'
def inline_cta(text, href, label="Get Your Free Estimate"):
    return f'''<div class="inline-cta">
      <p class="inline-cta__text">{text}</p>
      <a href="{href}" class="btn btn--primary" data-cta="inline_cta">{label}</a>
    </div>'''

def related_block(article_cards, service_cards):
    arts = "".join(
        f'<a href="/resources/{slug}/" class="service-card" data-cta="related_article">'
        f'<span class="resource-card__category">{cat}</span>'
        f'<h3 class="service-card__title">{title}</h3>'
        f'<span class="service-card__link">Read More &rarr;</span></a>'
        for slug, cat, title in article_cards)
    svcs = "".join(
        f'<a href="{href}" class="service-card" data-cta="related_service">'
        f'<h3 class="service-card__title">{title}</h3>'
        f'<p class="service-card__desc">{desc}</p>'
        f'<span class="service-card__link">Learn More &rarr;</span></a>'
        for href, title, desc in service_cards)
    return f'''    <section class="section section--cream" aria-labelledby="related-heading">
      <div class="container">
        <p class="section-eyebrow">Keep Reading</p>
        <h2 id="related-heading" class="section-title">Related Articles</h2>
        <div class="services__grid">{arts}</div>
        <p class="section-eyebrow" style="margin-top:48px;">Related Services</p>
        <h2 class="section-title">How We Can Help</h2>
        <div class="services__grid">{svcs}</div>
      </div>
    </section>'''

def article_page(slug, title, description, headline, category_label, date_iso, date_disp,
                 read_time, hero_alt, aeo, body_blocks, faq, related_articles, related_services):
    url = f"{BASE}/resources/{slug}/"
    crumbs = [("Home", "/"), ("Resources", "/resources/"), (headline, None)]
    crumbs_schema = [("Home", "/"), ("Resources", f"{BASE}/resources/"), (headline, url)]
    img = f"{BASE}/images/{slug}-hero.jpg"
    body = "\n".join(body_blocks)
    faq_html = faq_section("Frequently Asked Questions", faq, bg="white") if faq else ""
    crumb_items = "".join(
        f'<li><a href="{u}">{n}</a></li>' if u else f'<li aria-current="page">{n}</li>'
        for n, u in crumbs)
    article_main = f'''    <section class="article-wrap">
      <div class="container">
        <article class="article">
          <nav class="breadcrumb breadcrumb--dark" aria-label="Breadcrumb"><ol>{crumb_items}</ol></nav>
          <span class="resource-card__category">{category_label}</span>
          <h1 class="article__title">{headline}</h1>
          <div class="article__meta">By <strong>Eliseo Ayala</strong> &bull; Ayala Pro Painting &bull; <time datetime="{date_iso}">{date_disp}</time> &bull; {read_time} min read</div>
          <img class="article__hero" src="/images/placeholder.svg" alt="{hero_alt}" width="1200" height="675" fetchpriority="high">
          <p class="article__lead">{aeo}</p>
          {body}
        </article>
      </div>
    </section>'''
    end_cta = cta_banner("Need Professional Help? Get Your Free Estimate",
                         "Get a free, no-obligation estimate from Riverview's trusted, locally owned painting professionals.")
    return dict(slug=f"resources/{slug}", title=title, description=description, canonical=url,
                schemas=[article_schema(headline, description, url, date_iso, img),
                         breadcrumb(crumbs_schema), faqpage(faq)],
                body="\n\n".join([article_main, faq_html, related_block(related_articles, related_services), end_cta]))

# ---------------------------------------------------------------- standalone helpers
def page_schema(typ, name, desc, url):
    return json.dumps({"@context": "https://schema.org", "@type": typ, "name": name,
                       "description": desc, "url": url}, ensure_ascii=False, indent=2)

def founder_story(h2, paragraphs, signature, img_alt, bg="white"):
    ps = "".join(f"<p>{p}</p>" for p in paragraphs)
    return f'''    <section class="section section--{bg}" aria-labelledby="story-heading">
      <div class="container">
        <div class="split split--reverse">
          <div class="split__media">
            <img src="/images/placeholder.svg" alt="{img_alt}" width="600" height="800" loading="lazy">
          </div>
          <div class="split__content">
            <p class="section-eyebrow" style="text-align:left;margin-left:0;">Our Story</p>
            <h2 id="story-heading" class="section-title" style="text-align:left;margin-left:0;">{h2}</h2>
            <div class="prose" style="margin:0;">{ps}</div>
            <p class="about-preview__signature">{signature}</p>
          </div>
        </div>
      </div>
    </section>'''

def credentials_section(h2, items, bg="white"):
    lis = "".join(
        f'<li class="credential"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        f'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg><span>{t}</span></li>'
        for t in items)
    return f'''    <section class="section section--cream" aria-labelledby="cred-heading">
      <div class="container">
        <p class="section-eyebrow">Credentials</p>
        <h2 id="cred-heading" class="section-title">{h2}</h2>
        <ul class="credentials">{lis}</ul>
      </div>
    </section>'''

GALLERY_FILTERS = [("all", "All"), ("interior", "Interior"), ("exterior", "Exterior"),
                   ("cabinet", "Cabinets"), ("commercial", "Commercial"), ("pressure-washing", "Pressure Washing")]

def gallery_filtered_section(cards, bg="white"):
    pills = "".join(
        f'<button class="filter-pill{" is-active" if key=="all" else ""}" data-filter="{key}" type="button">{label}</button>'
        for key, label in GALLERY_FILTERS)
    items = ""
    for c in cards:
        items += f'''<button class="gallery-item" type="button" data-category="{c['cat']}" data-caption="{c['title']}" data-detail="{c['detail']}" data-full="/images/placeholder.svg" aria-label="View {c['title']}">
          <span class="project-card__img"><img src="/images/placeholder.svg" alt="{c['alt']}" width="800" height="600" loading="lazy"></span>
          <span class="project-card__caption"><span class="project-card__title">{c['title']}</span><span class="project-card__detail">{c['detail']}</span></span>
        </button>'''
    return f'''    <section class="section section--{bg}" aria-label="Project gallery">
      <div class="container">
        <div class="filter-bar gallery-filter" role="tablist" aria-label="Filter projects by type">{pills}</div>
        <div class="gallery__grid gallery-grid">{items}</div>
        <p class="gallery-note">We add new projects regularly. Follow us on <a href="https://www.instagram.com/ayalapropainting" target="_blank" rel="noopener noreferrer" data-outbound>Instagram</a> for our latest work.</p>
      </div>
    </section>'''

def rating_summary_first(bg="cream"):
    return f'''    <section class="section section--{bg}" aria-label="Overall rating">
      <div class="container">
        <div class="rating-summary">
          <div class="rating-summary__stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="rating-summary__headline">Be Our First Reviewer</p>
          <p class="rating-summary__sub">We&rsquo;re a new, locally owned company building our reputation one project at a time. If we&rsquo;ve painted for you, we&rsquo;d be grateful for your honest feedback on Google.</p>
          <a href="https://www.google.com/maps" target="_blank" rel="noopener noreferrer" class="btn btn--primary" data-outbound>Leave Us a Review &rarr;</a>
        </div>
      </div>
    </section>'''

def reviews_grid(h2, reviews, bg="white"):
    cards = ""
    for r in reviews:
        cards += f'''<blockquote class="review-card">
          <div class="review-card__stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="review-card__quote">{r['quote']}</p>
          <p class="review-card__name">{r['name']}</p>
          <p class="review-card__type">{r['project']}</p>
          <span class="review-card__source">{r['source']}</span>
        </blockquote>'''
    return f'''    <section class="section section--{bg}" aria-labelledby="reviews-heading">
      <div class="container">
        <p class="section-eyebrow">In Their Words</p>
        <h2 id="reviews-heading" class="section-title">{h2}</h2>
        <div class="reviews-grid">{cards}</div>
      </div>
    </section>'''

def review_sources(bg="cream"):
    plats = [("Google", "https://www.google.com/maps"), ("Yelp", "https://www.yelp.com"),
             ("Facebook", "https://www.facebook.com/ayalapropainting")]
    links = "".join(
        f'<a href="{u}" target="_blank" rel="noopener noreferrer" class="source-link" data-outbound>{n}</a>'
        for n, u in plats)
    return f'''    <section class="section section--{bg}" aria-labelledby="sources-heading">
      <div class="container" style="text-align:center;">
        <p class="section-eyebrow">Find Us Online</p>
        <h2 id="sources-heading" class="section-title">Find Us on These Platforms</h2>
        <div class="source-links">{links}</div>
      </div>
    </section>'''

# ---------------------------------------------------------------- legal / sitemap
NOINDEX = "noindex, follow"

def legal_page(slug, title, description, h1, last_updated, sections, robots=NOINDEX):
    url = f"{BASE}/{slug}/"
    label = h1
    crumbs = [("Home", "/"), (label, None)]
    crumbs_schema = [("Home", "/"), (label, url)]
    crumb_items = "".join(
        f'<li><a href="{u}">{n}</a></li>' if u else f'<li aria-current="page">{n}</li>'
        for n, u in crumbs)
    secs = ""
    for h2, paras in sections:
        secs += a_h2(h2) + "".join(a_p(p) for p in paras)
    body = f'''    <section class="article-wrap">
      <div class="container">
        <article class="article legal">
          <nav class="breadcrumb breadcrumb--dark" aria-label="Breadcrumb"><ol>{crumb_items}</ol></nav>
          <h1 class="article__title">{h1}</h1>
          <p class="legal__updated">Last Updated: {last_updated}</p>
          {secs}
        </article>
      </div>
    </section>'''
    return dict(slug=slug, title=title, description=description, canonical=url, robots=robots,
                schemas=[page_schema("WebPage", h1, description, url), breadcrumb(crumbs_schema)],
                body=body)

def link_group(title, links):
    lis = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in links)
    return f'<div class="sitemap-group"><h2 class="sitemap-group__title">{title}</h2><ul class="sitemap-list">{lis}</ul></div>'

def sitemap_section(groups):
    return f'''    <section class="section section--white" aria-label="Site links">
      <div class="container">
        <div class="sitemap-grid">{"".join(groups)}</div>
      </div>
    </section>'''

# ---------------------------------------------------------------- page shell
DEFAULT_ROBOTS = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"

def render(slug, title, description, canonical, schemas, body, robots=DEFAULT_ROBOTS,
           lang="en", head_extra="", header=None, footer=None):
    header = HEADER if header is None else header
    footer = FOOTER if footer is None else footer
    schema_blocks = "\n".join(
        f'  <script type="application/ld+json">\n  {s}\n  </script>' for s in schemas)
    og_desc = description if len(description) <= 200 else description[:197] + "..."
    extra = ("\n  " + head_extra) if head_extra else ""
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="{robots}">{extra}

  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/images/og-homepage.jpg">
  <meta property="og:locale" content="en_US">
  <meta property="og:site_name" content="Ayala Pro Painting">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{og_desc}">
  <meta name="twitter:image" content="{BASE}/images/og-homepage.jpg">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">

  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/svg+xml" href="/images/logo.svg">

  <link rel="stylesheet" href="/css/styles.css">
  <script src="/js/main.js" defer></script>

{schema_blocks}
</head>

<body>
{header}

  <main id="main-content">

{body}

  </main>

{footer}
</body>
</html>
'''
    out_dir = os.path.join(SITE, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return slug


# ================================================================ PAGES
def build_all():
    built = []
    for modname in ("pages", "areas", "resources", "standalone", "legal", "es"):
        try:
            mod = __import__(modname)
        except ImportError:
            continue
        for p in mod.PAGES:
            built.append(render(**p))
    return built

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    for slug in build_all():
        print("built:", slug + "/index.html")
    # Static-bucket post-process: convert root-relative href/src into depth-correct
    # relative paths + explicit index.html on directory links (storage.googleapis.com).
    from relativize import relativize_site
    n = len(relativize_site(SITE))
    print("relativized:", n, "HTML files for static-bucket hosting")
