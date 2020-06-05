from symulator.plants.plant import Plant
import random


class Dandelion(Plant):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def set_organizm(self):
        self.name = "dandelion"

    def choose_plant(self):
        child = Dandelion(self.world)
        return child

    def propagate(self):
        for times in range(0, 3):
            propagation_chance = random.randint(0, 100)
            if propagation_chance <= 20:
                self.world.pygame.current_text.append("Dandelion propagates succesfully.")
                child = self.choose_plant()
                child.location.set_nearby_parent(self.location)
                self.born_child(child)

