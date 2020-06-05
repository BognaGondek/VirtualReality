from symulator.animal.animal import Animal
from symulator.location.cell import Directions
import pygame
import random
import copy


class Human(Animal):

    def __init__(self, world):
        super().__init__(world)
        self._special_ability_duration_current = -5
        self.set_organizm()

    @property
    def special_ability_duration(self):
        return self._special_ability_duration_current

    @special_ability_duration.setter
    def special_ability_duration(self, value):
        self._special_ability_duration = value

    def outside_effect(self, org):
        if self._special_ability_duration_current > 0:
            self.world.pygame.current_text.append("There is only place for one of us.")
            self.world.pygame.current_text.append("*Smokes a fag and throws it on a nearby brushwood.*")
            self.world.pygame.current_text.append("Surrounding organisms are set to fire.")
            self.kill_surrounding_organisms(org, "")

    def set_organizm(self):
        self.name = "human"
        self.strength = 5
        self.initiative = 5

    def choose_animal(self):
        return None

    def __parse_player_choice(self):
        player_choice = self.world.pygame.parse_player_choice(self.location)
        if (player_choice == 404  # error
            or (player_choice == 7 and self._special_ability_duration_current > -5)):
            self.world.pygame.current_text.append("Human was not able to perform given action.")
            return
        if player_choice == 7:  # special ability
            self.world.pygame.current_text.append("Special ability has been activated.")
            self._special_ability_duration_current = 5
            return
        x = self.location.current_position.cell.row
        y = self.location.current_position.cell.column
        n_m = self.location.current_position.n
        self.world.pygame.current_text.append("Human movement action was chosen.")
        if player_choice == Directions.UP:
            self.location.current_position.try_to_move_helper(
                Directions.UP, Directions.UP, x - 1, n_m)
            return
        if player_choice == Directions.DOWN:
            self.location.current_position.try_to_move_helper(
                Directions.DOWN, Directions.DOWN, x + 1, n_m)
            return
        if player_choice == Directions.LEFT:
            self.location.current_position.try_to_move_helper(
                Directions.LEFT, Directions.LEFT, y - 1, n_m)
            return
        if player_choice == Directions.RIGHT:
            self.location.current_position.try_to_move_helper(
                Directions.RIGHT, Directions.RIGHT, y + 1, n_m)
            return

    def __act(self):
        self.world.pygame.current_text.append("Choose direction with arrow keys or special ability with enter.")
        if self._special_ability_duration_current == -5:
            self.world.pygame.current_text.append("Special ability is ready to be used.")
        elif self._special_ability_duration_current > 0:
            self.world.pygame.current_text.append("Special ability active.")
        else:
            self.world.pygame.current_text.append("Special ability still in cooldown.")
            self.world.pygame.current_text.append(f'Wait {(5 + self._special_ability_duration_current)} rounds.')
        text = "Press any key to continue..."
        self.world.pygame.current_text.append(text)
        self.world.pygame.print_statements()
        self.world.pygame.wait()
        self.world.pygame.visualize()
        self.__parse_player_choice()

    def action(self):
        if self._special_ability_duration_current != -5:
            self._special_ability_duration_current -= 1
        self.__act()
        super(Animal, self).action()