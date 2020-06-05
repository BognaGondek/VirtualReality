from symulator.organism.organism import Organism
from symulator.location.location import Directions
import pygame
import math
from pygame.locals import *
from pygame import mixer


class Pygame:

    def __init__(self, world_map):
        pygame.init()

        mixer.init()
        mixer.music.load('theme.mp3')
        pygame.mixer.music.play(-1, 0)

        self.world_visual_details = world_map
        self.__width = 1280
        self.__height = 960
        self._screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption("World Symulator")
        pygame.display.set_icon(pygame.image.load('pictures/world.png'))
        self.__load_pictures()
        self._font = pygame.font.Font('freesansbold.ttf', 16)
        self._statement_min_x = 32
        self._statement_y = 672
        self._counter = 0
        self._current_text = []

    def __load_pictures(self):
        self.pictures = {}
        antelope = pygame.image.load('pictures/antelope.png')
        self.pictures.update({"antelope": antelope})
        blueberry = pygame.image.load('pictures/blueberry.png')
        self.pictures.update({"blueberry": blueberry})
        cyber = pygame.image.load('pictures/cyber.png')
        self.pictures.update({"cyber sheep": cyber})
        dandelion = pygame.image.load('pictures/dandelion.png')
        self.pictures.update({"dandelion": dandelion})
        fox = pygame.image.load('pictures/fox.png')
        self.pictures.update({"fox": fox})
        grass = pygame.image.load('pictures/grass.png')
        self.pictures.update({"grass": grass})
        guarana = pygame.image.load('pictures/guarana.png')
        self.pictures.update({"guarana": guarana})
        player = pygame.image.load('pictures/player.png')
        self.pictures.update({"human": player})
        sheep = pygame.image.load('pictures/sheep.png')
        self.pictures.update({"sheep": sheep})
        turtle = pygame.image.load('pictures/turtle.png')
        self.pictures.update({"turtle": turtle})
        weed = pygame.image.load('pictures/weed.png')
        self.pictures.update({"weed": weed})
        wolf = pygame.image.load('pictures/wolf.png')
        self.pictures.update({"wolf": wolf})
        focus = pygame.image.load('pictures/focus.png')
        self.pictures.update({"focus": focus})
        heart = pygame.image.load('pictures/heart.png')
        self.pictures.update({"heart": heart})

    def __object(self, organism, y, x):
        image = self.pictures[organism.name]
        self._screen.blit(image, (x, y))

    def show_love(self, location):
        y = location.cell.row * 32
        x = location.cell.column * 32
        image = self.pictures["heart"]
        self._screen.blit(image, (x, y))
        pygame.display.update()

    def movement(self, organism, direction):
        y = organism.location.previous_position.cell.row * 32
        x = organism.location.previous_position.cell.column * 32
        for t in range(10):
            self.visualize()
            if direction == Directions.UP:
                y -= 3.2
            if direction == Directions.DOWN:
                y += 3.2
            if direction == Directions.LEFT:
                x -= 3.2
            if direction == Directions.RIGHT:
                x += 3.2
            self.__object(organism, y, x)
            pygame.display.update()
            pygame.time.delay(65)
        organism.location.even_position()

    def visualize(self):
        self._screen.fill((107, 142, 35))
        for r in range(20):
            for c in range(20):
                y = r * 32
                x = c * 32
                if isinstance(self.world_visual_details.map[r][c], Organism):
                    # Attention!
                    # Current positon may be needed in future.
                    self._screen.blit(self.pictures["focus"], (x, y))
                    self.__object(self.world_visual_details.map[r][c], y, x)
                else:
                    self._screen.blit(self.pictures["focus"], (x, y))
        self.print_menu()
        pygame.display.update()

    def print_save_menu(self):
        name_x = 672 + 32
        name_y = 32
        to_be_printed = "Do you wish to save current game? [  up arrow - yes / down arrow - no ]"
        text = self._font.render(to_be_printed, True, (0, 0, 0))
        self._screen.blit(text, (name_y, name_x))
        pygame.display.update()

    @staticmethod
    def parse_save_load_create_kye():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        return False
                    if event.key == pygame.K_UP:
                        return True

    def print_load_menu(self):
        name_x = 672+32
        name_y = 32
        to_be_printed = "Do you wish to load previous game? [ up arrow - yes / down arrow - no ]"
        text = self._font.render(to_be_printed, True, (0, 0, 0))
        self._screen.blit(text, (name_y, name_x))
        pygame.display.update()

    def print_menu(self):
        name_x = 672
        name_y = 32
        text = self._font.render("Bogna Gondek s180244", True, (0, 0, 0))
        self._screen.blit(text, (name_y, name_x))

    @staticmethod
    def wait():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    return

    @property
    def statement_min_x(self):
        return self._statement_min_x

    @property
    def current_text(self):
        return self._current_text

    def __clear_current_text(self):
        self.current_text.clear()

    def __clear_counter(self):
        self._counter = 0

    def __print_statement(self, text):
        x = self._statement_min_x + self._counter*32
        y = self._statement_y
        self._counter += 1
        text = self._font.render(text, True, (0, 0, 0))
        self._screen.blit(text, (y, x))

    def print_statements(self):
        self.current_text.insert(0, "Events...")
        for text in self._current_text:
            self.__print_statement(text)
        self.__clear_counter()
        self.__clear_current_text()
        pygame.display.update()

    @staticmethod
    def parse_player_choice(location):
        special_ability = 7
        error = 404
        keys = pygame.key.get_pressed()
        x = location.current_position.cell.row
        y = location.previous_position.cell.column
        n_m = location.previous_position.n
        if keys[pygame.K_UP]:
            return Directions.UP
        if keys[pygame.K_DOWN]:
            return Directions.DOWN
        if keys[pygame.K_LEFT]:
            return Directions.LEFT
        if keys[pygame.K_RIGHT]:
            return Directions.RIGHT
        if keys[pygame.K_RETURN]:
            return special_ability
        return error

    def wish_to_create_own_board(self):
        name_x = 672 + 32
        name_y = 32
        to_be_printed = "Do you wish to create simulation? [  up arrow - yes / down arrow - no ]"
        text = self._font.render(to_be_printed, True, (0, 0, 0))
        self._screen.blit(text, (name_y, name_x))
        pygame.display.update()

    def parse_statements(self):
        text = "Press any key to continue..."
        self.current_text.append(text)
        self.print_statements()
        self.wait()
        self.visualize()

    def print_create_menu(self):
        name_x = 672 + 32
        name_y = 32
        to_be_printed = "Click enter to end creation. Click with mouse to chooce place for organism."
        text = self._font.render(to_be_printed, True, (0, 0, 0))
        self._screen.blit(text, (name_y, name_x))
        name_x = 672 + 32 + 32
        name_y = 32
        to_be_printed = "Click key to choose organism: w - weed, b - blueberry, p - guarana, "
        text = self._font.render(to_be_printed, True, (0, 0, 0))
        self._screen.blit(text, (name_y, name_x))
        name_x = 672 + 32 + 32 + 32
        name_y = 32
        to_be_printed = "m - dandelion, g - grass, c - cyber sheep, a - antelope, t - turtle,"
        text = self._font.render(to_be_printed, True, (0, 0, 0))
        self._screen.blit(text, (name_y, name_x))
        name_x = 672 + 32 + 32 + 32 + 32
        name_y = 32
        to_be_printed = "f - fox, s - sheep, l - wolf, h - human"
        text = self._font.render(to_be_printed, True, (0, 0, 0))
        self._screen.blit(text, (name_y, name_x))
        pygame.display.update()

    def add_organism_menu(self, world):
        chosen_organism = ""
        player = None
        x, y = 0, 0
        self.visualize()
        self.print_create_menu()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_w:
                        chosen_organism = "weed"
                    if event.key == pygame.K_b:
                        chosen_organism = "blueberry"
                    if event.key == pygame.K_p:
                        chosen_organism = "guarana"
                    if event.key == pygame.K_m:
                        chosen_organism = "dandelion"
                    if event.key == pygame.K_g:
                        chosen_organism = "grass"
                    if event.key == pygame.K_c:
                        chosen_organism = "cyber sheep"
                    if event.key == pygame.K_a:
                        chosen_organism = "antelope"
                    if event.key == pygame.K_t:
                        chosen_organism = "turtle"
                    if event.key == pygame.K_f:
                        chosen_organism = "fox"
                    if event.key == pygame.K_s:
                        chosen_organism = "sheep"
                    if event.key == pygame.K_l:
                        chosen_organism = "wolf"
                    if event.key == pygame.K_h:
                        chosen_organism = "human"
                    if event.key == pygame.K_RETURN:
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = int(math.floor(x/32))
                    y = int(math.floor(y/32))
                    print(x, y)
                    world.add_organism_by_mouse_button(y, x, chosen_organism)