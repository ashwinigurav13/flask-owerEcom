from flask import Blueprint, jsonify, request, g, render_template, url_for,redirect
from flask import session
from flask_ecommerce import db
from flask_ecommerce.products.models import Products
import os
from werkzeug import secure_filename
from flask_ecommerce.cart.models import Cart
mod = Blueprint('products', __name__)
path='D:\\pythonpractice\\flask_ecommerce_api\\flask_ecommerce\\static\\img'



@mod.route('/addproduct', methods=['GET','POST'])
def add_product():

    if(request.method=='POST'):
        subcat_id=request.form.get('subcat_id')
        prod_name=request.form.get('prod_name')
        prod_desc = request.form.get('prod_desc')
        prod_price=request.form.get('prod_price')
        prod_qty=request.form.get('prod_qty')
        prod_brand = request.form.get('prod_brand')
        prod_image =  request.files['file']
        img = prod_image.filename.split('/')[-1]

        prod_image.save(os.path.join(path,secure_filename(prod_image.filename)))

        entry = Products(subcat_id=subcat_id,prod_name=prod_name,
                         prod_desc=prod_desc, prod_price=prod_price,
                         prod_qty=prod_qty, prod_brand=prod_brand,prod_image=img)
        db.session.add(entry)
        db.session.commit()
        return 'product added sucssfuly'
    else:
        subcategory = db.engine.execute('select * from subcategory')
        return render_template('addproducts.html', subcategory=subcategory)

@mod.route('/product:?<prod_id>',methods=['GET'])
def product(prod_id):
    if 'user_id' in session:
        login = session['username']
        user_id = session['user_id']

        viewcart = db.engine.execute(f'select prod_name, prod_image, cart_qty, prod_price from products inner join cart'
                                     f' on products.prod_id = cart.cart_pid and cart.cart_uid={user_id}')
        products = Products.query.filter(Products.prod_id == prod_id).first()
        qty = Cart.query.filter(Cart.cart_uid == user_id).count()

        return render_template('product.html',productinfo=products, users=login ,logout='<---',viewcart=viewcart,user_id=user_id,qty=qty)
    else:
        products = Products.query.filter(Products.prod_id == prod_id).first()
        return render_template('product.html', productinfo=products, users='login', logout='<---')
