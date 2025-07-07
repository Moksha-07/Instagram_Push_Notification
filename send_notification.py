import random
import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\smoks\Downloads\service credentials.json")
firebase_admin.initialize_app(cred)

# Function to return a random Instagram-style notification
def get_random_instagram_notification():
    notifications = [
        "user1 liked your photo",
        "user2 sent you a friend request",
        "user3 started a live video",
        "user4 commented on your post",
        "user5 tagged you in a photo",
        "user6 shared your post",
        "user7 followed you",
        "user8 sent you a message",
    ]
    return random.choice(notifications)

# Function to send a notification using FCM
def send_notification(token, title, body):
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=token,
        )

        response = messaging.send(message)
        print("Successfully sent message:", response)
        return response

    except Exception as e:
        print("Error sending message:", e)
        return None

# Main execution
if __name__ == "__main__":
    fcm_token = "f21BsxKgwCe7nKv4k1fjGL:APA91bGDLMQL8Rh42SBlz2mw5K-PKxz4BHreckMzJb-FwjmP5CP0g-pqxJ1Zf8bTglulDTSZxz4i2god_VSSbAe3AdG_Z7lJF4Vmby2FGnaTmzWSTc65l8U"
    notification_body = get_random_instagram_notification()
    notification_title = "Instagram Notification"
    send_notification(fcm_token, notification_title, notification_body)
