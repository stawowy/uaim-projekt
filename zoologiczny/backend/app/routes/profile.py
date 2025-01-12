from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ..models import User
from .. import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile/<username>')
@jwt_required()
def get_user(username):
    """
    Get user profile information by username.

    Args:
        username (str): The username of the user to retrieve.

    Responses:
    200 OK:
    {
        "user_id": 1,
        "username": "username",
        "first_name": "First",
        "last_name": "Last",
        "email": "user@example.com",
        "phone": "1234567890"
    }

    404 Not Found:
    {
        "error": "User not found"
    }
    """
    user = db.session.query(User).filter_by(username=username).first()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    res = {
        "user_id": user.user_id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone": user.phone
    }

    return jsonify(res)