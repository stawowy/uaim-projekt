from flask import Blueprint
from ..models import Product
from .. import db

products_bp = Blueprint('products', __name__)