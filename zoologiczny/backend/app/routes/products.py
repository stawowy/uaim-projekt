from flask import Blueprint, jsonify
from json import dumps
from ..models import Product
from .. import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def get_products():
    products = db.session.query(Product).all()

    if not products:
        return jsonify({'error': "No products found"}), 404

    res = []

    for product in products:
        prod_dict = {
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "category": product.category.value,
            "rating": product.rating,
            "image_path": product.image_path
        }

        res.append(prod_dict)

    return dumps(res)



@products_bp.route('/products/<product_id>')
def get_product_by_id(product_id):
    product = db.session.query(Product).filter_by(product_id=product_id).first()

    if not product:
        return jsonify({'error': 'Product not found'}), 404

    res = {
        "product_id": product.product_id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock_quantity": product.stock_quantity,
        "category": product.category.value,
        "subcategory": product.subcategory,
        "rating": product.rating,
        "image_path": product.image_path
    }

    return jsonify(res)