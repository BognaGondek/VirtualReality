from symulator.map import Map
from symulator.organism.organism_list import OrganismList
from symulator.visualization import Pygame
from symulator.animal.antelope import Antelope
from symulator.animal.fox import Fox
from symulator.animal.human import Human
from symulator.animal.sheep import Sheep
from symulator.animal.turtle import Turtle
from symulator.animal.wolf import Wolf
from symulator.animal.cyber_sheep import CyberSheep
from symulator.plants.blueberry import Blueberry
from symulator.plants.dandelion import Dandelion
from symulator.plants.grass import Grass
from symulator.plants.guarana import Guarana
from symulator.plants.weed import Weed


class World:

    def __init__(self):
        self._class_map = Map()
        self._all_org = OrganismList()
        self.__n = 20
        self.__m = 20
        self.weed = []
        self._pygame = Pygame(self.class_map)
        self._player = None

    @property
    def pygame(self):
        return self._pygame

    @property
    def class_map(self):
        return self._class_map

    @property
    def org_list(self):
        return self._all_org

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    def add_organism(self, org):
        self._all_org.push(org)

    def clear_org_list(self):
        for index in range(0, self._all_org.size()):
            if index < self._all_org.size() and not self._all_org.get_organism(index).alivness:
                self._all_org.pop(index)

    def run_the_world(self):
        for index in range(0, self._all_org.size()):
            if self._all_org.get_organism(index).alivness:
                organism = self._all_org.get_organism(index)
                self.pygame.current_text.append("It's " + organism.name + " tour.")
                x = organism.location.current_position.cell.row
                y = organism.location.current_position.cell.column
                self.pygame.current_text.append("Current position: " + f'({x}, {y}).')
                organism.action()
                self.pygame.parse_statements()
        self.clear_org_list()
        self.org_list.print()

    def add_weed(self, org):
        self.weed.append(org)

    def prepare_organism_to_settle(self, org):
        org.born = True
        while self.class_map.check_if_field_occupied(org, org.location):
            org.location.set_randomly()
        org.location.even_position()
        self.org_list.push(org)
        self.class_map.update_map(org)

    def return_organism(self, counter):
        if counter in range(0, 3) or counter == "dandelion":
            return Dandelion(self)
        elif counter in range(3, 6) or counter == "grass":
            return Grass(self)
        elif counter in range(6, 9) or counter == "guarana":
            return Guarana(self)
        elif counter in range(9, 10) or counter == "blueberry":
            return Blueberry(self)
        elif counter in range(10, 13) or counter == "weed":
            return Weed(self)
        elif counter in range(13, 15) or counter == "cyber sheep":
            return CyberSheep(self)
        elif counter in range(15, 18) or counter == "wolf":
            return Wolf(self)
        elif counter in range(18, 21) or counter == "antelope":
            return Antelope(self)
        elif counter in range(21, 24) or counter == "fox":
            return Fox(self)
        elif counter in range(24, 27) or counter == "sheep":
            return Sheep(self)
        elif counter in range(27, 30) or counter == "turtle":
            return Turtle(self)
        elif counter in range(30, 31) or counter == "human":
            return Human(self)

    def create_the_world(self):
        organism_counter = 0
        out_side_counter = 2
        while out_side_counter != 0:
            while organism_counter != 30:
                organism = self.return_organism(organism_counter)
                self.prepare_organism_to_settle(organism)
                organism_counter += 1
            organism_counter = 0
            out_side_counter -= 1
        player = self.return_organism(30)  # Human number.
        self.prepare_organism_to_settle(player)
        self.pygame.current_text.append("World has been successfully generated.")
        self.pygame.visualize()
        self.pygame.parse_statements()

    def add_organism_by_mouse_button(self, x, y, org):
        if org == "":
            return
        if self.player is not None and org == "human":
            self.player.alivness = False
            self.class_map.update_map(self.player)
            self.clear_org_list()
        organism = self.return_organism(org)
        organism.location.current_position.cell.set_cell(x, y)
        if not organism.location.current_position.check_validity_of_position(organism.location.current_position):
            return
        if organism.name == "human":
            self.player = organism
        organism.born = True
        organism.location.even_position()
        self.org_list.push(organism)
        if self.class_map.check_if_field_occupied(organism, organism.location):
            self.class_map.get_organism(organism.location.current_position).alivness = False
            self.clear_org_list()
        self.class_map.update_map(organism)
        self.pygame.visualize()
        self.pygame.print_create_menu()