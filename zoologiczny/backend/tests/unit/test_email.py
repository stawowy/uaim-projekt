import pytest
from flask import Flask
from utils.email import send_invoice_email
from models import Invoice

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SENDER_EMAIL_ADDRESS'] = 'email@example.com'
    app.config['SENDER_EMAIL_PASSWORD'] = 'password'
    with app.app_context():
        yield app

def test_send_email(mocker, app):
    smtp_mock = mocker.patch('smtplib.SMTP')
    smtp_instance = smtp_mock.return_value

    invoice = Invoice(order_id=1,
                      invoice_number='INV-123',
                      total_amount=100.00)

    send_invoice_email(invoice, 'email@mail.com')

    smtp_instance.starttls.assert_called_once()
    smtp_instance.login.assert_called_once_with('email@example.com', 'password')
    smtp_instance.sendmail.assert_called_once()
    smtp_instance.quit.assert_called_once()