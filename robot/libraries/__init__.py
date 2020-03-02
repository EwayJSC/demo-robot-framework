"""Test libraries contains all the implementation of keywords"""
import os

from robot.api import logger

from libraries import errors


ENVIRONMENT_SWITCHER = {
    "PIPELINE": "http://api:8080",
    "STAGING": "https://staging.api.com",
    "PRODUCTION": "http://production.api.com"
}


ERROR = {
    "NotFound": errors.NotFound,
    "Invalid": errors.Invalid,
    "AuthError": errors.AuthError,
    "Forbidden": errors.Forbidden,
    "Required": errors.Required,
    "BadRequest": errors.BadRequest,
    "InternalError": errors.InternalError
}


class BaseLib(object):
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'PIPELINE')
    ENDPOINTS_SERVICE = ENVIRONMENT_SWITCHER.get(
        ENVIRONMENT, ENVIRONMENT_SWITCHER["PIPELINE"])

    def __init__(self):
        self._result = None  # the result of test should be set in this param
        self._error = None
        self._response = None
        self.logger = logger

    def set_up(self):
        """
        Set up DB and env, inject default sample for testing purpose
        :return: void
        """
        raise NotImplementedError

    def tear_down(self):
        """
        Tear down function, call at the end of test
        :return: void
        """
        raise NotImplementedError

    def thing_not_ok(self, result):
        self._response = result.content
        self.logger.error(self._response)

    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        Example:
        | Push Buttons     | 1 + 2 = |
        | Result Should Be | 3       |
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))

    def should_be_error(self, exp=None):
        """Verifies that the current result is an Exception.

        Example:
        | Push Buttons     | 1 / 0 = |
        | Should be error  | AuthError
        """
        assert self._result == exp

    def should_be_success(self):
        try:
            assert self._result is True
            assert self._error is None
        except AssertionError as e:
            self.logger.error(self._response)
            raise e
