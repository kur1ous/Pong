import pygame, math
from settings import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, up_key, down_key, groups):
        super().__init__(groups)
        self.up_key = up_key
        self.down_key = down_key
        self.points = 0

        self.image = pygame.Surface((20, 100))
        self.image.fill((255,255,255))

        self.rect = self.image.get_frect(center = (x, SCREEN_HEIGHT / 2))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[self.up_key]:
            self.rect.y -= 1

        if keys[self.down_key]:
            self.rect.y += 1

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def give_points(self, num):
        self.points += num