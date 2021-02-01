import datetime

from itsdangerous import URLSafeSerializer
from flask_ecommerce import db, auth
from flask import current_app as app, g

from flask_ecommerce.products.models import Products
from flask_ecommerce.user.models import User


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column('order_id', db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.ForeignKey('user.user_id'), nullable=False)
    #payment_id = db.Column('payment_id', db.String())
    firstname = db.Column('firstname', db.String(64))
    lastname = db.Column('lastname', db.String(64))
    email = db.Column('email', db.String(120), unique=True)
    address = db.Column('address', db.String(200))
    city = db.Column('city', db.String(200))
    country = db.Column('country', db.String(200))
    phone_no = db.Column('phone_no', db.String(10))
    pincode = db.Column('pincode', db.String(6))
    payment_mode = db.Column('payment_mode', db.String(64))
    dttm = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    orderdet = db.relationship('OrderDetails', backref='order')
    ''' prod_name = db.Column('prod_name', db.String(120), index=True, unique=True)
     prod_desc = db.Column('prod_desc', db.String(120))
     prod_price = db.Column('prod_price', db.Integer)
     total_price = db.Column('total_price', db.Integer)'''

class OrderDetails(db.Model):
    __tablename__ = 'orderdetails'
    id = db.Column('orderdet_id', db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column('order_id', db.ForeignKey('orders.order_id'), nullable=False)
    prod_id = db.Column('prod_id', db.ForeignKey('products.prod_id'), nullable=False)