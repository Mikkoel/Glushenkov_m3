class Warrior:
    health: int
    attack: int
    is_alive: bool


    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 1:
            self.is_alive = False



class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack += 2


def fight(First, Second):
        while First.is_alive and Second.is_alive:
            Second.get_damage(First.attack)
            if Second.is_alive:
                First.get_damage(Second.attack)
        return First.is_alive and (not Second.is_alive)


if __name__ == "__main__":
    chuck = Warrior()
    carl = Knight()
    print(fight(chuck, carl))
