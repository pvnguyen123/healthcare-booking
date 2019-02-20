import flask
from flask import Flask
from flask_cors import CORS
from datetime import timedelta
from urllib.parse import quote_plus as urlquote

from healthcarebooking import auth, api
from healthcarebooking.extensions import db, jwt, migrate


def create_app(config=None, testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('healthcarebooking', static_folder='../healthcarebooking-fe/dist')

    configure_app(app, testing)
    configure_extensions(app, cli)
    register_blueprints(app)
    register_static_contents(app)

    @app.before_request
    def make_session_permanent():
        flask.session.permanent = True
        app.permanent_session_lifetime = timedelta(days=14)

    @app.teardown_request
    def teardown_request(e=None):
        """ Ensure sessions are clean up after each request
        """
        if e:
            db.session.rollback()
        db.session.remove()

    return app


def configure_app(app, testing=False):
    """set configuration for application
    """
    # default configuration
    app.config.from_object('healthcarebooking.config')

    if testing is True:
        # override with testing config
        app.config.from_object('healthcarebooking.configtest')
    else:
        # override with env variable, fail silently if not set
        app.config.from_envvar("HEALTHCAREBOOKING_CONFIG", silent=True)

    db_user = urlquote(app.config['DB_USER'])
    db_password = app.config.get('DB_PASSWORD')
    db_password = urlquote(db_password) if db_password else None
    db_host = urlquote(app.config['DB_HOST'])
    db_name = urlquote(app.config['DB_NAME'])

    if db_password:
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}?ssl_ca=BaltimoreCyberTrustRoot.crt.pem'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}@{db_host}/{db_name}'

    # Setup CORs
    headers = ['accept', 'origin', 'Content-Type']
    origins = ['http://localhost:4200/*', 'http://localhost:5000/*']
    CORS(app,
        origins=origins,
        resources=['/api/*', '/auth/*'],
        allow_headers=headers,
        supports_credentials=True)


def configure_extensions(app, cli):
    """configure flask extensions
    """
    db.init_app(app)
    jwt.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)


def register_static_contents(app):
    # Routes
    @app.route('/')
    def root():
        return app.send_static_file('index.html')

    @app.route('/<path:path>')
    def static_proxy(path):
        # send_static_file will guess the correct MIME type
        return app.send_static_file(path)
