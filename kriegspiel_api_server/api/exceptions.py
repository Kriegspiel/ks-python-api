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


class ValidationError(ApiException):
    http_code = 400
    string_code = 'VALIDATION_ERROR'

    def __init__(self, errors_dict):
        self.errors = errors_dict

    def to_dict(self):
        d = super(ValidationError, self).to_dict()
        d.update({
            'errors': self.errors,
        })
        return d