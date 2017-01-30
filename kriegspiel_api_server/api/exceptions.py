# -*- coding: utf-8 -*-


class ApiException(Exception):
    """
    Base Kriegspiel API exception.
    """
    http_code = None
    string_code = None

    def to_dict(self):
        return {
            'code': self.string_code,
        }


class NotAuthenticated(ApiException):
    http_code = 401
    string_code = 'NOT_AUTHENTICATED'


class AuthenticationError(ApiException):
    http_code = 401
    string_code = 'AUTHENTICATION_FAILED'


class ApiValidationError(ApiException):
    http_code = 400
    string_code = 'VALIDATION_ERROR'

    def __init__(self, errors_dict):
        self.errors = errors_dict

    def to_dict(self):
        d = super(ApiValidationError, self).to_dict()
        d.update({
            'errors': self.errors,
        })
        return d


class UserNotFound(ApiException):
    http_code = 403
    string_code = 'USER_NOT_FOUND'


class NotFound(ApiException):
    http_code = 404
    string_code = 'NOT_FOUND'