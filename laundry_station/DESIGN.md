---
name: Laundry Station
description: A well-run workshop for serviced laundry, posted prices, and done-for-you routes.
colors:
  station-navy: "#0C479C"
  signal-amber: "#FFB020"
  signal-blue: "#066FE5"
  deep-navy: "#07132B"
  ink-blue: "#042E74"
  pale-blue: "#F3F7FC"
  soft-blue: "#E5EEF8"
  line-blue: "#CFDEF0"
  warm-cream: "#FEF7E7"
  ice-blue: "#E8F2FF"
  map-blue: "#EAF3FF"
  warm-map: "#FFF5DD"
  wash-sky: "#DDF1FF"
  rinse-mint: "#E7FAEF"
  soft-lilac: "#F0ECFF"
  coral-wash: "#FFE9DF"
  lemon-foam: "#FFF8D8"
  aqua-rinse: "#DFF8F7"
  rose-linen: "#FFEAF1"
  blue-border: "#8DCBFF"
  mint-border: "#8CDDAF"
  lilac-border: "#B9A9FF"
  coral-border: "#FFB394"
  lemon-border: "#D8C064"
  rose-border: "#F4A8C2"
  cobalt: "#1358B8"
  royal-blue: "#0C6FE8"
  deep-service-blue: "#17479E"
  blue-ink: "#073A86"
  deep-gold: "#D89500"
  rich-yellow: "#F7BD16"
  surface-blue: "#E4F2FF"
  surface-gold: "#FFF1BC"
  surface-mint: "#DCF7E9"
  surface-lilac: "#EAE5FF"
  surface-coral: "#FFE1D4"
  shadow-black-28: "rgba(0, 0, 0, .28)"
  white-overlay-12: "rgba(255, 255, 255, .12)"
  white-overlay-22: "rgba(255,255,255,.22)"
  white-overlay-32: "rgba(255, 255, 255, .32)"
  white-overlay-35: "rgba(255, 255, 255, .35)"
  white-overlay-82: "rgba(255, 255, 255, .82)"
  white-overlay-90: "rgba(255,255,255,.9)"
  white-overlay-92: "rgba(255,255,255,.92)"
typography:
  display:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(2.125rem, 1.44rem + 2.85vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(1.5rem, 1.32rem + .7vw, 2rem)"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0"
  page-title:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(2rem, 1.55rem + 1.7vw, 2.75rem)"
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: "0"
  title:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(1.25rem, 1.17rem + .35vw, 1.5rem)"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0"
  subhead:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "0"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: "0"
  lede:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "clamp(1.0625rem, 1rem + .25vw, 1.1875rem)"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0"
  body-large:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0"
  small:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
  micro:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "0"
  nav:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0"
  step-number:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0"
  label:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 600
    lineHeight: 1
rounded:
  sm: "6px"
  md: "10px"
  lg: "14px"
  full: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  section-mobile: "48px"
  section-tablet: "64px"
  section-desktop: "96px"
components:
  button-primary:
    backgroundColor: "{colors.signal-amber}"
    textColor: "{colors.deep-navy}"
    rounded: "{rounded.md}"
    padding: "14px 24px"
    height: "48px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.station-navy}"
    rounded: "{rounded.md}"
    padding: "14px 24px"
    height: "48px"
  card-service:
    backgroundColor: "#FFFFFF"
    textColor: "{colors.ink-blue}"
    rounded: "{rounded.lg}"
    padding: "24px"
---

# Design System: Laundry Station

## Overview

**Creative North Star: "The Well-Run Workshop"**

Laundry Station should feel orderly, repaired, direct, and local. The homepage uses a shop-floor visual language: white and pale-blue work surfaces, navy structural type, squared controls with softened corners, and visible facts instead of promotional noise.

The design is intentionally plain-spoken. It does not try to look like a boutique service or a discount laundromat. The page earns trust by making service paths, posted prices, map context, and unresolved owner inputs easy to see.

**Key Characteristics:**
- Alternating white and pale-blue bands with one dark footer.
- Amber appears only on Schedule Pickup.
- Service cards, Board tables, chips, and FAQ rows form the reusable component base.
- Unknown owner values render as dashed amber staging gaps, never as guessed copy.

## Colors

The palette is a bright wash-day system with controlled saturated contrast: blue remains the brand anchor, cobalt and royal blue can own important homepage bands, rich yellow/deep gold support action and process moments, and light mint, lilac, coral, lemon, aqua, and rose tints separate quieter sections. Avoid black, brown, espresso, and muddy dark surfaces.

### Primary
- **Station Navy**: Main brand color for structure, headings, nav emphasis, and labels.
- **Deep Navy**: Body ink on bright action fills and the dark footer ground.

### Secondary
- **Signal Blue**: Links, line icons, focus rings, and informational emphasis.

### Tertiary
- **Signal Amber**: Conversion action fill only. It is not used for headings, body text, decorative badges, or general emphasis.

### Neutral
- **Pale Blue**: Alternating section bands and map/placeholder grounds.
- **Soft Blue**: Final conversion band and table headers.
- **Line Blue**: Decorative dividers, card borders, and table rules.
- **Ink Blue**: Secondary text on light surfaces.

### Named Rules

**The Amber Budget Rule.** Amber is for Schedule Pickup only, with deep navy text. Never use white text on amber.

**The Posted Facts Rule.** Do not use ratings, review counts, availability numbers, or savings colors unless the fact exists and renders on the page.

## Typography

**Display Font:** Archivo, system-ui, sans-serif  
**Body Font:** Inter, system-ui, sans-serif

**Character:** Archivo reads like sturdy signage. Inter keeps dense service copy and Spanish expansion legible.

### Hierarchy
- **Display** (Archivo 700, responsive 34-56px, 1.08): Homepage H1 only.
- **Headline** (Archivo 600, responsive 24-32px, 1.2): Section headings.
- **Title** (Archivo 600, responsive 20-24px, 1.3): Service card titles and subheads.
- **Body** (Inter 400, 16-17px, 1.65): Paragraphs, service descriptions, FAQ answers, and footer copy.
- **Label** (Archivo 600, 16px, 1): Buttons and table emphasis.

### Named Rules

**The No Eyebrow Rule.** Headings stand alone. Do not add kicker, overline, or label text above a heading.

## Layout

Pages use full-width bands with a centered content container capped at 1200px. Desktop sections use 96px vertical padding, tablets use 64px, and mobile uses 48px. The homepage alternates surfaces from hero to footer so separate blocks do not need decorative dividers.

Desktop supports three-column service and pillar grids. Tablet and mobile collapse to single-column prose and stacked cards where clarity matters. The Board table becomes stacked label/value cards below 600px so pricing data never hides behind horizontal scroll.

## Elevation & Depth

The system is flat by default. Borders and tonal surfaces do most of the depth work. Shadows appear only for state or overlay: card hover, sticky header, mobile action bar, and nav dropdowns.

### Shadow Vocabulary
- **Hover lift** (`0 1px 2px rgba(7, 19, 43, .06)`): Service cards on hover.
- **Sticky lift** (`0 2px 8px rgba(7, 19, 43, .08)`): Header and mobile action bar.
- **Overlay lift** (`0 8px 24px rgba(7, 19, 43, .10)`): Service dropdown.

### Named Rules

**The Flat-At-Rest Rule.** Cards and tables rest on a hairline border. They lift only when interaction or overlay state requires it.

## Shapes

Corners are lightly rounded, never pill-shaped except for non-button utility marks. Small controls use 6px, buttons use 10px, cards/tables/media frames use 14px. Borders are thin and blue-tinted, with stronger control borders for interactive elements.

## Components

### Buttons
- **Shape:** Equipment-like rounded rectangle (10px).
- **Primary:** Signal Amber fill, Deep Navy text, 14px/24px padding, 48px minimum height.
- **Hover / Focus:** Amber darkens slightly on hover; focus uses a 3px Signal Blue outline.
- **Secondary:** Transparent fill, Station Navy label, stronger blue border, same metrics as primary.

### Chips
- **Style:** Pale surface fill, Line Blue border, small Inter text.
- **Use:** Language, payment, hours, and staging facts. Linked chips receive a 44px tap target.

### Cards / Containers
- **Corner Style:** 14px.
- **Background:** White cards, usually on pale-blue bands.
- **Shadow Strategy:** Border at rest, soft lift on hover.
- **Internal Padding:** 24px desktop/tablet, 20px mobile.

### Navigation
- **Style:** Sticky white header with a bottom hairline and dropdown service menu.
- **States:** Hover uses Station Navy text and a Signal Blue underline.
- **Mobile:** Hamburger opens a stacked menu; a bottom action bar keeps Call and Schedule Pickup visible.

### The Board
- **Style:** Semantic table in a rounded white container, soft-blue header row, horizontal rules only.
- **Mobile:** Rows stack into label/value cards. No horizontal scroll.

### FAQ
- **Style:** Native details/summary rows with bottom borders only.
- **State:** Chevron rotates on open; answers remain in the DOM for search and accessibility.

### Staging Tokens
- **Style:** Dashed amber border, pale amber fill, monospace label.
- **Use:** Owner-supplied hard facts that must not be guessed.

## Do's and Don'ts

### Do:
- **Do** keep the homepage answer-first and local.
- **Do** use the supplied logo and replace photo placeholders with real Laundry Station photography.
- **Do** keep amber rare enough that Schedule Pickup is visible at a glance.
- **Do** leave owner-supplied unknowns as visible staging gaps until confirmed.

### Don't:
- **Don't** add star ratings, review counts, availability figures, savings percentages, or cheapest-language without real evidence.
- **Don't** use "under new management" as a banner or trust-strip phrase.
- **Don't** add decorative eyebrows above headings.
- **Don't** use stock laundromat photos for the hero or Open Graph image.
