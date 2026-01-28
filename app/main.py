from flask import Flask, jsonify
import requests
import json
import os

app = Flask(__name__)

LOCAL_DATA_FILE = "data/solar_data.json"
CENTRAL_SERVER = os.getenv("CENTRAL_API", "http://central-server/api/upload")

@app.route("/")
def home():
    return jsonify({"status": "Solar Sync Service Running"})

@app.route("/sync")
def sync_data():
    try:
        with open(LOCAL_DATA_FILE) as f:
            data = json.load(f)

        response = requests.post(CENTRAL_SERVER, json=data, timeout=10)

        return jsonify({
            "message": "Sync Successful",
            "server_response": response.status_code
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
