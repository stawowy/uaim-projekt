from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ..models import User
from .. import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile/<user_id>')
@jwt_required()
def get_user(user_id):
    user = db.session.query(User).filter_by(user_id=user_id).first()

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