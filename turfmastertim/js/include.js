/**
 * EDGE 2 HEDGES — Header / Footer include + UI behaviors
 *
 * Loads partials/header.html into <div id="site-header"></div>
 * Loads partials/footer.html into <div id="site-footer"></div>
 *
 * The site is hosted on a raw file server (Google Cloud Storage)
 * with no server-side rewrites. Every link must be a strict
 * relative path that ends in an explicit file (typically
 * index.html). Because the partials are shared across pages
 * stored at varying directory depths, this script computes the
 * current page's depth and rewrites every relative href / src
 * inside the loaded partial markup so it resolves correctly.
 *
 * Each .html page must include:
 *   <div id="site-header"></div>
 *   ...page content...
 *   <div id="site-footer"></div>
 *   <script src="../../js/include.js" defer></script>     <!-- adjust ../ count to match depth -->
 */

(function () {
  'use strict';

  // ---------------------------------------------------------------
  // 1. Derive the depth prefix from THIS script tag's own src.
  //
  //    Each page already ships with a depth-correct relative
  //    reference to this file:
  //      depth 0 (root)        =>  src="js/include.js"
  //      depth 1 (/about/...)  =>  src="../js/include.js"
  //      depth 2 (/x/y/...)    =>  src="../../js/include.js"
  //
  //    Counting the leading "../" segments gives us the prefix
  //    we need to reach the site root from the current page.
  //    This works regardless of where the site is mounted —
  //    file://, https://example.com/, or
  //    https://storage.googleapis.com/<bucket>/ — because we
  //    never rely on window.location.pathname to figure out
  //    where the site root lives.
  // ---------------------------------------------------------------
  function depthPrefix() {
    const scripts = document.getElementsByTagName('script');
    for (let i = scripts.length - 1; i >= 0; i--) {
      const raw = scripts[i].getAttribute('src');
      if (raw && /(^|\/)js\/include\.js(\?|#|$)/.test(raw)) {
        const m = raw.match(/^((?:\.\.\/)*)/);
        return m ? m[1] : '';
      }
    }
    return '';
  }

  // ---------------------------------------------------------------
  // 2. Decide whether a given href / src value is an internal
  //    relative path that needs the depth prefix prepended.
  // ---------------------------------------------------------------
  const ABSOLUTE_OR_SCHEME = /^(?:[a-z][a-z0-9+.-]*:|\/\/|#)/i;
  function needsPrefix(value) {
    if (!value) return false;
    if (ABSOLUTE_OR_SCHEME.test(value)) return false; // tel:, mailto:, https:, //cdn, #anchor
    if (value.startsWith('/')) return false;          // already root-absolute (shouldn't occur after refactor)
    return true;
  }

  // ---------------------------------------------------------------
  // 3. Load a partial HTML file into a target element and rewrite
  //    its relative paths so they resolve from the current page.
  // ---------------------------------------------------------------
  async function loadPartial(targetId, partialFilename, prefix) {
    const target = document.getElementById(targetId);
    if (!target) return null;

    const url = prefix + 'partials/' + partialFilename;
    try {
      const response = await fetch(url, { cache: 'no-cache' });
      if (!response.ok) {
        console.error('Failed to load ' + url + ': HTTP ' + response.status);
        return null;
      }
      const html = await response.text();

      // Parse the partial in isolation, rewrite paths, then inject.
      const tpl = document.createElement('template');
      tpl.innerHTML = html;
      rewritePaths(tpl.content, prefix);
      target.replaceWith(...tpl.content.childNodes);
      return true;
    } catch (err) {
      console.error('Error loading ' + url + ':', err);
      return null;
    }
  }

  function rewritePaths(root, prefix) {
    if (!prefix) return; // depth 0 — partials are already correct as-is.
    const els = root.querySelectorAll('[href], [src]');
    els.forEach((el) => {
      const href = el.getAttribute('href');
      if (needsPrefix(href)) el.setAttribute('href', prefix + href);
      const src = el.getAttribute('src');
      if (needsPrefix(src)) el.setAttribute('src', prefix + src);
    });
  }

  // ---------------------------------------------------------------
  // 4. Mark the active nav link based on the current path.
  // ---------------------------------------------------------------
  function markActiveNav() {
    const path = window.location.pathname;
    let activeKey = 'home';

    if (/\/services\//.test(path))           activeKey = 'services';
    else if (/\/service-areas\//.test(path)) activeKey = 'service-areas';
    else if (/\/about\//.test(path))         activeKey = 'about';
    else if (/\/blog\//.test(path))          activeKey = 'blog';
    else if (/\/contact\//.test(path))       activeKey = 'contact';

    document.querySelectorAll('[data-nav]').forEach((link) => {
      if (link.getAttribute('data-nav') === activeKey) {
        link.classList.add('is-active');
      }
    });
  }

  // ---------------------------------------------------------------
  // 5. Sticky header shadow on scroll.
  // ---------------------------------------------------------------
  function wireStickyHeader() {
    const header = document.querySelector('[data-header]');
    if (!header) return;

    const onScroll = () => {
      if (window.scrollY > 4) header.dataset.scrolled = 'true';
      else delete header.dataset.scrolled;
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // ---------------------------------------------------------------
  // 6. Mobile hamburger menu toggle.
  // ---------------------------------------------------------------
  function wireMobileMenu() {
    const btn = document.querySelector('[data-hamburger]');
    const mobileNav = document.querySelector('[data-mobile-nav]');
    if (!btn || !mobileNav) return;

    btn.addEventListener('click', () => {
      const open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      if (open) {
        mobileNav.setAttribute('hidden', '');
      } else {
        mobileNav.removeAttribute('hidden');
      }
    });
  }

  // ---------------------------------------------------------------
  // 7. Set the current year in the footer.
  // ---------------------------------------------------------------
  function setFooterYear() {
    const el = document.querySelector('[data-year]');
    if (el) el.textContent = String(new Date().getFullYear());
  }

  // ---------------------------------------------------------------
  // 8. Boot.
  // ---------------------------------------------------------------
  async function init() {
    const prefix = depthPrefix();
    await Promise.all([
      loadPartial('site-header', 'header.html', prefix),
      loadPartial('site-footer', 'footer.html', prefix),
    ]);

    markActiveNav();
    wireStickyHeader();
    wireMobileMenu();
    setFooterYear();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
