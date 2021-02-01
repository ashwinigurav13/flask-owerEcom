from flask import Blueprint, jsonify, request, g, render_template, redirect, flash, url_for
from flask import current_app as app
from flask import session
from itsdangerous import URLSafeSerializer
from flask_ecommerce import db, auth
from flask_ecommerce.cart.models import Cart
from flask_ecommerce.orders.models import Order

mod = Blueprint('cart', __name__)



@mod.route('/addcart/<prod_id>', methods=['GET'])
def addcart(prod_id):
    #  if request.method=='POST':
        if 'user_id' in session:
            user_id=session['user_id']

            pid = Cart.query.filter(Cart.cart_pid == prod_id, Cart.cart_uid == user_id).first()
            if pid:
                qty = pid.cart_qty+1
                db.engine.execute(f'update cart set cart_qty = {qty} where cart_uid = {user_id}')
                db.session.commit()
                return redirect(url_for('users.home'))
            else:
                db.engine.execute(f'insert into cart(cart_uid,cart_pid) values({user_id},{prod_id})')
                db.session.commit()
                flash('added to cart')
                return 'added to cart'
        else:
            return redirect(url_for('users.login'))

   # else:
   #     return redirect(url_for('users.login'))


@mod.route('/removecart/<cart_id>',methods=['GET'])
def removecart(cart_id):

    db.engine.execute(f'delete from cart where cart_id={cart_id}')

    return redirect(url_for('users.home'))



@mod.route('/checkout?<user_id>', methods=['GET'])
def checkout(user_id):
  if 'user_id' in session:
       user_id=session['user_id']
       login=session['username']
       carts = db.engine.execute(f'select prod_name, prod_image, cart_qty, prod_price from products inner join cart'
                                    f' on products.prod_id = cart.cart_pid and cart.cart_uid={user_id}')

       qty = Cart.query.filter(Cart.cart_uid == user_id).count()
       return render_template('checkout.html', carts=carts, user_id=user_id, users=login, logout='<---', qty=qty)
  else:
      return redirect(url_for('users.login'))



'''@mod.route('/order/<user_id>', methods=['GET'])
def order(user_id):
    if 'user_id' in session:
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        address = request.form.get('address')
        tel = request.form.get('tel')
        pincode = request.form.get('zipcode')

        entry = Order(firstname=firstname, lastname=lastname, email=email, address=address, phone_no=tel, pincode=pincode)
        db.session.add(entry)
        db.session.commit()'''