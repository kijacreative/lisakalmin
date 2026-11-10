/* ===== Masterclass settings: shared by the landing page and the thank-you page =====
   Fill these in for each class. While a value is empty (or still a [PLACEHOLDER]),
   the pages show the placeholder copy and work in preview mode. */
window.EVENT = {
  title: 'Opening the Flow of Money: Letting Go of Your Stops',
  // start and end in Pacific time with the UTC offset: -08:00 from early November, -07:00 from mid March
  start: '',                       // e.g. '2026-12-02T17:30:00-08:00'
  end: '',                         // e.g. '2026-12-02T19:00:00-08:00'
  registerUrl: '[REGISTER LINK]',  // the Kit form's subscription URL, e.g. https://app.kit.com/forms/1234567/subscriptions
  zoomUrl: '[ZOOM LINK]',          // goes into the calendar invites
  thankYouUrl: 'thank-you/',       // where preview-mode registrations land (Kit redirects here once connected)
  // one small Kit form per answer on the thank-you page, each set to add its own tag
  tagForms: {
    'never-enough': '',
    'undercharge': '',
    'avoid-looking': '',
    'in-and-out': ''
  }
};

(function () {
  var E = window.EVENT;
  var ready = function (v) { return !!v && v.indexOf('[') === -1; };
  E.isSet = function (k) { return ready(E[k]); };
  var PT = 'America/Los_Angeles';
  var fmt = function (d, o) { return new Intl.DateTimeFormat('en-US', Object.assign({ timeZone: PT }, o)).format(d); };
  var time = function (d) { return fmt(d, { hour: 'numeric', minute: '2-digit' }).replace(' AM', ' am').replace(' PM', ' pm'); };

  // the date line: placeholders stay in the copy until a real start and end are set
  E.when = function () {
    if (!E.isSet('start') || !E.isSet('end')) return null;
    var s = new Date(E.start), e = new Date(E.end);
    return {
      date: fmt(s, { weekday: 'long', month: 'long', day: 'numeric' }),
      start: time(s).replace(/ (am|pm)$/, ''),
      end: time(e),
      short: fmt(s, { month: 'short', day: 'numeric' })
    };
  };
  E.fill = function (root) {
    var w = E.when(); if (!w) return;
    (root || document).querySelectorAll('[data-date]').forEach(function (el) { el.textContent = w.date; });
    (root || document).querySelectorAll('[data-start]').forEach(function (el) { el.textContent = w.start; });
    (root || document).querySelectorAll('[data-end]').forEach(function (el) { el.textContent = w.end; });
    (root || document).querySelectorAll('[data-short]').forEach(function (el) { el.textContent = w.short; });
  };

  // countdown: dashes until there is a date, gone once class has started
  E.countdown = function (box) {
    if (!box) return;
    var cells = { d: box.querySelector('[data-c="d"]'), h: box.querySelector('[data-c="h"]'), m: box.querySelector('[data-c="m"]'), s: box.querySelector('[data-c="s"]') };
    if (!E.isSet('start')) return;
    var t0 = new Date(E.start), pad = function (n) { return (n < 10 ? '0' : '') + n; }, timer;
    function tick() {
      var t = (t0 - new Date()) / 1000;
      if (t <= 0) { box.hidden = true; clearInterval(timer); return; }
      cells.d.textContent = pad(Math.floor(t / 86400)); cells.h.textContent = pad(Math.floor(t % 86400 / 3600));
      cells.m.textContent = pad(Math.floor(t % 3600 / 60)); cells.s.textContent = pad(Math.floor(t % 60));
    }
    tick(); timer = setInterval(tick, 1000);
  };
})();
