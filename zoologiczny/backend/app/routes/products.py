from flask import Blueprint, jsonify
from json import dumps
from ..models import Product
from .. import db
from decimal import Decimal

products_bp = Blueprint('products', __name__)

def decimal_serializer(obj):
    """
    Utility to serialize Decimal objects to strings.

    Args:
        obj (Decimal): The Decimal object to serialize.

    Returns:
        str: The serialized Decimal object as a string.

    Raises:
        TypeError: If the object is not of type Decimal.
    """
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError('type not serializable&quot;')



@products_bp.route('/products')
def get_products():
    """
    Get a list of all products.

    Responses:
    200 OK:
    [
        {
            "product_id": 1,
            "name": "Product Name",
            "description": "Product Description",
            "price": "10.00",
            "stock_quantity": 100,
            "category": "Category",
            "subcategory": "Subcategory",
            "rating": "4.5",
            "image_path": "path/to/image.jpg"
        },
        ...
    ]

    404 Not Found:
    {
        "error": "No products found"
    }
    """
    products = db.session.query(Product).all()

    if not products:
        return jsonify({'error': "No products found"}), 404

    res = []

    for product in products:
        prod_dict = {
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

        res.append(prod_dict)

    return dumps(res, default=decimal_serializer)


@products_bp.route('/products/<product_id>')
def get_product_by_id(product_id):
    """
    Get specific product data by ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Responses:
    200 OK:
    {
        "product_id": 1,
        "name": "Product Name",
        "description": "Product Description",
        "price": "10.00",
        "stock_quantity": 100,
        "category": "Category",
        "subcategory": "Subcategory",
        "rating": "4.5",
        "image_path": "path/to/image.jpg"
    }

    404 Not Found:
    {
        "error": "Product not found"
    }
    """
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

    return dumps(res, default=decimal_serializer)