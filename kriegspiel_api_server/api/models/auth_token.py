# -*- coding: utf-8 -*-

import random
import string

from django.db import models
from django.utils import timezone
from django.conf import settings


def random_string(n=100):
    return ''.join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits)
        for _ in range(n)
    )


class AuthToken(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(default=timezone.now)
    value = models.CharField(max_length=100, default=random_string, db_index=True)
