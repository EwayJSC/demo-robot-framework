"""Base error of API"""


class BaseError(Exception):
    pass


class NotFound(BaseError):
    pass


class Invalid(BaseError):
    pass


class AuthError(BaseError):
    pass


class Forbidden(BaseError):
    pass


class Required(BaseError):
    pass


class BadRequest(BaseError):
    pass


class InternalError(BaseError):
    pass
