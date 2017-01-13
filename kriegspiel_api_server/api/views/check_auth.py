# -*- coding: utf-8 -*-


from api.views.base import ApiView
from api.response import ApiResponse
from api.exceptions import NotAuthenticated


class CheckAuth(ApiView):

    def get(self, request):
        if request.user and request.user.is_authenticated():
            return ApiResponse()
        else:
            raise NotAuthenticated
