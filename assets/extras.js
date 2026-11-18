/* Cookie bar and quiz pop-up, shared by every page.
   - Cookie bar: shows until the visitor chooses. "Accept" turns on analytics cookies through
     Google consent mode (the defaults are set in each page's <head>). Stored in localStorage lk_consent.
   - Quiz pop-up: opens the first time the visitor scrolls. Closing it, or finishing the quiz,
     hides it for 30 days (localStorage lk_quizpop_until). Clicking through to the quiz hides it
     for the rest of the visit. Never on the quiz or masterclass pages, never for masterclass
     attendees arriving on the course page with ?code=, never once they have clicked to check out. */
(function () {
  var DAY = 864e5;
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    sget: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    sset: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  };
  // the quiz page calls this when a result is shown
  window.lkQuizDone = function () { store.set('lk_quizpop_until', String(Date.now() + 30 * DAY)); };

  var css = '' +
    '.lkc{position:fixed;left:16px;right:16px;bottom:16px;z-index:60;max-width:880px;margin:0 auto;display:flex;align-items:center;gap:16px 24px;flex-wrap:wrap;' +
    'background:#141B16;color:#F8F4EC;border:1px solid rgba(227,181,188,.22);border-radius:18px;padding:16px 20px;box-shadow:0 18px 40px -16px rgba(0,0,0,.55);' +
    "font:400 15px/1.5 'Jost',system-ui,sans-serif;transform:translateY(20px);opacity:0;transition:opacity .25s,transform .25s}" +
    '.lkc.on{transform:none;opacity:1}' +
    '.lkc p{margin:0;flex:1 1 320px;color:rgba(248,244,236,.85)}' +
    '.lkc .b{display:flex;gap:10px;flex:0 0 auto}' +
    ".lkc button{min-height:44px;padding:10px 22px;border-radius:999px;font:700 15px/1 'Jost',system-ui,sans-serif;cursor:pointer;border:1px solid rgba(248,244,236,.4);background:transparent;color:#F8F4EC}" +
    '.lkc button.y{background:#A04E5C;border-color:#A04E5C;color:#fff}' +
    '.lkc button.y:hover{background:#873F4C}.lkc button:not(.y):hover{background:rgba(248,244,236,.08)}' +
    '.lkq{position:fixed;inset:0;z-index:50;display:grid;place-items:center;padding:20px;background:rgba(20,27,22,.62);opacity:0;transition:opacity .25s}' +
    '.lkq.on{opacity:1}' +
    '.lkq .box{position:relative;width:min(520px,100%);max-height:calc(100vh - 40px);overflow:auto;background:#F8F4EC;color:#232C26;border-radius:20px;padding:clamp(28px,5vw,44px);box-shadow:0 30px 70px -20px rgba(0,0,0,.55);transform:translateY(12px);transition:transform .25s;text-align:left}' +
    '.lkq.on .box{transform:none}' +
    ".lkq .k{margin:0 0 12px;font:500 12px/1.4 'Jost',system-ui,sans-serif;letter-spacing:.3em;text-transform:uppercase;color:#A04E5C}" +
    ".lkq h2{margin:0 0 14px;font-family:'Plus Jakarta Sans','Jost',system-ui,sans-serif;font-weight:800;font-size:clamp(26px,4vw,32px);line-height:1.12;letter-spacing:-.01em;color:#2F3B33}" +
    ".lkq .t{margin:0 0 24px;color:#56635B;font:400 17px/1.55 'Jost',system-ui,sans-serif}" +
    ".lkq .go{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:54px;padding:14px 24px;border-radius:999px;background:#A04E5C;color:#fff;font:700 18px/1.2 'Jost',system-ui,sans-serif;text-decoration:none;box-sizing:border-box}" +
    '.lkq .go:hover{background:#873F4C}' +
    ".lkq .no{display:block;margin:14px auto 0;background:none;border:0;color:#56635B;font:400 15px 'Jost',system-ui,sans-serif;text-decoration:underline;text-underline-offset:4px;cursor:pointer}" +
    '.lkq .x{position:absolute;top:12px;right:12px;width:40px;height:40px;border-radius:50%;border:0;background:transparent;color:#56635B;font-size:26px;line-height:1;cursor:pointer}' +
    '.lkq .x:hover{background:#E9E3D6}' +
    '@media (max-width:560px){.lkc{left:10px;right:10px;bottom:10px;padding:14px 16px}.lkc .b{width:100%}.lkc button{flex:1}}' +
    '@media (prefers-reduced-motion:reduce){.lkc,.lkq,.lkq .box{transition:none}}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  function ready(fn) { if (document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn); }

  ready(function () {
    /* ---------- cookie bar ---------- */
    if (!store.get('lk_consent')) {
      var bar = document.createElement('div');
      bar.className = 'lkc'; bar.setAttribute('role', 'region'); bar.setAttribute('aria-label', 'Cookie consent');
      bar.innerHTML = '<p>We use cookies to understand how visitors use this site, so we can make it better. Is that okay with you?</p>' +
        '<div class="b"><button type="button" data-c="denied">Decline</button><button type="button" class="y" data-c="granted">Accept cookies</button></div>';
      document.body.appendChild(bar);
      requestAnimationFrame(function () { requestAnimationFrame(function () { bar.classList.add('on'); }); });
      bar.addEventListener('click', function (e) {
        var b = e.target.closest('[data-c]'); if (!b) return;
        var v = b.getAttribute('data-c');
        store.set('lk_consent', v);
        if (v === 'granted' && typeof window.gtag === 'function') {
          window.gtag('consent', 'update', { ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted', analytics_storage: 'granted' });
          (window.dataLayer = window.dataLayer || []).push({ event: 'cookie_consent_granted' });
        }
        bar.classList.remove('on'); setTimeout(function () { bar.remove(); }, 260);
      });
    }

    /* ---------- quiz pop-up ---------- */
    var path = location.pathname;
    if (/^\/(quiz|masterclass)(\/|$)/.test(path)) return;
    if (/^\/course(\/|$)/.test(path) && new URLSearchParams(location.search).get('code')) return;
    if (Number(store.get('lk_quizpop_until') || 0) > Date.now()) return;
    if (store.sget('lk_quizpop_session')) return;

    var pop = document.createElement('div');
    pop.className = 'lkq'; pop.hidden = true;
    pop.setAttribute('role', 'dialog'); pop.setAttribute('aria-modal', 'true'); pop.setAttribute('aria-labelledby', 'lkq-h');
    pop.innerHTML = '<div class="box">' +
      '<button class="x" type="button" data-qclose aria-label="Close">×</button>' +
      '<p class="k">Free money mindset quiz · 5 minutes</p>' +
      '<h2 id="lkq-h">Are you under-earning without realizing it?</h2>' +
      '<p class="t">Take the Underearning Financial Scorecard. Rate 30 quick statements and see which money pattern is running your income, and what to do about it.</p>' +
      '<a class="go" href="/quiz/">Take the free quiz <span aria-hidden="true">→</span></a>' +
      '<button class="no" type="button" data-qclose>No thanks</button>' +
      '</div>';
    document.body.appendChild(pop);

    var done = false, last = null;
    function snooze() { store.set('lk_quizpop_until', String(Date.now() + 30 * DAY)); }
    function open() {
      if (done) return; done = true; cleanup();
      store.sset('lk_quizpop_session', '1');
      last = document.activeElement; pop.hidden = false;
      requestAnimationFrame(function () { pop.classList.add('on'); pop.querySelector('.go').focus({ preventScroll: true }); });
      document.addEventListener('keydown', onKey);
    }
    function close() {
      snooze();
      pop.classList.remove('on'); document.removeEventListener('keydown', onKey);
      setTimeout(function () { pop.hidden = true; if (last && last.focus) last.focus({ preventScroll: true }); }, 250);
    }
    function onKey(e) {
      if (e.key === 'Escape') return close();
      if (e.key === 'Tab') {
        var f = pop.querySelectorAll('a,button'), a = f[0], b = f[f.length - 1];
        if (e.shiftKey && document.activeElement === a) { e.preventDefault(); b.focus(); }
        else if (!e.shiftKey && document.activeElement === b) { e.preventDefault(); a.focus(); }
      }
    }
    // a real scroll, not a nudge: a quarter of the screen
    function onScroll() { if (window.scrollY > window.innerHeight * 0.25) open(); }
    function cleanup() { removeEventListener('scroll', onScroll); }
    pop.addEventListener('click', function (e) { if (e.target === pop || e.target.closest('[data-qclose]')) close(); });
    // someone heading to checkout is not interrupted
    document.addEventListener('click', function (e) {
      if (!done && e.target.closest('[data-checkout],[data-commerce],a[href*="kit.com"]')) { done = true; store.sset('lk_quizpop_session', '1'); cleanup(); }
    }, true);
    addEventListener('scroll', onScroll, { passive: true });
  });
})();
