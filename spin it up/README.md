# Spin It Up Laundry — Website

Static marketing site for Spin It Up Laundry (`spinituplaundry.net`), built from the
TradeWorks AI Strategy & Architecture document and per-page Developer Guides (v1.0).

This repo contains **Phases 1–3** of the roadmap: the full English site, the neighborhood
area pages, every service page, the complete Spanish (`/es/`) site, and the Resources/blog
silo (hub + 5 articles). **35 pages total** — the build is content-complete. What remains
is operational (real photos, Cents URL, form backend, GTM, attorney review) — see
"Before launch" below.

## What's here

```
site/                     ← deployable static site (this is what you publish) — 30 pages
  index.html              ← Homepage
  services/               ← Services hub + 5 service pages (incl. ironing-pressing)
  areas/                  ← Areas hub + avondale, irving-park, logan-square, hermosa, albany-park
  resources/             ← Resources hub + 5 articles (cents-app, winter tips,
                            comforter how-to, airbnb guide, ebt assistance)
  pricing/  contact/  faq/  about/
  privacy-policy/  terms-of-service/  accessibility/
  es/                     ← Spanish site: /es/ + servicios (+3), precios, contacto, preguntas-frecuentes
  404.html
  css/main.css            ← design system (tokens, components) — single stylesheet
  js/main.js              ← header scroll, mobile menu, FAQ accordion, sticky CTA, form handling
  images/                 ← logo + PLACEHOLDER photos (replace before launch)
  sitemap.xml  robots.txt

build/                    ← dev-time generator (NOT deployed)
  generate.py             ← wraps each page's content with shared chrome (bilingual EN/ES)
  gen_areas.py            ← data-driven generator for the 5 area-page content fragments
  pages.json              ← per-page metadata (title, meta, canonical, lang, hreflang…)
  content/*.html          ← each page's unique <main> content
  content/_<page>_head.html ← per-page JSON-LD schema

Spin it Up/               ← original source dev guides (.docx) + extracted text (_txt/)
```

### Bilingual notes
- Spanish pages set `lang: "es"` + `alt: <english-url>` in `pages.json`; the generator
  emits reciprocal `hreflang` (en/es/x-default) and a working EN|ES language toggle.
- The Spanish nav points untranslated pages (Areas, About, Commercial, Pressing) to their
  English versions, per the Spanish dev guide.
- To re-generate the 5 area pages after editing local content, run
  `python build/gen_areas.py` (writes content fragments), then `python build/generate.py`.

## How it's built

The site is plain static HTML/CSS/JS — no framework, no runtime dependencies.
The shared "chrome" (header, mobile menu, footer, sticky CTA bar) is identical on
every page, so to avoid copy-paste drift it lives in one place (`build/generate.py`)
and is stamped into each page at build time. **The output in `site/` is pure static
HTML** — the generator is only a dev convenience.

### Rebuild after editing content

```bash
python build/generate.py
```

Edit a page's body in `build/content/<page>.html`, its `<head>` schema in
`build/content/_<page>_head.html`, or its meta in `build/pages.json`, then rerun.
Shared header/footer markup lives in `build/generate.py`.

### Preview locally

```bash
cd site
python -m http.server 8080
# open http://127.0.0.1:8080/
```

## ⚠️ Replace before launch (placeholders)

The dev guides flag several values that require real client data:

| Placeholder | Where | What to do |
|---|---|---|
| `[CENTS_APP_URL]` (currently `href="#"` on Schedule-Pickup buttons + `data-cents`) | all pages | Replace `CENTS = "#"` in `build/generate.py` and the `href="#" data-cents` links in service-page content with the live Cents ordering URL |
| Placeholder images | `site/images/*.jpg` | Replace with **real** Spin It Up photos (storefront, interior, 130 lb machines, folded laundry, owner). Interim source: client Yelp/Instagram. Keep filenames. |
| `[OWNER NAME]`, `[He/She/They]`, founding year | `build/content/about.html` + `_about_head.html` | Client provides real story + founder/foundingDate for schema |
| `[CENTS_PRIVACY_URL]` | `build/content/privacy-policy.html` | Real Cents privacy policy URL |
| Effective / Last-updated dates | legal pages | Currently set to May 24, 2026 — confirm at publish time |
| Pricing values | pricing + service pages | Confirm all $ amounts with client (audit-based estimates) |
| `YOUR_PLACE_ID` | review links (footer, homepage) | Replace with the Google Business Profile place ID |
| App Store / Google Play links | pickup-delivery page | Real Cents app store URLs (currently `#`) |
| Form backend | contact + commercial forms | Forms validate + show an on-page success message client-side only. Wire `action` to a real endpoint (Formspree, Netlify Forms, Cloud Function) that emails `info@spinituplaundry.net`. See `js/main.js` `form.js-form`. |
| GA4 / GTM | site-wide | `js/main.js` pushes events to `window.dataLayer` (no-op until GTM is installed). Add the GTM container snippet to the generator's `<head>`. |

Legal pages (privacy, terms, accessibility) are a **starting framework only** and must be
reviewed by an attorney before publishing (EBT data, Illinois BIPA, two-party consent).

## Optional future work

The roadmap pages are all built. Nice-to-haves that remain:

- Spanish translations of the Areas and About pages (currently English; the Spanish nav
  links to the English versions, as specified in the Spanish dev guide).
- More blog articles in `/resources/` over time for topical authority.
- The Resources articles were authored to the strategy doc's topic list (no per-page dev
  guide existed for them); have the client review the content like any other page.

Adding a page: drop a `build/content/<page>.html`, an optional `_<page>_head.html`,
and a `build/pages.json` entry, then rerun the generator.

## Notes on guide fidelity

- The Strategy doc (§6.4) defines the sticky mobile CTA bar globally as **Call Now +
  Schedule Pickup**, so it's uniform site-wide. A few individual page guides suggested
  per-page sticky overrides (e.g. "Get Directions" on self-service/contact) — these were
  left as the global default for consistency and can be added per-page if desired.
- All copy, meta tags, JSON-LD, and structure follow the per-page Developer Guides.
