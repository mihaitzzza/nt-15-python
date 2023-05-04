import os
import pygame
from utility.directions import Directions
from utility.sizes import WINDOW_HEIGHT, WINDOW_WIDTH

SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.normpath("assets/images/spaceship.png")), (100, 100))


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, coord_x=400, coord_y=300, directions=None):
        super().__init__()

        # Mandatory Sprite attribute (public)
        self.image = SPACESHIP_IMAGE

        # Mandatory Sprite attribute (public)
        self.rect = self.image.get_rect()
        self.rect.center = (coord_x, coord_y)

        # Custom attributes
        self.__directions = directions

    def handle_movement(self):
        if self.__directions:
            key_pressed = pygame.key.get_pressed()
            for move_key, move_direction in self.__directions.items():
                if key_pressed[move_key]:
                    if move_direction == Directions.move_up:
                        if self.rect.y != 0:
                            self.__go_up()
                    if move_direction == Directions.move_down:
                        if self.rect.y != WINDOW_HEIGHT:
                            self.__go_down()
                    if move_direction == Directions.move_left:
                        if self.rect.x != 0:
                            self.__go_left()
                    if move_direction == Directions.move_right:
                        if self.rect.x != WINDOW_WIDTH:
                            self.__go_right()

    def __go_up(self):
        self.rect.y -= 10

    def __go_down(self):
        self.rect.y += 10

    def __go_left(self):
        self.rect.x -= 10

    def __go_right(self):
        self.rect.x += 10
