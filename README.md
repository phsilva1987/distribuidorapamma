# Distribuidora Pamma — site institucional

Site estático (HTML + CSS + JS, sem dependências) da Distribuidora Pamma.
Uma página por aba, no mesmo padrão do BrMoveToGo:

| Página | Arquivo gerado | Conteúdo-fonte |
|---|---|---|
| Início | `index.html` | `src/pages/home.html` |
| Marcas | `marcas/index.html` | `src/pages/marcas.html` |
| Empresa | `empresa/index.html` | `src/pages/empresa.html` |
| Política comercial | `politica-comercial/index.html` | `src/pages/politica.html` |
| Contato | `contato/index.html` | `src/pages/contato.html` |
| Erro 404 | `404.html` | `src/pages/404.html` |

Header, footer, SEO (title, description, Open Graph, canonical) e ícones ficam em `tools/build.py`.

## Como editar

1. Altere o conteúdo em `src/pages/*.html` (ou header/footer em `tools/build.py`).
2. Gere as páginas: `python3 tools/build.py`
3. Teste localmente: `python3 -m http.server 8000` e abra http://localhost:8000
4. Faça commit dos arquivos gerados junto com a fonte.

Estilos: `assets/css/site.css` · Scripts: `assets/js/site.js` · Imagens: `assets/img/`

## Configurações importantes

- **WhatsApp comercial:** variável `WA_NUMBER` em `assets/js/site.js` (`5511911752030`). Todos os botões usam esse número.
- **Instagram:** https://www.instagram.com/distribuidorapamma/ (header, home, contato e rodapé).
- **Domínio:** `distribuidorapamma.com` (constante `SITE_URL` em `tools/build.py`).

## Pendências de conteúdo

- [ ] Razão social e CNPJ no rodapé
- [ ] E-mail comercial
- [ ] Número na Alameda Tucunaré
- [ ] Logo oficial em SVG/PNG (hoje o "PAMMA" é texto estilizado)
