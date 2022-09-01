def start_play(player1, player2):
    movements_p1 = [len(x) for x in player1.get_movements()]
    hits_p1 = [len(x) for x in player1.get_hits()]
    sum_buttons_p1 = sum(movements_p1 + hits_p1)
    movements_p2 = [len(x) for x in player2.get_movements()]
    hits_p2 = [len(x) for x in player2.get_hits()]
    sum_buttons_p2 = sum(movements_p2 + hits_p2)

    start_p1 = (player1, player2)
    start_p2 = (player2, player1)

    start = start_p1 if sum_buttons_p1 < sum_buttons_p2 else start_p2

    if sum_buttons_p1 == sum_buttons_p2:
        start = start_p1 if movements_p1 < movements_p2 else start_p2
        if movements_p1 == movements_p2:
            start = start_p1 if hits_p1 < hits_p2 else start_p2
            if hits_p1 == hits_p2:
                start = start_p1
    return start


def validation_data(payload):
    validation = True
    movements_and_hits_player1 = payload.get("player1")
    movements_and_hits_player2 = payload.get("player2")
    if movements_and_hits_player1 and movements_and_hits_player2:
        for data in payload:
            if "movimientos" in payload[data] and "golpes" in payload[data]:
                if (
                    len(payload[data]["movimientos"]) > 0
                    and len(payload[data]["golpes"]) > 0
                ):
                    continue
                else:
                    validation = False
            else:
                validation = False
    else:
        validation = False
    return validation
