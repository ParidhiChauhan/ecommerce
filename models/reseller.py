from . import db
from datetime import datetime
class Reseller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reseller_code = db.Column(db.String(20), unique=True, nullable=False)
    reseller_name = db.Column(db.String(100), nullable=False)
    available_wallet = db.Column(db.Float, nullable=False)
    membership = db.Column(db.String(50))
    total_credit_limit = db.Column(db.Float, nullable=False)
    mobile_number = db.Column(db.String(15))
    registration_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Reseller(db.Model):
#     __tablename__ = 'resellers'

#     id = db.Column(db.Integer, primary_key=True)
#     reseller_code = db.Column(db.String(20), unique=True, nullable=False)
#     reseller_name = db.Column(db.String(100), nullable=False)
#     available_wallet = db.Column(db.Float, nullable=False)
#     membership = db.Column(db.String(50))
#     total_credit_limit = db.Column(db.Float, nullable=False)
#     mobile_number = db.Column(db.String(15))
#     registration_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self):
#         return f'<Reseller {self.reseller_code}>'

