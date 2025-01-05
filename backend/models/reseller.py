

from . import db

class Reseller(db.Model):
    __tablename__ = 'resellers'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    available_wallet = db.Column(db.Float, default=0.0)
    membership = db.Column(db.String(50))
    total_credit_limit = db.Column(db.Float, default=0.0)
    mobile_number = db.Column(db.String(15))
    registration_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Reseller(code='{self.code}', name='{self.name}', wallet={self.available_wallet})>"
