# -*- coding: utf-8 -*-

import chess
from django.db import models
from django.utils import timezone, cache
from django.utils.functional import cached_property

import kriegspiel.models


class Game(models.Model):

    white = models.ForeignKey('kriegspiel.User', related_name='+', null=True)
    black = models.ForeignKey('kriegspiel.User', related_name='+', null=True)
    created_by = models.ForeignKey('kriegspiel.User', related_name='+')
    created_at = models.DateTimeField(default=timezone.now)
    rules = models.CharField(max_length=100, default='chess')
    name = models.CharField(max_length=200)

    @cached_property
    def board(self):
        print('running query')
        board = chess.Board()
        for move in self.move_set.order_by('created_at').all():
            board.push(move.as_python_chess_move())
        return board