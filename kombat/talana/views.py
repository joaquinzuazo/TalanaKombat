from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def start_play(player1, player2):
    movements_p1 = [len(x) for x in player1['movimientos']]
    hits_p1 = [len(x) for x in player1['golpes']]
    sum_buttons_p1 = sum(movements_p1 + hits_p1)
    movements_p2 = [len(x) for x in player2['movimientos']]
    hits_p2 = [len(x) for x in player2['golpes']]
    sum_buttons_p2 = sum(movements_p2 + hits_p2)
    
    start = 1 if sum_buttons_p1 < sum_buttons_p2 else 2
    if sum_buttons_p1 == sum_buttons_p2:
        start = 1 if movements_p1 < movements_p2 else 2
        if movements_p1 == movements_p2:
            start = 1 if hits_p1 < hits_p2 else 2
            if hits_p1 == hits_p2:
                start = 1
    return start

@api_view(["GET"])
def combat(request):
    player1 = request.data.get("player1")
    player2 = request.data.get("player2")
    if player1 and player2:
        print(start_play(player1, player2))
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

