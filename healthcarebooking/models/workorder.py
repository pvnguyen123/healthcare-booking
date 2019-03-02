from healthcarebooking.extensions import db
from sqlalchemy.orm import relationship


class Workorder(db.Model):
    """Basic workorder model
    """
    __tablename__ = 'workorder'
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.Integer, db.ForeignKey('profile.id'))
    client = db.Column(db.Integer, db.ForeignKey('profile.id'))
    creation = db.Column(db.DateTime, nullable=False)
    acceptance = db.Column(db.DateTime, nullable=True)
    closure = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(80), unique=False, nullable=False)
    notes = db.Column(db.String(2000), unique=False, nullable=True)
    active = db.Column(db.Boolean, default=True)

    # addresses = relationship("Address", back_populates="company")
    profiles = relationship("CompanyPeople", back_populates="company")
    tasks = relationship("Task")

    def __repr__(self):
        return f'<Workorder {self.id} {self.provider} {self.client}{self.creation}{self.status}>'
