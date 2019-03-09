from healthcarebooking.extensions import db
from sqlalchemy import Column, DateTime, Integer, String, Boolean


class Address(db.Model):
    """Basic user model
    """
    id = Column(Integer, primary_key=True)
    line1 = Column(String(250), nullable=False, index=True)
    line2 = Column(String(250), index=True)
    city = Column(String(80), nullable=False, index=True)
    state = Column(String(80), nullable=False, index=True)
    zip_code = Column(String(80), nullable=False, index=True)
    active = Column(Boolean, default=True, index=True)
    created = Column(DateTime, index=True)
    updated = Column(DateTime, index=True)

    def __repr__(self):
        return f'<Address {self.line1}>'
