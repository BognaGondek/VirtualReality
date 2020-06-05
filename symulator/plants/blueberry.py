from symulator.plants.plant import Plant


class Blueberry(Plant):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def set_organizm(self):
        self.name = "blueberry"
        self.strength = 99

    def choose_plant(self):
        child = Blueberry(self.world)
        return child

    def outside_effect(self, org):
        self.world.pygame.current_text.append("Blueberry intoxicates " + org.name)
        org.alivness = False
