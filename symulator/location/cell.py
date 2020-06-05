class Directions:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Cell:

    def __init__(self, x=0, y=0):
        self._row = x
        self._column = y

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    @row.setter
    def row(self, x):
        self._row = x

    @column.setter
    def column(self, y):
        self._column = y

    def set_cell(self, x, y):
        self._row = x
        self._column = y

    def __eq__(self, other):
        if self._row == other.row and self._column == other.column:
            return True
        else:
            return False
