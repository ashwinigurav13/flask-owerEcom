from itsdangerous import URLSafeSerializer
from flask_ecommerce import db, auth
from flask import current_app as app, g


class Payment(db.Model):
    __tablename__ = 'payment'
    payment_id = db.Column('payment_id', db.Integer, primary_key=True, autoincrement=True)
    payment_mode = db.Column('payment_mode', db.String(64), unique=True)
    prod_id = db.Column('prod_id', db.ForeignKey('products.prod_id'), nullable=False)
    #orders = db.relationship('Order', backref=db.backref('payment'), uselist=False, lazy='select', cascade="all,delete")