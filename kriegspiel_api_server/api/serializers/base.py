# -*- coding: utf-8 -*-

from marshmallow import Schema

from api.exceptions import ApiValidationError


class Serializer(Schema):

    def __init__(self, *args, **kwargs):
        super(Serializer, self).__init__(*args, **kwargs)
        self.errors = None

    def load_data(self, data):
        """
        Deserialize data to an object defined by its Schema and raises a
        ValidationError if there are eny errors.
        :param data:
        :return:
        """
        data, errors = self.load(data)
        if errors:
            raise ApiValidationError(errors)
        return data
