# -*- coding: utf-8 -*-

import chess




class BaseRuleSet(object):

    def validate_turn(self, game, turn):
        raise NotImplementedError()

    def serialize_board(self, board):
        raise NotImplementedError()


class OrdinaryChess(BaseRuleSet):
    pass