from flask_ecommerce import db, auth
from flask import current_app as app, g


class Products(db.Model):
    __tablename__ = 'products'
    prod_id = db.Column('prod_id', db.Integer, primary_key=True, autoincrement=True)
    subcat_id = db.Column('subcat_id', db.ForeignKey('subcategory.subcat_id'), nullable=True)
    prod_name = db.Column('prod_name', db.String(120), index=True, unique=True)
    prod_desc = db.Column('prod_desc', db.String(120))
    prod_price = db.Column('prod_price', db.Integer)
    prod_qty = db.Column('prod_qty', db.Integer)
    prod_image = db.Column('prod_image', db.String(120))
    prod_brand = db.Column('prod_brand', db.String(80))
    #prod_carts = db.relationship('Cart', backref=db.backref('products'), uselist=False, lazy='select', cascade="all,delete")
    #orders = db.relationship('Order', backref='products', uselist=False, cascade="all,delete")
    payments = db.relationship('Payment', backref='products', uselist=False, lazy='select', cascade="all,delete")
    orderdet = db.relationship('OrderDetails', backref='products')

