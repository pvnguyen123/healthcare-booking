from healthcarebooking.extensions import db
from sqlalchemy import ForeignKey, Column, Integer


class AssociationUserRegion(db.Model):
    """Basic provider region association definition. This is use to deterine whixh regions a provider will work
    """
    __tablename__ = 'association_user_region'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    region_id = Column(Integer, ForeignKey('region.id'), primary_key=True)

    def __repr__(self):
        return f'<AssociationWorkOrderTask {self.user_id} {self.region_id}>'
