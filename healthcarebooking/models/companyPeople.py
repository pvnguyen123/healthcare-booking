from healthcarebooking.extensions import db
from sqlalchemy.orm import relationship


class CompanyPeople(db.Model):
    #Basic company people assosiaction
    __tablename__ = 'company_people'
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), primary_key=True)
    join_date = db.Column(db.DateTime, nullable=False)
    separate_date = db.Column(db.DateTime, nullable=True)

    company = relationship("Company", back_populates="profiles")
    profile = relationship("Profile", back_populates="companies")

    # addresses = relationship("Address", back_populates="company")
    # people = relationship("Profile", secondary="company_people", back_populates="profile") #many to many. Company can have many people, people can be related to many companies (ie. providers).


    def __repr__(self):
        return f'<Company {self.name} {self.phone}>'
