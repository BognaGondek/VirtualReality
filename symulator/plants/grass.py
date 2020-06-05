from symulator.plants.plant import Plant


class Grass(Plant):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def set_organizm(self):
        self.name = "grass"

    def choose_plant(self):
        child = Grass(self.world)
        return child
