class Player:
    def __init__(self, name, special_shots, health, movements, hits):
        self.name = name
        self.special_shots = special_shots
        self.health = health
        self.movements = movements
        self.hits = hits

    def get_special_shots(self):
        return self.special_shots

    def get_movements(self):
        return self.movements

    def get_len_movements(self):
        return len(self.movements)

    def get_hits(self):
        return self.hits

    def get_combination(self, index):
        return f"{self.movements[index]}+{self.hits[index]}"

    def spear_attack(self, index):
        try:
            hit = self.get_combination(index)
            hits = self.get_special_shots()

            for h in hits:
                movement = ""
                if hit.find(h) == 0:
                    movement = f'{self.name} lanza {hits[hit]["text"]}'
                    return {"movement": movement, "damage": hits[h]["damage"]}
                elif hit.find(h) > 0:
                    movement = f'{self.name} se mueve y lanza {hits[h]["text"]}'
                    return {"movement": movement, "damage": hits[h]["damage"]}
                else:
                    if h:
                        movement = f"{self.name} se mueve"
                    else:
                        continue

            return {"movement": movement, "damage": 0}
        except:
            return {"damage": 0}

    def received_attack(self, damage: int):
        self.health -= damage

    def is_alive(self):
        if self.health > 0:
            return True
        return False
