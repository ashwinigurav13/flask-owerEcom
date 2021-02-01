from flask_ecommerce import db
from flask import current_app as app, g


class Category(db.Model):
    __tablename__ = 'category'
    cat_id = db.Column('cat_id', db.Integer, primary_key=True, autoincrement=True)
    cat_name = db.Column('cat_name', db.String(64), index=True, unique=True)
    Subcategorys = db.relationship('Subcategory', backref=db.backref('category'), uselist=False, lazy='select', cascade="all,delete")

class Subcategory(db.Model):
    __tablename__ = 'subcategory'
    subcat_id = db.Column('subcat_id', db.Integer, primary_key=True, autoincrement = True)
    cat_id = db.Column('cat_id', db.ForeignKey('category.cat_id'), nullable=False)
    subcat_name = db.Column('subcat_name', db.String(120), unique=True)
    product = db.relationship('Products', backref=db.backref('subcategory'), uselist=False, lazy='select', cascade="all,delete")


