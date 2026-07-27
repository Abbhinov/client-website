"""
Spin It Up Laundry — Page Hero Images (v3)
==========================================
5 new SVGs for non-service pages, matching v2 style with illustration
shifted further right (~130px) to give more breathing room for text.

PAGES:
  hero-services.svg   — services overview
  hero-pricing.svg    — pricing
  hero-about.svg      — about
  hero-contact.svg    — contact
  hero-faq.svg        — FAQ

LAYOUT:
  viewBox 1600 x 900 (16:9)
  Left ~55% (x 0–860): background only — text overlay zone (BIGGER than v2)
  Right ~45% (x 860–1600): illustration
"""

import os

OUT_DIR = "/home/claude/output_v3"
os.makedirs(OUT_DIR, exist_ok=True)

# Where the illustration content begins horizontally.
# v2 was ~720, now shifted right by ~130px.
RX = 860  # right-zone start
RC = (RX + 1600) // 2  # right-zone center: ~1230

C = {
    "bg_top": "#0A1A3D", "bg_bot": "#142A55", "bg_glow": "#3A6FB0", "bg_warm": "#D89A55",
    "chrome_hi": "#F4F7FA", "chrome_mid": "#A8B5C5", "chrome_low": "#3D4A5C", "chrome_dark": "#1B2330",
    "glass_hi": "#EAF3FF", "glass_mid": "#7BA4D6", "glass_low": "#1E3458",
    "brand_dark": "#0B2447", "brand": "#19376D", "brand_lt": "#576CBC",
    "amber": "#E6A23C", "amber_dk": "#B07820", "amber_lt": "#F4C77F",
    "linen_hi": "#F8F4EC", "linen_mid": "#E4DDC9", "linen_low": "#A89B7A",
    "shirt_blue": "#A8C5E4", "shirt_pink": "#C97B7B", "shirt_sage": "#8DA88B", "shirt_olive": "#A89853",
    "brick": "#8B4F3D", "brick_lt": "#A8624F", "brick_dk": "#5C3326",
    "white": "#FFFFFF", "off_white": "#F0F4F8",
    "gray_lt": "#CFD6E0", "gray_md": "#7C8699", "gray_dk": "#3A4456", "ink": "#0A1A3D",
    "mint": "#5FB07A", "coral": "#C46A5C", "lilac": "#876FB0",
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
  <linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{C['chrome_hi']}"/>
    <stop offset="18%" stop-color="#D7DEE8"/>
    <stop offset="48%" stop-color="{C['chrome_mid']}"/>
    <stop offset="78%" stop-color="#6E7C92"/>
    <stop offset="100%" stop-color="{C['chrome_low']}"/>
  </linearGradient>
  <linearGradient id="chromeSide" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{C['chrome_low']}"/>
    <stop offset="30%" stop-color="#7888A0"/>
    <stop offset="70%" stop-color="{C['chrome_mid']}"/>
    <stop offset="100%" stop-color="{C['chrome_hi']}"/>
  </linearGradient>
  <linearGradient id="panelDark" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#202B3E"/>
    <stop offset="100%" stop-color="{C['chrome_dark']}"/>
  </linearGradient>
  <radialGradient id="glassDoor" cx="35%" cy="28%" r="75%">
    <stop offset="0%" stop-color="{C['glass_hi']}" stop-opacity="0.95"/>
    <stop offset="22%" stop-color="#C7DBF2" stop-opacity="0.85"/>
    <stop offset="55%" stop-color="{C['glass_mid']}" stop-opacity="0.75"/>
    <stop offset="100%" stop-color="{C['glass_low']}" stop-opacity="0.95"/>
  </radialGradient>
  <linearGradient id="doorRing" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#C5CCD8"/>
    <stop offset="50%" stop-color="#7A8497"/>
    <stop offset="100%" stop-color="{C['chrome_dark']}"/>
  </linearGradient>
  <linearGradient id="lcdGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0E1A2F"/>
    <stop offset="100%" stop-color="#1E3458"/>
  </linearGradient>

  <!-- Brick texture pattern for the about page -->
  <pattern id="brickPattern" x="0" y="0" width="80" height="32" patternUnits="userSpaceOnUse">
    <rect width="80" height="32" fill="{C['brick']}"/>
    <rect width="80" height="32" fill="{C['brick_dk']}" opacity="0.3"/>
    <line x1="0" y1="0" x2="80" y2="0" stroke="{C['brick_dk']}" stroke-width="1.5"/>
    <line x1="0" y1="16" x2="80" y2="16" stroke="{C['brick_dk']}" stroke-width="1.5"/>
    <line x1="40" y1="0" x2="40" y2="16" stroke="{C['brick_dk']}" stroke-width="1.5"/>
    <line x1="0" y1="16" x2="0" y2="32" stroke="{C['brick_dk']}" stroke-width="1.5"/>
    <line x1="80" y1="16" x2="80" y2="32" stroke="{C['brick_dk']}" stroke-width="1.5"/>
    <rect x="2" y="2" width="36" height="12" fill="{C['brick_lt']}" opacity="0.25"/>
    <rect x="42" y="2" width="36" height="12" fill="{C['brick_lt']}" opacity="0.2"/>
    <rect x="2" y="18" width="76" height="12" fill="{C['brick_lt']}" opacity="0.22"/>
  </pattern>

  <!-- Warm window light gradient (for about) -->
  <linearGradient id="windowLight" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#FFE2B0" stop-opacity="0.95"/>
    <stop offset="100%" stop-color="#E89F4C" stop-opacity="0.75"/>
  </linearGradient>

  <!-- Paper / card -->
  <linearGradient id="paperGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{C['linen_hi']}"/>
    <stop offset="100%" stop-color="{C['linen_mid']}"/>
  </linearGradient>

  <!-- Map streets gradient -->
  <linearGradient id="mapGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1F345C"/>
    <stop offset="100%" stop-color="#13234A"/>
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
  <filter id="glow-warm" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="8"/>
  </filter>
  <filter id="glow-amber" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="12"/>
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
# 1. SERVICES OVERVIEW — curated still-life with washer, folded stack,
#    phone, iron, all the brand's services in one composition.
# ──────────────────────────────────────────────────────────────────
def services_overview():
    inner = []

    # Central washing machine — the brand's hero object
    cx = 1180
    inner.append(f'''
  <g transform="translate({cx - 140}, 200)" filter="url(#ds-soft)">
    <!-- floor shadow -->
    <ellipse cx="140" cy="560" rx="200" ry="20" fill="#000" opacity="0.55"/>
    <!-- side panel -->
    <path d="M 280 32 L 296 44 L 296 540 L 280 528 Z" fill="url(#chromeSide)"/>
    <!-- main body -->
    <rect x="0" y="32" width="280" height="500" rx="14" fill="url(#chrome)" stroke="#5C6E85" stroke-width="1.5"/>
    <!-- control panel -->
    <rect x="10" y="44" width="260" height="78" rx="8" fill="url(#panelDark)"/>
    <!-- LCD -->
    <rect x="24" y="60" width="96" height="46" rx="4" fill="url(#lcdGrad)" stroke="#000" stroke-width="1"/>
    <text x="72" y="93" text-anchor="middle" font-family="monospace" font-size="22" font-weight="800" fill="{C['amber_lt']}">SPIN</text>
    <!-- knob -->
    <circle cx="210" cy="82" r="22" fill="#1B2330"/>
    <circle cx="210" cy="82" r="19" fill="url(#chrome)"/>
    <circle cx="210" cy="82" r="14" fill="#3D4A5C"/>
    <rect x="208.5" y="69" width="3" height="10" rx="1" fill="{C['amber']}"/>
    <!-- LED dots -->
    <circle cx="138" cy="68" r="3" fill="{C['mint']}"/>
    <circle cx="156" cy="68" r="3" fill="{C['amber']}"/>
    <circle cx="174" cy="68" r="3" fill="{C['coral']}"/>
    <!-- brand strip -->
    <rect x="10" y="130" width="260" height="4" fill="{C['amber']}"/>
    <text x="140" y="148" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="700" fill="{C['gray_dk']}" letter-spacing="4">SPIN IT UP</text>
    <!-- door bezel -->
    <circle cx="140" cy="330" r="128" fill="#7A8497"/>
    <circle cx="140" cy="330" r="122" fill="url(#doorRing)"/>
    <circle cx="140" cy="330" r="108" fill="#1B2330"/>
    <circle cx="140" cy="330" r="102" fill="url(#glassDoor)"/>
    <!-- clothes inside -->
    <g transform="translate(140, 330)">
      <ellipse cx="-28" cy="18" rx="54" ry="36" fill="{C['shirt_pink']}" opacity="0.85"/>
      <ellipse cx="30" cy="-10" rx="48" ry="34" fill="{C['shirt_blue']}" opacity="0.85"/>
      <ellipse cx="18" cy="36" rx="42" ry="24" fill="{C['shirt_sage']}" opacity="0.75"/>
    </g>
    <!-- highlight -->
    <ellipse cx="100" cy="285" rx="38" ry="18" fill="#FFFFFF" opacity="0.45"/>
    <!-- handle -->
    <rect x="265" y="318" width="14" height="24" rx="3" fill="url(#chromeSide)"/>
    <!-- coin/card reader -->
    <rect x="30" y="475" width="220" height="38" rx="6" fill="#1E2A40" stroke="#3D4A5C" stroke-width="1"/>
    <rect x="44" y="485" width="50" height="18" rx="2" fill="{C['chrome_dark']}"/>
    <text x="69" y="498" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="{C['amber_lt']}">CARD</text>
    <rect x="102" y="485" width="50" height="18" rx="2" fill="{C['brand_lt']}"/>
    <text x="127" y="498" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="{C['white']}">EBT</text>
    <circle cx="230" cy="494" r="4" fill="{C['mint']}"/>
    <!-- kick plate -->
    <rect x="-4" y="528" width="304" height="18" rx="3" fill="{C['chrome_dark']}"/>
  </g>''')

    # Folded laundry stack to the right of washer
    inner.append('<g filter="url(#ds-soft)">')
    stack_cx = 1490
    yy = 695
    for dx, h, depth, top, front, edge in [
        ( 4, 44, 18, C["shirt_blue"],  "#6A8FB8", "#3D5B82"),
        (-3, 40, 16, C["linen_hi"],    "#C9C1AB", "#7C7458"),
        ( 6, 42, 16, C["shirt_pink"],  "#A0584C", "#6B3328"),
        (-4, 40, 16, C["linen_hi"],    "#C9C1AB", "#7C7458"),
    ]:
        w = 180 - abs(dx) * 2
        x = stack_cx - w/2 + dx
        yy -= h
        inner.append(f'<rect x="{x}" y="{yy+depth/2}" width="{w}" height="{h-depth/2}" rx="3" fill="{front}"/>')
        inner.append(f'<path d="M {x} {yy+depth/2} L {x+6} {yy} L {x+w+6} {yy} L {x+w} {yy+depth/2} Z" fill="{top}"/>')
        inner.append(f'<path d="M {x+w} {yy+depth/2} L {x+w+6} {yy} L {x+w+6} {yy+h-depth/2-2} L {x+w} {yy+h-2} Z" fill="{edge}"/>')
        inner.append(f'<line x1="{x+8}" y1="{yy+h/2+3}" x2="{x+w-8}" y2="{yy+h/2+3}" stroke="{edge}" stroke-width="1" opacity="0.5"/>')
    inner.append('</g>')

    # Iron resting on top of the stack
    inner.append(f'''
  <g transform="translate(1430, 510) rotate(-8)" filter="url(#ds-tight)">
    <!-- soleplate -->
    <path d="M 0 30 Q 0 10 18 6 L 110 6 Q 140 6 150 30 L 150 42 L -2 42 L 0 30 Z"
          fill="#A8B5C5" stroke="#3D4A5C" stroke-width="1.5"/>
    <!-- shell -->
    <path d="M 12 6 Q 18 -18 50 -22 L 100 -22 Q 130 -22 138 -4 Q 140 4 138 6 Z" fill="{C['brand']}" stroke="{C['brand_dark']}" stroke-width="1.5"/>
    <!-- handle -->
    <path d="M 36 -22 Q 50 -54 75 -54 Q 100 -54 116 -22" fill="none" stroke="{C['ink']}" stroke-width="9" stroke-linecap="round"/>
    <path d="M 40 -22 Q 54 -48 75 -48 Q 96 -48 112 -22" fill="none" stroke="{C['amber']}" stroke-width="5" stroke-linecap="round"/>
    <!-- LED -->
    <circle cx="108" cy="-8" r="3" fill="{C['coral']}"/>
  </g>''')

    # Tiny steam puffs from iron
    inner.append(f'''
  <g opacity="0.65">
    <ellipse cx="1495" cy="475" rx="14" ry="9" fill="{C['glass_hi']}"/>
    <ellipse cx="1515" cy="450" rx="10" ry="7" fill="{C['glass_hi']}" opacity="0.7"/>
    <ellipse cx="1500" cy="425" rx="7" ry="5" fill="{C['glass_hi']}" opacity="0.5"/>
  </g>''')

    # Phone leaning against the front of the washer (lower-left)
    inner.append(f'''
  <g transform="translate(905, 540) rotate(-8)" filter="url(#ds-soft)">
    <rect x="0" y="0" width="130" height="240" rx="22" fill="#1A2436" stroke="#3D4A5C" stroke-width="1"/>
    <rect x="6" y="6" width="118" height="228" rx="18" fill="{C['off_white']}"/>
    <rect x="50" y="13" width="30" height="8" rx="4" fill="#000"/>
    <!-- header -->
    <rect x="14" y="34" width="102" height="46" rx="6" fill="{C['brand']}"/>
    <text x="65" y="55" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="12" fill="{C['white']}">Spin It Up</text>
    <text x="65" y="69" text-anchor="middle" font-family="sans-serif" font-size="6" fill="{C['amber_lt']}" letter-spacing="1.5">SERVICES</text>
    <!-- service rows -->
    <g font-family="sans-serif" font-size="7" fill="{C['ink']}">
      <rect x="14" y="90" width="102" height="22" rx="4" fill="#F1F5F9"/>
      <circle cx="24" cy="101" r="5" fill="{C['amber']}"/>
      <text x="34" y="103.5" font-weight="700">Self-Service</text>
      <rect x="14" y="118" width="102" height="22" rx="4" fill="#F1F5F9"/>
      <circle cx="24" cy="129" r="5" fill="{C['mint']}"/>
      <text x="34" y="131.5" font-weight="700">Wash &amp; Fold</text>
      <rect x="14" y="146" width="102" height="22" rx="4" fill="#F1F5F9"/>
      <circle cx="24" cy="157" r="5" fill="{C['coral']}"/>
      <text x="34" y="159.5" font-weight="700">Pickup &amp; Delivery</text>
      <rect x="14" y="174" width="102" height="22" rx="4" fill="#F1F5F9"/>
      <circle cx="24" cy="185" r="5" fill="{C['lilac']}"/>
      <text x="34" y="187.5" font-weight="700">Commercial</text>
      <rect x="14" y="202" width="102" height="22" rx="4" fill="#F1F5F9"/>
      <circle cx="24" cy="213" r="5" fill="{C['brand_lt']}"/>
      <text x="34" y="215.5" font-weight="700">Ironing</text>
    </g>
  </g>''')

    # Floor reflection wash
    inner.append(f'''
  <g opacity="0.18">
    <ellipse cx="1180" cy="770" rx="380" ry="12" fill="{C['bg_warm']}"/>
  </g>''')

    return svg_wrap("\n".join(inner),
                    "Spin It Up Laundry — All Services",
                    "Washing machine, folded laundry stack, steam iron, and a phone showing the full service menu")


# ──────────────────────────────────────────────────────────────────
# 2. PRICING — a prominent "rate card" with all services + prices,
#    coins / receipt accents.
# ──────────────────────────────────────────────────────────────────
def pricing():
    inner = []

    # Receipt curling at the bottom-left of the card (decorative)
    inner.append(f'''
  <g transform="translate(900, 580) rotate(-8)" filter="url(#ds-soft)">
    <path d="M 0 0 L 110 0 L 110 220 Q 95 230 80 220 Q 65 230 50 220 Q 35 230 20 220 Q 5 230 0 220 Z"
          fill="{C['linen_hi']}"/>
    <path d="M 0 0 L 110 0 L 110 220 Q 95 230 80 220 Q 65 230 50 220 Q 35 230 20 220 Q 5 230 0 220 Z"
          fill="none" stroke="{C['linen_low']}" stroke-width="0.8" opacity="0.5"/>
    <text x="55" y="22" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="11" fill="{C['ink']}" letter-spacing="2">RECEIPT</text>
    <line x1="10" y1="32" x2="100" y2="32" stroke="{C['gray_md']}" stroke-width="0.6" stroke-dasharray="2 2"/>
    <g font-family="monospace" font-size="8" fill="{C['gray_dk']}">
      <text x="10" y="48">WASH &amp; FOLD</text>
      <text x="100" y="48" text-anchor="end" font-weight="700" fill="{C['ink']}">$24.00</text>
      <text x="10" y="64">16 LB @ $1.50</text>
      <text x="10" y="84">DELIVERY</text>
      <text x="100" y="84" text-anchor="end" fill="{C['mint']}" font-weight="700">FREE</text>
      <text x="10" y="100">DETERGENT</text>
      <text x="100" y="100" text-anchor="end">INCL.</text>
    </g>
    <line x1="10" y1="118" x2="100" y2="118" stroke="{C['gray_dk']}" stroke-width="1"/>
    <g font-family="monospace" font-size="9" fill="{C['ink']}" font-weight="800">
      <text x="10" y="135">TOTAL</text>
      <text x="100" y="135" text-anchor="end" fill="{C['brand']}">$24.00</text>
    </g>
    <line x1="10" y1="148" x2="100" y2="148" stroke="{C['gray_md']}" stroke-width="0.6" stroke-dasharray="2 2"/>
    <text x="55" y="166" text-anchor="middle" font-family="sans-serif" font-size="7" fill="{C['gray_md']}">THANK YOU!</text>
    <text x="55" y="180" text-anchor="middle" font-family="sans-serif" font-size="6" fill="{C['gray_md']}">SPIN IT UP · AVONDALE</text>
    <!-- barcode -->
    <g fill="{C['ink']}">
      <rect x="20" y="190" width="2" height="20"/>
      <rect x="25" y="190" width="1" height="20"/>
      <rect x="28" y="190" width="3" height="20"/>
      <rect x="34" y="190" width="1" height="20"/>
      <rect x="37" y="190" width="2" height="20"/>
      <rect x="42" y="190" width="1" height="20"/>
      <rect x="45" y="190" width="3" height="20"/>
      <rect x="51" y="190" width="1" height="20"/>
      <rect x="54" y="190" width="2" height="20"/>
      <rect x="59" y="190" width="3" height="20"/>
      <rect x="65" y="190" width="1" height="20"/>
      <rect x="68" y="190" width="2" height="20"/>
      <rect x="73" y="190" width="3" height="20"/>
      <rect x="79" y="190" width="1" height="20"/>
      <rect x="82" y="190" width="2" height="20"/>
      <rect x="87" y="190" width="3" height="20"/>
      <rect x="93" y="190" width="1" height="20"/>
    </g>
  </g>''')

    # Main pricing card — central, dominant
    card_x, card_y = 1050, 130
    card_w, card_h = 480, 640
    inner.append(f'''
  <g filter="url(#ds-soft)">
    <!-- card body with subtle paper gradient -->
    <rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" rx="14" fill="url(#paperGrad)"/>
    <rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" rx="14" fill="none" stroke="{C['linen_low']}" stroke-width="1.5" opacity="0.6"/>
    <!-- top accent bar -->
    <rect x="{card_x}" y="{card_y}" width="{card_w}" height="60" rx="14" fill="{C['brand']}"/>
    <rect x="{card_x}" y="{card_y + 46}" width="{card_w}" height="14" fill="{C['brand']}"/>
    <rect x="{card_x}" y="{card_y + 58}" width="{card_w}" height="3" fill="{C['amber']}"/>
    <!-- header -->
    <text x="{card_x + card_w/2}" y="{card_y + 38}" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="22" fill="{C['white']}" letter-spacing="6">OUR RATES</text>
  </g>''')

    # Line items
    rows = [
        ("01", "SELF-SERVICE",         "Per load",      "$3.50"),
        ("02", "WASH &amp; FOLD",       "Per pound",     "$1.50"),
        ("03", "PICKUP &amp; DELIVERY", "Min. 10 lb",    "FREE"),
        ("04", "COMMERCIAL",            "Custom quote",  "B2B"),
        ("05", "IRONING &amp; PRESSING","Per item",      "$3.00"),
    ]
    row_h = 88
    start_y = card_y + 100
    for i, (num, name, sub, price) in enumerate(rows):
        y = start_y + i * row_h
        inner.append(f'''
  <g>
    <text x="{card_x + 32}" y="{y + 32}" font-family="Georgia, serif" font-size="32" font-weight="300" fill="{C['amber']}" opacity="0.85">{num}</text>
    <text x="{card_x + 88}" y="{y + 22}" font-family="sans-serif" font-size="14" font-weight="800" fill="{C['ink']}" letter-spacing="1.5">{name}</text>
    <text x="{card_x + 88}" y="{y + 42}" font-family="sans-serif" font-size="11" fill="{C['gray_md']}">{sub}</text>
    <text x="{card_x + card_w - 32}" y="{y + 36}" text-anchor="end" font-family="Georgia, serif" font-weight="800" font-size="24" fill="{C['brand']}">{price}</text>
  </g>''')
        if i < len(rows) - 1:
            inner.append(f'<line x1="{card_x + 32}" y1="{y + 70}" x2="{card_x + card_w - 32}" y2="{y + 70}" stroke="{C["linen_low"]}" stroke-width="1" opacity="0.4"/>')

    # Footer note
    inner.append(f'''
  <text x="{card_x + card_w/2}" y="{card_y + card_h - 26}" text-anchor="middle" font-family="sans-serif" font-size="10" fill="{C['gray_md']}" letter-spacing="3">TRANSPARENT · NO HIDDEN FEES</text>''')

    # Small coins scattered at the base
    def coin(x, y, r, label="$"):
        return f'''
  <g transform="translate({x},{y})" filter="url(#ds-tight)">
    <circle r="{r}" fill="{C['amber']}"/>
    <circle r="{r - 3}" fill="{C['amber_dk']}" opacity="0.3"/>
    <circle r="{r - 5}" fill="none" stroke="{C['amber_dk']}" stroke-width="1" opacity="0.6"/>
    <text x="0" y="{r * 0.35}" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="{int(r * 1.1)}" fill="{C['brand_dark']}">{label}</text>
  </g>'''
    inner.append(coin(1020, 800, 26))
    inner.append(coin(1080, 820, 20))
    inner.append(coin(1135, 805, 18))
    inner.append(coin(1490, 815, 24, "¢"))

    return svg_wrap("\n".join(inner),
                    "Spin It Up Laundry — Pricing",
                    "Service rate card listing all five services with transparent pricing, plus a sample receipt and coins")


# ──────────────────────────────────────────────────────────────────
# 3. ABOUT — Avondale storefront at night, warm windows, signage.
# ──────────────────────────────────────────────────────────────────
def about():
    inner = []

    # Streetlight beam coming down from upper-right
    inner.append(f'''
  <g opacity="0.18">
    <path d="M 1520 60 L 1600 60 L 1600 600 L 1450 800 Z" fill="{C['bg_warm']}"/>
    <circle cx="1540" cy="80" r="40" fill="{C['amber_lt']}" filter="url(#glow-amber)"/>
  </g>
  <!-- streetlight pole -->
  <line x1="1550" y1="80" x2="1550" y2="850" stroke="{C['chrome_dark']}" stroke-width="3" opacity="0.7"/>
  <path d="M 1538 78 Q 1550 50 1562 78" fill="none" stroke="{C['chrome_dark']}" stroke-width="3" opacity="0.7"/>
  <circle cx="1550" cy="80" r="14" fill="{C['amber_lt']}"/>
  <circle cx="1550" cy="80" r="8" fill="{C['white']}"/>''')

    # Sidewalk in front
    inner.append(f'''
  <rect x="{RX}" y="780" width="{1600 - RX}" height="120" fill="#1A2A4A" opacity="0.7"/>
  <line x1="{RX}" y1="780" x2="1600" y2="780" stroke="{C['gray_dk']}" stroke-width="1" opacity="0.6"/>
  <!-- sidewalk tile lines -->
  <g stroke="{C['gray_dk']}" stroke-width="1" opacity="0.35">
    <line x1="{RX + 70}" y1="780" x2="{RX + 60}" y2="900"/>
    <line x1="{RX + 200}" y1="780" x2="{RX + 195}" y2="900"/>
    <line x1="{RX + 330}" y1="780" x2="{RX + 332}" y2="900"/>
    <line x1="{RX + 460}" y1="780" x2="{RX + 470}" y2="900"/>
    <line x1="{RX + 590}" y1="780" x2="{RX + 610}" y2="900"/>
  </g>''')

    # Brick building facade
    bx, by, bw, bh = RX + 30, 130, 660, 650
    inner.append(f'''
  <!-- back wall (slightly darker) -->
  <rect x="{bx - 10}" y="{by - 10}" width="{bw + 20}" height="{bh + 10}" fill="{C['brick_dk']}"/>
  <!-- brick facade -->
  <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="url(#brickPattern)"/>
  <!-- subtle warm wash on the brick (from the streetlight) -->
  <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="{C['bg_warm']}" opacity="0.10"/>
  <!-- top cornice / parapet -->
  <rect x="{bx - 14}" y="{by - 18}" width="{bw + 28}" height="18" fill="{C['brick_dk']}"/>
  <rect x="{bx - 6}" y="{by - 22}" width="{bw + 12}" height="6" fill="{C['brick_lt']}" opacity="0.7"/>
  <!-- bottom kick / base of building -->
  <rect x="{bx - 14}" y="{by + bh - 28}" width="{bw + 28}" height="28" fill="{C['brick_dk']}"/>''')

    # Signage band — "SPIN IT UP LAUNDRY"
    sign_y = by + 70
    sign_h = 70
    inner.append(f'''
  <g filter="url(#ds-tight)">
    <rect x="{bx + 20}" y="{sign_y}" width="{bw - 40}" height="{sign_h}" fill="{C['brand_dark']}" stroke="{C['amber']}" stroke-width="3"/>
    <rect x="{bx + 28}" y="{sign_y + 8}" width="{bw - 56}" height="{sign_h - 16}" fill="none" stroke="{C['amber_lt']}" stroke-width="1" opacity="0.5"/>
    <text x="{bx + bw/2}" y="{sign_y + 38}" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="32" fill="{C['amber_lt']}" letter-spacing="6">SPIN IT UP</text>
    <text x="{bx + bw/2}" y="{sign_y + 60}" text-anchor="middle" font-family="sans-serif" font-size="11" fill="{C['white']}" letter-spacing="8" opacity="0.85">LAUNDRY · AVONDALE</text>
  </g>
  <!-- warm glow behind signage -->
  <ellipse cx="{bx + bw/2}" cy="{sign_y + sign_h/2}" rx="{bw/2 + 20}" ry="50" fill="{C['amber_lt']}" opacity="0.15" filter="url(#glow-amber)"/>''')

    # Two large storefront windows below the sign, showing warm interior
    win_y = sign_y + sign_h + 24
    win_w = (bw - 60) / 2 - 10
    win_h = bh - (win_y - by) - 50

    def storefront_window(wx):
        return f'''
  <g>
    <!-- frame -->
    <rect x="{wx - 4}" y="{win_y - 4}" width="{win_w + 8}" height="{win_h + 8}" fill="{C['chrome_dark']}"/>
    <!-- glass -->
    <rect x="{wx}" y="{win_y}" width="{win_w}" height="{win_h}" fill="url(#windowLight)"/>
    <!-- mullion -->
    <line x1="{wx + win_w/2}" y1="{win_y}" x2="{wx + win_w/2}" y2="{win_y + win_h}" stroke="{C['chrome_dark']}" stroke-width="4"/>
    <line x1="{wx}" y1="{win_y + win_h/2}" x2="{wx + win_w}" y2="{win_y + win_h/2}" stroke="{C['chrome_dark']}" stroke-width="3"/>
    <!-- interior: washing machines visible (silhouettes) -->
    <g opacity="0.55">
      <rect x="{wx + 16}" y="{win_y + win_h - 220}" width="50" height="180" rx="6" fill="{C['chrome_dark']}"/>
      <circle cx="{wx + 41}" cy="{win_y + win_h - 130}" r="20" fill="{C['glass_low']}"/>
      <rect x="{wx + 78}" y="{win_y + win_h - 220}" width="50" height="180" rx="6" fill="{C['chrome_dark']}"/>
      <circle cx="{wx + 103}" cy="{win_y + win_h - 130}" r="20" fill="{C['glass_low']}"/>
      <rect x="{wx + 140}" y="{win_y + win_h - 220}" width="50" height="180" rx="6" fill="{C['chrome_dark']}"/>
      <circle cx="{wx + 165}" cy="{win_y + win_h - 130}" r="20" fill="{C['glass_low']}"/>
      <rect x="{wx + 202}" y="{win_y + win_h - 220}" width="50" height="180" rx="6" fill="{C['chrome_dark']}"/>
      <circle cx="{wx + 227}" cy="{win_y + win_h - 130}" r="20" fill="{C['glass_low']}"/>
    </g>
    <!-- glass highlight / reflection -->
    <path d="M {wx + 8} {win_y + 8} L {wx + 60} {win_y + 8} L {wx + 30} {win_y + 80} L {wx + 8} {win_y + 60} Z" fill="#FFFFFF" opacity="0.18"/>
    <!-- warm overall glow on the glass -->
    <rect x="{wx}" y="{win_y}" width="{win_w}" height="{win_h}" fill="{C['bg_warm']}" opacity="0.18"/>
  </g>'''

    inner.append(storefront_window(bx + 30))
    inner.append(storefront_window(bx + 30 + win_w + 20))

    # Door between windows? Actually let me skip door - the storefront is the two windows
    # Add an "OPEN" sign hanging in one of the windows
    inner.append(f'''
  <g transform="translate({bx + 30 + win_w + 20 + win_w - 80}, {win_y + 30})">
    <line x1="40" y1="-20" x2="40" y2="0" stroke="{C['chrome_dark']}" stroke-width="1"/>
    <rect x="0" y="0" width="80" height="30" rx="4" fill="{C['coral']}"/>
    <text x="40" y="20" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="14" fill="{C['white']}" letter-spacing="4">OPEN</text>
  </g>''')

    # Light spill on sidewalk in front of the windows (warm pools)
    inner.append(f'''
  <g opacity="0.30">
    <ellipse cx="{bx + 30 + win_w/2}" cy="800" rx="{win_w * 0.55}" ry="22" fill="{C['amber_lt']}"/>
    <ellipse cx="{bx + 30 + win_w + 20 + win_w/2}" cy="800" rx="{win_w * 0.55}" ry="22" fill="{C['amber_lt']}"/>
  </g>''')

    # Address plaque
    inner.append(f'''
  <g transform="translate({bx - 12}, {by + bh - 22})" filter="url(#ds-tight)">
    <rect x="0" y="0" width="120" height="36" fill="{C['brand_dark']}" stroke="{C['amber']}" stroke-width="1.5"/>
    <text x="60" y="14" text-anchor="middle" font-family="sans-serif" font-size="7" font-weight="700" fill="{C['amber_lt']}" letter-spacing="2">ESTABLISHED</text>
    <text x="60" y="30" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="14" fill="{C['white']}">AVONDALE</text>
  </g>''')

    return svg_wrap("\n".join(inner),
                    "About Spin It Up Laundry",
                    "Brick storefront of the Avondale laundromat at night, with warm-lit windows showing washing machines inside")


# ──────────────────────────────────────────────────────────────────
# 4. CONTACT — stylized neighborhood map + pin + contact card.
# ──────────────────────────────────────────────────────────────────
def contact():
    inner = []

    # Map panel
    mx, my, mw, mh = RX + 30, 140, 660, 620
    inner.append(f'''
  <g filter="url(#ds-soft)">
    <!-- map background -->
    <rect x="{mx}" y="{my}" width="{mw}" height="{mh}" rx="14" fill="url(#mapGrad)" stroke="{C['brand_lt']}" stroke-width="1" opacity="1"/>
  </g>''')

    # Map streets — irregular grid suggesting a Chicago neighborhood
    inner.append('<g stroke="#3A5688" stroke-width="14" stroke-linecap="round" fill="none" opacity="0.55">')
    # Diagonal grand avenue (suggests Milwaukee Ave / Elston which cut across Avondale's grid)
    inner.append(f'<path d="M {mx + 40} {my + mh - 60} L {mx + mw - 60} {my + 80}"/>')
    # Horizontal streets
    for y_off in [120, 230, 340, 460]:
        inner.append(f'<line x1="{mx + 20}" y1="{my + y_off}" x2="{mx + mw - 20}" y2="{my + y_off}"/>')
    # Vertical streets
    for x_off in [120, 280, 440, 560]:
        inner.append(f'<line x1="{mx + x_off}" y1="{my + 30}" x2="{mx + x_off}" y2="{my + mh - 30}"/>')
    inner.append('</g>')

    # Inner thinner street lines (light secondary streets)
    inner.append('<g stroke="#5478A0" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.35">')
    for y_off in [70, 175, 285, 400, 530]:
        inner.append(f'<line x1="{mx + 20}" y1="{my + y_off}" x2="{mx + mw - 20}" y2="{my + y_off}" stroke-dasharray="1 3"/>')
    inner.append('</g>')

    # A few small "block" rectangles suggesting buildings
    inner.append(f'''
  <g fill="#1F345C" opacity="0.6">
    <rect x="{mx + 60}" y="{my + 60}" width="40" height="40" rx="2"/>
    <rect x="{mx + 160}" y="{my + 150}" width="60" height="36" rx="2"/>
    <rect x="{mx + 320}" y="{my + 250}" width="50" height="50" rx="2"/>
    <rect x="{mx + 470}" y="{my + 180}" width="40" height="30" rx="2"/>
    <rect x="{mx + 150}" y="{my + 400}" width="80" height="40" rx="2"/>
    <rect x="{mx + 400}" y="{my + 480}" width="50" height="50" rx="2"/>
  </g>''')

    # The big amber location pin — central, with pulse rings
    pin_x = mx + mw / 2 + 30
    pin_y = my + mh / 2 - 20
    inner.append(f'''
  <g transform="translate({pin_x}, {pin_y})">
    <!-- pulse rings -->
    <circle r="60" fill="none" stroke="{C['amber']}" stroke-width="2" opacity="0.25"/>
    <circle r="44" fill="none" stroke="{C['amber']}" stroke-width="2" opacity="0.4"/>
    <circle r="28" fill="{C['amber']}" opacity="0.18"/>
    <!-- glow -->
    <circle r="50" fill="{C['amber_lt']}" opacity="0.35" filter="url(#glow-amber)"/>
    <!-- pin shape (teardrop) -->
    <g filter="url(#ds-soft)">
      <path d="M 0 -50 Q 26 -50 26 -22 Q 26 0 0 32 Q -26 0 -26 -22 Q -26 -50 0 -50 Z" fill="{C['amber']}" stroke="{C['amber_dk']}" stroke-width="2"/>
      <circle cx="0" cy="-26" r="10" fill="{C['white']}"/>
      <circle cx="0" cy="-26" r="5" fill="{C['amber_dk']}"/>
      <!-- highlight -->
      <ellipse cx="-8" cy="-40" rx="6" ry="3" fill="{C['white']}" opacity="0.5"/>
    </g>
  </g>''')

    # "YOU ARE HERE" label below pin
    inner.append(f'''
  <g transform="translate({pin_x}, {pin_y + 60})">
    <rect x="-70" y="0" width="140" height="32" rx="16" fill="{C['white']}" filter="url(#ds-tight)"/>
    <text x="0" y="20" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="800" fill="{C['ink']}" letter-spacing="2">SPIN IT UP</text>
  </g>''')

    # Compass rose
    inner.append(f'''
  <g transform="translate({mx + mw - 60}, {my + 60})" opacity="0.65">
    <circle r="22" fill="none" stroke="{C['amber_lt']}" stroke-width="1.5"/>
    <path d="M 0 -22 L 4 0 L 0 22 L -4 0 Z" fill="{C['amber_lt']}"/>
    <path d="M -22 0 L 0 -4 L 22 0 L 0 4 Z" fill="{C['amber_lt']}" opacity="0.5"/>
    <text x="0" y="-26" text-anchor="middle" font-family="sans-serif" font-size="9" font-weight="800" fill="{C['amber_lt']}">N</text>
  </g>''')

    # Contact card floating in the top-left of the right zone
    cx_card, cy_card, cw_card, ch_card = RX - 30, 150, 220, 380
    inner.append(f'''
  <g transform="translate({cx_card}, {cy_card})" filter="url(#ds-soft)">
    <rect x="0" y="0" width="{cw_card}" height="{ch_card}" rx="14" fill="{C['white']}"/>
    <rect x="0" y="0" width="{cw_card}" height="60" rx="14" fill="{C['brand']}"/>
    <rect x="0" y="46" width="{cw_card}" height="14" fill="{C['brand']}"/>
    <rect x="0" y="58" width="{cw_card}" height="2" fill="{C['amber']}"/>
    <text x="{cw_card/2}" y="38" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="16" fill="{C['white']}" letter-spacing="3">GET IN TOUCH</text>

    <!-- phone -->
    <g transform="translate(20, 88)">
      <circle cx="14" cy="14" r="14" fill="{C['amber']}" opacity="0.18"/>
      <path d="M 7 8 Q 7 6 9 6 L 12 6 Q 14 6 14 8 L 15 13 Q 15 14 14 15 L 12 16 Q 14 19 17 21 L 18 19 Q 19 18 20 18 L 25 19 Q 27 19 27 21 L 27 24 Q 27 26 25 26 Q 13 26 7 14 Q 7 12 7 8 Z" fill="{C['amber']}"/>
      <text x="42" y="10" font-family="sans-serif" font-size="9" font-weight="700" fill="{C['gray_md']}" letter-spacing="1.5">CALL</text>
      <text x="42" y="26" font-family="sans-serif" font-size="13" font-weight="800" fill="{C['ink']}">(773) 555-WASH</text>
    </g>

    <!-- email -->
    <g transform="translate(20, 156)">
      <circle cx="14" cy="14" r="14" fill="{C['amber']}" opacity="0.18"/>
      <rect x="6" y="9" width="16" height="11" rx="1.5" fill="none" stroke="{C['amber']}" stroke-width="1.8"/>
      <path d="M 6 10 L 14 16 L 22 10" fill="none" stroke="{C['amber']}" stroke-width="1.8"/>
      <text x="42" y="10" font-family="sans-serif" font-size="9" font-weight="700" fill="{C['gray_md']}" letter-spacing="1.5">EMAIL</text>
      <text x="42" y="26" font-family="sans-serif" font-size="11" font-weight="700" fill="{C['ink']}">hi@spinituplaundry.net</text>
    </g>

    <!-- hours -->
    <g transform="translate(20, 224)">
      <circle cx="14" cy="14" r="14" fill="{C['amber']}" opacity="0.18"/>
      <circle cx="14" cy="14" r="8" fill="none" stroke="{C['amber']}" stroke-width="1.8"/>
      <line x1="14" y1="9" x2="14" y2="14" stroke="{C['amber']}" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="14" y1="14" x2="18" y2="17" stroke="{C['amber']}" stroke-width="1.8" stroke-linecap="round"/>
      <text x="42" y="10" font-family="sans-serif" font-size="9" font-weight="700" fill="{C['gray_md']}" letter-spacing="1.5">HOURS</text>
      <text x="42" y="26" font-family="sans-serif" font-size="12" font-weight="800" fill="{C['ink']}">Daily 6 AM – 10 PM</text>
    </g>

    <!-- address -->
    <g transform="translate(20, 292)">
      <circle cx="14" cy="14" r="14" fill="{C['amber']}" opacity="0.18"/>
      <path d="M 14 6 Q 19 6 19 11 Q 19 16 14 22 Q 9 16 9 11 Q 9 6 14 6 Z" fill="none" stroke="{C['amber']}" stroke-width="1.8"/>
      <circle cx="14" cy="11" r="2" fill="{C['amber']}"/>
      <text x="42" y="10" font-family="sans-serif" font-size="9" font-weight="700" fill="{C['gray_md']}" letter-spacing="1.5">VISIT</text>
      <text x="42" y="26" font-family="sans-serif" font-size="11" font-weight="700" fill="{C['ink']}">2845 N Sawyer Ave</text>
      <text x="42" y="40" font-family="sans-serif" font-size="11" fill="{C['gray_md']}">Avondale, Chicago</text>
    </g>
  </g>''')

    return svg_wrap("\n".join(inner),
                    "Contact Spin It Up Laundry",
                    "Stylized map of the Avondale neighborhood with a pin marking the laundromat, beside a contact card with phone, email, hours, and address")


# ──────────────────────────────────────────────────────────────────
# 5. FAQ — overlapping speech bubbles with Q&A snippets.
# ──────────────────────────────────────────────────────────────────
def faq():
    inner = []

    # A subtle giant "?" in the background
    inner.append(f'''
  <g opacity="0.08" font-family="Georgia, serif" font-weight="800" font-size="600" fill="{C['amber']}">
    <text x="1380" y="700" text-anchor="middle">?</text>
  </g>''')

    # Bubble factory
    def bubble(x, y, w, h, fill, tail_side, q_or_a, label, line1, line2):
        # tail_side: 'left' or 'right'
        if tail_side == 'left':
            tail = f'<path d="M {x + 30} {y + h} L {x + 16} {y + h + 22} L {x + 56} {y + h} Z" fill="{fill}"/>'
        else:
            tail = f'<path d="M {x + w - 30} {y + h} L {x + w - 16} {y + h + 22} L {x + w - 56} {y + h} Z" fill="{fill}"/>'

        icon_fill = C['white'] if 'A' in q_or_a else C['amber']
        icon_text_color = C['brand_dark'] if 'A' in q_or_a else C['white']
        # Q/A indicator
        if q_or_a == 'Q':
            qa_icon = f'''
    <circle cx="{x + 32}" cy="{y + 32}" r="18" fill="{C['amber']}"/>
    <text x="{x + 32}" y="{y + 39}" text-anchor="middle" font-family="Georgia, serif" font-weight="800" font-size="20" fill="{C['white']}">?</text>'''
        else:
            qa_icon = f'''
    <circle cx="{x + 32}" cy="{y + 32}" r="18" fill="{C['mint']}"/>
    <path d="M {x + 24} {y + 32} L {x + 30} {y + 38} L {x + 41} {y + 26}" stroke="{C['white']}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'''

        text_color = C['white'] if fill == C['brand'] else C['ink']
        label_color = C['amber_lt'] if fill == C['brand'] else C['gray_md']

        return f'''
  <g filter="url(#ds-soft)">
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}"/>
    {tail}
    {qa_icon}
    <text x="{x + 62}" y="{y + 24}" font-family="sans-serif" font-size="9" font-weight="800" fill="{label_color}" letter-spacing="2">{label}</text>
    <text x="{x + 62}" y="{y + 46}" font-family="sans-serif" font-size="14" font-weight="700" fill="{text_color}">{line1}</text>
    {f'<text x="{x + 62}" y="{y + 66}" font-family="sans-serif" font-size="13" fill="{text_color}" opacity="0.85">{line2}</text>' if line2 else ''}
  </g>'''

    # Four overlapping bubbles arranged like a chat thread
    inner.append(bubble(910,  155, 360, 88, C['off_white'], 'left',  'Q',
                       "QUESTION",  "How long does", "wash &amp; fold take?"))
    inner.append(bubble(1140, 290, 380, 88, C['brand'], 'right', 'A',
                       "ANSWER", "About 4 hours for", "most orders. Same day."))
    inner.append(bubble(890,  430, 350, 88, C['off_white'], 'left',  'Q',
                       "QUESTION",  "Do you accept", "EBT?"))
    inner.append(bubble(1180, 565, 360, 88, C['brand'], 'right', 'A',
                       "ANSWER", "Yes — cash, card,", "and EBT all work."))
    inner.append(bubble(940,  700, 350, 88, C['off_white'], 'left',  'Q',
                       "QUESTION",  "What about", "delicate items?"))

    # A small "more answers below" hint at the bottom
    inner.append(f'''
  <g transform="translate(1350, 750)">
    <text x="0" y="0" font-family="sans-serif" font-size="11" font-weight="700" fill="{C['amber_lt']}" letter-spacing="2" opacity="0.7">MORE ANSWERS</text>
    <path d="M -8 14 L 130 14" stroke="{C['amber_lt']}" stroke-width="1.5" opacity="0.5"/>
    <path d="M 122 8 L 130 14 L 122 20" fill="none" stroke="{C['amber_lt']}" stroke-width="1.5" stroke-linecap="round" opacity="0.7"/>
  </g>''')

    # A few floating ❓ marks for atmosphere
    inner.append(f'''
  <g font-family="Georgia, serif" font-weight="800" fill="{C['amber']}">
    <text x="1500" y="180" font-size="32" opacity="0.45">?</text>
    <text x="870" y="350" font-size="22" opacity="0.4">?</text>
    <text x="1490" y="490" font-size="26" opacity="0.5">?</text>
    <text x="880" y="630" font-size="20" opacity="0.4">?</text>
  </g>''')

    return svg_wrap("\n".join(inner),
                    "Spin It Up Laundry — Frequently Asked Questions",
                    "A series of overlapping speech bubbles representing common questions and answers in a chat-style layout")


# ──────────────────────────────────────────────────────────────────
# Render
# ──────────────────────────────────────────────────────────────────
files = {
    "hero-services.svg":  services_overview(),
    "hero-pricing.svg":   pricing(),
    "hero-about.svg":     about(),
    "hero-contact.svg":   contact(),
    "hero-faq.svg":       faq(),
}
for name, content in files.items():
    p = os.path.join(OUT_DIR, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ {name}  ({os.path.getsize(p):,} bytes)")
print(f"\n→ {OUT_DIR}")
