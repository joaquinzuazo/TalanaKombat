from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from talana.process.fight import fight
from talana.process.helpers.helpers import validation_data


@api_view(["POST"])
def combat(request):
    if validation_data(request.data):
        movements_and_hits_player1 = request.data.get("player1")
        movements_and_hits_player2 = request.data.get("player2")
        response = fight(movements_and_hits_player1, movements_and_hits_player2)
        return Response(response, status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "Alguna dato se encuentra vacío o incorrecto"},
            status=status.HTTP_400_BAD_REQUEST,
        )
