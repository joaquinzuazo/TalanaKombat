class Player():
    def __init__(self, name, special_shots, life, movements, hits):
        self.name = name
        self.special_shots = special_shots
        self.life = life
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
        return f'{self.movements[index]}+{self.hits[index]}'

    def received_attack(self, damage: int):
        self.life -= damage

    def is_alive(self):
        if self.life > 0:
            return True
        return False