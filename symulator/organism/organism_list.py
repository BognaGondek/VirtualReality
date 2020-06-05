class OrganismList:

    def __init__(self):
        self._organism = []

    @staticmethod
    def return_preferred(left_org, right_org):
        if (left_org.initiative > right_org.initiative
                or (left_org.initiative == right_org.initiative
                    and left_org.lifetime > right_org.lifetime)):
            return left_org
        return right_org

    def __determine_pisiton_in_list(self, new_org):
        index = len(self._organism) - 1
        while (index in range(0, len(self._organism))
               and new_org.initiative > self._organism[index].initiative):
            index -= 1
        if (index in range(0, len(self._organism))
                and new_org.initiative == self._organism[index].initiative):
            while (index in range(0, len(self._organism))
                   and new_org.lifetime > self._organism[index].lifetime):
                index -= 1
        return index  # return index of more active or/and older animal

    def __push_under_priority(self, new_org):
        border_index = self.__determine_pisiton_in_list(new_org)
        self._organism.insert(border_index + 1, new_org)

    def push(self, new_org):
        if len(self._organism) == 0:
            self._organism.append(new_org)
        elif len(self._organism) == 1:
            if new_org != self.return_preferred(self._organism[0], new_org):
                self._organism.insert(1, new_org)
            else:
                self._organism.insert(0, new_org)
        else:
            self.__push_under_priority(new_org)

    def pop(self, index):
        self._organism.pop(index)

    def check_if_end(self):
        if len(self._organism) == 0 or len(self._organism) == 1:
            return True
        else:
            counter = 1
            previous_name = self._organism[0].name
            while counter in range(0, len(self._organism)):
                if self._organism[counter].name != previous_name:
                    return False
                counter += 1
        return True

    def get_organism(self, index):
        return self._organism[index]

    def size(self):
        return len(self._organism)

    def print(self):
        print("All organisms rounds end.")
        for index in range(0, self.size()):
            print(self._organism[index].name, self._organism[index].initiative,
                  self._organism[index].lifetime, self._organism[index].strength,
                  self._organism[index].alivness, end=" ")
            self._organism[index].location.print_position_change()
            print()