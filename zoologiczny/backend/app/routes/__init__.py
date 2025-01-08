from .login import login_bp
from .register import register_bp
from .products import products_bp
from .profile import profile_bp
from .cart import cart_bp

def register_blueprints(app):
    app.register_blueprint(login_bp, url_prefix="/api")
    app.register_blueprint(register_bp, url_prefix="/api")
    app.register_blueprint(products_bp, url_prefix="/api")
    app.register_blueprint(profile_bp, url_prefix="/api")
    app.register_blueprint(cart_bp, url_prefix="/api")
    