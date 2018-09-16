import flask
from flask import Flask
from flask_cors import CORS
from datetime import timedelta

from healthcarebooking import auth, api
from healthcarebooking.extensions import db, jwt, migrate
from http.client import FORBIDDEN, UNAUTHORIZED


def create_app(config=None, testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('healthcarebooking')

    configure_app(app, testing)
    configure_extensions(app, cli)
    register_blueprints(app)


    @app.errorhandler(UNAUTHORIZED)
    @app.errorhandler(FORBIDDEN)
    def forbidden_handler(error):
        return 'UNAUTHORIZED', UNAUTHORIZED

    @app.errorhandler(404)
    def not_found_handler(error):
        return error, 404

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

    # Setup CORs
    headers = ['accept', 'origin', 'Content-Type']
    origins = ['http://localhost:4200/*', 'http://localhost:5000/*']
    CORS(app,
        origins=origins,
        resources=['/api/*', '/admin', '/auth'],
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
