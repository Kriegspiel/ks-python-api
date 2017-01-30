# -*- coding: utf-8 -*-

import enum
import chess

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


def validate_chess_square(square):
    if len(square) != 2 or not isinstance(square, str):
        raise ValidationError(_('square should be a two symbol string'))
    if square[0] not in 'abcdefgh':
        raise ValidationError(_('invalid row: {}'.format(square[0])))
    if square[1] not in '12345678':
        raise ValidationError(_('invalid column: {}'.format(square[1])))


class Move(models.Model):
    player = models.ForeignKey('kriegspiel.User', related_name='+')
    game = models.ForeignKey('kriegspiel.Game')
    created_at = models.DateTimeField(default=timezone.now)
    from_square = models.CharField(max_length=2,
                                   validators=[validate_chess_square])
    to_square = models.CharField(max_length=2,
                                 validators=[validate_chess_square])
    result = models.IntegerField()

    def as_python_chess_move(self):
        uci = self.from_square + self.to_square
        return chess.Move.from_uci(uci)


class MoveResult(object):
    INVALID = -1
    MOVED = 0
    PIECE_TAKEN = 1
    CHECK = 2
    CHECKMATE = 3
    STALEMATE = 4
    LOSS_ON_TIME = 5  # player has lost on time
    RESIGNATION = 6   # other player has resigned