from healthcarebooking.extensions import db
from sqlalchemy import ForeignKey, Column, Integer, Boolean, String, DateTime
from sqlalchemy.orm import relationship


class Company(db.Model):
    """Basic company model
    """
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), comment='Company Name', index=True)
    email = Column(String(80), comment='Who registered the company', index=True)
    phone = Column(String(80), comment='Company Phone Number', index=True)
    active = Column(Boolean, default=True, comment='Company is active flag', index=True)
    address_id = Column(Integer, ForeignKey('address.id'), comment='Company Address', index=True)
    created = Column(DateTime, index=True)
    last_updated = Column(DateTime, index=True)

    address = relationship("Address")
    profiles = relationship("Profile", secondary="association_company_profile")

    def __repr__(self):
        return f'<Company {self.id} {self.name}>'
