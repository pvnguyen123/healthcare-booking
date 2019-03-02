from healthcarebooking.extensions import db
from sqlalchemy.orm import relationship


class Company(db.Model):
    """Basic company model
    """
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False, comment='Company name')
    registerbyEmail =db.Column(db.String(80), unique=False, nullable=False, comment='Who registered the company')
    registerDate = db.Column(db.DateTime, nullable=False)
    confirmedDate = db.Column(db.DateTime, nullable=True)
    phone = db.Column(db.String(80), unique=False, nullable=False)
    active = db.Column(db.Boolean, default=True)

    # addresses = relationship("Address", back_populates="company")

    tasks = relationship("Task")
    profiles = relationship("CompanyPeople", back_populates="company")
    def __repr__(self):
        return f'<Company {self.name} {self.phone}>'
