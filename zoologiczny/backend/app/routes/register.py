from flask import Blueprint, request, jsonify
from ..models import User
from .. import db, bcrypt

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone = data.get('phone')

    if not (username and email and password and first_name and last_name and phone):
        return jsonify({'error': 'All fields are required'}), 400

    # Check if the user already exists
    if User.query.filter((User.username == username) | (User.email == email) | (User.phone == phone)).first():
        return jsonify({'error': 'User already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password_hash=hashed_password, 
                    first_name=first_name, last_name=last_name, phone=phone)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error: {str(e)}'}), 500