import pygame
from gui.spaceship import Spaceship
from utility.colors import PRIMARY
from utility.sizes import WINDOW_WIDTH, WINDOW_HEIGHT
from utility.directions import Directions


class Game:
    def __init__(self):
        pygame.init()

        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.__screen.fill(PRIMARY)  # (R, G, B) / (R, G, B, A)
        self.__is_running = True
        self.__player_1_spaceship = Spaceship(305, 205, directions={
            pygame.K_w: Directions.move_up,
            pygame.K_s: Directions.move_down,
            pygame.K_a: Directions.move_left,
            pygame.K_d: Directions.move_right,
        })
        self.__player_2_spaceship = Spaceship(500, 400, directions={
            pygame.K_UP: Directions.move_up,
            pygame.K_DOWN: Directions.move_down,
            pygame.K_LEFT: Directions.move_left,
            pygame.K_RIGHT: Directions.move_right,
        })
        self.__sprites = pygame.sprite.Group()

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False
                break

        self.__player_1_spaceship.handle_movement()
        self.__player_2_spaceship.handle_movement()

    def __draw(self):
        self.__screen.fill(PRIMARY)
        self.__sprites.draw(self.__screen)
        pygame.display.update()

    def run(self):
        self.__sprites.add(self.__player_1_spaceship)
        self.__sprites.add(self.__player_2_spaceship)

        while self.__is_running:
            self.__handle_events()
            self.__draw()
            self.__clock.tick(60)

        pygame.quit()
