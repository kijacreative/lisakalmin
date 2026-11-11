// Inner pages: the mobile menu.
(function () {
  var root = document.documentElement, burger = document.getElementById('burger'), sheet = document.getElementById('sheet');
  if (!burger || !sheet) return;
  function setMenu(open) {
    root.classList.toggle('menu-open', open);
    sheet.hidden = !open;
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    if (open) sheet.querySelector('a').focus();
  }
  burger.addEventListener('click', function () { setMenu(!root.classList.contains('menu-open')); });
  addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('menu-open')) { setMenu(false); burger.focus(); } });
  sheet.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
})();
