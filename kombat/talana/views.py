from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def combat(request):
    movements_and_hits_player1 = request.data.get("player1")
    movements_and_hits_player2 = request.data.get("player2")
    return Response(status=status.HTTP_200_OK)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

