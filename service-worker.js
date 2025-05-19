const CACHE_NAME = 'guitar-directory-cache-v1';
const urlsToCache = [
    '/', // Root path
    '/index.html',
    '/content.html',
    '/videos.html',
    '/comingsoon.html',
    '/styles.css', // Add your CSS file if applicable
    '/script.js',  // Add your JS file if applicable
    '/icon-192x192.png',
    '/icon-512x512.png'
];

// Install the service worker and cache assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(urlsToCache);
        })
    );
});

// Fetch assets from the cache or network
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});

// Update the service worker and remove old caches
self.addEventListener('activate', (event) => {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (!cacheWhitelist.includes(cacheName)) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});