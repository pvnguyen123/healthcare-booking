from healthcarebooking.extensions import db
from sqlalchemy import ForeignKey, Column, Integer, Enum, DateTime, Boolean, Text
from sqlalchemy.orm import relationship


class WorkOrder(db.Model):
    """Basic workorder model
    """
    __tablename__ = 'work_order'
    id = Column(Integer, primary_key=True)
    provider = Column(Integer, ForeignKey('profile.id'), index=True)
    client = Column(Integer, ForeignKey('profile.id'), index=True)
    company_id = Column(Integer, ForeignKey('company.id'), index=True)
    address = Column(Integer, ForeignKey('address.id'), index=True)

    status = Column(Enum('open', 'closed'), index=True)
    notes = Column(Text)
    active = Column(Boolean, default=True, index=True)
    schedule_date = Column(DateTime, nullable=False, index=True)
    acceptance = Column(DateTime, index=True)
    completed = Column(DateTime, index=True)
    created = Column(DateTime, index=True)
    last_updated = Column(DateTime, index=True)

    addresses = relationship("Address")
    company = relationship("Company")
    tasks = relationship("Task", secondary='association_workorder_task')

    def __repr__(self):
        return f'<WorkOrder {self.id}>'
