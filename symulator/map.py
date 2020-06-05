from symulator.organism.organism import Organism


class Map:
    _map = [[None for r in range(21)] for c in range(21)]
    __n = 20
    __m = 20

    # Map has a constant size of 5x4.

    def print(self):
        print(chr(27) + "[2J")  # clear terminal
        for r in range(21):
            for c in range(21):
                if isinstance(self._map[r][c], Organism):
                    print(self._map[r][c].name[0], end=' ')
                else:
                    print(0, end=' ')
            print()

    def get_organism(self, position):
        if self._map[position.cell.row][position.cell.column] == 0:
            return None
        else:
            return self._map[position.cell.row][position.cell.column]

    def add_organism(self, organism, cell):
        self._map[cell.row][cell.column] = organism

    def remove_organism(self, cell):
        self._map[cell.row][cell.column] = None

    def update_map(self, organism):
        if self.get_organism(organism.location.previous_position) == organism:
            self.remove_organism(organism.location.previous_position.cell)
        if organism.alivness:
            self.add_organism(organism, organism.location.current_position.cell)

    def check_if_field_occupied(self, organism, location):
        row = location.current_position.cell.row
        column = location.current_position.cell.column
        if self._map[row][column] is not None and self._map[row][column] != organism:
            return True
        return False

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    @property
    def map(self):
        return self._map
