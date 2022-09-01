from talana.constants.constants import constant_player_data
from talana.entities.player import Player
from talana.process.helpers.helpers import start_play


def fight(movements_and_hits_player1, movements_and_hits_player2):
    player1 = Player(
        constant_player_data["player1"]["name"],
        constant_player_data["player1"]["special"],
        constant_player_data["player1"]["health"],
        movements_and_hits_player1["movimientos"],
        movements_and_hits_player1["golpes"],
    )

    player2 = Player(
        constant_player_data["player2"]["name"],
        constant_player_data["player2"]["special"],
        constant_player_data["player2"]["health"],
        movements_and_hits_player2["movimientos"],
        movements_and_hits_player2["golpes"],
    )

    if player1 and player2:
        first, second = start_play(player1, player2)
        game_rounds = max(first.get_len_movements(), second.get_len_movements())
        response = {"combat": []}

        for r in range(game_rounds):
            first_mov = first.spear_attack(r)
            if "movement" in first_mov:
                response["combat"].append(first_mov["movement"])
            second.received_attack(first_mov["damage"])
            if not second.is_alive():
                response["combat"].append(
                    f"{first.name} gana la pelea y aun le queda {first.health} puntos de salud"
                )
                return response
            second_mov = second.spear_attack(r)
            if "movement" in second_mov:
                response["combat"].append(second_mov["movement"])
            first.received_attack(second_mov["damage"])
            if not first.is_alive():
                response["combat"].append(
                    f"{second.name} gana la pelea y aun le queda {second.health} puntos de salud"
                )
                return response
        else:
            if first.health > second.health:
                response["combat"].append(
                    f"Terminaron las rondas y {first.name} gana la pelea y aun le queda {first.health} puntos de salud"
                )
                return response
            elif first.health < second.health:
                response["combat"].append(
                    f"Terminaron las rondas y {second.name} gana la pelea y aun le queda {second.health} puntos de salud"
                )
                return response
            else:
                response["combat"].append(
                    f"Terminaron las rondas y hay un empate, al finalizar las rondas ambos tienen {second.health} puntos de salud"
                )
                return response
