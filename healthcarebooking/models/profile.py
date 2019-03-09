from healthcarebooking.extensions import db
from sqlalchemy import Column, DateTime, Integer, String, Boolean


class Profile(db.Model):
    """Basic user profile model definition
    """
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(80), nullable=True, index=True)
    lastname = Column(String(80), nullable=True, index=True)
    phone = Column(String(255), nullable=True, index=True)
    created = Column(DateTime, nullable=True, index=True)
    updated = Column(DateTime, nullable=True, index=True)
    active = Column(Boolean, default=True, index=True)

    def __repr__(self):
        return f'<Profile {self.id}>'
