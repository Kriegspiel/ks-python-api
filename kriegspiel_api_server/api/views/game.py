# -*- coding: utf-8 -*-

from api.views.base import AuthenticatedApiView, ApiView
from api.response import ApiResponse
from api.serializers.game import GameSerializer
from api.kriegspiel_helpers import get_user_or_api_exception

from kriegspiel.models import Game


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

