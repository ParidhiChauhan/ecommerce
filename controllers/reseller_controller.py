from flask import Blueprint, render_template, redirect, url_for, request, flash
from datetime import datetime
from models import db
from models.reseller import Reseller

# reseller_bp = Blueprint('reseller', __name__, url_prefix='/reseller')
reseller_bp = Blueprint('reseller', __name__)
@reseller_bp.route('/create', methods=['GET', 'POST'])
def create_reseller():
    if request.method == 'POST':
        try:
            code_val = request.form['code']
            # return code
            name = request.form['name']
            available_wallet = float(request.form['available_wallet'])
            membership = request.form.get('membership', None)  # Optional field
            total_credit_limit = float(request.form['total_credit_limit'])
            mobile_number = request.form.get('mobile_number', None)  # Optional field
            registration_date = datetime.strptime(request.form['registration_date'], '%Y-%m-%d')
            
            # Create a new Reseller object and add it to the database
            new_reseller = Reseller(
                reseller_code=code_val,
                reseller_name=name,
                available_wallet=available_wallet,
                membership=membership,
                total_credit_limit=total_credit_limit,
                mobile_number=mobile_number,
                registration_date=registration_date
            )
            # return new_reseller
            db.session.add(new_reseller)
            db.session.commit()
            
            # Redirect to the reseller list or another appropriate page after successful creation
            return redirect(url_for('reseller.list_resellers'))

        except KeyError as e:
            # Handle KeyError gracefully (e.g., log error, display a message to the user)
            error_message = f"KeyError: {str(e)}"
            return render_template('error.html', error_message=error_message)

        except ValueError as e:
            # Handle ValueError for type conversion (e.g., invalid date format)
            error_message = f"ValueError: {str(e)}"
            return render_template('error.html', error_message=error_message)

    # If it's a GET request, render the form template
    return render_template('create_reseller.html')
@reseller_bp.route('/list')
def list_resellers():
    
    resellers = Reseller.query.all()
    return render_template('list_resellers.html', resellers=resellers)