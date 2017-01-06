# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model

from api.views.base import ApiView
from api.serializers.auth import SignInSerializer
from api.exceptions import AuthenticationError
from api.response import ApiResponse
from api.models import AuthToken

from django.db import connection


class SignIn(ApiView):
    def post(self, request):
        data = SignInSerializer().load_data(request.POST)
        user = get_user_model().objects.filter(email=data['email']).first()
        if user is None or not user.check_password(data['password']):
            raise AuthenticationError()
        token = AuthToken.objects.create(user_id=user.id)
        print(connection.queries)
        return ApiResponse({'token': token.value})
