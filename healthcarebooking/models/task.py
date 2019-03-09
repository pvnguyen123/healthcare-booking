from healthcarebooking.extensions import db
from sqlalchemy import ForeignKey, Column, Integer, DateTime, String, Text


class Task(db.Model):
    """ Task Table Definition
    """
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, comment='Task Name', index=True)
    description = Column(Text, comment='Task Description')
    duration = Column(Integer, nullable=True, index=True)
    company_id = Column(Integer, ForeignKey('company.id'), index=True)
    created = Column(DateTime, index=True)
    last_updated = Column(DateTime, index=True)

    def __repr__(self):
        return f'<Task {self.name}>'
