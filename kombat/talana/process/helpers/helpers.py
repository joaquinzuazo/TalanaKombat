def attack(self, index):
        try:
            golpe = self.get_combination(index)
            golpes = self.get_special_shots()
            print(golpe)

            for g in golpes:
                movimiento = ''
                if golpe.find(g) == 0:
                    movimiento = f'lanza un {golpes[golpe]["text"]}'
                    print(movimiento)
                    return golpes[g]['damage']
                elif golpe.find(g) > 0:
                    movimiento = f'se movio y lanza un {golpes[g]["text"]}'
                    print(movimiento)
                    return golpes[g]['damage']
                else:
                    if g:
                        movimiento = "se movio"
                    else:
                        print("nada")
                    
            print(movimiento)
            return 0


            # if golpe in golpes:
            #     print(f'{self.name} lanza un {golpes[golpe]["text"]}')
            #     return golpes[golpe]['damage']
            # elif golpe[-1] == 'P' or golpe[-1] == 'K':
            #     print(f'{self.name} conecta {golpes[golpe[-1]]["text"]}')
            #     return golpes[golpe[-1]]['damage']
            # else:
            #     return 0
        except:
            return 0

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