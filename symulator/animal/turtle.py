from symulator.animal.animal import Animal
import random


class Turtle(Animal):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def outside_effect(self, org):
        self.world.pygame.current_text.append("Wolf attacks " + org.name + ".")
        org.aliveness = False

    def set_organizm(self):
        self.name = "turtle"
        self.strength = 2
        self.initiative = 4

    def choose_animal(self):
        child = Turtle(self.world)
        return child

    def action(self):
        chance_to_move = random.randrange(0, 101)
        if chance_to_move <= 25:
            self.location.current_position.move()
            x = self.location.current_position.cell.row
            y = self.location.current_position.cell.column
            self.world.pygame.current_text.append("Moves to: " + f'({x}, {y}).')
        else:
            self.world.pygame.current_text.append("Turtle does not move.")
        super(Animal, self).action()

    @staticmethod
    def defend_itself(self, org):
        max_strength_to_defend = 5
        if org.strength < max_strength_to_defend:
            self.world.pygame.current_text.append("Turtle successfully defends itself.")
            return True
        return False
