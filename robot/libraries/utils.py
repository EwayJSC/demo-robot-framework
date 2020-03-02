import functools
import random
import string

from libraries.errors import BaseError


def random_string(length):
    """Random a string with specific length"""
    return ''.join([random.choice(string.ascii_letters) for _ in range(length)])


def catch_exception(f):
    @functools.wraps(f)
    def func(self, *args, **kwargs):
        try:
            self._result = True
            self._error = None
            return f(self, *args, **kwargs)
        except BaseError as e:
            self._result = e.__class__.__name__
            self._error = e
            return e

    return func
