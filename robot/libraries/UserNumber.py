"""
Library to test user number service

Test target: User Number service
To cover:
✔ Get current number                GET        /users/<username>/number
✔ Create new number                 POST       /users/<username>/number
"""
import requests

from libraries import utils
from libraries import BaseLib


class UserNumber(BaseLib):
    def __init__(self):
        super(UserNumber, self).__init__()

    def tear_down(self):
        pass

    def set_up(self):
        pass

    @utils.catch_exception
    def get_user_number(self, name):
        """
        Get current number of user - GET /users/<name>/number
        :param name: name of user
        """
        url = self.ENDPOINTS_SERVICE + "/users/%s/number" % name
        result = requests.get(url)

        try:
            assert result.status_code == 200
        except AssertionError:
            self.thing_not_ok(result)

        self._result = True
        self._error = None
        return result.content

    @utils.catch_exception
    def create_user_number(self, name):
        """
        Get current number of user - POST /users/<name>/number
        :param name: name of user
        """
        url = self.ENDPOINTS_SERVICE + "/users/%s/number" % name
        result = requests.post(url)

        try:
            assert result.status_code == 200
        except AssertionError:
            self.thing_not_ok(result)

        self._result = True
        self._error = None
        return result.content

    @staticmethod
    def random_username():
        """Generate random new user name"""
        return utils.random_string(10)
