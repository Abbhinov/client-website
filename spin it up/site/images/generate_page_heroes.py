"""
Spin It Up Laundry — Page Hero Images (about, faq, pricing, contact, areas).
Same house style as generate_service_images_v2.py: 1600x900, deep-navy
gradient background with a warm upper-right glow, on-brand illustration on
the right (the left third stays calm for the text overlay). Sits behind a
dark overlay on the page, so compositions are clean and graphic.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

P = {
    "bg_top": "#0A1A3D", "bg_bot": "#142A55", "bg_glow": "#3A6FB0", "bg_warm": "#D89A55",
    "brand_dark": "#0B2447", "brand": "#19376D", "brand_lt": "#576CBC",
    "amber": "#E6A23C", "amber_dk": "#B07820", "amber_lt": "#F4C77F",
    "glass_hi": "#EAF3FF", "glass_mid": "#7BA4D6", "glass_low": "#1E3458",
    "off_white": "#F0F4F8", "white": "#FFFFFF", "ink": "#0A1A3D",
    "steel_hi": "#D7DEE8", "steel_mid": "#A8B5C5", "steel_low": "#3D4A5C",
}

DEFS = f"""
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{P['bg_top']}"/><stop offset="100%" stop-color="{P['bg_bot']}"/>
  </linearGradient>
  <radialGradient id="glow" cx="80%" cy="16%" r="70%">
    <stop offset="0%" stop-color="{P['bg_warm']}" stop-opacity="0.34"/>
    <stop offset="38%" stop-color="{P['bg_glow']}" stop-opacity="0.20"/>
    <stop offset="100%" stop-color="{P['bg_top']}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="vig" cx="50%" cy="48%" r="80%">
    <stop offset="58%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity="0.38"/>
  </radialGradient>
  <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{P['brand_lt']}"/><stop offset="55%" stop-color="{P['brand']}"/><stop offset="100%" stop-color="{P['brand_dark']}"/>
  </linearGradient>
  <linearGradient id="amber" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{P['amber_lt']}"/><stop offset="55%" stop-color="{P['amber']}"/><stop offset="100%" stop-color="{P['amber_dk']}"/>
  </linearGradient>
  <radialGradient id="glass" cx="36%" cy="28%" r="78%">
    <stop offset="0%" stop-color="{P['glass_hi']}" stop-opacity="0.95"/>
    <stop offset="55%" stop-color="{P['glass_mid']}" stop-opacity="0.7"/>
    <stop offset="100%" stop-color="{P['glass_low']}" stop-opacity="0.95"/>
  </radialGradient>
  <linearGradient id="steel" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{P['steel_hi']}"/><stop offset="50%" stop-color="{P['steel_mid']}"/><stop offset="100%" stop-color="{P['steel_low']}"/>
  </linearGradient>
  <linearGradient id="white" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{P['white']}"/><stop offset="100%" stop-color="#D9E2EC"/>
  </linearGradient>
  <filter id="ds" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="9"/><feOffset dy="12"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.30"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>"""

def doc(title, desc, body):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" '
        'preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="t d">\n'
        f'<title id="t">{title}</title>\n<desc id="d">{desc}</desc>\n'
        + DEFS +
        '\n<rect width="1600" height="900" fill="url(#bg)"/>'
        '\n<rect width="1600" height="900" fill="url(#glow)"/>'
        '\n<g opacity="0.05" stroke="' + P['bg_warm'] + '" stroke-width="1">'
        '<line x1="0" y1="180" x2="1600" y2="180"/><line x1="0" y1="360" x2="1600" y2="360"/>'
        '<line x1="0" y1="540" x2="1600" y2="540"/><line x1="0" y1="720" x2="1600" y2="720"/></g>\n'
        + body +
        '\n<rect width="1600" height="900" fill="url(#vig)"/>\n</svg>\n'
    )

def pin(cx, cy, r, fill="url(#amber)"):
    H = r * 2.3
    return (
        f'<g filter="url(#ds)">'
        f'<path d="M {cx-r},{cy} A {r},{r} 0 1 1 {cx+r},{cy} L {cx},{cy+H} Z" fill="{fill}"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r*0.42}" fill="{P["off_white"]}"/></g>'
    )

def building(x, base, w, h, fill="url(#panel)", cols=3, rows=4, wcol=P["glass_mid"]):
    s = [f'<rect x="{x}" y="{base-h}" width="{w}" height="{h}" rx="6" fill="{fill}"/>']
    gx, gy = w/(cols+1), h/(rows+1)
    ww, wh = gx*0.6, gy*0.55
    for r in range(rows):
        for c in range(cols):
            wx = x + gx*(c+1) - ww/2
            wy = (base-h) + gy*(r+1) - wh/2 + 6
            s.append(f'<rect x="{wx:.0f}" y="{wy:.0f}" width="{ww:.0f}" height="{wh:.0f}" rx="2" fill="{wcol}" opacity="0.85"/>')
    return "".join(s)

def house(x, base, w, bodyH, roofH, fill="url(#panel)", roof=P["brand_dark"]):
    top = base - bodyH
    return (
        f'<rect x="{x}" y="{top}" width="{w}" height="{bodyH}" rx="4" fill="{fill}"/>'
        f'<path d="M {x-12},{top} L {x+w/2},{top-roofH} L {x+w+12},{top} Z" fill="{roof}"/>'
        f'<rect x="{x+w*0.18}" y="{top+bodyH*0.30}" width="{w*0.22}" height="{bodyH*0.28}" fill="{P["glass_mid"]}" opacity="0.85"/>'
        f'<rect x="{x+w*0.58}" y="{top+bodyH*0.30}" width="{w*0.22}" height="{bodyH*0.28}" fill="{P["glass_mid"]}" opacity="0.85"/>'
        f'<rect x="{x+w*0.40}" y="{top+bodyH*0.55}" width="{w*0.20}" height="{bodyH*0.45}" fill="{P["amber"]}" opacity="0.9"/>'
    )

def bubble(x, y, w, h, fill, tail=True):
    t = (f'<path d="M {x+w*0.22},{y+h} l 0,40 l 40,-40 Z" fill="{fill}"/>') if tail else ""
    return f'<g filter="url(#ds)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h*0.28}" fill="{fill}"/>{t}</g>'

def qmark(cx, cy, size, color):
    return (
        f'<text x="{cx}" y="{cy}" font-family="Georgia, \'Times New Roman\', serif" '
        f'font-size="{size}" font-weight="700" fill="{color}" '
        f'text-anchor="middle" dominant-baseline="central">?</text>'
    )

def floor(yline=770):
    return (f'<rect x="0" y="{yline}" width="1600" height="{900-yline}" fill="#091532" opacity="0.5"/>'
            f'<line x1="0" y1="{yline}" x2="1600" y2="{yline}" stroke="{P["brand_lt"]}" stroke-width="1" opacity="0.25"/>')

# ── Scenes ─────────────────────────────────────────────────────────
def scene_about():
    b = [floor()]
    # storefront facade
    b.append('<g filter="url(#ds)">')
    b.append('<rect x="880" y="250" width="560" height="520" rx="10" fill="url(#panel)"/>')
    b.append('</g>')
    # awning (amber + offwhite stripes)
    aw = ['<g filter="url(#ds)">']
    for i in range(7):
        col = P["amber"] if i % 2 == 0 else P["off_white"]
        aw.append(f'<path d="M {900+i*80},300 l 80,0 l -16,60 l -80,0 Z" fill="{col}"/>')
    aw.append('</g>')
    b.append("".join(aw))
    b.append('<rect x="884" y="296" width="552" height="14" rx="4" fill="url(#steel)"/>')
    # shop windows with a washer
    b.append(f'<rect x="918" y="400" width="220" height="300" rx="8" fill="{P["glass_low"]}"/>')
    b.append(f'<rect x="930" y="412" width="196" height="276" rx="6" fill="url(#glass)" opacity="0.85"/>')
    b.append('<circle cx="1028" cy="560" r="74" fill="url(#steel)"/>')
    b.append(f'<circle cx="1028" cy="560" r="54" fill="url(#glass)"/>')
    b.append(f'<circle cx="1028" cy="560" r="54" fill="none" stroke="{P["steel_low"]}" stroke-width="6"/>')
    # door
    b.append(f'<rect x="1190" y="470" width="170" height="230" rx="6" fill="{P["glass_low"]}"/>')
    b.append(f'<rect x="1202" y="482" width="146" height="206" rx="4" fill="url(#glass)" opacity="0.8"/>')
    b.append(f'<rect x="1330" y="560" width="10" height="48" rx="5" fill="{P["steel_hi"]}"/>')
    # sign
    b.append(f'<rect x="960" y="330" width="380" height="48" rx="8" fill="{P["brand_dark"]}"/>')
    b.append(f'<circle cx="998" cy="354" r="16" fill="url(#amber)"/>')
    b.append(f'<rect x="1028" y="346" width="280" height="16" rx="8" fill="{P["off_white"]}" opacity="0.85"/>')
    return doc("About Spin It Up Laundry",
               "Illustration of the Spin It Up Laundry storefront in Avondale", "".join(b))

def scene_faq():
    b = []
    b.append(bubble(820, 250, 420, 240, "url(#panel)"))
    b.append(qmark(1030, 365, 150, P["off_white"]))
    b.append(bubble(1140, 470, 300, 180, "url(#amber)"))
    b.append(qmark(1290, 558, 110, P["brand_dark"]))
    b.append(bubble(700, 520, 250, 150, P["off_white"]))
    b.append(qmark(825, 593, 92, P["brand"]))
    return doc("Frequently Asked Questions",
               "Illustration of question-and-answer speech bubbles", "".join(b))

def scene_pricing():
    b = [floor()]
    # big price tag, slightly rotated
    b.append('<g transform="rotate(-12 1120 470)" filter="url(#ds)">')
    b.append('<path d="M 980,330 L 1230,330 L 1300,470 L 1230,610 L 980,610 Z" fill="url(#amber)"/>')
    b.append(f'<circle cx="1018" cy="392" r="26" fill="{P["brand_dark"]}"/>')
    b.append(f'<circle cx="1018" cy="392" r="11" fill="{P["amber_lt"]}"/>')
    b.append(f'<text x="1150" y="470" font-family="Georgia, serif" font-size="150" font-weight="700" '
             f'fill="{P["brand_dark"]}" text-anchor="middle" dominant-baseline="central">$</text>')
    b.append('</g>')
    # string to top
    b.append(f'<path d="M 1010,360 C 1030,250 1120,230 1180,210" fill="none" stroke="{P["off_white"]}" stroke-width="6" opacity="0.6"/>')
    # coin stack
    for i, cy in enumerate(range(700, 560, -34)):
        b.append(f'<ellipse cx="900" cy="{cy}" rx="78" ry="26" fill="url(#amber)"/>')
        b.append(f'<ellipse cx="900" cy="{cy}" rx="78" ry="26" fill="none" stroke="{P["amber_dk"]}" stroke-width="3"/>')
    b.append(f'<text x="900" y="560" font-family="Georgia, serif" font-size="40" font-weight="700" '
             f'fill="{P["brand_dark"]}" text-anchor="middle" dominant-baseline="central">$</text>')
    return doc("Laundry Pricing",
               "Illustration of a price tag and a stack of coins", "".join(b))

def street_grid(ox, oy, w, h, n=4, m=3, color=None, op=0.5):
    color = color or P["brand_lt"]
    s = [f'<g stroke="{color}" stroke-width="3" opacity="{op}" fill="none">']
    for i in range(n+1):
        y = oy + h*i/n
        s.append(f'<line x1="{ox}" y1="{y:.0f}" x2="{ox+w}" y2="{y:.0f}"/>')
    for j in range(m+1):
        x = ox + w*j/m
        s.append(f'<line x1="{x:.0f}" y1="{oy}" x2="{x:.0f}" y2="{oy+h}"/>')
    s.append('</g>')
    return "".join(s)

def scene_contact():
    b = [floor()]
    b.append(street_grid(760, 300, 760, 440, n=4, m=4, op=0.45))
    # a couple of block fills
    b.append(f'<rect x="950" y="490" width="180" height="92" rx="6" fill="url(#panel)" opacity="0.85"/>')
    b.append(f'<rect x="1330" y="345" width="130" height="90" rx="6" fill="url(#panel)" opacity="0.7"/>')
    # big pin at an intersection
    b.append(pin(1140, 415, 70))
    # small chat bubble
    b.append(bubble(820, 300, 150, 96, P["off_white"], tail=True))
    b.append(f'<circle cx="862" cy="346" r="9" fill="{P["brand"]}"/><circle cx="896" cy="346" r="9" fill="{P["brand"]}"/><circle cx="930" cy="346" r="9" fill="{P["brand"]}"/>')
    return doc("Contact Us",
               "Illustration of a map location pin on a street grid", "".join(b))

def skyline(seed, accent_i=1):
    """Row of buildings/houses for a neighborhood. Deterministic per seed."""
    base = 770
    b = [floor(base)]
    heights = [(seed*37 + i*53) % 170 + 150 for i in range(7)]
    x = 740
    for i, h in enumerate(heights):
        w = 110 + ((seed*13 + i*29) % 40)
        if (seed + i) % 3 == 0:
            b.append(house(x, base, w, h*0.7, 46, fill="url(#panel)"))
        else:
            cols = 2 + (i % 2)
            rows = 3 + (h > 250)
            fill = "url(#amber)" if i == accent_i else "url(#panel)"
            wcol = P["brand_dark"] if i == accent_i else P["glass_mid"]
            b.append(building(x, base, w, h, fill=fill, cols=cols, rows=rows, wcol=wcol))
        x += w + 18
    # location pin floating above the accent building
    b.append(pin(740 + sum(110 for _ in range(accent_i)) + 80, 250, 56))
    return b

def scene_area(name_title, seed, accent_i):
    return doc(f"Laundry services for {name_title}",
               f"Stylized neighborhood skyline representing {name_title}",
               "".join(skyline(seed, accent_i)))

def scene_areas_hub():
    b = [floor()]
    b.append(street_grid(700, 280, 840, 470, n=5, m=5, op=0.4))
    # scattered blocks
    blocks = [(820,560,150,80),(1050,400,170,90),(1300,540,150,80),(980,650,140,70),(1330,360,120,70)]
    for (x,y,w,h) in blocks:
        b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="url(#panel)" opacity="0.8"/>')
    # diagonal road
    b.append(f'<path d="M 700,300 L 1540,700" stroke="{P["amber"]}" stroke-width="8" opacity="0.45"/>')
    # several pins
    for (cx,cy,r) in [(900,430,52),(1170,520,60),(1380,440,48)]:
        b.append(pin(cx, cy, r))
    return doc("Service areas",
               "Illustration of a neighborhood map with location pins", "".join(b))

FILES = {
    "hero-about.svg":        scene_about(),
    "hero-faq.svg":          scene_faq(),
    "hero-pricing.svg":      scene_pricing(),
    "hero-contact.svg":      scene_contact(),
    "hero-areas.svg":        scene_areas_hub(),
    "hero-avondale.svg":     scene_area("Avondale", 3, 1),
    "hero-irving-park.svg":  scene_area("Irving Park", 7, 2),
    "hero-logan-square.svg": scene_area("Logan Square", 11, 3),
    "hero-hermosa.svg":      scene_area("Hermosa", 5, 0),
    "hero-albany-park.svg":  scene_area("Albany Park", 9, 4),
}

for fn, svg in FILES.items():
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", fn, len(svg), "bytes")
