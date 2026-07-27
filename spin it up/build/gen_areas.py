#!/usr/bin/env python3
"""Generate the 5 neighborhood area-page content fragments + JSON-LD from a
data table. Run once (or after editing AREAS); then `python build/generate.py`.
All 5 pages share one template — only the local content differs."""
import os, json, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content")
MAPS = "https://www.google.com/maps/dir/?api=1&destination=3710+N+Kimball+Ave,+Chicago,+IL+60618"

CHEV = '<svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'

SERVICE = {
    "self-service": ("Self-Service Laundry", "/services/self-service/", "View Self-Service →"),
    "wash-fold":    ("Wash &amp; Fold Drop-Off", "/services/wash-and-fold/", "View Wash &amp; Fold →"),
    "pickup":       ("Pickup &amp; Delivery", "/services/pickup-delivery/", "Schedule Pickup →"),
}

ALL = [("avondale","Avondale"),("irving-park","Irving Park"),("logan-square","Logan Square"),
       ("hermosa","Hermosa"),("albany-park","Albany Park")]

def map_q(area_q):
    return ("https://www.google.com/maps?q=" + area_q.replace(" ", "+") +
            "+to+3710+N+Kimball+Ave+Chicago+IL+60618&output=embed")

AREAS = {
"avondale": {
  "name":"Avondale","title":"Laundromat in Avondale, Chicago | Spin It Up — 3710 N Kimball Ave",
  "desc":"Avondale's neighborhood laundromat at 3710 N Kimball Ave. 41 washers, 52 dryers, 130 lb machines. Self-service, wash & fold, pickup & delivery. EBT accepted.",
  "h1":"Laundry Services for Avondale, Chicago",
  "sub":"You're here. Our facility is at 3710 N Kimball Ave.",
  "primary":"directions",
  "aeo":"Spin It Up Laundry is located at 3710 N Kimball Ave in the heart of the Avondale neighborhood on Chicago's Northwest Side, ZIP 60618. We are the neighborhood's closest full-service laundromat, with 41 washers and 52 dryers including 130 lb commercial-capacity machines. Avondale residents can walk in for self-service laundry, drop off for professional wash-and-fold starting at $1.50 per pound, or schedule pickup and delivery through the Cents app. We accept cash, credit, debit, EBT, and laundry cards, and we're open from 6:00 AM to 11:00 PM every day of the week.",
  "about_h":"About the Avondale Neighborhood",
  "about_rows":[("Population","35,489"),("Demographics","51.2% Hispanic, 37.3% White, 4.8% Asian"),("Median Household Income","$92,645"),("ZIP Code(s)","60618"),("Housing Stock","Brick two-flats, Chicago bungalows, workers' cottages, and contemporary new construction. Most residents rent. Beautiful brownstone two-flats still in original form line many streets."),("Local Landmarks","St. Hyacinth Basilica, Eli's Cheesecake World, Forno Rosso Pizzeria Napoletana, Revolution Brewing (nearby), colorful murals on thoroughfares"),("Transit Access","CTA Blue Line (Belmont, Addison stations), CTA buses on Belmont Ave, Kimball Ave, Diversey Ave")],
  "about_para":"Avondale is Spin It Up's home neighborhood — our facility at 3710 N Kimball Ave sits in the heart of this community. Ranked the world's 5th coolest neighborhood by Time Out in 2025, Avondale has become one of Chicago's most vibrant areas for families, young professionals, and small businesses. The neighborhood's housing stock — predominantly brick two-flats and bungalows — means most residents rely on shared or no in-unit laundry facilities. Walk-in self-service and drop-off wash-and-fold are available directly at our facility with zero delivery wait.",
  "why_h":"Why Avondale Residents Choose Spin It Up",
  "why_para":"Many of Avondale's brick two-flats and vintage bungalows do not have in-unit laundry hookups. Newer condo conversions may have shared basement laundry rooms with limited machine availability. For residents in these buildings, a nearby laundromat with modern machines, reasonable pricing, and long hours is essential — not a luxury.",
  "services_h":"Services Available to Avondale Residents",
  "services":[("self-service","Walk in anytime, 6 AM–11 PM. 41 washers, 52 dryers. EBT accepted. Free drying Tue–Thu."),("wash-fold","Drop off dirty, pick up clean. Starting at $1.50/lb. Next-day turnaround."),("pickup","Schedule from the Cents app. We come to you. Starting at $1.75/lb.")],
  "services_note":"Walk-in self-service, wash-and-fold drop-off, AND pickup &amp; delivery all available.",
  "getting_h":"Visit Us at 3710 N Kimball Ave",
  "by_car":"You're here. Our facility is at 3710 N Kimball Ave. Free parking in front of the building.",
  "by_bus":"CTA Blue Line (Belmont, Addison stations), CTA buses on Belmont Ave, Kimball Ave, Diversey Ave",
  "map_q":"Avondale Chicago",
  "faq":[("Where exactly is Spin It Up in Avondale?","We are at 3710 N Kimball Ave, between Irving Park Rd and Addison St, near the intersection with School St. Free parking is available directly in front of the laundromat."),("Do I need to drive or can I walk?","Many Avondale residents are within walking distance. We are also accessible via CTA buses on Kimball Ave and Belmont Ave, and a short walk from the Blue Line Belmont station. If you drive, free parking is available in front of the building and on surrounding streets."),("Can I get pickup and delivery in Avondale?","Yes. Avondale is our primary delivery zone. Schedule through the Cents app and we'll pick up from your door and deliver back clean, typically within 24 hours."),("Do you accept EBT in Avondale?","Yes. We accept EBT for self-service washing and drying. We are one of the only laundromats in the Avondale area that accepts EBT.")],
  "cta_h":"Avondale's Neighborhood Laundromat",
  "cta_sub":"3710 N Kimball Ave, Avondale • Open 6 AM–11 PM • Free drying Tue–Wed–Thu.",
},
"irving-park": {
  "name":"Irving Park","title":"Laundromat Near Irving Park, Chicago | Spin It Up — Pickup & Delivery",
  "desc":"Laundry services for Irving Park, Chicago. Self-service, wash & fold, pickup & delivery. 41 washers, 52 dryers, 130 lb machines at 3710 N Kimball Ave.",
  "h1":"Laundry Services for Irving Park, Chicago",
  "sub":"~1.5 miles north of our facility. A 5-minute drive via Kimball Ave or a short bus ride.",
  "primary":"pickup",
  "aeo":"Spin It Up Laundry provides laundry services to Irving Park residents from our facility at 3710 N Kimball Ave in neighboring Avondale, approximately 1.5 miles south of the Irving Park Blue Line station. Irving Park customers can drive to our facility in about 5 minutes via Kimball Ave, take the CTA bus, or schedule pickup and delivery through the Cents app without leaving home. We offer self-service laundry with 41 washers and 52 dryers, professional wash-and-fold drop-off starting at $1.50 per pound, and door-to-door delivery with most orders returned within 24 hours.",
  "about_h":"About the Irving Park Neighborhood",
  "about_rows":[("Population","53,832"),("Demographics","43.5% White, 40.4% Hispanic, 8.6% Asian"),("Median Household Income","$64,598"),("ZIP Code(s)","60618, 60630, 60641"),("Housing Stock","Large Victorian homes, Foursquare and Revival styles, Craftsman bungalows, Prairie-style homes. The Old Irving Park Historic District features some of Chicago's most historic homes, including pre-Chicago Fire residences. The Villa District is a Chicago Landmark with unique Craftsman homes on boulevard-style streets."),("Local Landmarks","Old Irving Park Historic District, The Villa District (Chicago Landmark), Independence Park Field House, Smoque BBQ, Sabatino's Italian Restaurant, Thai Aree, The Whistle Stop Inn (Chicago Landmark)"),("Transit Access","CTA Blue Line (Irving Park station), Metra Milwaukee District/North Line (Irving Park station), CTA buses on Irving Park Rd, Pulaski Rd, Addison St")],
  "about_para":"Irving Park is Spin It Up's neighbor to the north, directly accessible via Kimball Ave. With 53,000 residents and a mix of historic single-family homes and multi-unit buildings, Irving Park has strong demand for professional laundry services. The neighborhood's multi-generational character — long-term residents in Victorian homes alongside young families in renovated bungalows — creates a broad customer base for both self-service and pickup delivery.",
  "why_h":"Why Irving Park Residents Choose Spin It Up",
  "why_para":"Many of Irving Park's historic homes were built before in-unit laundry was standard. Even updated homes in the Old Irving Park and Villa districts may have basement laundry with aging equipment. Multi-unit brick buildings along the main corridors typically have limited shared laundry. For these residents, a modern laundromat with new machines and extended hours is a practical necessity.",
  "services_h":"Services Available to Irving Park Residents",
  "services":[("pickup","Schedule from the Cents app. We pick up from your door in Irving Park and deliver back within 24 hours."),("wash-fold","Drive to 3710 N Kimball Ave — about 5 minutes via Kimball Ave. Drop off dirty, pick up clean. $1.50/lb."),("self-service","Visit our facility. 41 washers, 52 dryers, 130 lb machines. EBT accepted.")],
  "services_note":"Pickup &amp; delivery available throughout Irving Park via the Cents app.",
  "getting_h":"Getting to Spin It Up from Irving Park",
  "by_car":"~1.5 miles north of our facility. A 5-minute drive via Kimball Ave. Free parking in front of the building.",
  "by_bus":"CTA Blue Line (Irving Park station), Metra Milwaukee District/North Line (Irving Park station), CTA buses on Irving Park Rd, Pulaski Rd, Addison St",
  "map_q":"Irving Park Chicago",
  "faq":[("How far is Spin It Up from Irving Park?","Our facility at 3710 N Kimball Ave is approximately 1.5 miles south of the Irving Park Blue Line station. That's about a 5-minute drive straight down Kimball Ave or a short CTA bus ride on the Kimball (#82) bus."),("Do you deliver to Irving Park?","Yes. Irving Park is one of our primary delivery zones. Schedule a pickup through the Cents app, and we'll come to your door. Most orders are returned within 24 hours."),("I live in Old Irving Park. Can I still get delivery?","Yes. Our delivery area covers all of Irving Park, including Old Irving Park, The Villas, West Walker, and Kilbourn Park. Enter your address in the Cents app to confirm."),("Is there parking at Spin It Up if I drive from Irving Park?","Yes. Free parking is available directly in front of our building at 3710 N Kimball Ave. Street parking is also available on Kimball and surrounding residential streets.")],
  "cta_h":"Irving Park's Neighborhood Laundromat",
  "cta_sub":"3710 N Kimball Ave, Avondale • Open 6 AM–11 PM • Free drying Tue–Wed–Thu.",
},
"logan-square": {
  "name":"Logan Square","title":"Laundromat Near Logan Square, Chicago | Spin It Up — Delivery",
  "desc":"Laundry services for Logan Square, Chicago. Self-service, wash & fold from $1.50/lb, pickup & delivery. 130 lb machines. Open 6 AM–11 PM daily.",
  "h1":"Laundry Services for Logan Square, Chicago",
  "sub":"~1.5 miles south of our facility. A 5–8 minute drive via Kimball Ave or California Ave.",
  "primary":"pickup",
  "aeo":"Spin It Up Laundry serves Logan Square residents from our facility at 3710 N Kimball Ave in neighboring Avondale, approximately 1.5 miles north of the Logan Square Blue Line station. Logan Square customers can visit our facility for self-service laundry with 41 washers and 52 dryers, drop off for professional wash-and-fold starting at $1.50 per pound, or schedule pickup and delivery through the Cents app for door-to-door service. Delivery throughout Logan Square and Palmer Square is available seven days a week, with most orders completed within 24 hours of pickup.",
  "about_h":"About the Logan Square Neighborhood",
  "about_rows":[("Population","70,869"),("Demographics","51.5% White, 34.5% Hispanic, 5.3% Black, 4.9% Asian"),("Median Household Income","$103,469"),("ZIP Code(s)","60614, 60618, 60622, 60647"),("Housing Stock","Mix of vintage brick two-flats, renovated bungalows, luxury condo conversions, and new-construction apartment buildings. The historic boulevard system features ornamental graystones and mansion-style homes. Palmer Square has leafy tree-lined streets with single-family homes. High density of renters, especially along Milwaukee Ave corridor."),("Local Landmarks","Illinois Centennial Memorial column in Logan Square, Palmer Square Park, Logan Boulevard historic homes, Revolution Brewing, Longman &amp; Eagle, Lula Cafe, The Logan Theatre, Emporium Arcade Bar"),("Transit Access","CTA Blue Line (Logan Square station, California station), CTA buses on Fullerton Ave, Milwaukee Ave, Diversey Ave, California Ave")],
  "about_para":"Logan Square is Chicago's largest neighboring community area with nearly 71,000 residents and the highest median income in our delivery zone. The neighborhood's density and renter-heavy demographics create strong demand for laundry services. Logan Square's busy professional population makes pickup and delivery especially attractive — these are exactly the customers who value convenience and are willing to pay for door-to-door service.",
  "why_h":"Why Logan Square Residents Choose Spin It Up",
  "why_para":"Logan Square's building stock ranges from century-old brick two-flats to modern condo conversions. Many vintage buildings have limited or no in-unit laundry. Even newer buildings may only offer shared laundry rooms. For the neighborhood's large renter population, apartment laundry rooms are often insufficient — limited machines, long wait times, and aging equipment. A professional laundry service eliminates this friction entirely.",
  "services_h":"Services Available to Logan Square Residents",
  "services":[("pickup","Schedule from the Cents app. We pick up from your door in Logan Square and deliver back within 24 hours."),("wash-fold","Drive to 3710 N Kimball Ave — a 5–8 minute drive via Kimball Ave or California Ave. Drop off dirty, pick up clean. $1.50/lb."),("self-service","Visit our facility. 41 washers, 52 dryers, 130 lb machines. EBT accepted.")],
  "services_note":"Pickup &amp; delivery available throughout Logan Square and Palmer Square via the Cents app.",
  "getting_h":"Getting to Spin It Up from Logan Square",
  "by_car":"~1.5 miles south of our facility. A 5–8 minute drive via Kimball Ave or California Ave. Free parking in front of the building.",
  "by_bus":"CTA Blue Line (Logan Square station, California station), CTA buses on Fullerton Ave, Milwaukee Ave, Diversey Ave, California Ave",
  "map_q":"Logan Square Chicago",
  "faq":[("How far is Spin It Up from Logan Square?","Our facility at 3710 N Kimball Ave is approximately 1.5 miles north of the Logan Square Blue Line station. That's about a 5–8 minute drive via Kimball Ave or California Ave. The Kimball (#82) CTA bus also runs directly to our location."),("Do you deliver to Logan Square and Palmer Square?","Yes. Both Logan Square and Palmer Square are in our primary delivery zone. Schedule a pickup through the Cents app from anywhere in the neighborhood, and we'll pick up and deliver to your door."),("I'm an Airbnb host in Logan Square. Do you offer commercial service?","Yes. We provide commercial laundry services for Airbnb and vacation rental hosts throughout Logan Square. Volume-based pricing, reliable turnaround, and scheduled pickup are available. Visit our Commercial Services page or call (773) 654-1275 for a quote."),("What's the closest laundromat to Logan Square?","Spin It Up Laundry at 3710 N Kimball Ave in Avondale is one of the closest full-service laundromats to Logan Square, with the largest machines in the area (130 lb capacity). We also offer pickup and delivery so you don't have to leave your neighborhood at all.")],
  "cta_h":"Logan Square's Neighborhood Laundromat",
  "cta_sub":"3710 N Kimball Ave, Avondale • Open 6 AM–11 PM • Free drying Tue–Wed–Thu.",
},
"hermosa": {
  "name":"Hermosa","title":"Laundromat Near Hermosa, Chicago | Spin It Up — Pickup & Delivery",
  "desc":"Laundry services for Hermosa, Chicago. Self-service, wash & fold, pickup & delivery. EBT accepted. 130 lb machines. Open 6 AM–11 PM daily.",
  "h1":"Laundry Services for Hermosa, Chicago",
  "sub":"~1 mile west of our facility. A 5-minute drive via Fullerton Ave or Belmont Ave.",
  "primary":"pickup",
  "aeo":"Spin It Up Laundry serves Hermosa and Kelvyn Park residents from our facility at 3710 N Kimball Ave in neighboring Avondale, approximately one mile east. Hermosa residents can drive to our facility in about 5 minutes via Fullerton Ave or Belmont Ave, or schedule pickup and delivery through the Cents app. We offer 41 washers and 52 dryers including 130 lb commercial machines, professional wash-and-fold starting at $1.50 per pound, and EBT acceptance for self-service laundry. We are open 6:00 AM to 11:00 PM, seven days a week.",
  "about_h":"About the Hermosa Neighborhood",
  "about_rows":[("Population","~25,000"),("Demographics","Predominantly Hispanic, historically working-class"),("Median Household Income","Below citywide median"),("ZIP Code(s)","60639, 60641"),("Housing Stock","Classic Chicago bungalows (the Hermosa Bungalow Historic District was added to the National Register of Historic Places in 2018 with 298 contributing bungalows), workers' cottages, brick two-flats, and small apartment buildings. Average home age dates to 1919, with 63% of structures built before 1940. Two sub-neighborhoods: Hermosa (south of Fullerton) and Kelvyn Park (north of Fullerton)."),("Local Landmarks","Walt Disney's childhood home (2156 N Tripp Ave), Hermosa Bungalow Historic District (National Register), Kelvyn Park High School, Ken-Well Park, historic Westinghouse Electric and Wrigley Company factory sites"),("Transit Access","Metra Milwaukee District/North Line (Hermosa station), CTA buses on Fullerton Ave, Belmont Ave, Armitage Ave, Pulaski Rd. Divvy bike stations available.")],
  "about_para":"Hermosa sits directly west of Avondale, making Spin It Up one of the closest modern laundromats for Hermosa residents. The neighborhood's housing stock is among the oldest in our delivery zone — homes averaging over 100 years old — and very few have in-unit laundry. Hermosa's affordability and family-centric character mean residents value practical services with fair pricing, including EBT acceptance.",
  "why_h":"Why Hermosa Residents Choose Spin It Up",
  "why_para":"Hermosa's century-old bungalows and workers' cottages were built decades before in-unit laundry machines existed. Most single-family homes may have basement hookups, but many renters in two-flats and small apartment buildings have no laundry access at all. The neighborhood's affordability-conscious residents benefit from our competitive pricing, EBT acceptance, and free drying specials.",
  "services_h":"Services Available to Hermosa Residents",
  "services":[("pickup","Schedule from the Cents app. We pick up from your door in Hermosa and deliver back within 24 hours."),("wash-fold","Drive to 3710 N Kimball Ave — a 5-minute drive via Fullerton Ave or Belmont Ave. Drop off dirty, pick up clean. $1.50/lb."),("self-service","Visit our facility. 41 washers, 52 dryers, 130 lb machines. EBT accepted.")],
  "services_note":"Pickup &amp; delivery available throughout Hermosa and Kelvyn Park via the Cents app.",
  "getting_h":"Getting to Spin It Up from Hermosa",
  "by_car":"~1 mile east of our facility. A 5-minute drive via Fullerton Ave or Belmont Ave. Free parking in front of the building.",
  "by_bus":"Metra Milwaukee District/North Line (Hermosa station), CTA buses on Fullerton Ave, Belmont Ave, Armitage Ave, Pulaski Rd. Divvy bike stations available.",
  "map_q":"Hermosa Chicago",
  "faq":[("How far is Spin It Up from Hermosa?","Our facility at 3710 N Kimball Ave is approximately 1 mile east of central Hermosa. That's about a 5-minute drive via Fullerton Ave or Belmont Ave. CTA buses on Fullerton (#74) and Belmont (#77) run to the Kimball Ave area."),("Do you deliver to Hermosa?","Yes. Hermosa and Kelvyn Park are both in our primary delivery zone. Schedule through the Cents app and we'll pick up and deliver to your door, typically within 24 hours."),("Do you accept EBT?","Yes. We accept EBT for self-service washing and drying at our facility. Hermosa residents can use EBT the same as cash — swipe at the counter to load a laundry card."),("Is there free drying?","Every Tuesday, Wednesday, and Thursday, all dryers are free when you wash with us. This is a permanent weekly special available to all customers.")],
  "cta_h":"Hermosa's Neighborhood Laundromat",
  "cta_sub":"3710 N Kimball Ave, Avondale • Open 6 AM–11 PM • Free drying Tue–Wed–Thu.",
},
"albany-park": {
  "name":"Albany Park","title":"Laundromat Near Albany Park, Chicago | Spin It Up — Delivery",
  "desc":"Laundry services for Albany Park, Chicago. Pickup & delivery via the Cents app, plus self-service & wash & fold at 3710 N Kimball Ave. EBT accepted. Se habla español.",
  "h1":"Laundry Services for Albany Park, Chicago",
  "sub":"~2.5 miles north of our facility. Pickup &amp; delivery available — schedule from the Cents app and we'll come to you.",
  "primary":"pickup",
  "aeo":"Spin It Up Laundry serves Albany Park residents from our facility at 3710 N Kimball Ave in neighboring Avondale, approximately 2.5 miles south. Albany Park customers can schedule laundry pickup and delivery through the Cents app without leaving the neighborhood — we pick up from your door, wash, dry, and fold everything at our facility, and deliver it back within 24 hours. For customers who prefer to visit in person, our facility is a quick drive south on Kimball Ave or Kedzie Ave. We offer 41 washers and 52 dryers, professional wash-and-fold starting at $1.50 per pound, and EBT acceptance for self-service laundry. Se habla español.",
  "about_h":"About the Albany Park Neighborhood",
  "about_rows":[("Population","46,620"),("Demographics","44.5% Hispanic, 33.3% White, 15.0% Asian, 3.8% Black — one of the most ethnically diverse neighborhoods in the United States"),("Languages","Over 40 languages spoken in Albany Park public schools"),("Median Income","~$61,759"),("ZIP Codes","60625, 60630"),("Housing Stock","Charming bungalows, large Victorians, multi-unit apartment buildings. Median construction year: 1938. Over 53% of homes built before 1940. 59.2% of housing units are renter-occupied."),("Local Landmarks","West Lawrence Ave international food corridor, River Park (30+ acres), Ronan Park, Eugene Field Park, North Branch of the Chicago River, Ravenswood Manor sub-neighborhood"),("Transit Access","CTA Brown Line (Kedzie, Francisco, Montrose stations), CTA buses on Lawrence Ave (#81), Kedzie Ave (#82B), Kimball Ave (#82)")],
  "about_para":"Albany Park is one of Chicago's most culturally diverse neighborhoods — over 40 languages are spoken in its public schools, and its food corridor along West Lawrence Avenue represents cuisines from Korea, Mexico, the Middle East, the Philippines, Guatemala, and beyond. With 46,000 residents and a housing stock where nearly 60% of units are renter-occupied, the neighborhood has strong demand for accessible, affordable laundry services. Many of Albany Park's pre-war bungalows and multi-unit apartment buildings lack in-unit laundry. Our pickup and delivery service brings modern laundry directly to these residents' doors.",
  "why_h":"Why Albany Park Residents Choose Spin It Up",
  "why_para":"Albany Park's housing is among the oldest in our delivery zone, with a median construction date of 1938. Most of the neighborhood's bungalows and apartment buildings were built decades before in-unit laundry machines existed. For renters in multi-unit buildings — who make up nearly 60% of Albany Park households — shared laundry rooms with limited, aging machines are common. Our pickup and delivery service through the Cents app eliminates this friction entirely: schedule from your phone, and we handle the rest. For residents who prefer to visit our facility, the drive south on Kimball Ave or Kedzie Ave takes about 8 minutes.",
  "services_h":"Services Available to Albany Park Residents",
  "services":[("pickup","Schedule from the Cents app. We pick up from your door in Albany Park and deliver back within 24 hours."),("wash-fold","Drive to 3710 N Kimball Ave — about 2.5 miles, 8 minutes. Drop off dirty, pick up clean. $1.50/lb."),("self-service","Visit our facility. 41 washers, 52 dryers, 130 lb machines. EBT accepted.")],
  "services_note":"Albany Park is in our <strong>extended delivery zone</strong>. Delivery is available — enter your address in the Cents app to confirm coverage for your specific location.",
  "getting_h":"Getting to Spin It Up from Albany Park",
  "by_car":"~2.5 miles south via Kimball Ave or Kedzie Ave. About 8 minutes in normal traffic. Free parking in front of the building.",
  "by_bus":"CTA #82 Kimball bus runs directly between Albany Park and our facility. #82B Kedzie bus also connects. ~15–20 minute ride.",
  "map_q":"Albany Park Chicago",
  "faq":[("Do you deliver to Albany Park?","Yes. Albany Park is in our extended delivery zone. Most Albany Park addresses are covered. Enter your address in the Cents app to confirm delivery availability for your specific location. If your address falls outside our current zone, call us at (773) 654-1275 — we may be able to arrange delivery."),("How far is Spin It Up from Albany Park?","Our facility at 3710 N Kimball Ave in Avondale is approximately 2.5 miles south of central Albany Park. That's about an 8-minute drive via Kimball Ave or Kedzie Ave. The CTA #82 Kimball bus runs directly between Albany Park and our location."),("Do you have staff who speak Spanish?","Yes. Se habla español. Our attendants can assist Spanish-speaking customers at our facility. Our website also has a Spanish-language version."),("What payment methods do you accept?","We accept cash, credit cards, debit cards, EBT (for self-service washing and drying), and our reloadable laundry card. Pickup and delivery orders are paid via credit or debit card through the Cents app.")],
  "cta_h":"Albany Park's Laundry Solution",
  "cta_sub":"Schedule pickup from your phone or visit us at 3710 N Kimball Ave, Avondale. Se habla español.",
},
}

PICKUP_BTN = '<a href="#" data-cents class="btn btn--primary">Schedule Pickup</a>'
DIR_BTN = '<a href="%s" class="btn btn--primary">Get Directions</a>' % MAPS

def render(slug, a):
    name = a["name"]
    hero_primary = DIR_BTN if a["primary"] == "directions" else PICKUP_BTN
    # about table rows
    about_rows = "\n".join(
        '            <tr><td data-label="">%s</td><td>%s</td></tr>' % (k, v) for k, v in a["about_rows"])
    # service cards
    cards = []
    for key, desc in a["services"]:
        title, link, cta = SERVICE[key]
        cards.append('          <a class="card service-card" href="%s"><h3 class="card__title">%s</h3><p class="card__text">%s</p><span class="card__cta">%s</span></a>' % (link, title, desc, cta))
    cards = "\n".join(cards)
    # siblings
    sibs = "\n".join(
        '          <a class="badge badge--service" style="font-size:15px;padding:8px 16px;" href="/areas/%s/">%s</a>' % (s, n)
        for s, n in ALL if s != slug)
    # faq
    faq_items = []
    for q, ans in a["faq"]:
        ans2 = ans.replace("(773) 654-1275", '<a href="tel:+17736541275">(773) 654-1275</a>')
        ans2 = ans2.replace("Commercial Services page", '<a href="/services/commercial/">Commercial Services</a> page')
        faq_items.append('          <div class="faq__item"><button class="faq__q" aria-expanded="false">%s%s</button><div class="faq__a"><div class="faq__a-inner"><p>%s</p></div></div></div>' % (q, CHEV, ans2))
    faq_items = "\n".join(faq_items)
    cta_primary = DIR_BTN.replace('btn--primary"', 'btn--primary btn--lg"') if a["primary"] == "directions" else PICKUP_BTN.replace('btn--primary"', 'btn--primary btn--lg"')

    body = f'''    <!-- HERO -->
    <section class="page-hero" aria-label="Laundry services for {name}">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <ol><li><a href="/">Home</a></li><li><a href="/areas/">Service Areas</a></li><li aria-current="page">{name}</li></ol>
        </nav>
        <h1>{a["h1"]}</h1>
        <p class="page-hero__lead">{a["sub"]}</p>
        <div class="page-hero__ctas">
          {hero_primary}
          <a href="tel:+17736541275" class="btn btn--outline-white">Call (773) 654-1275</a>
        </div>
      </div>
    </section>

    <!-- AEO INTRO -->
    <section class="section" style="padding-bottom:0;">
      <div class="container">
        <p style="max-width:800px;margin:0 auto;text-align:center;font-size:1.125rem;">{a["aeo"]}</p>
      </div>
    </section>

    <!-- ABOUT NEIGHBORHOOD -->
    <section class="section section--alt" aria-labelledby="about-h">
      <div class="container" style="max-width:900px;">
        <div class="section__head section__head--left"><h2 id="about-h">{a["about_h"]}</h2></div>
        <table class="price-table price-table--responsive" style="margin-top:0;">
          <tbody>
{about_rows}
          </tbody>
        </table>
        <p style="margin-top:var(--space-6);">{a["about_para"]}</p>
      </div>
    </section>

    <!-- WHY HERE -->
    <section class="section" aria-labelledby="why-h">
      <div class="container" style="max-width:800px;">
        <div class="section__head section__head--left"><h2 id="why-h">{a["why_h"]}</h2></div>
        <p>{a["why_para"]}</p>
      </div>
    </section>

    <!-- SERVICES AVAILABLE -->
    <section class="section section--alt" data-section="services" aria-labelledby="svc-h">
      <div class="container">
        <div class="section__head"><h2 id="svc-h">{a["services_h"]}</h2></div>
        <div class="card-grid">
{cards}
        </div>
        <p class="text-center mt-8" style="color:var(--fresh-cyan);font-weight:600;">{a["services_note"]}</p>
      </div>
    </section>

    <!-- GETTING HERE -->
    <section class="section" aria-labelledby="get-h">
      <div class="container">
        <div class="section__head section__head--left" style="max-width:760px;"><h2 id="get-h">{a["getting_h"]}</h2></div>
        <div class="areas-split">
          <div class="map-embed"><iframe src="{map_q(a["map_q"])}" title="Map showing route from {name} to Spin It Up Laundry at 3710 N Kimball Ave" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
          <div class="feature-list">
            <div class="feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 17h2l.64-2.54a6 6 0 0 0-.46-4.32l-1.1-2.2A3 3 0 0 0 17.4 6H6.6a3 3 0 0 0-2.68 1.94l-1.1 2.2a6 6 0 0 0-.46 4.32L3 17h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/></svg><div><h3 class="feature__title">By Car</h3><p class="feature__text">{a["by_car"]}</p></div></div>
            <div class="feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 6v6M16 6v6M2 12h19.6M18 18h.01M6 18h.01M4 6h16a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2Z"/></svg><div><h3 class="feature__title">By Transit</h3><p class="feature__text">{a["by_bus"]}</p></div></div>
            <div class="feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 17h4V5H2v12h3"/><path d="M20 17h2v-3.34a4 4 0 0 0-1.17-2.83L19 9h-5v8h1"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg><div><h3 class="feature__title">By Pickup &amp; Delivery</h3><p class="feature__text">Schedule through the Cents app. Enter your address to confirm coverage. Most orders completed within 24 hours.</p></div></div>
          </div>
        </div>
        <div class="center-cta"><a class="btn btn--outline" href="{MAPS}">Get Directions</a></div>
      </div>
    </section>

    <!-- NEARBY NEIGHBORHOODS -->
    <section class="section section--alt" data-section="nearby" aria-labelledby="near-h">
      <div class="container text-center">
        <div class="section__head"><h2 id="near-h" style="font-size:1.75rem;">We Also Serve</h2></div>
        <div style="display:flex;flex-wrap:wrap;gap:var(--space-3);justify-content:center;">
{sibs}
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section" data-section="faq" aria-labelledby="faq-h">
      <div class="container">
        <div class="section__head"><h2 id="faq-h">{name} Laundry FAQ</h2></div>
        <div class="faq">
{faq_items}
        </div>
        <div class="center-cta"><a href="/faq/" style="font-weight:600;">View All FAQs →</a></div>
      </div>
    </section>

    <!-- CTA -->
    <section class="section band-blue cta-block" data-section="cta" aria-labelledby="cta-h">
      <div class="container">
        <h2 id="cta-h">{a["cta_h"]}</h2>
        <p class="cta-block__subtitle">{a["cta_sub"]}</p>
        <div class="cta-block__btns">
          {cta_primary}
          <a class="btn btn--outline-white btn--lg" href="tel:+17736541275">Call (773) 654-1275</a>
        </div>
      </div>
    </section>'''

    # JSON-LD head
    faq_schema = ",\n".join(
        '      { "@type": "Question", "name": %s, "acceptedAnswer": { "@type": "Answer", "text": %s } }'
        % (json.dumps(q), json.dumps(ans)) for q, ans in a["faq"])
    head = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Laundry Service in {name}",
    "description": {json.dumps(a["desc"])},
    "url": "https://spinituplaundry.net/areas/{slug}/",
    "provider": {{
      "@type": "Laundromat",
      "name": "Spin It Up Laundry",
      "telephone": "+1-773-654-1275",
      "address": {{ "@type": "PostalAddress", "streetAddress": "3710 N Kimball Ave", "addressLocality": "Chicago", "addressRegion": "IL", "postalCode": "60618" }}
    }},
    "areaServed": {{ "@type": "Neighborhood", "name": "{name}" }},
    "serviceType": "Laundry Service"
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://spinituplaundry.net/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Service Areas", "item": "https://spinituplaundry.net/areas/" }},
      {{ "@type": "ListItem", "position": 3, "name": "{name}", "item": "https://spinituplaundry.net/areas/{slug}/" }}
    ]
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{faq_schema}
    ]
  }}
  </script>'''
    return body, head

manifest = {}
for slug, a in AREAS.items():
    body, head = render(slug, a)
    open(os.path.join(CONTENT, slug + ".html"), "w", encoding="utf-8").write(body + "\n")
    open(os.path.join(CONTENT, "_" + slug + "_head.html"), "w", encoding="utf-8").write(head + "\n")
    manifest[slug] = {
        "out": "areas/%s/index.html" % slug, "active": "areas", "hreflang": False,
        "title": a["title"], "description": a["desc"],
        "canonical": "https://spinituplaundry.net/areas/%s/" % slug,
        "og_title": a["title"], "og_description": a["desc"],
        "og_image": "https://spinituplaundry.net/images/og-%s.jpg" % slug,
    }
print(json.dumps(manifest, indent=2, ensure_ascii=False))
