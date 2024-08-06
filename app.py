import re
import os
import logging

from flask import Flask, render_template, request, jsonify
from threading import Thread

app = Flask(__name__)

driver_locations = {}
tracking_status = False  # Глобальная переменная для хранения статуса отслеживания

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dispatcher')
def dispatcher():
    return render_template('dispatcher.html')

@app.route('/start-tracking', methods=['POST'])
def start_tracking():
    global tracking_status
    tracking_status = True
    return jsonify({'status': 'success'})

@app.route('/stop-tracking', methods=['POST'])
def stop_tracking():
    global tracking_status
    tracking_status = False
    return jsonify({'status': 'success'})

@app.route('/update-location', methods=['POST'])
def update_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(f'Received location: Latitude: {latitude}, Longitude: {longitude}')
    
    # Логика для обработки данных местоположения и определения успешности
    # В данном примере предполагается, что если данные получены, отслеживание активное
    return jsonify({'status': 'success'}) if tracking_status else jsonify({'status': 'error'})

@app.route('/get-locations', methods=['GET'])
def get_locations():
    return jsonify(driver_locations), 200

# Start Flask app in a separate thread
def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# Start bot polling and Flask app
if __name__ == "__main__":
    Thread(target=run_flask).start()
