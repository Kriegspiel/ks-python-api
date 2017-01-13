# -*- coding: utf-8 -*-

from django.http.response import JsonResponse


class ApiResponse(JsonResponse):
    """
    A JsonResponse class that wrappes response data in a dictionary with
    a `status` key and either `data` or `error` based on the status_code.
    """

    def __init__(self, data=None, status=200):
        if data is None:
            data = {}
        if status < 400:
            wrapped_data = {
                'status': 'ok',
                'data': data,
            }
        else:
            wrapped_data = {
                'status': 'error',
                'error': data,
            }
        super(ApiResponse, self).__init__(data=wrapped_data, status=status)
