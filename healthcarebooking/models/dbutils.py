# NOTE: This was taken from the conduit mp

import logging
from sqlalchemy.inspection import inspect
from pin3.extensions import db

LOGGER = logging.getLogger(__name__)


def get_primary_keys(clss):
    """ Get the models primary keys. """
    return [key.name for key in inspect(clss).primary_key]


def get_column_names(clss):
    """ Get all column names. """
    return [column.key for column in clss.__table__.columns]


def from_dict(clss, data, filter_keys=[], ignore_keys=[]):
    """ Create record or adjust an existing one.

    :param dict data: The data that you want to insert into a record.
    :param list filter_keys: If provided, the keys that you want to check when you grab an existing entry.
    :return: The record that is created or updated.
    """
    record = None
    if len(filter_keys) == 0:
        # Try to grab a record based off of the primary key.
        record = clss.query.get(tuple([data.get(key) for key in get_primary_keys(clss)]))
    else:
        # Try to grab a record based off of the filter keys provided.
        filter_dict = {}
        for key in filter_keys:
            value = data.get(key)
            # This avoids the case where you have empty fields matching to pre-existing records.
            if value is not None:
                filter_dict[key] = data.get(key)
        if len(filter_dict) > 0:
            record = clss.query.filter_by(**filter_dict).first()

    if record is None:
        # Create a new record if one does not already exist.
        primary_keys = dict((key, data.get(key)) for key in get_primary_keys(clss))
        record = clss(**primary_keys)

    for key, value in data.items():
        if key not in ignore_keys:
            setattr(record, key, value)

    return record


def create(clss, *args, **kwargs):
    """ Create object and insert into database. """
    obj = clss(*args, **kwargs)
    db.session.add(obj)
    db.session.flush()
    return obj


def update(clss, **kwargs):
    """ Try to update a model.
    If the model does not exist based on the passed in primary keys, return None.
    You must pass in all primary keys.

    :param dict kwargs: Key word arguments passed in with the fields of the model.
    :return: The model that was updated or None.
    """
    primary_keys = [key.name for key in inspect(clss).primary_key]
    primary_key_filter = dict((k, kwargs[k]) for k in primary_keys)
    find_query = clss.query.filter_by(**primary_key_filter)
    if find_query.first():
        find_query.update(kwargs)
        return find_query.first()
    return None


def create_or_update(clss, **kwargs):
    """ Create or update an existing model with the arguments provided.
    If the model already exist, update it or create it if not.
    You must pass in all primary keys.

    :param dict kwargs: The fields of the model to update.
    :return: The model that was created or updated.
    """
    model = update(clss, **kwargs)
    if model is None:
        model = create(clss, **kwargs)
        db.session.add(model)
    return model
