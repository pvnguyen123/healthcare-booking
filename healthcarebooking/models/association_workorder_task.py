from healthcarebooking.extensions import db
from sqlalchemy import ForeignKey, Column, Integer


class AssociationWorkOrderTask(db.Model):
    """Basic workorder task relatinship definition
    """
    __tablename__ = 'association_workorder_task'
    workorder_id = Column(Integer, ForeignKey('work_order.id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('task.id'), primary_key=True)

    def __repr__(self):
        return f'<AssociationWorkOrderTask {self.workorder_id} {self.task_id}>'
