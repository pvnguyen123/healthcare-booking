''' General util methods
'''
from itertools import zip_longest
import time
import flask


def remove_emptys(arr):
    return [item for item in arr if item]


def dasherize(text):
    return text.replace('_', '-')


def append_ts(text):
    now = round(time.time())
    return f'{text}&_ts={now}'


def get_timestamp():
    return round(time.time())


def union(*args):
    ''' Merge multiple arguments together and remoreve dups and emptys
    '''
    results = []
    for item in args:
        if isinstance(item, (list, tuple)):
            results.extend(item)
        else:
            results.append(item)

    results = remove_emptys(results)
    return list(set(results))


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def strip_non_ascii(value):
    """
    Strip and ignore all non ascii char
    """
    return ''.join([i if ord(i) < 128 else ' ' for i in value])


def error_response(status_code, message=None, errors=None):
    """Create an error response that conforms to the JSON API specification.

    :param str message: the error message to put in the "details" key
    :param int status_code: an error HTTP status code
    :returns: a Flask response
    :rtype: :class:`flask.Response`
    """
    response = None
    if errors:
        response = flask.jsonify(errors)
    else:
        response = flask.jsonify({
            'errors': [
                {
                    'detail': message,
                },
            ],
        })

    response.status_code = status_code
    return response
