# -*- coding: utf-8 -*-

from marshmallow import fields

from api.serializers.base import Serializer


class UserSerializer(Serializer):
    username = fields.String()
