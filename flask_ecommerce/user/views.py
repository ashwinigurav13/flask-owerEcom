from flask import Blueprint, jsonify, request, g, render_template, flash, url_for
from flask_sqlalchemy import SQLAlchemy
#from app import app
from flask import render_template, request, session
from sqlalchemy import func
from flask_ecommerce.cart.models import Cart
from flask_ecommerce.products.models import Products
from flask_ecommerce.category.models import Subcategory
from itsdangerous import URLSafeSerializer
from werkzeug.utils import redirect

from flask_ecommerce import db, auth
from flask_ecommerce.user.models import User

mod = Blueprint('users', __name__)


@mod.route('/')
def home():

    '''products=Products.query.filter(Products.prod_id, Products.subcat_id, Products.prod_name,
                                  Products.prod_desc, Products.prod_price, Products.prod_qty,
                                  Products.prod_image, Products.prod_brand)
'''
    results = db.engine.execute('SELECT * FROM products')

    if 'user_id' in session:
        login = session['username']
        user_id = session['user_id']

        viewcart = db.engine.execute(f'select prod_name, prod_image, cart_qty, prod_price from products inner join cart'
                                     f' on products.prod_id = cart.cart_pid and cart.cart_uid={user_id}')

        qty = Cart.query.filter(Cart.cart_uid == user_id).count()



        return render_template('index.html', results=results, users=login , viewcart=viewcart, logout='<---', qty=qty, user_id=user_id)
    else:
        return render_template('index.html', results=results, users='login', logout='<---')



@mod.route('/registration',methods=['GET','POST'])
def registration():

    if(request.method=='POST'):
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        phone = request.form.get('phone_no')
        address = request.form.get('address')
        pincode = request.form.get('pincode')

        entry=User(username=username,email=email,password=password,phone_no=phone,address=address,pincode=pincode)
        db.session.add(entry)
        db.session.commit()
        return redirect (url_for('users.login'))
    else:
        return render_template('registration.html')


@mod.route('/login', methods=['GET', 'POST'])
def login():
     if (request.method == 'POST'):
         username = request.form.get('username')
         password = request.form.get('password')

         if 'user_id' in session:
             return redirect(url_for('users.home'))
         else:
            users = User.query.filter(User.username == username, User.password == password).first()
            if users:
                session['user_id'] = users.user_id
                session['username'] = users.username
                return redirect(url_for('users.home'))
            else:
                return redirect(url_for('users.registration'))
     else:
         return render_template('login.html')


@mod.route('/logout')
def logout():
    session.pop('user_id',None)
    flash("log out succsfully")
    results = db.engine.execute('SELECT * FROM products')
    flash("logout sucssful")
    return redirect(url_for('users.home'))



