
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/telemetry')
def telemetry():
    return jsonify({
        'latitude': 12.970600,
        'longitude': 77.648100,
        'altitude': 3.0,
        'battery': 95,
        'mode': 'AUTO'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
