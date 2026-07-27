# -*- coding: utf-8 -*-
"""Legal / utility pages: Privacy Policy, Terms of Service, Accessibility Statement, HTML Sitemap."""
from build import (BASE, legal_page, NOINDEX, light_header, link_group, sitemap_section,
                   page_schema, breadcrumb)

PAGES = []
UPDATED = "June 1, 2026"

# ===================================================================== PRIVACY POLICY
PAGES.append(legal_page(
  slug="privacy",
  title="Privacy Policy | Ayala Pro Painting",
  description="Read the Ayala Pro Painting privacy policy. Learn how we collect, use, and protect your personal information when you visit our website or request services.",
  h1="Privacy Policy", last_updated=UPDATED, robots=NOINDEX,
  sections=[
    ("Information We Collect",
     ["We collect information you voluntarily provide when you request an estimate, contact us, or interact with our website. This includes your name, phone number, email address, street address, and details about your painting project. We also automatically collect certain technical information when you visit our website, including your IP address, browser type, device type, pages visited, and referring URL, through cookies and similar tracking technologies."]),
    ("How We Use Your Information",
     ["We use the information you provide to respond to your estimate requests, schedule consultations, communicate about your painting project, send follow-up correspondence, and improve our services. We use automatically collected data to analyze website traffic, improve user experience, measure advertising effectiveness, and maintain site security. We do not sell, rent, or trade your personal information to third parties for marketing purposes."]),
    ("Third-Party Services",
     ["Our website uses Google Analytics 4 (GA4) to analyze traffic patterns and user behavior. We may use Google Tag Manager, Microsoft Clarity for heatmaps and session recordings (with personally identifiable information excluded), and reCAPTCHA v3 for spam prevention. These services may collect and process data according to their own privacy policies. We also use Google Maps for our service area display and may use email marketing platforms for newsletters and promotions."]),
    ("Cookies &amp; Tracking Technologies",
     ["Our website uses cookies and similar technologies to remember your preferences, analyze site usage, and support our marketing efforts. You can control cookie settings through your browser preferences. Disabling cookies may affect some website functionality. We respect Do Not Track browser signals where technically feasible."]),
    ("Data Security",
     ["We implement reasonable security measures to protect your personal information from unauthorized access, alteration, or disclosure. Form submissions are transmitted over encrypted HTTPS connections. However, no method of electronic transmission or storage is 100% secure, and we cannot guarantee absolute security."]),
    ("Your Rights",
     ["You have the right to request access to, correction of, or deletion of your personal information. To exercise these rights, contact us at info@ayalapropainting.com or call (813) 555-0199. California residents have additional rights under the CCPA, including the right to know what personal information is collected, the right to delete personal information, and the right to opt out of the sale of personal information. We do not sell personal information."]),
    ("Call Recording Disclosure",
     ["Florida is a two-party consent state for call recording (FL Statute 934.03). If we record phone calls for quality assurance or training purposes, you will be notified at the beginning of the call and given the opportunity to opt out. Calls are never recorded without disclosure."]),
    ("Children&rsquo;s Privacy",
     ["Our website and services are not directed to individuals under the age of 13. We do not knowingly collect personal information from children. If you believe we have inadvertently collected information from a child, please contact us immediately and we will take steps to delete it."]),
    ("Changes to This Policy",
     ["We may update this privacy policy from time to time. Changes will be posted on this page with an updated effective date. We encourage you to review this policy periodically."]),
    ("Contact Us",
     ["If you have questions about this privacy policy or our data practices, please contact us at: Ayala Pro Painting, Riverview, FL 33578. Email: <a href=\"mailto:info@ayalapropainting.com\">info@ayalapropainting.com</a>. Phone: <a href=\"tel:8135550199\" data-phone>(813) 555-0199</a>."]),
  ],
))

# ===================================================================== TERMS OF SERVICE
PAGES.append(legal_page(
  slug="terms",
  title="Terms of Service | Ayala Pro Painting",
  description="Read the Ayala Pro Painting terms of service. Understand the terms governing your use of our website and engagement of our painting services.",
  h1="Terms of Service", last_updated=UPDATED, robots=NOINDEX,
  sections=[
    ("Acceptance of Terms",
     ["By accessing or using the Ayala Pro Painting website (ayalapropainting.com), you agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use our website. These terms apply to all visitors, users, and others who access the website."]),
    ("Services Description",
     ["Ayala Pro Painting provides residential and commercial painting services, pressure washing, drywall repair, and related services in the Riverview, Florida and south Hillsborough County area. Information on our website, including pricing, service descriptions, and availability, is provided for general informational purposes and may change without notice. Published pricing ranges are estimates and do not constitute binding offers."]),
    ("Estimates &amp; Proposals",
     ["Written estimates provided by Ayala Pro Painting are valid for 30 days from the date of issue unless otherwise stated. Estimates are based on the conditions observed during our on-site assessment and may be adjusted if additional work is discovered during the project. Any additional work will be discussed with you and approved before proceeding. A signed proposal or verbal acceptance constitutes agreement to the scope and pricing outlined in the estimate."]),
    ("Payment Terms",
     ["A 25% deposit is required to secure your project date on our schedule. The remaining balance is due upon satisfactory completion of the project. We accept cash, check, and all major credit cards. For commercial projects exceeding $10,000, milestone-based payment schedules are available. Late payments may be subject to a 1.5% monthly service charge."]),
    ("Warranty",
     ["Residential painting projects are covered by a 2-year workmanship warranty from the date of completion. Commercial projects carry a 1-year workmanship warranty. The warranty covers defects in our workmanship including premature peeling, bubbling, cracking, or fading under normal conditions. The warranty does not cover damage caused by physical impact, water intrusion from structural defects, acts of nature, or modifications made by others after project completion. Paint product warranties are provided by the respective manufacturers."]),
    ("Scheduling &amp; Cancellation",
     ["We schedule projects based on availability and make every effort to adhere to agreed timelines. Weather conditions, material availability, and unforeseen circumstances may affect scheduling. We will communicate any schedule changes promptly. Cancellation of a confirmed project with less than 48 hours notice may result in forfeiture of the deposit. Cancellation with more than 48 hours notice will result in a full deposit refund."]),
    ("Intellectual Property",
     ["All content on the Ayala Pro Painting website, including text, images, graphics, logos, and code, is the property of Ayala Pro Painting or its content providers and is protected by copyright law. You may not reproduce, distribute, or create derivative works from this content without written permission."]),
    ("Limitation of Liability",
     ["Ayala Pro Painting&rsquo;s liability for any claim arising from our services is limited to the total amount paid for the specific project giving rise to the claim. We are not liable for indirect, incidental, consequential, or punitive damages. This limitation applies to the fullest extent permitted by Florida law."]),
    ("Governing Law",
     ["These terms are governed by the laws of the State of Florida, without regard to conflict of law principles. Any disputes arising from these terms or our services shall be resolved in the courts of Hillsborough County, Florida."]),
    ("Changes to Terms",
     ["We reserve the right to update these terms at any time. Changes will be posted on this page with an updated effective date. Continued use of the website after changes constitutes acceptance of the revised terms."]),
    ("Contact",
     ["Questions about these terms should be directed to: Ayala Pro Painting, Riverview, FL 33578. Email: <a href=\"mailto:info@ayalapropainting.com\">info@ayalapropainting.com</a>. Phone: <a href=\"tel:8135550199\" data-phone>(813) 555-0199</a>."]),
  ],
))

# ===================================================================== ACCESSIBILITY STATEMENT
PAGES.append(legal_page(
  slug="accessibility",
  title="Accessibility Statement | Ayala Pro Painting",
  description="Ayala Pro Painting is committed to website accessibility for all users. Learn about our WCAG 2.1 AA compliance efforts and how to report accessibility issues.",
  h1="Accessibility Statement", last_updated=UPDATED,
  robots="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1",
  sections=[
    ("Our Commitment",
     ["Ayala Pro Painting is committed to ensuring that our website is accessible to all visitors, including individuals with disabilities. We strive to conform to the Web Content Accessibility Guidelines (WCAG) 2.1 at the AA level, which provides guidelines for making web content more accessible to people with a wide range of disabilities, including visual, auditory, physical, speech, cognitive, language, learning, and neurological disabilities."]),
    ("Accessibility Features",
     ["Our website includes the following accessibility features: semantic HTML5 markup for proper structure and navigation; ARIA landmarks and labels on major page sections and interactive elements; keyboard navigation support for all interactive elements; visible focus indicators on all focusable elements; a skip-to-content link on every page; alt text on all meaningful images; sufficient color contrast meeting WCAG 2.1 AA requirements (minimum 4.5:1 for normal text, 3:1 for large text); resizable text that remains functional at 200% zoom; click-to-call phone numbers accessible to screen readers; and form labels properly associated with their inputs."]),
    ("Ongoing Efforts",
     ["We regularly review our website against WCAG 2.1 AA standards and make updates as needed. Accessibility is considered in every new page and feature we develop. We test with keyboard navigation and screen reader technology as part of our quality assurance process."]),
    ("Known Limitations",
     ["While we strive for full accessibility, some content may not yet meet all WCAG 2.1 AA requirements. Specifically: embedded Google Maps may have limited accessibility for keyboard and screen reader users; third-party review widgets may have their own accessibility limitations; and some older PDF documents may not be fully accessible. We are actively working to address these limitations."]),
    ("Feedback &amp; Contact",
     ["If you experience any difficulty accessing our website or have suggestions for improving accessibility, please contact us. We take accessibility feedback seriously and will make reasonable efforts to address reported issues. Contact us at: Email: <a href=\"mailto:info@ayalapropainting.com\">info@ayalapropainting.com</a>. Phone: <a href=\"tel:8135550199\" data-phone>(813) 555-0199</a>. Mailing Address: Ayala Pro Painting, Riverview, FL 33578. We aim to respond to accessibility feedback within 5 business days."]),
    ("Third-Party Content",
     ["Our website may contain links to third-party websites and embedded content (such as Google Maps and review platform widgets) that are not under our control. We cannot guarantee the accessibility of third-party content but encourage you to report any issues to the respective third-party provider."]),
  ],
))

# ===================================================================== HTML SITEMAP
_main = [("Home", "/"), ("About", "/about/"), ("Contact &amp; Free Estimate", "/contact/"),
         ("Gallery", "/gallery/"), ("Pricing Guide", "/pricing/"), ("Customer Reviews", "/reviews/"),
         ("Espa&ntilde;ol (Spanish)", "/es/")]
_services = [("All Services", "/services/"), ("Residential Painting", "/services/residential-painting/"),
             ("Interior Painting", "/services/interior-painting/"), ("Exterior Painting", "/services/exterior-painting/"),
             ("Cabinet Painting &amp; Refinishing", "/services/cabinet-painting/"), ("Deck &amp; Patio Staining", "/services/deck-patio-staining/"),
             ("Garage Floor Epoxy", "/services/garage-floor-epoxy/"), ("Drywall Repair", "/services/drywall-repair/"),
             ("Pressure Washing", "/services/pressure-washing/"), ("Color Consultation", "/services/color-consultation/"),
             ("Commercial Painting", "/services/commercial-painting/"), ("Commercial Interior", "/services/commercial-interior/"),
             ("Commercial Exterior", "/services/commercial-exterior/"), ("HOA &amp; Multi-Family", "/services/hoa-multifamily/"),
             ("Property Management", "/services/property-management/")]
_areas = [("All Service Areas", "/areas/"), ("Riverview", "/areas/riverview/"), ("Brandon", "/areas/brandon/"),
          ("Valrico", "/areas/valrico/"), ("Lithia", "/areas/lithia/"), ("Fish Hawk", "/areas/fish-hawk/"),
          ("Apollo Beach", "/areas/apollo-beach/"), ("Sun City Center", "/areas/sun-city-center/"), ("Ruskin", "/areas/ruskin/"),
          ("Gibsonton", "/areas/gibsonton/"), ("Bloomingdale", "/areas/bloomingdale/"), ("Seffner", "/areas/seffner/"),
          ("Wimauma", "/areas/wimauma/")]
_resources = [("All Resources", "/resources/"),
              ("How Much Does It Cost to Paint a House in Riverview?", "/resources/cost-paint-house-riverview/"),
              ("Interior vs. Exterior Paint", "/resources/interior-vs-exterior-paint-florida/"),
              ("Cabinet Painting Guide", "/resources/guide-cabinet-painting-florida/"),
              ("How to Choose Paint Colors", "/resources/choose-paint-color-florida-home/"),
              ("Why Florida Homes Need Repainting More Often", "/resources/florida-homes-repaint-frequency/"),
              ("HOA Painting Requirements", "/resources/hoa-painting-requirements-riverview/"),
              ("Epoxy Garage Floor Guide", "/resources/epoxy-garage-floor-guide-tampa/"),
              ("Preparing for Exterior Painting", "/resources/prepare-home-exterior-painting-florida/")]
_legal = [("Privacy Policy", "/privacy/"), ("Terms of Service", "/terms/"),
          ("Accessibility Statement", "/accessibility/"), ("Sitemap", "/sitemap/")]

PAGES.append(dict(
  slug="sitemap",
  title="Sitemap | Ayala Pro Painting",
  description="Complete sitemap of the Ayala Pro Painting website. Find all pages including services, service areas, resources, and company information.",
  canonical=f"{BASE}/sitemap/",
  robots=NOINDEX,
  schemas=[
    page_schema("WebPage", "Sitemap", "Complete list of all pages on the Ayala Pro Painting website.", f"{BASE}/sitemap/"),
    breadcrumb([("Home", "/"), ("Sitemap", f"{BASE}/sitemap/")])],
  body="\n\n".join([
    light_header("Sitemap", "Sitemap",
      "Every page on the Ayala Pro Painting website, organized by section. Looking for something specific? Use the links below.",
      [("Home", "/"), ("Sitemap", None)]),
    sitemap_section([
      link_group("Main Pages", _main),
      link_group("Services", _services),
      link_group("Service Areas", _areas),
      link_group("Resources", _resources),
      link_group("Legal &amp; Utility", _legal),
    ]),
  ]),
))
