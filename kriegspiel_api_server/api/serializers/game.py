# -*- coding: utf-8 -*-

from marshmallow import fields, validate

from api.serializers.base import Serializer
from api.serializers.user import UserSerializer
from api.serializers.fields import Timestamp, Username


class ListGamesQueryParams(Serializer):
    include_finished = fields.Boolean(default=False)
    limit = fields.Integer(default=100)
    offset = fields.Integer(default=0)


class GameSerializer(Serializer):
    created_by = Username(dump_only=True)
    created_at = Timestamp(dump_only=True)
    white = Username()
    black = Username()
    name = fields.String(validate=(validate.Length(min=1)), required=True)