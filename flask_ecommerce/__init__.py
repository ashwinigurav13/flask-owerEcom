from flask import Flask, g, render_template
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_httpauth import HTTPTokenAuth

# db variable initialization
db = SQLAlchemy()
# Token based auth
auth = HTTPTokenAuth('Bearer')

def create_app(config_name):
    app = Flask(__name__,template_folder='templates')
    app.config.from_object(app_config[config_name])
    db.init_app(app)


    # Import a module / component using its blueprint handler variable
    from flask_ecommerce.category.views import mod as category_module
    from flask_ecommerce.user.views import mod as users_module
    from flask_ecommerce.orders.views import mod as order_module
    from flask_ecommerce.products.views import mod as product_module
    from flask_ecommerce.payment.views import mod as payment_module
    from flask_ecommerce.vendor.views import mod as vendor_module
    from flask_ecommerce.cart.views import mod as cart_module
    # Register blueprint(s)
    # app.register_blueprint(json_users_module)
    app.register_blueprint(category_module)
    app.register_blueprint(users_module)
    app.register_blueprint(order_module)
    app.register_blueprint(product_module)
    app.register_blueprint(payment_module)
    app.register_blueprint(vendor_module)
    app.register_blueprint(cart_module)


    return app

