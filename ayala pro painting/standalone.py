# -*- coding: utf-8 -*-
"""Standalone pages: About, Pricing, Gallery, Reviews."""
from build import (BASE, page_hero, light_header, founder_story, feature_section,
                   credentials_section, map_section, area_callout, cta_banner,
                   table_section, faq_section, inline_cta, a_p,
                   gallery_filtered_section, rating_summary_first, reviews_grid, review_sources,
                   page_schema, breadcrumb, faqpage)

PAGES = []

# ===================================================================== ABOUT
PAGES.append(dict(
  slug="about",
  title="About Ayala Pro Painting | Riverview FL Painters",
  description="Meet Eliseo Ayala and the Ayala Pro Painting team. Locally owned in Riverview, FL. Licensed, insured, and committed to quality painting for every customer.",
  canonical=f"{BASE}/about/",
  schemas=[
    page_schema("AboutPage", "About Ayala Pro Painting", "Locally owned painting company in Riverview, FL, owned and operated by Eliseo Ayala.", f"{BASE}/about/"),
    breadcrumb([("Home", "/"), ("About", f"{BASE}/about/")])],
  body="\n\n".join([
    page_hero("Who We Are", "About Ayala Pro Painting",
      "Ayala Pro Painting is Riverview's locally owned residential and commercial painting company, owned and operated by Eliseo Ayala. We combine the reliability and process of a larger operation with the personal accountability of a true owner-operator — the owner is on every job, every estimate is transparent, and every project is backed by a written workmanship warranty.",
      [("Home", "/"), ("About", None)], estimate_label="Get a Free Estimate"),
    founder_story("Meet Eliseo Ayala — Owner, Lead Painter, Your Neighbor",
      ["[PLACEHOLDER &mdash; customize with Eliseo's real story.] Every paint job tells a story, and mine started with a simple belief: if you're going to do something, do it right or don't do it at all.",
       "I founded Ayala Pro Painting in Riverview because I saw too many homeowners getting let down by contractors who cut corners, skipped prep work, and disappeared when problems showed up. I wanted to build something different &mdash; a company where the owner is on every job, every estimate is transparent, and every customer gets the quality they were promised.",
       "I'm not just the name on the truck. I'm the person who shows up to assess your project, the one who checks every wall before we call it done, and the one who answers the phone if anything isn't right. That's the advantage of hiring a locally owned company. When you hire Ayala Pro Painting, you're hiring me &mdash; and I take that personally."],
      "&mdash; Eliseo Ayala, Owner &amp; Lead Painter",
      "Eliseo Ayala, owner of Ayala Pro Painting, at a job site in Riverview, FL"),
    feature_section("Our Values", "What We Stand For", [
      ("Owner Accountability", "When you hire us, you get Eliseo on your project &mdash; not a subcontractor, not a franchise manager. One person responsible for your results from start to finish."),
      ("Honest Craftsmanship", "We never cut corners on preparation, use inferior products to save money, or rush a project to move on. Quality takes time, and we give it the time it deserves."),
      ("Transparent Communication", "You'll always know what your project costs, what's happening on any given day, and what to expect next. No surprises, no hidden fees, no unanswered calls."),
      ("Community Investment", "We live and work in Riverview. Your home is in our neighborhood. We treat every project like our reputation depends on it &mdash; because it does."),
      ("Florida Expertise", "We don't just paint in Florida &mdash; we paint for Florida. Every product choice, prep step, and technique is selected for this climate."),
      ("Standing Behind Our Work", "Every project comes with a written 2-year workmanship warranty. If something isn't right, we make it right. Period."),
    ], bg="white"),
    credentials_section("Licensed. Insured. Ready to Work.", [
      "Florida Licensed Contractor (DBPR) [license # on request]",
      "$1 Million General Liability Insurance",
      "Workers' Compensation Coverage",
      "EPA RRP Certified (Lead-Safe) for pre-1978 homes",
      "2-Year Written Workmanship Warranty",
      "Premium Sherwin-Williams &amp; Benjamin Moore Products",
    ]),
    map_section("Proudly Serving Riverview &amp; South Hillsborough County",
      "Based in Riverview, we serve homeowners and businesses across south and east Hillsborough County.", bg="white"),
    area_callout("Areas We Serve", bg="cream"),
    cta_banner("Ready to Work With a Painting Company That Puts You First?",
      "Get a free, no-obligation estimate from Riverview's locally owned, owner-operated painting professionals."),
  ]),
))

# ===================================================================== PRICING
_pricing_faq = [
 ("How do I get an exact price for my painting project?",
  "Contact us for a free on-site estimate. We visit your property, assess the scope, discuss your preferences, and provide a detailed, itemized written estimate within 24-48 hours. There is no cost or obligation for estimates."),
 ("Why are your prices higher than some competitors?",
  "Our pricing reflects premium Sherwin-Williams and Benjamin Moore products, comprehensive surface preparation, two coats on all surfaces, owner oversight, and a written warranty. Less expensive quotes often use lower-quality paint, skip prep steps, or apply only one coat. We believe the right paint job should last, which means doing it right from the start."),
 ("Do you offer financing or payment plans?",
  "We currently accept cash, check, and all major credit cards. We are exploring financing options for larger projects. Contact us to discuss payment arrangements for your specific situation."),
 ("How much does pressure washing cost by itself?",
  "Standalone pressure washing starts at $150 for a standard driveway and $250 for a full house wash. However, pressure washing is included at no additional charge with every exterior painting project."),
 ("Is there a deposit required?",
  "We require a 25% deposit to secure your project date on our schedule, with the balance due upon satisfactory completion. For larger commercial projects, we offer milestone-based payment schedules."),
 ("How often will I need to repaint?",
  "With our premium products and thorough preparation, you can expect interior paint to last 5-7 years in living areas and exterior paint to last 7-10 years — significantly longer than standard-grade paint jobs. High-traffic areas and Florida-facing exterior walls may need attention sooner."),
]
PAGES.append(dict(
  slug="pricing",
  title="Painting Costs in Riverview FL | Ayala Pro Painting Pricing",
  description="Transparent painting prices for Riverview, FL homes & businesses. Interior, exterior, cabinets & more. See typical costs and request your free personalized estimate!",
  canonical=f"{BASE}/pricing/",
  schemas=[
    page_schema("WebPage", "Painting Costs in Riverview, FL", "Transparent painting price ranges for residential and commercial projects in Riverview, FL.", f"{BASE}/pricing/"),
    breadcrumb([("Home", "/"), ("Pricing", f"{BASE}/pricing/")]),
    faqpage(_pricing_faq)],
  body="\n\n".join([
    light_header("Transparent Pricing", "How Much Does Painting Cost in Riverview, FL?",
      "Painting costs in Riverview vary based on the type of service, property size, surface condition, and the level of preparation required. We believe in transparent pricing &mdash; no hidden fees, no surprise charges, and no vague estimates. The ranges below reflect typical costs for Riverview-area projects using premium Sherwin-Williams and Benjamin Moore products and our comprehensive preparation. For a precise quote, contact us for a free on-site estimate; we provide detailed, itemized proposals within 24-48 hours.",
      [("Home", "/"), ("Pricing", None)]),
    table_section("Residential", "Interior Painting Prices in Riverview", None,
      ["Service", "Typical Range", "Key Factors"], [
      ["Single Room (walls + ceiling)", "$300 &ndash; $800", "Room size, ceiling height, wall condition, coats"],
      ["Full Interior &mdash; 2BR/1BA", "$1,800 &ndash; $3,500", "Total room count, prep needed"],
      ["Full Interior &mdash; 3BR/2BA", "$2,500 &ndash; $5,500", "Standard Riverview home size"],
      ["Full Interior &mdash; 4BR/3BA", "$4,000 &ndash; $8,000", "Larger homes, higher ceilings"],
      ["Accent Wall", "$150 &ndash; $350", "Wall size, color change, texture"],
      ["Trim, Doors &amp; Baseboards (per room)", "$200 &ndash; $600", "Linear footage, condition, detail"],
      ["Ceiling Only (per room)", "$200 &ndash; $500", "Height, texture type"],
      ], bg="white", anchor="interior"),
    table_section("", "Exterior Painting Prices", None,
      ["Service", "Typical Range", "Key Factors"], [
      ["Single-Story (1,500-2,000 sq ft)", "$3,000 &ndash; $5,000", "Power wash, prep, 2 coats body + trim"],
      ["Two-Story (2,000-3,000 sq ft)", "$4,500 &ndash; $7,500", "Height premium, ladders/scaffolding"],
      ["Large Home (3,000+ sq ft)", "$7,000 &ndash; $12,000+", "Total surface area, detail, access"],
      ["Trim, Fascia &amp; Soffits Only", "$1,500 &ndash; $3,500", "When body paint is still good"],
      ["Front Door &amp; Shutters", "$300 &ndash; $800", "Quick refresh, big curb-appeal impact"],
      ["Stucco Repair + Paint (add-on)", "$500 &ndash; $2,000", "Depends on severity"],
      ], bg="white", anchor="exterior"),
    inline_cta("Want a precise number for your home?", "/contact/", "Get Your Free Estimate"),
    table_section("", "Specialty Service Prices", "Pressure washing and color consultation are included free with related painting projects.",
      ["Service", "Typical Range", "Key Factors"], [
      ["Cabinet Refinishing &mdash; Small Kitchen", "$3,500 &ndash; $5,000", "15-20 doors/drawers"],
      ["Cabinet Refinishing &mdash; Medium Kitchen", "$5,000 &ndash; $7,000", "20-30 doors/drawers"],
      ["Cabinet Refinishing &mdash; Large Kitchen", "$7,000 &ndash; $10,000+", "30+ doors/drawers, island"],
      ["Deck/Patio Staining (200-400 sq ft)", "$800 &ndash; $1,500", "Size, condition, product type"],
      ["Garage Floor Epoxy (2-car)", "$2,500 &ndash; $4,500", "Most common garage size"],
      ["Pressure Washing &mdash; Driveway", "$150 &ndash; $300", "Standard 2-car driveway"],
      ["Pressure Washing &mdash; Full House", "$250 &ndash; $500", "Based on home size"],
      ["Drywall Repair (per patch)", "$75 &ndash; $300", "Small holes to large sections"],
      ["Color Consultation (standalone)", "$150 &ndash; $500", "Free with painting projects"],
      ], bg="cream", anchor="specialty"),
    table_section("Commercial", "Commercial Painting Prices in Tampa Bay", None,
      ["Service", "Typical Range", "Notes"], [
      ["Commercial Interior (per sq ft)", "$1.50 &ndash; $3.50 / sq ft", "Wall area, ceiling height"],
      ["Commercial Exterior (per sq ft)", "$1.50 &ndash; $4.00 / sq ft", "Surface type, access"],
      ["HOA/Townhome (per unit exterior)", "$2,000 &ndash; $4,500 / unit", "Volume discounts community-wide"],
      ["Condo Building (per building)", "$8,000 &ndash; $25,000", "Size, stories, substrate"],
      ["Property Management Turnover", "$800 &ndash; $3,500 / unit", "Based on unit size (1BR-3BR)"],
      ["After-Hours / Weekend Premium", "Add 10-15%", "For occupied commercial spaces"],
      ], bg="white", anchor="commercial"),
    feature_section("Included", "What's Included in Our Pricing?", [
      ("Surface Preparation", "Power washing, cleaning, scraping, sanding, patching, and priming &mdash; all included in the quoted price."),
      ("Premium Products", "Sherwin-Williams and Benjamin Moore paints. We never substitute cheaper products to cut costs."),
      ("Two Coats Standard", "Two full coats on all surfaces unless a single coat is specifically appropriate."),
      ("Protection &amp; Cleanup", "Furniture moving, floor covering, landscape protection, masking, and complete cleanup."),
      ("Owner Oversight", "Eliseo personally oversees every project. Included, not an upcharge."),
      ("Written Warranty", "2-year workmanship warranty on residential projects, 1-year on commercial."),
    ], bg="cream"),
    table_section("Factors", "What Factors Affect the Cost of Your Project?", None,
      ["Factor", "Impact", "Details"], [
      ["Property Size", "Major", "Total square footage of surfaces being painted is the primary cost driver"],
      ["Surface Condition", "Major", "Extensive peeling, cracking, or damage requires more prep = higher cost"],
      ["Ceiling Height", "Moderate", "Vaulted ceilings and stairwells require ladders or scaffolding"],
      ["Number of Colors", "Minor-Moderate", "Multiple colors add masking, cutting in, and product"],
      ["Product Selection", "Moderate", "Premium products cost more up front but last longer"],
      ["Access Difficulty", "Moderate", "Tight spaces or second-story access adds time and equipment"],
      ["Existing Color", "Minor", "Dark-to-light changes may require extra primer and coats"],
      ["Repairs Needed", "Variable", "Drywall, stucco, or wood repair scope affects cost"],
      ], bg="white", anchor="factors"),
    faq_section("Painting Cost Questions", _pricing_faq, bg="cream"),
    cta_banner("Ready for Your Free, Personalized Estimate?",
      "The ranges above are starting points &mdash; your actual cost depends on your specific property. Let us provide a precise, no-obligation quote."),
  ]),
))

# ===================================================================== GALLERY
_gallery_cards = [
  dict(cat="exterior", title="Exterior Repaint &mdash; Panther Trace, Riverview", detail="Exterior Painting | 2-story CBS/stucco | Sherwin-Williams Duration", alt="Exterior house painting project in Panther Trace, Riverview FL by Ayala Pro Painting"),
  dict(cat="interior", title="Interior Refresh &mdash; Riverview", detail="Interior Painting | 3BR/2BA | low-VOC eggshell", alt="Interior painting project in Riverview FL by Ayala Pro Painting"),
  dict(cat="cabinet", title="Kitchen Cabinet Refinish &mdash; Fish Hawk", detail="Cabinet Refinishing | white enamel | sprayed finish", alt="White kitchen cabinet refinishing project in Fish Hawk FL by Ayala Pro Painting"),
  dict(cat="commercial", title="Storefront Repaint &mdash; Brandon", detail="Commercial Exterior | after-hours schedule", alt="Commercial storefront painting project in Brandon FL by Ayala Pro Painting"),
  dict(cat="exterior", title="Two-Story Stucco &mdash; Valrico", detail="Exterior Painting | elastomeric coating", alt="Two-story stucco exterior painting project in Valrico FL by Ayala Pro Painting"),
  dict(cat="pressure-washing", title="Driveway &amp; House Wash &mdash; Apollo Beach", detail="Pressure Washing | pre-paint prep", alt="Driveway and house pressure washing project in Apollo Beach FL by Ayala Pro Painting"),
  dict(cat="interior", title="Living Room &amp; Trim &mdash; Brandon", detail="Interior Painting | accent wall + trim", alt="Living room and trim painting project in Brandon FL by Ayala Pro Painting"),
  dict(cat="cabinet", title="Bathroom Vanity Refinish &mdash; Riverview", detail="Cabinet Refinishing | navy enamel", alt="Navy bathroom vanity refinishing project in Riverview FL by Ayala Pro Painting"),
  dict(cat="commercial", title="Office Suite Repaint &mdash; Riverview", detail="Commercial Interior | low-VOC | weekend work", alt="Commercial office suite interior painting in Riverview FL by Ayala Pro Painting"),
]
PAGES.append(dict(
  slug="gallery",
  title="Our Painting Work | Riverview FL Projects | Ayala Pro Painting",
  description="See real painting projects completed by Ayala Pro Painting in Riverview, FL. Before & after photos of interior, exterior, cabinet, and commercial work.",
  canonical=f"{BASE}/gallery/",
  schemas=[
    page_schema("CollectionPage", "Our Painting Work", "Portfolio of real painting projects completed by Ayala Pro Painting in Riverview, FL.", f"{BASE}/gallery/"),
    page_schema("ImageGallery", "Ayala Pro Painting Project Gallery", "Before-and-after painting project photos from Riverview and Tampa Bay.", f"{BASE}/gallery/"),
    breadcrumb([("Home", "/"), ("Our Work", f"{BASE}/gallery/")])],
  body="\n\n".join([
    light_header("Project Gallery", "Our Painting Work in Riverview &amp; Tampa Bay",
      "Every project below represents real work completed for real customers in the Riverview area. No stock photos, no borrowed portfolios &mdash; just honest craftsmanship from Ayala Pro Painting. [PLACEHOLDER images shown until real project photos are added.]",
      [("Home", "/"), ("Our Work", None)]),
    gallery_filtered_section(_gallery_cards, bg="white"),
    cta_banner("Like What You See? Let's Talk About Your Project.",
      "Get a free, no-obligation estimate from Riverview's trusted painting professionals."),
  ]),
))

# ===================================================================== REVIEWS
_reviews = [
  dict(quote="[PLACEHOLDER] Eliseo and his crew repainted our whole exterior and the prep work was incredible — they caught wood rot two other quotes missed. Finished on schedule and the color is perfect.",
       name="[Customer Name]", project="Exterior Painting — Riverview, FL", source="Google"),
  dict(quote="[PLACEHOLDER] Spotless work from start to finish. They covered everything, cleaned up each day, and the owner checked in personally. Great value for the quality.",
       name="[Customer Name]", project="Interior Painting — Brandon, FL", source="Google"),
  dict(quote="[PLACEHOLDER] Our kitchen looks brand new. The color consultation helped us pick the perfect white, it was done on time, and it's backed by a warranty. Highly recommend.",
       name="[Customer Name]", project="Cabinet Refinishing — Fish Hawk, FL", source="Google"),
  dict(quote="[PLACEHOLDER] Pressure washed and repainted the exterior to meet our HOA standards. Curb appeal is night and day, and they knew exactly what Florida weather requires.",
       name="[Customer Name]", project="Exterior + Pressure Wash — Apollo Beach, FL", source="Google"),
]
PAGES.append(dict(
  slug="reviews",
  title="Customer Reviews | Ayala Pro Painting Riverview FL",
  description="See what Riverview homeowners say about Ayala Pro Painting. Real reviews from real customers. 5-star rated painting services. Read reviews or leave yours!",
  canonical=f"{BASE}/reviews/",
  # NOTE: No AggregateRating schema — added only once real reviews exist (per dev guide).
  schemas=[
    page_schema("WebPage", "Customer Reviews", "Customer reviews and testimonials for Ayala Pro Painting in Riverview, FL.", f"{BASE}/reviews/"),
    breadcrumb([("Home", "/"), ("Reviews", f"{BASE}/reviews/")])],
  body="\n\n".join([
    light_header("Customer Reviews", "What Our Customers Say About Ayala Pro Painting",
      "We let our work speak for itself &mdash; and our customers speak for us. Every review below is from a real homeowner or business we've served in the Riverview and Tampa Bay area.",
      [("Home", "/"), ("Reviews", None)]),
    rating_summary_first(bg="cream"),
    reviews_grid("Reviews From Riverview &amp; Tampa Bay", _reviews, bg="white"),
    review_sources(bg="cream"),
    cta_banner("Ready to Experience 5-Star Painting Service?",
      "Get a free, no-obligation estimate from Riverview's trusted, locally owned painting professionals."),
  ]),
))
