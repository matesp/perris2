

//asignar un nombre y versión al cache
const CACHE_NAME = 'v1_cache',
  urlsToCache = [
    './',
    // 'https://use.fontawesome.com/releases/v5.3.1/css/all.css',
    // 'https://use.fontawesome.com/releases/v5.0.7/css/all.css',
    // 'https://use.fontawesome.com/releases/v5.0.6/webfonts/fa-brands-400.woff2',
    './Contactanos',
    './static/css/estilo.css',
    './static/css/galeria.css',
    './static/css/registro.css',
    './static/css/index.css',
    './static/css/lightbox.min.css',
    './static/js/app.js',
    './static/js/galeria.js',
    './static/js/lightbox.min.js',
    './static/img/logo.png'
  ]


//durante la fase de instalación, generalmente se almacena en caché los activos estáticos
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache)
          .then(() => self.skipWaiting())
      })
      .catch(err => console.log('Falló registro de cache', err))
  )
})

//una vez que se instala el SW, se activa y busca los recursos para hacer que funcione sin conexión
self.addEventListener('activate', e => {
  const cacheWhitelist = [CACHE_NAME]

  e.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            //Eliminamos lo que ya no se necesita en cache
            if (cacheWhitelist.indexOf(cacheName) === -1) {
              return caches.delete(cacheName)
            }
          })
        )
      })
      // Le indica al SW activar el cache actual
      .then(() => self.clients.claim())
  )
})

//cuando el navegador recupera una url
self.addEventListener('fetch', function(event) {
  event.respondWith(
    fetch(event.request).catch(function() {
      return caches.match(event.request);
    })
  );
});