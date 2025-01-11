from flask import Blueprint, jsonify

test_bp = Blueprint('test', __name__)

@test_bp.route('/test')
def home():
    return jsonify({"message": "Backend is running!"})