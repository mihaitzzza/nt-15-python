import pygame
from gui.spaceship import Spaceship
from gui.bullet import Bullet
from utility.colors import PRIMARY
from utility.sizes import WINDOW_WIDTH, WINDOW_HEIGHT
from utility.directions import Directions, Positions


class Game:
    def __init__(self):
        pygame.init()

        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.__screen.fill(PRIMARY)  # (R, G, B) / (R, G, B, A)
        self.__is_running = True
        self.__player_1_spaceship = Spaceship(
            pygame.K_SPACE,
            coord_x=305,
            coord_y=205,
            velocity=1,
            orientation=Positions.down,
            directions={
                pygame.K_w: Directions.move_up,
                pygame.K_s: Directions.move_down,
                pygame.K_a: Directions.move_left,
                pygame.K_d: Directions.move_right,
            })
        self.__player_2_spaceship = Spaceship(
            pygame.K_p,
            coord_x=500,
            coord_y=400,
            velocity=2,
            directions={
                pygame.K_UP: Directions.move_up,
                pygame.K_DOWN: Directions.move_down,
                pygame.K_LEFT: Directions.move_left,
                pygame.K_RIGHT: Directions.move_right,
            })
        self.__spacehip_sprites = pygame.sprite.Group()
        self.__bullet_sprites = pygame.sprite.Group()

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False
                break

            if event.type == pygame.KEYDOWN:
                self.__player_1_spaceship.fire(self.__bullet_sprites, self.__spacehip_sprites)
                self.__player_2_spaceship.fire(self.__bullet_sprites, self.__spacehip_sprites)

        self.__player_1_spaceship.handle_movement()
        self.__player_2_spaceship.handle_movement()

    def __draw(self):
        self.__screen.fill(PRIMARY)
        self.__spacehip_sprites.draw(self.__screen)
        self.__bullet_sprites.draw(self.__screen)
        pygame.display.update()

    def run(self):
        self.__spacehip_sprites.add(self.__player_1_spaceship)
        self.__spacehip_sprites.add(self.__player_2_spaceship)

        while self.__is_running:
            self.__handle_events()
            self.__spacehip_sprites.update()
            self.__bullet_sprites.update()
            self.__draw()
            self.__clock.tick(60)

        pygame.quit()
