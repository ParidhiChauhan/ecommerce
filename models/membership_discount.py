from . import db

class MembershipDiscount(db.Model):
    __tablename__ = 'membership_discounts'

    id = db.Column(db.Integer, primary_key=True)
    min_price = db.Column(db.Numeric(10, 2), nullable=False)
    max_price = db.Column(db.Numeric(10, 2), nullable=False)
    gold = db.Column(db.Integer, nullable=False)
    silver = db.Column(db.Integer, nullable=False)
    bronze = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<MembershipDiscount {self.id}>'

