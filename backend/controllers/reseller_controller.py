from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from . import db
from models.reseller import Reseller

reseller_bp = Blueprint('reseller', __name__, url_prefix='/admin/reseller')

@reseller_bp.route('/list')
def list_resellers():
    resellers = Reseller.query.all()
    return render_template('admin/reseller_list.html', resellers=resellers)

@reseller_bp.route('/create', methods=['GET', 'POST'])
def create_reseller():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        available_wallet = float(request.form['available_wallet'])
        membership = request.form['membership']
        total_credit_limit = float(request.form['total_credit_limit'])
        mobile_number = request.form['mobile_number']
        registration_date = datetime.strptime(request.form['registration_date'], '%Y-%m-%d')

        new_reseller = Reseller(
            code=code,
            name=name,
            available_wallet=available_wallet,
            membership=membership,
            total_credit_limit=total_credit_limit,
            mobile_number=mobile_number,
            registration_date=registration_date
        )

        db.session.add(new_reseller)
        db.session.commit()

        return redirect(url_for('reseller.list_resellers'))

    return render_template('admin/create_reseller.html')
