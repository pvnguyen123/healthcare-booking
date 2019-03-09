"""Simple blacklist implementation using database

Using database may not be your prefered solution to handle blacklist in your
final application, but remember that's just a cookiecutter template. Feel free
to dump this code and adapt it for your needs.

For this reason, we don't include advanced tokens management in this
example (view all tokens for a user, revoke from api, etc.)

If we choose to use database to handle blacklist in this example, it's mainly
because it will allow you to run the example without needing to setup anything else
like a redis or a memcached server.

This example is heavily inspired by https://github.com/vimalloc/flask-jwt-extended/blob/master/examples/database_blacklist/
"""
from healthcarebooking.extensions import db
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class TokenBlacklist(db.Model):
    """Blacklist representation
    """
    id = Column(Integer, primary_key=True)
    jti = Column(String(36), nullable=False, unique=True)
    token_type = Column(String(10), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    revoked = Column(Boolean, nullable=False)
    expires = Column(DateTime, nullable=False)

    user = relationship('User', lazy='joined')

    def to_dict(self):
        return {
            'token_id': self.id,
            'jti': self.jti,
            'token_type': self.token_type,
            'user_identity': self.user_identity,
            'revoked': self.revoked,
            'expires': self.expires
        }
