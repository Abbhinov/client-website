"""UI/Visual audit script for Easy Clean Service static site.

Captures screenshots at 3 viewports for ~10 templates and runs DOM checks
via page.evaluate. Outputs JSON-per-page to audit-screenshots/<slug>.json
and PNG screenshots to audit-screenshots/<slug>-<width>.png.
"""

import json
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
SHOTS = ROOT / "audit-screenshots"
SHOTS.mkdir(exist_ok=True)

BASE = "http://localhost:8080"

PAGES = [
    ("homepage", "/index.html"),
    ("service-detail-regular-house-cleaning", "/services/regular-house-cleaning-tampa/index.html"),
    ("service-area-brandon", "/service-areas/brandon/index.html"),
    ("service-areas-hub", "/service-areas/index.html"),
    ("about", "/about/index.html"),
    ("contact", "/contact/index.html"),
    ("blog-index", "/blog/index.html"),
    ("blog-post-cost-tampa", "/blog/house-cleaning-cost-tampa/index.html"),
    ("services-hub", "/services/index.html"),
    ("privacy", "/privacy/index.html"),
]

VIEWPORTS = [
    ("desktop", 1440, 900),
    ("tablet", 768, 1024),
    ("mobile", 390, 844),
]

DOM_CHECKS_JS = r"""
() => {
  function rectsOf(el) {
    const r = el.getBoundingClientRect();
    return {x: r.x, y: r.y, w: r.width, h: r.height};
  }
  function tag(el) {
    let s = el.tagName.toLowerCase();
    if (el.id) s += '#' + el.id;
    if (el.className && typeof el.className === 'string') {
      s += '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.');
    }
    return s;
  }

  const out = {};
  out.viewport = {w: window.innerWidth, h: window.innerHeight};
  out.bodyScrollWidth = document.body.scrollWidth;
  out.horizontalOverflow = document.body.scrollWidth > window.innerWidth + 1;

  // Find offending wide elements (top 20)
  const wide = [];
  document.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width > window.innerWidth + 1 && r.height > 0) {
      wide.push({selector: tag(el), w: Math.round(r.width), left: Math.round(r.left)});
    }
  });
  wide.sort((a,b) => b.w - a.w);
  out.wideElements = wide.slice(0, 15);

  // Children wider than parent
  const overflowChildren = [];
  document.querySelectorAll('body *').forEach(el => {
    const parent = el.parentElement;
    if (!parent) return;
    const rEl = el.getBoundingClientRect();
    const rPar = parent.getBoundingClientRect();
    if (rEl.width > rPar.width + 2 && rEl.width > 50 && rPar.width > 0) {
      overflowChildren.push({selector: tag(el), elW: Math.round(rEl.width), parentW: Math.round(rPar.width), parent: tag(parent)});
    }
  });
  out.overflowChildren = overflowChildren.slice(0, 15);

  // Small tap targets (clickables < 44x44)
  const smallTargets = [];
  document.querySelectorAll('a, button, [role=button], input[type=button], input[type=submit]').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) return; // hidden
    if (el.offsetParent === null && getComputedStyle(el).position !== 'fixed') return;
    if (r.width < 44 || r.height < 44) {
      smallTargets.push({selector: tag(el), w: Math.round(r.width), h: Math.round(r.height), text: (el.innerText || el.value || '').slice(0, 30)});
    }
  });
  out.smallTapTargets = smallTargets.slice(0, 20);

  // Low-opacity text
  const lowOpacity = [];
  document.querySelectorAll('body *').forEach(el => {
    if (el.children.length > 0) return;
    const txt = (el.innerText || '').trim();
    if (!txt) return;
    const op = parseFloat(getComputedStyle(el).opacity);
    if (op < 0.5) {
      lowOpacity.push({selector: tag(el), opacity: op, text: txt.slice(0, 40)});
    }
  });
  out.lowOpacityText = lowOpacity.slice(0, 10);

  // FAQ check
  const faqItems = document.querySelectorAll('.faq-acc-item');
  out.faq = {count: faqItems.length, panels: []};
  faqItems.forEach((it, i) => {
    const panel = it.querySelector('.faq-acc-panel');
    out.faq.panels.push({
      i,
      hasPanel: !!panel,
      panelTextLen: panel ? (panel.innerText || '').trim().length : 0,
      panelDisplay: panel ? getComputedStyle(panel).display : null,
    });
  });

  // Before/after gallery
  const ba = document.querySelectorAll('.ba-slider');
  const photos = document.querySelectorAll('.gallery-photo');
  out.gallery = {
    baSliders: ba.length,
    galleryPhotos: photos.length,
    photoCaptions: [],
  };
  photos.forEach((p, i) => {
    const cap = p.querySelector('figcaption, .gallery-caption, .ba-label');
    out.gallery.photoCaptions.push({
      i,
      hasCaption: !!cap,
      captionText: cap ? (cap.innerText || '').trim().slice(0, 60) : null,
    });
  });

  // Exit-intent modal
  const exit = document.querySelector('.exit-modal, #exit-modal, [data-exit-modal]');
  out.exitModal = exit ? {
    present: true,
    display: getComputedStyle(exit).display,
    visibility: getComputedStyle(exit).visibility,
    hidden: exit.hidden,
    classes: exit.className,
  } : {present: false};

  // Mobile nav toggle
  const navToggle = document.querySelector('.nav-toggle, .menu-toggle, .hamburger');
  out.navToggle = navToggle ? {
    present: true,
    display: getComputedStyle(navToggle).display,
    visible: navToggle.offsetParent !== null,
    rect: rectsOf(navToggle),
  } : {present: false};

  // Sticky mobile CTA bar
  const ctaBar = document.querySelector('.mobile-cta-bar, .sticky-cta, .bottom-cta');
  out.mobileCtaBar = ctaBar ? {
    present: true,
    display: getComputedStyle(ctaBar).display,
    visible: ctaBar.offsetParent !== null,
    rect: rectsOf(ctaBar),
  } : {present: false};

  // Check overlap of CTA bar with estimate form (if both present)
  const form = document.querySelector('form, .estimate-form, #estimate, .quote-form');
  if (ctaBar && form && ctaBar.offsetParent !== null) {
    const rB = ctaBar.getBoundingClientRect();
    const rF = form.getBoundingClientRect();
    out.mobileCtaBar.overlapsForm = rB.top < rF.bottom && rB.bottom > rF.top;
    out.mobileCtaBar.formRect = rectsOf(form);
  }

  // Tables overflow
  const tables = [];
  document.querySelectorAll('table').forEach((t, i) => {
    const parent = t.parentElement;
    const pRect = parent.getBoundingClientRect();
    tables.push({
      i,
      tableW: t.scrollWidth,
      parentClientW: parent.clientWidth,
      parentOverflowX: getComputedStyle(parent).overflowX,
      overflows: t.scrollWidth > parent.clientWidth + 1,
      parentTag: tag(parent),
    });
  });
  out.tables = tables;

  // Headings list (for typography sanity)
  const headings = [];
  ['h1','h2','h3'].forEach(t => {
    document.querySelectorAll(t).forEach(h => {
      const cs = getComputedStyle(h);
      headings.push({
        tag: t,
        text: (h.innerText || '').trim().slice(0, 60),
        fontSize: cs.fontSize,
        textAlign: cs.textAlign,
      });
    });
  });
  out.headings = headings.slice(0, 20);

  // Breadcrumb check
  const breadcrumb = document.querySelector('.breadcrumb, .breadcrumbs, nav[aria-label*="readcrumb" i]');
  out.breadcrumb = breadcrumb ? {
    present: true,
    text: (breadcrumb.innerText || '').replace(/\n/g, ' | ').slice(0, 200),
    hasArrow: (breadcrumb.innerText || '').includes('>') || (breadcrumb.innerText || '').includes('›') || (breadcrumb.innerText || '').includes('/'),
  } : {present: false};

  // How-it-works step numbers
  const steps = document.querySelectorAll('.step, .step-card, .how-it-works .step, [class*="step-num"]');
  out.steps = [];
  steps.forEach(s => {
    out.steps.push({
      selector: tag(s),
      text: (s.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 100),
    });
  });

  // Footer columns
  const footer = document.querySelector('footer');
  if (footer) {
    const cols = footer.querySelectorAll('.footer-col, .footer-column, footer > div > div, footer ul');
    out.footer = {
      cols: cols.length,
      rect: rectsOf(footer),
    };
  }

  // Curly vs straight quotes
  const txt = document.body.innerText || '';
  out.quotes = {
    straight: (txt.match(/'/g) || []).length,
    straightDouble: (txt.match(/"/g) || []).length,
    curlySingleLeft: (txt.match(/‘/g) || []).length,
    curlySingleRight: (txt.match(/’/g) || []).length,
    curlyDoubleLeft: (txt.match(/“/g) || []).length,
    curlyDoubleRight: (txt.match(/”/g) || []).length,
  };

  // Town 'N' Country variations
  const lower = txt.toLowerCase();
  out.tnc = {
    straight: (txt.match(/Town 'N' Country/g) || []).length,
    curly: (txt.match(/Town ‘N’ Country/g) || []).length,
    appearances: (lower.match(/town .n. country/g) || []).length,
  };

  return out;
}
"""


def run():
    results = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for slug, path in PAGES:
            page_results = {}
            for vp_name, w, h in VIEWPORTS:
                context = browser.new_context(
                    viewport={"width": w, "height": h},
                    device_scale_factor=1,
                    reduced_motion="reduce",  # disables reveal-on-scroll opacity:0
                )
                # Suppress exit-intent modal before any page script runs
                context.add_init_script(
                    """
                    try { sessionStorage.setItem('ecs_exit_shown', '1'); } catch(e) {}
                    """
                )
                page = context.new_page()
                url = BASE + path
                try:
                    page.goto(url, wait_until="networkidle", timeout=20000)
                except Exception as e:
                    print(f"[WARN] {slug} {vp_name}: goto failed: {e}")
                # Wait a bit for fonts/images and any deferred init
                page.wait_for_timeout(1400)
                # Force reveal-on-scroll content to be visible (intersection observer
                # only fires for elements that enter the viewport; full-page screenshot
                # needs them all visible).
                page.evaluate(
                    """() => {
                        document.querySelectorAll('.reveal-on-scroll').forEach(el => el.classList.add('is-visible'));
                        // Also ensure exit modal is hidden if it slipped through
                        const m = document.getElementById('exit-intent-modal');
                        if (m && !m.hidden) { m.hidden = true; document.body.style.overflow = ''; }
                    }"""
                )
                page.wait_for_timeout(200)
                # Screenshot
                shot_path = SHOTS / f"{slug}-{w}.png"
                try:
                    page.screenshot(path=str(shot_path), full_page=True)
                except Exception as e:
                    print(f"[WARN] {slug} {vp_name}: screenshot failed: {e}")
                # DOM checks
                try:
                    dom = page.evaluate(DOM_CHECKS_JS)
                except Exception as e:
                    dom = {"error": str(e)}
                page_results[vp_name] = dom

                # FAQ click test (only on mobile/desktop to save time, do on first iter)
                if vp_name == "desktop":
                    try:
                        faq_count = page.locator(".faq-acc-item").count()
                        if faq_count > 0:
                            first = page.locator(".faq-acc-item").first
                            # find clickable: button or summary or the item itself
                            trigger = first.locator(".faq-acc-trigger, button, summary").first
                            try:
                                trigger.click(timeout=2000)
                                page.wait_for_timeout(400)
                                expanded = page.evaluate(
                                    """() => {
                                        const it = document.querySelector('.faq-acc-item');
                                        if (!it) return null;
                                        const panel = it.querySelector('.faq-acc-panel');
                                        if (!panel) return null;
                                        const cs = getComputedStyle(panel);
                                        const r = panel.getBoundingClientRect();
                                        return {
                                            display: cs.display,
                                            height: r.height,
                                            classes: it.className,
                                        };
                                    }"""
                                )
                                page_results["faqClickTest"] = {"ok": True, "afterClick": expanded}
                            except Exception as e:
                                page_results["faqClickTest"] = {"ok": False, "error": str(e)}
                    except Exception as e:
                        page_results["faqClickTest"] = {"ok": False, "error": str(e)}

                context.close()
                print(f"[OK] {slug} {vp_name} ({w}x{h})")

            results[slug] = page_results
            # Save per-page JSON
            with open(SHOTS / f"{slug}.json", "w", encoding="utf-8") as f:
                json.dump(page_results, f, indent=2, ensure_ascii=False, default=str)

        browser.close()

    # Save aggregate
    with open(SHOTS / "_all-results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)

    print("\nDONE. Results in", SHOTS)


if __name__ == "__main__":
    run()
