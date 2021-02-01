from flask import Blueprint, jsonify, request, g
from flask import current_app as app
from flask import session
from itsdangerous import URLSafeSerializer
from flask_ecommerce import db, auth
from flask_ecommerce.category.models import Category

mod = Blueprint('category', __name__, url_prefix='/category')