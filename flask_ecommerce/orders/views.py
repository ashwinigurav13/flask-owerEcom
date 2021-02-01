from io import BytesIO

from flask import Blueprint, jsonify, request, g, flash, url_for, Response, make_response
from flask import current_app as app
from flask import session
from werkzeug.utils import redirect
from reportlab.pdfgen import canvas
from flask_ecommerce import db
from flask_ecommerce.cart.models import Cart
from flask_ecommerce.orders.models import Order

mod = Blueprint('orders', __name__)

@mod.route('/placeorder', methods=['GET', 'POST'])
def placeorder():
    if request.method == 'POST':
        if 'user_id' in session:
            user_id = session['user_id']

            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            email = request.form.get('email')
            address = request.form.get('address')
            city = request.form.get('city')
            country = request.form.get('country')
            pincode = request.form.get('pincode')
            phone = request.form.get('tel')
            payments = request.form.get('payment')

            data = Order(user_id=user_id, firstname=firstname, lastname=lastname, email=email, address=address, city=city,
                          country=country, phone_no=phone, pincode=pincode, payment_mode=payments)

            db.session.add(data)
            db.session.commit()

            orders = Order.query.filter().order_by(Order.order_id.desc()).first()
            order_id = orders.order_id
            session['order_id'] = order_id

            cartdetails = Cart.query.filter(Cart.cart_uid == user_id).all()

            for row in cartdetails:
                db.engine.execute(f'insert into orderdetails (order_id, prod_id) values({order_id}, {row.cart_pid})')
                db.engine.execute(f'delete from cart where cart_id = {row.cart_id} ')

            db.session.commit()
            flash('Your order place successfully')
            #return 'Your order place successfully'
            return redirect(url_for('orders.reportpdf'))
        else:
            return redirect(url_for('users.login'))
    else:
        return redirect(url_for('users.home'))


@mod.route('/reportpdf')
def reportpdf():
    #response = Response(content_type='application/pdf')
    #response.headers['Content-Type'] = 'application/pdf'
    #response.headers['Content-Disposition'] = 'attachment;filename=invoice.pdf'

    #response = make_response(pdf)
    request.headers['Content-Type'] = 'application/pdf'
    request.headers['Content-Disposition'] = 'attachment; filename="order_invoice.pdf"'

    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    data = Order.query.filter(Order.order_id == session['order_id']).first()
    name = str(data.firstname)+"  "+str(data.lastname)
    #c = canvas.Canvas('first_invoice.pdf')
    c.setFont("Courier", 20)
    c.drawCentredString(200, 750, 'Order Invoice')
    c.setFont("Courier", 14)
    c.drawString(90, 700, 'Customer Name : ')
    c.drawString(250, 700, name)
    c.save()
    return "Your Order place successfully... thanks for shopping with us.."



''' c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Order Invoice')
    c.setFont("Courier", 14)

    c.drawString(10, 650, 'First Name:')

    c.drawString(10, 600, 'Last Name:')

    c.drawString(10, 550, 'Address:')

    c.drawString(10, 500, 'City:')

    c.drawString(250, 500, 'State:')

    c.drawString(10, 450, 'Zip Code:')
'''


''' response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment;filename=invoice.pdf'''
    #return response

'''@mod.route('/reportpdf')
def reportpdf():
    try:

        data = db.engine.execute("SELECT emp_id, emp_first_name, emp_last_name, emp_designation FROM employee")
        result = data.fetchall()

        pdf = FPDF()
        pdf.add_page()

        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, 'Employee Data', align='C')
        pdf.ln(10)

        pdf.set_font('Courier', '', 12)

        col_width = page_width / 4

        pdf.ln(1)

        th = pdf.font_size

        for row in result:
            pdf.cell(col_width, th, str(row['order_id']), border=1)
            pdf.cell(col_width, th, row['order_date'], border=1)
            pdf.cell(col_width, th, row['emp_last_name'], border=1)
            pdf.cell(col_width, th, row['emp_designation'], border=1)
            pdf.ln(th)

        pdf.ln(10)

        pdf.set_font('Times', '', 10.0)
        pdf.cell(page_width, 0.0, '- end of report -', align='C')

        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf',
                        headers={'Content-Disposition': 'attachment;filename=employee_report.pdf'})
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()'''