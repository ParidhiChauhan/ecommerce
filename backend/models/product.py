from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), nullable=False)
    product_code = db.Column(db.String(80), nullable=False)
    product_title = db.Column(db.String(120), nullable=False)
    
    product_price = db.Column(db.Float, nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    track_quantity = db.Column(db.Boolean, default=False)
    product_status = db.Column(db.String(10), nullable=False)
    free_shipping = db.Column(db.String(10), nullable=False)
    product_variant = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(255), nullable=False)  # Example of a required field