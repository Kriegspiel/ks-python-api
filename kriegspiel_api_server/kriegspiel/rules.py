# -*- coding: utf-8 -*-


class BaseRuleSet(object):

    def validate_turn(self, game, turn):
        raise NotImplementedError()
