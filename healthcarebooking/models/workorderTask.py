from healthcarebooking.extensions import db
from sqlalchemy.orm import relationship


class WorkorderTask(db.Model):
    """Basic workorder task model
    """
    __tablename__ = 'workorder_task'
    workorder_id = db.Column(db.Integer, db.ForeignKey('workorder.id'), primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), primary_key=True)


    # addresses = relationship("Address", back_populates="company")

    def __repr__(self):
        return f'<Workorder {self.id} {self.provider} {self.client} {self.creation} {self.status}>'
