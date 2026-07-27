"""
Spin It Up Laundry — Service Page Hero Images (v2)
==================================================
5 SVG heroes, one per service page.

CHANGES FROM v1:
- Full canvas background (deep navy with warm upper-right light) so text
  doesn't float on a blank white area.
- Multi-stop gradients on every surface — chrome, glass, fabric.
- Drop shadows, floor reflections, perspective hints.
- Muted, naturalistic colors instead of flat candy palette.

LAYOUT:
- viewBox 1600 x 900 (16:9)
- Left ~45% (x 0–720): background color only — text overlay zone.
- Right ~55% (x 720–1600): illustration.
"""

import os, textwrap

OUT_DIR = "/home/claude/output_v2"
os.makedirs(OUT_DIR, exist_ok=True)

# ──────────────────────────────────────────────────────────────────
# Palette — muted & dimensional, not candy-flat
# ──────────────────────────────────────────────────────────────────
C = {
    # Background atmosphere
    "bg_top":      "#0A1A3D",
    "bg_bot":      "#142A55",
    "bg_glow":     "#3A6FB0",
    "bg_warm":     "#D89A55",

    # Chrome / steel
    "chrome_hi":   "#F4F7FA",
    "chrome_mid":  "#A8B5C5",
    "chrome_low":  "#3D4A5C",
    "chrome_dark": "#1B2330",

    # Glass / door
    "glass_hi":    "#EAF3FF",
    "glass_mid":   "#7BA4D6",
    "glass_low":   "#1E3458",

    # Brand accents (muted)
    "brand_dark":  "#0B2447",
    "brand":       "#19376D",
    "brand_lt":    "#576CBC",
    "amber":       "#E6A23C",
    "amber_dk":    "#B07820",
    "amber_lt":    "#F4C77F",

    # Fabric / linens
    "linen_hi":    "#F8F4EC",
    "linen_mid":   "#E4DDC9",
    "linen_low":   "#A89B7A",
    "shirt_blue":  "#A8C5E4",
    "shirt_dk":    "#5478A0",
    "shirt_pink":  "#C97B7B",
    "shirt_sage":  "#8DA88B",
    "shirt_olive": "#A89853",

    # Wicker
    "wick_hi":     "#DBB07A",
    "wick_mid":    "#9F7541",
    "wick_low":    "#5D4220",

    # UI
    "ink":         "#0A1A3D",
    "white":       "#FFFFFF",
    "off_white":   "#F0F4F8",
    "gray_lt":     "#CFD6E0",
    "gray_md":     "#7C8699",
    "gray_dk":     "#3A4456",
    "mint":        "#5FB07A",
    "coral":       "#C46A5C",
    "lilac":       "#876FB0",
}


# ──────────────────────────────────────────────────────────────────
# Shared defs — gradients, filters, light source
# ──────────────────────────────────────────────────────────────────
SHARED_DEFS = f"""
<defs>
  <!-- Full background gradient: deep navy with a warm light glow -->
  <linearGradient id="bgBase" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"  stop-color="{C['bg_top']}"/>
    <stop offset="100%" stop-color="{C['bg_bot']}"/>
  </linearGradient>
  <radialGradient id="bgGlow" cx="78%" cy="18%" r="65%">
    <stop offset="0%"  stop-color="{C['bg_warm']}" stop-opacity="0.35"/>
    <stop offset="35%" stop-color="{C['bg_glow']}" stop-opacity="0.20"/>
    <stop offset="100%" stop-color="{C['bg_top']}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="bgVignette" cx="50%" cy="50%" r="80%">
    <stop offset="60%" stop-color="#000" stop-opacity="0"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.35"/>
  </radialGradient>

  <!-- Floor gradient at bottom -->
  <linearGradient id="floorGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"  stop-color="{C['bg_bot']}" stop-opacity="0"/>
    <stop offset="60%" stop-color="#091532" stop-opacity="0.55"/>
    <stop offset="100%" stop-color="#040A1F" stop-opacity="0.85"/>
  </linearGradient>

  <!-- Chrome / brushed steel -->
  <linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"  stop-color="{C['chrome_hi']}"/>
    <stop offset="18%" stop-color="#D7DEE8"/>
    <stop offset="48%" stop-color="{C['chrome_mid']}"/>
    <stop offset="78%" stop-color="#6E7C92"/>
    <stop offset="100%" stop-color="{C['chrome_low']}"/>
  </linearGradient>
  <linearGradient id="chromeSide" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"  stop-color="{C['chrome_low']}"/>
    <stop offset="30%" stop-color="#7888A0"/>
    <stop offset="70%" stop-color="{C['chrome_mid']}"/>
    <stop offset="100%" stop-color="{C['chrome_hi']}"/>
  </linearGradient>
  <linearGradient id="panelDark" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"  stop-color="#202B3E"/>
    <stop offset="100%" stop-color="{C['chrome_dark']}"/>
  </linearGradient>

  <!-- Glass / washer door -->
  <radialGradient id="glassDoor" cx="35%" cy="28%" r="75%">
    <stop offset="0%"  stop-color="{C['glass_hi']}" stop-opacity="0.95"/>
    <stop offset="22%" stop-color="#C7DBF2" stop-opacity="0.85"/>
    <stop offset="55%" stop-color="{C['glass_mid']}" stop-opacity="0.75"/>
    <stop offset="100%" stop-color="{C['glass_low']}" stop-opacity="0.95"/>
  </radialGradient>
  <linearGradient id="doorRing" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"  stop-color="#C5CCD8"/>
    <stop offset="50%" stop-color="#7A8497"/>
    <stop offset="100%" stop-color="{C['chrome_dark']}"/>
  </linearGradient>

  <!-- LCD display -->
  <linearGradient id="lcdGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"  stop-color="#0E1A2F"/>
    <stop offset="100%" stop-color="#1E3458"/>
  </linearGradient>

  <!-- Linen / white fabric -->
  <linearGradient id="linenGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"  stop-color="{C['linen_hi']}"/>
    <stop offset="100%" stop-color="{C['linen_mid']}"/>
  </linearGradient>

  <!-- Wicker basket -->
  <linearGradient id="wickerLight" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"  stop-color="{C['wick_hi']}"/>
    <stop offset="100%" stop-color="{C['wick_mid']}"/>
  </linearGradient>
  <radialGradient id="wickerBowl" cx="50%" cy="30%" r="70%">
    <stop offset="0%"  stop-color="{C['wick_hi']}"/>
    <stop offset="60%" stop-color="{C['wick_mid']}"/>
    <stop offset="100%" stop-color="{C['wick_low']}"/>
  </radialGradient>

  <!-- Drop shadows -->
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
  <filter id="glow-warm" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="6"/>
  </filter>
  <filter id="steam-blur" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="1.2"/>
  </filter>
</defs>"""


def background_layer() -> str:
    """Common full-canvas background applied to every service hero."""
    return f"""
  <!-- Full background -->
  <rect width="1600" height="900" fill="url(#bgBase)"/>
  <rect width="1600" height="900" fill="url(#bgGlow)"/>

  <!-- Subtle horizontal light streaks (very faint) -->
  <g opacity="0.06" stroke="{C['bg_warm']}" stroke-width="1" fill="none">
    <line x1="0" y1="160" x2="1600" y2="160"/>
    <line x1="0" y1="320" x2="1600" y2="320"/>
    <line x1="0" y1="480" x2="1600" y2="480"/>
    <line x1="0" y1="640" x2="1600" y2="640"/>
  </g>

  <!-- Floor wash at bottom for grounding -->
  <rect x="0" y="540" width="1600" height="360" fill="url(#floorGrad)"/>

  <!-- Vignette to focus the eye on the right -->
  <rect width="1600" height="900" fill="url(#bgVignette)"/>"""


def svg_wrap(inner: str, title: str, desc: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="t d">
  <title id="t">{title}</title>
  <desc id="d">{desc}</desc>
  {SHARED_DEFS}
  {background_layer()}
  {inner}
</svg>'''


# ──────────────────────────────────────────────────────────────────
# 1. SELF-SERVICE LAUNDRY  — three washers, slight 3/4 perspective,
#    glass-door realism, floor reflection, fluorescent halo overhead.
# ──────────────────────────────────────────────────────────────────
def self_service() -> str:
    # Ceiling fluorescent light bar — top right of the scene
    ceiling = f"""
  <g opacity="0.85">
    <rect x="870" y="60" width="640" height="22" rx="4" fill="#1E3458"/>
    <rect x="878" y="66" width="624" height="10" rx="3" fill="#F8FAFF" opacity="0.9"/>
    <ellipse cx="1190" cy="110" rx="430" ry="80" fill="#F8FAFF" opacity="0.10"/>
    <ellipse cx="1190" cy="125" rx="320" ry="50" fill="#F8FAFF" opacity="0.07"/>
  </g>"""

    # Helper to build ONE washing machine at given x (front-facing with side hint)
    def washer(x, time_str="28:00", door_state="clothes", color_palette=None):
        W, H = 280, 560     # machine footprint
        # The slight 3/4: a thin "side" panel on the right of each washer
        side_w = 18
        parts = []

        # Floor shadow under machine
        parts.append(f'<ellipse cx="{x + W/2}" cy="{780}" rx="{W/2 + 30}" ry="22" fill="#000" opacity="0.55" filter="url(#glow-warm)"/>')

        # Right side panel (perspective hint)
        parts.append(f'<path d="M {x+W} 240 L {x+W+side_w} 252 L {x+W+side_w} 772 L {x+W} 760 Z" fill="url(#chromeSide)"/>')

        # Front panel (the main face)
        parts.append(f'<rect x="{x}" y="240" width="{W}" height="520" rx="14" fill="url(#chrome)" stroke="#5C6E85" stroke-width="1.5"/>')

        # Top control deck — dark panel
        parts.append(f'<rect x="{x+10}" y="252" width="{W-20}" height="78" rx="8" fill="url(#panelDark)"/>')

        # LCD display
        lcd_x, lcd_y = x + 24, 268
        parts.append(f'<rect x="{lcd_x}" y="{lcd_y}" width="96" height="46" rx="4" fill="url(#lcdGrad)" stroke="#000" stroke-width="1"/>')
        parts.append(f'<text x="{lcd_x+48}" y="{lcd_y+33}" text-anchor="middle" font-family="monospace" font-size="22" font-weight="800" fill="{C["amber_lt"]}" opacity="0.92">{time_str}</text>')
        # Display reflection
        parts.append(f'<rect x="{lcd_x+2}" y="{lcd_y+2}" width="92" height="14" rx="3" fill="#FFFFFF" opacity="0.10"/>')

        # Knob — central with realistic shading
        kx, ky = x + W - 70, lcd_y + 22
        parts.append(f'<circle cx="{kx}" cy="{ky}" r="22" fill="#1B2330"/>')
        parts.append(f'<circle cx="{kx}" cy="{ky}" r="19" fill="url(#chrome)"/>')
        parts.append(f'<circle cx="{kx}" cy="{ky-1}" r="14" fill="#3D4A5C"/>')
        parts.append(f'<rect x="{kx-1.5}" y="{ky-13}" width="3" height="10" rx="1" fill="{C["amber"]}"/>')
        parts.append(f'<circle cx="{kx-6}" cy="{ky-6}" r="4" fill="#FFFFFF" opacity="0.4"/>')

        # Buttons row (small LED dots)
        for i, color in enumerate(["#5FB07A", C["amber"], "#C46A5C"]):
            cx_b = lcd_x + 110 + i * 18
            parts.append(f'<circle cx="{cx_b}" cy="{lcd_y+8}" r="3" fill="{color}"/>')
            parts.append(f'<circle cx="{cx_b}" cy="{lcd_y+8}" r="6" fill="{color}" opacity="0.25"/>')

        # Brand strip
        parts.append(f'<rect x="{x+10}" y="338" width="{W-20}" height="4" fill="{C["amber"]}"/>')
        parts.append(f'<text x="{x + W/2}" y="356" text-anchor="middle" font-family="Georgia, serif" font-size="9" font-weight="700" fill="{C["gray_dk"]}" letter-spacing="3">SPIN IT UP</text>')

        # Door bezel — concentric rings
        cxd, cyd = x + W/2, 540
        parts.append(f'<circle cx="{cxd}" cy="{cyd}" r="138" fill="#7A8497"/>')
        parts.append(f'<circle cx="{cxd}" cy="{cyd}" r="132" fill="url(#doorRing)"/>')
        parts.append(f'<circle cx="{cxd}" cy="{cyd}" r="118" fill="#1B2330"/>')

        # Glass door with realistic radial shading
        parts.append(f'<circle cx="{cxd}" cy="{cyd}" r="112" fill="url(#glassDoor)"/>')

        # Inside the drum — clothes / motion blur
        if door_state == "spinning":
            # Motion-blurred colorful streak using arcs
            parts.append(f'''
        <g transform="translate({cxd},{cyd})">
          <ellipse rx="100" ry="65" fill="{C["coral"]}" opacity="0.55"/>
          <ellipse rx="90" ry="55" transform="rotate(30)" fill="{C["amber"]}" opacity="0.45"/>
          <ellipse rx="92" ry="60" transform="rotate(-25)" fill="{C["mint"]}" opacity="0.35"/>
          <!-- swirl motion lines -->
          <path d="M -85 -25 A 90 90 0 0 1 -15 -95" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.55"/>
          <path d="M 80 -10 A 90 90 0 0 1 60 75" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.55"/>
          <path d="M -50 80 A 95 95 0 0 1 -90 20" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" opacity="0.4"/>
        </g>''')
        else:
            cp = color_palette or [C["shirt_blue"], C["shirt_pink"], C["shirt_sage"]]
            parts.append(f'''
        <g transform="translate({cxd},{cyd})">
          <ellipse cx="-32" cy="22" rx="58" ry="40" fill="{cp[0]}" opacity="0.85"/>
          <ellipse cx="35" cy="-12" rx="52" ry="38" fill="{cp[1]}" opacity="0.85"/>
          <ellipse cx="20" cy="40" rx="46" ry="28" fill="{cp[2]}" opacity="0.75"/>
          <!-- fold lines hint -->
          <line x1="-70" y1="20" x2="0" y2="22" stroke="#FFFFFF" stroke-width="1" opacity="0.3"/>
          <line x1="-5" y1="-15" x2="60" y2="-10" stroke="#FFFFFF" stroke-width="1" opacity="0.3"/>
        </g>''')

        # Glass highlight (top-left of door)
        parts.append(f'<ellipse cx="{cxd-50}" cy="{cyd-55}" rx="42" ry="20" fill="#FFFFFF" opacity="0.45"/>')
        parts.append(f'<ellipse cx="{cxd-35}" cy="{cyd-50}" rx="14" ry="6" fill="#FFFFFF" opacity="0.65"/>')

        # Hinge dot + handle on the right
        parts.append(f'<circle cx="{cxd+128}" cy="{cyd}" r="5" fill="#3D4A5C"/>')
        parts.append(f'<rect x="{cxd+125}" y="{cyd-12}" width="14" height="24" rx="3" fill="url(#chromeSide)"/>')

        # Coin/card reader strip
        parts.append(f'<rect x="{x+30}" y="690" width="{W-60}" height="42" rx="6" fill="#1E2A40" stroke="#3D4A5C" stroke-width="1"/>')
        parts.append(f'<rect x="{x+44}" y="702" width="56" height="18" rx="2" fill="{C["chrome_dark"]}"/>')
        parts.append(f'<text x="{x+72}" y="716" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="{C["amber_lt"]}">CARD</text>')
        parts.append(f'<rect x="{x+110}" y="702" width="56" height="18" rx="2" fill="{C["brand_lt"]}"/>')
        parts.append(f'<text x="{x+138}" y="716" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="{C["white"]}">EBT</text>')
        parts.append(f'<circle cx="{x+W-50}" cy="711" r="4" fill="{C["mint"]}"/>')

        # Base / kick plate
        parts.append(f'<rect x="{x-4}" y="755" width="{W+8+side_w}" height="20" rx="3" fill="{C["chrome_dark"]}"/>')

        return "\n  ".join(parts)

    # Tile floor receding to a slight right vanishing point
    tiles = ['<g opacity="0.18" stroke="#3A6FB0" stroke-width="1" fill="none">']
    # horizontal tile lines (perspective lines converging slightly to the right)
    for i, y in enumerate([790, 810, 832, 856, 882]):
        tiles.append(f'<line x1="640" y1="{y}" x2="1600" y2="{y}"/>')
    # vertical lines
    for x_t in [700, 820, 940, 1060, 1180, 1300, 1420, 1540]:
        tiles.append(f'<line x1="{x_t}" y1="785" x2="{x_t}" y2="900"/>')
    tiles.append('</g>')

    machines = "\n  ".join([
        washer(740, "28:00", "clothes", [C["shirt_olive"], C["shirt_pink"], C["shirt_sage"]]),
        washer(1020, "14:32", "spinning"),
        washer(1300, "42:15", "clothes", [C["shirt_blue"], C["shirt_olive"], C["shirt_pink"]]),
    ])

    # Soft bubbles drifting up — small, atmospheric
    bubbles = ""
    for cx, cy, r, op in [(1180, 200, 8, 0.4), (1230, 165, 5, 0.35),
                          (1100, 145, 6, 0.3), (1280, 195, 4, 0.3),
                          (1050, 190, 5, 0.35)]:
        bubbles += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{C["glass_hi"]}" opacity="{op}"/>\n  '

    # Floor reflection under the machines — soft elongated highlight
    reflection = f"""
  <g opacity="0.18">
    <ellipse cx="1180" cy="800" rx="450" ry="14" fill="{C['bg_warm']}"/>
    <ellipse cx="1180" cy="810" rx="380" ry="8" fill="{C['bg_warm']}"/>
  </g>"""

    return svg_wrap(
        ceiling + "\n  " + "\n  ".join(tiles) + reflection + "\n  " + machines + "\n  " + bubbles,
        "Self-Service Laundry at Spin It Up",
        "Three modern washing machines in a brightly lit Avondale laundromat"
    )


# ──────────────────────────────────────────────────────────────────
# 2. WASH & FOLD  — service counter scene: stacked folded laundry,
#    wicker basket on a wooden counter, soft lamp glow.
# ──────────────────────────────────────────────────────────────────
def wash_and_fold() -> str:
    inner = []

    # Counter surface (wood gradient — but tinted to match brand background)
    inner.append(f"""
  <defs>
    <linearGradient id="counterGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"  stop-color="#3B5278"/>
      <stop offset="50%" stop-color="#23365C"/>
      <stop offset="100%" stop-color="#0F1E40"/>
    </linearGradient>
    <radialGradient id="counterLight" cx="65%" cy="20%" r="55%">
      <stop offset="0%"  stop-color="{C['bg_warm']}" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="{C['bg_warm']}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- Counter top (front portion) -->
  <path d="M 0 680 L 1600 680 L 1600 900 L 0 900 Z" fill="url(#counterGrad)"/>
  <rect x="0" y="680" width="1600" height="4" fill="#5A7BAA" opacity="0.8"/>
  <rect width="1600" height="900" fill="url(#counterLight)"/>
""")

    # Stack of folded items — realistic with shadow + fold details, sitting on the counter
    stack_cx = 1090
    stack_base_y = 680  # counter top
    # Each fold is a 3D-ish slab with top face, front face, and shadow
    fold_specs = [
        # (offset_x, h_total, depth, top_color, front_color, edge_color, has_label)
        ( -8, 60, 24, C["shirt_blue"],   "#6A8FB8",  "#3D5B82",  False),
        (  6, 58, 22, C["linen_hi"],     "#C9C1AB",  "#7C7458",  True),   # white with label
        ( -4, 60, 24, C["shirt_sage"],   "#6D8E6C",  "#3F5C3F",  False),
        (  8, 56, 22, C["shirt_pink"],   "#A0584C",  "#6B3328",  False),
        ( -2, 58, 22, C["shirt_olive"],  "#8A7E40",  "#574E28",  False),
        (  4, 54, 20, C["shirt_blue"],   "#6A8FB8",  "#3D5B82",  False),
        ( -6, 50, 18, C["linen_hi"],     "#C9C1AB",  "#7C7458",  False),
    ]
    # Build from bottom up — each fold sits on top of the previous
    y = stack_base_y
    stack_svg = ['<g filter="url(#ds-soft)">']
    for dx, h, depth, top, front, edge, has_label in reversed(fold_specs):
        w = 360 - abs(dx) * 2
        x = stack_cx - w/2 + dx
        y -= h
        # front face
        stack_svg.append(f'<rect x="{x}" y="{y+depth/2}" width="{w}" height="{h-depth/2}" rx="3" fill="{front}"/>')
        # top face (parallelogram for a slight 3D tilt)
        stack_svg.append(
            f'<path d="M {x} {y+depth/2} '
            f'L {x+8} {y} '
            f'L {x+w+8} {y} '
            f'L {x+w} {y+depth/2} Z" '
            f'fill="{top}"/>'
        )
        # right side face
        stack_svg.append(
            f'<path d="M {x+w} {y+depth/2} '
            f'L {x+w+8} {y} '
            f'L {x+w+8} {y+h-depth/2-2} '
            f'L {x+w} {y+h-2} Z" '
            f'fill="{edge}"/>'
        )
        # fold crease lines
        stack_svg.append(f'<line x1="{x+12}" y1="{y+h/2+5}" x2="{x+w-8}" y2="{y+h/2+5}" stroke="{edge}" stroke-width="1" opacity="0.5"/>')
        stack_svg.append(f'<line x1="{x+w-26}" y1="{y+depth/2+4}" x2="{x+w-26}" y2="{y+h-6}" stroke="{edge}" stroke-width="1" opacity="0.4"/>')
        # subtle highlight on top edge
        stack_svg.append(f'<line x1="{x+8}" y1="{y}" x2="{x+w+8}" y2="{y}" stroke="#FFFFFF" stroke-width="1" opacity="0.45"/>')
        # Service label on the white fold
        if has_label:
            label_x, label_y = x + w - 90, y + 14
            stack_svg.append(f'''
    <g transform="translate({label_x}, {label_y})">
      <rect width="76" height="24" rx="3" fill="{C["amber"]}" opacity="0.95"/>
      <text x="38" y="16" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="10" fill="{C["brand_dark"]}" letter-spacing="1.5">FRESH</text>
    </g>''')
    stack_svg.append('</g>')
    inner.extend(stack_svg)

    # Wicker basket — to the left of the stack, on the counter
    # Realistic with curved shading + detailed weave
    inner.append(f'''
  <g transform="translate(830, 580)" filter="url(#ds-soft)">
    <!-- back rim (drawn first, behind body) -->
    <ellipse cx="0" cy="0" rx="180" ry="34" fill="{C['wick_mid']}"/>
    <ellipse cx="0" cy="-3" rx="172" ry="28" fill="{C['wick_low']}"/>
    <!-- body -->
    <path d="M -180 0 Q -180 130 0 145 Q 180 130 180 0 Z" fill="url(#wickerBowl)"/>
    <!-- weave hatching, clipped to body -->
    <clipPath id="basketClip"><path d="M -180 0 Q -180 130 0 145 Q 180 130 180 0 Z"/></clipPath>
    <g clip-path="url(#basketClip)" stroke="{C['wick_low']}" stroke-width="1.4" opacity="0.55">
      <!-- vertical strands -->
      <path d="M -170 0 Q -170 100 -170 140" fill="none"/>
      <path d="M -140 0 Q -140 105 -140 140" fill="none"/>
      <path d="M -100 0 Q -100 115 -100 145" fill="none"/>
      <path d="M -60 0 Q -60 120 -60 148" fill="none"/>
      <path d="M -20 0 Q -20 125 -20 150" fill="none"/>
      <path d="M 20 0 Q 20 125 20 150" fill="none"/>
      <path d="M 60 0 Q 60 120 60 148" fill="none"/>
      <path d="M 100 0 Q 100 115 100 145" fill="none"/>
      <path d="M 140 0 Q 140 105 140 140" fill="none"/>
      <path d="M 170 0 Q 170 100 170 140" fill="none"/>
      <!-- horizontal weave rows (curved) -->
      <path d="M -180 18 Q 0 30 180 18" fill="none"/>
      <path d="M -180 44 Q 0 56 180 44" fill="none"/>
      <path d="M -180 70 Q 0 82 180 70" fill="none"/>
      <path d="M -180 96 Q 0 110 180 96" fill="none"/>
      <path d="M -178 120 Q 0 132 178 120" fill="none"/>
    </g>
    <!-- dark inner shadow at the very top to give "opening" depth -->
    <ellipse cx="0" cy="0" rx="170" ry="28" fill="none" stroke="{C['wick_low']}" stroke-width="3" opacity="0.55"/>
    <!-- front rim (drawn last to overlap the body top) -->
    <ellipse cx="0" cy="0" rx="180" ry="34" fill="none" stroke="{C['wick_low']}" stroke-width="2.5"/>
    <ellipse cx="0" cy="-2" rx="180" ry="32" fill="none" stroke="{C['wick_hi']}" stroke-width="2" opacity="0.5"/>
    <!-- handles -->
    <path d="M -175 -5 q -22 -2 -22 -22 q 0 -16 16 -16" fill="none" stroke="{C['wick_low']}" stroke-width="4.5" stroke-linecap="round"/>
    <path d="M 175 -5 q 22 -2 22 -22 q 0 -16 -16 -16" fill="none" stroke="{C['wick_low']}" stroke-width="4.5" stroke-linecap="round"/>
    <!-- a hint of a folded towel poking out of the top of the basket -->
    <rect x="-50" y="-14" width="100" height="20" rx="3" fill="{C['linen_hi']}"/>
    <rect x="-50" y="-14" width="100" height="2" fill="#FFFFFF" opacity="0.5"/>
    <line x1="-30" y1="-2" x2="30" y2="-2" stroke="{C['linen_low']}" stroke-width="1" opacity="0.4"/>
  </g>''')

    # Lavender sprig leaning out of the basket
    inner.append(f'''
  <g transform="translate(870, 570) rotate(-22)">
    <line x1="0" y1="0" x2="0" y2="-140" stroke="#4A6B4F" stroke-width="2.5" stroke-linecap="round"/>
    <g fill="{C['lilac']}">
      <ellipse cx="-4" cy="-118" rx="4" ry="9"/>
      <ellipse cx="4"  cy="-128" rx="4" ry="9"/>
      <ellipse cx="-4" cy="-138" rx="4" ry="9"/>
      <ellipse cx="4"  cy="-146" rx="4" ry="8"/>
      <ellipse cx="-3" cy="-154" rx="3" ry="7"/>
    </g>
    <!-- small leaves -->
    <ellipse cx="-8" cy="-80" rx="4" ry="10" fill="#5C7F62" transform="rotate(-30, -8, -80)"/>
    <ellipse cx="8" cy="-60" rx="4" ry="10" fill="#5C7F62" transform="rotate(30, 8, -60)"/>
  </g>''')

    # Small soft sparkle dots indicating "fresh"
    inner.append(f'''
  <g fill="{C['amber_lt']}" opacity="0.7">
    <circle cx="930" cy="240" r="2.5"/>
    <circle cx="1480" cy="320" r="2"/>
    <circle cx="820" cy="430" r="2"/>
    <circle cx="1520" cy="500" r="2.5"/>
  </g>''')

    # Hanging price tag from the top of the stack
    inner.append(f'''
  <g transform="translate(1280, 200)">
    <line x1="0" y1="0" x2="0" y2="100" stroke="{C['gray_lt']}" stroke-width="1.5" opacity="0.85"/>
    <g transform="translate(0, 100)" filter="url(#ds-tight)">
      <path d="M -64 0 L 52 0 L 74 26 L 52 52 L -64 52 L -64 0 Z" fill="{C['linen_hi']}"/>
      <path d="M -64 0 L 52 0 L 74 26 L 52 52 L -64 52 L -64 0 Z" fill="none" stroke="{C['gray_dk']}" stroke-width="1.5"/>
      <circle cx="-54" cy="26" r="4" fill="{C['gray_dk']}"/>
      <circle cx="-54" cy="26" r="2" fill="{C['linen_hi']}"/>
      <text x="4" y="22" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="700" fill="{C['gray_dk']}" letter-spacing="2">FROM</text>
      <text x="4" y="42" text-anchor="middle" font-family="Georgia, serif" font-size="17" font-weight="800" fill="{C['brand']}">$1.50/lb</text>
    </g>
  </g>''')

    return svg_wrap("\n".join(inner),
                    "Wash and Fold Service",
                    "Stack of folded laundry beside a wicker basket on a counter, with lavender and price tag")


# ──────────────────────────────────────────────────────────────────
# 3. PICKUP & DELIVERY  — phone with detailed app UI, laundry bag on
#    a doorstep with a delivery van silhouette behind, dashed route.
# ──────────────────────────────────────────────────────────────────
def pickup_delivery() -> str:
    inner = []

    # City silhouette in the background (very subtle, far)
    inner.append(f'''
  <g opacity="0.20" fill="{C['brand_dark']}">
    <path d="M 700 620 L 700 540 L 740 540 L 740 520 L 780 520 L 780 540 L 820 540
             L 820 500 L 860 500 L 860 540 L 920 540 L 920 510 L 970 510 L 970 540
             L 1010 540 L 1010 480 L 1060 480 L 1060 540 L 1110 540 L 1110 520
             L 1160 520 L 1160 540 L 1220 540 L 1220 500 L 1280 500 L 1280 540
             L 1340 540 L 1340 520 L 1400 520 L 1400 540 L 1460 540 L 1460 510
             L 1520 510 L 1520 540 L 1600 540 L 1600 620 Z"/>
  </g>
  <!-- tiny window dots in the silhouette -->
  <g fill="{C['amber_lt']}" opacity="0.35">
    <rect x="752" y="528" width="3" height="3"/>
    <rect x="828" y="510" width="3" height="3"/>
    <rect x="1020" y="500" width="3" height="3"/>
    <rect x="1170" y="528" width="3" height="3"/>
    <rect x="1290" y="510" width="3" height="3"/>
    <rect x="1410" y="528" width="3" height="3"/>
  </g>''')

    # Delivery van silhouette — mid-ground, behind the bag (positioned to not conflict with phone)
    inner.append(f'''
  <g transform="translate(1050, 580)" filter="url(#ds-soft)">
    <!-- van body -->
    <rect x="-160" y="-90" width="280" height="130" rx="10" fill="{C['brand_lt']}"/>
    <rect x="-160" y="-90" width="280" height="22" fill="{C['brand']}"/>
    <!-- cab section -->
    <path d="M 120 -90 L 170 -55 L 170 40 L 120 40 Z" fill="{C['brand_lt']}"/>
    <!-- windshield -->
    <path d="M 120 -88 L 165 -55 L 165 -20 L 120 -20 Z" fill="{C['glass_mid']}" opacity="0.7"/>
    <line x1="120" y1="-55" x2="165" y2="-55" stroke="{C['brand']}" stroke-width="1.5"/>
    <!-- side door panel line -->
    <line x1="20" y1="-90" x2="20" y2="40" stroke="{C['brand']}" stroke-width="2"/>
    <!-- van branding -->
    <text x="-100" y="-15" font-family="Georgia, serif" font-weight="800" font-size="20" fill="{C['white']}">SPIN IT UP</text>
    <text x="-100" y="5" font-family="sans-serif" font-size="10" fill="{C['amber_lt']}" letter-spacing="2">PICKUP &amp; DELIVERY</text>
    <!-- a little laundry icon -->
    <circle cx="60" cy="-2" r="14" fill="{C['white']}" opacity="0.9"/>
    <circle cx="60" cy="-2" r="8" fill="{C['brand_lt']}"/>
    <!-- wheels -->
    <circle cx="-90" cy="50" r="22" fill="{C['ink']}"/>
    <circle cx="-90" cy="50" r="10" fill="{C['chrome_mid']}"/>
    <circle cx="-90" cy="50" r="5" fill="{C['chrome_dark']}"/>
    <circle cx="90" cy="50" r="22" fill="{C['ink']}"/>
    <circle cx="90" cy="50" r="10" fill="{C['chrome_mid']}"/>
    <circle cx="90" cy="50" r="5" fill="{C['chrome_dark']}"/>
    <!-- headlight glow -->
    <circle cx="168" cy="20" r="6" fill="{C['amber_lt']}"/>
    <circle cx="168" cy="20" r="16" fill="{C['amber_lt']}" opacity="0.25" filter="url(#glow-warm)"/>
  </g>''')

    # Dashed route from phone to bag area (curved)
    inner.append(f'''
  <path d="M 1240 300 Q 1430 460 1340 600 Q 1240 700 920 700"
        fill="none" stroke="{C['amber_lt']}" stroke-width="3"
        stroke-dasharray="12 10" stroke-linecap="round" opacity="0.85"/>
  <!-- destination pin at the end of route -->
  <g transform="translate(920, 700)">
    <circle r="10" fill="{C['amber']}" filter="url(#glow-warm)" opacity="0.4"/>
    <circle r="6" fill="{C['amber']}"/>
    <circle r="3" fill="{C['white']}"/>
  </g>''')

    # Laundry bag in the foreground — drawstring sack with realistic shading
    inner.append(f'''
  <g transform="translate(770, 540)" filter="url(#ds-soft)">
    <!-- ground shadow -->
    <ellipse cx="120" cy="280" rx="135" ry="18" fill="#000" opacity="0.5"/>
    <!-- main body of the sack with side shading -->
    <defs>
      <linearGradient id="sackGrad" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="{C['brand_dark']}"/>
        <stop offset="35%" stop-color="{C['brand']}"/>
        <stop offset="65%" stop-color="{C['brand_lt']}"/>
        <stop offset="100%" stop-color="{C['brand_dark']}"/>
      </linearGradient>
    </defs>
    <path d="M 30 80
             C 0 105, -10 200, 25 270
             C 60 305, 200 305, 235 270
             C 270 200, 260 105, 230 80
             C 215 70, 195 65, 130 65
             C 65 65, 45 70, 30 80 Z"
          fill="url(#sackGrad)"/>
    <!-- highlight along the left curve -->
    <path d="M 40 90 C 30 140, 30 220, 60 275" stroke="{C['brand_lt']}"
          stroke-width="6" fill="none" stroke-linecap="round" opacity="0.55"/>
    <path d="M 220 90 C 230 140, 230 220, 200 275" stroke="{C['brand_dark']}"
          stroke-width="8" fill="none" stroke-linecap="round" opacity="0.55"/>
    <!-- gathered top (dark cinched neck) -->
    <ellipse cx="130" cy="55" rx="58" ry="18" fill="{C['brand_dark']}"/>
    <!-- gathered ripples -->
    <path d="M 80 55 Q 90 38 100 50 Q 110 32 120 48 Q 130 30 140 48 Q 150 36 160 55"
          fill="none" stroke="{C['brand']}" stroke-width="3" stroke-linecap="round"/>
    <!-- drawstring ties -->
    <path d="M 88 50 Q 70 28 60 60" fill="none" stroke="{C['amber']}" stroke-width="4" stroke-linecap="round"/>
    <path d="M 172 50 Q 190 25 200 55" fill="none" stroke="{C['amber']}" stroke-width="4" stroke-linecap="round"/>
    <!-- ID tag swinging from the drawstring -->
    <g transform="translate(180, 95) rotate(15)">
      <line x1="0" y1="-30" x2="0" y2="0" stroke="{C['amber']}" stroke-width="2"/>
      <rect x="-26" y="0" width="52" height="32" rx="3" fill="{C['linen_hi']}" stroke="{C['gray_dk']}" stroke-width="1.5"/>
      <circle cx="0" cy="6" r="2.5" fill="{C['gray_dk']}"/>
      <text x="0" y="20" text-anchor="middle" font-family="sans-serif" font-size="7" font-weight="800" fill="{C['gray_dk']}" letter-spacing="0.6">SPIN IT UP</text>
      <text x="0" y="29" text-anchor="middle" font-family="Georgia, serif" font-size="10" font-weight="800" fill="{C['brand']}">#1842</text>
    </g>
  </g>''')

    # Smartphone in the top-right with detailed app UI
    inner.append(f'''
  <g transform="translate(1190, 140) rotate(-5)" filter="url(#ds-soft)">
    <!-- phone outer body -->
    <rect x="-4" y="-4" width="268" height="478" rx="40" fill="#000" opacity="0.4"/>
    <rect x="0" y="0" width="260" height="470" rx="36" fill="#1A2436"/>
    <!-- bezel highlight -->
    <rect x="3" y="3" width="254" height="464" rx="33" fill="none" stroke="#3D4A5C" stroke-width="1"/>
    <!-- screen -->
    <rect x="10" y="10" width="240" height="450" rx="28" fill="{C['off_white']}"/>
    <!-- dynamic island -->
    <rect x="100" y="20" width="60" height="14" rx="7" fill="#000"/>

    <!-- Status bar -->
    <text x="28" y="55" font-family="sans-serif" font-size="11" font-weight="700" fill="{C['ink']}">9:41</text>
    <text x="230" y="55" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="700" fill="{C['ink']}">●●●</text>

    <!-- Header band -->
    <rect x="20" y="72" width="220" height="68" rx="14" fill="{C['brand']}"/>
    <rect x="20" y="72" width="220" height="68" rx="14" fill="url(#bgGlow)" opacity="0.4"/>
    <text x="130" y="104" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="20" fill="{C['white']}">Spin It Up</text>
    <text x="130" y="124" text-anchor="middle" font-family="sans-serif" font-size="10" fill="{C['amber_lt']}" letter-spacing="2">PICKUP &amp; DELIVERY</text>

    <!-- Address card -->
    <rect x="20" y="154" width="220" height="60" rx="10" fill="#F1F5F9"/>
    <rect x="20" y="154" width="220" height="60" rx="10" fill="none" stroke="#E2E8F0" stroke-width="1"/>
    <circle cx="42" cy="184" r="11" fill="{C['coral']}"/>
    <path d="M 42 181 v 6 M 39 184 h 6" stroke="{C['white']}" stroke-width="1.7"/>
    <text x="62" y="178" font-family="sans-serif" font-size="9" font-weight="800" fill="{C['gray_md']}" letter-spacing="0.8">PICKUP FROM</text>
    <text x="62" y="196" font-family="sans-serif" font-size="11" font-weight="700" fill="{C['ink']}">2845 N Sawyer Ave</text>
    <text x="62" y="208" font-family="sans-serif" font-size="9" fill="{C['gray_md']}">Avondale, Chicago</text>

    <!-- Time card -->
    <rect x="20" y="226" width="220" height="60" rx="10" fill="#F1F5F9"/>
    <rect x="20" y="226" width="220" height="60" rx="10" fill="none" stroke="#E2E8F0" stroke-width="1"/>
    <circle cx="42" cy="256" r="11" fill="{C['amber']}"/>
    <path d="M 42 250 v 6 l 4 3" stroke="{C['white']}" stroke-width="1.7" stroke-linecap="round" fill="none"/>
    <text x="62" y="250" font-family="sans-serif" font-size="9" font-weight="800" fill="{C['gray_md']}" letter-spacing="0.8">PICKUP TIME</text>
    <text x="62" y="268" font-family="sans-serif" font-size="11" font-weight="700" fill="{C['ink']}">Today · 4:00 – 5:00 PM</text>
    <text x="62" y="282" font-family="sans-serif" font-size="9" font-weight="800" fill="{C['mint']}">● Driver assigned · 12 min away</text>

    <!-- Order summary -->
    <text x="30" y="310" font-family="sans-serif" font-size="10" font-weight="800" fill="{C['gray_md']}" letter-spacing="0.8">ORDER</text>
    <line x1="30" y1="318" x2="230" y2="318" stroke="#E2E8F0" stroke-width="1"/>
    <text x="30"  y="338" font-family="sans-serif" font-size="11" fill="{C['ink']}">Wash &amp; Fold · 18 lb</text>
    <text x="230" y="338" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="800" fill="{C['ink']}">$27.00</text>
    <text x="30"  y="358" font-family="sans-serif" font-size="11" fill="{C['ink']}">Delivery</text>
    <text x="230" y="358" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="800" fill="{C['mint']}">FREE</text>
    <line x1="30" y1="370" x2="230" y2="370" stroke="#E2E8F0" stroke-width="1"/>
    <text x="30"  y="392" font-family="sans-serif" font-size="11" font-weight="800" fill="{C['ink']}">Total</text>
    <text x="230" y="392" text-anchor="end" font-family="Georgia, serif" font-size="14" font-weight="800" fill="{C['brand']}">$27.00</text>

    <!-- CTA -->
    <rect x="20" y="408" width="220" height="46" rx="23" fill="{C['amber']}"/>
    <text x="130" y="437" text-anchor="middle" font-family="sans-serif" font-weight="800" font-size="13" fill="{C['white']}" letter-spacing="0.5">SCHEDULE PICKUP</text>

    <!-- screen reflection highlight -->
    <path d="M 30 30 Q 110 80 50 200 Q 25 130 30 30 Z" fill="{C['white']}" opacity="0.10"/>
  </g>''')

    # Toast notification (smaller, top-left of phone)
    inner.append(f'''
  <g transform="translate(740, 200)" filter="url(#ds-soft)">
    <rect width="330" height="76" rx="16" fill="{C['off_white']}"/>
    <circle cx="40" cy="38" r="22" fill="{C['mint']}"/>
    <path d="M 28 38 l 8 8 l 14 -15" stroke="{C['white']}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="74" y="34" font-family="sans-serif" font-size="14" font-weight="800" fill="{C['ink']}">Pickup confirmed</text>
    <text x="74" y="54" font-family="sans-serif" font-size="11" fill="{C['gray_md']}">Your driver is on the way · ETA 12 min</text>
  </g>''')

    return svg_wrap("\n".join(inner),
                    "Pickup and Delivery service",
                    "Smartphone with the Spin It Up app, a tagged laundry bag, and a delivery van silhouette")


# ──────────────────────────────────────────────────────────────────
# 4. COMMERCIAL  — large industrial machine in 3/4 view with detail,
#    stack of white commercial linens, clipboard, doorway hint.
# ──────────────────────────────────────────────────────────────────
def commercial() -> str:
    inner = []

    # Wall hint with a doorway opening on the far right (perspective depth)
    inner.append(f'''
  <defs>
    <linearGradient id="wallGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1B2D54"/>
      <stop offset="100%" stop-color="#0F1E3F"/>
    </linearGradient>
  </defs>
  <!-- Back wall stripe -->
  <rect x="700" y="0" width="900" height="680" fill="url(#wallGrad)" opacity="0.55"/>
  <!-- Doorway (rectangular cut with light spilling through) -->
  <rect x="1480" y="180" width="100" height="430" rx="2" fill="{C['amber_lt']}" opacity="0.15"/>
  <rect x="1490" y="200" width="80" height="410" rx="2" fill="{C['amber']}" opacity="0.12"/>
  <!-- second machine glimpse through doorway -->
  <rect x="1505" y="320" width="56" height="240" rx="4" fill="#5C6E85" opacity="0.45"/>
  <circle cx="1533" cy="440" r="22" fill="{C['glass_mid']}" opacity="0.5"/>
''')

    # Pipes along the top (industrial detail)
    inner.append(f'''
  <g stroke="{C['chrome_low']}" stroke-width="14" fill="none" stroke-linecap="round" opacity="0.7">
    <line x1="700" y1="90" x2="1440" y2="90"/>
    <line x1="700" y1="120" x2="1440" y2="120"/>
  </g>
  <g fill="{C['chrome_mid']}" opacity="0.7">
    <circle cx="780" cy="90" r="10"/>
    <circle cx="1060" cy="90" r="10"/>
    <circle cx="1340" cy="90" r="10"/>
    <circle cx="780" cy="120" r="10"/>
    <circle cx="1060" cy="120" r="10"/>
    <circle cx="1340" cy="120" r="10"/>
  </g>''')

    # Large industrial commercial washer
    inner.append(f'''
  <g transform="translate(1120, 170)" filter="url(#ds-soft)">
    <!-- floor shadow -->
    <ellipse cx="200" cy="620" rx="270" ry="22" fill="#000" opacity="0.6"/>
    <!-- side panel hinting depth -->
    <path d="M 410 60 L 442 80 L 442 600 L 410 580 Z" fill="url(#chromeSide)"/>
    <!-- main body -->
    <rect x="0" y="60" width="410" height="540" rx="20" fill="url(#chrome)" stroke="#5C6E85" stroke-width="2"/>
    <!-- top dark control panel -->
    <rect x="0" y="60" width="410" height="100" rx="20" fill="url(#panelDark)"/>
    <rect x="0" y="120" width="410" height="40" fill="url(#panelDark)"/>
    <!-- Brand mark -->
    <text x="205" y="100" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="24" fill="{C['white']}">SPIN IT UP</text>
    <text x="205" y="125" text-anchor="middle" font-family="sans-serif" font-size="11" fill="{C['amber_lt']}" letter-spacing="4">COMMERCIAL · 130 LB</text>

    <!-- BIG LCD display -->
    <rect x="40" y="178" width="180" height="68" rx="6" fill="url(#lcdGrad)" stroke="#000" stroke-width="1.5"/>
    <text x="130" y="222" text-anchor="middle" font-family="monospace" font-size="30" font-weight="800" fill="{C['amber_lt']}">44:30</text>
    <text x="130" y="240" text-anchor="middle" font-family="monospace" font-size="9" fill="{C['amber_lt']}" opacity="0.7" letter-spacing="2">HEAVY · WHITES</text>

    <!-- big knob -->
    <circle cx="290" cy="212" r="40" fill="#1B2330"/>
    <circle cx="290" cy="212" r="35" fill="url(#chrome)"/>
    <circle cx="290" cy="212" r="22" fill="#3D4A5C"/>
    <rect x="288" y="187" width="4" height="12" rx="2" fill="{C['amber']}"/>
    <circle cx="282" cy="206" r="6" fill="#FFFFFF" opacity="0.5"/>
    <g stroke="{C['gray_md']}" stroke-width="2" stroke-linecap="round">
      <line x1="290" y1="170" x2="290" y2="176"/>
      <line x1="332" y1="212" x2="326" y2="212"/>
      <line x1="290" y1="254" x2="290" y2="248"/>
      <line x1="248" y1="212" x2="254" y2="212"/>
    </g>

    <!-- secondary knobs -->
    <circle cx="355" cy="195" r="14" fill="{C['amber']}"/>
    <circle cx="355" cy="195" r="6" fill="{C['white']}"/>
    <circle cx="355" cy="230" r="10" fill="{C['mint']}"/>
    <circle cx="355" cy="230" r="14" fill="{C['mint']}" opacity="0.3" filter="url(#glow-warm)"/>

    <!-- amber brand strip -->
    <rect x="0" y="265" width="410" height="5" fill="{C['amber']}"/>
    <rect x="0" y="268" width="410" height="2" fill="{C['amber_dk']}"/>

    <!-- HUGE door -->
    <circle cx="205" cy="430" r="170" fill="#7A8497"/>
    <circle cx="205" cy="430" r="160" fill="url(#doorRing)"/>
    <circle cx="205" cy="430" r="145" fill="#1B2330"/>
    <circle cx="205" cy="430" r="138" fill="url(#glassDoor)"/>
    <!-- Linens tumbling inside -->
    <g transform="translate(205, 430)">
      <ellipse cx="-45" cy="-35" rx="72" ry="44" fill="{C['linen_hi']}" opacity="0.95"/>
      <ellipse cx="35" cy="-5" rx="68" ry="42" fill="{C['linen_mid']}" opacity="0.85"/>
      <ellipse cx="-15" cy="40" rx="78" ry="38" fill="{C['linen_hi']}" opacity="0.92"/>
      <ellipse cx="45" cy="55" rx="55" ry="30" fill="{C['linen_low']}" opacity="0.6"/>
      <line x1="-100" y1="-30" x2="10" y2="-30" stroke="{C['linen_low']}" stroke-width="1.5" opacity="0.6"/>
      <line x1="-15" y1="-5" x2="90" y2="-5" stroke="{C['linen_low']}" stroke-width="1.5" opacity="0.6"/>
      <line x1="-85" y1="40" x2="60" y2="40" stroke="{C['linen_low']}" stroke-width="1.5" opacity="0.5"/>
    </g>
    <!-- Glass highlight -->
    <ellipse cx="155" cy="368" rx="58" ry="26" fill="#FFFFFF" opacity="0.45"/>
    <ellipse cx="175" cy="370" rx="18" ry="8" fill="#FFFFFF" opacity="0.7"/>
    <!-- Door bolts -->
    <g fill="#3D4A5C">
      <circle cx="205" cy="270" r="6"/>
      <circle cx="365" cy="430" r="6"/>
      <circle cx="205" cy="590" r="6"/>
      <circle cx="45" cy="430" r="6"/>
    </g>
    <!-- Door handle -->
    <rect x="370" y="418" width="22" height="24" rx="4" fill="url(#chromeSide)"/>
    <!-- Bottom info strip -->
    <rect x="40" y="540" width="330" height="34" rx="6" fill="#1E2A40"/>
    <text x="205" y="562" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="{C['amber_lt']}" letter-spacing="3">HIGH-CAPACITY · ENERGY EFFICIENT</text>

    <!-- Kick plate at bottom -->
    <rect x="-6" y="595" width="448" height="20" rx="4" fill="{C['chrome_dark']}"/>
  </g>''')

    # Stack of folded white linens on a rolling cart in front-left
    stack_svg = ['<g filter="url(#ds-soft)">']
    yy = 690  # start at this y for the bottom of the bottommost fold
    for i, (dx, h, depth) in enumerate([(-6, 60, 22), (4, 56, 20), (-3, 58, 22), (6, 54, 20), (-4, 50, 18)]):
        w = 280 - abs(dx) * 2
        xx = 770 - w/2 + dx
        yy -= h
        # front face
        stack_svg.append(f'<rect x="{xx}" y="{yy+depth/2}" width="{w}" height="{h-depth/2}" rx="3" fill="{C["linen_mid"]}"/>')
        # top face
        stack_svg.append(f'<path d="M {xx} {yy+depth/2} L {xx+8} {yy} L {xx+w+8} {yy} L {xx+w} {yy+depth/2} Z" fill="{C["linen_hi"]}"/>')
        # right side
        stack_svg.append(f'<path d="M {xx+w} {yy+depth/2} L {xx+w+8} {yy} L {xx+w+8} {yy+h-depth/2-2} L {xx+w} {yy+h-2} Z" fill="{C["linen_low"]}"/>')
        # blue stripe accent on each towel (commercial branding)
        stack_svg.append(f'<rect x="{xx+12}" y="{yy+h/2}" width="{w-24}" height="3" fill="{C["brand_lt"]}" opacity="0.6"/>')
        # subtle crease
        stack_svg.append(f'<line x1="{xx+w-22}" y1="{yy+depth/2+5}" x2="{xx+w-22}" y2="{yy+h-6}" stroke="{C["linen_low"]}" stroke-width="1" opacity="0.4"/>')

    stack_svg.append('</g>')
    inner.append("\n  ".join(stack_svg))

    # Rolling cart wheels under the linen stack
    inner.append(f'''
  <g transform="translate(720, 700)">
    <rect x="0" y="0" width="300" height="14" rx="3" fill="{C['chrome_dark']}"/>
    <circle cx="40" cy="30" r="14" fill="{C['ink']}"/>
    <circle cx="40" cy="30" r="6" fill="{C['chrome_mid']}"/>
    <circle cx="260" cy="30" r="14" fill="{C['ink']}"/>
    <circle cx="260" cy="30" r="6" fill="{C['chrome_mid']}"/>
  </g>''')

    # Clipboard with B2B checklist (smaller, less central than before)
    inner.append(f'''
  <g transform="translate(960, 100) rotate(-6)" filter="url(#ds-tight)">
    <rect width="160" height="200" rx="6" fill="#9F7541"/>
    <rect x="4" y="4" width="152" height="192" rx="4" fill="{C['off_white']}"/>
    <rect x="64" y="-10" width="32" height="18" rx="3" fill="{C['gray_dk']}"/>
    <rect x="70" y="-5" width="20" height="8" rx="2" fill="{C['ink']}"/>
    <text x="80" y="32" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="13" fill="{C['ink']}">B2B ORDER</text>
    <line x1="18" y1="42" x2="142" y2="42" stroke="{C['gray_lt']}" stroke-width="1"/>
    <g font-family="sans-serif" font-size="10" fill="{C['ink']}">
      <rect x="18" y="56" width="11" height="11" rx="2" fill="{C['mint']}"/>
      <path d="M 20 62 l 3.5 3.5 l 5 -5" stroke="{C['white']}" stroke-width="1.7" fill="none" stroke-linecap="round"/>
      <text x="35" y="65">120 lb Linens</text>
      <rect x="18" y="76" width="11" height="11" rx="2" fill="{C['mint']}"/>
      <path d="M 20 82 l 3.5 3.5 l 5 -5" stroke="{C['white']}" stroke-width="1.7" fill="none" stroke-linecap="round"/>
      <text x="35" y="85">Salon Towels</text>
      <rect x="18" y="96" width="11" height="11" rx="2" fill="{C['mint']}"/>
      <path d="M 20 102 l 3.5 3.5 l 5 -5" stroke="{C['white']}" stroke-width="1.7" fill="none" stroke-linecap="round"/>
      <text x="35" y="105">Airbnb Sheets</text>
      <rect x="18" y="116" width="11" height="11" rx="2" stroke="{C['gray_md']}" stroke-width="1.3" fill="none"/>
      <text x="35" y="125">Gym Uniforms</text>
      <rect x="18" y="136" width="11" height="11" rx="2" stroke="{C['gray_md']}" stroke-width="1.3" fill="none"/>
      <text x="35" y="145">Restaurant Aprons</text>
    </g>
    <line x1="18" y1="158" x2="142" y2="158" stroke="{C['gray_lt']}" stroke-width="1"/>
    <text x="18" y="174" font-family="sans-serif" font-size="8" font-weight="800" fill="{C['gray_md']}" letter-spacing="0.8">TURNAROUND</text>
    <text x="18" y="190" font-family="Georgia, serif" font-size="13" font-weight="800" fill="{C['brand']}">24 HOURS</text>
  </g>''')

    return svg_wrap("\n".join(inner),
                    "Commercial Laundry Services",
                    "Large 130-pound commercial washing machine, stack of folded white linens on a rolling cart, and a B2B order clipboard")


# ──────────────────────────────────────────────────────────────────
# 5. IRONING & PRESSING  — ironing board in 3/4 perspective, shirt
#    mid-press with steam, hanging pressed shirts in background.
# ──────────────────────────────────────────────────────────────────
def ironing_pressing() -> str:
    inner = []

    # Hanging garment rack in the background (small, hinting at the service environment)
    def garment(x, color, opacity, kind="shirt"):
        if kind == "jacket":
            return f'''
    <g transform="translate({x}, 180)">
      <!-- hanger -->
      <path d="M 0 0 q 0 -14 12 -14 q 12 0 12 12" fill="none" stroke="{C['chrome_mid']}" stroke-width="2"/>
      <path d="M 12 10 L -42 48 L 66 48 Z" fill="none" stroke="{C['chrome_mid']}" stroke-width="2"/>
      <!-- jacket body with collar and lapels -->
      <path d="M -48 45 L -52 80 L -55 240 L -25 250 L -25 100 L 12 80 L 49 100 L 49 250 L 79 240 L 76 80 L 72 45 L 35 65 L 12 75 L -11 65 Z"
            fill="{color}" opacity="{opacity}"/>
      <!-- lapels -->
      <path d="M -25 100 L -15 80 L 12 75 L 12 100 Z" fill="{color}" stroke="#000" stroke-width="0.8" opacity="0.5"/>
      <path d="M 49 100 L 38 80 L 12 75 L 12 100 Z" fill="{color}" stroke="#000" stroke-width="0.8" opacity="0.5"/>
      <line x1="12" y1="100" x2="12" y2="250" stroke="#000" stroke-width="1" opacity="0.4"/>
    </g>'''
        # dress shirt
        return f'''
    <g transform="translate({x}, 180)">
      <!-- hanger -->
      <path d="M 0 0 q 0 -14 12 -14 q 12 0 12 12" fill="none" stroke="{C['chrome_mid']}" stroke-width="2"/>
      <path d="M 12 10 L -38 48 L 62 48 Z" fill="none" stroke="{C['chrome_mid']}" stroke-width="2"/>
      <!-- shoulders / yoke -->
      <path d="M -42 45 Q -50 70 -48 100 L -28 95 L -10 75 Q 12 80 34 75 L 52 95 L 72 100 Q 70 70 62 45 Z"
            fill="{color}" opacity="{opacity}"/>
      <!-- collar V -->
      <path d="M -10 75 L 12 92 L 34 75 L 26 70 L 12 78 L -2 70 Z" fill="{color}" opacity="{opacity * 0.6}"/>
      <!-- body -->
      <path d="M -48 100 L -52 230 L -22 240 L -22 100 Z" fill="{color}" opacity="{opacity}"/>
      <path d="M 52 100 L 56 230 L 26 240 L 26 100 Z" fill="{color}" opacity="{opacity}"/>
      <path d="M -22 100 L -22 245 L 26 245 L 26 100 Z" fill="{color}" opacity="{opacity * 0.92}"/>
      <!-- button placket -->
      <line x1="2" y1="92" x2="2" y2="245" stroke="#000" stroke-width="0.8" opacity="0.4"/>
      <!-- a few subtle wrinkles -->
      <path d="M -42 130 Q -32 180 -42 230" stroke="#000" stroke-width="0.6" fill="none" opacity="0.25"/>
      <path d="M 42 130 Q 52 180 42 230" stroke="#000" stroke-width="0.6" fill="none" opacity="0.25"/>
    </g>'''

    inner.append(f'''
  <g opacity="0.6">
    <!-- horizontal bar -->
    <line x1="780" y1="180" x2="1560" y2="180" stroke="{C['chrome_mid']}" stroke-width="4"/>
    <line x1="780" y1="180" x2="1560" y2="180" stroke="#FFFFFF" stroke-width="1" opacity="0.4"/>
    {garment(840,  C['shirt_blue'],  0.75)}
    {garment(960,  C['linen_hi'],    0.85)}
    {garment(1080, C['shirt_pink'],  0.7)}
    {garment(1200, '#1A2436',        0.85, 'jacket')}
    {garment(1320, C['shirt_sage'],  0.75)}
    {garment(1440, C['linen_hi'],    0.8)}
  </g>''')

    # IRONING BOARD in 3/4 perspective — receding to the right
    inner.append(f'''
  <g filter="url(#ds-soft)">
    <!-- Board surface (parallelogram for perspective) -->
    <path d="M 700 600
             L 1500 540
             L 1560 580
             L 740 660 Z"
          fill="{C['linen_hi']}" stroke="{C['linen_low']}" stroke-width="1.5"/>
    <!-- Board edge (thin shadow under board) -->
    <path d="M 700 600 L 1500 540 L 1500 552 L 700 612 Z" fill="{C['linen_low']}" opacity="0.4"/>
    <!-- Board cloth pattern hint (subtle stitches) -->
    <g stroke="{C['linen_low']}" stroke-width="1" opacity="0.25" stroke-dasharray="4 6" fill="none">
      <path d="M 720 612 L 1495 552"/>
      <path d="M 720 632 L 1500 572"/>
    </g>
    <!-- Board legs (X-frame) -->
    <line x1="820" y1="650" x2="900" y2="870" stroke="{C['chrome_low']}" stroke-width="6" stroke-linecap="round"/>
    <line x1="900" y1="640" x2="820" y2="870" stroke="{C['chrome_low']}" stroke-width="6" stroke-linecap="round"/>
    <line x1="1320" y1="570" x2="1400" y2="800" stroke="{C['chrome_low']}" stroke-width="6" stroke-linecap="round"/>
    <line x1="1400" y1="560" x2="1320" y2="800" stroke="{C['chrome_low']}" stroke-width="6" stroke-linecap="round"/>
    <!-- floor shadow under board -->
    <ellipse cx="1130" cy="870" rx="430" ry="14" fill="#000" opacity="0.45"/>
  </g>''')

    # Dress shirt mid-press on the board — laid flat with realistic folds
    inner.append(f'''
  <g transform="translate(950, 480)" filter="url(#ds-tight)">
    <!-- shirt body laid flat -->
    <path d="M -150 130
             L -180 100
             L -160 78
             L -120 88
             L -100 60
             Q -70 80 -20 80
             Q 30 80 60 60
             L 80 88
             L 120 78
             L 140 100
             L 110 130
             L 110 200
             L -150 200 Z"
          fill="{C['linen_hi']}" stroke="{C['linen_low']}" stroke-width="2"/>
    <!-- collar -->
    <path d="M -100 60 L -20 95 L 60 60 L 40 50 L -20 70 L -80 50 Z"
          fill="{C['linen_mid']}" stroke="{C['linen_low']}" stroke-width="1.5"/>
    <!-- placket + buttons -->
    <line x1="-20" y1="90" x2="-20" y2="200" stroke="{C['linen_low']}" stroke-width="1.5"/>
    <g fill="{C['linen_low']}">
      <circle cx="-20" cy="110" r="2.5"/>
      <circle cx="-20" cy="135" r="2.5"/>
      <circle cx="-20" cy="160" r="2.5"/>
      <circle cx="-20" cy="185" r="2.5"/>
    </g>
    <!-- pocket -->
    <rect x="-90" y="120" width="44" height="42" rx="2" fill="none" stroke="{C['linen_low']}" stroke-width="1.5"/>
    <!-- realistic fabric shadow / wrinkle hints -->
    <path d="M -130 110 Q -110 130 -100 150" stroke="{C['linen_low']}" stroke-width="1" fill="none" opacity="0.4"/>
    <path d="M 80 105 Q 95 130 105 155" stroke="{C['linen_low']}" stroke-width="1" fill="none" opacity="0.4"/>
    <path d="M -50 175 Q -20 185 10 175" stroke="{C['linen_low']}" stroke-width="1" fill="none" opacity="0.3"/>
    <!-- ironed crisp gleam (specular highlight on the pressed area) -->
    <path d="M -60 100 Q -20 110 50 100 L 50 130 Q -20 140 -60 130 Z" fill="#FFFFFF" opacity="0.35"/>
  </g>''')

    # Steam puffs rising from where iron is — soft, with blur filter
    inner.append(f'''
  <g filter="url(#steam-blur)" opacity="0.92">
    <ellipse cx="1010" cy="380" rx="48" ry="28" fill="{C['glass_hi']}"/>
    <ellipse cx="1055" cy="330" rx="38" ry="22" fill="{C['glass_hi']}"/>
    <ellipse cx="1025" cy="280" rx="30" ry="18" fill="{C['glass_hi']}" opacity="0.85"/>
    <ellipse cx="1080" cy="245" rx="24" ry="15" fill="{C['glass_hi']}" opacity="0.7"/>
    <ellipse cx="1050" cy="205" rx="18" ry="12" fill="{C['glass_hi']}" opacity="0.55"/>
    <ellipse cx="1140" cy="335" rx="28" ry="17" fill="{C['glass_hi']}" opacity="0.75"/>
    <ellipse cx="1175" cy="290" rx="20" ry="13" fill="{C['glass_hi']}" opacity="0.6"/>
    <ellipse cx="1200" cy="245" rx="14" ry="10" fill="{C['glass_hi']}" opacity="0.45"/>
  </g>''')

    # THE IRON — sitting ON the shirt, tilted slightly, with realistic chrome + steam
    inner.append(f'''
  <g transform="translate(940, 490) rotate(-10)" filter="url(#ds-soft)">
    <!-- shadow on the shirt under the iron -->
    <ellipse cx="160" cy="90" rx="170" ry="14" fill="#000" opacity="0.35"/>
    <!-- soleplate -->
    <defs>
      <linearGradient id="soleGrad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#A8B5C5"/>
        <stop offset="60%" stop-color="#6E7C92"/>
        <stop offset="100%" stop-color="#3D4A5C"/>
      </linearGradient>
    </defs>
    <path d="M 0 60
             Q 0 22 40 12
             L 280 12
             Q 340 12 360 60
             L 360 85
             L -8 85
             L 0 60 Z"
          fill="url(#soleGrad)" stroke="#2D3845" stroke-width="2"/>
    <!-- soleplate highlight strip -->
    <path d="M 8 30 Q 40 22 80 24 L 280 24 Q 330 24 348 50"
          stroke="#FFFFFF" stroke-width="2" fill="none" opacity="0.55" stroke-linecap="round"/>
    <!-- steam holes -->
    <g fill="#1B2330">
      <circle cx="50"  cy="55" r="3.5"/>
      <circle cx="90"  cy="55" r="3.5"/>
      <circle cx="130" cy="55" r="3.5"/>
      <circle cx="170" cy="55" r="3.5"/>
      <circle cx="210" cy="55" r="3.5"/>
      <circle cx="250" cy="55" r="3.5"/>
      <circle cx="290" cy="55" r="3.5"/>
    </g>
    <!-- main shell (colored body) -->
    <defs>
      <linearGradient id="ironShell" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="{C['brand_lt']}"/>
        <stop offset="55%" stop-color="{C['brand']}"/>
        <stop offset="100%" stop-color="{C['brand_dark']}"/>
      </linearGradient>
    </defs>
    <path d="M 28 12
             Q 35 -40 100 -55
             L 250 -55
             Q 310 -55 320 -10
             Q 325 6 320 12 Z"
          fill="url(#ironShell)" stroke="{C['brand_dark']}" stroke-width="2"/>
    <!-- shell highlight -->
    <path d="M 45 5 Q 60 -38 110 -48" stroke="#FFFFFF" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.45"/>
    <path d="M 280 5 Q 295 -25 305 -10" stroke="#FFFFFF" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.5"/>
    <!-- handle -->
    <path d="M 88 -55 Q 105 -135 175 -135 Q 250 -135 268 -55"
          fill="none" stroke="{C['ink']}" stroke-width="16" stroke-linecap="round"/>
    <path d="M 95 -55 Q 112 -125 175 -125 Q 245 -125 261 -55"
          fill="none" stroke="{C['amber']}" stroke-width="9" stroke-linecap="round"/>
    <path d="M 100 -55 Q 116 -118 175 -118"
          fill="none" stroke="{C['amber_lt']}" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
    <!-- water tank window -->
    <rect x="55" y="-30" width="58" height="26" rx="5" fill="{C['glass_hi']}" opacity="0.65" stroke="{C['brand_dark']}" stroke-width="1.5"/>
    <line x1="60" y1="-14" x2="108" y2="-14" stroke="{C['brand']}" stroke-width="1" opacity="0.6"/>
    <!-- temp dial -->
    <circle cx="210" cy="-20" r="16" fill="#FFFFFF" stroke="{C['ink']}" stroke-width="2"/>
    <circle cx="210" cy="-20" r="12" fill="{C['off_white']}"/>
    <rect x="208.5" y="-32" width="3" height="10" rx="1" fill="{C['coral']}"/>
    <circle cx="206" cy="-23" r="2.5" fill="#FFFFFF" opacity="0.6"/>
    <!-- LED indicator -->
    <circle cx="258" cy="-20" r="6" fill="{C['coral']}"/>
    <circle cx="258" cy="-20" r="11" fill="{C['coral']}" opacity="0.35" filter="url(#glow-warm)"/>
  </g>''')

    return svg_wrap("\n".join(inner),
                    "Ironing and Pressing Service",
                    "Steam iron pressing a dress shirt on a board with pressed garments hanging behind")


# ──────────────────────────────────────────────────────────────────
# Render
# ──────────────────────────────────────────────────────────────────
files = {
    "hero-self-service.svg":     self_service(),
    "hero-wash-and-fold.svg":    wash_and_fold(),
    "hero-pickup-delivery.svg":  pickup_delivery(),
    "hero-commercial.svg":       commercial(),
    "hero-ironing-pressing.svg": ironing_pressing(),
}
for name, content in files.items():
    p = os.path.join(OUT_DIR, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ {name}  ({os.path.getsize(p):,} bytes)")
print(f"\n→ {OUT_DIR}")
