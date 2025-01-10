from flask import Blueprint
from ..models import User
from .. import db

cart_bp = Blueprint('cart', __name__)