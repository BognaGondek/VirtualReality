from symulator.organism.organism import Organism
from abc import ABC, abstractmethod
import random


class Plant(Organism, ABC):

    @abstractmethod
    def set_organizm(self):
        pass

    @abstractmethod
    def choose_plant(self):
        pass

    def static(self):
        return True

    def outside_effect(self, org):
        pass

    def propagate(self):
        propagation_chance = random.randint(0, 100)
        if propagation_chance <= 20:
            self.world.pygame.current_text.append(self.name + " propagates succesfully.")
            child = self.choose_plant()
            child.location.set_nearby_parent(self.location)
            self.born_child(child)

    def action(self):
        self.propagate()
        super().action()
