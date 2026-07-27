# -*- coding: utf-8 -*-
"""Spanish landing page (/es/). No dedicated dev guide — authored from the homepage
structure per the strategy's bilingual differentiator. Self-contained Spanish header
and footer (same classes as the English partials so all CSS/JS keep working)."""
import json
from build import BASE, breadcrumb, faqpage

PHONE = "(813) 555-0199"

# --------------------------------------------------------------- Spanish header
ES_HEADER = '''  <!-- BARRA DE ANUNCIO -->
  <div id="announcement-bar" class="announcement-bar" role="complementary" aria-label="Anuncio">
    <div class="announcement-bar__content">
      <p>Programe su estimado de pintura gratis hoy &mdash;
        <a href="/es/#contacto" class="announcement-bar__link" data-cta="announcement_bar">&iexcl;ahora sirviendo Riverview, Brandon y todo el sur del condado de Hillsborough!</a>
      </p>
    </div>
    <button class="announcement-bar__close" aria-label="Cerrar anuncio" type="button">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
        <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
      </svg>
    </button>
  </div>

  <header class="header" id="site-header" role="banner">
    <a href="#main-content" class="skip-link">Saltar al contenido principal</a>
    <div class="header__container">
      <button class="header__hamburger" aria-label="Abrir men&uacute;" aria-expanded="false" aria-controls="main-nav" type="button">
        <span class="header__hamburger-line"></span>
        <span class="header__hamburger-line"></span>
        <span class="header__hamburger-line"></span>
      </button>
      <a href="/es/" class="header__logo" aria-label="Ayala Pro Painting - Inicio">
        <img src="/images/logo.svg" alt="Ayala Pro Painting" width="180" height="48">
      </a>
      <nav class="header__nav" id="main-nav" role="navigation" aria-label="Navegaci&oacute;n principal">
        <ul class="header__nav-list">
          <li class="header__nav-item header__nav-item--dropdown">
            <a href="/services/" class="header__nav-link" aria-haspopup="true" aria-expanded="false">Servicios</a>
            <ul class="header__dropdown" role="menu">
              <li><a href="/services/interior-painting/" role="menuitem">Pintura Interior</a></li>
              <li><a href="/services/exterior-painting/" role="menuitem">Pintura Exterior</a></li>
              <li><a href="/services/cabinet-painting/" role="menuitem">Pintura de Gabinetes</a></li>
              <li><a href="/services/commercial-painting/" role="menuitem">Pintura Comercial</a></li>
              <li><a href="/services/pressure-washing/" role="menuitem">Lavado a Presi&oacute;n</a></li>
              <li class="header__dropdown-all"><a href="/services/" role="menuitem">Todos los Servicios &rarr;</a></li>
            </ul>
          </li>
          <li class="header__nav-item header__nav-item--dropdown">
            <a href="/areas/" class="header__nav-link" aria-haspopup="true" aria-expanded="false">&Aacute;reas que Servimos</a>
            <ul class="header__dropdown" role="menu">
              <li><a href="/areas/riverview/" role="menuitem">Riverview</a></li>
              <li><a href="/areas/brandon/" role="menuitem">Brandon</a></li>
              <li><a href="/areas/valrico/" role="menuitem">Valrico</a></li>
              <li><a href="/areas/fish-hawk/" role="menuitem">Fish Hawk</a></li>
              <li><a href="/areas/apollo-beach/" role="menuitem">Apollo Beach</a></li>
              <li class="header__dropdown-all"><a href="/areas/" role="menuitem">Todas las &Aacute;reas &rarr;</a></li>
            </ul>
          </li>
          <li class="header__nav-item"><a href="/gallery/" class="header__nav-link">Nuestro Trabajo</a></li>
          <li class="header__nav-item"><a href="/about/" class="header__nav-link">Acerca de</a></li>
          <li class="header__nav-item"><a href="/" class="header__nav-link" lang="en" hreflang="en">English</a></li>
        </ul>
      </nav>
      <div class="header__actions">
        <a href="tel:8135550199" class="header__phone" data-phone aria-label="Llame al (813) 555-0199">
          <svg class="header__phone-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>
          </svg>
          <span class="header__phone-text">(813) 555-0199</span>
          <span class="header__phone-icon-mobile sr-only">Ll&aacute;menos</span>
        </a>
        <a href="/es/#contacto" class="btn btn--primary header__cta" data-cta="header">Estimado Gratis</a>
      </div>
    </div>
  </header>
  <div class="nav-backdrop" id="nav-backdrop" hidden></div>'''

# --------------------------------------------------------------- Spanish footer
ES_FOOTER = '''  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__col footer__company">
          <a href="/es/" class="footer__logo" aria-label="Ayala Pro Painting - Inicio">
            <img src="/images/logo-white.svg" alt="Ayala Pro Painting" width="150" height="40">
          </a>
          <p class="footer__tagline">Pintura profesional para Riverview y Tampa Bay.</p>
          <div class="footer__social">
            <a href="https://www.facebook.com/ayalapropainting" target="_blank" rel="noopener noreferrer" data-outbound aria-label="Ayala Pro Painting en Facebook">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12a10 10 0 1 0-11.56 9.88v-6.99H7.9V12h2.54V9.8c0-2.5 1.49-3.89 3.78-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56V12h2.78l-.44 2.89h-2.34v6.99A10 10 0 0 0 22 12z"/></svg>
            </a>
            <a href="https://www.instagram.com/ayalapropainting" target="_blank" rel="noopener noreferrer" data-outbound aria-label="Ayala Pro Painting en Instagram">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
            </a>
            <a href="https://www.google.com/maps" target="_blank" rel="noopener noreferrer" data-outbound aria-label="Ayala Pro Painting en Google">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>
            </a>
          </div>
        </div>
        <div class="footer__col">
          <h2 class="footer__title">Servicios</h2>
          <ul class="footer__links">
            <li><a href="/services/interior-painting/">Pintura Interior</a></li>
            <li><a href="/services/exterior-painting/">Pintura Exterior</a></li>
            <li><a href="/services/cabinet-painting/">Pintura de Gabinetes</a></li>
            <li><a href="/services/commercial-painting/">Pintura Comercial</a></li>
            <li><a href="/services/pressure-washing/">Lavado a Presi&oacute;n</a></li>
            <li><a href="/services/">Todos los Servicios</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h2 class="footer__title">&Aacute;reas de Servicio</h2>
          <ul class="footer__links">
            <li><a href="/areas/riverview/">Riverview</a></li>
            <li><a href="/areas/brandon/">Brandon</a></li>
            <li><a href="/areas/valrico/">Valrico</a></li>
            <li><a href="/areas/fish-hawk/">Fish Hawk</a></li>
            <li><a href="/areas/apollo-beach/">Apollo Beach</a></li>
            <li><a href="/areas/">Todas las &Aacute;reas</a></li>
          </ul>
        </div>
        <div class="footer__col footer__contact">
          <h2 class="footer__title">Contacto</h2>
          <p><a href="tel:8135550199" data-phone>(813) 555-0199</a></p>
          <p><a href="mailto:info@ayalapropainting.com">info@ayalapropainting.com</a></p>
          <p>Riverview, FL 33578</p>
          <p>Lun&ndash;S&aacute;b 7:00 AM &ndash; 6:00 PM</p>
          <a href="/es/#contacto" class="btn btn--primary footer__cta" data-cta="footer">Estimado Gratis</a>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; 2026 Ayala Pro Painting. Todos los derechos reservados.</span>
      <nav class="footer__legal" aria-label="Legal">
        <a href="/privacy/">Pol&iacute;tica de Privacidad</a>
        <a href="/terms/">T&eacute;rminos de Servicio</a>
        <a href="/accessibility/">Accesibilidad</a>
        <a href="/" lang="en" hreflang="en">English</a>
      </nav>
    </div>
  </footer>

  <div class="sticky-cta" id="sticky-cta" aria-label="Acciones r&aacute;pidas" role="complementary">
    <a href="tel:8135550199" class="sticky-cta__btn sticky-cta__btn--phone" data-phone data-section="mobile_sticky_bar" aria-label="Llamar a Ayala Pro Painting">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>
      </svg>
      <span>Llamar</span>
    </a>
    <a href="/es/#contacto" class="sticky-cta__btn sticky-cta__btn--estimate" data-cta="mobile_sticky_bar">
      <span>Estimado Gratis</span>
    </a>
  </div>'''

# --------------------------------------------------------------- Spanish FAQ
_es_faq = [
 ("¿Cuánto cuesta pintar el interior de una casa en Riverview, FL?",
  "El costo de pintar el interior en Riverview generalmente varía de $2,500 a $5,500 para una casa estándar de 3 habitaciones, dependiendo del número de cuartos, la altura de los techos, la condición de las paredes y el número de manos de pintura. Incluye toda la preparación, el sellador, dos manos de pintura premium y la limpieza completa."),
 ("¿Con qué frecuencia se debe repintar el exterior de una casa en Florida?",
  "En el clima de Tampa Bay, el exterior generalmente necesita repintarse cada 5 a 7 años — antes que en climas más fríos — debido al sol intenso, la humedad y las tormentas de Florida. Usamos productos premium y una preparación minuciosa para que el acabado dure el mayor tiempo posible."),
 ("¿Ofrecen servicio en español?",
  "Sí. Eliseo y nuestro equipo brindan servicio completo en español e inglés. Desde el estimado inicial hasta la finalización del proyecto, nos comunicamos en el idioma que usted prefiera."),
 ("¿Están licenciados y asegurados?",
  "Por supuesto. Ayala Pro Painting es un contratista de pintura licenciado en Florida con seguro de responsabilidad civil de $1 millón y cobertura de compensación laboral. Con gusto proporcionamos un certificado de seguro a su HOA o administrador de propiedad."),
]

CHECK = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>')

def _svc(href, title, desc):
    return (f'<a href="{href}" class="service-card" data-cta="service_card"><h3 class="service-card__title">{title}</h3>'
            f'<p class="service-card__desc">{desc}</p><span class="service-card__link">Más Información &rarr;</span></a>')

def _why(title, desc):
    return f'<div class="feature-card"><h3>{title}</h3><p>{desc}</p></div>'

def _faq_html():
    items = ""
    for q, a in _es_faq:
        items += (f'<div class="faq__item"><button class="faq__question" aria-expanded="false">{q}'
                  f'<span class="faq__icon" aria-hidden="true">+</span></button>'
                  f'<div class="faq__answer"><div class="faq__answer-inner">{a}</div></div></div>')
    return items

_areas_links = "".join(f'<a href="{u}">{n}</a>' for n, u in [
    ("Riverview", "/areas/riverview/"), ("Brandon", "/areas/brandon/"), ("Valrico", "/areas/valrico/"),
    ("Lithia", "/areas/lithia/"), ("Fish Hawk", "/areas/fish-hawk/"), ("Apollo Beach", "/areas/apollo-beach/"),
    ("Sun City Center", "/areas/sun-city-center/"), ("Ruskin", "/areas/ruskin/")]) + '<a href="/areas/">Todas las &Aacute;reas &rarr;</a>'

BODY = f'''    <!-- Hero -->
    <section class="hero" id="hero" aria-label="Ayala Pro Painting" data-section="hero">
      <picture class="hero__bg">
        <img src="/images/hero-homepage.svg" alt="Pintores profesionales completando un proyecto de pintura exterior en un vecindario de Riverview, FL" width="1920" height="1080" fetchpriority="high">
      </picture>
      <div class="hero__overlay"></div>
      <div class="container">
        <div class="hero__content">
          <p class="hero__eyebrow">Con Licencia y Asegurado &nbsp;|&nbsp; Riverview, FL</p>
          <h1 class="hero__title">Pintores Profesionales en Riverview, FL en Quienes Puede Confiar</h1>
          <p class="hero__text">Ayala Pro Painting es una compa&ntilde;&iacute;a de pintura residencial y comercial de propiedad local que sirve a Riverview, Florida y el sur del condado de Hillsborough. Dirigida por su due&ntilde;o, Eliseo Ayala, ofrecemos pintura interior, pintura exterior, renovaci&oacute;n de gabinetes y recubrimientos comerciales con la responsabilidad personal del due&ntilde;o en cada trabajo. Usamos productos premium resistentes a la humedad de Sherwin-Williams y Benjamin Moore para acabados que resisten el sol, las tormentas y el aire salino de Tampa Bay. Llame hoy para su estimado de pintura gratis y sin compromiso.</p>
          <div class="hero__ctas">
            <a href="/es/#contacto" class="btn btn--primary btn--lg" data-cta="hero">Obtenga su Estimado Gratis</a>
            <a href="tel:8135550199" class="btn btn--outline-white btn--lg" data-phone>Llame al (813) 555-0199</a>
          </div>
          <p class="hero__trust">&#9733; Calificaci&oacute;n 5 Estrellas &nbsp;&bull;&nbsp; Con Licencia y Asegurado &nbsp;&bull;&nbsp; Estimados Gratis &nbsp;&bull;&nbsp; Garant&iacute;a de 2 A&ntilde;os</p>
        </div>
      </div>
    </section>

    <!-- Servicios -->
    <section class="section section--white" aria-labelledby="serv-heading" data-section="services_grid">
      <div class="container">
        <p class="section-eyebrow">Nuestros Servicios</p>
        <h2 id="serv-heading" class="section-title">&iquest;Qu&eacute; Servicios de Pintura Ofrecemos en Riverview?</h2>
        <p class="section-subtitle">Desde refrescar un solo cuarto hasta repintar un edificio comercial entero, Ayala Pro Painting ofrece soluciones de pintura completas, adaptadas al clima &uacute;nico de Riverview. Cada proyecto incluye preparaci&oacute;n detallada, productos premium y una garant&iacute;a escrita.</p>
        <div class="services__grid">
          {_svc("/services/interior-painting/", "Pintura Interior", "Paredes, techos, molduras y puertas con preparaci&oacute;n meticulosa y acabados duraderos resistentes a la humedad de Florida.")}
          {_svc("/services/exterior-painting/", "Pintura Exterior", "Recubrimientos resistentes a los rayos UV y al clima, con nuestro proceso de preparaci&oacute;n de 7 pasos hecho para Florida.")}
          {_svc("/services/cabinet-painting/", "Pintura de Gabinetes", "Renovaci&oacute;n de gabinetes de cocina y ba&ntilde;o con un acabado liso de calidad de f&aacute;brica, en cualquier color.")}
          {_svc("/services/commercial-painting/", "Pintura Comercial", "Oficinas, locales comerciales, HOAs y propiedades multifamiliares con m&iacute;nima interrupci&oacute;n a su negocio.")}
          {_svc("/services/pressure-washing/", "Lavado a Presi&oacute;n", "Limpieza profesional de entradas, terrazas, cercas y exteriores antes de pintar o como servicio independiente.")}
          {_svc("/services/deck-patio-staining/", "Tinte de Terrazas y Patios", "Tintes y selladores premium dise&ntilde;ados para la exposici&oacute;n al sol y la humedad de Florida.")}
        </div>
        <div class="services__cta"><a href="/services/" class="btn btn--secondary" data-cta="services_all">Ver Todos los Servicios</a></div>
      </div>
    </section>

    <!-- Por qué elegirnos -->
    <section class="section section--cream" aria-labelledby="why-heading">
      <div class="container">
        <p class="section-eyebrow">Por Qu&eacute; Ayala Pro Painting</p>
        <h2 id="why-heading" class="section-title">&iquest;Por Qu&eacute; Conf&iacute;an en Nosotros en Riverview?</h2>
        <div class="feature-grid">
          {_why("El Due&ntilde;o en Cada Trabajo", "Eliseo supervisa personalmente cada proyecto, desde el estimado inicial hasta la inspecci&oacute;n final.")}
          {_why("Servicio Biling&uuml;e", "Servicio completo en espa&ntilde;ol e ingl&eacute;s &mdash; estimados, comunicaci&oacute;n y manejo del proyecto en el idioma que prefiera.")}
          {_why("Productos para Florida", "Pinturas premium resistentes a la humedad, formuladas para el sol y la humedad de Tampa Bay.")}
          {_why("Precios Transparentes", "Estimados detallados por escrito. Sin cargos sorpresa, sin tarifas ocultas.")}
          {_why("Garant&iacute;a Escrita", "Cada proyecto residencial respaldado por una garant&iacute;a de mano de obra de 2 a&ntilde;os por escrito.")}
          {_why("Con Licencia y Asegurado", "Contratista licenciado en Florida con $1 mill&oacute;n en responsabilidad civil y compensaci&oacute;n laboral.")}
        </div>
      </div>
    </section>

    <!-- Áreas -->
    <section class="section section--white area-callout" aria-labelledby="areas-heading">
      <div class="container">
        <h2 id="areas-heading" class="section-title">Servimos Riverview y el Sur del Condado de Hillsborough</h2>
        <p class="section-subtitle">Con orgullo servimos a propietarios y negocios en toda la regi&oacute;n:</p>
        <div class="area-callout__list">{_areas_links}</div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section section--cream" aria-labelledby="faq-heading" data-section="faq">
      <div class="container">
        <p class="section-eyebrow">Preguntas Frecuentes</p>
        <h2 id="faq-heading" class="section-title">Preguntas Comunes Sobre Pintura en Riverview</h2>
        <div class="faq">{_faq_html()}</div>
      </div>
    </section>

    <!-- CTA / Contacto -->
    <section class="cta-banner" id="contacto" data-section="bottom_cta_banner">
      <div class="container">
        <div class="cta-banner__inner">
          <h2 class="cta-banner__title">&iquest;Listo para Transformar su Propiedad?</h2>
          <p class="cta-banner__text">Obtenga un estimado gratis y sin compromiso de los profesionales de pintura de confianza de Riverview. La mayor&iacute;a de los estimados se entregan en 24&ndash;48 horas.</p>
          <div class="cta-banner__ctas">
            <a href="/contact/" class="btn btn--primary btn--lg" data-cta="bottom_cta_banner">Obtenga su Estimado Gratis</a>
            <a href="tel:8135550199" class="btn btn--outline-white btn--lg" data-phone>Llame al (813) 555-0199</a>
          </div>
        </div>
      </div>
    </section>'''

_es_localbusiness = json.dumps({
    "@context": "https://schema.org", "@type": "HousePainter", "name": "Ayala Pro Painting",
    "description": "Compañía de pintura residencial y comercial de propiedad local en Riverview, FL y el área de Tampa Bay.",
    "url": f"{BASE}/es/", "telephone": "+1-813-555-0199", "email": "info@ayalapropainting.com",
    "address": {"@type": "PostalAddress", "addressLocality": "Riverview", "addressRegion": "FL",
                "postalCode": "33578", "addressCountry": "US"},
    "areaServed": {"@type": "City", "name": "Riverview"},
    "openingHours": "Mo-Sa 07:00-18:00", "priceRange": "$$"
}, ensure_ascii=False, indent=2)

HREFLANG = ('<link rel="alternate" hreflang="en" href="https://ayalapropainting.com/">\n'
            '  <link rel="alternate" hreflang="es" href="https://ayalapropainting.com/es/">\n'
            '  <link rel="alternate" hreflang="x-default" href="https://ayalapropainting.com/">')

PAGES = [dict(
  slug="es",
  title="Pintores en Riverview FL | Ayala Pro Painting | Estimados Gratis",
  description="Pintura residencial y comercial profesional en Riverview, FL. Con licencia, asegurada y de propiedad local. Servicio en español. ¡Llame para su estimado gratis!",
  canonical=f"{BASE}/es/",
  lang="es",
  head_extra=HREFLANG,
  header=ES_HEADER,
  footer=ES_FOOTER,
  schemas=[
    _es_localbusiness,
    breadcrumb([("Inicio", "/es/")]),
    faqpage(_es_faq)],
  body=BODY,
)]
