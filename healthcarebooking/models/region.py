from healthcarebooking.extensions import db
from sqlalchemy import Column, DateTime, Integer, String, Boolean


class Region(db.Model):
    """Regions to be use for provider availability. This can be cities or any regions acceptable description
    """
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, index=True)

    def __repr__(self):
        return f'<Profile {self.name}>'
