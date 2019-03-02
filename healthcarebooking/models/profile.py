from healthcarebooking.extensions import db
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import relationship


class Profile(db.Model):
    """Basic user model
    """
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(80), nullable=True, index=True)
    lastname = Column(String(80), nullable=True, index=True)
    phone = Column(String(255), nullable=True, index=True)
    created = Column(DateTime, nullable=True, index=True)
    updated = Column(DateTime, nullable=True, index=True)
    active = Column(Boolean, default=True, index=True)

    addresses = relationship("Address", back_populates="profile")
    companies = relationship("CompanyPeople", back_populates="profile")


    def __repr__(self):
        return f'<Person {self.firstname} {self.lastname}>'
