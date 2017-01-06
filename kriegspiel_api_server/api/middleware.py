# -*- coding: utf-8 -*-

import warnings

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AnonymousUser
from django.conf import settings

from api.exceptions import ApiException
from api.response import ApiResponse
from api.models import AuthToken


class ApiMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, ApiException):
            return ApiResponse(exception.to_dict(), exception.http_code)


def token_middleware(get_response):
    """
    A middleware that checks authentication token and sets request.user instance
    if the token is valid.
    """
    def middleware(request):
        if request.user is not None:
            warnings.warn(_("request.user has been set before token_middleware"
                            " and will be overriten. To disable this message"
                            " remove AuthenticationMiddleware from middleware"
                            "list."))
        token_header = request.META.get(settings.TOKEN_HEADER)
        token_value = token_header.split(settings.TOKEN_PREFIX)[-1].strip()
        token = AuthToken.objects.filter(
            value=token_value, user_id__is_active=True).first()
        if token:
            request.user = token.user
        else:
            request.user = AnonymousUser()
        return get_response(request)

    return middleware