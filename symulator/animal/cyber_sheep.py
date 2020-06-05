from symulator.animal.animal import Animal
import math


class CyberSheep(Animal):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def set_organizm(self):
        self.name = "cyber sheep"
        self.strength = 11
        self.initiative = 4

    def choose_animal(self):
        child = CyberSheep(self.world)
        return child

    def choose_closest_weed(self):
        p_index = len(self.world.weed) - 1
        index = len(self.world.weed) - 1
        cyber_x = self.location.current_position.cell.row
        cyber_y = self.location.current_position.cell.column
        result = 0
        final_distance = 100
        to_be_deleted = []

        while index >= 0:
            if p_index != len(self.world.weed) - 1:
                p_index = len(self.world.weed) - 1
                index = len(self.world.weed) - 1
            if not self.world.weed[index].alivness:
                self.world.weed.pop(index)
            index -= 1
        index = len(self.world.weed) - 1
        while index >= 0:
            x = self.world.weed[index].location.current_position.cell.row
            y = self.world.weed[index].location.current_position.cell.column
            distance = abs(x - cyber_x) + abs(y - cyber_y)
            if not (final_distance < distance):
                final_distance = distance
            if final_distance == distance:
                result = index
            print(self.world.weed[index], distance, result, end=" ")
            self.world.weed[index].location.print_position_change()
            index -= 1
        print(result)
        return result

    def action(self):
        index = self.choose_closest_weed()
        if len(self.world.weed) != 0:
            self.location.current_position.move_towards(self.world.weed[index].location.current_position)
        else:
            self.location.current_position.move()
            x = self.location.current_position.cell.row
            y = self.location.current_position.cell.column
            self.world.pygame.current_text.append("Moves to: " + f'({x}, {y}).')
        super(Animal, self).action()