from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from datetime import timedelta
from ..models import User
from .. import db, bcrypt

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user and return access and refresh tokens.

    Request JSON:
    {
        "email": "user@example.com",
        "password": "password"
    }

    Responses:
    200 OK:
    {
        "message": "Login successful",
        "username": "username",
        "access_token": "access_token",
        "refresh_token": "refresh_token"
    }

    400 Bad Request:
    {
        "error": "Email and password are required"
    }

    401 Unauthorized:
    {
        "error": "Invalid email or password"
    }
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not (email and password):
        return jsonify({'error': 'Email and password are required'}), 400

    user = db.session.query(User).filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(minutes=current_app.config['ACCESS_TOKEN_EXPIRATION_MINUTES']))
    refresh_token = create_refresh_token(identity=str(user.user_id))
    return jsonify({'message': 'Login successful', 'username': user.username, 'access_token': access_token, 'refresh_token': refresh_token}), 200


@login_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """
    Refresh the access token using the refresh token.

    Request Headers:
    {
        "Authorization": "Bearer <refresh_token>"
    }

    Responses:
    200 OK:
    {
        "access_token": "new_access_token"
    }

    401 Unauthorized:
    {
        "msg": "Missing Authorization Header"
    }
    """
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=str(user_id), expires_delta=timedelta(minutes=current_app.config['ACCESS_TOKEN_EXPIRATION_MINUTES']))
    return jsonify({"access_token": access_token})