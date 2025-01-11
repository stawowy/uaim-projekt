from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text
import random
import os
from app.models import db, User, Product, Animal, Plant, Order, OrderItem, Payment, Invoice

app = Flask(__name__)

# Replace with your actual database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Simple route to check if backend is working
@app.route('/test')
def home():
    return jsonify({"message": "Backend is running!"})

# Random route to return some random data
@app.route('/random')
def random_data():
    return jsonify({"random_number": random.randint(1, 100)})

    
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{ 'name': product.name, 'price': product.price } for product in products])

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'order_id': order.order_id,
        'total_amount': order.total_amount,
        'status': order.status.name
    } for order in orders])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)