from flask import Blueprint, render_template,request, redirect, url_for

from models.membership_discount import db, MembershipDiscount
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin_dashboard.html')



@admin_bp.route('/membership_discount', methods=['GET', 'POST'])
def membership_discount():
    if request.method == 'POST':
        data = request.form.to_dict()
        discount_id = data.get('id')
        if discount_id:
            # Update existing discount
            discount = MembershipDiscount.query.get(discount_id)
            discount.min_price = data['min_price']
            discount.max_price = data['max_price']
            discount.gold = data['gold']
            discount.silver = data['silver']
            discount.bronze = data['bronze']
            db.session.commit()
        else:
            # Add new discount
            new_discount = MembershipDiscount(
                min_price=data['min_price'],
                max_price=data['max_price'],
                gold=data['gold'],
                silver=data['silver'],
                bronze=data['bronze']
            )
            db.session.add(new_discount)
            db.session.commit()
        return redirect(url_for('admin.membership_discount'))

    discounts = MembershipDiscount.query.all()
    return render_template('membership_discount.html', discounts=discounts)

@admin_bp.route('/delete_discount/<int:discount_id>', methods=['POST'])
def delete_discount(discount_id):
    discount = MembershipDiscount.query.get(discount_id)
    db.session.delete(discount)
    db.session.commit()
    return redirect(url_for('admin.membership_discount'))