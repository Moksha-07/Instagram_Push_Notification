importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js');

firebase.initializeApp({
    apiKey: "AIzaSyDamG4eiSPB0tD3NzZEyClS1eIVZqBqALI",
    authDomain: "notification-89dac.firebaseapp.com",
    projectId: "notification-89dac",
    storageBucket: "notification-89dac.appspot.com",
    messagingSenderId: "662608467431",
    appId: "1:662608467431:web:36f15c21add94406559942",
    measurementId: "G-9RRSV61R32"
});

const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload) {
    console.log('[firebase-messaging-sw.js] Received background message', payload);
    const notificationTitle = payload.notification.title || 'Background Message Title';
    const notificationOptions = {
        body: payload.notification.body || 'Background Message body',
        icon: '/default-icon.png' // optional
    };

    return self.registration.showNotification(notificationTitle, notificationOptions);
});
