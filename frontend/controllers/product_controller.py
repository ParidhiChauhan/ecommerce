from flask import Blueprint, render_template

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/')
def product_list():
    # Fetch products from the database
    products = [
        {'id': 1, 'name': 'Product 1', 'description': 'Description 1', 'price': 10, 'quantity': 5},
        {'id': 2, 'name': 'Product 2', 'description': 'Description 2', 'price': 20, 'quantity': 3},
        # Add more products as needed
    ]
    return render_template('product_list.html', products=products)

