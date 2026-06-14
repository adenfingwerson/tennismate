const CACHE_NAME = 't-mate-v1';
const ASSETS = [
    '/',
    '/index.html',
    '/manifest.json',
    '/assets/aden.jpg',
    '/assets/icon-192.png',
    '/assets/icon-512.png'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(ASSETS);
        })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            // Return cached response if found, else fetch from network
            return response || fetch(event.request);
        })
    );
});
