# -*- coding: utf-8 -*-

import enum

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_chess_square(square):
    if len(square) != 2 or not isinstance(square, str):
        raise ValidationError(_('square should be a two symbol string'))
    if square[0] not in 'abcdefgh':
        raise ValidationError(_('invalid row: {}'.format(square[0])))
    if square[1] not in '12345678':
        raise ValidationError(_('invalid column: {}'.format(square[1])))


class Turn(models.Model):
    player = models.ForeignKey('kriegspiel.User', related_name='+')
    game = models.ForeignKey('kriegspiel.Game')
    from_square = models.CharField(max_length=2,
                                   validators=[validate_chess_square])
    to_square = models.CharField(max_length=2,
                                 validators=[validate_chess_square])
    result = models.IntegerField()


class TurnResult(object):
    INVALID = -1
    MOVED = 0
    PIECE_TAKEN = 1
    CHECK = 2
    CHECKMATE = 3
    STALEMATE = 4
    LOSS_ON_TIME = 5  # player has lost on time
    RESIGNATION = 6   # other player has resigned