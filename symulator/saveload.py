from symulator.world import World


class SaveLoad:

    @staticmethod
    def save(world):
        with open("world_saved.txt", "w") as file:
            index = world.org_list.size() - 1
            while index >= 0:
                org = world.org_list.get_organism(index)
                file.write(f'{org.name}, {org.strength}, {org.lifetime}, '
                           f'{org.location.current_position.cell.row}, '
                           f'{org.location.current_position.cell.column}')
                if org.name == "human":
                    file.write(f', {org.special_ability_duration}')
                file.write('\n')
                index -= 1
        world.pygame.current_text.append("World has been succesfully saved.")
        world.pygame.parse_statements()

    @staticmethod
    def load(world):
        with open("world_saved.txt", "r") as file:
            if file.mode == "r":
                line_content = file.readlines()
            for line in line_content:
                information = line.split(sep=",")
                org = world.return_organism(information[0])
                org.strength = int(information[1])
                org.lifetime = int(information[2])
                org.location.current_position.cell.row = int(information[3])
                org.location.current_position.cell.column = int(information[4])
                if org.name == "human":
                    org.special_ability_duration = int(information[5])
                org.born = True
                org.location.even_position()
                world.org_list.push(org)
                world.class_map.update_map(org)
        world.pygame.visualize()
        world.pygame.current_text.append("World has been succesfully loaded.")
        world.pygame.parse_statements()