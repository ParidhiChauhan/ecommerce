from flask import Flask, render_template, redirect, url_for, request, flash,session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models.product import Product

from models.user import User
# Initialize Flask application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:root@localhost/ecommerce_db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            # Login successful, redirect to dashboard or profile
            flash('Login successful!', 'success')
            return redirect(url_for(product_list))
        else:
            # Login failed, show error message
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password)
        
        new_user = User(username=username, password=hashed_password,is_admin=False)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')


    
@app.route('/product_list', methods=['GET', 'POST'])
def product_list():
    if request.method == 'POST':
        # Assuming you have a form to add products to cart
        product_id = request.form.get('product_id')
        product = Product.query.get(product_id)

        if 'cart' not in session:
            session['cart'] = []

        session['cart'].append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1  # Default quantity
        })

        flash('Product added to cart successfully!', 'success')

    products = Product.query.all()
    return render_template('product_list.html', products=products)

@app.route('/cart')
def cart():
    if 'cart' not in session or len(session['cart']) == 0:
        flash('Your cart is empty.', 'info')
        return redirect(url_for('product_list'))

    total_price = sum(item['price'] * item['quantity'] for item in session['cart'])
    return render_template('cart.html', cart=session['cart'], total_price=total_price)

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    if 'cart' in session:
        for item in session['cart']:
            if item['id'] == product_id:
                session['cart'].remove(item)
                flash('Product removed from cart.', 'warning')
                break

    return redirect(url_for('cart'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
