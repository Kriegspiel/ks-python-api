# -*- coding: utf-8 -*-

from django.db import models


class MoveResult(models.Model):
    move = models.ForeignKey('Move')

