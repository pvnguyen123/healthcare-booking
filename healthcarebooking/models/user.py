from healthcarebooking.extensions import db, pwd_context
from sqlalchemy import Column, Integer, String, Boolean


class User(db.Model):
    """Basic user model
    """
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False, index=True)
    email = Column(String(80), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    active = Column(Boolean, default=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def __repr__(self):
        return "<User %s>" % self.username
