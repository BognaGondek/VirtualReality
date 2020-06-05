from symulator.animal.animal import Animal


class Fox(Animal):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def outside_effect(self, org):
        self.world.pygame.current_text.append("Fox attacks " + org.name + ".")
        org.aliveness = False

    def set_organizm(self):
        self.name = "fox"
        self.strength = 3
        self.initiative = 7

    def choose_animal(self):
        child = Fox(self.world)
        return child

    def action(self):
        self.location.current_position.move()
        self.good_smell()
        x = self.location.current_position.cell.row
        y = self.location.current_position.cell.column
        self.world.pygame.current_text.append("Moves to: " + f'({x}, {y}).')
        super(Animal, self).action()

    def good_smell(self):
        smelled = [0 for i in range(0, 4)]
        self.world.pygame.current_text.append("Fox smells his surroundings.")
        while (self.world.class_map.get_organism(self.location.current_position) is not None
               and (self.world.class_map.get_organism(self.location.current_position).strength > self.strength)):
            self.__remember_danger(smelled, self.location)
            self.__prepare_to_smell_again()
            self.location.current_position.move()
            if self.check_if_trapped(smelled):
                self.world.pygame.current_text.append("Fox realised he is trapped.")
                self.__prepare_to_smell_again()
                break

    def __prepare_to_smell_again(self):
        x = self.location.previous_position.cell.row
        y = self.location.previous_position.cell.column
        self.location.current_position.cell.set_cell(x, y)

    def __remember_danger(self, smelled, location):
        c_x = location.current_position.cell.row
        c_y = location.current_position.cell.column
        p_x = location.previous_position.cell.row
        p_y = location.previous_position.cell.column
        if c_x == p_x + 1 or not self.location.current_position.check_validity_of_movement(p_x + 1, self.world.n):
            smelled[0] = 1
        if c_x == p_x - 1 or not self.location.current_position.check_validity_of_movement(p_x - 1, self.world.n):
            smelled[1] = 1
        if c_y == p_y + 1 or not self.location.current_position.check_validity_of_movement(p_y + 1, self.world.m):
            smelled[2] = 1
        if c_y == p_y - 1 or not self.location.current_position.check_validity_of_movement(p_y - 1, self.world.m):
            smelled[3] = 1

    @staticmethod
    def check_if_trapped(smelled):
        for number in smelled:
            if number == 0:
                return False
        return True
