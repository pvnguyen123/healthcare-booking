"""Default configuration

Use env var to override
"""
DEBUG = True
SECRET_KEY = "changeme"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/booking_stg"
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
