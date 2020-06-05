import os
from symulator.world import World
from symulator.visualization import Pygame
from symulator.saveload import SaveLoad


world = World()
vis = Pygame(world.class_map)
vis.visualize()
vis.print_load_menu()
result = vis.parse_save_load_create_kye()
did_lode = False

if result:
    if (os.path.exists('world_saved.txt')
            and os.path.getsize('world_saved.txt') > 0):
        SaveLoad.load(world)
        did_lode = True
    else:
        world.pygame.current_text.append("World coud not have been loaded.")
        world.pygame.current_text.append("World will be created.")

vis.visualize()
vis.wish_to_create_own_board()
second_result = vis.parse_save_load_create_kye()

if second_result:
    vis.add_organism_menu(world)

if not did_lode and not second_result:
    world.create_the_world()

vis.visualize()

while not world.org_list.check_if_end():
    world.run_the_world()
    vis.visualize()
    world.pygame.print_save_menu()
    if world.pygame.parse_save_load_create_kye():
        SaveLoad.save(world)

world.pygame.current_text.append("Simulation has reached its end.")
world.pygame.parse_statements()
exit(0)
