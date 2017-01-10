# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Game(models.Model):

    white = models.ForeignKey('kriegspiel.User', related_name='+', null=True)
    black = models.ForeignKey('kriegspiel.User', related_name='+', null=True)
    created_by = models.ForeignKey('kriegspiel.User', related_name='+')
    created_at = models.DateTimeField(default=timezone.now)
    rules = models.CharField(max_length=100, default='chess')
    name = models.CharField(max_length=200)
