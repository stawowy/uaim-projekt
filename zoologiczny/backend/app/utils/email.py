import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import current_app

def send_invoice_email(invoice, receiver_email):
    # Email configuration
    sender_email = current_app.config.get("SENDER_EMAIL_ADDRESS")
    sender_password = current_app.config.get("SENDER_EMAIL_PASSWORD")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    subject = f"Invoice {invoice.invoice_number}"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    body = f"""
    Drogi kliencie,

    Załączamy informacje o fakturze:

    Numer faktury: {invoice.invoice_number}
    Data wydania: {invoice.invoice_date}
    Całkowity koszt: {invoice.total_amount}
    Status: {invoice.invoice_status}

    Dziękujemy za korzystanie z naszych usług i życzymy miłego dnia!
    
    Sklep Zoologiczny
    """
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f"Invoice email sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send invoice email: {e}")