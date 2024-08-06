from flask import Flask, request, jsonify

app = Flask(__name__)

driver_locations = {}

@app.route('/update-location', methods=['POST'])
def update_location():
    data = request.get_json()
    driver_id = data.get('driver_id', 'default_driver')  # Используйте уникальный идентификатор водителя
    driver_locations[driver_id] = {
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }
    return jsonify({'status': 'success'}), 200

@app.route('/get-locations', methods=['GET'])
def get_locations():
    return jsonify(driver_locations), 200

# Start Flask app in a separate thread
def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# Start bot polling and Flask app
if __name__ == "__main__":
    Thread(target=run_flask).start()
