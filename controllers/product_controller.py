from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import db
from models.product import Product

product_bp = Blueprint('product', __name__)
@product_bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        category = request.form['category']
        product_code = request.form['product_code']
        name = request.form['name']
        product_title = request.form['product_title']

        product_price = float(request.form['product_price'])
        product_quantity = int(request.form['product_quantity'])
        track_quantity = True if request.form.get('track_quantity') else False
        product_status = request.form['product_status']
        free_shipping = request.form['free_shipping']
        product_variant = request.form['product_variant']

        new_product = Product(
            category=category,
            product_code=product_code,
            name=name,
            product_title=product_title,
            
            product_price=product_price,
            product_quantity=product_quantity,
            track_quantity=track_quantity,
            product_status=product_status,
            free_shipping=free_shipping,
            product_variant=product_variant
        )

        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('product.list_products'))

    return render_template('add_product.html')

@product_bp.route('/list', methods=['GET'])
def list_products():
    products = Product.query.all()
    return render_template('product_list.html', products=products)
