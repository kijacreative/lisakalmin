# Lisa Kalmin — Threshold

Static one-page site for lisakalmin.com. No build step: `index.html` plus `img/`.
The hero is a WebGL hall (three.js 0.170 loaded from jsDelivr); without WebGL it falls back to a plain gradient.

Preview locally:

```bash
python3 -m http.server 4173
```

Deploys on Vercel as a static site (see `vercel.json`).
