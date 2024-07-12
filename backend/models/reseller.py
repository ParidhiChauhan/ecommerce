from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Reseller(Base):
    __tablename__ = 'resellers'

    id = Column(Integer, primary_key=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    available_wallet = Column(Float, default=0.0)
    membership = Column(String(50))
    total_credit_limit = Column(Float, default=0.0)
    mobile_number = Column(String(15))
    registration_date = Column(DateTime)

    def __repr__(self):
        return f"<Reseller(code='{self.code}', name='{self.name}', wallet={self.available_wallet})>"
