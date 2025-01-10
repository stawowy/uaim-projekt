from flask import Blueprint, jsonify, request
from ..models import User
from .. import db

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    return "dupa"