"""
Static-site refactor for raw GCS bucket hosting.

Applies to all *.html files in site/:
  Rule 1: Strip absolute paths (/) and production domain (cleanslatepw.com); replace
          with relative paths based on each file's depth from site/.
  Rule 2: Append index.html to every directory-style link.
  Rule 3: <link rel="stylesheet">, <script src>, <img src> all use relative paths.
  Rule 4: Inline the three partials (announcement-bar, header, footer) directly into
          every HTML file so paths inside the partials get relativized per host page.

Out of scope: sitemap.xml and robots.txt reference the production domain by necessity
(sitemap.xml URLs MUST be absolute per spec). They'll need a domain swap at deploy time.
"""
import re
from pathlib import Path

ROOT = Path(r"C:\Users\Abbhinov\vscode\cleanslate-PW\site")
PROD = "https://cleanslatepw.com"

# Load raw partials once
partials = {}
for name in ("announcement-bar", "header", "footer"):
    partials[name] = (ROOT / "partials" / f"{name}.html").read_text(encoding="utf-8")


def make_relative(abs_url: str, depth: int) -> str:
    """
    Convert an absolute URL (root-relative or production-domain) to a relative URL
    appropriate for a page at the given depth. Returns input unchanged if it's not
    something we should transform.
    """
    # Pull off the path component
    if abs_url.startswith(PROD):
        path_part = abs_url[len(PROD):] or "/"
    elif abs_url.startswith("/"):
        path_part = abs_url
    else:
        return abs_url

    # Separate query and fragment
    fragment = ""
    if "#" in path_part:
        path_part, frag = path_part.split("#", 1)
        fragment = "#" + frag
    query = ""
    if "?" in path_part:
        path_part, q = path_part.split("?", 1)
        query = "?" + q

    # Strip leading slash
    if path_part.startswith("/"):
        path_part = path_part[1:]

    # Directory-style links need an explicit index.html
    if path_part == "" or path_part.endswith("/"):
        path_part = path_part + "index.html"
    else:
        last_seg = path_part.split("/")[-1]
        if "." not in last_seg:
            # No file extension on the last segment — treat as directory
            path_part = path_part + "/index.html"
        # otherwise has an extension (e.g. .css, .svg, .xml, .jpg) — leave as file

    prefix = "../" * depth if depth > 0 else ""
    return prefix + path_part + query + fragment


# --- transformations ---

ATTR_RE = re.compile(r'\b(href|src)=(["\'])([^"\']+)\2')
META_CONTENT_RE = re.compile(r'(content=")(https?://cleanslatepw\.com[^"]+|/[^"]+)"')
JSONLD_BLOCK_RE = re.compile(
    r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL
)
JSONLD_URL_RE = re.compile(r'"(https?://cleanslatepw\.com[^"]*)"')


def transform_attr(match: re.Match, depth: int) -> str:
    attr_name = match.group(1)
    quote = match.group(2)
    url = match.group(3)

    # Special schemes: leave alone
    if url.startswith(("tel:", "mailto:", "javascript:", "data:", "#")):
        return match.group(0)
    # External domains other than cleanslatepw.com: leave alone
    if url.startswith(("http://", "https://")) and not url.startswith(PROD):
        return match.group(0)
    # Already relative: leave alone
    if not (url.startswith("/") or url.startswith(PROD)):
        return match.group(0)

    new_url = make_relative(url, depth)
    return f"{attr_name}={quote}{new_url}{quote}"


def transform_meta(content: str, depth: int) -> str:
    def repl(m):
        before, url = m.group(1), m.group(2)
        new_url = make_relative(url, depth)
        return f"{before}{new_url}\""
    return META_CONTENT_RE.sub(repl, content)


def transform_jsonld(content: str, depth: int) -> str:
    def block_repl(bm):
        block = bm.group(0)
        def url_repl(um):
            return f'"{make_relative(um.group(1), depth)}"'
        return JSONLD_URL_RE.sub(url_repl, block)
    return JSONLD_BLOCK_RE.sub(block_repl, content)


def inline_partials(content: str) -> str:
    """
    Replace <div data-include="...header.html"></div> etc. with the raw partial
    content. The unified transform pass that follows will then relativize all paths
    in one shot, including those introduced by the partial.
    """
    for name, raw in partials.items():
        pattern = rf'<div\s+data-include="[^"]*partials/{re.escape(name)}\.html"\s*></div>'
        content = re.sub(pattern, raw, content)
    return content


def process_file(file: Path) -> int:
    rel = file.relative_to(ROOT)
    depth = len(rel.parts) - 1
    text = file.read_text(encoding="utf-8")

    text = inline_partials(text)
    text = ATTR_RE.sub(lambda m: transform_attr(m, depth), text)
    text = transform_meta(text, depth)
    text = transform_jsonld(text, depth)

    file.write_text(text, encoding="utf-8")
    return depth


# --- run ---
processed = []
for f in sorted(ROOT.rglob("*.html")):
    if "partials" in f.parts:
        continue
    depth = process_file(f)
    processed.append((depth, f.relative_to(ROOT)))

for depth, path in sorted(processed):
    print(f"  d{depth}: {path}")
print(f"\nProcessed {len(processed)} HTML files")
