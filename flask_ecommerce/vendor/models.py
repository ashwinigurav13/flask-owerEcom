from itsdangerous import URLSafeSerializer
from flask_ecommerce import db, auth
from flask import current_app as app, g

class Vendor(db.Model):
    __tablename__ = 'vendor'
    vendor_id = db.Column('vendor_id', db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column('firstname', db.String(64))
    lastname = db.Column('lastname', db.String(64))
    email = db.Column('email', db.String(120), unique=True)
    password = db.Column('password', db.String(128))
    address = db.Column('address', db.String(200))
    phone_no = db.Column('phone_no', db.String(10))
    pincode = db.Column('pincode', db.String(6))