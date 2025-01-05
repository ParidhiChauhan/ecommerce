# category_controller.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Category

category_bp = Blueprint('category', __name__, url_prefix='/category')

@category_bp.route('/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        new_category_name = request.form.get('new_category_name')
        parent_option = request.form.get('parent_option')
        parent_category_id = request.form.get('parent_category')
        new_subcategory_name = request.form.get('new_subcategory_name')

        if new_category_name:
            # Create new category
            new_category = Category(name=new_category_name)

            if parent_option == 'parent':
                # If it's a parent category
                db.session.add(new_category)
                db.session.commit()
                flash('New parent category added successfully!', 'success')
            elif parent_option == 'not_parent' and parent_category_id:
                # If it's a subcategory
                parent_category = Category.query.get(parent_category_id)
                if parent_category:
                    new_subcategory = Category(name=new_subcategory_name, parent=parent_category)
                    db.session.add(new_subcategory)
                    db.session.commit()
                    flash('New subcategory added successfully!', 'success')
                else:
                    flash('Parent category not found!', 'danger')
            else:
                flash('Invalid category information!', 'danger')

            return redirect(url_for('category.add_category'))

    categories = Category.query.all()
    return render_template('add_category.html', categories=categories)



