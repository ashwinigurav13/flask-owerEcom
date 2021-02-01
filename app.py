from flask import Flask, render_template
import os
from flask_ecommerce import create_app, db

config_name = os.getenv('FLASK_CONFIG', 'development') # Default is 'development' if FLASK_CONFIG is not set.
app = create_app(config_name)


if __name__=='__main__':
    with app.app_context(): # Allow application context
        db.create_all()
    app.run(debug=True, port=5000)


































'''from flask import Flask, render_template
import os
from flask_ecommerce import create_app, db


app = Flask(__name__, template_folder='templates')

#config_name = os.getenv('FLASK_CONFIG', 'development') # Default is 'development' if FLASK_CONFIG is not set.
#app = create_app(config_name)


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/product")
def product():
    return render_template('product.html')


@app.route("/checkout")
def checkout():
    return render_template('checkout.html')

@app.route("/store")
def store():
    return render_template('store.html,sql')

@app.route("/blank")
def blank():
    return render_template('blank.html')


@app.route("/mobile")
def mobile():

    return render_template('mobile.html')



@app.route("/login")
def login():

    return render_template('login.html')


@app.route("/registration")
def registration():

    return render_template('registration.html')


if __name__ == "__main__":
    with app.app_context():
         db.create_all()
    app.run(debug=True, port=5050)

'''