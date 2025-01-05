# models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()

# Import all models that use db (SQLAlchemy instance)
from .user import User
from .product import Product  # Assuming Product is another model you have

# Optionally, you can define helper functions or variables related to models here
# models/__init__.py

from .category import Category
 # Import other models if present

# Optionally, you might configure your SQLAlchemy instance here if needed

from .reseller import Reseller
from .membership_discount import MembershipDiscount