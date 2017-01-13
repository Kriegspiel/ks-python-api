# -*- coding: utf-8 -*-

from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api.exceptions import AuthenticationError


class ApiView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ApiView, self).dispatch(request, *args, **kwargs)


class AuthenticatedApiView(ApiView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        user = getattr(request, 'user', None)
        if not user or not user.is_authenticated():
            raise AuthenticationError()
        return super(AuthenticatedApiView, self).dispatch(request, *args, **kwargs)
