#!/usr/bin/env python3
"""Gera o site estático da Distribuidora Pamma.

Cada aba vira uma página própria (pasta/index.html) com header e footer comuns.
Edite o conteúdo em src/pages/*.html e rode:  python3 tools/build.py
Placeholders: {{R}} = caminho relativo até a raiz (ex.: "" ou "../").
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
SITE_URL = "https://distribuidorapamma.com"

# slug -> (arquivo de saída, título, descrição, item de menu ativo)
PAGES = {
    "home": ("index.html", "Distribuidora Pamma | Distribuidora B2B de eletro e informática em Alphaville",
             "Distribuidora B2B em Alphaville/Barueri com mais de 25 marcas de eletrônicos, informática e eletroportáteis. Pedido mínimo R$ 1.000 FOB e frete CIF no Sudeste a partir de R$ 5.000.", "home"),
    "marcas": ("marcas/index.html", "Marcas e categorias | Distribuidora Pamma",
               "Samsung, LG, Britânia, Philco, Dell, Lenovo e mais de 25 marcas para revendas e empresas. Conheça as categorias da Distribuidora Pamma.", "marcas"),
    "empresa": ("empresa/index.html", "Empresa e estrutura | Distribuidora Pamma",
                "Escritório e centro de distribuição próprios na Alameda Tucunaré, Alphaville, Barueri/SP.", "empresa"),
    "politica": ("politica-comercial/index.html", "Política comercial | Distribuidora Pamma",
                 "Pedido mínimo R$ 1.000 FOB, frete CIF Sudeste a partir de R$ 5.000, faturamento em 28 dias e boleto mediante análise de crédito.", "politica"),
    "contato": ("contato/index.html", "Contato e cotação | Distribuidora Pamma",
                "Solicite sua cotação pelo WhatsApp (11) 91175-2030 ou pelo formulário. Alameda Tucunaré, Alphaville, Barueri/SP.", "contato"),
    "404": ("404.html", "Página não encontrada | Distribuidora Pamma", "Página não encontrada.", ""),
}

NAV = [
    ("home", "", "Início"),
    ("marcas", "marcas/", "Marcas"),
    ("empresa", "empresa/", "Empresa"),
    ("politica", "politica-comercial/", "Política comercial"),
    ("contato", "contato/", "Contato"),
]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2Zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.25-8.24 4.54 0 8.24 3.7 8.24 8.24 0 4.55-3.7 8.24-8.24 8.24Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.25-.64.81-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.23.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28Z"/></symbol>
<symbol id="i-ig" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/></g><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path fill="currentColor" d="M12 22s-8-6.46-8-12.5a8 8 0 0 1 16 0C20 15.54 12 22 12 22Zm0-9a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Z"/></symbol>
<symbol id="i-box" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5v-9Z"/><path d="m3 7.5 9 4.5 9-4.5M12 12v9"/></g></symbol>
<symbol id="i-tv" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></g></symbol>
<symbol id="i-laptop" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="4" width="14" height="10" rx="1.5"/><path d="M2.5 18h19l-1.5-4H4l-1.5 4Z"/></g></symbol>
<symbol id="i-blender" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h10l-1.5 10h-7L7 3Z"/><path d="M7.5 13h9l1 7h-11l1-7ZM12 16.5h.01"/></g></symbol>
<symbol id="i-fan" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="10" r="1.6"/><path d="M12 8.4c0-3 1-5.4 3-5.4s2.4 3-3 5.4ZM13.4 10.8c2.6 1.5 4.2 3.5 3.2 5.2s-3.8.5-3.2-5.2ZM10.6 10.8c-2.6 1.5-5.1 1.9-6.1.2s1.6-3.6 6.1-.2ZM12 11.6V21M8 21h8"/></g></symbol>
<symbol id="i-truck" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M2 6h12v10H2zM14 9h4l4 4v3h-8z"/><circle cx="6" cy="18" r="2" fill="#fff"/><circle cx="18" cy="18" r="2" fill="#fff"/></g></symbol>
<symbol id="i-doc" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h6"/></g></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></g></symbol>
<symbol id="i-card" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18M7 15h4"/></g></symbol>
<symbol id="i-cart" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h2l2.4 11h10.2L20 8H6.2"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/></g></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 3 4 6v6c0 4.5 3.4 8 8 9 4.6-1 8-4.5 8-9V6l-8-3Z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></g></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/></symbol>
</svg>"""

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23163f73'/%3E"
           "%3Ctext x='32' y='45' font-family='Arial,Helvetica,sans-serif' font-size='38' font-weight='700' fill='%23fff' text-anchor='middle'%3EP%3C/text%3E%3C/svg%3E")

SCHEMA = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WholesaleStore","name":"Distribuidora Pamma",
"url":"https://distribuidorapamma.com/","image":"https://distribuidorapamma.com/assets/img/og-pamma.jpg",
"telephone":"+55-11-91175-2030",
"address":{"@type":"PostalAddress","streetAddress":"Alameda Tucunaré","addressLocality":"Barueri","addressRegion":"SP","addressCountry":"BR"},
"areaServed":"BR","sameAs":["https://www.instagram.com/distribuidorapamma/"]}
</script>"""


def asset_version():
    h = hashlib.sha1()
    for f in ("assets/css/site.css", "assets/js/site.js"):
        h.update((ROOT / f).read_bytes())
    return h.hexdigest()[:8]


VER = None


def layout(slug, body):
    out, title, desc, active = PAGES[slug]
    depth = out.count("/")
    R = "/" if slug == "404" else "../" * depth  # 404 é servido em qualquer caminho
    path = "" if out in ("index.html", "404.html") else out.replace("index.html", "")
    canonical = f"{SITE_URL}/{path}"

    nav = "\n".join(
        f'<a href="{R}{href}"' + (' aria-current="page"' if key == active else "") + f">{label}</a>"
        for key, href, label in NAV
    )
    noindex = '<meta name="robots" content="noindex" />' if slug == "404" else ""

    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta name="theme-color" content="#163f73" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  {noindex}
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="pt_BR" />
  <meta property="og:site_name" content="Distribuidora Pamma" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{SITE_URL}/assets/img/og-pamma.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" href="{FAVICON}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" />
  <link rel="stylesheet" href="{R}assets/css/site.css?v={VER}" />
  {SCHEMA if slug == "home" else ""}
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
{ICONS}

<header class="site-header" id="siteHeader">
  <nav class="wrap" aria-label="Principal">
    <a class="brand" href="{R or './'}" aria-label="Distribuidora Pamma — início">
      <span class="brand-mark" aria-hidden="true">P</span>
      <span class="brand-txt"><span class="logo">PAMMA</span><small>Distribuidora B2B</small></span>
    </a>
    <div class="navlinks" id="navlinks">
{nav}
    </div>
    <div class="nav-right">
      <a class="btn btn-wa btn-sm js-wa hdr-wa" href="{R}contato/">
        <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg><span>Solicitar cotação</span>
      </a>
      <button class="icon-btn menu-btn" id="menuBtn" aria-label="Abrir menu" aria-expanded="false" aria-controls="navlinks">
        <svg class="ico" aria-hidden="true"><use href="#i-menu"/></svg>
      </button>
    </div>
  </nav>
</header>

<main id="conteudo">
{body.replace("{{R}}", R)}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{R or './'}"><span class="brand-mark" aria-hidden="true">P</span><span class="brand-txt"><span class="logo">PAMMA</span><small>Distribuidora B2B</small></span></a>
        <p style="max-width:360px; line-height:1.65; margin:18px 0 0">Distribuidora B2B de eletrônicos, informática e eletroportáteis para empresas e revendedores.</p>
        <!-- TODO: inserir razão social e CNPJ oficiais -->
      </div>
      <div>
        <h4>Navegação</h4>
        <ul>
          <li><a href="{R or './'}">Início</a></li>
          <li><a href="{R}marcas/">Marcas</a></li>
          <li><a href="{R}empresa/">Empresa</a></li>
          <li><a href="{R}politica-comercial/">Política comercial</a></li>
          <li><a href="{R}contato/">Contato</a></li>
        </ul>
      </div>
      <div>
        <h4>Atendimento</h4>
        <ul>
          <li><a class="js-wa" href="{R}contato/">WhatsApp (11) 91175-2030</a></li>
          <li><a class="ig-text" href="https://www.instagram.com/distribuidorapamma/" target="_blank" rel="noopener"><svg class="ico" aria-hidden="true"><use href="#i-ig"/></svg> Instagram</a></li>
        </ul>
      </div>
      <div>
        <h4>Endereço</h4>
        <ul>
          <li><a href="https://www.google.com/maps/search/?api=1&amp;query=Alameda+Tucunar%C3%A9+Alphaville+Barueri+SP" target="_blank" rel="noopener">Alameda Tucunaré<br>Alphaville • Barueri/SP</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year"></span> Distribuidora Pamma. Todos os direitos reservados.</span>
      <span>Marcas citadas pertencem aos respectivos titulares.</span>
    </div>
  </div>
</footer>

<a class="fab js-wa" href="{R}contato/" aria-label="Falar no WhatsApp"><svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg></a>
<script src="{R}assets/js/site.js?v={VER}" defer></script>
</body>
</html>
"""
    dest = ROOT / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    return out


def sitemap():
    urls = [o.replace("index.html", "") for s, (o, *_ ) in PAGES.items() if s != "404"]
    items = "\n".join(f"  <url><loc>{SITE_URL}/{u}</loc></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}\n</urlset>\n',
        encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    VER = asset_version()
    for slug in PAGES:
        body = (SRC / "pages" / f"{slug}.html").read_text(encoding="utf-8")
        print("gerado:", layout(slug, body))
    sitemap()
    print("gerado: sitemap.xml, robots.txt")
