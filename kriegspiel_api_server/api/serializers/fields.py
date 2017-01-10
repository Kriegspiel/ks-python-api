# -*- coding: utf-8 -*-

from datetime import datetime

import pytz
from marshmallow import fields
from django.conf import settings

from api import exceptions
from kriegspiel.models import User


class Timestamp(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is not None:
            return int(value.timestamp())
        else:
            return None

    def _deserialize(self, value, attr, data):
        value = int(value)
        timezone = pytz.timezone(settings.TIME_ZONE)
        return datetime.fromtimestamp(value, timezone)


class Username(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is not None:
            return value.username
        else:
            return None

    def _deserialize(self, value, attr, data):
        try:
            return User.objects.get(username=value)
        except User.DoesNotExist:
            raise exceptions.UserNotFound()
