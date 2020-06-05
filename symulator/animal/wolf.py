from symulator.animal.animal import Animal


class Wolf(Animal):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def outside_effect(self, org):
        self.world.pygame.current_text.append("Wolf attacks " + org.name + ".")
        org.aliveness = False

    def set_organizm(self):
        self.name = "wolf"
        self.strength = 9
        self.initiative = 5

    def choose_animal(self):
        child = Wolf(self.world)
        return child