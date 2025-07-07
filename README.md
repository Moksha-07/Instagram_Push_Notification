# 📲 Instagram Push Notification System (Using Firebase)

*This is a simple web-based push notification system using Firebase Cloud Messaging (FCM). It sends push notifications from a Python backend to the user’s browser, like Instagram-style alerts.*

## 📁 Project Structure

*instagram-push-notification/*

│
├──*static/*

   └── *firebase-messaging-sw.js*   # Firebase Service Worker (background listener)

├──*Templates/*

  ├── index.html   # Main page with permission request
   
  └── default-icon.png           # Notification icon shown in browser

├── *send_notification.py*          # Script to trigger/send a notification

├── *app.py*                        # Flask app that serves the frontend

## ⚙️ How It Works
*On the User Side (Frontend):*

*The browser loads index.html.*

*It asks the user for notification permission.*

*If allowed, it gets a device token from Firebase.*

*That token is sent to your backend or stored for later.*

*On the Admin Side (Backend):*
*You run send_notification.py.*

*It uses Firebase credentials to send a message to the user’s browser.*

*The user receives a browser notification (like Instagram).*

## 🛠️ Setup Instructions
## 🔑 1. Firebase Setup

*Create a Firebase project at https://console.firebase.google.com*

*Go to Cloud Messaging, and copy your sender ID and server key.*

*Create a file named firebase-messaging-sw.js in /static.*

## 📝 2. Configure index.html

*Add your Firebase config in this format:*

*const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"*
};

## ▶️ Running the App

## 1. Install dependencies

pip install flask requests

## 2. Run the web server

python app.py
Visit: http://localhost:5000

## 3. Send Notification (from backend)

python send_notification.py


## 🔔 Features
*Simple push notification using Firebase*

*Notification icon (default-icon.png)*

*Flask-based web app*

*User token registration*

*Works on modern browsers (Chrome, Firefox)*

## 📦 Requirements
*Python 3.7+*

*Flask*

*Firebase Cloud Messaging*

*Internet connection*

✅ Example Notification
*Title: New Message*

*Body: User 1 liked your post*
