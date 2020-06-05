from symulator.animal.animal import Animal


class Sheep(Animal):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def set_organizm(self):
        self.name = "sheep"
        self.strength = 4
        self.initiative = 4

    def choose_animal(self):
        child = Sheep(self.world)
        return child