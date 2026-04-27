self.addEventListener('install', (e) => {
  console.log('تثبيت التطبيق...');
});

self.addEventListener('fetch', (e) => {
  // هذا الجزء يسمح للتطبيق بالعمل حتى عند ضعف الإنترنت
  e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
});

