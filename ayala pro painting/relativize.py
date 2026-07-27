#!/usr/bin/env python3
"""
Rewrite root-relative href/src/data-full attributes in every generated HTML file
into STRICT relative paths for hosting on a raw static bucket (storage.googleapis.com)
with no server-side routing or directory-index resolution.

Rules applied (to every .html file under site/, excluding partials/ templates):
  1. /-rooted paths -> path relative to THIS file's folder depth (./, ../, ../../).
  2. Internal directory links get an explicit "index.html" appended.
  3. Asset links (.css/.js/.svg/.ico/...) are relativized but NOT given index.html.

Intentionally NOT touched: production-domain URLs in <link rel="canonical"> and
hreflang <link> tags (SEO metadata must stay absolute; they don't affect navigation),
and JSON-LD URLs (script content, not href/src). CSS has no url() paths; the single
JS-generated nav link is made depth-aware at runtime via rootPrefix() in main.js.
"""
import os, re

ATTR_RE = re.compile(r'(?P<attr>\b(?:href|src|data-full))="(?P<val>/[^"]*)"')
FILE_EXT_RE = re.compile(r'\.[A-Za-z0-9]{2,5}$')

def relativize_value(val, prefix):
    # Split off a fragment (#...) so we transform only the path portion.
    frag = ""
    if "#" in val:
        val, frag = val.split("#", 1)
        frag = "#" + frag
    if val == "":            # was a pure "#anchor" — leave path empty
        return prefix.rstrip("/") + "/" + frag if frag else prefix
    rest = val[1:]           # strip leading "/"
    if rest == "":           # "/" -> home
        target = "index.html"
    elif rest.endswith("/"):  # explicit directory -> append index.html
        target = rest + "index.html"
    elif FILE_EXT_RE.search(rest.split("/")[-1]):  # last segment looks like a file
        target = rest
    else:                    # directory without trailing slash -> append /index.html
        target = rest + "/index.html"
    return prefix + target + frag

def relativize_html(text, depth):
    prefix = "./" if depth == 0 else ("../" * depth)
    def repl(m):
        return '%s="%s"' % (m.group("attr"), relativize_value(m.group("val"), prefix))
    return ATTR_RE.sub(repl, text)

def relativize_site(site_dir, exclude_dirs=("partials",)):
    changed = []
    for root, dirs, files in os.walk(site_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for fn in files:
            if not fn.endswith(".html"):
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, site_dir).replace("\\", "/")
            depth = rel.count("/")          # parts-1 == directory depth below site/
            with open(full, encoding="utf-8") as f:
                text = f.read()
            new = relativize_html(text, depth)
            if new != text:
                with open(full, "w", encoding="utf-8") as f:
                    f.write(new)
                changed.append(rel)
    return changed

if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    site = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
    changed = relativize_site(site)
    print("Relativized %d HTML files:" % len(changed))
    for c in changed:
        print("  " + c)
