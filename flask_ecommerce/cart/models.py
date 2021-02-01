from flask_ecommerce import db, auth
from flask import current_app as app, g
from flask_ecommerce.user.models import *


class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column('cart_id', db.Integer,primary_key=True, autoincrement=True)
    cart_uid = db.Column('cart_uid', db.Integer, nullable=False)
    cart_pid = db.Column('cart_pid', db.Integer, nullable=False)
    cart_qty = db.Column('cart_qty', db.Integer, nullable=False, default=1)