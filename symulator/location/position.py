from symulator.location.cell import Cell, Directions
import random
random.seed()
SETTER = -1


class Position:

    def __init__(self):
        self.__n = 20
        self.__m = 20
        self._cell = Cell(0, 0)

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, other):
        self._cell.set_cell(other.row, other.column)

    def generate_position(self):
        self._cell.set_cell(random.randint(0, self.n - 1), random.randint(0, self.m - 1))

    @staticmethod
    def check_validity_of_position(position):
        if (position.cell.row >= position.n or position.cell.row < 0 or
                position.cell.column >= position.m or position.cell.column < 0):
            return False
        return True

    @staticmethod
    def check_validity_of_movement(x, border):
        if x >= border or x < 0:
            return False
        return True

    @staticmethod
    def choose_direction():
        return random.randint(Directions.UP, Directions.RIGHT)

    def try_to_move_helper(self, chosen_direction, direction, z, border):
        if chosen_direction == direction and self.check_validity_of_movement(z, border):
            if direction == Directions.UP or direction == Directions.DOWN:
                self._cell.row = z
            else:
                self._cell.column = z
            return True
        return False

    def try_to_move(self, _direction):
        direction = self.choose_direction()
        direction = direction if _direction == SETTER else _direction
        if (self.try_to_move_helper(direction, int(Directions.UP), self.cell.row - 1, self.n)
                or self.try_to_move_helper(direction, int(Directions.DOWN), self.cell.row + 1, self.n)
                or self.try_to_move_helper(direction, int(Directions.LEFT), self.cell.column - 1, self.m)
                or self.try_to_move_helper(direction, int(Directions.RIGHT), self.cell.column + 1, self.m)):
            return True
        else:
            return False

    def move(self, double=False):
        direction = self.choose_direction() if double else SETTER
        while True:
            if self.try_to_move(direction):
                break
            elif double:
                direction = self.choose_direction()
        if double:
            self.try_to_move(direction)

    def move_towards(self, pos):
        x = pos.cell.row
        y = pos.cell.column
        if x != self.cell.row:
            if x > self.cell.row:
                self.try_to_move_helper(Directions.DOWN, Directions.DOWN,
                                        self.cell.row + 1, self.n)
            else:
                self.try_to_move_helper(Directions.UP, Directions.UP,
                                        self.cell.row - 1, self.n)
            return
        elif y != self.cell.column:
            if y > self.cell.column:
                self.try_to_move_helper(Directions.RIGHT, Directions.RIGHT,
                                        self.cell.column + 1, self.m)
            else:
                self.try_to_move_helper(Directions.LEFT, Directions.LEFT,
                                        self.cell.column - 1, self.m)
            return