from symulator.organism.organism import Organism
from abc import ABC, abstractmethod
import random


class Animal(Organism, ABC):

    @abstractmethod
    def set_organizm(self):
        pass

    @abstractmethod
    def choose_animal(self):
        pass

    def static(self):
        return False

    def outside_effect(self, org):
        pass

    def engender(self):
        child = self.choose_animal()
        child.location.set_nearby_parents(self.location)
        self.born_child(child)
        self.location.step_back()

    def action(self):
        self.location.current_position.move()
        x = self.location.current_position.cell.row
        y = self.location.current_position.cell.column
        self.world.pygame.current_text.append("Moves to: " + f'({x}, {y}).')
        super().action()

    @staticmethod
    def defend_itself(self, org):
        return False

    @staticmethod
    def try_to_run_away(self, org):
        return False