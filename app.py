from flask import Flask, render_template, jsonify
import json
from model.anomaly_detector import detect_anomalies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    with open('data/build_metrics.json', 'r') as f:
        builds = json.load(f)
    return jsonify(builds)

@app.route('/detect')
def detect():
    with open('data/build_metrics.json', 'r') as f:
        builds = json.load(f)
    result = detect_anomalies(builds)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
