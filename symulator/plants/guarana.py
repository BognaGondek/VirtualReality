from symulator.plants.plant import Plant


class Guarana(Plant):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def set_organizm(self):
        self.name = "guarana"

    def choose_plant(self):
        child = Guarana(self.world)
        return child

    def outside_effect(self, org):
        guarana_boost = 3
        self.world.pygame.current_text.append("Guarana strengthens " + org.name + ".")
        org.strength = org.strength + guarana_boost
