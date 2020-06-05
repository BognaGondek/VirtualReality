from symulator.location.position import Position, Directions


class Location:

    def __init__(self):
        self._previous_position = Position()
        self._current_positon = Position()
        self._direction = None

    def set_randomly(self):
        self._previous_position.generate_position()
        x = self._previous_position.cell.row
        y = self._previous_position.cell.column
        self._current_positon.cell.set_cell(x, y)

    def even_position(self):
        x = self._current_positon.cell.row
        y = self._current_positon.cell.column
        self._previous_position.cell.set_cell(x, y)

    def print_position_change(self):
        print(f'({self._previous_position.cell.row}, {self._previous_position.cell.column})->', end='')
        print(f'({self._current_positon.cell.row}, {self._current_positon.cell.column})')

    def set_nearby_parent(self, parent_position):
        x = parent_position.current_position.cell.row
        y = parent_position.current_position.cell.column
        self._current_positon.cell.set_cell(x, y)
        self._current_positon.move()
        # self.even_position()
        self._previous_position.cell.set_cell(x, y)

    def set_nearby_parents(self, mother_position):
        self.set_nearby_parent(mother_position)
        x = mother_position.previous_position.cell.row
        y = mother_position.previous_position.cell.column
        self._current_positon.cell.set_cell(x, y)
        while self._current_positon.cell == mother_position.previous_position.cell:
            self.set_nearby_parent(mother_position)

    def step_back(self):
        x = self._previous_position.cell.row
        y = self._previous_position.cell.column
        self._current_positon.cell.set_cell(x, y)

    @property
    def previous_position(self):
        return self._previous_position

    @property
    def current_position(self):
        return self._current_positon

    @property
    def moved(self):
        return self.moved

    @property
    def direction(self):
        self.__update_direction()
        return self._direction

    # This choose_next_field() function goes as follows:
    #    [3][4][5]
    #    [2][X][6] - X is an initial position
    #    [1][0][7]
    # Used for human special ability and hogweeed intoxication.

    # Fuction choose_next_field(position, counter)
    # does not check border.
    @staticmethod
    def choose_next_field(position, counter):
        x = position.cell.row
        y = position.cell.column
        if counter == 0 or counter == 6 or counter == 7:
            return position.cell.set_cell(x + 1, y)
        elif counter == 1:
            return position.cell.set_cell(x, y - 1)
        elif counter == 2 or counter == 3:
            return position.cell.set_cell(x - 1, y)
        elif counter == 4 or counter == 5:
            return position.cell.set_cell(x, y + 1)

    @staticmethod
    def check_for_diagonal(previous_position, current_position):
        if ((previous_position.cell.row == current_position.cell.row - 1
             and previous_position.cell.column == current_position.cell.column - 1)
            or (previous_position.cell.row == current_position.cell.row - 1
                and previous_position.cell.column == current_position.cell.column + 1)
            or (previous_position.cell.row == current_position.cell.row + 1
                and previous_position.cell.column == current_position.cell.column - 1)
            or (previous_position.cell.row == current_position.cell.row + 1
                and previous_position.cell.column == current_position.cell.column + 1)):
            return True
        return False

    @previous_position.setter
    def previous_position(self, other):
        x = other.cell.row
        y = other.cell.column
        self._previous_position.cell.set_cell(x, y)

    @current_position.setter
    def current_position(self, other):
        x = other.cell.row
        y = other.cell.column
        self.current_position.cell.set_cell(x, y)

    @moved.setter
    def moved(self, value):
        self.moved = value

    @staticmethod
    def _up(px, cx):
        if cx == px - 1:
            return True
        return False

    @staticmethod
    def _down(px, cx):
        if cx == px + 1:
            return True
        return False

    @staticmethod
    def _left(py, cy):
        if cy == py - 1:
            return True
        return False

    @staticmethod
    def _right(py, cy):
        if cy == py + 1:
            return True
        return False

    def __update_direction(self):
        p_x = self.previous_position.cell.row
        p_y = self.previous_position.cell.column
        c_x = self.current_position.cell.row
        c_y = self.current_position.cell.column
        if self._up(p_x, c_x):
            self._direction = Directions.UP
        elif self._down(p_x, c_x):
            self._direction = Directions.DOWN
        elif self._left(p_y, c_y):
            self._direction = Directions.LEFT
        elif self._right(p_y, c_y):
            self._direction = Directions.RIGHT
