from flask import Blueprint
from ..models import User
from .. import db

profile_bp = Blueprint('profile', __name__)