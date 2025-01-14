from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
import uuid
from ..models import Product, Order, OrderItem, Invoice, User
from .. import db
from app.utils.email import send_invoice_email

order_bp = Blueprint('order', __name__)

@order_bp.route('/order', methods=['POST'])
@jwt_required()
def place_order():
    """
    Place a new order.

    Request JSON:
    {
        "user_id": 1,
        "products": {
            "1": 2,
            "2": 1
        },
        "shipping_address": "Test address"
    }

    Responses:
    201 Created:
    {
        "message": "Order placed successfully"
    }

    400 Bad Request:
    {
        "error": "Missing fields"
    }

    404 Not Found:
    {
        "error": "Product not found"
    }

    409 Conflict:
    {
        "error": "Specified quantity too large"
    }
    """
    data = request.json
    user_id = data.get('user_id')
    products_dict = data.get('products')
    shipping_address = data.get('shipping_address')

    if not (user_id and products_dict):
        return jsonify({'error': 'Missing fields'}), 400

    total = 0
    order_items = []

    for pid, amount in products_dict.items():
        product = db.session.query(Product).filter_by(product_id=int(pid)).first()

        if product:
            if amount > product.stock_quantity:
                return jsonify({'error': 'Specified quantity too large'}), 409
            product.stock_quantity -= amount
            price = product.price
            order_items.append({'product_id': pid, 'quantity': amount, 'price': price})
        else:
            return jsonify({'error': 'Product not found'}), 404

        total += price * amount

    if shipping_address:
        new_order = Order(user_id=user_id, total_amount=total, shipping_address=shipping_address)
    else:
        new_order = Order(user_id=user_id, total_amount=total)
        
    new_order_items = []

    for item in order_items:
        new_order_items.append(OrderItem(order_id=new_order.order_id, product_id=item['product_id'], 
                                quantity=item['quantity'], price=item['price']))

    new_invoice = Invoice(order_id=new_order.order_id, invoice_number=uuid.uuid4(), total_amount=total)

    try:
        db.session.add(new_order)
        db.session.add_all(new_order_items)
        db.session.add(new_invoice)
        db.session.commit()
        send_invoice_email(new_invoice, db.session.query(User).filter_by(user_id=user_id).first().email)
        return jsonify({'message': 'Order placed successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error: {str(e)}'}), 500

    


