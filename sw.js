self.addEventListener('install', (event) => {
    self.skipWaiting();
});

self.addEventListener('push', (event) => {
    const data = event.data ? event.data.json() : { title: '提醒', body: '該做事情囉！' };
    event.waitUntil(
        self.registration.showNotification(data.title, {
            body: data.body,
            icon: 'https://cdn-icons-png.flaticon.com/512/1827/1827265.png',
            badge: 'https://cdn-icons-png.flaticon.com/512/1827/1827265.png'
        })
    );
});

// 監聽通知點擊
self.addEventListener('notificationclick', (event) => {
    event.notification.close();
    event.waitUntil(
        clients.openWindow('/') 
    );
});