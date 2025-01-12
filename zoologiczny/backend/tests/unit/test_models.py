import datetime
from models import User, Product, Order, OrderItem, Invoice

def test_user_model():
    user = User(username='test_user',
                password_hash='password',
                email='email@mail.com',
                first_name='Test',
                last_name='User',
                phone='123456789')
    assert user.username == 'test_user'
    assert user.password_hash == 'password'
    assert user.email == 'email@mail.com'
    assert user.first_name == 'Test'
    assert user.last_name == 'User'
    assert user.phone == '123456789'

def test_product_model():
    product = Product(name='Test Product',
                      description='This is a test product',
                      price=100.00,
                      stock_quantity=10,
                      category='Inne',
                      subcategory='Karma',
                      rating=4.5,
                      image_path='test_image.jpg')
    assert product.name == 'Test Product'
    assert product.description == 'This is a test product'
    assert product.price == 100.00
    assert product.stock_quantity == 10
    assert product.category == 'Inne'
    assert product.subcategory == 'Karma'
    assert product.rating == 4.5
    assert product.image_path == 'test_image.jpg'

def test_order_model():
    order = Order(user_id=1,
                   total_amount=100.00,
                   shipping_address='Test Address',
                   status='pending')
    assert order.user_id == 1
    assert order.total_amount == 100.00
    assert order.shipping_address == 'Test Address'
    assert order.status == 'pending'

def test_order_item_model():
    order_item = OrderItem(order_id=1,
                           product_id=1,
                           quantity=2,
                           price=100.00)
    assert order_item.order_id == 1
    assert order_item.product_id == 1
    assert order_item.quantity == 2
    assert order_item.price == 100.00

def test_invoice_model():
    now = datetime.datetime.now()
    invoice = Invoice(order_id=1,
                      invoice_number='INV-123',
                      invoice_date=now,
                      total_amount=100.00,
                      invoice_status='paid')
    assert invoice.order_id == 1
    assert invoice.total_amount == 100.00
    assert invoice.invoice_number == 'INV-123'
    assert invoice.invoice_date == now
    assert invoice.invoice_status == 'paid'