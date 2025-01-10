from flask import Blueprint
from ..models import User
from .. import db

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register_user():
    return