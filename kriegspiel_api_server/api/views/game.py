# -*- coding: utf-8 -*-

from django.db import transaction

from api.views.base import AuthenticatedApiView, ApiView
from api.response import ApiResponse
from api.serializers.game import GameSerializer
from api import exceptions

from kriegspiel.models import Game, Move


class GamesView(AuthenticatedApiView):

    def get(self, request):
        """
        List all games.
        """
        return ApiResponse()

    def post(self, request):
        """
        Create a new game.
        """
        input_serializer = GameSerializer().load_data(request.POST)
        game = Game.objects.create(
            created_by=request.user,
            name=input_serializer['name'],
            white=input_serializer.get('white'),
            black=input_serializer.get('black'),
        )
        output_serializer, errors = GameSerializer().dump(game)
        return ApiResponse(data=output_serializer)

class TurnView(AuthenticatedApiView):

    def post(self, request, game_id):
        game = Game.objects.filter(id=game_id).first()
        if game is None or request.user.id not in [game.white_id, game.black_id]:
            raise exceptions.NotFound()
        with transaction.atomic():
            pass # todo: validate move, save it to db