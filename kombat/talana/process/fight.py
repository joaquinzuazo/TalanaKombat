from talana.constants.constants import constant_player_data
from talana.entities.player import Player
from talana.process.helpers.helpers import start_play

def fight(movements_and_hits_player1, movements_and_hits_player2):
    player1 = Player(
        constant_player_data['player1']['name'],
        constant_player_data['player1']['special'],
        constant_player_data['player1']['health'],
        movements_and_hits_player1["movimientos"],
        movements_and_hits_player1["golpes"]
    )

    player2 = Player(
        constant_player_data['player2']['name'],
        constant_player_data['player2']['special'],
        constant_player_data['player2']['health'], 
        movements_and_hits_player2["movimientos"],
        movements_and_hits_player2["golpes"]
    )


    if player1 and player2:
        first, second = start_play(player1, player2)
        rondas = max(first.get_len_movements(), second.get_len_movements())