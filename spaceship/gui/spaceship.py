import os
import pygame
from utility.directions import Directions, Positions
from utility.sizes import WINDOW_HEIGHT, WINDOW_WIDTH
from gui.bullet import Bullet


def get_padded_number(index):
    if index < 100:
        return f"0{index}"

    return str(index)

SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.normpath("assets/images/spaceship.png")), (100, 100))
VELOCITY = 10

MOVING_IMAGES = [
    pygame.transform.scale(pygame.image.load(os.path.normpath(f"assets/images/animation/frame_{get_padded_number(i)}_delay-0.04s.png")), (100, 100))
    for i in range(25, 122)
]


class Spaceship(pygame.sprite.Sprite):
    def __init__(
        self,
        fire_key,
        coord_x=400,
        coord_y=300,
        directions=None,
        velocity=VELOCITY,
        orientation=Positions.up,
    ):
        super().__init__()

        # Mandatory Sprite attribute (public)
        if orientation == Positions.up:
            self.image = SPACESHIP_IMAGE
        else:
            self.image = pygame.transform.rotate(SPACESHIP_IMAGE, 180)

        # Mandatory Sprite attribute (public)
        self.rect = self.image.get_rect()
        self.rect.center = (coord_x, coord_y)

        # Custom attributes
        self.__directions = directions
        self.__velocity = velocity
        self.__hp = 100
        self.__fire_key = fire_key
        self.__orientation = orientation
        self.__last_fire_count = 0
        self.__image_index = 0
        self.__is_moving = False

    def hit(self, power=10):
        self.__hp -= power

    def fire(self, bullet_sprites, spaceship_sprites):
        if self.__last_fire_count == 0 and self.__hp > 0:
            key_pressed = pygame.key.get_pressed()

            if key_pressed[self.__fire_key]:
                self.__last_fire_count = 1

                bullet_x = self.rect.x + self.image.get_width() / 2

                if self.__orientation == Positions.up:
                    bullet_y = self.rect.y
                else:
                    bullet_y = self.rect.y + self.image.get_height()

                bullet_move_direction = Directions.move_up if self.__orientation == Positions.up else Directions.move_down

                bullet = Bullet(bullet_x, bullet_y, bullet_move_direction, spaceship_sprites, self)
                bullet_sprites.add(bullet)

    def handle_movement(self):
        self.__is_moving = False

        if self.__directions:
            key_pressed = pygame.key.get_pressed()
            for move_key, move_direction in self.__directions.items():
                if key_pressed[move_key]:
                    if move_direction == Directions.move_up:
                        self.__go_up()
                    if move_direction == Directions.move_down:
                        self.__go_down()
                    if move_direction == Directions.move_left:
                        self.__go_left()
                    if move_direction == Directions.move_right:
                        self.__go_right()

    def __go_up(self):
        self.__is_moving = True
        if self.rect.y - self.__velocity >= 0:
            self.rect.y -= self.__velocity
        else:
            self.rect.y = 0

    def __go_down(self):
        self.__is_moving = True
        if self.rect.y + self.image.get_height() <= WINDOW_HEIGHT - self.__velocity:
            self.rect.y += self.__velocity
        else:
            self.rect.y = WINDOW_HEIGHT - self.image.get_height()

    def __go_left(self):
        self.__is_moving = True
        if self.rect.x - self.__velocity >= 0:
            self.rect.x -= self.__velocity
        else:
            self.rect.x = 0

    def __go_right(self):
        self.__is_moving = True
        if self.rect.x + self.image.get_width() <= WINDOW_WIDTH - self.__velocity:
            self.rect.x += self.__velocity
        else:
            self.rect.x = WINDOW_WIDTH - self.image.get_width()

    def update(self, *args, **kwargs) -> None:
        if self.__last_fire_count >= 60:
            self.__last_fire_count = 0
        elif self.__last_fire_count >= 1:
            self.__last_fire_count += 1

        if self.__hp <= 0:
            self.kill()

        if self.__is_moving:
            if self.__image_index >= len(MOVING_IMAGES):
                self.__image_index = 0
            if self.__orientation == Positions.up:
                self.image = MOVING_IMAGES[self.__image_index]
            else:
                self.image = pygame.transform.rotate(MOVING_IMAGES[self.__image_index], 180)
            self.__image_index += 1
        else:
            if self.__orientation == Positions.up:
                self.image = SPACESHIP_IMAGE
            else:
                self.image = pygame.transform.rotate(SPACESHIP_IMAGE, 180)
