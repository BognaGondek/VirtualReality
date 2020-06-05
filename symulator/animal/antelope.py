from symulator.animal.animal import Animal
import random
import copy


class Antelope(Animal):

    def __init__(self, world):
        super().__init__(world)
        self._flight = False
        self.set_organizm()

    @property
    def flight(self):
        return self._flight

    @flight.setter
    def flight(self, value):
        self._flight = value

    def set_organizm(self):
        self.name = "antelope"
        self.strength = 4
        self.initiative = 4

    def choose_animal(self):
        child = Antelope(self.world)
        return child

    def action(self):
        self.location.current_position.move(True)
        x = self.location.current_position.cell.row
        y = self.location.current_position.cell.column
        self.world.pygame.current_text.append("Moves to: " + f'({x}, {y}).')
        super(Animal, self).action()

    def try_to_run_away(self, org):
        escape_chance = random.randint(0, 101)
        if escape_chance <= 50:
            self.world.pygame.current_text.append("Antelope looks for a way to escape.")
            result = self.__look_for_a_safe_place(org)
            return result
        return False

    def __look_for_a_safe_place(self, org):
        field_counter = 0
        can_run_away = False
        temporary_position = copy.deepcopy(self.location.current_position)
        temporary_position_const = copy.deepcopy(self.location.current_position)
        is_init = False
        if self.world.class_map.get_organism(temporary_position) != self:
            is_init = True
        else:
            is_init = False
        while True:
            if field_counter == 8:  # 8 fields around field of particular organism
                break
            self.location.choose_next_field(temporary_position, field_counter)
            if temporary_position.check_validity_of_position(temporary_position):
                if ((self.world.class_map.get_organism(temporary_position) is None)
                        or (is_init and self.world.class_map.get_organism(temporary_position) == self)
                        or (is_init and self.world.class_map.get_organism(temporary_position) == org)):
                    if not self.location.check_for_diagonal(temporary_position_const, temporary_position):
                        can_run_away = True
                        break
            field_counter += 1

        if can_run_away:
            if not is_init:  # specific map situation
                self.flight = True
            self.world.pygame.current_text.append("Antelope successfully runs away.")
            new_x = temporary_position.cell.row
            new_y = temporary_position.cell.column
            self.location.current_position.cell.set_cell(new_x, new_y)
            self.world.class_map.update_map(self)
            self.location.previous_position.cell.set_cell(new_x, new_y)
        else:
            self.world.pygame.current_text.append("Realises there is no way to escape.")

        return can_run_away
