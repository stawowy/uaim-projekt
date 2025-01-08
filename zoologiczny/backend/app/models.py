from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()

# Enum for Order Status
class OrderStatus(Enum):
    pending = 'pending'      # Order placed but not yet processed
    shipped = 'shipped'      # Order shipped
    delivered = 'delivered'  # Order delivered
    canceled = 'canceled'    # Order canceled

# Enum for Payment Status
class PaymentStatus(Enum):
    pending = 'pending'      # Payment not yet made
    completed = 'completed'  # Payment successful
    failed = 'failed'        # Payment failed

# Enum for Payment Method
class PaymentMethod(Enum):
    credit_card = 'credit_card'    # Payment via credit card
    paypal = 'paypal'              # Payment via PayPal
    bank_transfer = 'bank_transfer'  # Payment via bank transfer

# Enum for Invoice Status
class InvoiceStatus(Enum):
    pending = 'pending'    # Invoice not yet paid
    paid = 'paid'          # Invoice paid

# Enum for User Role
class UserRole(Enum):
    admin = 'admin'
    customer = 'customer'
    employee = 'employee'


# User Model
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    role = db.Column(db.Enum(UserRole, name="user_role_enum"), default=UserRole.customer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"


# Product Model
class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Product {self.name}>"


# Animal Model
class Animal(db.Model):
    __tablename__ = 'animals'

    animal_id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Animal {self.species}>"


# Plant Model
class Plant(db.Model):
    __tablename__ = 'plants'

    plant_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Plant {self.name}>"


# Order Model
class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'))
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    shipping_address = db.Column(db.Text)
    status = db.Column(db.Enum(OrderStatus, name="order_status_enum"), default=OrderStatus.pending)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f"<Order {self.order_id}>"


# OrderItem Model
class OrderItem(db.Model):
    __tablename__ = 'order_items'

    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', ondelete='CASCADE'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.animal_id'))
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.plant_id'))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    order = db.relationship('Order', backref=db.backref('order_items', lazy=True))
    product = db.relationship('Product', backref=db.backref('order_items', lazy=True), foreign_keys=[product_id])
    animal = db.relationship('Animal', backref=db.backref('order_items', lazy=True), foreign_keys=[animal_id])
    plant = db.relationship('Plant', backref=db.backref('order_items', lazy=True), foreign_keys=[plant_id])

    def __repr__(self):
        return f"<OrderItem {self.order_item_id}>"


# Payment Model
class Payment(db.Model):
    __tablename__ = 'payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', ondelete='CASCADE'))
    payment_method = db.Column(db.Enum(PaymentMethod, name="payment_method_enum"), nullable=False)
    payment_status = db.Column(db.Enum(PaymentStatus, name="payment_status_enum"), default=PaymentStatus.pending)
    payment_amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)

    order = db.relationship('Order', backref=db.backref('payments', lazy=True))

    def __repr__(self):
        return f"<Payment {self.payment_id}>"


# Invoice Model
class Invoice(db.Model):
    __tablename__ = 'invoices'

    invoice_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', ondelete='CASCADE'))
    invoice_number = db.Column(db.String(100), unique=True, nullable=False)
    invoice_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    invoice_status = db.Column(db.Enum(InvoiceStatus, name="invoice_status_enum"), default=InvoiceStatus.pending)

    order = db.relationship('Order', backref=db.backref('invoices', lazy=True))

    def __repr__(self):
        return f"<Invoice {self.invoice_number}>"
