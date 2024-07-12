from flask import Blueprint, render_template
import requests

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    products = requests.get('http://localhost:5000/products/list').json()
    return render_template('index.html', products=products)

@main_bp.route('/product/<int:product_id>')
def product_details(product_id):
    product = requests.get(f'http://localhost:5000/products/{product_id}').json()
    return render_template('product_details.html', product=product)
