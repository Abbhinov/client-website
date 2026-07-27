#!/usr/bin/env python3
"""
Bake-and-relativize script for static GCS hosting.

For every HTML file in the workspace (excluding build/temp folders):
  1. Inline all <div data-include="/partials/X.html"></div> placeholders with
     the partial's contents.
  2. Convert every href="/foo" and src="/foo" to a strictly relative path based
     on the page's depth (./, ../, ../../).
  3. Append /index.html to every internal directory link (paths that don't
     point at an explicit file extension).
  4. Preserve external https://... URLs, mailto:, tel:, anchor (#...), and
     metadata URLs in canonical/OG/JSON-LD/hreflang (those are not navigated
     to by the browser).

Re-run safely: idempotent on already-baked files because the regex only
matches absolute paths that start with "/".
"""

import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent  # workspace root

EXCLUDE_DIRS = {'_extracted', 'example', 'images', 'css', 'js', 'partials'}

# Partials live here. We read them once and inline per-page.
PARTIAL_DIR = ROOT / 'partials'

# ---------------------------------------------------------------------------
# Regex helpers
# ---------------------------------------------------------------------------

# Match href="/..." or src="/..." (single or double quotes), but NOT
# protocol-relative // URLs.
PATH_ATTR = re.compile(r'(\s(?:href|src)\s*=\s*)(["\'])(/(?!/)[^"\']*)(\2)', re.IGNORECASE)

# Match <div data-include="..."></div>
INCLUDE_TAG = re.compile(r'<div\s+data-include\s*=\s*"([^"]+)"\s*></div>')

# File-extension regex used to detect "this path points at a real asset"
# vs "this is a directory link that needs index.html appended".
ASSET_EXT = re.compile(
    r'\.(html?|css|js|ico|png|jpe?g|gif|svg|webp|json|xml|txt|pdf|woff2?|mp4|webm|map)$',
    re.IGNORECASE,
)


def page_depth(path: pathlib.Path) -> int:
    """Number of '../' segments needed to reach project root from this page."""
    rel = path.relative_to(ROOT)
    return len(rel.parts) - 1  # subtract 1 for the file itself


def relativize(absolute_path: str, depth: int) -> str:
    """Convert '/foo/bar' (or '/foo/bar?qs#frag') to a depth-relative path,
    appending '/index.html' when the path does not already look like an asset."""
    # Split off query and fragment so we don't mangle them.
    path = absolute_path
    fragment = ''
    if '#' in path:
        path, frag = path.split('#', 1)
        fragment = '#' + frag
    query = ''
    if '?' in path:
        path, q = path.split('?', 1)
        query = '?' + q

    # Strip leading slash.
    path = path.lstrip('/')

    if path == '':
        # Root URL → homepage
        path = 'index.html'
    elif not ASSET_EXT.search(path):
        # Directory-like; append index.html
        path = path.rstrip('/') + '/index.html'

    # Build prefix
    prefix = './' if depth == 0 else '../' * depth
    return prefix + path + query + fragment


def fix_paths_in(content: str, depth: int) -> str:
    def repl(m: re.Match) -> str:
        attr_eq = m.group(1)
        quote = m.group(2)
        raw = m.group(3)
        return f'{attr_eq}{quote}{relativize(raw, depth)}{quote}'

    return PATH_ATTR.sub(repl, content)


def inline_partials(content: str, depth: int) -> str:
    """Replace <div data-include="..."></div> with the partial's inlined HTML,
    rewriting paths inside the partial relative to the current page's depth."""
    def repl(m: re.Match) -> str:
        target = m.group(1).lstrip('/')
        partial = ROOT / target
        if not partial.exists():
            print(f'  ! missing partial: {target}')
            return m.group(0)
        body = partial.read_text(encoding='utf-8')
        return fix_paths_in(body, depth)
    return INCLUDE_TAG.sub(repl, content)


def html_files():
    """Yield every HTML file we should process."""
    for path in ROOT.rglob('*.html'):
        rel_parts = path.relative_to(ROOT).parts
        if any(p in EXCLUDE_DIRS for p in rel_parts):
            continue
        yield path


def main() -> None:
    files = sorted(html_files())
    print(f'Processing {len(files)} HTML files\n')
    for path in files:
        depth = page_depth(path)
        content = path.read_text(encoding='utf-8')
        # 1. Inline partials (paths inside them get fixed)
        new_content = inline_partials(content, depth)
        # 2. Fix any remaining absolute paths in the page body
        new_content = fix_paths_in(new_content, depth)
        if new_content != content:
            path.write_text(new_content, encoding='utf-8')
            print(f'  baked  {path.relative_to(ROOT)}  (depth={depth})')
        else:
            print(f'  skip   {path.relative_to(ROOT)}  (already relative)')
    print('\nDone.')


if __name__ == '__main__':
    main()
