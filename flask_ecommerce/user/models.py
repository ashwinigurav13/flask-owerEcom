from itsdangerous import URLSafeSerializer
from flask_ecommerce import db, auth
from flask_ecommerce.cart.models import *
from flask import current_app as app, g

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column('user_id', db.Integer, primary_key=True, autoincrement=True)
    username = db.Column('username', db.String(64), index=True, unique=True)
    email = db.Column('email', db.String(120), unique=True)
    password = db.Column('password', db.String(128))
    address = db.Column('address', db.String(200))
    phone_no = db.Column('phone_no', db.String(10))
    pincode = db.Column('pincode', db.String(16))

    #prod_carts = db.relationship('Cart', backref='user', uselist=False, lazy='select', cascade="all,delete")
    orders = db.relationship('Order', backref='user', uselist=True, lazy='joined', cascade="all,delete")

