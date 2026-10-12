// Owee Pad: funciona sin conexión cuando se aloja en un sitio propio (https).
const CACHE = "owee-pad-3.3";
const FILES = ["./", "./index.html", "./owee.js", "./owee.css", "./owee-glyph-map.json", "./manifest.webmanifest", "./icon.svg",
  "./fonts/OweeSans-Regular.woff2", "./fonts/OweeSchool-Regular.woff2"];
self.addEventListener("install", e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES))));
self.addEventListener("activate", e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))));
self.addEventListener("fetch", e => e.respondWith(caches.match(e.request).then(r => r || fetch(e.request))));
