from healthcarebooking.extensions import db
from sqlalchemy import ForeignKey, Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import relationship


class Address(db.Model):
    """Basic user model
    """
    id = Column(Integer, primary_key=True)
    line1 = Column(String(250), nullable=False, index=True)
    line2 = Column(String(250), index=True)
    city = Column(String(80), index=True)
    state = Column(String(80), index=True)
    zipcode = Column(String(80), index=True)
    active = Column(Boolean, default=True, index=True)
    created = Column(DateTime, index=True)
    updated = Column(DateTime, index=True)

    profile_id = Column(Integer, ForeignKey('profile.id'), index=True)
    profile = relationship("Profile", back_populates="addresses")

    def __repr__(self):
        return f'<Address {self.line1}>'
