from healthcarebooking.extensions import db
from sqlalchemy.orm import relationship


class Task(db.Model):
    #Task Table
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False, comment='task name')
    expected_duration = db.Column(db.Integer, nullable=True)
    datecreated = db.Column(db.DateTime, nullable=False)
    datedeleted = db.Column(db.DateTime, nullable=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    # addresses = relationship("Address", back_populates="company")
    # people = relationship("Profile", secondary="company_people", back_populates="profile") #many to many. Company can have many people, people can be related to many companies (ie. providers).
    #workorders = relationship("WorkorderTask", back_populates="task")

    def __repr__(self):
        return f'<Company {self.name} {self.phone}>'
