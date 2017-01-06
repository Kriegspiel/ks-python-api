# -*- coding: utf-8 -*-

from marshmallow import fields, validate

from api.serializers.base import Serializer


class SignInSerializer(Serializer):
    email = fields.String(load_only=True,
                          required=True,
                          validate=[validate.Email, validate.Length(1, 100)])
    password = fields.String(validate=[validate.Length(1, 100)],
                             required=True,
                             load_only=True)
