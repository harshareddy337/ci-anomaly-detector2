from flask import Flask, render_template, jsonify
import json
from model.anomaly_detector import detect_anomalies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    import random

    builds = []
    start_id = random.randint(100, 200)  # Random starting build ID
    for i in range(start_id, start_id + 5):
        build = {
            "build_id": i,
            "duration": random.randint(40, 130),
            "status": random.choice(["SUCCESS", "FAILURE"])
        }
        builds.append(build)
    return jsonify(builds)

@app.route('/detect')
def detect():
    print("🔍 /detect endpoint triggered — running anomaly detection only.")
    try:
        with open('data/build_metrics.json', 'r') as f:
            builds = json.load(f)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    result = detect_anomalies(builds)
    return jsonify({
        "builds": builds,
        "anomalies": result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
