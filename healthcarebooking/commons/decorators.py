# General util methods
import logging
from flask import current_app
from functools import wraps
from linkedin.web import login_required as li_login_required
from pin3.extensions import db
from pin3.helpers.pagination import paginate

LOG = logging.getLogger(__name__)


def with_transaction(fn):
    """ A decorator that applies a transaction over a method
    """
    def decorate(*args, **kw):
        try:
            ret = fn(*args, **kw)
            db.session.commit()
            return ret

        except:
            db.session.rollback()
            raise

    return decorate


def marshal_with(schema_type: type, many: bool=False):
    """
    A decorator function for generating json data for
    @param schema_type: The marshmallow schema to use for serialization
    @param many: The response is a list of records
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            schema = schema_type(many=many)

            if many:
                return paginate(result, schema)

            return schema.dump(result).data, 200
        return wrapper

    return decorator


def login_required(func):
    """
    If you decorate a view with this, it will ensure that the current user is
    logged in and authenticated before calling the actual view. (If they are
    not, it calls the :attr:`LoginManager.unauthorized` callback.) For
    example::

        @app.route('/post')
        @login_required
        def post():
            pass

    If there are only certain times you need to require that your user is
    logged in, you can do so with::

        if not current_user.is_authenticated():
            return current_app.login_manager.unauthorized()

    ...which is essentially the code that this function adds to your views.

    It can be convenient to globally turn off authentication when unit
    testing. To enable this, if either of the application
    configuration variables `LOGIN_DISABLED` or `TESTING` is set to
    `True`, this decorator will be ignored.

    :param func: The view function to decorate.
    :type func: function
    """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        LOG.warn('auth disabled')
        return func(*args, **kwargs)

    return decorated_view if current_app.login_manager._login_disabled else li_login_required(func)
