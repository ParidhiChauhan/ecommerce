from flask import Flask, render_template, request, redirect, url_for, flash
from models import db
from controllers.auth_controller import auth_bp
from controllers.admin_controller import admin_bp
from controllers.product_controller import product_bp
from controllers.category_controller import category_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:root@localhost/ecommerce_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(category_bp, url_prefix='/categories')
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    subcategories = db.relationship('Category', backref=db.backref('parent', remote_side=[id]), lazy='dynamic')

    def __repr__(self):
        return f'<Category {self.name}>'


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        new_category_name = request.form.get('new_category_name')
        is_parent = request.form.get('is_parent')

        if new_category_name:
            if is_parent == 'yes':
                new_category = Category(name=new_category_name)
            else:
                parent_category_id = request.form.get('parent_category')
                parent_category = Category.query.get(parent_category_id)
                if parent_category:
                    new_category = Category(name=new_category_name, parent_id=parent_category.id)
                else:
                    flash('Parent category not found!', 'danger')
                    return redirect(url_for('add_category'))

            db.session.add(new_category)
            db.session.commit()
            flash('Category added successfully!', 'success')
            return redirect(url_for('add_category'))
        else:
            flash('Category name is required!', 'danger')

        return redirect(url_for('add_category'))

    categories = Category.query.all()
    return render_template('add_category.html', categories=categories)

@app.route('/reseller/create', methods=['GET', 'POST'])
def create_reseller():
    # Implementation code for creating a reseller
    return render_template('create_reseller.html')

@app.route('/resellers', methods=['GET'])
def list_resellers():
    resellers = [
        {'code': '001', 'name': 'Reseller 1'},
        {'code': '002', 'name': 'Reseller 2'},
        # Add more reseller data as needed
    ]
    return render_template('list_resellers.html', resellers=resellers)

@app.route('/admin/dashboard')
def admin_dashboard():
    categories = Category.query.all()
    return render_template('admin_dashboard.html', categories=categories)

@app.route('/product/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Handle form submission
        # ...
        pass

    categories = Category.query.all()
    return render_template('add_product.html', categories=categories)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

