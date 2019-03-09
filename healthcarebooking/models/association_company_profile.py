from healthcarebooking.extensions import db
from sqlalchemy import ForeignKey, Column, Integer, Enum


class AssociationCompanyProfile(db.Model):
    """ Basic company and profile assosiaction
    """
    __tablename__ = 'association_company_profile'
    company_id = Column(Integer, ForeignKey('company.id'), primary_key=True)
    profile_id = Column(Integer, ForeignKey('profile.id'), primary_key=True)
    association_type = Column(Enum('admin', 'member', 'client', 'provider'))

    def __repr__(self):
        return f'<AssociationCompanyProfile company {self.company_id}: profile {self.profile_id}>'
