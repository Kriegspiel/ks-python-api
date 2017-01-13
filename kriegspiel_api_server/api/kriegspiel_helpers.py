# -*- coding: utf-8 -*-

from kriegspiel.models import User
from api import exceptions


def get_user_or_api_exception(username, ):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        raise exceptions.UserNotFound()
