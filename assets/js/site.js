// Distribuidora Pamma — scripts compartilhados
(function () {
  // Número único do comercial (DDI + DDD + número). Alterar somente aqui.
  var WA_NUMBER = '5511911752030';
  var waLink = function (msg) {
    return 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(msg || 'Olá!');
  };

  // Links de WhatsApp
  document.querySelectorAll('.js-wa').forEach(function (a) {
    a.href = waLink(a.dataset.msg || 'Olá! Gostaria de solicitar uma cotação com a Distribuidora Pamma.');
    a.target = '_blank';
    a.rel = 'noopener';
  });

  // Ano no rodapé
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Menu mobile
  var btn = document.getElementById('menuBtn');
  var nav = document.getElementById('navlinks');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Animação de entrada
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // Formulário → WhatsApp
  var form = document.getElementById('leadForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = function (id) { var el = form.querySelector('#' + id); return el ? el.value.trim() : ''; };
      var missing = ['nome', 'empresa', 'telefone'].filter(function (id) { return !v(id); })[0];
      if (missing) { form.querySelector('#' + missing).focus(); form.reportValidity(); return; }

      var linhas = [
        'Olá! Sou ' + v('nome') + ', da empresa ' + v('empresa') + '.',
        '',
        'WhatsApp: ' + v('telefone'),
        v('cnpj') ? 'CNPJ: ' + v('cnpj') : null,
        'Cidade/UF: ' + (v('cidade') || '-'),
        v('categoria') ? 'Categoria: ' + v('categoria') : null,
        '',
        'Gostaria de solicitar uma cotação.',
        v('mensagem')
      ].filter(function (l) { return l !== null; });

      window.open(waLink(linhas.join('\n')), '_blank', 'noopener');
    });
  }
})();
