/* =========================================================
   Cool & Cozy AC Repair — Cloudflare Worker
   Language auto-redirect at the edge.

   Behavior:
     - Only acts on the apex / www root path. Deep links pass through.
     - Honors the `lang-preference` cookie first (set by the in-page toggle).
     - Falls back to Accept-Language (ranked, q-value aware).
     - Defaults to English if neither es nor en is found.
     - Never redirects requests already on es.coolcozyac.com.

   Deploy:
     1. Cloudflare dashboard → Workers & Pages → Create Worker.
     2. Paste this file; Save & Deploy.
     3. Add a Trigger / Route: `coolcozyac.com/*` (and `www.coolcozyac.com/*` if used).
        Do NOT route `es.coolcozyac.com/*` here — the Spanish site bypasses this Worker.
     4. Make sure the apex/`www` DNS records are proxied (orange cloud) so the Worker runs.
   ========================================================= */

const ES_ORIGIN = 'https://es.coolcozyac.com/';
const EN_HOSTS = new Set(['coolcozyac.com', 'www.coolcozyac.com']);

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // Safety: only act on the English-side hostnames.
    if (!EN_HOSTS.has(url.hostname)) {
      return fetch(request);
    }

    // Only the root (or explicit /index.html) is a redirect candidate.
    // Deep links — /about, /services/ac-repair, etc. — always pass through.
    if (url.pathname !== '/' && url.pathname !== '/index.html') {
      return fetch(request);
    }

    // 1. Manual preference wins.
    const pref = readCookie(request.headers.get('Cookie'), 'lang-preference');
    if (pref === 'en') return fetch(request);
    if (pref === 'es') return Response.redirect(ES_ORIGIN, 302);

    // 2. Auto-detect from Accept-Language.
    const detected = detectLanguage(request.headers.get('Accept-Language') || '');
    if (detected === 'es') return Response.redirect(ES_ORIGIN, 302);

    // Default: serve English.
    return fetch(request);
  },
};

function readCookie(header, name) {
  if (!header) return null;
  const parts = header.split(/;\s*/);
  for (const p of parts) {
    const eq = p.indexOf('=');
    if (eq < 0) continue;
    if (p.slice(0, eq).trim() === name) {
      return decodeURIComponent(p.slice(eq + 1));
    }
  }
  return null;
}

function detectLanguage(acceptLanguage) {
  // Accept-Language: "es-MX,es;q=0.9,en;q=0.8,*;q=0.5"
  const ranked = acceptLanguage
    .split(',')
    .map((entry) => {
      const [tag, ...params] = entry.trim().split(';');
      const qParam = params.find((x) => x.trim().startsWith('q='));
      const q = qParam ? parseFloat(qParam.split('=')[1]) : 1.0;
      return { base: tag.toLowerCase().split('-')[0], q: isNaN(q) ? 0 : q };
    })
    .filter((x) => x.base)
    .sort((a, b) => b.q - a.q);

  for (const { base } of ranked) {
    if (base === 'es') return 'es';
    if (base === 'en') return 'en';
  }
  return 'en';
}
