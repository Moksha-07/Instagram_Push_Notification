from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# ✅ Route to serve the home page (index.html)
@app.route('/')
def index():
    return render_template('index.html')  # Looks inside templates/index.html

# ✅ Route to serve the Firebase service worker
@app.route('/firebase-messaging-sw.js')
def service_worker():
    return send_from_directory('static', 'firebase-messaging-sw.js')

# Database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sql12345',
            database='notifications_db'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Endpoint to store notification
@app.route('/store-notification', methods=['POST'])
def store_notification():
    data = request.json
    title = data.get('title')
    body = data.get('body')
    notification_type = data.get('type')
    source = data.get('source', 'Instagram')

    if not title or not body:
        return jsonify({"error": "Title and body are required"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO notifications (title, body, type, source)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE received_at = CURRENT_TIMESTAMP
        """
        cursor.execute(query, (title, body, notification_type, source))
        connection.commit()
        return jsonify({"message": "Notification stored successfully"}), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
