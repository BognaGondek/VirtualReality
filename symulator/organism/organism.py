from abc import ABC, abstractmethod
from symulator.location.location import Location
import copy


class OrganismsName:
    GRASS = 0
    MILT = 1
    PAULINA_GUARANA = 2
    BLUEBERRY = 3
    SOSNOWSKYS_HOGWEED = 4
    ANTELOPE = 5
    FOX = 6
    SHEEP = 7
    TURTLE = 8
    LUPUS = 9
    HUMAN = 10


class Organism(ABC):

    def __init__(self, world):
        self._name = ""
        self._strength = 0
        self._initiative = 0
        self._lifetime = 0
        self._alivness = True
        self._born = False
        self._location = Location()
        self._world = world
        # commentator

    @abstractmethod
    def outside_effect(self, org):
        pass

    @abstractmethod
    def static(self):
        pass

    @abstractmethod
    def set_organizm(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength

    @property
    def initiative(self):
        return self._initiative

    @property
    def lifetime(self):
        return self._lifetime

    @property
    def alivness(self):
        return self._alivness

    @property
    def born(self):
        return self._born

    @property
    def location(self):
        return self._location

    @property
    def world(self):
        return self._world

    @world.setter
    def world(self, value):
        self._world = value

    @location.setter
    def location(self, value):
        self._location = value

    @born.setter
    def born(self, value):
        self._born = value

    @alivness.setter
    def alivness(self, value):
        self._alivness = value

    @lifetime.setter
    def lifetime(self, value):
        self._lifetime = value

    @initiative.setter
    def initiative(self, value):
        self._initiative = value

    @strength.setter
    def strength(self, value):
        self._strength = value

    @name.setter
    def name(self, value):
        self._name = value

    @staticmethod
    def check_if_stronger(init, best):
        if best.strength <= init.strength:
            return True
        return False

    def did_collide(self):
        return self.world.class_map.check_if_field_occupied(self, self.location)

    def die(self):
        if self.world.class_map.get_organism(self.location.previous_position) == self:
            self.world.class_map.update_map(self)

    def get_rival(self):
        return self.world.class_map.map.get_organism(self.location.current_position)

    def parse_collision(self, org):
        if not org.alivness:
            org.die()
            self.world.pygame.current_text.append(org.name.capitalize() + " has died.")
        else:
            self.world.pygame.current_text.append(org.name.capitalize() + " has survived.")
            self.location.print_position_change()
            org.world.class_map.update_map(self)

    def plant_collision(self, init, best):
        if self.check_if_stronger(init, best):
            best.alivness = False
        else:
            init.alivness = False

    @staticmethod
    def run_away_helper(init, best):
        if init.name == "antelope":
            return init.try_to_run_away(best)

    def animal_plant_colission(self, init, best):
        if self.run_away_helper(init, best) or self.run_away_helper(best, init):
            return
        if init.static() is True:
            init.outside_effect(best)
            if init.strength < best.strength:
                self.world.pygame.current_text.append(init.name.capitalize() + " gets eaten by " + best.name + ".")
                init.alivness = False
        else:
            best.outside_effect(init)
            if init.strength >= best.strength:
                self.world.pygame.current_text.append(best.name.capitalize() + " gets eaten by " + init.name + ".")
                best.alivness = False

    def animal_collision(self, init, best):
        if self.run_away_helper(init, best) or self.run_away_helper(best, init):
            return
        if init.name == best.name and init.born:
            self.world.pygame.show_love(best.location.current_position)
            self.world.pygame.show_love(init.location.previous_position)
            self.world.pygame.parse_statements()
            init.engender()
        elif self.check_if_stronger(init, best):
            if best.defend_itself(self, init):
                if not init.born:
                    init.alivness = False
                    self.world.pygame.current_text.append(init.name.capitalize() +
                                                          " is to weak to find another place to live.")
                else:
                    init.location.step_back()
                    self.world.pygame.current_text.append(init.name.capitalize() + " has to step back.")
            else:
                best.alivness = False
        else:
            init.alivness = False

    def collision(self):
        rival = self.world.class_map.get_organism(self.location.current_position)
        self.world.pygame.current_text.append(self.name.capitalize() + " has come into collision with " + rival.name + ".")

        # Parse player special ability.
        if self.name == "human":
            self.outside_effect(None)
        elif rival.name == "human":
            rival.outside_effect(self)

        if self.static() and rival.static():
            self.plant_collision(self, rival)
        elif not self.static() and not rival.static():
            self.animal_collision(self, rival)
            pass
        else:
            self.animal_plant_colission(self, rival)

        self.parse_collision(self)
        self.parse_collision(rival)
        self.world.pygame.visualize()

        if rival.name == "antelope":
            if rival.flight:
                rival.flight = False
                self.world.class_map.add_organism(rival, rival.location.current_position.cell)
                self.world.pygame.visualize()

    def action(self):
        if self.did_collide():
            self.collision()
        else:
            self.world.class_map.update_map(self)
        self.lifetime = self.lifetime + 1
        self.location.even_position()

    def born_child(self, child):
        self.world.pygame.current_text.append(child.name.capitalize() + " baby has appeard.")
        self.world.pygame.movement(child, child.location.direction)
        if child.did_collide():
            child.collision()
        if child.alivness:
            self.world.pygame.current_text.append(child.name.capitalize() + " baby has been born.")
            child.born = True
            self.world.org_list.push(child)
            self.world.org_list.print()
            child.location.even_position()
            self.world.class_map.update_map(child)
            self.world.pygame.visualize()

    def kill_surrounding_organisms(self, survivor=None, name=""):
        position_around = copy.deepcopy(self.location.current_position)
        counter = 8
        field_counter = 0
        while counter != 0:
            self.location.choose_next_field(position_around, field_counter)
            field_counter += 1
            counter -= 1
            self.__kill_neighbour(self, survivor, position_around, name)
        self.world.pygame.visualize()

    def __kill_neighbour(self, org, surv, pos, name):
        rival = self.world.class_map.get_organism(pos)
        if rival is None:
            return
        if self.location.current_position.check_validity_of_position(pos):
            if ((rival.static() is False) and (self.static() is True)) or self.static() is False:
                print(rival.name)
                print(name)
                if rival != org and rival != surv and rival.name != name:
                    self.world.pygame.current_text.append(rival.name.capitalize() + " has died.")
                    rival.alivness = False
                    print(rival.alivness)
                    rival.location.print_position_change()
                    self.world.class_map.update_map(rival)
