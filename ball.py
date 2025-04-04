import pygame
from settings import *
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, x_velocity, y_velocity, groups):
        super().__init__(groups)
        self.x = x 
        self.y = y
        self.radius = radius
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        self.image = pygame.Surface((2*radius, 2*radius))



    def draw(self):
        pygame.draw.circle(screen,(self.colour), (self.x, self.y), self.radius)


    def move(self):
        self.x = self.x+self.x_velocity
        self.y = self.y+self.y_velocity

    def wall_collision(self):
        if self.x >= SCREEN_WIDTH-self.radius:
            self.x_velocity *= -1
        if self.x <= 0+self.radius:
            self.x_velocity *= -1
        if self.y >= SCREEN_HEIGHT-self.radius:
            self.y_velocity *= -1
        if self.y <= 0+self.radius:
            self.y_velocity *= -1
        
