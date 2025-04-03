import pygame
from settings import *
import random

class Ball():
    def __init__(self, x, y, radius, x_velocity, y_velocity):
        self.x = x 
        self.y = y
        self.radius = random.randint(30, 100)
        self.x_velocity = random.randint(1, 15)
        self.y_velocity = random.randint(1, 15)
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.move()
        # self.wall_collision()

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
        
