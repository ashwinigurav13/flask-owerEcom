from flask import Blueprint, jsonify, request, g, render_template, url_for
from flask import current_app as app
from flask import session
from itsdangerous import URLSafeSerializer
from werkzeug.utils import redirect

from flask_ecommerce import db, auth
from flask_ecommerce.vendor.models import Vendor

mod = Blueprint('vendor', __name__)


@mod.route('/venregistration', methods=['GET', 'POST'])
def venregistration():

    if(request.method=='POST'):
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone_no')
        address = request.form.get('address')
        pincode = request.form.get('pincode')


        entry=Vendor(firstname=firstname,lastname=lastname,email=email,password=password,phone_no=phone,address=address,pincode=pincode)
        db.session.add(entry)
        db.session.commit()
        return render_template('vendorlogin.html')
    else:
        return render_template('venregistration.html')



@mod.route('/vendorlogin', methods=['GET', 'POST'])
def venlogin():
    if (request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('password')

        if 'user_id' in session:
            return redirect(url_for('users.home'))
        else:
            vendor = Vendor.query.filter(Vendor.email == email, Vendor.password == password).first()
            if vendor:
                session['user_id'] = vendor.email
                #session['username'] = vendor.username
                return redirect(url_for('products.add_product'))
            else:
                return redirect(url_for('vendor.venlogin'))
    else:
        return render_template('vendorlogin.html')