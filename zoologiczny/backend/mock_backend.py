# mock_backend.py
from flask import Flask, jsonify
import random

app = Flask(__name__)

# Simple route to check if backend is working
@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})

# Random route to return some random data
@app.route('/random')
def random_data():
    return jsonify({"random_number": random.randint(1, 100)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
