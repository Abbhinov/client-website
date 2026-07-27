"""
Spin It Up Laundry — Service Area / Neighborhood Hero Images (v4)
=================================================================
6 SVGs for local-SEO neighborhood pickup & delivery pages.

PAGES:
  hero-area-avondale.svg
  hero-area-logan-square.svg
  hero-area-irving-park.svg
  hero-area-roscoe-village.svg
  hero-area-albany-park.svg
  hero-area-bucktown.svg

LAYOUT — same as v3:
  viewBox 1600 x 900 (16:9)
  Left ~55% (x 0–860): background only — text overlay zone
  Right ~45% (x 860–1600): illustration

DESIGN:
  - Each neighborhood gets a horizontal "neighborhood plaque" banner
    with the name and a PICKUP & DELIVERY subtitle (the local-SEO hook).
  - A characteristic skyline silhouette below the banner — building
    shapes vary by neighborhood (bungalows, 3-flats, monument, etc).
  - A Spin It Up delivery van in the foreground with a laundry bag.
  - A dashed route to a destination pin showing "delivery here".
"""

import os

OUT_DIR = "/home/claude/output_v4"
os.makedirs(OUT_DIR, exist_ok=True)

RX = 860  # right-zone start (matches v3)

C = {
    "bg_top": "#0A1A3D", "bg_bot": "#142A55", "bg_glow": "#3A6FB0", "bg_warm": "#D89A55",
    "chrome_hi": "#F4F7FA", "chrome_mid": "#A8B5C5", "chrome_low": "#3D4A5C", "chrome_dark": "#1B2330",
    "glass_hi": "#EAF3FF", "glass_mid": "#7BA4D6", "glass_low": "#1E3458",
    "brand_dark": "#0B2447", "brand": "#19376D", "brand_lt": "#576CBC",
    "amber": "#E6A23C", "amber_dk": "#B07820", "amber_lt": "#F4C77F",
    "linen_hi": "#F8F4EC", "linen_mid": "#E4DDC9", "linen_low": "#A89B7A",
    "brick": "#8B4F3D", "brick_lt": "#A8624F", "brick_dk": "#5C3326",
    "white": "#FFFFFF", "off_white": "#F0F4F8",
    "gray_lt": "#CFD6E0", "gray_md": "#7C8699", "gray_dk": "#3A4456", "ink": "#0A1A3D",
    "mint": "#5FB07A", "coral": "#C46A5C", "lilac": "#876FB0",
    "warm_window": "#F4C77F",
}

SHARED_DEFS = f"""
<defs>
  <linearGradient id="bgBase" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{C['bg_top']}"/>
    <stop offset="100%" stop-color="{C['bg_bot']}"/>
  </linearGradient>
  <radialGradient id="bgGlow" cx="78%" cy="18%" r="65%">
    <stop offset="0%" stop-color="{C['bg_warm']}" stop-opacity="0.35"/>
    <stop offset="35%" stop-color="{C['bg_glow']}" stop-opacity="0.20"/>
    <stop offset="100%" stop-color="{C['bg_top']}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="bgVignette" cx="50%" cy="50%" r="80%">
    <stop offset="60%" stop-color="#000" stop-opacity="0"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.35"/>
  </radialGradient>
  <linearGradient id="floorGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{C['bg_bot']}" stop-opacity="0"/>
    <stop offset="60%" stop-color="#091532" stop-opacity="0.55"/>
    <stop offset="100%" stop-color="#040A1F" stop-opacity="0.85"/>
  </linearGradient>
  <linearGradient id="chromeSide" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{C['chrome_low']}"/>
    <stop offset="100%" stop-color="{C['chrome_mid']}"/>
  </linearGradient>
  <linearGradient id="vanBody" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{C['brand_lt']}"/>
    <stop offset="100%" stop-color="{C['brand']}"/>
  </linearGradient>
  <linearGradient id="signGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{C['linen_hi']}"/>
    <stop offset="100%" stop-color="{C['linen_mid']}"/>
  </linearGradient>
  <linearGradient id="skylineGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1A2C53"/>
    <stop offset="100%" stop-color="#0E1D40"/>
  </linearGradient>

  <filter id="ds-soft" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="10"/>
    <feOffset dy="14"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.32"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="ds-tight" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
    <feOffset dy="6"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.40"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glow-amber" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="10"/>
  </filter>
</defs>"""


def background_layer():
    return f"""
  <rect width="1600" height="900" fill="url(#bgBase)"/>
  <rect width="1600" height="900" fill="url(#bgGlow)"/>
  <g opacity="0.06" stroke="{C['bg_warm']}" stroke-width="1" fill="none">
    <line x1="0" y1="160" x2="1600" y2="160"/>
    <line x1="0" y1="320" x2="1600" y2="320"/>
    <line x1="0" y1="480" x2="1600" y2="480"/>
    <line x1="0" y1="640" x2="1600" y2="640"/>
  </g>
  <rect x="0" y="540" width="1600" height="360" fill="url(#floorGrad)"/>
  <rect width="1600" height="900" fill="url(#bgVignette)"/>"""


def svg_wrap(inner, title, desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="t d">
  <title id="t">{title}</title>
  <desc id="d">{desc}</desc>
  {SHARED_DEFS}
  {background_layer()}
  {inner}
</svg>'''


# ──────────────────────────────────────────────────────────────────
# REUSABLE COMPONENTS
# ──────────────────────────────────────────────────────────────────

def neighborhood_plaque(name, subtitle="PICKUP &amp; DELIVERY", x=900, y=140):
    """A horizontal plaque/sign showing the neighborhood name prominently."""
    w, h = 660, 170
    # Adjust the display font-size based on name length
    name_size = 48 if len(name) <= 12 else 40 if len(name) <= 16 else 34
    return f"""
  <g transform="translate({x}, {y})" filter="url(#ds-soft)">
    <!-- back plate (darker, slight offset for stacked sign look) -->
    <rect x="6" y="8" width="{w}" height="{h}" rx="10" fill="{C['brand_dark']}" opacity="0.9"/>
    <!-- main plaque -->
    <rect x="0" y="0" width="{w}" height="{h}" rx="10" fill="url(#signGrad)"/>
    <!-- top brand strip -->
    <rect x="0" y="0" width="{w}" height="34" rx="10" fill="{C['brand']}"/>
    <rect x="0" y="22" width="{w}" height="12" fill="{C['brand']}"/>
    <rect x="0" y="32" width="{w}" height="3" fill="{C['amber']}"/>
    <!-- top eyebrow -->
    <text x="{w/2}" y="22" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="800" fill="{C['amber_lt']}" letter-spacing="5">SPIN IT UP · {subtitle}</text>
    <!-- inner border -->
    <rect x="14" y="48" width="{w - 28}" height="{h - 62}" fill="none" stroke="{C['amber']}" stroke-width="1.5" opacity="0.6"/>
    <!-- decorative corner accents -->
    <g fill="{C['amber']}" opacity="0.7">
      <circle cx="24" cy="58" r="3"/>
      <circle cx="{w - 24}" cy="58" r="3"/>
      <circle cx="24" cy="{h - 24}" r="3"/>
      <circle cx="{w - 24}" cy="{h - 24}" r="3"/>
    </g>
    <!-- name (the headliner) -->
    <text x="{w/2}" y="{h/2 + 22}" text-anchor="middle"
          font-family="Georgia, serif" font-weight="800" font-size="{name_size}"
          fill="{C['brand_dark']}" letter-spacing="3">{name.upper()}</text>
    <!-- subline -->
    <text x="{w/2}" y="{h - 26}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="{C['gray_md']}" letter-spacing="3">FREE DELIVERY · SAME-DAY AVAILABLE</text>
  </g>"""


def delivery_van(x=900, y=620, label="SPIN IT UP"):
    """A simplified but well-detailed delivery van facing right."""
    return f"""
  <g transform="translate({x}, {y})" filter="url(#ds-soft)">
    <!-- ground shadow -->
    <ellipse cx="155" cy="120" rx="170" ry="14" fill="#000" opacity="0.55"/>
    <!-- back cargo box -->
    <rect x="-10" y="-90" width="240" height="130" rx="8" fill="url(#vanBody)" stroke="{C['brand_dark']}" stroke-width="1.5"/>
    <!-- top stripe -->
    <rect x="-10" y="-90" width="240" height="22" fill="{C['brand']}"/>
    <!-- cab section (slants forward) -->
    <path d="M 230 -90 L 290 -50 L 290 40 L 230 40 Z" fill="url(#vanBody)" stroke="{C['brand_dark']}" stroke-width="1.5"/>
    <!-- windshield -->
    <path d="M 230 -88 L 285 -50 L 285 -16 L 230 -16 Z" fill="{C['glass_mid']}" opacity="0.75"/>
    <line x1="230" y1="-50" x2="285" y2="-50" stroke="{C['brand_dark']}" stroke-width="1.5"/>
    <!-- door seam -->
    <line x1="105" y1="-90" x2="105" y2="40" stroke="{C['brand_dark']}" stroke-width="1.5"/>
    <line x1="105" y1="-30" x2="115" y2="-30" stroke="{C['brand_dark']}" stroke-width="1"/>
    <!-- side branding -->
    <text x="60" y="-20" font-family="Georgia, serif" font-weight="800" font-size="22" fill="{C['white']}" letter-spacing="1">{label}</text>
    <text x="60" y="-2" font-family="sans-serif" font-size="9" fill="{C['amber_lt']}" letter-spacing="3">LAUNDRY · PICKUP &amp; DELIVERY</text>
    <!-- small circular icon on the door -->
    <circle cx="155" cy="18" r="14" fill="{C['amber']}"/>
    <circle cx="155" cy="18" r="9" fill="{C['white']}"/>
    <circle cx="155" cy="18" r="4" fill="{C['brand']}"/>
    <!-- wheels -->
    <circle cx="42" cy="50" r="22" fill="{C['ink']}"/>
    <circle cx="42" cy="50" r="14" fill="{C['chrome_mid']}"/>
    <circle cx="42" cy="50" r="6" fill="{C['chrome_dark']}"/>
    <path d="M 42 38 v 24 M 30 50 h 24" stroke="{C['chrome_dark']}" stroke-width="1" opacity="0.6"/>
    <circle cx="225" cy="50" r="22" fill="{C['ink']}"/>
    <circle cx="225" cy="50" r="14" fill="{C['chrome_mid']}"/>
    <circle cx="225" cy="50" r="6" fill="{C['chrome_dark']}"/>
    <path d="M 225 38 v 24 M 213 50 h 24" stroke="{C['chrome_dark']}" stroke-width="1" opacity="0.6"/>
    <!-- headlight glow -->
    <circle cx="288" cy="14" r="6" fill="{C['amber_lt']}"/>
    <circle cx="295" cy="20" r="18" fill="{C['amber_lt']}" opacity="0.30" filter="url(#glow-amber)"/>
    <!-- side mirror -->
    <rect x="223" y="-44" width="10" height="6" fill="{C['chrome_dark']}"/>
  </g>"""


def laundry_bag_small(x, y):
    """Compact drawstring laundry bag for the foreground."""
    return f"""
  <g transform="translate({x}, {y})" filter="url(#ds-tight)">
    <ellipse cx="50" cy="118" rx="60" ry="8" fill="#000" opacity="0.5"/>
    <path d="M 15 38 C 0 50 -4 100 12 122 C 28 138 72 138 88 122 C 104 100 100 50 85 38 C 78 33 70 30 50 30 C 30 30 22 33 15 38 Z"
          fill="{C['brand']}" stroke="{C['brand_dark']}" stroke-width="1.5"/>
    <path d="M 22 50 C 14 70 14 100 24 122" stroke="{C['brand_lt']}" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.6"/>
    <ellipse cx="50" cy="32" rx="32" ry="9" fill="{C['brand_dark']}"/>
    <path d="M 30 32 Q 36 22 42 30 Q 48 18 54 30 Q 60 22 66 32" fill="none" stroke="{C['brand']}" stroke-width="2"/>
    <path d="M 32 30 Q 22 16 18 36" fill="none" stroke="{C['amber']}" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 68 30 Q 78 14 82 36" fill="none" stroke="{C['amber']}" stroke-width="2.5" stroke-linecap="round"/>
  </g>"""


def destination_pin(x, y):
    """A pulsing amber map pin marking the delivery destination."""
    return f"""
  <g transform="translate({x}, {y})">
    <circle r="34" fill="none" stroke="{C['amber']}" stroke-width="1.5" opacity="0.30"/>
    <circle r="22" fill="none" stroke="{C['amber']}" stroke-width="1.5" opacity="0.5"/>
    <circle r="20" fill="{C['amber_lt']}" opacity="0.25" filter="url(#glow-amber)"/>
    <g filter="url(#ds-tight)">
      <path d="M 0 -28 Q 16 -28 16 -12 Q 16 0 0 18 Q -16 0 -16 -12 Q -16 -28 0 -28 Z" fill="{C['amber']}" stroke="{C['amber_dk']}" stroke-width="1.5"/>
      <circle cx="0" cy="-14" r="5" fill="{C['white']}"/>
    </g>
  </g>"""


def route_dashed(start, end, curve_offset=(0, -60)):
    sx, sy = start
    ex, ey = end
    cx, cy = (sx + ex) / 2 + curve_offset[0], (sy + ey) / 2 + curve_offset[1]
    return f"""
  <path d="M {sx} {sy} Q {cx} {cy} {ex} {ey}"
        fill="none" stroke="{C['amber_lt']}" stroke-width="2.5"
        stroke-dasharray="8 8" stroke-linecap="round" opacity="0.8"/>"""


# ──────────────────────────────────────────────────────────────────
# SKYLINE BUILDERS — each neighborhood gets a characteristic silhouette
# ──────────────────────────────────────────────────────────────────

# Building helpers (drawn as silhouettes against the navy sky)
def building_two_flat(x, y, w=80, h=120, lit_windows=None):
    """Chicago 2-flat: brick rectangle, 2 floors of windows, modest cornice."""
    if lit_windows is None:
        lit_windows = [1, 3]  # which windows are lit (0-indexed)
    parts = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#skylineGrad)" stroke="#0A1730" stroke-width="1"/>']
    # cornice
    parts.append(f'<rect x="{x - 4}" y="{y}" width="{w + 8}" height="6" fill="#091226"/>')
    # 2 floors x 2 windows
    win_w, win_h = 14, 22
    for floor in range(2):
        for col in range(2):
            wx = x + 12 + col * (w - 24 - win_w)
            wy = y + 22 + floor * 44
            idx = floor * 2 + col
            color = C['warm_window'] if idx in lit_windows else "#1B2E5A"
            parts.append(f'<rect x="{wx}" y="{wy}" width="{win_w}" height="{win_h}" fill="{color}" opacity="{0.85 if idx in lit_windows else 1}"/>')
    return "\n  ".join(parts)


def building_three_flat(x, y, w=90, h=170, lit_windows=None):
    """Chicago 3-flat: 3 floors, often with bay windows."""
    if lit_windows is None:
        lit_windows = [0, 2, 5]
    parts = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#skylineGrad)" stroke="#0A1730" stroke-width="1"/>']
    parts.append(f'<rect x="{x - 4}" y="{y}" width="{w + 8}" height="6" fill="#091226"/>')
    # bay window protrusion in the middle
    parts.append(f'<rect x="{x + w/2 - 14}" y="{y + 8}" width="28" height="{h - 8}" fill="#152952" stroke="#0A1730" stroke-width="1"/>')
    win_w, win_h = 12, 22
    for floor in range(3):
        for col in range(3):
            if col == 1:
                wx = x + w/2 - 10
            elif col == 0:
                wx = x + 8
            else:
                wx = x + w - 8 - win_w
            wy = y + 18 + floor * 50
            idx = floor * 3 + col
            color = C['warm_window'] if idx in lit_windows else "#1B2E5A"
            parts.append(f'<rect x="{wx}" y="{wy}" width="{win_w}" height="{win_h}" fill="{color}" opacity="{0.85 if idx in lit_windows else 1}"/>')
    return "\n  ".join(parts)


def building_bungalow(x, y, w=100, h=70, lit_windows=None):
    """Chicago bungalow: low brick home with a pitched front gable."""
    if lit_windows is None:
        lit_windows = [0, 1]
    parts = []
    # house body
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#skylineGrad)" stroke="#0A1730" stroke-width="1"/>')
    # gable roof
    parts.append(f'<path d="M {x - 4} {y} L {x + w/2} {y - 28} L {x + w + 4} {y} Z" fill="#091226" stroke="#000" stroke-width="1"/>')
    # windows
    win_w, win_h = 16, 22
    for col in range(2):
        wx = x + 10 + col * (w - 20 - win_w)
        wy = y + 20
        idx = col
        color = C['warm_window'] if idx in lit_windows else "#1B2E5A"
        parts.append(f'<rect x="{wx}" y="{wy}" width="{win_w}" height="{win_h}" fill="{color}" opacity="{0.85 if idx in lit_windows else 1}"/>')
    # door
    parts.append(f'<rect x="{x + w/2 - 6}" y="{y + h - 28}" width="12" height="28" fill="#0A1730"/>')
    return "\n  ".join(parts)


def building_warehouse(x, y, w=180, h=140, lit_windows=None):
    """Industrial warehouse/loft conversion — wide, with grid of small windows."""
    if lit_windows is None:
        lit_windows = [2, 5, 7, 10]
    parts = []
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#skylineGrad)" stroke="#0A1730" stroke-width="1"/>')
    parts.append(f'<rect x="{x - 4}" y="{y}" width="{w + 8}" height="8" fill="#091226"/>')
    # grid of small windows (4 across, 3 down)
    win_w, win_h = 22, 28
    for row in range(3):
        for col in range(4):
            wx = x + 14 + col * 40
            wy = y + 14 + row * 40
            idx = row * 4 + col
            color = C['warm_window'] if idx in lit_windows else "#1B2E5A"
            parts.append(f'<rect x="{wx}" y="{wy}" width="{win_w}" height="{win_h}" fill="{color}" opacity="{0.8 if idx in lit_windows else 1}"/>')
            # window cross detail
            parts.append(f'<line x1="{wx + win_w/2}" y1="{wy}" x2="{wx + win_w/2}" y2="{wy + win_h}" stroke="#0A1730" stroke-width="0.8" opacity="0.7"/>')
    return "\n  ".join(parts)


def building_storefront(x, y, w=120, h=100, awning_color=None, lit=True):
    """Small commercial storefront with an awning."""
    awning_color = awning_color or C['amber']
    parts = []
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#skylineGrad)" stroke="#0A1730" stroke-width="1"/>')
    parts.append(f'<rect x="{x - 4}" y="{y}" width="{w + 8}" height="6" fill="#091226"/>')
    # awning
    parts.append(f'<path d="M {x - 6} {y + 30} L {x + w + 6} {y + 30} L {x + w - 6} {y + 46} L {x + 6} {y + 46} Z" fill="{awning_color}" opacity="0.85"/>')
    # storefront window (lit)
    win_color = C['warm_window'] if lit else "#1B2E5A"
    parts.append(f'<rect x="{x + 8}" y="{y + 52}" width="{w - 16}" height="{h - 60}" fill="{win_color}" opacity="0.85"/>')
    parts.append(f'<line x1="{x + w/2}" y1="{y + 52}" x2="{x + w/2}" y2="{y + h - 8}" stroke="#0A1730" stroke-width="1"/>')
    return "\n  ".join(parts)


def logan_square_monument(x, y):
    """The famous Logan Square Illinois Centennial Monument — tall column with eagle on top."""
    parts = []
    base_w, base_h = 50, 30
    # base
    parts.append(f'<rect x="{x - base_w/2}" y="{y + 220}" width="{base_w}" height="{base_h}" fill="#091226" stroke="#000" stroke-width="1"/>')
    parts.append(f'<rect x="{x - base_w/2 - 6}" y="{y + 218}" width="{base_w + 12}" height="6" fill="#091226"/>')
    # tall fluted column
    parts.append(f'<rect x="{x - 8}" y="{y + 40}" width="16" height="180" fill="#152952" stroke="#091226" stroke-width="1"/>')
    # column flutes
    for i in range(3):
        parts.append(f'<line x1="{x - 4 + i * 4}" y1="{y + 50}" x2="{x - 4 + i * 4}" y2="{y + 215}" stroke="#091226" stroke-width="0.8" opacity="0.7"/>')
    # capital (top of column)
    parts.append(f'<rect x="{x - 12}" y="{y + 32}" width="24" height="10" fill="#091226"/>')
    parts.append(f'<rect x="{x - 14}" y="{y + 28}" width="28" height="5" fill="#152952"/>')
    # eagle on top — stylized silhouette with spread wings
    parts.append(f'''<g transform="translate({x}, {y + 18})">
      <path d="M 0 0 L -3 -14 L 0 -16 L 3 -14 Z" fill="{C['amber']}" stroke="#091226" stroke-width="0.5"/>
      <path d="M 0 -2 Q -16 -10 -22 -4 Q -14 -2 -6 0 Z" fill="{C['amber']}" stroke="#091226" stroke-width="0.5"/>
      <path d="M 0 -2 Q 16 -10 22 -4 Q 14 -2 6 0 Z" fill="{C['amber']}" stroke="#091226" stroke-width="0.5"/>
    </g>''')
    return "\n  ".join(parts)


def tree(x, y, scale=1.0):
    """Simple boulevard tree silhouette."""
    s = scale
    return f"""
  <g transform="translate({x}, {y})">
    <rect x="{-3 * s}" y="{-10 * s}" width="{6 * s}" height="{30 * s}" fill="#091226"/>
    <circle cx="0" cy="{-32 * s}" r="{24 * s}" fill="#0E2042"/>
    <circle cx="{-14 * s}" cy="{-24 * s}" r="{16 * s}" fill="#0E2042"/>
    <circle cx="{14 * s}" cy="{-24 * s}" r="{16 * s}" fill="#0E2042"/>
    <circle cx="0" cy="{-44 * s}" r="{14 * s}" fill="#0E2042"/>
  </g>"""


# ──────────────────────────────────────────────────────────────────
# THE 6 NEIGHBORHOOD HEROES
# ──────────────────────────────────────────────────────────────────

def hero_avondale():
    """Avondale — home turf. Industrial/warehouse character + 2-flats."""
    inner = [neighborhood_plaque("Avondale", x=900, y=140)]
    # Skyline at y=420 to ~560
    inner.append(building_warehouse(880, 430, lit_windows=[2, 5, 7, 10]))   # left
    inner.append(building_two_flat(1080, 450, lit_windows=[0, 3]))
    inner.append(building_two_flat(1180, 440, lit_windows=[1, 2]))
    inner.append(building_three_flat(1280, 400, lit_windows=[1, 4, 6]))
    inner.append(building_two_flat(1390, 450, lit_windows=[0, 2, 3]))
    inner.append(building_warehouse(1490, 470, w=110, h=100, lit_windows=[3, 6]))
    # trees
    inner.append(tree(1060, 600, 0.6))
    inner.append(tree(1380, 600, 0.55))
    # delivery van
    inner.append(delivery_van(x=1090, y=660))
    # bag in front of van
    inner.append(laundry_bag_small(950, 660))
    # pin marking destination
    inner.append(destination_pin(1480, 660))
    # route from van to pin
    inner.append(route_dashed((1385, 670), (1480, 660), curve_offset=(0, -40)))
    # "HOME BASE" badge for Avondale
    inner.append(f'''
  <g transform="translate(1500, 360)">
    <circle r="40" fill="{C['amber']}"/>
    <circle r="34" fill="none" stroke="{C['brand_dark']}" stroke-width="1.5"/>
    <text x="0" y="-6" text-anchor="middle" font-family="sans-serif" font-size="9" font-weight="800" fill="{C['brand_dark']}" letter-spacing="2">OUR</text>
    <text x="0" y="10" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="800" fill="{C['brand_dark']}">HOME</text>
  </g>''')
    return svg_wrap("\n".join(inner),
                    "Spin It Up Laundry — Avondale Pickup &amp; Delivery",
                    "Avondale neighborhood scene with brick warehouses and two-flats, a Spin It Up delivery van, and a 'home base' badge")


def hero_logan_square():
    """Logan Square — features the iconic Illinois Centennial Monument."""
    inner = [neighborhood_plaque("Logan Square", x=900, y=140)]
    # The monument — the visual anchor for Logan Square
    inner.append(logan_square_monument(1130, 320))
    # boulevard trees flanking it
    inner.append(tree(1050, 600, 0.7))
    inner.append(tree(1220, 600, 0.65))
    inner.append(tree(900, 600, 0.6))
    # 3-flats and storefronts on the sides
    inner.append(building_three_flat(910, 410, w=80, h=160, lit_windows=[0, 4, 7]))
    inner.append(building_storefront(1290, 470, awning_color=C['coral']))
    inner.append(building_three_flat(1440, 400, w=85, h=170, lit_windows=[1, 3, 5, 8]))
    # delivery van
    inner.append(delivery_van(x=1100, y=660))
    inner.append(laundry_bag_small(960, 660))
    inner.append(destination_pin(1480, 660))
    inner.append(route_dashed((1395, 670), (1480, 660), curve_offset=(0, -40)))
    return svg_wrap("\n".join(inner),
                    "Spin It Up Laundry — Logan Square Pickup &amp; Delivery",
                    "Logan Square neighborhood with the Illinois Centennial Monument, three-flats, storefronts, and a delivery van")


def hero_irving_park():
    """Irving Park — residential bungalows + 2-flats, Metra hint."""
    inner = [neighborhood_plaque("Irving Park", x=900, y=140)]
    # Mix of bungalows and 2-flats — residential character
    inner.append(building_bungalow(890, 490, lit_windows=[0]))
    inner.append(building_two_flat(1010, 440, lit_windows=[1, 2, 3]))
    inner.append(building_bungalow(1110, 490, lit_windows=[0, 1]))
    inner.append(building_two_flat(1230, 440, lit_windows=[0, 2]))
    inner.append(building_bungalow(1340, 490, lit_windows=[1]))
    inner.append(building_two_flat(1460, 440, lit_windows=[0, 1, 3]))
    # Metra train tracks hint at the back (subtle elevated structure)
    inner.append(f'''
  <g opacity="0.5">
    <line x1="880" y1="395" x2="1600" y2="395" stroke="{C['chrome_low']}" stroke-width="4"/>
    <line x1="880" y1="408" x2="1600" y2="408" stroke="{C['chrome_low']}" stroke-width="2"/>
    <g fill="{C['chrome_low']}">
      <rect x="920" y="408" width="6" height="30"/>
      <rect x="1080" y="408" width="6" height="50"/>
      <rect x="1240" y="408" width="6" height="40"/>
      <rect x="1400" y="408" width="6" height="50"/>
      <rect x="1560" y="408" width="6" height="40"/>
    </g>
  </g>''')
    # boulevard trees
    inner.append(tree(990, 600, 0.55))
    inner.append(tree(1310, 600, 0.5))
    # delivery van
    inner.append(delivery_van(x=1100, y=660))
    inner.append(laundry_bag_small(960, 660))
    inner.append(destination_pin(1480, 660))
    inner.append(route_dashed((1395, 670), (1480, 660), curve_offset=(0, -40)))
    return svg_wrap("\n".join(inner),
                    "Spin It Up Laundry — Irving Park Pickup &amp; Delivery",
                    "Irving Park neighborhood with Chicago bungalows, two-flats, Metra train tracks, and a delivery van")


def hero_roscoe_village():
    """Roscoe Village — charming small storefronts and family homes."""
    inner = [neighborhood_plaque("Roscoe Village", x=900, y=140)]
    # Storefronts dominate (it's a charming commercial street feel)
    inner.append(building_storefront(890, 470, w=110, h=100, awning_color=C['mint']))
    inner.append(building_storefront(1010, 480, w=100, h=90, awning_color=C['coral']))
    inner.append(building_two_flat(1120, 440, lit_windows=[0, 2, 3]))
    inner.append(building_storefront(1220, 480, w=110, h=90, awning_color=C['amber']))
    inner.append(building_storefront(1340, 470, w=100, h=100, awning_color=C['lilac']))
    inner.append(building_two_flat(1450, 440, w=80, h=140, lit_windows=[1, 3]))
    # Lots of trees (Roscoe Village is leafy)
    inner.append(tree(870, 600, 0.55))
    inner.append(tree(990, 605, 0.5))
    inner.append(tree(1190, 605, 0.6))
    inner.append(tree(1310, 600, 0.5))
    inner.append(tree(1430, 605, 0.55))
    # delivery van
    inner.append(delivery_van(x=1100, y=660))
    inner.append(laundry_bag_small(960, 660))
    inner.append(destination_pin(1480, 660))
    inner.append(route_dashed((1395, 670), (1480, 660), curve_offset=(0, -40)))
    return svg_wrap("\n".join(inner),
                    "Spin It Up Laundry — Roscoe Village Pickup &amp; Delivery",
                    "Roscoe Village neighborhood with colorful storefront awnings, leafy trees, and a delivery van")


def hero_albany_park():
    """Albany Park — denser, diverse, Lawrence Ave commercial character."""
    inner = [neighborhood_plaque("Albany Park", x=900, y=140)]
    # Dense mix — taller 3-flats and many storefronts
    inner.append(building_three_flat(880, 400, w=85, h=170, lit_windows=[0, 2, 4, 6, 8]))
    inner.append(building_storefront(985, 480, w=110, h=90, awning_color=C['coral']))
    inner.append(building_three_flat(1110, 400, w=90, h=170, lit_windows=[1, 3, 5, 7]))
    inner.append(building_storefront(1220, 480, w=100, h=90, awning_color=C['amber']))
    inner.append(building_three_flat(1340, 410, w=80, h=160, lit_windows=[0, 4, 6, 8]))
    inner.append(building_storefront(1440, 480, w=110, h=90, awning_color=C['mint']))
    # streetlights (it's Lawrence Ave — busy)
    inner.append(f'''
  <g stroke="{C['chrome_low']}" fill="{C['chrome_low']}" opacity="0.6">
    <line x1="1060" y1="580" x2="1060" y2="640" stroke-width="2"/>
    <circle cx="1060" cy="578" r="5" fill="{C['amber_lt']}"/>
    <line x1="1290" y1="580" x2="1290" y2="640" stroke-width="2"/>
    <circle cx="1290" cy="578" r="5" fill="{C['amber_lt']}"/>
  </g>''')
    # delivery van
    inner.append(delivery_van(x=1100, y=660))
    inner.append(laundry_bag_small(960, 660))
    inner.append(destination_pin(1480, 660))
    inner.append(route_dashed((1395, 670), (1480, 660), curve_offset=(0, -40)))
    return svg_wrap("\n".join(inner),
                    "Spin It Up Laundry — Albany Park Pickup &amp; Delivery",
                    "Albany Park neighborhood with three-flats and street-level shops along a busy commercial avenue")


def hero_bucktown():
    """Bucktown — three-flats with bay windows, brownstones, leafy."""
    inner = [neighborhood_plaque("Bucktown", x=900, y=140)]
    # Almost all 3-flats — bucktown is famous for them
    inner.append(building_three_flat(880, 420, w=90, h=160, lit_windows=[0, 3, 5, 7]))
    inner.append(building_three_flat(990, 400, w=90, h=180, lit_windows=[1, 2, 4, 8]))
    inner.append(building_three_flat(1110, 410, w=95, h=170, lit_windows=[0, 4, 6]))
    inner.append(building_three_flat(1230, 400, w=90, h=180, lit_windows=[3, 5, 7]))
    inner.append(building_three_flat(1350, 420, w=85, h=160, lit_windows=[1, 4, 8]))
    inner.append(building_three_flat(1465, 400, w=95, h=180, lit_windows=[0, 2, 5, 7]))
    # Lots of trees (bucktown is leafy)
    inner.append(tree(870, 600, 0.6))
    inner.append(tree(1050, 605, 0.55))
    inner.append(tree(1200, 600, 0.65))
    inner.append(tree(1340, 605, 0.55))
    inner.append(tree(1480, 600, 0.6))
    # delivery van
    inner.append(delivery_van(x=1100, y=660))
    inner.append(laundry_bag_small(960, 660))
    inner.append(destination_pin(1480, 660))
    inner.append(route_dashed((1395, 670), (1480, 660), curve_offset=(0, -40)))
    return svg_wrap("\n".join(inner),
                    "Spin It Up Laundry — Bucktown Pickup &amp; Delivery",
                    "Bucktown neighborhood featuring rows of classic Chicago three-flats with bay windows and leafy boulevards")


# ──────────────────────────────────────────────────────────────────
# Render
# ──────────────────────────────────────────────────────────────────
files = {
    "hero-area-avondale.svg":       hero_avondale(),
    "hero-area-logan-square.svg":   hero_logan_square(),
    "hero-area-irving-park.svg":    hero_irving_park(),
    "hero-area-roscoe-village.svg": hero_roscoe_village(),
    "hero-area-albany-park.svg":    hero_albany_park(),
    "hero-area-bucktown.svg":       hero_bucktown(),
}
for name, content in files.items():
    p = os.path.join(OUT_DIR, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ {name}  ({os.path.getsize(p):,} bytes)")
print(f"\n→ {OUT_DIR}")
