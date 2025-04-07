import pygame
from settings import *
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, groups):
        super().__init__(groups)
        self.x = x 
        self.y = y
        self.radius = radius

        self.image = pygame.Surface((2*radius, 2*radius))
        self.image.set_colorkey((0,0,0))
        self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pygame.draw.circle(self.image, self.colour, (radius,radius), radius)

        self.rect = self.image.get_frect(center=(x,y))
        self.x_velocity = 1
        self.y_velocity = 1

    def update(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        if self.rect.right >= SCREEN_WIDTH and self.x_velocity >= 0:
            self.x_velocity *= -1
        if self.rect.left <= 0 and self.x_velocity <= 0:
            self.x_velocity *= -1
        if self.rect.bottom >= SCREEN_HEIGHT and self.y_velocity >= 0:
            self.y_velocity *= -1
        if self.rect.top <= 0 and self.y_velocity <= 0:
            self.y_velocity *= -1
