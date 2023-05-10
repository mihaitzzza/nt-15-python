import pygame
from utility.directions import Directions

VELOCITY = 5
HIT_POWER = 20


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, moving_direction, spaceship_sprites, owner):
        super().__init__()

        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.__moving_direction = moving_direction
        self.__spaceship_sprites = spaceship_sprites
        self.__owner = owner

    def update(self, *args, **kwargs) -> None:
        collided_sprites = pygame.sprite.spritecollide(self, self.__spaceship_sprites, False)
        for collided_spaceship in collided_sprites:
            if collided_spaceship != self.__owner:
                collided_spaceship.hit(HIT_POWER)
                self.kill()

        if self.__moving_direction == Directions.move_up:
            self.rect.y -= VELOCITY
        else:
            self.rect.y += VELOCITY
